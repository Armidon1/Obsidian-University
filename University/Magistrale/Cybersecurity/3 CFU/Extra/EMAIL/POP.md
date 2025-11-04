# 📥 Post Office Protocol (POP / POP3)

### Definizione

Il **POP** (Post Office Protocol), quasi universalmente utilizzato nella sua **versione 3** (da cui **POP3**), è un **protocollo standard di livello Applicazione** della suite TCP/IP, specificato da **RFC 1939**.

La sua funzione è esclusivamente quella di **recuperare (scaricare) messaggi di posta elettronica** da un server di posta (un _Mail Delivery Agent_, [[MDA]]) a un client di posta locale (un _Mail User Agent_, [[MUA]]).

Il suo modello operativo è paragonabile a quello di un ufficio postale: il client si connette al server, "ritira" tutta la posta in attesa, la scarica sul dispositivo locale e (nella sua modalità operativa predefinita) **elimina i messaggi dal server**.

### Dettagli Tecnici e Cybersecurity per Ingegneri

|**Caratteristica**|**Dettaglio Tecnico**|**Implicazione di Sicurezza e Funzionale**|
|---|---|---|
|**Porte Standard**|**110** (POP3, connessione _plaintext_), **995** (**POP3S**, connessione cifrata SSL/TLS)|L'uso della porta 110 è **altamente insicuro** e deprecato. Trasmette credenziali (`USER`/`PASS`) e contenuto delle email in chiaro, esponendoli a _sniffing_ e _Man-in-the-Middle_ (MITM). La porta 995 (POP3S) è l'unica opzione sicura.|
|**Protocollo di Base**|Protocollo **basato su testo** (ASCII) con un dialogo _request-response_ a stati.|Semplice da analizzare e implementare, ma richiede l'uso di `STLS` (estensione non molto comune per POP3) o il _wrapper_ SSL/TLS della porta 995 per la sicurezza.|
|**Stati del Protocollo**|**1. AUTHORIZATION:** Il client si autentica (`USER`, `PASS`). **2. TRANSACTION:** Il client gestisce i messaggi (`STAT`, `LIST`, `RETR`, `DELE`). **3. UPDATE:** Il server esegue le richieste (elimina i messaggi marcati `DELE`) e chiude la connessione (`QUIT`).|La sessione è _stateful_. I messaggi marcati per l'eliminazione (`DELE`) vengono rimossi solo dopo il comando `QUIT` (fase UPDATE). Se la connessione cade, i messaggi non vengono eliminati.|
|**Comandi Chiave**|`USER [username]` e `PASS [password]` (Autenticazione), `STAT` (Stato: n° messaggi e dimensione), `LIST [msg]` (Lista messaggi e dimensioni), `RETR [msg]` (Recupera l'intero messaggio), `DELE [msg]` (Marca un messaggio per l'eliminazione), `QUIT` (Chiude la sessione).|L'autenticazione è il punto debole. **APOP** (Authenticated POP) era un vecchio tentativo (RFC 1939) di usare un hash MD5 per evitare l'invio della password in chiaro, ma è obsoleto e soppiantato da SSL/TLS (POP3S).|
|**Modello Operativo**|**Download-and-Delete** (predefinito). Esiste una modalità "Keep" (lascia i messaggi sul server), ma POP3 non gestisce la sincronizzazione dello stato (es. "letto/non letto") sul server.|Questo modello crea una copia locale. Se il dispositivo locale viene compromesso o rubato, l'intero archivio di posta è compromesso.|

### Implicazioni in Cybersecurity

1. **Trasmissione in Chiaro (Plaintext):** L'uso di POP3 sulla porta 110 è una grave vulnerabilità. Un attaccante sulla stessa rete (es. Wi-Fi pubblica) può intercettare le credenziali di accesso e il contenuto di ogni e-mail scaricata. **L'uso di POP3S (porta 995) è obbligatorio** in qualsiasi contesto moderno.
    
2. **Singolo Punto di Fallimento (SPoF):** Il modello "download-and-delete" trasforma il dispositivo client nell'unico archivio della posta. Questo è un rischio enorme in termini di _Data Loss_ (guasto hardware, smarrimento) e _Data Breach_ (furto del dispositivo, malware sul client come i ransomware).
    
3. **Autenticazione Debole:** Il protocollo base non supporta nativamente meccanismi moderni come **OAuth 2.0** o **MFA** (Multi-Factor Authentication), rendendolo un bersaglio per attacchi di _brute-force_ o _password spraying_ contro la porta 110/995, a meno che non sia protetto da servizi esterni.
    

### Differenza Chiave: POP3 vs. IMAP

La differenza ingegneristica fondamentale tra POP3 e IMAP è lo **stato della sessione**:

- **POP3:** È un protocollo "offline". Si connette, scarica tutto, si disconnette. Lo stato (quale mail è letta, in quale cartella si trova) **esiste solo sul client**.
    
- **IMAP (Internet Message Access Protocol):** È un protocollo "online". Mantiene una connessione persistente e **sincronizza lo stato** tra il client e il server. Il server è la fonte autorevole (_source of truth_) per tutte le e-mail e le cartelle.
    

Per questo motivo, POP3 è inadatto all'uso multi-dispositivo (es. smartphone e laptop), dove IMAP è invece lo standard.