---

tags:

- hacking-exposed-7
- windows
- credential-dumping
- privilege-escalation
- chapter-4 created: 2026-05-16

---

# Credential Dumping: LSA Secrets vs LSASS Memory

> [!abstract] TL;DR Sono **due tecniche complementari**, non alternative. Catturano credenziali di **utenti diversi** da **fonti diverse**:
> 
> - **LSA Secrets** (disco) → password dei **service account** (spesso in plaintext)
> - **LSASS memory** (RAM) → hash NTLM degli **utenti interattivi** connessi di recente

---

## Il problema centrale

Quando comprometti una macchina Windows e vuoi credenziali, devi chiederti: **chi ha lasciato credenziali qui sopra?**

La risposta dipende da come l'utente ha interagito con la macchina. Esistono **tre categorie distinte** di "presenza" su un sistema Windows:

```
┌─────────────────────────────────────────────────────────┐
│                  MACCHINA WINDOWS                       │
│                                                         │
│  1. SERVIZI IN ESECUZIONE                               │
│     gira 24/7, account di dominio o locali              │
│     → LSA Secrets (disco, spesso plaintext)             │
│                                                         │
│  2. UTENTI LOGGATI IN PASSATO                           │
│     login storici (ultimi 10), funzione "DC offline"    │
│     → HKLM\SECURITY\CACHE (DCC2, hash da craccare)      │
│                                                         │
│  3. UTENTI ATTIVI O DI RECENTE                          │
│     sessioni interattive, RDP, console                  │
│     → LSASS (RAM, hash NTLM diretti)                    │
└─────────────────────────────────────────────────────────┘
```

Ogni tecnica colpisce **una sola** di queste tre categorie. Non si sovrappongono.

---

## 1. LSA Secrets (Dumping Cached Passwords)

### Dove vivono

```
HKLM\SECURITY\Policy\Secrets    ← chiave del registry
%SystemRoot%\System32\config\SECURITY  ← file su disco
```

### Cosa contengono

|Tipo di credenziale|Formato|
|---|---|
|Password dei service account|**Plaintext** 💀|
|Cached domain logons (ultimi 10)|Hash DCC2 (da craccare)|
|Password FTP / web|Plaintext|
|Credenziali RAS dial-up|Plaintext|
|Machine account password|Cifrata|
|Auto-logon password|Plaintext|

### Perché esistono

Windows ha bisogno di poter:

- Riavviare automaticamente i servizi senza chiedere la password ogni volta
- Autenticare gli utenti di dominio anche quando il DC è irraggiungibile (vedi [[windows_domain_logon]])
- Riconnettersi automaticamente a risorse remote

### Tool

```bash
# Storico (Hacking Exposed 7)
lsadump2.exe                    # DLL injection in LSASS, obsoleto
Cain & Abel → LSA Secrets       # vedi [[cain_and_abel_legacy]]
gsecdump (Truesec)              # x86/x64, Win2000-2008

# Moderni (2026)
mimikatz → lsadump::secrets
mimikatz → lsadump::cache       # solo cached domain logons (DCC2)
Impacket → secretsdump.py -system SYSTEM -security SECURITY LOCAL
```

### Output tipico (LSA Secrets con mimikatz)

```
[NL$1 - 11/05/2026]
RID: 000003e9 (1001)
User: CORP\alice
MsCacheV2: 0102030405060708...    ← hash DCC2, da craccare

[_SC_MSSQLSERVER]
cur/text: Sql@dmin2024!           ← PLAINTEXT, jackpot

[_SC_BackupExec]
cur/text: Backup#Service99       ← PLAINTEXT
```

> [!tip] Il vero valore degli LSA Secrets I service account in plaintext sono spesso account di dominio con privilegi elevati (per fare backup, gestire database, ecc.). Comprometti una macchina secondaria, ottieni credenziali del dominio principale senza craccare nulla.

---

## 2. LSASS Memory Dumping

