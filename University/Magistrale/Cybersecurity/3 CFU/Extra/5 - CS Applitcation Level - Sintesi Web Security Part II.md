Ecco una sintesi delle principali vulnerabilità trattate nelle slide ("[[5 - CS Application Level - Web Security Part II]] "), con relative definizioni brevi e citazioni alle fonti:

### 1. Vulnerabilità legate alla Same Origin Policy (SOP)

- **DNS Rebinding:** Un attacco che aggira la SOP abusando del sistema DNS. L'attaccante fa visitare alla vittima un sito (es. `evil.com`) e poi cambia rapidamente l'indirizzo IP associato a quel dominio per farlo puntare a un IP privato interno (es. `10.0.0.3`). Il browser, credendo di parlare con la stessa origine, permette allo script malevolo di leggere dati dalla rete interna privata,.
- **JSON-P (Vulnerabilità intrinseca):** Una tecnica definita "hack" per aggirare la SOP, che consiste nell'includere script esterni per ricevere dati JSON avvolti in una funzione (callback). È vulnerabile perché richiede fiducia totale nella terza parte (che può eseguire qualsiasi codice nella tua pagina) e perché l'origine importatrice non può validare lo script,.

### 2. Vulnerabilità dei Cookie

- **Cookie Tossing:** Un attacco in cui un sottodominio malevolo (o compromesso) imposta un cookie definendo l'attributo `Domain` per il dominio padre (es. `.example.com`). Questo cookie viene inviato dal browser anche al dominio principale e ad altri sottodomini, potenzialmente sovrascrivendo i cookie di sessione legittimi o bypassando protezioni CSRF,.
- **Cookie Jar Overflow:** L'attaccante genera un numero enorme di cookie per riempire il limite di memoria del browser ("jar"), forzando la cancellazione dei cookie più vecchi (inclusi quelli protetti da `HttpOnly`). Una volta eliminati i legittimi, l'attaccante può impostarne di nuovi a suo piacimento,.
- **Cookie Overwrite:** Poiché il browser invia al server solo nome e valore del cookie (senza attributi come `Domain` o `Secure`), un attaccante su un sottodominio può sovrascrivere un cookie sicuro del dominio principale, e il server non è in grado di distinguerli.

### 3. Cross-Site Request Forgery (CSRF)

- **Definizione:** Un attacco che abusa del fatto che il browser allega automaticamente i cookie di sessione alle richieste. L'attaccante induce la vittima (già autenticata su un sito target) a visitare una pagina malevola che invia una richiesta "invisibile" verso il sito target (es. un bonifico bancario). Il server esegue l'operazione credendo sia legittima perché riceve i cookie corretti,.

### 4. Cross-Site Scripting (XSS)

- **Definizione Generale:** Una vulnerabilità di iniezione che permette a un attaccante di eseguire codice JavaScript arbitrario nel browser della vittima. Le slide distinguono tre tipi:
    - **Reflected XSS:** Il payload malevolo inviato dall'attaccante viene immediatamente riflesso dal server nella pagina di risposta (es. risultati di ricerca).
    - **Stored XSS:** Il payload malevolo viene salvato permanentemente sul server (es. in un commento o in un database) e servito alla vittima quando visita la pagina,.
    - **DOM-based XSS:** L'iniezione avviene interamente lato client ("browser-side"). Uno script legittimo della pagina prende dati controllati dall'utente (Sorgente, es. URL) e li inserisce in modo insicuro nel DOM (Sink, es. `innerHTML`) senza passare dal server,.

### 5. Altre Vulnerabilità

- **Client-side Messaging (postMessage issues):** Vulnerabilità che si verifica quando una pagina riceve messaggi via `postMessage` da altre finestre senza validare correttamente l'origine (`evt.origin`) del mittente, permettendo a siti malevoli di inviare comandi o dati dannosi.
- **Dangling Markup Injection:** Un'alternativa all'XSS usata quando non si possono eseguire script. L'attaccante inietta tag HTML non chiusi (es. `<img src='...`) per "inglobare" il resto del contenuto della pagina (inclusi token segreti) fino alla successiva virgoletta, inviando i dati al proprio server.
- **SSL Stripping:** Un attacco di rete in cui un intermediario (Man-in-the-Middle) forza il downgrade della connessione della vittima da HTTPS a HTTP, intercettando i dati prima che vengano cifrati. Può essere mitigato tramite HSTS,.