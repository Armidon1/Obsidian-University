# 📂 DirBuster & Directory Busting

> [!info] Cos'è Il **directory busting** è la tecnica di enumerare file e directory nascoste su un web server inviando richieste HTTP con nomi presi da una wordlist. DirBuster è il tool originale con interfaccia grafica, ma oggi è quasi completamente rimpiazzato da **gobuster** e **ffuf** — più veloci, più flessibili e usabili da CLI.

---

## 🧠 Perché si fa directory busting

I web server spesso espongono percorsi non linkati nelle pagine pubbliche:

- Pannelli di amministrazione (`/admin`, `/dashboard`, `/manager`)
- File di configurazione (`/config.php`, `/.env`, `/web.config`)
- Backup (`/backup.zip`, `/old/`, `/archive/`)
- API endpoints (`/api/v1/users`, `/api/secret`)
- File di sviluppo (`/.git/`, `/README.md`, `/phpinfo.php`)

Senza directory busting questi percorsi restano invisibili.

---

## 🛠️ I tool principali

|Tool|Tipo|Velocità|Flessibilità|Uso consigliato|
|---|---|---|---|---|
|**DirBuster**|GUI (Java)|🐢 Lenta|⭐⭐|Legacy, quasi non più usato|
|**gobuster**|CLI (Go)|⚡ Veloce|⭐⭐⭐|Directory, DNS, vhost — il più usato in CTF|
|**ffuf**|CLI (Go)|⚡⚡ Velocissimo|⭐⭐⭐⭐⭐|Fuzzing avanzato, parametri, header|
|**feroxbuster**|CLI (Rust)|⚡⚡|⭐⭐⭐⭐|Ricorsivo automatico|
|**dirsearch**|CLI (Python)|⚡|⭐⭐⭐|Semplice, buone wordlist integrate|

---

## 📦 Installazione

```bash
# gobuster (consigliato)
sudo apt install gobuster

# ffuf
sudo apt install ffuf

# feroxbuster
sudo apt install feroxbuster

# DirBuster (legacy, GUI)
sudo apt install dirbuster
```

---

## 🚀 gobuster — utilizzo

### Modalità dir (directory busting)

```bash
# Base
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Con estensioni di file
gobuster dir -u http://<IP> -w <wordlist> -x php,html,txt,bak

# Con autenticazione HTTP Basic
gobuster dir -u http://<IP> -w <wordlist> -U admin -P password

# Con cookie di sessione
gobuster dir -u http://<IP> -w <wordlist> -c "session=abc123"

# Con header custom
gobuster dir -u http://<IP> -w <wordlist> -H "Authorization: Bearer token123"

# Ignora SSL non valido (HTTPS)
gobuster dir -u https://<IP> -w <wordlist> -k

# Filtra codici di risposta (default: 200,204,301,302,307,401,403,405,500)
gobuster dir -u http://<IP> -w <wordlist> -s 200,301,302

# Escludi codici di risposta
gobuster dir -u http://<IP> -w <wordlist> -b 404,403

# Thread (default: 10)
gobuster dir -u http://<IP> -w <wordlist> -t 50

# Salva output su file
gobuster dir -u http://<IP> -w <wordlist> -o gobuster_results.txt

# Verbose — mostra anche i 404
gobuster dir -u http://<IP> -w <wordlist> -v
```

### Modalità dns (subdomain enumeration)

```bash
# Enumera sottodomini
gobuster dns -d <dominio.com> -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# Mostra anche gli IP risolti
gobuster dns -d <dominio.com> -w <wordlist> -i
```

### Modalità vhost (virtual host enumeration)

```bash
# Enumera virtual host (Host header fuzzing)
gobuster vhost -u http://<IP> -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain
```

---

## 🚀 ffuf — utilizzo

`ffuf` usa `FUZZ` come placeholder nella URL — più flessibile di gobuster.

### Directory busting

```bash
# Base
ffuf -u http://<IP>/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Con estensioni
ffuf -u http://<IP>/FUZZ -w <wordlist> -e .php,.html,.txt,.bak

# Filtra per codice di risposta
ffuf -u http://<IP>/FUZZ -w <wordlist> -mc 200,301,302

# Filtra per dimensione risposta (esclude 404 con size costante)
ffuf -u http://<IP>/FUZZ -w <wordlist> -fs 1234

# Thread veloci
ffuf -u http://<IP>/FUZZ -w <wordlist> -t 100

# Output su file
ffuf -u http://<IP>/FUZZ -w <wordlist> -o ffuf_results.json -of json
```