### Dove vivono

```
Processo lsass.exe → memoria RAM
```

Niente disco. Niente registry. Solo RAM del processo `lsass.exe` in esecuzione.

### Cosa contengono

|Tipo di credenziale|Formato|
|---|---|
|NTLM hash della sessione attiva|Hash, usabile per PtH|
|Kerberos TGT + session key|Ticket binario|
|WDigest password|Plaintext (legacy, fino a Win 8.1)|
|Username + dominio|In chiaro|

### Quando le credenziali finiscono qui

Una credenziale entra in LSASS quando l'utente fa un [[interactive_logon|logon interattivo]]:

- Console fisica della macchina
- RDP (RemoteInteractive logon)
- "Run as administrator"
- Servizi che girano sotto un utente specifico

> [!warning] Persistenza pericolosa Anche dopo che l'utente si è **disconnesso**, le credenziali possono restare in LSASS per un periodo indefinito. Il libro di Hacking Exposed 7 sottolinea questo: _"these credentials are kept in memory even after the interactive session is terminated!"_

### Tool

```bash
# Storico (Hacking Exposed 7)
wce.exe                          # Windows Credentials Editor, Hernan Ochoa
pwdump variants                  # solo SAM, NON LSASS

# Moderni (2026)
mimikatz → sekurlsa::logonpasswords    # gold standard
mimikatz → sekurlsa::tickets           # Kerberos tickets
Impacket secretsdump (DRSUAPI/SAMR)
lsassy                                  # remote LSASS dumping
procdump → minidump LSASS → analisi offline con mimikatz
```

### Output tipico (mimikatz)

```
Authentication Id : 0 ; 387465 (00000000:0005e909)
Session           : RemoteInteractive from 2
User Name         : domainadmin
Domain            : CORP
Logon Server      : DC01
Logon Time        : 5/16/2026 9:42:13 AM
SID               : S-1-5-21-...

msv :
 [00000003] Primary
 * Username : domainadmin
 * Domain   : CORP
 * NTLM     : 8846f7eaee8fb117ad06bdd830b7586c  ← Pass-the-Hash diretto
 * SHA1     : e0fba38268d0ec66ef1cb452d5885e53...

kerberos :
 * Username : domainadmin
 * Domain   : CORP.LOCAL
 * Password : (null)
```

---

## La distinzione che conta

||**LSA Secrets**|**LSASS Memory**|
|---|---|---|
|**Locazione fisica**|Disco (registry)|RAM (`lsass.exe`)|
|**Chi cattura**|Service accounts + login storici|Utenti interattivi attivi/recenti|
|**Sopravvive al reboot**|✅ Sì|❌ No|
|**Formato dominante**|Plaintext (service accts)|Hash NTLM|
|**Serve craccare**|No (per service accts), sì per DCC2|No (PtH diretto)|
|**Utile quando**|Sempre — anche a server vuoto|Solo se qualcuno si è connesso|
|**Privilegi richiesti**|SYSTEM|SYSTEM o SeDebugPrivilege|
|**Bloccato da Credential Guard**|Parzialmente|Sì (vedi [[virtualization_based_security]])|

---

## Scenari reali

### Scenario A — Backup server alle 3 di notte

Nessuno è connesso. Compromettiamo il server.

**LSASS** → solo `MACHINE$` (account computer). Poco interessante.

**LSA Secrets** → service account `CORP\backup_svc` in plaintext. Spesso questi account hanno privilegi di "Backup Operator" su tutto il dominio. 🎯

> Vincitore: **LSA Secrets**

### Scenario B — Jump server alle 14:00

Un domain admin si è collegato un'ora fa via RDP e si è disconnesso.

**LSASS** → hash NTLM di `CORP\domainadmin` ancora in memoria. Pass-the-Hash → controllo del dominio. 🎯

**LSA Secrets** → soliti service account, già noti.

> Vincitore: **LSASS Memory**

