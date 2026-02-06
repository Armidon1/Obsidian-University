# Cross-Origin Resource Sharing (CORS)

**Tag:** #security #web-security #SOP #CORS #headers #mechanism

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

Il **Cross-Origin Resource Sharing (CORS)** è un meccanismo che permette di "rilassare" in modo controllato la **Same Origin Policy ([[SOP]])**. Consente al server di indicare esplicitamente quali origini (domini) diverse dalla propria sono autorizzate a caricare risorse e leggere le risposte tramite script (es. `fetch` o `XHR`).

- **Principio:** Il browser blocca la lettura delle risposte cross-origin a meno che il server non invii specifici header di autorizzazione che corrispondono all'origine della richiesta.
    

---

## ⚙️ Meccanismo di Funzionamento

Il comportamento del CORS varia a seconda del tipo di richiesta.

### 1. Simple Requests

Per richieste semplici (es. GET, HEAD, POST con content-type standard), il browser invia la richiesta direttamente.

- **Richiesta:** Il browser aggiunge automaticamente l'header `Origin: http://sito-richiedente.com`.
    
- **Risposta:** Il server deve includere l'header `Access-Control-Allow-Origin` con il valore dell'origine richiedente o `*` (wildcard).
    
- **Esito:** Se l'header manca o non corrisponde, il browser impedisce al codice JavaScript di leggere la risposta.
    

### 2. Preflight Requests (Non-Simple Requests)

Se la richiesta usa metodi "speciali" (es. PUT, DELETE) o header custom, il browser esegue una verifica preliminare.

1. **Preflight (OPTIONS):** Il browser invia una richiesta HTTP `OPTIONS` per chiedere il permesso. Include header come:
    
    - `Access-Control-Request-Method`: Il metodo che si intende usare (es. PUT).
        
    - `Access-Control-Request-Headers`: Eventuali header custom.
        
2. **Approvazione:** Il server risponde autorizzando i metodi e gli header (`Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`).
    
3. **Actual Request:** Solo se il preflight ha successo, il browser invia la richiesta vera e propria.
    

### 3. Credenziali (Cookies & Auth)

Per inviare cookie o header di autenticazione in una richiesta cross-origin:

- Il client deve impostare `{credentials: "include"}` nella fetch.
    
- Il server **deve** rispondere con `Access-Control-Allow-Credentials: true`.
    
- **Vincolo:** Se si usano credenziali, `Access-Control-Allow-Origin` **non può essere `*`**; deve specificare esattamente l'origine chiamante.
    

---

## 📨 Headers Principali

Le slide elencano i seguenti header chiave per la configurazione CORS:

|**Header (Response)**|**Descrizione**|
|---|---|
|`Access-Control-Allow-Origin`|Specifica le origini permesse (`*`, `null`, o un dominio specifico).|
|`Access-Control-Allow-Methods`|Lista dei metodi HTTP consentiti (es. `GET, POST, PUT`).|
|`Access-Control-Allow-Headers`|Lista degli header HTTP custom consentiti.|
|`Access-Control-Expose-Headers`|Lista degli header della risposta che il codice JavaScript è autorizzato a leggere.|
|`Access-Control-Allow-Credentials`|Booleano (`true`) necessario per accettare cookie/auth.|
|`Access-Control-Max-Age`|Tempo (in secondi) per cui il browser può "cachare" la risposta del preflight.|

---

## ⚠️ Pitfalls e Configurazioni Errate

Configurare male il CORS può vanificare la SOP e introdurre vulnerabilità.

### 1. Broken Origin Validation

Spesso i server non hanno una lista statica di origini, ma generano dinamicamente l'header `Access-Control-Allow-Origin` basandosi su una validazione (spesso errata) dell'header `Origin` in ingresso.

- **Errore Regex:** Una regola come `if ($origin ~ "example.com")` potrebbe matchare accidentalmente domini malevoli come `example.com.evil.com`.
    
- **Reflected Origin:** Una configurazione pigra che copia semplicemente l'header `Origin` della richiesta nella risposta (`Echo Origin`) trasforma la policy in un "allow all", esponendo i dati a chiunque.
    

### 2. The `null` Origin

L'header `Origin` può assumere il valore `null` in casi specifici (redirect cross-site, iframe sandboxed, file locali).

- **Rischio:** Alcuni server mettono in whitelist l'origine `null`. Un attaccante può sfruttare iframe sandboxed per inviare richieste con origine `null` e aggirare i controlli.
    

### 3. Fetch API vs W3C Spec

Le implementazioni moderne dei browser seguono la specifica Fetch API, che consente una **singola origine** nell'header `Access-Control-Allow-Origin` (o `*`), mentre la vecchia specifica W3C permetteva una lista. Questo costringe i server a implementare logiche di validazione dinamica lato backend, aumentando il rischio di errori nel codice.