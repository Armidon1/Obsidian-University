---

tags:

- active-directory
- lateral-movement
- post-exploit
- hacking-exposed-7
- red-team
- windows aliases:
- lateral movement
- movimento laterale
- pivot

---

# Lateral Movement — Spostarsi tra Host nel Dominio

## 1. Cosa è e perché esiste

> Il **lateral movement** è la fase in cui un attaccante, già con foothold su una macchina del dominio, si sposta su altri host per espandere l'accesso fino a raggiungere il target finale.

È lo step tra **initial access** (sei dentro una macchina) e **domain compromise** (controlli il dominio). Nessun attaccante reale resta sulla prima macchina compromessa — quella è quasi sempre solo il punto d'ingresso.

```
[Initial access: phishing su Mario]
       ↓
[Workstation Mario - utente standard]
       ↓ privilege escalation locale
[Workstation Mario - admin locale]
       ↓ dump LSASS → trovi hash di un IT admin
       ↓ LATERAL MOVEMENT con quell'hash      ← SIAMO QUI
[Server IT, Database server, Helpdesk, ...]
       ↓ raggiungi una macchina dove un Domain Admin è loggato
       ↓ dump LSASS → hash DA
       ↓ Pass-the-Hash come DA
[Domain Controller — game over]
```

> [!note] Nel ciclo kill chain Nella **Lockheed Martin Kill Chain** è parte dello Stage 4 (Exploitation). In **MITRE ATT&CK** è una tactic propria (TA0008 — Lateral Movement) con 9 tecniche distinte.

---

## 2. Prerequisiti — cosa serve per muoversi

Lateral movement **non è exploitation**. Non sfrutti bug del software remoto. Usi **credenziali valide** su un protocollo legittimo. Lo strumento di accesso (SMB, WinRM, RDP) si comporta come se fossi l'utente legittimo — perché in effetti **stai usando le sue credenziali rubate**.

I tipi di "credenziale" utilizzabili:

|Tipo|Da dove arrivano|Come si usano|
|---|---|---|
|**Password in chiaro**|Mimikatz (WDigest), Credential Manager, file di configurazione, browser|Login normale|
|**NT hash (NTLM)**|LSASS dump, SAM dump, secretsdump DCSync|[[pass_the_hash]]|
|**Kerberos TGT**|LSASS dump (Mimikatz), Rubeus|Pass-the-Ticket|
|**Kerberos TGS**|Roasting, dump|Pass-the-Ticket per servizio specifico|
|**Certificati**|Active Directory Certificate Services abuse|Authentication via PKINIT|

> [!tip] La regola d'oro Non serve la password in chiaro per autenticarsi. Su NTLM, **l'NT hash è equivalente alla password**. Su Kerberos, il **TGT è equivalente all'identità**. Questa è la base di tutti i Pass-the-X.

---

## 3. Tecniche di lateral movement — l'arsenale

### A. SMB-based — PsExec e famiglia

**PsExec** (Sysinternals) è il tool storico per eseguire comandi remoti tramite SMB. Workflow:

1. Copia un binary su `\\<target>\ADMIN$`
2. Crea un servizio remoto via SMB che lancia quel binary come SYSTEM
3. Lo avvia, cattura input/output via named pipe
4. Cleanup

```cmd
:: PsExec originale (necessita Sysinternals)
psexec \\target -u admin -p password cmd

:: Versione Impacket — funziona da Linux con hash
psexec.py corp.local/admin:password@target
psexec.py -hashes :NThash corp.local/admin@target
```

> [!warning] PsExec è rumoroso Crea sempre un servizio remoto (Event ID 7045 + 4697) e usa ADMIN$ share. Detection facile per qualsiasi EDR moderno. Va bene per CTF, in red team reali si usano alternative più stealthy.

### B. WMI execution — `wmiexec`

Sfrutta **WMI** (Windows Management Instrumentation) per eseguire comandi sulla macchina remota. Più stealthy di PsExec perché:

- Non crea servizi
- Non scrive sul disco remoto
- Usa protocollo legittimo (DCOM su porta 135 + porta dinamica)

