# 🖥️ Internet Message Access Protocol (IMAP)

### Definizione

**IMAP** (Internet Message Access Protocol), attualmente nella sua versione **IMAP4rev1** (specificata da **RFC 3501**), è un **protocollo standard di livello Applicazione** della suite TCP/IP. Come [[POP]]3, è un protocollo _pull_ utilizzato per il recupero della posta elettronica da un server.

Tuttavia, il suo modello operativo è fondamentalmente diverso da POP3. IMAP è progettato per un **accesso "online" e multi-dispositivo**. Il protocollo consente a un client (MUA) di **accedere e manipolare i messaggi di posta elettronica direttamente sul server**, come se fossero file su un filesystem remoto.

La caratteristica distintiva di IMAP è che il **server è la fonte autorevole (_source of truth_)**. Le e-mail rimangono sul server per impostazione predefinita, e IMAP sincronizza lo stato dei messaggi (es. "letto", "risposto", "eliminato") e la struttura delle cartelle tra tutti i client connessi.

### Dettagli Tecnici e Cybersecurity per Ingegneri

|**Caratteristica**|**Dettaglio Tecnico**|**Implicazione di Sicurezza e Funzionale**|
|---|---|---|
|**Porte Standard**|**143** (IMAP, _plaintext_), **993** (**IMAPS**, connessione cifrata SSL/TLS)|L'uso della porta 143 senza **STARTTLS** è **estremamente insicuro**, esponendo credenziali e contenuto delle email allo _sniffing_. La porta 993 (IMAPS) è lo standard sicuro preferito.|
|**Protocollo di Base**|Protocollo **basato su testo** (ASCII) con comandi _tagged_ (prefissati da un identificatore di comando, es. `A001`) per tracciare le risposte.|Più complesso di POP3. La natura _stateful_ e i comandi asincroni (come `IDLE`) lo rendono potente ma aumentano la superficie di attacco del server.|
|**Comandi Chiave**|`LOGIN` / `AUTHENTICATE` (Autenticazione), `LIST` (Elenca cartelle), `SELECT` (Seleziona una cartella, es. `INBOX`), `FETCH` (Recupera parti del messaggio, es. `BODY[TEXT]`), `STORE` (Modifica gli attributi/flag del messaggio), `COPY`, `MOVE`|`FETCH` è potente: permette di scaricare solo gli _header_ o parti specifiche (es. allegati), risparmiando banda. `STORE` è fondamentale per la sincronizzazione (es. `STORE 1 +FLAGS (\Seen)`).|
|**Identificatori e Stati**|**UID (Unique Identifier):** Un numero a 32 bit che identifica univocamente un messaggio _all'interno di una cartella_. Non cambia tra le sessioni. **Flags:** Attributi di stato (es. `\Seen`, `\Answered`, `\Flagged`, `\Deleted`).|L'uso di **UID** è cruciale per la sincronizzazione. Un client può chiedere "dammi tutti i messaggi con UID > X" per sincronizzare solo i nuovi messaggi, evitando di riscaricare tutto. I _Flags_ sono il cuore della sincronizzazione di stato.|
|**Modalità Operativa**|**Connesso / Sincronizzato.** Il client mantiene una copia cache locale e sincronizza i cambiamenti con il server.|Permette un accesso multi-dispositivo coerente. Se si legge un'email sullo smartphone, apparirà come letta anche sul PC.|

### Implicazioni in Cybersecurity

1. **Esposizione delle Credenziali (Porta 143):** Come per POP3, l'uso di IMAP non cifrato sulla porta 143 è una vulnerabilità critica. Un attaccante può intercettare le credenziali `LOGIN` e ottenere pieno accesso all'account. **IMAPS (993) o STARTTLS (su 143) sono obbligatori.**
    
2. **Il Server come Bersaglio ad Alto Valore:** Nel modello IMAP, **l'intero archivio di posta elettronica** (anni di comunicazioni, allegati sensibili) risiede sul server. Questo rende il server di posta un bersaglio primario per gli aggressori. Una singola violazione delle credenziali (tramite phishing, brute-force) o una vulnerabilità del server (es. 0-day) può esporre l'intera cronologia delle comunicazioni.
    
3. **Complessità del Protocollo e Superficie d'Attacco:** IMAP è significativamente più complesso di POP3. Supporta molti comandi, estensioni e una gestione complessa dello stato. Questa complessità aumenta la probabilità di **vulnerabilità nell'implementazione del server** (es. buffer overflow, _injection_ nei comandi, _logic flaw_ nella gestione dei permessi).
    
4. **Autenticazione Moderna:** Data la sua natura "always-on", l'autenticazione IMAP è un vettore di attacco comune. Le implementazioni moderne devono integrare meccanismi robusti come **OAuth 2.0** (usato da Google e Microsoft) per evitare di memorizzare la password dell'utente direttamente sul client, utilizzando invece token di accesso con scope limitato.
    

### Confronto Chiave: IMAP vs. [[POP]]3

|**Aspetto**|**POP3 (Post Office Protocol)**|**IMAP (Internet Message Access Protocol)**|
|---|---|---|
|**Modello**|**Offline (Download-and-Delete)**|**Online (Sincronizzazione)**|
|**Dati**|I messaggi vengono scaricati sul client e (di solito) rimossi dal server.|I messaggi e le cartelle risiedono sul server. Il client è uno "specchio".|
|**Stato**|Lo stato (es. "letto") è gestito **solo sul client**.|Lo stato (es. "letto", "risposto") è sincronizzato **sul server** e condiviso tra tutti i client.|
|**Uso**|Singolo dispositivo.|Multi-dispositivo (PC, smartphone, webmail).|
|**Rischio Dati**|**Perdita del client** = perdita di tutte le email.|**Compromissione del server/account** = perdita di tutte le email.|