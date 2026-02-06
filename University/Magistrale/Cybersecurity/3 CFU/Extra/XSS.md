# Cross-Site Scripting (XSS)

**Tag:** #security #web-security #vulnerability #XSS #javascript

---

## 📝 Definizione

Il **Cross-Site Scripting (XSS)** è una vulnerabilità di _code injection_ in cui un attaccante riesce a iniettare codice JavaScript all'interno delle pagine di un'applicazione web, il quale viene poi eseguito nel browser della vittima.

- **Causa principale:** Sanitizzazione impropria degli input dell'utente prima che questi vengano incorporati nella pagina.
    
- **Obiettivi:** Manipolare i contenuti del sito (DOM), mostrare informazioni false, o esfiltrare dati sensibili come i cookie di sessione.
    

---

## ⚠️ Tipologie di XSS

Le vulnerabilità XSS si classificano principalmente in tre categorie:

### 1. Reflected XSS (Non persistente)

L'applicazione web include i dati provenienti da una richiesta HTTP (es. parametri URL) direttamente nella risposta HTML senza un'adeguata sanitizzazione.

- **Vettore di attacco:** L'utente viene solitamente ingannato (tramite phishing o link malevoli) nel visitare un URL preparato dall'attaccante.
    
- **Esempio:** Un payload inserito in un parametro di ricerca viene riflesso nella pagina dei risultati ("Hai cercato: `<script>...`").
    

### 2. Stored XSS (Persistente)

Il payload malevolo viene inviato al server e **memorizzato permanentemente** (es. in un database, forum, log o commenti).

- **Esecuzione:** Il codice viene eseguito automaticamente dal browser della vittima quando questa carica la pagina contenente il contenuto memorizzato.
    
- **Caratteristica:** Non richiede un'interazione diretta istantanea con l'attaccante.
    

### 3. DOM-based XSS

L'iniezione avviene interamente lato client. I dati controllati dall'attaccante (Sorgente) vengono passati a un _"sink"_ sensibile o a un'API del browser senza sanitizzazione.

- **Sorgenti (Sources):** Elementi controllabili come `location.hash`, `document.referrer`, o `window.name`.
    
- **Sink:** Funzioni che modificano il DOM o eseguono codice, come `innerHTML`, `document.write`, o `eval`.
    
- **Particolarità:** Il payload potrebbe non raggiungere mai il server, rendendo inefficaci i filtri lato server.
    

---

## 🛡️ Prevenzione e Mitigazione

### Input Handling

- **Sanitizzazione e Encoding:** Tutti gli input utente devono essere preprocessati; i caratteri speciali HTML devono essere opportunamente codificati prima dell'inserimento nella pagina.
    
- **Librerie:** Evitare l'escaping manuale. Utilizzare librerie affidabili come **DOMPurify** (per il client-side) o motori di templating (es. Jinja, Smarty) che gestiscono l'escaping automaticamente.
    

### Content Security Policy (CSP)

Un header HTTP (`Content-Security-Policy`) che permette di controllare quali risorse il browser è autorizzato a caricare.

- Può limitare le sorgenti di script (`script-src`), bloccare script inline (`unsafe-inline`) e mitigare l'esecuzione di codice non autorizzato.
    

### Trusted Types

Una API del browser progettata per eliminare il DOM XSS.

- Blocca i sink di iniezione pericolosi (come `innerHTML`) impedendo loro di accettare stringhe semplici; richiede invece oggetti "Trusted" creati tramite policy specifiche nel codice JavaScript.
    

### Cookie Security

- Impostare il flag **HttpOnly** sui cookie impedisce a JavaScript di accedere al loro contenuto (es. `document.cookie`), proteggendo dal furto di sessione in caso di XSS.