```bash
wmiexec.py corp.local/admin:password@target
wmiexec.py -hashes :NThash corp.local/admin@target
```

Output: shell semi-interattiva. Ogni comando è una chiamata WMI separata, quindi nessuna shell persistente vera — ma sufficiente per esplorare.

### C. WinRM — `evil-winrm` (visto su Sauna)

**WinRM** (Windows Remote Management) è l'implementazione Microsoft di WS-Management. Porta 5985 (HTTP) o 5986 (HTTPS). È il modo "ufficiale" Microsoft per remote admin → presente su molti server, raramente sulle workstation.

```bash
# Login con password
evil-winrm -i 10.10.10.175 -u fsmith -p Thestrokes23

# Pass-the-Hash via WinRM (esattamente quello fatto su Sauna)
evil-winrm -i 10.10.10.175 -u Administrator -H <NThash>
```

> [!tip] Sauna playbook Su [[htb_sauna]] hai usato evil-winrm DUE volte:
> 
> 1. Login normale come `fsmith` con password crackata
> 2. **Pass-the-Hash** come `Administrator` con NT hash da DCSync
> 
> Entrambi sono lateral movement — la seconda volta è un classico PtH.

WinRM-based è considerata una delle vie più "pulite" di lateral movement perché è un protocollo legittimo, esiste documentazione Microsoft, e produce log diversi da PsExec.

### D. SMB exec — `smbexec`

Alternativa a PsExec senza dropping di binari sul target. Sfrutta SMB share per scrivere output di comandi in file temporanei.

```bash
smbexec.py corp.local/admin:password@target
```

Molto stealthy ma più lento di wmiexec.

### E. DCOM — Distributed COM

Sfrutta oggetti COM remoti per eseguire codice. Tecnica avanzata, usata in red team perché spesso non monitorata dagli EDR.

```bash
dcomexec.py corp.local/admin:password@target
```

Famiglia di tecniche: MMC20.Application, ShellWindows, ShellBrowserWindow.

### F. RDP — Remote Desktop

GUI completa sul target. Utile quando devi fare cose che non si fanno bene da shell (browser, applicazioni interattive). Più rumoroso degli altri (sessione interattiva visibile a chi è loggato fisicamente).

```bash
xfreerdp /u:admin /p:password /v:target /dynamic-resolution

# Pass-the-Hash su RDP — richiede "Restricted Admin mode" abilitato
xfreerdp /u:admin /pth:<NThash> /v:target /restricted-admin
```

### G. SSH — per host Linux nel dominio

Non solo Windows. Server Linux joinati al dominio AD via SSSD/realm sono lateral movement target validi.

```bash
ssh user@linux-server -i stolen_key
# oppure
sshpass -p 'password' ssh user@linux-server
```

### Riepilogo — quando usare quale

|Tecnica|Quando|Detection|
|---|---|---|
|**PsExec**|Default, sempre funziona|Alta (Event 7045, 4697)|
|**WMI / wmiexec**|Stealth medio|Media (Event 4688 + WMI logs se attivati)|
|**WinRM / evil-winrm**|Server, soprattutto se admin lo usa già|Bassa-Media (Event 4624 logon type 3)|
|**SMB exec**|PsExec è bloccato|Media|
|**DCOM**|Stealth alto in red team|Bassa (raramente monitorata)|
|**RDP**|Necessiti interactive|Alta (sessione visibile)|

---

## 4. Tool — l'arsenale lateral movement

### Impacket suite — Python, multi-platform

|Tool|Tecnica|
|---|---|
|`psexec.py`|SMB-based PsExec|
|`wmiexec.py`|WMI execution|
|`smbexec.py`|SMB silent execution|
|`dcomexec.py`|DCOM-based|
|`atexec.py`|Schedule task via SMB|
|`mssqlclient.py`|Login SQL Server, `xp_cmdshell`|

### evil-winrm (Ruby)

Specializzato per WinRM. Supporta password, NT hash, Kerberos ticket.

### NetExec / CrackMapExec (Python)

