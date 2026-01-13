guardare sempre prima [[CS 6cfu - Domande esame]]

Basandomi sui file inviati (2012-2025), ecco le domande d'esame specifiche su **Kerberos**. Questo protocollo è una costante negli esami scritti.

### 1. I Componenti Fondamentali (Ticket vs Authenticator)

Questa è la domanda teorica più frequente (es. Gennaio 2017, Febbraio 2025).

- **Domanda:** "Descrivi la differenza tra un Ticket e un Authenticator in Kerberos. A cosa servono?"
    
- **Risposta da 30:**
    
    - **Ticket:** È una credenziale a _lunga durata_ (es. 8 ore) emessa dal KDC per permettere l'accesso a un servizio. È cifrato con la chiave segreta del _Server_ (quindi il client non può leggerlo/modificarlo) e contiene l'identità del client e la chiave di sessione.
        
    - **Authenticator:** È una credenziale a _brevissima durata_ (pochi minuti) generata dal _Client_ per ogni richiesta. Serve a provare che il client è "vivo" ora e possiede la chiave di sessione. Contiene un Timestamp per prevenire i **Replay Attacks**.
        

### 2. La Sequenza dei Messaggi (Domanda di Analisi)

Spesso viene chiesto di descrivere il flusso o di analizzare un diagramma (es. Febbraio 2025).

- **Domanda:** "Descrivi la sequenza di messaggi in Kerberos (dal login iniziale) per permettere ad Alice di usare un servizio".
    
- **Risposta schematica:**
    
    1. **AS_REQ (Alice $\to$ KDC/AS):** Alice chiede di loggarsi. Invia il suo ID in chiaro.
        
    2. **AS_REP (KDC/AS $\to$ Alice):** Il KDC invia il **TGT** (Ticket Granting Ticket) cifrato con la chiave del KDC + la Session Key cifrata con la chiave di Alice (derivata dalla password).
        
    3. **TGS_REQ (Alice $\to$ TGS):** Alice vuole accedere a "Bob" (Server). Invia il TGT + un Authenticator.
        
    4. **TGS_REP (TGS $\to$ Alice):** Il TGS verifica il TGT e rilascia un **Service Ticket** per Bob (cifrato con la chiave di Bob).
        
    5. **AP_REQ (Alice $\to$ Bob):** Alice invia il Service Ticket + un nuovo Authenticator a Bob.
        
    6. **AP_REP (Bob $\to$ Alice):** (Opzionale) Bob conferma l'autenticazione inviando il Timestamp + 1 cifrato con la chiave di sessione.
        

### 3. Cross-Realm Authentication (Scenario Avanzato)

Una domanda specifica trovata nell'esame di Febbraio 2025.

- **Domanda:** "Describe the sequence of messages in Kerberos to allow Alice (in Wonderland realm) to use the services of Bob that is in the Oz realm."
    
- **Soluzione:**
    
    - Alice contatta il suo KDC locale (Wonderland) per ottenere un TGT.
        
    - Alice chiede al TGS locale un ticket per il **KDC remoto** (Oz).
        
    - Alice contatta il KDC remoto (Oz) presentando il ticket cross-realm.
        
    - Il KDC remoto rilascia il ticket per il server finale Bob (che è in Oz).
        
    - Alice contatta Bob.
        

### 4. Vulnerabilità e Replay

Domande sul "perché" delle cose.

- **Domanda:** "Perché Kerberos richiede orologi sincronizzati?"
    
- **Risposta:** Per validare il **Timestamp** negli Authenticator. Se l'orologio è sfasato, il server scarta la richiesta come se fosse un vecchio messaggio riprodotto (Replay Attack).
    
- **Domanda:** "Perché Kerberos è considerato più sicuro di Needham-Schroeder originale?"
    
- **Risposta:** Perché usa i **Timestamp** per limitare la finestra di validità dei messaggi, mitigando il problema del replay di vecchi ticket (vulnerabilità Denning-Sacco).
    

### 5. Ticket Granting Ticket (TGT)

- **Domanda:** "Cos'è il TGT e perché esiste?"
    
- **Risposta:** È un ticket speciale che permette di ottenere altri ticket. Serve per implementare il **Single Sign-On (SSO)**: l'utente digita la password una volta sola per ottenere il TGT, poi il sistema usa il TGT per richiedere l'accesso a mail, stampanti, ecc., senza richiedere la password ogni volta.
    

**Attenzione:** Memorizza bene la distinzione: **AS** (Authentication Server $\to$ rilascia TGT) vs **TGS** (Ticket Granting Server $\to$ rilascia Service Ticket). All'esame spesso si chiede la differenza tra le due fasi.