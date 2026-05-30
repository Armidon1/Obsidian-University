>[!Definizione]
>**HTTP (Hypertext Transfer Protocol)** è un **protocollo di livello applicazione** (Livello 7) che definisce il linguaggio per la comunicazione tra un **client** (come un browser web) e un **server web**.

Le sue caratteristiche chiave sono:

1. **Client-Server Model:** La comunicazione è sempre avviata dal client, che invia una **richiesta** (Request). Il server elabora la richiesta e restituisce una **risposta** (Response).
    
2. **Stateless (Senza Stato):** Questa è la sua proprietà fondamentale. Ogni richiesta è un evento indipendente. Il server **non conserva alcuna memoria** o stato delle richieste precedenti dello stesso client. Per gestire lo stato (come i login), si usano meccanismi esterni come i **Cookie**.
    
3. **Basato su Testo (Plain-Text):** I messaggi di richiesta e risposta (header e body) sono in testo semplice (ASCII), rendendoli leggibili dall'uomo e facili da ispezionare, ma intrinsecamente **non sicuri**.
    

La sua variante sicura, **[[HTTPS]]**, utilizza **[[TLS]] (Transport Layer Security)** per crittografare questa comunicazione.

## Introduction to HTTP

### Anatomy of a Typical Web Application
![[Pasted image 20251105115206.png]]

The web is based on a **client-server model**. A client (like your web browser) requests resources from a server, which processes the request and sends back a response.

A typical flow for a dynamic webpage looks like this:

1. **HTTP Request:** The user's browser (client) requests a webpage.
    
2. **Server Processing:** The web server receives the request. The web application (e.g., written in Python, PHP, or Java) sees that the page needs dynamic content.
    