Swiss army knife per AD lateral movement. Spraying, lateral execution, dump, BloodHound collect — tutto integrato.

```bash
# Spray una password su tutti gli host
nxc smb 10.10.10.0/24 -u admin -p 'Password123' 

# Eseguire un comando ovunque hai accesso
nxc smb 10.10.10.0/24 -u admin -H <hash> -x 'whoami'

# Dump SAM dove sei admin
nxc smb 10.10.10.0/24 -u admin -H <hash> --sam
```

> [!tip] Workflow tipico con NetExec
> 
> 1. `nxc smb <range> -u user -p pass` — vede dove le credenziali funzionano
> 2. Su quegli host, dump credenziali
> 3. Nuove credenziali → ripeti su un range più ampio
> 4. Espansione esponenziale finché non trovi credenziali di un account ad alto privilegio

### Rubeus / Mimikatz — Kerberos toolkit

Per estrarre/iniettare ticket Kerberos, eseguire Kerberoasting, Golden/Silver Ticket, S4U abuse.

### BloodHound — path planning

**Non è un tool di lateral movement**, è un tool di **pianificazione**. Ti mostra il grafo del dominio e calcola il path più breve da dove sei a dove vuoi arrivare.

Pattern d'uso:

```
1. Compromesso utente A
2. BloodHound: "Shortest path from A to Domain Admin"
3. Path: A → B → C → D → Domain Admin
4. Esegui ogni step con la tecnica appropriata
```

---

## 5. Concetti chiave correlati

### Local Admin Privilege Reuse

Molte aziende usano la **stessa password admin locale** su tutte le workstation per "comodità" IT. Se compromettì 1 workstation e dumpi l'hash dell'admin locale → con quell'hash puoi fare PtH su **tutte** le workstation.

Mitigazione: **LAPS** (Local Admin Password Solution) — Microsoft genera password casuali univoche per ogni macchina e le salva in AD con permessi ristretti.

### Logon Types — cosa lascia cosa in memoria

Quando un account si autentica su una macchina, lascia tracce diverse a seconda del **logon type**:

|Logon Type|Quando|Credenziali in LSASS?|
|---|---|---|
|**2 Interactive**|Login fisico / RDP|Sì (cleartext + hash)|
|**3 Network**|Accesso SMB share|Solo nel target, ma ridotte|
|**4 Batch**|Scheduled task|Sì|
|**5 Service**|Servizio|Sì|
|**9 NewCredentials**|RunAs|Sì|
|**10 RemoteInteractive**|RDP|Sì|
|**11 CachedInteractive**|Offline domain logon|Hash cached (DCC2)|

**Implicazione**: se vuoi rubare le credenziali di Mario, devi colpire una macchina dove Mario ha fatto **Interactive logon** (type 2) o **RemoteInteractive** (type 10) — non basta che si sia connesso via SMB.

BloodHound mostra queste sessioni: `Find user X's logon sessions` → ti dice su quali host Mario è loggato adesso.

### Hop-by-hop methodology

```
[Host A — credenziali utente1]
     ↓ dump LSASS
[trova hash di utente2 loggato su Host A]
     ↓ PtH su Host B (dove utente2 è admin)
[Host B — adesso sei utente2]
     ↓ dump LSASS
[trova hash di utente3 loggato su Host B]
     ↓ PtH su Host C
...
```

Ogni hop aumenta il privilegio o l'accesso. Si continua finché non si raggiunge il DA o un'altra credenziale "definitiva".

---

## 6. Detection — il lato blue team

### Event ID più rilevanti

|Event ID|Cosa indica|
|---|---|
|**4624** logon type 3|Network logon (SMB/WinRM/WMI da remoto)|
|**4624** logon type 10|RemoteInteractive (RDP)|
|**4648**|Logon with explicit credentials (RunAs, PtH spesso)|
|**4672**|Special privileges assigned to new logon|
|**4697 / 7045**|Service installation (PsExec firma)|
|**4688**|Process creation (cmd.exe, powershell.exe spawn remoto)|

### Pattern di detection

