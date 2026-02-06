# JSON-P (JSON with Padding)

**Tag:** #security #web-security #SOP #JSONP #data-exfiltration #CSP-bypass

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

**JSON-P** è una tecnica storica utilizzata per aggirare le restrizioni della **Same Origin Policy (SOP)** e permettere lo scambio di dati tra domini diversi.

Si basa sul fatto che il tag HTML `<script>` non è soggetto alle restrizioni SOP per il caricamento delle risorse (anche se la lettura del sorgente lo è, l'esecuzione no).

---

## ⚙️ Funzionamento

A differenza di una richiesta AJAX/Fetch standard (che verrebbe bloccata dalla SOP se cross-origin senza [[CORS]]), JSON-P funziona iniettando un tag script:

1. **Richiesta:** Il client crea dinamicamente un tag `<script src="http://api.com?callback=myFunc">`.
    
2. **Risposta (Padding):** Il server risponde non con puro JSON, ma con il codice JSON "impacchettato" (padded) all'interno di una chiamata a funzione JavaScript specificata dal client.
    
    - Esempio risposta: `myFunc({"id": 123, "data": "segreto"});`
        
3. **Esecuzione:** Il browser carica lo script ed esegue immediatamente la funzione `myFunc` definita nella pagina, passando i dati come argomento.
    

---

## ⚠️ Rischi di Sicurezza

### 1. Data Exfiltration (Furto di Dati)

Poiché i tag `<script>` possono essere inclusi da qualsiasi origine, un sito malevolo può includere un endpoint JSON-P di un sito vittima.

- Se l'endpoint restituisce dati sensibili e l'utente è autenticato (i cookie vengono inviati automaticamente), il sito dell'attaccante può definire la funzione di callback ed esfiltrare i dati dell'utente.
    
- **Contromisura:** Evitare JSON-P per dati sensibili; usare **CORS** con controlli di origine stretti.
    

### 2. CSP Bypass (Bypass della Content Security Policy)

Nelle slide, JSON-P è spesso citato come un "gadget" per aggirare le policy CSP.

- **Scenario:** Se una policy CSP consente l'esecuzione di script da un dominio fidato (es. `script-src 'self' https://trusted.com`) e quel dominio fidato ospita un endpoint JSON-P.
    
- **Attacco:** Un attaccante può iniettare uno script che punta all'endpoint JSON-P fidato, ma manipolando il parametro `callback` per eseguire codice arbitrario.
    
    - Esempio URL: `https://trusted.com/jsonp?callback=alert(1)//`
        
    - Risultato eseguito: `alert(1)//({...json...})` -> Il browser esegue l'alert perché la sorgente è considerata "fidata" dalla CSP.
        

---

## 📉 Stato Attuale

L'uso di JSON-P è **sconsigliato** nello sviluppo moderno.

- È stato largamente sostituito da **CORS** (Cross-Origin Resource Sharing), che offre un meccanismo standard e sicuro per il controllo degli accessi cross-domain.
    
- Rappresenta un rischio significativo se presente in domini inseriti in whitelist nelle Content Security Policy.