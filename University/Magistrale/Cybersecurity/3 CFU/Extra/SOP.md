# Same Origin Policy (SOP)

**Tag:** #security #web-security #SOP #browser-isolation #origin

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

La **Same Origin Policy (SOP)** è il meccanismo di sicurezza fondamentale implementato dai browser web moderni. Il suo obiettivo è garantire che gli script eseguiti su una pagina web, proveniente da una specifica origine, siano isolati dalle risorse provenienti da altre origini.

### Il concetto di "Origine"

Un'origine è definita dalla tripletta: **(Protocollo, Dominio, Porta)**. Due pagine hanno la stessa origine ("Same Origin") solo se tutti e tre questi elementi coincidono.

**Esempi di confronto con `https://example.com/index.html`**:

|**URL**|**Same Origin?**|**Motivo**|
|---|---|---|
|`https://example.com/profile.htm`|✅ Sì|Cambia solo il percorso (path)|
|`http://example.com/index.html`|❌ No|Protocollo diverso (HTTP vs HTTPS)|
|`https://shop.example.com/index.html`|❌ No|Hostname diverso (sottodominio)|
|`https://example.com:456/index.htm`|❌ No|Porta diversa (456 vs 443 default)|

---

## 🔒 Regole di Accesso

La SOP determina cosa uno script può o non può fare rispetto a risorse cross-origin.

### 🚫 Cosa è BLOCCATO (Accesso in lettura)

Se l'origine è diversa, il browser impedisce agli script di:

- **Accedere al DOM:** Non è possibile leggere o modificare il contenuto HTML (DOM) di iframe o finestre di altre origini.
    
- **Leggere dati di Storage:** Accesso negato a Cookie, LocalStorage e SessionStorage altrui.
    
- **Leggere Risposte di Rete:** Uno script può inviare una richiesta, ma **non può leggerne il corpo della risposta** (body).
    

### ✅ Cosa è PERMESSO (Inclusione e Scrittura)

Alcuni aspetti non sono soggetti alla SOP per permettere il funzionamento del web:

- **Inclusione di Risorse (Embedding):** È possibile includere risorse esterne come immagini, script (`<script src="...">`) e fogli di stile.
    
- **Form Submission:** È possibile inviare dati (POST/GET) verso un'altra origine tramite form HTML.
    
- **Invio Richieste:** È possibile inviare richieste (es. tramite Fetch API), anche se la lettura della risposta è bloccata (opaca).
    

---

## ⚠️ Eccezioni e Limitazioni

### 1. Complessità dell'Implementazione

Non esiste una definizione formale unica della SOP; i browser l'hanno evoluta tramite un approccio "penetrate-and-patch". Questo porta a incongruenze: uno studio ha rilevato che diversi browser si comportano in modo differente nel 23% dei test sull'accesso al DOM.

### 2. DNS Rebinding

Un attacco storico che aggira la SOP abusando del sistema DNS.

- **Meccanismo:** L'attaccante inganna il browser facendo risolvere il proprio dominio (`evil.com`) prima con il proprio IP, e successivamente (con un TTL breve) con l'IP privato della vittima (es. `10.0.0.3`) o localhost.
    
- **Risultato:** Il browser crede di parlare sempre con `evil.com` (rispettando la SOP), ma in realtà sta inviando richieste e leggendo risposte da un server interno alla rete privata.
    

### 3. Rilassamento della Policy

Esistono meccanismi legittimi per "rilassare" la SOP quando è necessario condividere dati tra origini diverse:

- **[[CORS]] (Cross-Origin Resource Sharing):** Il metodo standard e sicuro per permettere l'accesso cross-origin.
    
- **[[JSON-P]]:** Una tecnica "hack" storica (ora sconsigliata) che sfrutta il fatto che l'inclusione di `<script>` non è bloccata dalla SOP.