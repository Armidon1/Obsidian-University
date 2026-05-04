---

Tipo: Tool / Web Enumeration Categoria: Directory Busting / DNS / VHost tags:

- tool
- gobuster
- web-enumeration
- directory-busting
- dns-enumeration
- vhost
- fuzzing

---

# 🔍 gobuster

> [!info] Cos'è `gobuster` è un tool di enumerazione scritto in Go, veloce e multi-modalità. È lo strumento standard per il directory busting in CTF e pentest — trova file e directory nascosti su web server, enumera sottodomini DNS e virtual host. Quasi sempre è la prima cosa da lanciare dopo aver trovato una porta 80 o 443 aperta.

---

## 📦 Installazione

```bash
# Debian / Kali / Ubuntu (pre-installato su Kali)
sudo apt install gobuster

# Verifica versione
gobuster version
```

---

## 🗂️ Modalità disponibili

|Modalità|Comando|Uso|
|---|---|---|
|**dir**|`gobuster dir`|Directory e file su web server|
|**dns**|`gobuster dns`|Sottodomini DNS|
|**vhost**|`gobuster vhost`|Virtual host (Host header fuzzing)|
|**fuzz**|`gobuster fuzz`|Fuzzing generico (parametri, path)|
|**s3**|`gobuster s3`|Bucket AWS S3 pubblici|
|**gcs**|`gobuster gcs`|Bucket Google Cloud Storage|

---

## 🚀 Modalità dir — Directory Busting

La modalità più usata — trova file e directory su un web server.

### Sintassi base

```bash
gobuster dir -u <URL> -w <wordlist>
```

### Esempi pratici

```bash
# Base — directory su HTTP
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Con estensioni di file — essenziale per trovare script e config
gobuster dir -u http://<IP> -w <wordlist> -x php,html,txt,bak

# HTTPS — ignora certificato non valido
gobuster dir -u https://<IP> -w <wordlist> -k

# Più thread — più veloce (default: 10)
gobuster dir -u http://<IP> -w <wordlist> -t 50

# Salva output su file
gobuster dir -u http://<IP> -w <wordlist> -o dir_results.txt

# Con subdirectory specifica
gobuster dir -u http://<IP>/admin -w <wordlist> -x php,html
```

### Switch completi — modalità dir

|Switch|Descrizione|
|---|---|
|`-u <URL>`|URL target (obbligatorio)|
|`-w <file>`|Wordlist (obbligatorio)|
|`-x <ext>`|Estensioni da testare (es. `php,html,txt`)|
|`-t <n>`|Thread paralleli (default: 10)|
|`-o <file>`|Salva output su file|
|`-k`|Ignora errori certificato SSL|
|`-s <codici>`|Mostra solo questi codici HTTP (es. `200,301`)|
|`-b <codici>`|Escludi questi codici HTTP (es. `404,403`)|
|`-r`|Segui redirect (301, 302)|
|`-e`|Stampa URL completo nel risultato|
|`-v`|Verbose — mostra anche i path non trovati|
|`-q`|Quiet — niente banner, solo risultati|
|`-c <cookie>`|Cookie da includere nelle richieste|
|`-H <header>`|Header custom (es. `"Authorization: Bearer token"`)|
|`-U <user>`|Username per HTTP Basic Auth|
|`-P <pass>`|Password per HTTP Basic Auth|
|`-a <agent>`|User-Agent custom|
|`--timeout`|Timeout per richiesta (default: 10s)|
|`--delay`|Pausa tra richieste (es. `100ms`)|
|`--no-error`|Non mostrare errori di connessione|

---

## 🚀 Modalità dns — Subdomain Enumeration

Trova sottodomini validi di un dominio target.

```bash
# Base
gobuster dns -d <dominio.com> -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# Mostra anche gli IP risolti
gobuster dns -d <dominio.com> -w <wordlist> -i

# Con resolver DNS custom
gobuster dns -d <dominio.com> -w <wordlist> -r 8.8.8.8

# Output su file
gobuster dns -d <dominio.com> -w <wordlist> -o dns_results.txt
```

### Switch — modalità dns

|Switch|Descrizione|
|---|---|
|`-d <dominio>`|Dominio target (obbligatorio)|
|`-w <file>`|Wordlist (obbligatorio)|
|`-i`|Mostra IP dei sottodomini trovati|
|`-r <resolver>`|DNS resolver custom|
|`-t <n>`|Thread paralleli|
|`--wildcard`|Forza la scansione anche se c'è wildcard DNS|

---

## 🚀 Modalità vhost — Virtual Host Enumeration

Trova virtual host mandando richieste con header `Host: FUZZ.<dominio>`. Utile quando più siti girano sullo stesso IP.

```bash
# Base
gobuster vhost -u http://<IP> -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# Con dominio esplicito (aggiunge automaticamente il suffisso)
gobuster vhost -u http://<IP> -w <wordlist> --append-domain -d <dominio.com>

# Escludi risposte con dimensione specifica (filtra falsi positivi)
gobuster vhost -u http://<IP> -w <wordlist> --exclude-length 1234

# Ignora SSL
gobuster vhost -u https://<IP> -w <wordlist> -k
```

### Switch — modalità vhost

|Switch|Descrizione|
|---|---|
|`-u <URL>`|URL target (obbligatorio)|
|`-w <file>`|Wordlist (obbligatorio)|
|`--append-domain`|Aggiunge il dominio base al FUZZ|
|`-d <dominio>`|Dominio base da appendere|
|`--exclude-length`|Esclude risposte di questa dimensione|
|`-k`|Ignora errori SSL|

