# NetBIOS Session Service (NBSS) — TCP 139

Tags: #networking #enumeration #netbios #smb #windows #hacking-exposed

---

## Cos'è

NBSS è il terzo e più importante dei servizi NetBIOS dal punto di vista dell'attaccante. Gira su **TCP 139** e si occupa del **trasferimento dati reale** — file sharing, print sharing, comunicazione tra processi. È il livello su cui viaggia **[[SMB]] (Server Message Block)** nelle versioni più vecchie di Windows.

---

## Le tre porte NetBIOS — recap

|Porta|Protocollo|Servizio|Scopo|
|---|---|---|---|
|UDP 137|NetBIOS-NS|Name Service|Registrazione e risoluzione nomi|
|UDP 138|NetBIOS-DGM|Datagram Service|Messaggi connectionless e broadcast|
|**TCP 139**|**NetBIOS-SSN**|**Session Service**|**Trasferimento dati reale — SMB**|

---

## Come funziona

A differenza di UDP 137 e 138, NBSS usa **TCP** — stabilisce una connessione orientata alla sessione prima di trasferire dati:

```
# Sequenza di connessione NBSS
Client  →  TCP SYN              →  Server (porta 139)
Client  ←  TCP SYN-ACK          ←  Server
Client  →  TCP ACK              →  Server    ← connessione TCP stabilita
Client  →  NetBIOS Session Request →  Server  ← "voglio parlare con FILESERVER"
Client  ←  NetBIOS Positive Response ← Server  ← sessione NetBIOS stabilita
Client  →  SMB traffic          →  Server    ← dati reali (file, autenticazione...)
```

---

## Il rapporto con SMB

TCP 139 e SMB sono strettamente legati:

- **Windows NT/2000/XP** — SMB gira **sopra NetBIOS** → TCP 139
- **Windows 2000+ (opzionale)** — SMB può girare **direttamente su TCP** → porta **445** (SMB diretto, senza NetBIOS)
- **Windows moderno** — preferisce porta 445, mantiene 139 per compatibilità legacy

```
TCP 139  →  NetBIOS Session  →  SMB  →  file/print sharing  (vecchio)
TCP 445  →  SMB direttamente →  file/print sharing           (moderno)
```

> Quando Nmap trova **entrambe 139 e 445 aperte**, la macchina supporta SMB sia nel modo legacy che in quello moderno — tipico di Windows Server 2008/2012.

---

## Cosa viaggia su TCP 139 / SMB

|Funzione|Descrizione|
|---|---|
|**File sharing**|Accesso a cartelle condivise (share)|
|**Print sharing**|Condivisione stampanti di rete|
|**IPC$ (Inter-Process Communication)**|Canale per RPC, named pipes, enumerazione|
|**Autenticazione NTLM**|Handshake di autenticazione Windows|
|**Named pipes**|Comunicazione tra processi remoti|

---

## IPC$ — il target principale per l'enumerazione

`IPC$` è una share speciale che non contiene file ma espone **named pipes** per la comunicazione tra processi. È il canale usato per:

- Enumerare utenti, gruppi, share
- Comunicare con servizi remoti via RPC
- Autenticarsi al dominio

### Null Session su IPC$

L'attacco classico: connettersi a IPC$ con **credenziali vuote** per enumerare senza autenticarsi:

```cmd
# Tentativo null session da Windows
net use \\192.168.1.50\IPC$ "" /user:""

# Se ha successo → enumera con
net view \\192.168.1.50
```

```bash
# Da Linux con enum4linux
enum4linux -a 192.168.1.50

# Con smbclient
smbclient -L \\192.168.1.50 -N    # -N = no password
smbclient \\\\192.168.1.50\\IPC$ -N
```

> ⚠️ La null session era ampiamente sfruttabile su Windows NT/2000/XP. Su Windows Null Session moderni è **bloccata di default** — ma rimane comune su HTB e reti legacy.

---

## Enumerazione via TCP 139/445

