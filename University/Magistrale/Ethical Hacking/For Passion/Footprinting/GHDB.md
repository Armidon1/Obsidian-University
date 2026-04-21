# GHDB — Google Hacking Database

#linux #cybersecurity #osint #reconnaissance #google-dorks #linux-basics-for-hackers

---

## 🗂️ Overview

La **Google Hacking Database (GHDB)** è un indice categorizzato di query per motori di ricerca progettate per scoprire informazioni sensibili rese pubblicamente disponibili su internet — spesso **per errore**.

> Mantenuta da **OffSec** (gli stessi di Kali Linux e OSCP) come estensione dell'Exploit Database. 🔗 https://www.exploit-db.com/google-hacking-database

Il processo di "Google Hacking" fu popolarizzato nel 2000 da **Johnny Long**, hacker professionista, che coniò il termine **"Googledork"** — riferito a "una persona sciocca o inetta rivelata da Google". Il punto era sottolineare che non è un problema di Google, ma di **misconfigurazioni** da parte degli utenti o dei software.

```
Il motore di ricerca fa il suo lavoro — indicizza tutto ciò che trova.
Il problema è che trova cose che non avrebbero mai dovuto essere pubbliche.
```

Recentemente Google ha reso le cose più difficili. Si può provare ad usare però bing.com, github search, [[Shodan]], duckduckgo.

---

## 🧠 Come Funzionano i Google Dork

Un Google Dork è una **query avanzata** che sfrutta gli operatori speciali di Google per trovare informazioni specifiche che una ricerca normale non restituirebbe.

### Operatori fondamentali

```
site:         → limita la ricerca a un dominio specifico
intitle:      → cerca nel titolo della pagina
inurl:        → cerca nell'URL della pagina
intext:       → cerca nel corpo del testo
filetype:     → cerca un tipo di file specifico
ext:          → alternativa a filetype
cache:        → versione cache di Google di una pagina
link:         → pagine che linkano a un URL
related:      → siti simili a un dominio
"stringa"     → corrispondenza esatta della stringa
-parola       → esclude una parola dai risultati
OR            → uno o l'altro termine
*             → wildcard — qualsiasi parola
..            → range numerico (es. 2020..2024)
```

### Combinare operatori

```bash
site:gov filetype:pdf "confidential"
intitle:"index of" site:target.com
inurl:admin site:target.com -login
```

---

## 📂 Le 14 Categorie della GHDB

La GHDB organizza i dork in categorie per tipo di informazione trovata:

|#|Categoria|Cosa trova|
|---|---|---|
|1|**Footholds**|Punti di accesso iniziali, shell, backdoor|
|2|**Files Containing Usernames**|File con username in chiaro|
|3|**Sensitive Directories**|Directory sensibili esposte|
|4|**Web Server Detection**|Tipo e versione del web server|
|5|**Vulnerable Files**|File noti per essere vulnerabili|
|6|**Vulnerable Servers**|Server con configurazioni pericolose|
|7|**Error Messages**|Messaggi di errore con info interne|
|8|**Files Containing Juicy Info**|File con informazioni preziose|
|9|**Files Containing Passwords**|File con password in chiaro o hash|
|10|**Sensitive Online Shopping Info**|Dati di pagamento e acquisti|
|11|**Network or Vulnerability Data**|Topologie di rete, scan results|
|12|**Pages Containing Login Portals**|Pannelli di login esposti|
|13|**Various Online Devices**|Dispositivi IoT, router, webcam|
|14|**Advisories and Vulnerabilities**|Pagine con info su CVE specifici|

---

## 💀 Dork per Categoria — Esempi Pratici

### 🔴 Footholds — Accesso iniziale

```bash
intitle:"phpMyAdmin" inurl:"/phpmyadmin/"
inurl:"/shell.php"
inurl:"cmd.php" intitle:"cmd"
intitle:"Web Shell" inurl:shell
```

