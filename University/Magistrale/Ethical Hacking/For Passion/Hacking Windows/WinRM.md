# WinRM — Windows Remote Management

**Porte:** `5985/tcp` (HTTP) · `5986/tcp` (HTTPS)  
**OS:** Windows  
**Categoria:** #remote-access #enumeration #exploitation #windows

---

## 📖 Cos'è

WinRM è il protocollo Microsoft per la **gestione remota di sistemi Windows**, basato sullo standard WS-Management. Trasporta messaggi **[[SOAP]] over [[Obsidian-University/University/Magistrale/Cybersecurity/3 CFU/Extra/Web Technologies/HTTP|HTTP]]**, per questo nmap lo identifica come servizio HTTP.

È l'equivalente Windows di SSH — permette di eseguire comandi PowerShell da remoto.

> ⚠️ Il titolo "Not Found" su porta 5985 è normale — non è un web server tradizionale

---

## 🔍 Identificazione

```
5985/tcp open  http    Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: OS: Windows
```

### Nmap scripts

```bash
nmap -p 5985 --script http-auth-finder <IP>
```

---

## 🔌 Connessione — [[Evil-WinRM]]

Il tool principale su Kali per connettersi a WinRM:

```bash
# Installazione
sudo gem install evil-winrm

# Connessione con username e password
evil-winrm -i <IP> -u <utente> -p <password>

# Connessione con hash NTLM (Pass the Hash)
evil-winrm -i <IP> -u <utente> -H <NTLM_hash>

# Connessione con chiave SSL (porta 5986)
evil-winrm -i <IP> -u <utente> -p <password> -S
```

---

## ⚙️ Prerequisiti per l'accesso

Per connettersi via WinRM l'utente deve essere membro di uno di questi gruppi:

- `Administrators`
- `Remote Management Users`

---

## 💥 Post-exploitation — comandi utili nella shell

```powershell
# Info sistema
whoami
hostname
systeminfo

# Utenti e gruppi
net users
net localgroup administrators

# Privilegi utente corrente
whoami /priv

# Processi in esecuzione
Get-Process

# Servizi
Get-Service

# File e navigazione
Get-ChildItem
Get-ChildItem -Recurse -Filter "*.txt"

# Cerca la flag
Get-ChildItem -Path C:\ -Recurse -Filter "flag.txt" 2>$null
Get-ChildItem -Path C:\Users -Recurse -Filter "user.txt" 2>$null
```

---

## ⚠️ Misconfiguration comuni

- **Credenziali deboli** → accesso diretto con password semplici
- **WinRM esposto su internet** → dovrebbe essere accessibile solo sulla LAN
- **Utenti non amministratori** nel gruppo `Remote Management Users` con accesso non necessario

---

## 🛠️ Tool alternativi

```bash
# CrackMapExec — verifica credenziali WinRM
crackmapexec winrm <IP> -u <utente> -p <password>

# PowerShell nativo (da Windows)
Enter-PSSession -ComputerName <IP> -Credential <utente>
```

---

## 📚 Lezioni apprese

- WinRM su porta 5985 appare come HTTP in nmap — non confonderlo con un web server
- Evil-WinRM è lo strumento standard su Kali per ottenere shell Windows
- Serve avere credenziali valide — WinRM non ha vulnerabilità di accesso anonimo
- Supporta Pass-the-Hash con hash NTLM se non si ha la password in chiaro
- Su HTB le flag Windows si trovano tipicamente in `C:\Users\<utente>\Desktop\`

---

## 🔗 Riferimenti

- [Evil-WinRM GitHub](https://github.com/Hackplayers/evil-winrm)
- [HackTricks - WinRM](https://book.hacktricks.xyz/network-services-pentesting/5985-5986-pentesting-winrm)

---

## Tags

#winrm #windows #remote-access #evil-winrm #powershell #pentesting #port-5985 #htb