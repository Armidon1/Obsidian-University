# SSL Stripping & HSTS

**Tag:** #security #web-security #MITM #HTTPS #HSTS #downgrade-attack

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione: SSL Stripping

L'**SSL Stripping** è un attacco di tipo _Man-in-the-Middle_ (MITM) in cui un attaccante si interpone tra l'utente e il server, forzando la connessione a rimanere su protocollo **HTTP** (in chiaro) anche se il server supporta HTTPS.

- **Obiettivo:** Intercettare dati sensibili (password, cookie) che verrebbero altrimenti cifrati.
    
- **Funzionamento:** L'attaccante stabilisce una connessione HTTPS legittima con il server, ma comunica con la vittima via HTTP. L'attaccante modifica "al volo" le risposte del server, sostituendo tutti i link `https://` con `http://`.

## Esempio di attacco


> [!abstract] Visual Analysis
> ![[Pasted image 20260131142758.png]]
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

## 🛡️ Mitigazione: [[HSTS]] (HTTP Strict Transport Security)

Per contrastare l'SSL Stripping, è stato introdotto il meccanismo **HSTS**. È un header di risposta HTTP che permette a un server di dichiarare che tutte le future interazioni con esso **devono** avvenire su HTTPS.

### Funzionamento

Quando un browser riceve l'header `Strict-Transport-Security`:

1. **Upgrade Automatico:** Il browser converte automaticamente tutte le richieste HTTP in HTTPS prima di inviarle alla rete.
    
2. **Gestione Errori:** Se si verificano errori nella connessione sicura (es. certificato non valido), la connessione viene chiusa immediatamente senza permettere all'utente di aggiungere eccezioni di sicurezza.
    
3. **Vincolo:** L'header viene ignorato se ricevuto su una connessione HTTP non sicura (per evitare che un attaccante possa iniettarlo o rimuoverlo).
    

### Policy HSTS

L'header supporta diverse direttive:

- `max-age`: La durata (in secondi) per cui il browser deve ricordare di usare solo HTTPS per quel sito (es. 6307200 per 2 anni).
    
- `includeSubDomains`: Applica la regola anche a tutti i sottodomini.
    
- `preload`: Richiede l'inclusione nella lista di precaricamento del browser.
    

---

## ⚠️ Limitazioni e Bypass

### 1. Trust On First Use (TOFU)

L'HSTS soffre del problema del "primo utilizzo". Se un utente visita un sito per la prima volta (e non ha mai ricevuto l'header HSTS prima) e l'attaccante esegue l'SSL Stripping proprio in quel momento, la protezione non è attiva.

- **Soluzione:** **HSTS Preloading**. I browser moderni includono una lista "hardcoded" di siti che devono essere contattati solo via HTTPS (es. Google, PayPal). I siti possono richiedere di essere inseriti in questa lista tramite `hstspreload.org`.
    

### 2. NTP Attacks (Bypass tramite orario)

Le slide evidenziano un metodo ingegnoso per disattivare l'HSTS manipolando il protocollo NTP (Network Time Protocol).

- **Vulnerabilità:** Molti sistemi operativi usano NTP senza autenticazione per sincronizzare l'orologio.
    
- **Attacco:** Un attaccante MITM può inviare risposte NTP false, spostando l'orologio della vittima avanti nel futuro (es. di anni).
    
- **Risultato:** Se l'orologio di sistema supera la data di scadenza (`max-age`) della policy HSTS salvata nel browser, il browser considererà la policy scaduta e tornerà a permettere connessioni HTTP, rendendo nuovamente possibile l'SSL Stripping.