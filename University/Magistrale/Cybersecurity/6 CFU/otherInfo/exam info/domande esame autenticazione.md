guardare sempre prima [[CS 6cfu - Domande esame]]

Basandomi solo sugli esami che hai inviato (2012-2025), ecco cosa chiede effettivamente il professore sull'**Autenticazione e Protocolli**:

### 1. Autenticazione Challenge-Response (Il "Re" degli esercizi)

Questo è l'esercizio più frequente in assoluto. Il professore ti dà uno schema di autenticazione "fatto in casa" e ti chiede di romperlo.

- **Tipologia di Domanda:**
    
    - Ti viene dato un protocollo del tipo:
        
        1. $A \to B: A, N_A$
            
        2. $B \to A: B, N_B, Enc_K(N_A)$
            
        3. ...
            
    - **Richiesta 1:** "Analizza il protocollo e trova le vulnerabilità (Replay, Reflection, MITM)".
        
    - **Richiesta 2:** "Proponi una correzione (senza stravolgere il protocollo)".
        
- **Esempi Reali dagli Esami:**
    
    - **Gennaio 2019:** Protocollo con HMAC e nonces. Vulnerabile perché $B$ risponde alla sfida di $A$ _e_ manda la sua sfida nello stesso messaggio, permettendo un _Reflection Attack_.
        
    - **Giugno 2023:** Protocollo mutual authentication a 3 passi. Chiede di discutere la sicurezza.
        
    - **Febbraio 2015:** Protocollo "Leader Selection" (che è una variante di autenticazione di gruppo).
        
- **La Risposta Standard da Sapere:**
    
    - Se il protocollo è simmetrico ($A \to B$ è uguale a $B \to A$), è quasi sempre vulnerabile al **Reflection Attack**.
        
    - _Soluzione:_ Inserire l'identità del mittente _dentro_ la cifratura/HMAC (es. $Enc_K(A, N_B)$ invece di $Enc_K(N_B)$) o usare chiavi diverse per le due direzioni.
        

### 2. Autenticazione Password-Based (Sicurezza Pratica)

Domande molto pratiche su come gestire le password.

- **Salt & Rainbow Tables:**
    
    - "Cos'è il Salting e perché si usa?" (Per rendere unici gli hash di password uguali e prevenire attacchi precalcolati).
        
    - "Cosa sono le Rainbow Tables?" (Tabelle precalcolate per invertire gli hash delle password).
        
- **Offline Dictionary Attack:**
    
    - Descrivere l'attacco: L'attaccante ruba il file delle password (hash) e prova a indovinarle offline senza limiti di tentativi.
        
- **Replay & Reflection su Password:**
    
    - "Progetta un protocollo password-based che prevenga Replay e Reflection".
        
    - _Soluzione:_ Usare Challenge-Response basato sulla password (es. invio $Hash(Password, Nonce)$ invece della password in chiaro).
        

### 3. Kerberos e Needham-Schroeder

Meno frequente come esercizio di design, ma presente come domanda teorica o di analisi.

- **Domanda:**
    
    - "Descrivi la sequenza di messaggi in Kerberos per permettere ad Alice di usare un servizio".
        
    - "Cosa sono i Ticket e gli Authenticator in Kerberos? A cosa servono?"
        
        - _Ticket:_ Identità cifrata per il server (prova che la TTP ha garantito per Alice).
            
        - _Authenticator:_ Prova che Alice è viva _ora_ (contiene Timestamp/Nonce).
            
- **Domanda:**
    
    - "Illustra un esempio di Reflection Attack su un'autenticazione challenge-response".
        

### 4. Differenze Concettuali (Definizioni)

Domande brevi da 2-3 punti.

- **Autenticazione vs Integrità vs Autenticità:**
    
    - "L'autenticità implica l'integrità?" (Sì).
        
    - "Differenza tra autenticazione di messaggi (AoM) e di entità (AoE)".
        
- **Firma Digitale per Autenticazione:**
    
    - "Come usare una firma digitale per autenticare un utente ed evitare replay?"
        
    - _Risposta:_ Firmare un Nonce inviato dal server ($Sign_A(Nonce_B)$).
        

### Riassunto per lo Studio "Mirato"

1. **Impara a disegnare e rompere il protocollo Challenge-Response:** Se vedi $A \to B: N_A$ e poi $B \to A: N_B, K(N_A)$, pensa subito: "Trudy può aprire una seconda sessione e farsi risolvere la sfida da B?" (Reflection).
    
2. **Kerberos a memoria:** Ticket (Lunga durata, cifrato per il server) vs Authenticator (Breve durata, creato dal client).
    
3. **Password:** Mai inviarle in chiaro o solo hashate (Replay). Usare sempre Salt (Rainbow Tables) e Challenge-Response (Replay).