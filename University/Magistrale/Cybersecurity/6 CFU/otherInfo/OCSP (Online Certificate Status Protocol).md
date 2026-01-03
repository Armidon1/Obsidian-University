# OCSP (Online Certificate Status Protocol): La Verifica in Tempo Reale

**Tags:** #ingegneria #security #pki #ocsp #revocation #rfc6960

## 1. Definizione e Contesto

L'OCSP è il protocollo moderno per verificare la validità di un certificato digitale in tempo reale, superando i limiti di latenza e dimensione delle CRL.

È definito nello standard RFC 6960.

Invece di scaricare una lista statica di tutti i certificati revocati (come avviene con la CRL), il client interroga direttamente un'autorità competente chiedendo lo stato di uno specifico certificato.

### Differenza Concettuale

- **CRL:** "Dammi la lista di _tutti_ i passaporti rubati." (Approccio Offline/Batch)
    
- **OCSP:** "Questo _specifico_ passaporto numero 12345 è valido?" (Approccio Online/Query)
    

---

## 2. Architettura Request/Response

Il protocollo funziona secondo un modello client-server molto semplice.

**Il flusso logico è:**

$$\text{Client} \xrightarrow{\text{Query (Serial Number)}} \text{OCSP Responder} \xrightarrow{\text{Signed Response}} \text{Client}$$

### Le Risposte Possibili

Il Responder (spesso gestito dalla CA) può restituire tre stati:

1. **Good:** Il certificato non è revocato (nota: non garantisce che sia stato emesso, solo che non è nella lista nera).
    
2. **Revoked:** Il certificato è stato invalidato (pericolo!).
    
3. **Unknown:** La CA non ha informazioni su questo certificato (spesso interpretato come errore o certificato falso).
    

---

## 3. Struttura del Messaggio

I messaggi OCSP sono strutture ASN.1 leggere.

### OCSP Request

Contiene essenzialmente l'identificativo del certificato da controllare.

- **CertID:** Composto dall'hash dell'Issuer (Nome e Chiave) e dal **Serial Number** del certificato target.
    
- **Nonce (Opzionale):** Un numero casuale per prevenire attacchi di replay (evita che un attaccante ti rispedisca una vecchia risposta "Good" dopo che il certificato è stato revocato).
    

### OCSP Response

È un messaggio firmato digitalmente per garantirne l'autenticità.

**The response structure contains:**

Plaintext

```
OCSPResponse ::= SEQUENCE {
    responseStatus         OCSPResponseStatus,
    responseBytes          [0] EXPLICIT ResponseBytes OPTIONAL
}

BasicOCSPResponse ::= SEQUENCE {
    tbsResponseData      ResponseData,
    signatureAlgorithm   AlgorithmIdentifier,
    signature            BIT STRING,
    certs                [0] EXPLICIT SEQUENCE OF Certificate OPTIONAL
}
```

> [!abstract] Code Analysis
> 
> Campi Critici:
> 
> - **CertStatus:** Lo stato (Good/Revoked/Unknown).
>     
> - **ThisUpdate:** Quando è stata generata questa risposta.
>     
> - **NextUpdate:** Fino a quando questa risposta è considerata fresca.
>     
> - **Signature:** La firma del Responder (senza questa, chiunque potrebbe falsificare uno stato "Good").
>     

---

## 4. OCSP Stapling (L'Ottimizzazione Vitale)

L'OCSP standard ha due grossi problemi:

1. **Privacy:** La CA viene a sapere ogni volta che un utente visita un sito (perché riceve la richiesta OCSP).
    
2. **Performance:** Il browser deve fare una connessione extra (DNS lookup + TCP connect) al Responder prima di caricare il sito.
    

La soluzione è l'**OCSP Stapling** (RFC 6066).

### Come funziona

Invece di far chiamare la CA al _client_, è il **Server Web** stesso a farlo.

1. Il Server Web (es. `google.com`) contatta periodicamente la CA.
    
2. Ottiene una risposta OCSP firmata ("Il mio certificato è valido").
    
3. Il Server "spilla" (staples) questa risposta firmata direttamente dentro l'handshake TLS (nel messaggio `CertificateStatus`).
    
4. Il Client riceve il certificato **E** la prova di validità in un solo colpo.
    

> [!tip] Exam Focus
> 
> Vantaggi dello Stapling:
> 
> - **Zero Latenza:** Nessuna connessione extra per il client.
>     
> - **Privacy Totale:** La CA vede solo le richieste del Server, non gli IP degli utenti finali.
>     
> - **Robustezza:** Se il server OCSP della CA va offline, il sito web continua a funzionare servendo l'ultima risposta firmata valida (cachata).
>     

---

## 5. Sintesi: OCSP vs CRL

|**Caratteristica**|**OCSP (Standard)**|**CRL**|
|---|---|---|
|**Granularità**|Verifica puntuale (1 certificato)|Verifica batch (Tutta la lista)|
|**Tempestività**|Quasi Real-time|Ritardo dovuto al `NextUpdate`|
|**Banda**|Leggera (Pochi byte)|Pesante (Download MB)|
|**Privacy**|Pessima (CA traccia gli utenti)|Ottima (Check locale)|
|**Resilienza**|Se Responder è down, il browser si blocca (Soft-fail)|Se download fallisce, si usa cache vecchia|

> [!failure] Common Pitfall
> 
> OCSP "Soft-Fail": Molti browser moderni (come Chrome) usano una politica "Soft-Fail". Se il controllo OCSP fallisce (es. server down o bloccato da firewall), il browser assume che il certificato sia valido e procede. Questo perché un "Hard-Fail" romperebbe troppi siti legittimi. L'OCSP Stapling risolve questo problema permettendo al server di garantire la consegna della prova.