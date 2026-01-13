guardare sempre prima [[CS 6cfu - Domande esame]]

Certamente. Rispetto alla tua richiesta di usare l'**Opzione B** (Spiegazione Dettagliata basata sugli esami), ecco l'analisi approfondita per **PKI, X.509 e Autenticazione a Chiave Pubblica**.

---

### 1. La Necessità della PKI e i Certificati Digitali

La Domanda d'Esame:

"Cosa è un certificato digitale e quali problemi risolve? Quali controlli deve effettuare chi riceve un certificato?"

La Spiegazione (Il "Perché"):

Il problema fondamentale della crittografia asimmetrica non è la matematica, ma la fiducia.

Se io (Alice) voglio mandare un messaggio segreto a te (Bob), mi serve la tua Chiave Pubblica ($Pk_B$).

Se ti chiedo "Mandami la tua chiave", e l'attaccante (Trudy) intercetta la richiesta, Trudy mi manda la sua chiave pubblica ($Pk_T$) dicendo "Eccola, sono Bob".

Io cifro il messaggio con $Pk_T$. Trudy lo decifra, lo legge, lo ricifra con la vera chiave di Bob e glielo manda. Bob non si accorge di nulla. Questo è un Man-in-the-Middle.

Per risolverlo, ci serve una "terza parte fidata" che garantisca: "Questa chiave pubblica $Pk_B$ appartiene davvero a Bob". Questa parte è la Certification Authority (CA).

Il Certificato Digitale è proprio questo: un documento firmato dalla CA che lega un'identità a una chiave pubblica.

**Cosa scrivere all'esame:**

- **Definizione:** Un certificato digitale (standard X.509) è un documento elettronico firmato digitalmente da un'autorità fidata (CA) che associa in modo inequivocabile una Chiave Pubblica a un'Identità (Soggetto).
    
- **Problema risolto:** Risolve il problema dell'**autenticità delle chiavi pubbliche**, prevenendo attacchi Man-in-the-Middle durante la distribuzione delle chiavi. Crea una catena di fiducia.
    
- **Controlli (Chain of Trust):** Chi riceve il certificato deve verificare:
    
    1. **Firma:** La firma della CA sul certificato deve essere valida (usando la chiave pubblica della CA).
        
    2. **Validità Temporale:** La data corrente deve essere compresa tra `notBefore` e `notAfter`.
        
    3. **Revoca:** Il certificato non deve essere stato revocato (controllo tramite CRL o OCSP).
        
    4. **Identità:** Il campo `Subject` (o `Subject Alternative Name`) deve corrispondere all'entità con cui si sta comunicando (es. il dominio del sito web).
        

---

### 2. Autenticazione Challenge-Response Asimmetrica

La Domanda d'Esame:

"Descrivi un protocollo di autenticazione basato su chiave pubblica. Quali sono i vantaggi rispetto a quello simmetrico?"

La Spiegazione (Il "Perché"):

Nell'autenticazione simmetrica (es. password o Kerberos), il server deve conoscere il tuo segreto (o un hash/chiave derivata). Se il server viene hackerato, le tue credenziali sono a rischio.

Nell'autenticazione a chiave pubblica, tu provi la tua identità dimostrando di possedere la Chiave Privata, senza mai inviarla. Il server ha solo la tua Chiave Pubblica (che è pubblica, quindi se viene rubata non succede nulla di grave).