---

### 👤 Files Containing Usernames

```bash
filetype:log intext:"username"
filetype:cfg intext:"user ="
inurl:etc/passwd filetype:txt
intitle:"Index of" passwd
```

---

### 📁 Sensitive Directories

```bash
intitle:"index of" "parent directory"
intitle:"index of" ".git"
intitle:"index of" "backup"
intitle:"index of" "/admin"
intitle:"index of" "wp-content"
intitle:"index of" ".env"
```

> [!tip] Hacking Note `intitle:"index of"` trova directory listing aperte — server mal configurati che mostrano il contenuto delle cartelle come se fosse un filesystem. Spesso contengono backup, file di configurazione, database dump.

---

### 🌐 Web Server Detection

```bash
intitle:"Apache HTTP Server" intitle:"documentation"
"Apache/2.4.49" inurl:cgi-bin           # versione vulnerabile CVE-2021-41773
intitle:"IIS Windows Server"
"Microsoft-IIS/6.0" intitle:"Under Construction"
```

---

### ⚠️ Vulnerable Files

```bash
inurl:"wp-config.php" filetype:txt      # WordPress config esposta
inurl:".git" intitle:"index of"         # repository Git esposto
inurl:"configuration.php" filetype:php
inurl:"config.php" intext:"password"
inurl:"/.env" intext:"DB_PASSWORD"
```

> [!warning] Un file `.env` esposto contiene spesso `DB_PASSWORD`, `SECRET_KEY`, `API_KEY` e credenziali cloud — uno dei leak più devastanti e comuni.

---

### 🔐 Files Containing Passwords

```bash
filetype:txt intext:"password"
filetype:log intext:"password"
filetype:sql intext:"password" intext:"INSERT INTO"
filetype:bak inurl:"config"
filetype:xml intext:"password"
inurl:"credentials" filetype:txt
"index of" ".htpasswd"
```

---

### ❌ Error Messages — Info Leakage

```bash
intext:"Warning: mysql_connect()" filetype:php
intext:"Fatal error: Call to undefined function"
intext:"ORA-12541" intext:"TNS:no listener"       # Oracle DB error
intext:"Microsoft OLE DB Provider for SQL Server"
intext:"PostgreSQL query failed"
intext:"supplied argument is not a valid MySQL"
```

> [!tip] Hacking Note I messaggi di errore rivelano spesso il tipo di database, la versione, percorsi interni e talvolta query SQL — informazioni preziose per pianificare un attacco SQLi.

---

### 🔑 Login Portals — Pannelli Esposti

```bash
intitle:"Login" inurl:"/admin"
intitle:"Router login" inurl:"/login.cgi"
intitle:"Cisco" inurl:"/exec/show"
inurl:"/wp-admin/login" site:target.com
intitle:"Webmin" inurl:10000
intitle:"Outlook Web App" inurl:"/owa/auth"
intitle:"GlobalProtect" inurl:"/global-protect/login"    # VPN Palo Alto
intitle:"Citrix Gateway"
```

---

### 📷 Various Online Devices — IoT

```bash
inurl:"/view/index.shtml"                    # webcam Axis
intitle:"webcamXP" inurl:8080
inurl:"/mjpg/video.mjpg"                     # stream MJPEG
intitle:"Network Camera" inurl:"/eng/main"
inurl:":10000" intitle:"Webmin"
intitle:"SCADA" inurl:"/login"               # sistemi industriali
intitle:"Hikvision" inurl:"/doc/page/login"  # telecamere Hikvision
```

---

### 📊 Juicy Info — Documenti Sensibili

```bash
filetype:xls intext:"username password"
filetype:pdf "confidential" site:gov.it
filetype:doc "internal use only"
filetype:xlsx intext:"SSN" OR intext:"social security"
filetype:ppt "company confidential"
```

---

## 🔧 Usare la GHDB — Workflow

