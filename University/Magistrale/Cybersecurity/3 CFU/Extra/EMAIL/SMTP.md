## 📧 Simple Mail Transfer Protocol (SMTP)

### Definizione

**SMTP** (Simple Mail Transfer Protocol) è un **protocollo standard di comunicazione Internet** a livello di **Applicazione** della suite TCP/IP, specificato da **RFC 5321** (che ha aggiornato la precedente RFC 2821). La sua funzione principale è il **trasferimento e l'instradamento di messaggi di posta elettronica** (email) tra server di posta elettronica (Mail Transfer Agent - **MTA**) e tra un client di posta (Mail User Agent - **MUA**) e un server di posta.

Opera su un **modello push**, dove il server/client mittente (client SMTP) avvia la connessione e "spinge" il messaggio verso il server di posta ricevente (server SMTP), utilizzando **TCP** (Transmission Control Protocol) per garantire una trasmissione affidabile e ordinata.

### Dettagli Tecnici e Cybersecurity per Ingegneri

|**Caratteristica**|**Dettaglio Tecnico**|**Implicazione di Sicurezza**|
|---|---|---|
|**Porte Standard**|**25** (Tra MTA, spesso non cifrata), **587** (Submission client-to-server, con STARTTLS), **465** (SMTPS, storicamente in disuso, ma ancora usato da alcuni servizi).|L'uso della porta 25 senza cifratura espone i dati e i metadati al _sniffing_ (_traffic interception_). 587 con **STARTTLS** è il moderno standard preferito.|
|**Protocollo di Base**|Protocollo **basato su testo** (ASCII) in un dialogo _request-response_ tra client e server, iniziato con i comandi **HELO** o **EHLO**.|La natura _plaintext_ facilita l'interazione manuale (es. con `telnet` o `netcat`) ma espone le vulnerabilità.|
|**Comandi Chiave**|**EHLO** (Extended HELO), **MAIL FROM** (Indirizzo di _envelope sender_ o _return-path_), **RCPT TO** (Destinatario di _envelope_), **DATA** (Inizio del corpo del messaggio, terminato da un punto su una riga separata `.` ).|**MAIL FROM** e gli header `From`/`Sender` nel corpo del messaggio sono distinti. La mancanza di autenticazione intrinseca di base di SMTP consente lo **Spoofing** del _MAIL FROM_ (un problema risolto parzialmente da protocolli esterni).|
|**Autenticazione Originale**|**Assente** nel protocollo base (RFC 821).|Vulnerabilità critica che ha portato a massicci attacchi di **Spam** e **Phishing**.|
|**Estensioni di Sicurezza**|**SMTP-AUTH** (RFC 2554) per l'autenticazione del client con credenziali. **STARTTLS** (RFC 2487) per avviare una negoziazione TLS/SSL su una connessione non cifrata (tipicamente sulla porta 587 o 25).|SMTP-AUTH previene l'abuso dei _relay_ aperti. STARTTLS fornisce **Confidenzialità** e **Integrità** del messaggio durante il transito (trasformando la sessione in SMTPS).|
|**Protezioni Aggiuntive**|**SPF** (Sender Policy Framework), **DKIM** (DomainKeys Identified Mail), **DMARC** (Domain-based Message Authentication, Reporting, and Conformance).|Questi meccanismi operano a livello di DNS e server per **autenticare l'origine del messaggio** e mitigare lo spoofing e il phishing, lavorando _attorno_ alle lacune di sicurezza intrinseche di SMTP.|

### Implicazioni in Cybersecurity

1. **Spoofing e Phishing:** La debolezza fondamentale di SMTP è la sua originaria **mancanza di meccanismi di autenticazione e di verifica dell'origine** (il campo `MAIL FROM` può essere falsificato). Ciò è ampiamente sfruttato nel _Business Email Compromise_ (BEC) e negli attacchi di phishing. I protocolli esterni come SPF, DKIM e DMARC sono implementazioni difensive essenziali per combattere questo problema.
    
2. **Open Relay:** Un server SMTP configurato in modo errato che consente a _chiunque_ su Internet di inviare e-mail a _qualsiasi_ dominio esterno tramite esso (senza autenticazione) è chiamato **Open Relay**. Storicamente era un problema enorme, oggi è raro ma critico, in quanto il server diventa un veicolo per lo spam.
    