- **PsExec signature**: Event 7045 + servizio con nome random
- **WMI lateral**: log specifici di WMI-Activity (se abilitati)
- **WinRM**: 4624 con port 5985/5986
- **PtH detection**: 4624 + LogonType 9 (NewCredentials) o pattern anomali

### Tool di detection

- **SIEM** che correla eventi tra host (anomalous logon da host inusuali)
- **Microsoft Defender for Identity** (ex Azure ATP) — focus su AD-level attacks
- **CrowdStrike, SentinelOne, Carbon Black** — EDR con behavioral detection di lateral movement

---

## 7. Difese strutturali

|Difesa|Cosa mitiga|
|---|---|
|**LAPS**|Riuso di local admin password tra workstation|
|**Credential Guard** ([[virtualization_based_security]])|Estrazione credenziali da LSASS|
|**PPL su LSASS**|Mimikatz / pypykatz|
|**Restricted Admin mode su RDP**|Pass-the-Hash via RDP|
|**AD Tiering Model** (tier 0/1/2)|DA non si logga su workstation — impedisce dump del suo hash|
|**Disable LM/NTLMv1**|Net-NTLM downgrade attacks|
|**Network segmentation**|Workstation non si parlano tra loro|
|**MFA per accessi privilegiati**|Riutilizzo credenziali|
|**JEA (Just Enough Administration)**|Admin con privilegi limitati a operazioni specifiche|

> [!abstract] AD Tiering — il concetto chiave Il **tier 0** sono i Domain Controllers e gli account che li amministrano. Il principio: un DA **non deve mai loggarsi** su workstation o server di tier inferiore, altrimenti il suo hash finisce in LSASS di quelle macchine. Tier separation = blast radius limitato.

---

## 8. Connessione con Sauna

[[htb_sauna]] è un esempio minimal di lateral movement (su una sola macchina, ma il pattern è lo stesso):

```
Esterno
   ↓ AS-REP Roasting (unauth)
fsmith password crackata
   ↓ evil-winrm — LATERAL MOVEMENT (esterno → user shell)
shell fsmith
   ↓ enumerate (Winlogon registry)
password svc_loanmgr in chiaro
   ↓ enumeration (BloodHound)
svc_loanmgr ha DCSync rights
   ↓ secretsdump.py — privilege escalation
NT hash Administrator
   ↓ evil-winrm -H — Pass-the-Hash — LATERAL MOVEMENT (user → admin)
shell Administrator
```

Le due frecce "evil-winrm" sono entrambe lateral movement — la prima con password, la seconda con hash. Su un dominio vero invece di una sola macchina, ogni hop sarebbe verso un host diverso.

---

## Takeaways

1. **Lateral movement ≠ exploitation** — usi credenziali rubate su protocolli legittimi
2. **Tecniche principali**: PsExec (SMB), WMI, WinRM (più stealthy), RDP, SSH per Linux
3. **NetExec/CrackMapExec** è il tool che orchestra tutto in AD — spraying + execution + dump in un comando
4. **BloodHound** non esegue lateral movement — **pianifica** il path migliore
5. **Logon types** determinano cosa rimane in LSASS — `Find logon sessions` ti dice dove andare
6. **LAPS** rompe il riutilizzo di local admin — difesa più impattante contro lateral movement
7. **AD Tiering** è la difesa strutturale: DA non si logga mai dove un attaccante può dumpare LSASS
8. Le credenziali equivalgono all'identità: **NT hash = password** per NTLM, **TGT = identità** per Kerberos

---

## Wiki-links

- [[HTB - Sauna]]
- [[Privilege Escalation Windows]]
- [[Pass-the-Hash]]
- [[pass the ticket]]
- [[kerberoasting]]
- [[GetNPUsers - AS-REP Roasting]]
- [[Credential Dumping - LSA Secrets vs LSASS Memory]]
- [[VBS - Virtualization-Based Security (VBS)]]
- [[impacket]]
- [[bloodhound]]
- [[netexec_crackmapexec]]
- [[Active Directory (AD)]]
- [[mitre_attck]]
- [[hacking_exposed_7_windows]]