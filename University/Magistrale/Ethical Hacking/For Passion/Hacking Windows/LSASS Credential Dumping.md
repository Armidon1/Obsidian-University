# LSASS Credential Dumping

> [!abstract] Di cosa parla 
> Come si estraggono le credenziali dalla memoria del processo `lsass.exe`, la fonte principale per pass-the-hash e pass-the-ticket. È il "dump dalla RAM" del passo 2 della slide su Pass-the-Hash. La nota copre le tre fonti di credenziali (SAM / LSASS / LSA Secrets), come si dumpa LSASS in pratica, i tool moderni e la contromisura strutturale (Credential Guard). Precondizione ricorrente: è tutta roba _post-escalation_, serve admin locale / SYSTEM — non è un modo per entrare, è ciò che si fa una volta dentro.

---

## Tre fonti, non confonderle

> [!info] SAM vs LSASS vs LSA Secrets 
> Sono tre depositi diversi, spesso impacchettati insieme a sproposito. **SAM**: database degli account _locali_ su registro/disco (`HKLM\SAM`), contiene gli hash NT degli utenti locali. **LSASS**: il _processo in RAM_ (`lsass.exe`), dove stanno hash e ticket degli utenti _attualmente loggati_ — è la fonte del pass-the-hash. **LSA Secrets**: ramo di registro (`HKLM\SECURITY\Policy\Secrets`) con segreti _persistenti_ (password di service account, scheduled task, account computer). La domanda che smista: cerco un account locale (→ SAM), le credenziali di chi è loggato adesso (→ LSASS), o segreti di servizio persistenti (→ LSA Secrets)?

|Fonte|Dove vive|Cosa contiene|Serve per|
|---|---|---|---|
|SAM|registro / disco|hash NT utenti **locali**|PtH con account locale|
|LSASS|RAM (`lsass.exe`)|hash NT + **ticket Kerberos** dei loggati|**PtH / PtT**|
|LSA Secrets|registro|password service account, task, computer|movimento laterale, escalation|

---

## Perché LSASS è la miniera

> [!info] Cosa tiene in memoria 
> LSASS è il processo che gestisce l'autenticazione: mentre un utente è loggato, tiene in RAM il materiale che gli serve per autenticarsi ai servizi senza richiedere di nuovo la password (single sign-on). Contiene quindi gli **hash NT** degli utenti loggati, i loro **ticket Kerberos** (TGT e service ticket), e — su sistemi vecchi o malconfigurati — perfino password in **chiaro** via WDigest. È esattamente il "le password sono cifrate, ma le chiavi stanno in RAM" della slide: LSASS è dove si va a prendere le chiavi.

> [!warning] WDigest Provider di autenticazione legacy che teneva la password in **chiaro** in memoria per il SSO HTTP. Attivo di default fino a Windows 7 / Server 2008 R2; disabilitabile (e disabilitato di default dopo) via `UseLogonCredential=0`. Se attivo, il dump di LSASS restituisce direttamente le password in chiaro, senza nemmeno craccare. Solito pattern del capitolo: retrocompatibilità = buco.

---

## Come si dumpa in pratica

> [!info] Due strategie 
> **Diretta**: un tool legge la memoria di `lsass.exe` sul posto ed estrae le credenziali (richiede SeDebugPrivilege / SYSTEM). **Indiretta (dump & parse)**: prima si crea un file di dump del processo, poi lo si analizza _offline_ su un'altra macchina — utile per evitare di eseguire tool "sporchi" sul target. Il dump si può fare con `procdump` (SysInternals, firmato Microsoft, meno sospetto), con Task Manager (`Crea file di dump`), o via API `MiniDumpWriteDump`.

```text
# Dump indiretto con procdump, poi parsing offline con mimikatz
procdump.exe -accepteula -ma lsass.exe lsass.dmp
mimikatz # sekurlsa::minidump lsass.dmp
mimikatz # sekurlsa::logonpasswords
```

> [!info] Mimikatz — lo standard 
> Il tool di riferimento (successore di WCE, che la slide cita). Comandi chiave: `sekurlsa::logonpasswords` (hash e password dalla RAM), `sekurlsa::tickets` (ticket Kerberos per pass-the-ticket), `lsadump::sam` (hash dal SAM locale), `lsadump::secrets` (LSA Secrets). WCE resta il predecessore storico per lo stesso scopo.

> [!info] Impacket — da remoto 
> Su Linux / in scenari remoti, `secretsdump.py` di Impacket estrae in un colpo SAM + LSA Secrets + cache di dominio da una macchina target, dati credenziali admin. È il flusso tipico su HTB, che non tocca la RAM di LSASS direttamente ma sfrutta l'accesso remoto al registro / via DRSUAPI sul DC.

```bash
secretsdump.py DOMINIO/administrator:password@<IP-target>
```

> [!tip] Cosa esce e come si riusa 
> Dal dump escono **hash NT** → si riusano con pass-the-hash (`psexec.py -hashes ...`, `wmiexec`, `netexec`), e **ticket Kerberos** → si riusano con pass-the-ticket. Nessun cracking: l'hash _è_ la credenziale. Il DC compromesso via `secretsdump` (dump di `ntds.dit`) dà invece **tutti** gli hash del dominio in un colpo.

---

## Contromisure

> [!warning] Difese moderne 
> La slide dice "non c'è patch": vero all'epoca di WCE, ma oggi esistono mitigazioni strutturali. **Credential Guard** isola LSASS in un ambiente virtualizzato (VBS/Secure Kernel) così la sua memoria non è più leggibile → uccide il dump classico e con esso PtH/PtT. **LSA Protection** (`RunAsPPL`) marca LSASS come _protected process_, alzando la barriera al dump. **Disabilitare WDigest** toglie le password in chiaro dalla RAM. A monte, il solito principio: non far ottenere all'attaccante SYSTEM sulla macchina (least privilege, EDR), e **non far loggare account privilegiati** (Domain Admin) su host a rischio — perché ciò che non è in RAM non si dumpa.

> [!info] Il limite intrinseco Il dumping è sempre _post-escalation_: richiede già admin locale / SYSTEM. Non è un vettore d'ingresso, è ciò che amplifica una compromissione già avvenuta trasformandola in movimento laterale. Per questo la difesa vera è a monte (prevenire l'intrusione e l'escalation), non "patchare il dump".

---

## Fili rossi

> [!tip] Come si lega al resto **Hash NT = credenziale**: stesso concetto della nota NTLM e di Pass-the-Hash — dall'LSASS esce l'hash NT che si riusa senza craccare. **Ticket in RAM**: i ticket Kerberos dumpati da LSASS sono il materiale del pass-the-ticket, cugino del PtH visto nel flusso Kerberos. **Le tre fonti** riecheggiano i "tre depositi di credenziali" già distinti nel Cap. 4 (SAM / LSA Secrets / cache di dominio). **Retrocompatibilità = buco**: WDigest è l'ennesimo caso.

---

## Punti aperti

> [!question] Da verificare Quanto l'esame entra nel dettaglio dei comandi mimikatz/secretsdump rispetto al solo concetto delle tre fonti. Da confermare se il corso tratta Credential Guard / LSA Protection o si ferma al "non c'è patch" della slide. Resta da fare la nota Kerberos completa (flusso AS/TGS + PtT nel contesto) per chiudere il quadro.