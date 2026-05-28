# Web Application Hacking

> [!info] Nota indice (MOC) Questa è la nota-hub del **livello applicativo** del web hacking. Per il livello server (software e piattaforma) vedi la nota gemella [[Web Server Hacking]].

## Cos'è

Il **Web Application Hacking** prende di mira il _codice applicativo_ scritto dagli sviluppatori sopra il server: login, gestione delle sessioni, form, query al database, logica di business. Non è il software del web server a essere difettoso, ma il **modo in cui l'applicazione tratta i dati** che riceve.

> [!important] La distinzione chiave (e perché è il focus del corso)
> 
> - **Web Server Hacking** → bug del _server / piattaforma_ (spesso storici e patchati).
> - **Web Application Hacking** → bug del _codice applicativo_ (questa nota).
> 
> A differenza di molti exploit server, queste vulnerabilità sono **vive e attualissime**: la SQL injection, ad esempio, è ancora oggi tra le cause principali di data breach. Richiedono **analisi più profonda e pazienza**, e meno tool "premi un bottone".

> [!tip] Lo schema universale del livello app **L'applicazione si fida di dati che arrivano dal client e non dovrebbe.** Quasi ogni vulnerabilità qui sotto nasce da input non validato o non codificato correttamente. È il filo conduttore, come la "discrepanza di interpretazione" lo era per la [[Canonicalization]].

## Le aree

Ogni voce ha la sua nota dedicata.

### 1. [[Authentication Attacks]]

Attacchi a **come l'app verifica l'identità**. Credenziali deboli/di default, brute forcing del login, enumerazione degli username, bypass dell'autenticazione.

- _Esempi:_ brute force con [[Web Hacking Tools|THC-Hydra]], messaggi d'errore che rivelano se l'utente esiste.
- _Difesa:_ policy password robuste, **account lockout / rate limiting**, MFA, errori generici ("credenziali non valide").

### 2. [[Session Management]]

Dopo il login l'app ti riconosce tramite un **token di sessione** (cookie). Attacchi: **session hijacking** (rubare il token, spesso via [[XSS]]), **session fixation** (imporre un token noto), token **prevedibili** (analizzabili con il Sequencer di [[Burp Suite]]).

- _Difesa:_ token casuali e lunghi, cookie con flag **HttpOnly / Secure / SameSite**, rigenerare il token al login, timeout di sessione.

### 3. [[Authorization]]

Anche da autenticato: **cosa ti è permesso fare?** Attacchi di **privilege escalation** e **IDOR** (_Insecure Direct Object Reference_: cambi un `id` nell'URL e accedi ai dati di un altro utente), forced browsing.

- _Difesa:_ controlli di autorizzazione **lato server su ogni richiesta**, principio **deny-by-default**.

### 4. [[SQL Injection]]

Inietti SQL tramite input non validato → leggi/modifichi il database, bypassi il login, in casi estremi esegui comandi sul server.

- _Esempi:_ `' OR '1'='1`, UNION-based, **blind** SQLi.
- _Tool:_ **sqlmap** per sfruttarla. _Categoria: input validation attack._
- _Difesa:_ **prepared statements / query parametrizzate**, account DB a minimo privilegio.

### 5. [[XSS]]

_Cross-Site Scripting_: inietti **JavaScript** che gira nel browser di altri utenti. Tipi: **Stored**, **Reflected**, **DOM-based**.

- _Impatto:_ furto dei cookie di sessione (→ [[Session Management|session hijacking]]), defacement, keylogging.
- _Difesa:_ **output encoding** contestuale, **Content Security Policy (CSP)**, validazione input, cookie **HttpOnly**.

### 6. [[CSRF]]

_Cross-Site Request Forgery_: inganni il browser di un utente **già autenticato** facendogli inviare una richiesta indesiderata (es. cambio password) sfruttando la sua sessione attiva.

- _Difesa:_ **token anti-CSRF**, cookie **SameSite**, ri-autenticazione per le azioni sensibili.

## Difese trasversali

Il principio guida è uno: **non fidarsi mai dell'input del client**.

- **Validare e sanitizzare** tutto l'input **lato server** (il controllo client-side si aggira sempre).
- **Output encoding** contestuale (anti-[[XSS]]).
- **Query parametrizzate** per il database (anti-[[SQL Injection]]).
- **Sessioni robuste**: token casuali, cookie sicuri.
- **Autorizzazione server-side** su ogni richiesta, deny-by-default.
- **Difesa in profondità:** WAF, security header (CSP, HSTS), minimo privilegio.

## Strumenti

La metodologia applicativa (vedi [[Web Hacking Tools]]):

- **Discovery:** Google dorks (trovare app e file esposti via query mirate sui motori di ricerca).
- **Mapping:** web crawling (il crawler integrato di [[Burp Suite]] / OWASP ZAP).
- **Testing manuale:** **[[Burp Suite]]** (hub) + OWASP ZAP (free).
- **Exploitation:** **sqlmap** (SQLi), **THC-Hydra** (brute force credenziali).

## Collegamenti

- ⬆️ Genitore: [[Web Hacking]]
- ↔️ Gemella: [[Web Server Hacking]]
- 🛠️ Tool: [[Web Hacking Tools]] · [[Burp Suite]]
- 📚 Fonte: Hacking Exposed 7, sezione _Web Application Hacking_