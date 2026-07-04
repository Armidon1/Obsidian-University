---
tags: [ethl, hacking-exposed-7, credential-dumping, lsa-secrets, cap4]
capitolo: 4
data: 2026-07-02
collegamenti: ["[[ETHL - LSASS Credential Dumping]]", "[[ETHL - SAM (Security Accounts Manager)]]", "[[ETHL 0x12 - Cap 4 Hacking Windows]]"]
---

# LSA Secrets

> [!abstract] Di cosa parla
> Il terzo deposito di credenziali del trio SAM / LSASS / LSA Secrets. È dove Windows conserva i segreti **persistenti** che il sistema deve poter riusare da solo, anche dopo un riavvio, senza un utente presente. La chiave di lettura che lo distingue dagli altri due: non sono account locali (SAM) né credenziali di chi è loggato ora (LSASS), ma **segreti di servizio memorizzati sulla macchina**.

---

## Cosa sono

> [!info] Segreti persistenti
> Gli LSA Secrets sono credenziali e segreti che la Local Security Authority conserva per far funzionare servizi e integrazioni senza intervento umano. Sono cifrati a macchina spenta, ma la LSA li **decifra e li tiene disponibili in memoria dopo il boot/login**, perché il sistema deve poterli usare. Vivono nel ramo di registro `HKLM\SECURITY\Policy\Secrets`, leggibile solo con privilegio **SYSTEM**.

> [!info] Cosa contengono
> Il contenuto è tipicamente il più "succoso" delle tre fonti perché spesso è in chiaro: password dei **service account** (i servizi che partono con un account di dominio), password di **scheduled task**, la password dell'**account computer** usata per il canale col dominio, credenziali di **auto-logon**, segreti di connessioni **RAS/VPN**, e cache varie. A differenza del SAM (che dà hash), qui capita di trovare password direttamente utilizzabili.

---

## Perché contano

> [!info] Da segreto a escalation
> Un service account la cui password esce dagli LSA Secrets è spesso un account **di dominio** con privilegi non banali (a volte molto alti, per pigrizia amministrativa). Recuperarne la password in chiaro non è un hash da craccare: è una credenziale pronta per autenticarsi altrove. Per questo gli LSA Secrets sono un vettore diretto di **escalation** e movimento laterale, non solo di raccolta.

> [!info] Account computer
> La password dell'account computer nel dominio è particolarmente interessante: dà alla macchina (e a chi la ruba) un'identità autenticata nel dominio, utile in catene d'attacco più avanzate. È il tipo di segreto che sta qui e da nessun'altra parte.

---

## Come si estraggono

> [!info] Idea generale
> Si esportano/leggono i rami `SECURITY` e `SYSTEM` (serve la bootkey per decifrare, come per il SAM), e si decifrano i secret. Precondizione: **SYSTEM / admin locale**, oppure accesso offline ai rami. È sempre roba post-escalation.

> [!info] Con mimikatz
> Sulla macchina viva, con privilegi adeguati:

```text
mimikatz # token::elevate
mimikatz # lsadump::secrets
```

> [!info] Con Impacket
> `secretsdump.py` estrae gli LSA Secrets **insieme** a SAM e cache di dominio in un colpo — è il motivo per cui nelle note appare sempre lo stesso tool per tutte e tre le fonti.

```bash
# Remoto, con credenziali admin
secretsdump.py DOMINIO/administrator:password@<IP-target>

# Offline, da rami salvati (reg save HKLM\SECURITY / HKLM\SYSTEM)
secretsdump.py -security security.hive -system system.hive LOCAL
```

> [!tip] Cosa esce e come si usa
> Escono spesso **password in chiaro** di service/computer account → si riusano direttamente per autenticarsi (niente cracking). Se esce un hash, vale la solita via pass-the-hash / cracking. Il valore è che una singola macchina compromessa può rivelare le credenziali di un account di dominio riusato su molti sistemi.

---

## Cache di dominio (nota a margine)

> [!info] Non confondere
> Accanto agli LSA Secrets, `secretsdump` tira fuori anche la **cache dei logon di dominio** (gli ultimi 10 logon, hashati per il logon offline). Sono cose diverse: gli LSA Secrets sono segreti di servizio spesso in chiaro; la cache di dominio sono hash (formato "mscash/DCC2") che vanno **craccati** e sono progettati per essere lenti da craccare. Stessa estrazione, prede diverse.

---

## Contromisure

> [!warning] Come si difende
> Serve già **SYSTEM** per leggerli → difesa a monte (least privilege, EDR, non farsi ottenere admin locale). **Non usare account di dominio ad alti privilegi come service account** su macchine esposte: se la password finisce negli LSA Secrets, si è regalato un account privilegiato. Preferire **gMSA** (Group Managed Service Accounts), con password gestite e ruotate dal sistema, mai in chiaro riutilizzabile. **Disabilitare l'auto-logon**. Sicurezza **fisica** contro l'estrazione offline dei rami di registro.

---

## Fili rossi

> [!tip] Come si lega al resto
> **Terzo deposito**: chiude il trio con SAM (registro/disco, hash locali) e LSASS (RAM, hash+ticket dei loggati) — vedi la nota LSASS. **Password in chiaro**: è la fonte dove più spesso si salta il cracking. **Service account privilegiati**: il ponte verso escalation e movimento laterale, tema che riemerge con Kerberoasting (là si cracca l'hash del servizio, qui a volte si ha direttamente la password). **Retrocompatibilità / comodità = buco**: l'auto-logon e i service account riusati sono l'ennesimo caso di configurazione comoda ma insicura.

---

## Punti aperti

> [!question] Da verificare
> La distinzione precisa tra LSA Secrets e cache di dominio a livello di formato/uso, se l'esame la chiede. Da confermare se il corso tratta gMSA come contromisura o si ferma al "usa password forti sui service account".