### Scenario C — Master User Domain attack (esempio del libro, p. 196)

Il libro descrive: server in un **resource domain** esegue un servizio sotto un account del **master user domain** (vedi architettura NT in [[windows_domain_logon]]).

- Comprometti il server nel resource domain
- LSA Secrets → password in plaintext dell'account del master domain
- Pivot al master domain (= compromesso totale dell'azienda)

> [!warning] Lezione pratica **Mai usare account di dominio privilegiati per avviare servizi su macchine meno sicure.** Un service account su una macchina di secondo livello può scalare fino al dominio principale.

---

## Mappa mentale finale

```
"Chi fa girare i servizi qui?"
        ↓
  → LSA Secrets (disco)
  → password plaintext
  → utile sempre

"Chi si è seduto a questa macchina di recente?"
        ↓
  → LSASS Memory (RAM)
  → hash NTLM / ticket Kerberos
  → utile solo se c'è stata attività

→ Un attaccante serio fa ENTRAMBE.
```

---

## Difese

### Contro LSA Secrets dumping

- Non usare account di dominio privilegiati per servizi locali
- Group Managed Service Accounts (gMSA) — password gestite da AD, ruotate automaticamente
- Tier model: separare admin di workstation, server, e domain

### Contro LSASS dumping

- [[virtualization_based_security|Credential Guard]] — sposta i segreti in VTL 1
- Disabilitare WDigest (chiave registry: `UseLogonCredential = 0`)
- Protected Process Light (PPL) per LSASS
- Restricted Admin mode per RDP — non lascia credenziali sul target
- LAPS per account locali

---

## Collegamenti

- [[interactive_logon]] — perché le credenziali finiscono in LSASS
- [[windows_domain_logon]] — local vs domain logon, master domain
- [[virtualization_based_security]] — Credential Guard e i suoi limiti
- [[cain_and_abel_legacy]] — il tool storico per LSA Secrets
- [[pass_the_hash]] — uso pratico degli hash NTLM dumpati
- [[kerberos_pass_the_ticket]] — uso dei ticket dumpati da LSASS

---

## Fonti

- Hacking Exposed 7, Chapter 4, pp. 195–200
    - "Dumping Cached Passwords" (LSA Secrets)
    - "Dumping Hashes Stored in Memory" (WCE / LSASS)
- MITRE ATT&CK: T1003.001 (LSASS Memory), T1003.004 (LSA Secrets), T1003.005 (Cached Domain Credentials)

---
# Perché mantiene gli ultimi 10 utenti loggati nella cache ed anche gli account dei servizi?

Ottima domanda — e prima di rispondere, una piccola precisazione sulla tua sintesi:

Quando dici "quelli in cache contengono gli account dei servizi e gli ultimi 10 account loggati", stai unendo **due cose che il libro raggruppa sotto 'cached passwords' ma che sono tecnicamente distinte**:

```
HKLM\SECURITY\
    ├── Policy\Secrets  ←  LSA Secrets (service accounts in plaintext, ecc.)
    └── Cache\NL$1..NL$10  ←  Cached Domain Logons (hash DCC2 degli utenti di dominio)
```

Sono due meccanismi diversi che convivono nello stesso hive del registry. La tua domanda riguarda specificamente il secondo: **perché Windows conserva gli ultimi 10 login di dominio?**

---

## Il problema che risolve: il login offline

Immagina questo scenario concreto:

> Alice ha un laptop aziendale, `CORP\alice`. Lunedì mattina, in ufficio, si logga normalmente: il laptop contatta il Domain Controller, Kerberos fa il suo lavoro, tutto bene.
> 
> Martedì Alice prende l'aereo per una trasferta. Apre il laptop a 10.000 metri di quota. **Nessuna rete. Nessun DC raggiungibile.**
> 
> Digita la sua password di dominio. Cosa succede?

Senza caching → **non potrebbe loggarsi.** Il laptop non ha modo di verificare la sua password perché l'unica entità che la conosce (il DC) è irraggiungibile.

Con il caching → Windows ha salvato un **verifier** del login precedente. Quando Alice digita la password, Windows:

1. Calcola il DCC2 della password che ha appena digitato
2. Lo confronta con quello salvato in `HKLM\SECURITY\Cache\NL$1`
3. Se corrispondono → la fa entrare

Risultato: Alice lavora sull'aereo. Quando atterra e si riconnette alla rete aziendale, il sync con il DC riprende normalmente.

---

## Perché non salvare la password in chiaro?

Sarebbe più semplice — ma anche disastroso. Quindi Microsoft ha scelto un compromesso:

```
DCC2 = PBKDF2( MD4(password), username, 10.240 iterazioni )
```

Tre proprietà importanti:

1. **One-way**: dal DCC2 non risali alla password (devi craccare)
2. **Lento**: PBKDF2 con 10.240 iterazioni è volutamente CPU-intensivo, per rallentare il cracking
3. **Salt-like**: l'username fa da salt, quindi due utenti con la stessa password hanno DCC2 diversi

Il DCC2 **non serve per autenticarsi a servizi remoti** (a differenza dell'hash NTLM in LSASS, che permette Pass-the-Hash). Serve solo come "verifier locale": _"questa password corrisponde a quella che hai usato l'ultima volta che ti sei loggato?"_

> [!tip] Differenza pratica Un hash NTLM rubato → puoi accedere a share, server, ecc. (PtH) Un DCC2 rubato → devi craccarlo per ottenere la password in chiaro. Poi sì, hai la password.

---

## Perché "ultimi 10" e non infiniti?

Default storici:

- Windows workstation: 10
- Windows server: 25
- Configurabile via `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\CachedLogonsCount`

Tre motivi:

1. **Spazio**: ogni cache entry occupa memoria nel registry
2. **Sicurezza**: meno credenziali in giro = meno superficie d'attacco
3. **Senso pratico**: un laptop tipicamente ha 1–2 utenti. Un terminal server ne potrebbe avere di più, ma raramente più di 25

> [!warning] Hardening Il libro di Hacking Exposed 7 raccomanda di abbassare questo valore. Settarlo a `1` mantiene la funzionalità per l'utente principale del laptop ma elimina credenziali di amministratori che si sono loggati una volta per fare manutenzione. Settarlo a `0` disabilita del tutto il caching — utile per macchine fisse in azienda che non si scollegano mai dalla rete.

---

## Lo scenario d'attacco

Ecco perché questo "feature di comodità" diventa un problema:

```
Tu sei admin di dominio.
Vai in officina a fixare il PC di Bob.
Ti logghi con CORP\admin per installare un driver.
Ti scolleghi. Te ne vai.

3 mesi dopo, Bob viene infettato da malware.
L'attaccante dumpa HKLM\SECURITY\Cache.
Trova DCC2 di CORP\admin.
Lo cracca in 2 settimane perché la password era "Estate2024!".
```

Lezione: **un domain admin che si logga anche una sola volta su una macchina utente lascia una traccia che può essere sfruttata mesi dopo**. È uno dei motivi per cui esiste il **tier model** in sicurezza aziendale moderna: gli account privilegiati non devono MAI loggarsi su workstation utente.

---

## Riassunto

Windows mantiene gli ultimi N login di dominio in cache **per permettere il login offline degli utenti di dominio**. Il caso d'uso primario è il laptop aziendale fuori sede.

Il prezzo che si paga:

- Un attaccante che compromette la macchina può estrarre questi verifier
- Crackandoli, ottiene le password in chiaro degli utenti
- Anche utenti che non sono più "presenti" sulla macchina, ma ci sono passati

È il classico **trade-off tra usabilità e sicurezza**: senza questa feature i laptop sarebbero molto meno usabili, ma con essa ogni macchina diventa un piccolo archivio storico di credenziali da custodire.