3. **Crittografia:** L'SMTP di base non utilizza la crittografia. Se un server non supporta o non è configurato per forzare **STARTTLS** o utilizzare la porta **465 (SMTPS)**, l'intera comunicazione (incluse credenziali e contenuto dell'e-mail) avviene in chiaro (_plaintext_), rendendola vulnerabile ad attacchi _Man-in-the-Middle_ o intercettazioni.
    

Comprendere il flusso dei comandi SMTP (`EHLO`, `MAIL FROM`, `RCPT TO`, `DATA`) e la distinzione tra l'**_envelope_** (utilizzato per la consegna MTA) e gli **_header_** (visibili all'utente) è fondamentale per analizzare le minacce e implementare soluzioni di sicurezza adeguate.

---

Ecco la trascrizione arricchita dei contenuti forniti:

## SMTP e ESMTP

- **SMTP:** Simple Mail Transfer Protocol (RFC 821 → 5321). È il protocollo standard utilizzato per **inviare** (push) e-mail tra server (comunicazione MTA-MTA) e dal client al server (MUA-MSA). Funziona sulla porta 25 (per server-to-server) e 587 (per la submission).
    
- **ESMTP:** Extended SMTP (definito nello stesso RFC 5321).
    
    - Non è un protocollo separato, ma un **meccanismo di estensione** per SMTP.
        
    - Un client "moderno" avvia la connessione usando il comando `EHLO` (Extended Hello) invece del vecchio `HELO`.
        
    - Se il server supporta ESMTP, risponde con un elenco di tutte le estensioni (comandi aggiuntivi) che supporta. Questo rende il protocollo retrocompatibile ma estendibile.
        
    - Ha introdotto comandi fondamentali come `AUTH`, `STARTTLS` e `SIZE`.
        

---

### Comandi ESMTP Comuni

Queste estensioni aggiungono funzionalità cruciali che mancavano nell'SMTP originale:

|**Comando**|**Scopo**|**RFC**|
|---|---|---|
|**8BITMIME**|Permette la trasmissione di dati a 8 bit (MIME).|6152|
|**AUTH**|Abilita l'autenticazione SMTP (login).|4954|
|**STARTTLS**|Avvia la crittografia TLS sulla connessione.|3207|
|**SIZE**|Permette al client di dichiarare la dimensione del messaggio.|1870|
|**DSN**|Richiede notifiche sullo stato della consegna (Delivery Status Notifications).|3461|
|**PIPELINING**|Consente l'invio di comandi in pipeline (in sequenza) per efficienza.|2920|

---

## Esempio di Interazione SMTP

Queste immagini mostrano una sessione SMTP testuale tra un client (C:) e un server (S:). Si tratta di una serie di comandi e risposte in chiaro che negoziano l'invio di un messaggio.

![[Pasted image 20251028145421.png]]

![[Pasted image 20251028145437.png]]

### Analisi dell'Interazione

L'interazione segue questi passaggi:

1. **Connessione:** Il client apre una connessione TCP sulla porta 25 o 587 del server.
    
2. **Saluto:** Il client invia `EHLO` per presentarsi e scoprire le estensioni del server.
    
3. **Sicurezza (Opzionale):** Se il server offre `STARTTLS`, il client invia questo comando per crittografare la sessione.
    
4. **Autenticazione (Opzionale):** Se il server offre `AUTH`, il client si autentica (fondamentale sulla porta 587).
    
5. **Busta (Envelope):**
    
    - Il client specifica il mittente della "busta" con `MAIL FROM:<indirizzo>`.
        
    - Il client specifica il destinatario della "busta" con `RCPT TO:<indirizzo>`.
        
6. **Dati:**
    
    - Il client invia `DATA` per annunciare l'inizio del messaggio.
        
    - Il server risponde "OK, inizia pure, termina con un punto (`.`) su una riga vuota".
        
    - Il client invia tutte le **intestazioni** (Header), la linea vuota, e il **corpo** (Body).
        
    - Il client invia `.` per terminare.
        
7. **Chiusura:** Il server conferma la ricezione e il client invia `QUIT` per chiudere la connessione.
    

---

