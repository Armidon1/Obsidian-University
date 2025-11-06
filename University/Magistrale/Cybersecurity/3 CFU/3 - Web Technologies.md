# Web Technologies

Questi appunti offrono una panoramica completa delle **Tecnologie Web**, partendo dalle fondamenta del modello **client-server** e del protocollo **HTTP/HTTPS**. Spiegano l'anatomia di richieste, risposte e **URL**, e come ispezionarli.

Si passa poi ai **linguaggi** che compongono il web (Frontend e Backend) e all'evoluzione del protocollo (**HTTP/2 e HTTP/3**).

Infine, gli appunti trattano concetti cruciali per le applicazioni moderne, come la gestione dello **stato** (Cookie, Sessioni, Web Storage), la manipolazione del **DOM**, l'autenticazione e l'uso di tool di sicurezza professionali come **Burp Suite**, includendo sfide pratiche per applicare le nozioni apprese.

## Introduction to HTTP
[[HTTP]]

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

HTTP

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
You can see everything in a Network section in the [[3 - Web Technologies#Inspecting the Web with Developer Tools|Inspection Tool of the Browser]]
![[Pasted image 20251105115257.png]]

When the server replies, it also sends a plain-text message:

HTTP

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

### Inspecting the Web with Developer Tools
![[Pasted image 20251105115327.png]]
![[Pasted image 20251105115343.png]]![[Pasted image 20251105115426.png]]![[Pasted image 20251105115437.png]]![[Pasted image 20251105115445.png]]![[Pasted image 20251105115459.png]]![[Pasted image 20251105115520.png]]![[Pasted image 20251105115526.png]]![[Pasted image 20251105115532.png]]

All modern browsers include "Developer Tools" that allow you to inspect and debug web traffic and content.

You can typically access them by pressing **F12** or right-clicking and selecting "Inspect".

- **Network Tab:**
    
    - Shows a complete list of all HTTP requests and responses for a page.
        
    - You can select any request to inspect its **General** info (URL, Method, Status Code), **Request Headers**, and **Response Headers**.
        
    - You can also preview the response body or see which cookies were sent and received.
        
- **Elements Tab:**
    
    - Shows the live **HTML DOM** of the page.
        
    - You can inspect and even **edit the HTML and CSS** locally in your browser.
        
    - **Important:** These edits are **client-side only**. They happen only on your computer and are gone as soon as you refresh the page. This is useful for testing, but it does not change the actual server.
        
- **Application Tab (or Storage):**
    
    - Allows you to inspect various types of client-side storage.
        
    - You can see all **Cookies** for the current domain.
        
    - You can also see **Local Storage**, **Session Storage**, and other storage types.
        
    - You can edit and delete these values to test how the application responds.
        

---

## The Languages of the Web

### Client-Side (Frontend)
```HTML
<html>
	<body>
		<p>hello!</p>
	</body>
</html>
```
```CSS
p{
color: red;
}
```
```JAVASCRIPT
let d = window.document;
let p = d.getElementsByTagName('p')[0];
p.addEventListener('click', function () {
	this.style.color = 'blue';
});
```
These languages run _in the user's browser_.

- **HTML (Hypertext Markup Language):**
    
    - Defines the **structure** and content of the webpage (e.g., headings, paragraphs, images, links).
        
- **CSS (Cascading Style Sheets):**
    
    - Defines the **styling** and presentation of the page (e.g., colors, fonts, layout).
        
- **JavaScript:**
    
    - Adds **dynamic interactivity** and behavior to the page (e.g., reacting to user clicks, validating forms, fetching data from a server).
        

### Server-Side (Backend)

These languages run _on the web server_.

- **Common Languages:** Virtually any language can be used, but the most common are **Python** (with frameworks like Flask/Django), **NodeJS** (JavaScript), **Java**, **C#**, and **PHP**.
    
- **Purpose:** The server-side language is used to implement the core logic of the web application:
    
    - Session management (handling user logins).
        
    - Interaction with the database (reading/writing data).
        
    - Generation of dynamic response pages or API data.
    
    - ...
        

---

### Server-Side Examples

#### Quick and Dirty HTTP Server (Python)

You can start a simple web server from any directory (this is unsafe for production):

Bash

```
> python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

This serves the files from the current directory.

#### PHP (Hypertext Preprocessor)

- A C-like scripting language where HTML and PHP code can be mixed in the same file.
    
- Variable names start with `$`.
    
- The `.` operator is used for string concatenation.
    
- **Superglobal Arrays:** PHP provides global arrays to access request data:
    
    - `$_GET`: Parameters from the URL query string.
        
    - `$_POST`: Parameters from the body of a `POST` request.
        
    - `$_SESSION`: Parameters stored in the user's session.
        

**PHP Example (`index.php`):**

HTML

```
<HTML>
<BODY>
<P><?php echo "Hello " . $_GET["name"]; ?></P>
</BODY>
</HTML>
```

**Request & Response:**

- **Client Request:** `GET /index.php?name=Ugo HTTP/2`
    
- **Server Response (HTML):**
    
    HTML
    
    ```
    <HTML>
    <BODY>
    <P>Hello Ugo</P>
    </BODY>
    </HTML>
    ```
    
![[Pasted image 20251105115848.png]]

You can start a simple PHP server with:

> php -S 0.0.0.0:8000

OUTPUT:![[Pasted image 20251105115925.png]]



#### Python (with Flask framework)

Flask is a popular, lightweight web framework for Python.

**Python Example (`app.py`):**

Python

```
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    # Get the 'name' parameter from the query string
    name = request.args.get('name')
    return "<html>\n<body>\n<p>Hello %s</p></body></html>" % name
```
![[Pasted image 20251105120019.png]]
**Request & Response:** (Same as the PHP example)

You can install and run this server with:

Bash

```
> pip3 install flask
> python3 -m flask run
* Running on http://127.0.0.1:5000/
```

---

### Exposing a Local Server with `ngrok`
![[Pasted image 20251105120121.png]]

How do you make a local server (running on `http://localhost:5000`) reachable from the public internet for testing or demos?

**`ngrok`** is a tool that creates a **secure tunnel** to your localhost.

- It gives you a public, reachable URL (e.g., `https://...ngrok.io`).
    
- It works even if you are behind a NAT or firewall, as it creates an _outbound_ connection.
    
- It provides a web interface to inspect all traffic.
    

**How to use `ngrok`:**

1. Start your local HTTP server on a port (e.g., 5000).
    
2. Download and register `ngrok`.
    
3. Configure your authentication token: `> ngrok authtoken <your_token>`
    
4. Run `ngrok` to point to your local port: `> ngrok http 5000`
    
5. `ngrok` will give you a public "Forwarding" URL (e.g., `https://2781-151-31-172-3.ngrok.io`) that you can share.
    

---

### Training Challenge #12: Ping Pong!

- **URL:** `https://training12.webhack.it`
    
- **Description:** The page asks for a URL (from `ngrok.io`) that serves a page containing a specific piece of text.
    
- **Solution:** This challenge requires you to use the skills from the previous slides:
    
    1. Create a simple web server (like the Python/Flask or PHP example).
        
    2. Modify it to serve the _exact_ string of text requested by the challenge.
        
    3. Run the server locally.
        
    4. Use `ngrok` to get a public URL for your local server.
        
    5. Submit your `ngrok` URL to the challenge page.
        

---

## HTTP/2 and HTTP/3

### HTTP/2 (RFC 7540)

HTTP/2 is a major revision of HTTP, derived from Google's experimental SPDY protocol.

**Main Goals:**

- **High-level compatibility:** Maintain the same methods (`GET`, `POST`), status codes, and headers. Web applications don't need to change.
    
- **Decrease latency (improve page speed)** through:
    
    - **Header compression** (to reduce request size).
        
    - **Server Push** (allowing the server to send resources _before_ the client asks for them).
        
    - **Multiplexing** multiple requests over a single TCP connection.
        
    - Fixing the **head-of-line blocking (HOL)** problem.
        

Head-of-Line (HOL) Blocking in HTTP/1.x

In HTTP/1.1, a client can send multiple requests over one TCP connection (pipelining), but it must wait for the responses in the same order.

- **Problem:** If Request A is slow, it blocks Request B and Request C, even if they are ready on the server.
    
- This was so problematic that modern browsers disable pipelining and instead open multiple parallel TCP connections (e.g., 6-8) to a domain.
    

**HTTP/2 Key Ideas:**

- **Binary Protocol:** HTTP/2 is a binary protocol, not text-based like HTTP/1.1. This is more efficient to parse.
    
- **Frames, Messages, and Streams:**
    
    - **Frame:** The smallest unit of communication (e.g., a `HEADERS` frame, a `DATA` frame).
        
    - **Message:** A sequence of frames (e.g., one request or one response).
        
    - **Stream:** A bidirectional flow of messages.
        
- **Multiplexing:** The client and server can send frames for _multiple streams_ (e.g., streams 1, 3, and 5) over a _single TCP connection_ at the same time. This solves HOL blocking at the application layer: a slow response in stream 1 no longer blocks a fast response in stream 3.
    

### HTTP/3 and QUIC

- **Problem:** HTTP/2 solved HOL blocking at the _application_ layer, but it still exists at the _transport_ (TCP) layer. If a single TCP packet is lost, the entire TCP connection (and _all_ streams on it) must wait for that packet to be retransmitted.
    
- **HTTP/3** is the third revision, built on a new transport protocol called **QUIC**.
    
- **QUIC (Quick UDP Internet Connections):**
    
    - **Switches from TCP to UDP:** This is the key change. By using UDP, QUIC avoids the TCP HOL blocking problem. If a packet for stream 1 is lost, only stream 1 waits; streams 3 and 5 continue unaffected.
        
    - **Reliability:** QUIC re-implements reliability (error recovery, retransmissions) on top of UDP.
        
    - **Faster Handshake:** QUIC integrates the TLS (encryption) handshake with the connection handshake, reducing setup latency.
        

---

## Cookies and State Management

### HTTP(S) Sessions

- **Problem:** HTTP is stateless, but applications need to track users (e.g., "who is logged in?").
    
- **Solution:** The **session** concept.
    
    1. A user logs in.
        
    2. The server generates a unique **Session ID** (a random token) and stores it in its session database.
        
    3. The server sends this Session ID back to the client.
        
    4. The client attaches this Session ID to every subsequent request.
        
    5. The server uses the ID to look up the user's data.
        
- **Security Risk:** If an attacker steals a user's session token, they can hijack the session and impersonate that user.
    

### Cookies

Sessions are typically implemented using **cookies**.

- A cookie is a small piece of data that the server asks the browser to store.
    
- The browser automatically attaches the cookie to all future requests _to the same website_.
    

**Cookie Flow:**

1. **Client:** `POST /login` with username/password.
    
2. Server: Validates credentials, creates a session, and replies:
    
    200 OK
    
    Set-Cookie: session=XYZ; Secure; HttpOnly
    
3. **Client:** Stores the cookie `session=XYZ`.
    
4. Client: GET /reserved
    
    Cookie: session=XYZ (browser attaches it automatically)
    
5. **Server:** Sees `session=XYZ`, looks up the session, and serves the reserved page.
    

A cookie is identified by the triplet (`name`, `domain`, `path`).

### Cookies in Practice

#### Client-Side (JavaScript)

- Set a cookie:
    
    document.cookie = "username=John Doe; expires=Thu, 18 Dec 2023 12:00:00 UTC; path=/";
    
- Read cookies:
    
    let x = document.cookie; (Returns a single string of all cookies)
    
- Delete a cookie:
    
    Set its expiration date to a date in the past.
    
    document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    

#### Server-Side (PHP)

- Set a cookie:
    
    setcookie("user", "John Doe", time()+(86400*30), "/");
    
- Read a cookie:
    
    echo $_COOKIE["user"];
    
- Delete a cookie:
    
    setcookie("user", "", time() - 3600);
    

### Cookie Attributes and Security

When a server sets a cookie, it can add attributes to control its behavior:

- **`Expires` / `Max-Age`:** Defines when the cookie should be deleted. If omitted, it's a **session cookie** and is deleted when the browser closes.
    
- **`Domain` / `Path`:** Scopes the cookie to a specific domain and path.
    
- **`Secure`:** **(Security)** If this flag is present, the browser will _only_ send the cookie over an HTTPS connection.
    
- **`HttpOnly`:** **(Security)** This is a crucial flag. It prevents client-side JavaScript (`document.cookie`) from accessing the cookie. This is a primary defense against **Cross-Site Scripting (XSS)** attacks that try to steal session cookies.
    
- **`SameSite` (Strict/Lax/None):** **(Security)** A modern attribute that helps prevent **Cross-Site Request Forgery (CSRF)** attacks by controlling whether a cookie is sent with cross-site requests.
    

### What are Cookies used for?

1. **Authentication:** The most common use. The cookie (session token) proves the client has authenticated.
    
2. **Personalization:** Helps the website remember user preferences (e.g., theme, language).
    
3. **Tracking:** Follows a user's behavior, often across different sites.
    

**Third-Party Cookies**

- When a page hosts content from _other_ web servers (e.g., an ad, an analytics script), those servers can also set cookies. These are **third-party cookies**.
    
- Ad organizations use these to track users across _all_ sites that embed their scripts, building a detailed profile of browsing behavior.
    
- This is a major privacy concern and is the reason for **cookie banners** and laws like the EU's **GDPR**.
    

---

## Web Storage (DOM Storage)

Modern browsers provide another way for web apps to store key-value pairs on the client, separate from cookies.

- **Session Storage:** Kept _only for the current session_. Data is isolated per-tab and is deleted when the tab is closed.
    
- **Local Storage:** Permanent storage that persists across sessions (even after the browser is restarted). Data is shared between all tabs from the same origin.
    

**Properties:**

- Keys and values can only be strings.
    
- Maximum size is much larger than cookies (typically 5MB).
    
- Storage is **NOT encrypted** on disk.
    

### Cookie vs. Web Storage

|**Feature**|**Cookies**|**Web Storage (Local/Session)**|
|---|---|---|
|**Server Access**|**Sent to server with every request.**|**Client-side only.** Not sent to server unless manually added by JS.|
|**Capacity**|4KB|5MB+|
|**API**|Old, cumbersome (`document.cookie`)|Modern, simple (`.setItem()`, `.getItem()`)|
|**Concurrency**|Not well-defined (multiple tabs)|Uses database transactions|

**Web Storage in Practice (JavaScript):**

JavaScript

```
// Set data
localStorage.setItem("lastname", "Smith");

// Get data
console.log(localStorage.getItem("lastname"));

// Remove data
localStorage.removeItem("lastname");

// The API for sessionStorage is identical
sessionStorage.setItem("user", "Alice");
```

---

## Document Object Model (DOM)

The **DOM** is a cross-platform and language-independent interface that treats an HTML or XML document as a **tree structure**.

- Each node in the tree is an object representing a part of the document (e.g., an element, an attribute, or text).
    
- The DOM is the **in-memory representation** of the page.
    
- **JavaScript** can be used to easily modify the page _after_ it has loaded by modifying the DOM. When the DOM is changed, the browser automatically re-renders the page to reflect the changes.
    

### HTML DOM in Practice (JavaScript)

- **Finding elements:**
    
    - `document.getElementById(id)`
        
    - `document.getElementsByTagName(name)`
        
    - `document.getElementsByClassName(name)`
        
- **Modifying elements:**
    
    - `element.innerHTML = "New content"` (Changes the content inside an element)
        
    - `element.attribute = "new value"` (Changes an attribute, e.g., `img.src = "new.jpg"`)
        
    - `element.style.property = "new style"` (Changes a CSS property, e.g., `el.style.color = "red"`)
        
- **Changing the tree structure:**
    
    - `document.createElement(tagName)`
        
    - `element.appendChild(newElement)`
        
    - `element.removeChild(childElement)`
        

---

## Modern Web Applications

### Old Approach: Server-Side Rendering (SSR)

In the "old" approach, the server does most of the work.

- The client requests a page.
    
- The server (e.g., PHP, Django) generates the _entire_ HTML for that page.
    
- The server sends the "full page" back.
    
- The browser's only job is to render it. A minimal amount of JS is used for small effects.
    
- **Pros:** Simple logic; client is just a "viewer".
    
- **Cons:** Heavy load on the server; hard to scale; every click requires a full page reload, which is slow.
    

### Modern Approach: Client-Side Rendering (CSR)

In the "modern" approach, the client does most of the work.

- The server's main job is to provide a **REST API** (which sends data, usually in **JSON** format) and serve static resources (HTML, CSS, JS).
    
- The browser first loads a minimal HTML "shell" and a large JavaScript application.
    
- The JS application then runs, fetches data from the REST API, and _dynamically builds the HTML page_ on the client-side by modifying the DOM.
    
- **Pros:** Server load is low; clear separation between frontend (client) and backend (server); supports other clients (like a mobile app) that can also use the same REST API.
    
- **Cons:** Extremely complex client-side frameworks (e.g., React, Angular, Vue).
    

### Single-Page Application (SPA)

This is the paradigm used by most modern frameworks.

- There is only **one single HTML page** that is ever loaded.
    
- When the user clicks a link, the page **does not reload**.
    
- Instead, client-side JavaScript intercepts the click, performs a REST API request to get new data, and then dynamically modifies the DOM to render the new "page" or content.
    
- **Pros:** Very fast response time and better user experience.
    
- **Cons:** Can be difficult for search engine bots to crawl; complex to manage.
    

### WebSockets

HTTP was not designed for continuous interaction or _push notifications_ (where the server sends data without the client asking).

Modern browsers support **WebSockets**:

- A protocol that provides a **full-duplex, persistent communication channel** over a single TCP connection.
    
- After an initial HTTP handshake to "upgrade" the connection, the client and server can send messages to each other at any time.
    
- This is essential for real-time applications like chat, online gaming, and live data feeds.
    

JavaScript

```
// Create a new WebSocket connection
const socket = new WebSocket('ws://example.com:1234/updates');

// Fired when the connection is opened
socket.onopen = function () {
  // Send data to the server every 50ms
  setInterval(function() {
    if (socket.bufferedAmount == 0)
      socket.send(getUpdateData());
  }, 50);
};

// Fired when data is received from the server
socket.onmessage = function(event) {
  handleUpdateData(event.data);
};
```

---

## Web Authentication

### HTTP Basic Authentication (RFC 7617)

A simple authentication scheme built into HTTP.

1. **Client:** `GET / HTTP/1.1`
    
2. Server: HTTP/1.1 401 Unauthorized
    
    WWW-Authenticate: Basic realm="My Site"
    
3. Client: The browser shows a native username/password popup. The client then re-sends the request with an Authorization header.
    
    GET / HTTP/1.1
    
    Authorization: Basic <BASE64(username:password)>
    

- **Flaw:** This sends the username and password on _every request_, encoded in **Base64** (which is easily reversible, it is **not encryption**). It is only secure when used over HTTPS.
    

### HTTP Digest Authentication (RFC 7616)

A more complex scheme designed to avoid sending the password in clear text.

1. **Client:** `GET / HTTP/1.1`
    
2. Server: HTTP/1.1 401 Unauthorized
    
    WWW-Authenticate: Digest realm="...", nonce="...", ...
    
    (The server sends a nonce, a unique one-time value).
    
3. Client: The browser shows a popup. It then calculates a digest (a hash) based on the username, password, realm, nonce, and other values.
    
    GET / HTTP/1.1
    
    Authorization: Digest username="...", nonce="...", response="<\digest>", ...
    

- This is a **challenge-response** protocol. It's more secure than Basic but is now largely obsolete in favor of cookie-based sessions.
    

### OAuth and Single Sign On (SSO)

OAuth is a standard for **authorization and delegation**. It allows a user to grant a third-party application limited access to their resources on another server, _without_ giving that application their password.

**Roles:**

- **Client:** The application you are trying to use (e.g., a "music.com" website).
    
- **Resource Server:** The server that has your protected data (e.g., your Google Calendar).
    
- **Authorization Server / IdP (Identity Provider):** The server that you trust with your identity (e.g., `google.com`).
    

**Flow:**

1. The **Client** ("music.com") asks the **Authorization Server** ("Google") for authorization.
    
2. The user is redirected to Google, logs in, and "grants" permission.
    
3. The Authorization Server gives the Client an **authorization grant**.
    
4. The Client exchanges this grant for an **access token**.
    
5. The Client uses this **access token** to request the protected resource from the **Resource Server** ("Google Calendar").
    
6. The Resource Server validates the token and, if valid, returns the resource.
    

---

## Burp Suite

### What is Burp Suite?

- A platform of tools for performing web application security testing, made by **PortSwigger**.
    
- It is the industry-standard tool for web penetration testers.
    
- It is written in Java and has a free **Community Edition**.
    
- Its core function is to act as an **intercepting proxy**. It sits as a "man-in-the-middle" between your browser and the web server, allowing you to inspect and modify all HTTP/HTTPS traffic.
    

**Key Functionalities:**

- **HTTP(S) Interceptor:** Pause, view, and modify requests and responses in real-time.
    
- **HTTP(S) Repeater:** Re-send a single request multiple times with modifications.
    
- **HTTP(S) Intruder:** Automate sending thousands of requests (e.g., for brute-force attacks).
    
- **Decoder/Comparer:** Utilities for transforming data and comparing requests.
    

_(Note: While Burp is a powerful tool, you can accomplish the same things with other open-source tools. It is valuable for learning.)_

**PortSwigger Web Security Academy:**

- A free, online training center from the creators of Burp Suite.
    
- It covers all major web vulnerabilities with high-quality explanations and interactive labs.
    
- Reference: `https://portswigger.net/web-security`
    

### Burp Suite Tutorial

1. **Start Burp:** Open Burp and select a "Temporary project". Use the "Burp defaults".
    
2. **Go to Proxy Tab:** Navigate to the `Proxy` > `Intercept` tab.
    
3. **Open Browser:** Click **"Open Browser"**. This launches a pre-configured Chromium browser that is already set up to send its traffic through Burp. _Use this browser for testing._
    
4. **Intercept:** With "Intercept is on", navigate to a webpage in the Burp browser. The request will be "stuck" in Burp.
    
    - You can edit the request (e.g., change the URL or headers) before clicking **Forward**.
        
    - Or you can **Drop** the request entirely.
        
    - This is powerful but slow. Click the "Intercept is on" button to turn it **off**.
        
5. **HTTP History:** Go to the `Proxy` > `HTTP history` tab.
    
    - This tab shows a complete log of all requests and responses that have passed through the proxy.
        
    - You can select any item to inspect the full request and response.
        
6. **Send to Repeater:**
    
    - In the HTTP History, right-click any request and "Send to Repeater".
        
    - Go to the `Repeater` tab.
        
    - Here, you can modify the request (e.g., change the URL, headers, or body) and click **Send** to see the response. This is the most-used feature for testing.
        
7. **Decoder Tab:**
    
    - A simple utility to encode or decode data in various formats (e.g., Base64, URL-encoding, Hashing).
        
8. **Intruder Tab:**
    
    - Used for automated attacks. You can mark "payload positions" in a request (e.g., a password parameter) and have Burp send hundreds of requests, iterating through a list of values (like a password dictionary).
        

---

### Training Challenge #13

- **URL:** `https://training13.webhack.it`
    
- **Description:** A login page that is leaking crucial information.
    
- **Analysis:** Inspecting the page source (either in Dev Tools or Burp) reveals two HTML comments:
    
    1. ``
        
    2. ``
        
- **Solution**:
    
    1. The first comment tells us the username is `demo` and the password is the Base64 encoding of "demo".
        
    2. Use the **Decoder** tab in Burp to find that `base64("demo")` is `ZGVtbw==`.
        
    3. The second comment implies there is a hidden parameter `debug_mode` that should be set to `1`.
        
    4. Go to the login page, type anything, and intercept the `POST` request.
        
    5. Send the request to **Repeater**.
        
    6. In Repeater, modify the request body to be:
        
        user=demo&pass=ZGVtbw=&debug_mode=1
        
    7. Click **Send**. The response will contain the flag.