3. **Database Query:** The application queries a database to get user-specific data (like a user's profile, posts, or shopping cart).
    
4. **Response Generation:** The application uses this data to generate the final HTML page content.
    
5. **HTTP Response:** The server sends the finished HTML page back to the client.
    
6. **Rendering:** The client's browser renders the received HTML and displays the page to the user.
    

---

### Uniform Resource Locator (URL)
![[Pasted image 20251105115221.png]]

URLs are standardized identifiers used to locate resources (like documents, images, or APIs) on the Web.

A URL is composed of several parts:

https://example.com:443/page?name=photo#about

- **Protocol:** `https://`
    
    - The scheme to be used for the connection (e.g., `http`, `https`, `ftp`).
        
- **Hostname:** `example.com`
    
    - The domain name (or IP address) of the server to connect to. for example, if the router doesn't know the IP address of example.com, then it consult the DNS to know his IP address.
        
- **Port:** `:443`
    
    - The specific service port on the server. This is often optional, as protocols have default ports (`80` for HTTP, `443` for HTTPS).
        
- **Path:** `/page`
    
    - The path to the specific resource on the server (e.g., a file or an application endpoint).
        
- **Query String:** `?name=photo`
    
    - An ***optional*** set of key-value pairs passed to the resource, often used for dynamic content. Starts with a `?` and pairs are separated by `&`. These are parameters that the server may consider to find the resource we are asking for.
        
- **Fragment:** `#about`
    
    - An ***optional*** identifier that points to a specific part _within_ the resource. This is processed **client-side only** and is not sent to the server. So we are specifying that we want a specific sub-resource of the resource we are asking for.
        

URL Encoding

Reserved characters (like spaces, /, ?) cannot be used directly in certain parts of a URL. They must be percent-encoded.

- `%20` = `space`
    
- `%2F` = `/`
    
- Example: `https://example.com/page?name=my%20page`
    

### Enhanced edition

![[Pasted image 20260529191527.png]]
![[Pasted image 20260529191533.png]]![[Pasted image 20260529191538.png]]
HTTP request
Structure:
	1 request line (e.g., GET /index.html HTTP/1.1 )
	2 header (HTTP/1.1 MUST contain the Host field – host and
	port number of the requested resource)
	●3 empty line
	●4 message body (optional)
Note:
	●request line and header are terminated by a CRLF (“\r\n”)
	●empty line → CRLF
	usually implementations are flexible (e.g., CR may not be mandatory)


---

### The HTTP Protocol

HTTP (Hypertext Transfer Protocol) defines the structure of the communication (the "language") between a client and a web server.

**Properties:**

- **Stateless:** This is a fundamental concept. The server processes every request independently. It does **not remember** anything about previous requests.
    
    - To create stateful applications (like login sessions), mechanisms like **Cookies** are used to "remind" the server who the user is with each request.
        
- **Not Encrypted:** Standard HTTP is a plain-text protocol. Any intermediary on the network (e.g., on public Wi-Fi) can read and even modify the traffic. This is a major security risk.
    
- **Default Port:** 80
    

### The HTTPS Protocol

HTTPS is the **secure variant** of HTTP. It is not a separate protocol, but rather **HTTP delivered over a TLS connection**.

- **TLS (Transport Layer Security):** The modern, secure protocol that provides encryption for the connection. It is the successor to SSL (Secure Sockets Layer).
    
- **Default Port:** 443
    

**Security Properties:**

- **Confidentiality:** The content of the traffic is encrypted and cannot be inspected by network eavesdroppers.
    
- **Integrity:** The content of the traffic cannot be modified in transit without the client and server noticing (it would break the cryptographic seal).
    
- **Authentication:** The client can verify that it is communicating with the _expected_ server. This is achieved through **digital certificates** issued by a trusted Certificate Authority (CA).
    

---

### HTTP Request
![[Pasted image 20251105115247.png]]

When a client sends a request, it is formatted as a plain-text message:

``` HTTP
POST /login HTTP/2
Host: example.com
User-Agent: Mozilla/5.0 (Macintosh; ...)
Accept: text/html,application/xhtml+xml,...
Content-Type: application/x-www-form-urlencoded
Content-Length: 71
Referer: https://example.com/login

user=ugo&csrf_token=IjljMjlkMDE40DJmZWZIODhf
```

- **Request Line:**
    
    - `POST`: The **HTTP Method** (or "verb").
        
    - `/login`: The **Path** (and optional query string).
        
    - `HTTP/2`: The **HTTP Version**.
        
- **HTTP Headers:**
    
    - Key-value pairs providing metadata about the request.
        
    - `Host`: The _only_ mandatory header in modern HTTP. Specifies the server's hostname.
        
    - `User-Agent`: Identifies the client software (e.g., browser type).
        
    - `Content-Type`: Describes the format of the request body (if one exists).
        
    - `Referer`: The URL of the page that _led_ to this request.
        
- **Blank Line:** A single blank line separates the headers from the body.
    
- **Request Body:**
    
    - An optional body containing data for the server (e.g., form data, JSON). It is empty for `GET` requests.
        

**Common HTTP Methods:**

- **`GET`:** Used to _retrieve_ data. Should have no side effects.
    
- **`POST`:** Used to _submit_ data to a resource, often causing a change in state or side effects (e.g., creating a new user, posting a comment).
    
- **`HEAD`:** Same as `GET`, but the server responds _without_ the response body. Used to check headers (like `Last-Modified`) without downloading the file.
    
- **`PUT`:** Used to _replace_ a resource completely.
    
- **`DELETE`:** Used to _delete_ a resource.
    
- **`OPTIONS`:** Used to ask the server which methods and headers it supports for a resource.
    
- **`PATCH`:** Used to _partially modify_ a resource.
    

### HTTP Response
You can see everything in a Network section in the [[3 - CS - Application Level - Web Technologies#Inspecting the Web with Developer Tools|Inspection Tool of the Browser]]
![[Pasted image 20251105115257.png]]

When the server replies, it also sends a plain-text message:

``` HTTP
HTTP/2 200 OK
Server: nginx
Date: Mon, 22 Feb 2021 15:38:46 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 10459
Set-Cookie: session=apU8ig...; Secure; HttpOnly; Path=/
Strict-Transport-Security: max-age=63072000

<html>
  <body>login successful!</body>
</html>
```

- **Status Line:**
    
    - `HTTP/2`: The **HTTP Version**.
        
    - `200`: The **Status Code**.
        
    - `OK`: The **Reason Phrase** (a human-readable summary of the code).
        
- **HTTP Headers:**
    
    - Key-value pairs providing metadata about the response.
        
    - `Content-Type`: Describes the format of the response body (e.g., `text/html`, `application/json`, `image/png`).
        
    - `Set-Cookie`: Instructs the client to store a cookie.
        
    - `Strict-Transport-Security`: A security header that forces the browser to only use HTTPS.
        
- **Blank Line:** Separates headers from the body.
    
- **Response Body:**
    
    - The actual content (HTML, JSON, image data) that was requested. This is optional (e.g., for a `HEAD` request or a `204 No Content` response).
        

**Common HTTP Status Codes:**

- **`1xx` (Informational):** Request received, continuing process.
    
- **`2xx` (Success):** The action was successfully received, understood, and accepted.
    
    - `200 OK`: Standard success.
        
- **`3xx` (Redirection):** Further action must be taken to complete the request.
    
    - `301 Moved Permanently`: The resource has a new permanent URL.
        
    - `302 Found`: The resource is temporarily at a different URL.
        
- **`4xx` (Client Error):** The request contains bad syntax or cannot be fulfilled.
    
    - `400 Bad Request`: Generic client error.
        
    - `401 Unauthorized`: Authentication is required.
        
    - `403 Forbidden`: The server understood the request but refuses to authorize it.
        
    - `404 Not Found`: The requested resource could not be found.
        
- **`5xx` (Server Error):** The server failed to fulfill an apparently valid request.
    
    - `500 Internal Server Error`: A generic error on the server side.
        

---
## Differenza tra HEAD, GET e POST

Il tuo modello **sull'intento** dei metodi è in realtà corretto. Quello che ti manca è un pezzo diverso: il fatto che GET _può comunque trasportare dei dati_ — solo che li mette in un **posto diverso** rispetto a POST. È questo che le slide stanno mostrando, e che fa sembrare contraddittorio il tuo schema.

## Il malinteso da sciogliere

"GET serve per richiedere risorse" è giusto. Ma _richiedere una risorsa_ non significa "senza dati": la risorsa può essere **parametrizzata**. Quando fai `search.php?q=gatti`, stai ancora **recuperando** una risorsa (i risultati della ricerca) — i parametri descrivono semplicemente _quale_ risorsa o quale versione vuoi. Non stai "inviando roba da salvare", stai dicendo al server _cosa_ restituirti.

Quindi:

- **GET** = "dammi questa risorsa" → i parametri dicono _quale_. (intento: lettura)
- **POST** = "ecco dei dati da elaborare/registrare" → i parametri sono il _payload di un'azione_. (intento: scrittura/azione)
- **HEAD** = come GET ma il server restituisce **solo gli header, niente body** (per sapere se la risorsa esiste, la sua dimensione, la data di modifica, senza scaricarla). Il tuo modello su HEAD era giusto.

## La differenza concreta: _dove_ finiscono i parametri

Questo è il cuore delle due slide:

| |GET|POST|
|---|---|---|
|Dove vanno i parametri|nella **URL** (query string `?var1=a&var2=b`)|nel **body** della richiesta|
|Visibili nell'URL|**Sì**|**No**|
|Finiscono in cronologia, log, header `Referer`, bookmark|**Sì**|**No**|
|Limite di lunghezza|sì (le URL hanno un limite)|praticamente no|
|Intento (spec HTTP)|sicuro, idempotente (non dovrebbe cambiare stato)|non idempotente (cambia stato)|
|Refresh della pagina|innocuo|il browser avvisa ("reinviare i dati?")|

Guarda le slide con questa lente:

- **GET** (slide 1): i parametri sono _attaccati all'URL_ → `GET /submit.php?var1=a&var2=b HTTP/1.1`. Tutto nell'URL, niente body.
- **POST** (slide 2): i parametri stanno _dopo gli header, nel body_ → in fondo vedi `var1=a&var2=b` con `Content-Type: application/x-www-form-urlencoded` e `Content-Length: 13` (sono 13 caratteri). L'URL è pulito.

## Il "Case 2: GET + POST" che ti confonde

Quella slide mostra che i due canali **non si escludono**: una singola richiesta POST può portare parametri in **entrambi** i posti. Nel form:

```html
<form action="submit.php?var3=c&var4=d" method="post">
```

- `var3` e `var4` sono nell'**URL** dell'action → viaggiano nella query string (canale "GET").
- `var1` e `var2` sono i campi del form → viaggiano nel **body** (canale "POST").

Risultato: `POST /test.php?var3=c&var4=d` con `var1=a&var2=b` nel body. Una richiesta, due canali di parametri.

## Perché questo conta per il tuo corso (sicurezza)

La differenza "URL vs body" è esattamente ciò che spiega cose che hai già visto:

- I parametri **GET finiscono nei log del server, nella cronologia e nell'header `Referer`** → per questo dati sensibili (token di sessione, password) **non vanno mai messi in GET**.
- Il **CSRF via `<img>`** funziona _solo_ con GET: `<img src="bank.com/?act=...">` può scatenare una richiesta GET perché i parametri stanno nell'URL. Per fare CSRF su un endpoint POST serve invece un **form auto-inviato via JavaScript**, perché i dati devono stare nel body — è proprio la differenza tra i due scenari della tua nota [[CSRF]].
- La **reflected [[XSS]]** spesso passa per un parametro GET, perché basta un link preparato (`?q=<script>...`) — il payload sta nell'URL, comodo da consegnare in un link di phishing.

In sintesi: il _perché_ esistono (intento) lo avevi capito; il pezzo nuovo è il _dove_ mettono i dati (URL per GET, body per POST), ed è da lì che discendono quasi tutte le conseguenze pratiche e di sicurezza.