### Subdomain / VHost fuzzing

```bash
# Subdomain
ffuf -u http://FUZZ.<dominio> -w <wordlist> -mc 200

# VHost (Host header)
ffuf -u http://<IP> -H "Host: FUZZ.<dominio>" -w <wordlist> -fs <size_default>
```

### Fuzzing parametri GET

```bash
# Trova parametri nascosti
ffuf -u http://<IP>/page.php?FUZZ=test -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -fs <size_default>
```

### Fuzzing parametri POST

```bash
ffuf -u http://<IP>/login -X POST -d "username=admin&password=FUZZ" -w rockyou.txt -mc 200
```

---

## 📂 Wordlist consigliate

### Per directory busting

|Wordlist|Dimensione|Quando usarla|
|---|---|---|
|`dirbuster/directory-list-2.3-small.txt`|87K|Scansione veloce / prima passata|
|`dirbuster/directory-list-2.3-medium.txt`|220K|✅ Default per CTF|
|`dirbuster/directory-list-2.3-big.txt`|1.2M|Quando medium non basta|
|`seclists/Discovery/Web-Content/common.txt`|4.7K|Velocissima, file comuni|
|`seclists/Discovery/Web-Content/raft-medium-directories.txt`|30K|Buon compromesso|

### Per file specifici

|Wordlist|Uso|
|---|---|
|`seclists/Discovery/Web-Content/raft-medium-files.txt`|File generici|
|`seclists/Discovery/Web-Content/CGI-Map.txt`|CGI scripts|
|`seclists/Discovery/Web-Content/PHP.fuzz.txt`|File PHP|

### Per subdomain

|Wordlist|Dimensione|
|---|---|
|`seclists/Discovery/DNS/subdomains-top1million-5000.txt`|5K — veloce|
|`seclists/Discovery/DNS/subdomains-top1million-20000.txt`|20K — bilanciata|

```bash
# Percorso base wordlist su Kali
ls /usr/share/wordlists/dirbuster/
ls /usr/share/seclists/Discovery/Web-Content/

# Installare SecLists se non presente
sudo apt install seclists
```

---

## 🔄 Flusso tipico di web enumeration

```bash
# 1. Prima passata veloce
gobuster dir -u http://<IP> -w /usr/share/seclists/Discovery/Web-Content/common.txt -t 50

# 2. Passata più profonda con estensioni
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,bak -t 50

# 3. Se trovi una sottocartella interessante, scansiona ricorsivamente
gobuster dir -u http://<IP>/admin -w <wordlist> -x php,html -t 50

# 4. Controlla anche subdomain / vhost se c'è un dominio
gobuster dns -d <dominio> -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

---

## 💡 Tips & tricks

> [!tip] Scegliere le estensioni giuste Le estensioni da testare dipendono dallo stack tecnologico rilevato da nmap o Wappalyzer:
> 
> - PHP → `-x php,php3,php5,phtml`
> - ASP.NET → `-x asp,aspx,config`
> - Java → `-x jsp,do,action`
> - Generico → `-x html,txt,bak,old,zip`

> [!tip] Filtrare i falsi positivi con ffuf Molti server restituiscono sempre 200 anche per pagine inesistenti. Fai una prima richiesta su un path sicuramente inesistente, prendi la dimensione della risposta e usala con `-fs` per escluderla:
> 
> ```bash
> curl -s http://<IP>/pagina_che_non_esiste_mai | wc -c   # prendi questo numero
> ffuf -u http://<IP>/FUZZ -w <wordlist> -fs <numero>
> ```

---

## 🧪 Visto in azione

|Macchina|Piattaforma|Comando usato|
|---|---|---|
|_(aggiorna quando usi il tool)_|HackTheBox||

---

## 🔗 Riferimenti

- [gobuster — GitHub](https://github.com/OJ/gobuster)
- [ffuf — GitHub](https://github.com/ffuf/ffuf)
- [SecLists — GitHub](https://github.com/danielmiessler/SecLists)
- [HackTricks — Web Enumeration](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web)
- [[Tool/nmap|nmap]] — usato prima per identificare porte e tecnologie web
- [[Tool/hydra|hydra]] — brute force su login trovati con directory busting