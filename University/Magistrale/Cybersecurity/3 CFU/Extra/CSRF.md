# Cross-Site Request Forgery (CSRF)

**Tag:** #security #web-security #vulnerability #CSRF #session-management

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

Il **Cross-Site Request Forgery (CSRF)** è un attacco che abusa del meccanismo automatico con cui i browser allegano i cookie alle richieste HTTP. L'attaccante costringe il browser della vittima a eseguire azioni indesiderate su un'applicazione web in cui l'utente è attualmente autenticato.

- **Concetto chiave:** Il sito vulnerabile non riesce a distinguere se una richiesta è stata avviata intenzionalmente dall'utente o se è stata innescata da una pagina malevola di terze parti.
    
- **Prerequisito:** La vittima deve avere una sessione attiva (essere loggata) sul sito target.
    

---

## ⚙️ Meccanismo di Attacco

L'attacco segue generalmente questo flusso:

1. **Preparazione:** L'attaccante predispone una pagina web o un link malevolo che contiene una richiesta verso il sito target (es. `bank.com/transfer`).
    
2. **Esecuzione:** La vittima visita il sito dell'attaccante.
    
3. **Trigger:** La pagina malevola invia automaticamente la richiesta al sito target (es. tramite un form nascosto inviato via JavaScript per richieste POST, o caricando un'immagine per richieste GET).
    
4. **Autenticazione Automatica:** Il browser della vittima allega automaticamente i cookie di sessione validi alla richiesta verso il dominio target.
    
5. **Azione:** Il server riceve la richiesta, verifica i cookie (che sono validi) e la esegue (es. effettua il bonifico o cambia la password), credendo sia legittima.
    

---

## 🛡️ Prevenzione e Mitigazione

### 1. Anti-CSRF Tokens

La difesa più robusta consiste nell'utilizzare token segreti e imprevedibili che il browser non include automaticamente.

- **Synchronizer Token Pattern:** Il server genera una stringa casuale (token) e la inserisce come campo nascosto (`<input type="hidden">`) in tutti i form HTML. Al momento della sottomissione, il server verifica che il token sia presente e corretto.
    
- **Cookie-to-header:** Un token viene impostato in un cookie; il client (JavaScript) legge questo cookie e lo inserisce in un header HTTP personalizzato. Il server verifica la corrispondenza.
    

### 2. SameSite Cookie Attribute

Un attributo dei cookie che controlla se questi devono essere inviati nelle richieste cross-site.

- **Lax (Default moderni):** Il cookie viene inviato solo se la navigazione avviene nel "top-level" (l'utente cambia URL nella barra degli indirizzi), proteggendo da molti attacchi CSRF automatici ma non da tutti.
    
- **Strict:** Il cookie non viene mai inviato in richieste cross-site.
    
- **Nota:** Non protegge contro attaccanti che controllano un sottodominio ("related-domain attackers").
    

### 3. Referer Validation

L'applicazione verifica l'header HTTP `Referer` per assicurarsi che la richiesta provenga da una pagina consentita (dello stesso dominio).

- **Limiti:** L'header può essere soppresso per motivi di privacy o manipolato in certi contesti; la validazione può essere troppo permissiva ("Lenient") o rompere funzionalità legittime ("Strict").
    

### 4. Fetch Metadata

Utilizzo di nuovi header HTTP (`Sec-Fetch-Site`, `Sec-Fetch-Mode`, ecc.) che informano il server sul contesto della richiesta (es. se è cross-site o same-origin). Il server può usare queste informazioni per scartare richieste sospette (es. un bonifico bancario non dovrebbe essere innescato da un tag `<img>`).