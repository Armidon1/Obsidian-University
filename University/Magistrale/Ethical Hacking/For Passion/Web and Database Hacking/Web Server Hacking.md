# Web Server Hacking

> [!info] Nota indice (MOC) Questa è la nota-hub del **livello server** del web hacking. Per il livello applicativo (logica scritta dagli sviluppatori) vedi la nota gemella [[Web Application Hacking]].

## Cos'è

Il **Web Server Hacking** prende di mira il _software del server web e la sua piattaforma_ (IIS, [[Apache]], nginx) e non l'applicazione scritta sopra. Le vulnerabilità nascono quindi dal **server stesso**, dalla sua **configurazione**, dai **contenuti d'esempio** che porta con sé e dalle **estensioni** che ne ampliano le funzioni.

> [!important] La distinzione chiave
> 
> - **Web Server Hacking** → bug del _server / piattaforma_ (questa nota).
> - **Web Application Hacking** → bug del _codice applicativo_ ([[SQL Injection]], [[XSS]], autenticazione…).
> 
> Sono due metà distinte dello stesso capitolo. Molti exploit "server" qui dentro sono storici e patchati: studiali soprattutto per **capire i concetti**, non per memorizzare la sintassi.

## Le 6 aree

Ogni voce ha la sua nota dedicata. Riassunto + esempi-chiave per orientarsi:

### 1. [[Sample Files]]

File e applicazioni **d'esempio** che il server installa per dimostrare le sue funzionalità. Spesso pieni di buchi (lettura di file arbitrari, esposizione di variabili) e dimenticati in produzione.

- _Esempi:_ sample IIS tipo `showcode.asp` / `codebrws.asp`, le cartelle `/iissamples`, `/msadc`.
- _Difesa:_ **rimuovere tutti i file d'esempio** dai server di produzione.

### 2. [[Source Code Disclosure]]

Attacchi che ti restituiscono il **codice sorgente** degli script lato server (ASP, PHP, JSP) invece di farlo eseguire. Espone logica interna, password e stringhe di connessione.

- _Esempi:_ `ASP::$DATA`, bug case-sensitive di Apache su Windows, `+.htr`.
- _Spesso è la **conseguenza** di una [[Canonicalization|canonicalizzazione]]._
- _Difesa:_ patch + tenere gli script **fuori** dalla document root.

### 3. [[Canonicalization]]

Una stessa risorsa è raggiungibile con **più nomi**; la decisione di sicurezza presa sul nome "non canonico" viene aggirata, ma il filesystem risolve comunque il file.

- _Schema universale:_ due componenti interpretano lo **stesso nome** in modo diverso → l'attaccante sfrutta la discrepanza.
- _Esempi:_ `::$DATA`, case-sensitivity di Apache, **Unicode / Double Decode** (worm **Nimda**).
- _Difesa:_ patch, filtraggio input (es. **URLScan**), compartimentazione delle cartelle.

### 4. [[Server Extensions]]

Moduli che ampliano il server (**ISAPI** su IIS, **moduli** Apache, **WebDAV**, FrontPage Server Extensions, librerie SSL). Girano con i privilegi del server → un loro bug è gravissimo.

- _Esempi:_ buffer overflow ISAPI `.printer` / `.ida` (→ **Code Red**), overflow WebDAV `ntdll.dll`, worm **Slapper** su OpenSSL.
- _Difesa:_ **disabilitare le estensioni inutilizzate**, patch costanti.

### 5. [[Input Validation]]

A livello server significa soprattutto **buffer overflow** nel binario del server o nelle sue estensioni, dovuti a input non validato → esecuzione di codice.

- _Esempi:_ overflow `.ida` (**Code Red**), overflow chunked-encoding di Apache.
- _Nota:_ a livello _applicativo_ "input validation" significa invece XSS / SQLi → quella roba sta in [[Web Application Hacking]].
- _Difesa:_ patch + esecuzione con **minimo privilegio**.

### 6. [[DoS]]

Rendere il server **indisponibile**: esaurimento risorse, richieste malformate che lo fanno crashare, connessioni tenute aperte (**Slowloris**), flood di traffico.

- _Difesa:_ rate limiting, patch, protezioni a livello di rete.

## Difese trasversali

Valide per tutta la categoria:

- **Patch management** rigoroso: quasi tutti gli exploit qui sopra erano già corretti dalle patch.
- **Rimuovere** sample file, contenuti demo e default.
- **Minimo privilegio** per il processo del server.
- **Disabilitare** estensioni e moduli non usati.
- **Compartimentare** la struttura delle cartelle (script fuori dalla document root).
- **Filtrare l'input** a monte (es. URLScan strappa caratteri Unicode / doppio-esadecimali).

## Strumenti

- **Scanner di vulnerabilità web server:** [[Nikto]], [[Nessus]].
- **Filtri/hardening:** URLScan (IIS legacy).
- _(Gli strumenti più orientati all'app — Google dorks, crawling, Burp — stanno in [[Web Application Hacking]].)_

## Collegamenti

- ⬆️ Genitore: [[Web Hacking]]
- ↔️ Gemella: [[Web Application Hacking]]
- 📚 Fonte: Hacking Exposed 7, sezione _Web Server Hacking_