### 1. Consulta il sito direttamente

```
https://www.exploit-db.com/google-hacking-database
```

Filtra per categoria → copia il dork → incollalo su Google aggiungendo `site:target.com`

### 2. Su Google — aggiungere il target

```bash
# Dork generico dal GHDB
intitle:"index of" ".env"

# Applicato a un target specifico
intitle:"index of" ".env" site:target.com

# Su tutto il web (ricerca massiva)
intitle:"index of" ".env" -site:github.com
```

### 3. Con altri motori — GHDB non è solo Google

La GHDB include dork anche per:

- **Bing** → `site:target.com filetype:env`
- **GitHub** → `filename:.env DB_PASSWORD`
- **Shodan** → integrazione diretta con query specifiche

---

## 🔗 GitHub Dorks — Bonus

GitHub è una miniera d'oro per credenziali dimenticate nel codice:

```bash
# Su GitHub direttamente
filename:.env DB_PASSWORD
filename:config.php db_password
extension:sql "INSERT INTO" password
filename:id_rsa PRIVATE KEY
"api_key" "secret" language:python
"AWS_SECRET_ACCESS_KEY"
"-----BEGIN RSA PRIVATE KEY-----"
```

> [!warning] Sviluppatori che committano credenziali per sbaglio su repository pubblici è **uno dei leak più comuni in assoluto**. Anche se il commit viene rimosso, GitHub mantiene la storia — ed è comunque indicizzata da tool come `trufflehog` e `gitleaks`.

---

## 🛡️ Come Difendersi dai Google Dork

```bash
# robots.txt — dice ai crawler cosa non indicizzare
# (non è sicurezza, è solo una convenzione)
User-agent: *
Disallow: /admin/
Disallow: /.env
Disallow: /config/
Disallow: /backup/

# Verifica cosa Google ha indicizzato del tuo sito
site:tuosito.com

# Richiedi la rimozione di URL sensibili
https://search.google.com/search-console/remove-outdated-content
```

> [!tip] `robots.txt` non è sicurezza — è solo una richiesta educata ai crawler. Un attaccante lo legge per primo proprio per capire **cosa l'amministratore vuole nascondere**.

---

## 🗺️ GHDB nel Workflow di Reconnaissance

```
Footprinting passivo
        │
        ├── crt.sh          → sottodomini
        ├── Shodan          → dispositivi e servizi esposti
        ├── GHDB            → file e directory sensibili via Google
        │       │
        │       ├── filetype:env    → credenziali
        │       ├── intitle:index   → directory listing
        │       └── inurl:admin     → pannelli di amministrazione
        └── WiGLE           → reti Wi-Fi
```

---

## 🔗 Command Cheat Sheet

```bash
# Operatori base
site:target.com                          # limita al dominio
intitle:"testo"                          # nel titolo
inurl:"/admin"                           # nell'URL
intext:"password"                        # nel corpo
filetype:pdf                             # tipo di file
"stringa esatta"                         # match esatto
-parola                                  # escludi

# Dork ad alto impatto
intitle:"index of" ".env"               # file .env esposti
filetype:sql intext:"password"          # dump database
inurl:"wp-config.php" filetype:txt      # config WordPress
intitle:"index of" ".git"              # repository Git esposti
filetype:log intext:"password"          # log con credenziali
inurl:"/phpmyadmin/" intitle:"phpMyAdmin" # phpMyAdmin esposto
intitle:"Router" inurl:"/login.cgi"     # router esposti
```

---

## 🔗 Related Notes

- [[Shodan]]
- [[Nmap]]
- [[Enumeration & Footprinting]]
- [[Privilege Escalation Techniques]]
- [[Finding_Files]]

---

_Fonte: https://www.exploit-db.com/google-hacking-database — OffSec · Johnny Long, "Google Hacking for Penetration Testers" · Linux Basics for Hacking — OccupyTheWeb_