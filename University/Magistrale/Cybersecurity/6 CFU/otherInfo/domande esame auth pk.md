guardare sempre prima [[CS 6cfu - Domande esame]]

Basandomi rigorosamente sugli esami che hai inviato (2012-2025), ecco le domande d'esame e le relative spiegazioni per **Autenticazione a Chiave Pubblica, PKI e X.509**.

### 1. La Necessità della PKI (Domanda Fondamentale)

Domanda d'Esame:

"Cosa è un certificato digitale e quali problemi risolve? Quali controlli deve effettuare chi riceve un certificato?"

La Spiegazione (Il "Perché"):

Hai visto che l'autenticazione a chiave pubblica si basa sul possesso della chiave privata.

Io mando una sfida, tu la firmi con la tua privata, io verifico con la tua pubblica.

Funziona matematicamente. Ma c'è un buco enorme: Come faccio a sapere che la chiave pubblica è davvero tua?

Se Trudy mi manda la sua chiave pubblica dicendo "Sono Alice", e io ci credo, Trudy può impersonare Alice firmando con la sua privata.

La PKI (Public Key Infrastructure) serve a legare un'identità (Alice) a una chiave pubblica in modo fidato.

**Cosa scrivere all'esame:**

- **Certificato Digitale (X.509):** È un documento firmato da un'autorità fidata (CA - Certification Authority) che attesta che una certa Chiave Pubblica appartiene a un certo Soggetto (Subject).
    
- **Problema risolto:** Risolve il problema dell'autenticità delle chiavi pubbliche e previene attacchi Man-in-the-Middle sulla distribuzione delle chiavi.
    
- **Controlli da fare:**
    
    1. Verificare la **Firma della CA** sul certificato.
        
    2. Controllare la **Validità Temporale** (non scaduto).
        
    3. Controllare lo stato di **Revoca** (CRL o OCSP).
        
    4. Controllare che il **Subject** corrisponda all'entità attesa (es. il dominio del sito web).
        

---

### 2. Autenticazione Challenge-Response Asimmetrica

Domanda d'Esame:

"Descrivi un protocollo di autenticazione basato su chiave pubblica. Quali sono i vantaggi rispetto a quello simmetrico?"

La Spiegazione (Il "Perché"):

Nel simmetrico, Alice e Bob devono condividere un segreto $K$. Se Bob viene bucato, il segreto di Alice è perso.

Nell'asimmetrico, Alice ha la sua chiave privata $Sk_A$. Bob ha solo la pubblica $Pk_A$. Se Bob viene bucato, l'attaccante trova $Pk_A$ (che è pubblica comunque) e non può impersonare Alice. Questo è il vantaggio enorme: Nessun segreto condiviso.

**Cosa scrivere all'esame:**

- **Protocollo:**
    
    1. $B \to A$: $N_B$ (Nonce/Sfida)
        
    2. $A \to B$: $Sign_{Sk_A}(N_B)$ (Alice firma la sfida)
        
    3. $B$: Verifica $Verify(Pk_A, N_B, \text{Firma})$
        
- **Vantaggi:**
    
    1. **Non-Ripudio:** La firma prova che è stata proprio Alice (solo lei ha la privata).
        
    2. **Sicurezza in caso di compromissione server:** Se il server (Bob) viene compromesso, le credenziali di Alice (chiave privata) non sono esposte.
        
    3. **Scalabilità:** Non serve scambiare chiavi segrete a priori.
        

---

### 3. Revoca dei Certificati: CRL vs OCSP

Domanda d'Esame:

"Confronta CRL e OCSP. Quali sono i vantaggi di OCSP? Perché OCSP presenta problemi di privacy?"

La Spiegazione (Il "Perché"):

Un certificato può essere revocato prima della scadenza (es. chiave privata rubata).

- **CRL (Certificate Revocation List):** La CA pubblica una "lista nera" gigante di tutti i certificati revocati. Il client deve scaricarla tutta. È lento e pesante.
    
- **OCSP (Online Certificate Status Protocol):** Il client chiede alla CA _solo_ lo stato di _quel_ certificato specifico. "Il cert 123 è valido?". La CA risponde "Sì/No" con una risposta firmata. È veloce.
    

Il problema Privacy di OCSP:

Se ogni volta che visiti pornhub.com il tuo browser chiede alla CA "È valido il certificato di Pornhub?", la CA sa esattamente quali siti visiti e quando.

**Cosa scrivere all'esame:**

- **CRL:** Lista completa dei certificati revocati. Lenta da scaricare, non sempre aggiornata in tempo reale (window of vulnerability).
    
- **OCSP:** Protocollo query-response in tempo reale per un singolo certificato. Più efficiente e tempestivo.
    
- **Privacy OCSP:** La CA riceve le richieste di verifica e può tracciare la navigazione degli utenti (sa quale sito stanno visitando).
    
- **OCSP Stapling (Bonus):** Il server web scarica lui stesso la prova OCSP firmata dalla CA e la "spilla" (staple) al certificato inviato al client. Risolve il problema privacy e carico sulla CA.
    

---

### 4. X.509 e Autenticazione Three-Way (Anti-Replay)

Domanda d'Esame:

"Come usare la firma digitale per l'autenticazione prevenendo il Replay Attack?"

La Spiegazione (Il "Perché"):

Se firmo un messaggio statico ("Sono Alice"), Trudy lo registra e lo riusa.

Devo firmare qualcosa che cambia sempre: un Nonce o un Timestamp.

Nello standard X.509 "Three-Way Authentication", si usano i Nonce per non dipendere dagli orologi sincronizzati (che sono un problema).

Cosa scrivere all'esame:

Per prevenire il replay, la firma digitale deve essere applicata su dati freschi, tipicamente un Nonce inviato dal verificatore.

Protocollo:

1. $A \to B$: $N_A$ (Alice inizia)
    
2. $B \to A$: $N_B, Sign_B(N_A, N_B, A)$ (Bob firma la sfida di Alice e la sua, legandole ad A)
    
3. $A \to B$: $Sign_A(N_B, B)$ (Alice firma la sfida di Bob legandola a B)
    
    Questo "legame" (firmare l'identità del destinatario) previene attacchi di tipo Man-in-the-Middle e Reflection.
    

### 5. OpenSSL e Certificati

Domanda Pratica:

"Analizza il comando: openssl x509 -in cert.pem -text -noout"

**Cosa scrivere all'esame:**

- `openssl x509`: Tool per gestire certificati X.509.
    
- `-in cert.pem`: File di input contenente il certificato.
    
- `-text`: Stampa il certificato in formato testuale leggibile (decodifica ASN.1).
    
- `-noout`: Non stampa la versione codificata (PEM/Base64) in output, solo il testo decodificato. Serve per ispezionare il contenuto (Issuer, Subject, Validità, Chiave Pubblica).
    

---

### Sintesi per il Ripasso (Memorizza Questo)

1. **A cosa serve il Certificato?** A legare Chiave Pubblica $\leftrightarrow$ Identità (garantito dalla CA).
    
2. **OCSP vs CRL:** OCSP è real-time e leggero, ma traccia l'utente. CRL è offline e pesante.
    
3. **Auth Asimmetrica:** $A$ firma il Nonce di $B$. Nessun segreto condiviso.
    
4. **Sicurezza:** Se $Pk_A$ non è certificata, l'autenticazione è vulnerabile a MITM.