```bash
# Nmap — rileva SMB e versione
nmap -sV -p 139,445 192.168.1.50

# Nmap NSE — enumerazione SMB completa
nmap --script smb-enum-shares 192.168.1.50
nmap --script smb-enum-users 192.168.1.50
nmap --script smb-os-discovery 192.168.1.50
nmap --script smb-security-mode 192.168.1.50

# Tutto insieme
nmap --script smb-enum-shares,smb-enum-users,smb-os-discovery -p 139,445 192.168.1.50

# enum4linux — tool dedicato per enumerazione NetBIOS/SMB
enum4linux -a 192.168.1.50      # enumerazione completa
enum4linux -U 192.168.1.50      # solo utenti
enum4linux -S 192.168.1.50      # solo share
enum4linux -G 192.168.1.50      # solo gruppi

# smbclient — interazione manuale con share
smbclient -L \\192.168.1.50 -N           # lista share senza password
smbclient \\\\192.168.1.50\\files -N     # accedi alla share "files"
```

### Cosa si ottiene dall'enumerazione SMB

```
Share         Type    Comment
-----         ----    -------
IPC$          IPC     Remote IPC
ADMIN$        Disk    Remote Admin
C$            Disk    Default share
files         Disk    Company files   ← interessante ⚠️
backup        Disk    Backup storage  ← interessante ⚠️

Users:
administrator, john, mary, serviceaccount

Groups:
Domain Admins, Domain Users, IT-Staff
```

---

## Vulnerabilità storiche su TCP 139/445

TCP 139 e 445 sono storicamente tra le porte più sfruttate in assoluto:

|CVE|Nome|Anno|Descrizione|
|---|---|---|---|
|MS08-067|Conficker|2008|RCE via Server Service su TCP 139/445|
|MS17-010|EternalBlue / WannaCry|2017|RCE via SMBv1 su TCP 445|
|CVE-2020-0796|SMBGhost|2020|RCE via SMBv3 compressione su TCP 445|

```bash
# Check EternalBlue con Nmap NSE
nmap --script smb-vuln-ms17-010 -p 445 192.168.1.50

# Check MS08-067
nmap --script smb-vuln-ms08-067 -p 445 192.168.1.50
```

---

## TCP 139 vs TCP 445

| |TCP 139 (NetBIOS+SMB)|TCP 445 (SMB diretto)|
|---|---|---|
|Introdotto|Windows NT|Windows 2000|
|NetBIOS richiesto|Sì|No|
|Uso moderno|Legacy/compatibilità|Standard moderno|
|Presente su|Tutto Windows|Windows 2000+|
|Attacchi noti|Null session, MS08-067|EternalBlue, SMBGhost|

> Se su HTB trovi **solo 445** → Windows relativamente moderno Se trovi **139 e 445** → sistema più vecchio o configurazione legacy Se trovi **solo 139** → sistema molto datato (Windows NT/9x)

---

## Workflow tipico su HTB

```
1. nmap -sV -p 139,445 <target>
           ↓
2. enum4linux -a <target>         → utenti, share, gruppi, OS
           ↓
3. smbclient -L \\<target> -N    → lista share accessibili
           ↓
4. smbclient \\\\<target>\\share -N  → esplora share
           ↓
5. nmap --script smb-vuln-*      → check vulnerabilità note
           ↓
6. Exploit (EternalBlue, null session, credenziali deboli...)
```

---

## Contromisure

- Disabilitare SMBv1 (vettore EternalBlue) su tutti i sistemi
- Bloccare TCP 139 e 445 sul perimetro — mai esposti su internet
- Disabilitare null session (`RestrictAnonymous = 2` nel registro)
- Applicare patch MS17-010 (ancora molti sistemi vulnerabili)
- Abilitare SMB signing per prevenire relay attacks

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Enumeration
- MS17-010: https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010
- `man smbclient`
- `man enum4linux`
- → vedi anche: [[NetBIOS_NBNS]] (UDP 137)
- → vedi anche: [[NetBIOS_NBDS]] (UDP 138)