---

## 📂 Wordlist consigliate

### Per directory (modalità dir)

|Wordlist|Percorso|Quando usarla|
|---|---|---|
|`common.txt`|`/usr/share/seclists/Discovery/Web-Content/common.txt`|Prima passata veloce|
|`directory-list-2.3-small.txt`|`/usr/share/wordlists/dirbuster/`|Veloce|
|`directory-list-2.3-medium.txt`|`/usr/share/wordlists/dirbuster/`|✅ Default CTF|
|`directory-list-2.3-big.txt`|`/usr/share/wordlists/dirbuster/`|Quando medium non basta|
|`raft-medium-directories.txt`|`/usr/share/seclists/Discovery/Web-Content/`|Alternativa valida|

### Per subdomain / vhost (modalità dns e vhost)

|Wordlist|Percorso|
|---|---|
|`subdomains-top1million-5000.txt`|`/usr/share/seclists/Discovery/DNS/`|
|`subdomains-top1million-20000.txt`|`/usr/share/seclists/Discovery/DNS/`|

### Estensioni per `-x` in base allo stack

|Stack|Estensioni|
|---|---|
|PHP|`php,php3,php5,phtml,inc`|
|ASP.NET|`asp,aspx,ashx,asmx,config,cs`|
|Java|`jsp,jspx,do,action,xml`|
|Generico|`html,htm,txt,bak,old,zip,sql,log,xml,json`|

---

## 🔄 Flusso tipico in CTF

```bash
# Step 1 — passata veloce per vedere subito cosa c'è
gobuster dir -u http://<IP> \
  -w /usr/share/seclists/Discovery/Web-Content/common.txt \
  -t 50 -q

# Step 2 — passata più profonda con estensioni (basata sullo stack rilevato con nmap)
gobuster dir -u http://<IP> \
  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
  -x php,html,txt,bak \
  -t 50 \
  -o gobuster_medium.txt

# Step 3 — se trovi una cartella interessante, approfondisci
gobuster dir -u http://<IP>/secret \
  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
  -x php,html \
  -t 30

# Step 4 — se c'è un dominio o un virtual host
gobuster vhost -u http://<IP> \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  --append-domain \
  -t 30
```

---

## 💡 Tips & tricks

> [!tip] Estensioni giuste = metà del lavoro Fare gobuster senza `-x` trova solo directory. Aggiungere le estensioni corrette in base allo stack (rilevato da nmap o Wappalyzer) è spesso la differenza tra trovare e non trovare la flag.

> [!tip] Aumenta i thread con cautela Il default è 10 thread — in CTF puoi tranquillamente andare a 50-100. In ambienti reali stai attento: troppi thread possono triggerare rate limiting o IDS, o mettere down servizi fragili.

> [!tip] Guarda i codici 403 Un 403 Forbidden significa che la directory esiste ma non hai accesso — potrebbe essere un target interessante per bypass (`/.htaccess`, `../`, encoding). Non ignorarla come un semplice 404.

> [!tip] Aggiungi `/etc/hosts` per i vhost Se gobuster vhost trova un virtual host tipo `dev.macchina.htb`, aggiungilo al tuo `/etc/hosts` prima di navigarci:
> 
> ```bash
> echo "<IP> dev.macchina.htb" | sudo tee -a /etc/hosts
> ```

---

## 🐛 Errori comuni e soluzioni

|Errore|Causa|Soluzione|
|---|---|---|
|`Error: error on running gobuster: unable to connect`|IP/URL errato o porta chiusa|Verificare con nmap e curl|
|Risultati tutti 200|Server restituisce 200 anche per 404|Usare ffuf con `-fs` per filtrare|
|Troppo lento|Thread troppo bassi|Aumentare `-t` (es. `-t 50`)|
|Troppi falsi positivi|Wildcard DNS abilitato|Aggiungere `--wildcard` in modalità dns|
|Certificato SSL rifiutato|Certificato self-signed|Aggiungere `-k`|

---

## 🔄 Confronto gobuster vs ffuf

||gobuster|ffuf|
|---|---|---|
|**Velocità**|⚡ Veloce|⚡⚡ Più veloce|
|**Semplicità**|✅ Più semplice|⚠️ Sintassi con FUZZ|
|**Modalità**|dir, dns, vhost, s3|Tutto tramite FUZZ|
|**Filtri output**|Basici|✅ Avanzati (size, words, lines)|
|**Fuzzing parametri**|❌ Limitato|✅ Ottimo|
|**Uso consigliato**|Directory, DNS, VHost|Fuzzing avanzato, parametri POST/GET|

---

## 🧪 Visto in azione

|Macchina|Piattaforma|Comando usato|
|---|---|---|
|_(aggiorna quando usi il tool)_|HackTheBox||

---

## 🔗 Riferimenti

- [gobuster — GitHub](https://github.com/OJ/gobuster)
- [SecLists — GitHub](https://github.com/danielmiessler/SecLists)
- [HackTricks — Web Enumeration](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web)
- [[Tool/ffuf|ffuf]] — alternativa più flessibile per fuzzing avanzato
- [[Tool/DirBuster|DirBuster]] — il predecessore con GUI
- [[Tool/nmap|nmap]] — usato prima per identificare il web server
- [[Tool/hydra|hydra]] — brute force sui login trovati con gobuster