Il meccanismo è sempre **Challenge-Response** per evitare il **Replay Attack** (se mandassi solo una firma statica, l'attaccante la copierebbe e la riuserebbe).

**Cosa scrivere all'esame:**

- **Protocollo:**
    
    1. **Bob (Verifier) $\to$ Alice (Prover):** Invia un Nonce (numero casuale) $N_B$.
        
    2. **Alice $\to$ Bob:** Invia la firma digitale del Nonce calcolata con la sua Chiave Privata: $S = Sign_{Sk_A}(N_B)$.
        
    3. **Bob:** Verifica la firma usando la Chiave Pubblica di Alice: $Verify(Pk_A, N_B, S)$. Se è valida, Alice è autenticata.
        
- **Vantaggi rispetto al Simmetrico:**
    
    1. **Nessun segreto condiviso:** Il server non memorizza segreti sensibili dell'utente. Se il server è compromesso, l'attaccante non può impersonare l'utente altrove.
        
    2. **Non-Ripudio:** La firma digitale fornisce una prova forte che l'utente ha compiuto l'azione (solo lui ha la privata), cosa che l'HMAC simmetrico non fa.
        
    3. **Scalabilità:** Non serve distribuire chiavi segrete a coppie ($N^2$ chiavi). Basta pubblicare le chiavi pubbliche.
        

---

### 3. Revoca: CRL vs OCSP

La Domanda d'Esame:

"Confronta CRL e OCSP. Quali sono i vantaggi di OCSP? Perché OCSP presenta problemi di privacy?"

La Spiegazione (Il "Perché"):

A volte un certificato deve morire prima della scadenza (es. ho perso il portatile con la chiave privata). La CA deve dirlo al mondo.

- **CRL (Certificate Revocation List):** È come l'elenco cartaceo delle carte di credito rubate che i negozianti avevano negli anni '80. La CA pubblica un file enorme con _tutti_ i seriali revocati. Il browser deve scaricarlo tutto. È inefficiente.
    
- **OCSP (Online Certificate Status Protocol):** È come il POS moderno. Il browser chiede alla CA: "La carta 123 è valida?". La CA risponde in tempo reale.
    

_Il problema Privacy:_ Se chiedi alla CA "È valido il certificato di `sitobrutti.com`?", la CA capisce che stai visitando quel sito.

**Cosa scrivere all'esame:**

- **CRL:** È una lista statica di tutti i certificati revocati, firmata dalla CA.
    
    - _Svantaggi:_ Può diventare molto grande (lentezza nel download) e non è aggiornata in tempo reale (rischio di accettare un certificato revocato di recente).
        
- **OCSP:** È un protocollo di interrogazione online. Il client chiede lo stato di un singolo certificato.
    
    - _Vantaggi:_ Risposte rapide, traffico dati ridotto, stato aggiornato in tempo reale.
        
- **Problema Privacy OCSP:** La CA riceve le richieste di verifica dai client per ogni sito visitato, permettendo alla CA di tracciare la cronologia di navigazione degli utenti.
    
- **Soluzione (Bonus):** **OCSP Stapling**. Il server web scarica periodicamente la risposta OCSP firmata dalla CA e la invia ("spilla") al client durante l'handshake TLS. Il client non deve contattare la CA (privacy salva) e ha la prova di validità.
    

---

### 4. Autenticazione Three-Way e Anti-Replay

La Domanda d'Esame:

"Come usare la firma digitale per l'autenticazione prevenendo il Replay Attack?"

La Spiegazione (Il "Perché"):

Abbiamo detto che firmare un dato statico è pericoloso. Bisogna firmare qualcosa di fresco.

Lo standard X.509 definisce un protocollo a 3 vie per evitare di dipendere dagli orologi sincronizzati (che sono necessari se usi i Timestamp, come in Kerberos).

L'idea è scambiarsi dei Nonce e firmarli a vicenda.

Cosa scrivere all'esame:

Per prevenire il Replay, la firma digitale deve essere applicata a dati "freschi" (nonce o timestamp) e legata all'identità del destinatario (per evitare Reflection/MITM).

Protocollo a 3 vie (Three-Way Authentication):

1. **A $\to$ B:** $N_A$ (Alice invia il suo Nonce).
    
2. **B $\to$ A:** $N_B, Sign_{Sk_B}(N_A, N_B, A)$ (Bob firma il nonce di Alice, il proprio, e l'identità di Alice).
    
3. A $\to$ B: $Sign_{Sk_A}(N_B, B)$ (Alice firma il nonce di Bob e l'identità di Bob).
    
    Includendo il nome del destinatario nella firma, si previene che un attaccante possa riutilizzare il messaggio in un contesto diverso (Reflection).
    

---

### 5. Comandi OpenSSL (Analisi Pratica)

La Domanda Pratica:

"Analizza il comando: openssl x509 -in cert.pem -text -noout"

La Spiegazione (Il "Perché"):

Questo comando è il pane quotidiano per chi lavora con i certificati. Serve a leggere cosa c'è dentro un file .pem (che è illeggibile a occhio nudo perché è Base64) e vederne i dettagli (Chi l'ha emesso? Quando scade?).

**Cosa scrivere all'esame:**

- `openssl x509`: È il comando per la gestione dei certificati in formato X.509.
    
- `-in cert.pem`: Specifica il file di input contenente il certificato.
    
- `-text`: Decodifica il contenuto binario/Base64 e lo stampa in formato testuale leggibile dall'uomo (mostra Subject, Issuer, Validity, Public Key, Extensions, ecc.).
    
- `-noout`: Sopprime l'output della versione codificata del certificato (evita di ristampare il blocco `-----BEGIN CERTIFICATE-----`), mostrando solo il testo decodificato.