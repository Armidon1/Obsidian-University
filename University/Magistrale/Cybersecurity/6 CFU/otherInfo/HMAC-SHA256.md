# 🛡️ HMAC-SHA256

### Definizione

**[[HMAC]]-SHA256** (Hash-based Message Authentication Code using [[SHA-2]]56) è una costruzione specifica di **[[MAC]] (Message Authentication Code)** che utilizza la funzione di hash crittografica **SHA-256** in combinazione con una **chiave segreta crittografica**.

È lo standard industriale _de facto_ per garantire contemporaneamente:

1. **Integrità:** Il messaggio non è stato modificato.
    
2. **Autenticità:** Il messaggio è stato creato da qualcuno che possiede la chiave segreta.
    

### Perché HMAC? (Il Problema di "Hash(Key || Msg)")

Per un ingegnere, è fondamentale capire perché non usiamo semplicemente `SHA256(Key + Message)`.

Le funzioni di hash basate sulla costruzione Merkle-Damgård (come SHA-256, SHA-1, MD5) sono vulnerabili al **Length Extension Attack**.2

- _Il problema:_ Se un attaccante conosce `H(Key || Messaggio)` e la lunghezza di `Key || Messaggio`, può calcolare l'hash valido di `Key || Messaggio || Estensione` **senza conoscere la Key**.
    
- _La soluzione HMAC:_ HMAC utilizza una struttura a **doppio hashing annidato** che immunizza la funzione contro questo attacco.
    

### Funzionamento Tecnico (La Costruzione)

L'algoritmo HMAC-SHA256 è definito come:

$$HMAC(K, m) = \text{SHA256}((K' \oplus opad) \mathbin{||} \text{SHA256}((K' \oplus ipad) \mathbin{||} m))$$

Dove:

- **$K'$**: È la chiave $K$, normalizzata. Se $K$ è più lunga della dimensione del blocco (64 byte per SHA-256), viene prima hashata. Se è più corta, viene riempita con zeri (padded).
    
- **$ipad$**: Inner padding (byte `0x36` ripetuto 64 volte).
    
- **$opad$**: Outer padding (byte `0x5c` ripetuto 64 volte).
    
- **$\oplus$**: Operazione XOR.
    
- **$||$**: Concatenazione.
    

In pratica, esegue due passaggi:

1. **Inner Hash:** Hasha il messaggio con una versione "mascherata" della chiave (XOR con ipad).
    
2. **Outer Hash:** Hasha il risultato del primo passaggio con un'altra versione "mascherata" della chiave (XOR con opad).
    

### Specifiche Ingegneristiche

|**Caratteristica**|**Dettaglio Tecnico**|
|---|---|
|**Output Size**|**256 bit (32 byte)**. Spesso codificato in Hex (64 caratteri) o Base64 (44 caratteri).|
|**Block Size**|512 bit (64 byte). Questo è il blocco interno su cui opera la funzione di compressione di SHA-256.|
|**Dimensione Chiave**|Può essere di qualsiasi lunghezza, ma per sicurezza ottimale dovrebbe essere **almeno uguale all'output size (32 byte)**. Chiavi più lunghe del block size (64 byte) non aggiungono sicurezza extra (vengono hashati).|
|**Performance**|Molto veloce. Richiede essenzialmente 2 chiamate alla funzione di compressione SHA-256 in più rispetto all'hashing semplice del solo messaggio. Ideale per volumi elevati di richieste.|

### Applicazioni Comuni

- **JWT (JSON Web Tokens):** HMAC-SHA256 (indicato come algoritmo `HS256`) è l'algoritmo di firma simmetrico standard per i token web.
    
- **Sicurezza API (es. AWS Signature v4):** Molte API REST richiedono che ogni richiesta HTTP includa un header di firma calcolato tramite HMAC-SHA256 usando la _Secret Key_ dell'utente. Questo impedisce la manomissione della richiesta (es. cambiare l'importo di un ordine) durante il transito.
    
- **Autenticazione Challenge-Response:** Usato per provare la conoscenza di una password senza trasmetterla (es. in protocolli SASL o CRAM-MD5 aggiornati).


---

## 🎲 HMAC-SHA256 come [[PRF (Pseudorandom Function)]]

### Il Concetto

Sebbene HMAC sia nato principalmente come **MAC** (per garantire integrità e autenticità), la sua costruzione crittografica soddisfa anche la definizione formale di una **PRF (Pseudo-Random Function)**.

Questo significa che HMAC-SHA256 non si limita a "firmare" i dati, ma può essere utilizzato come un generatore di output che sono **matematicamente indistinguibili dal rumore casuale**, a condizione che la chiave sia segreta.

### Perché è una PRF? (La Prova di Sicurezza)

Per un ingegnere, HMAC-SHA256 è una PRF perché rispetta le seguenti proprietà:

1. **Output Deterministico ma "Caotico":** Dato un input $x$ e una chiave $K$, produce sempre lo stesso output $y$. Tuttavia, non esiste alcuna correlazione rilevabile tra $x$ e $y$ (non linearità).
    
2. **Indistinguibilità:** Senza conoscere la chiave $K$, se un avversario osserva una serie di output $HMAC(K, x_1), HMAC(K, x_2), \dots$, non può distinguerli da una sequenza di stringhe di 256 bit generate da un vero generatore casuale (TRNG).
    
3. **Compressione come PRF:** La sicurezza di HMAC come PRF si basa sull'assunzione che la **funzione di compressione** sottostante di SHA-256 agisca essa stessa come una PRF quando una parte dell'input (la chiave) è segreta.
    

### Applicazioni di HMAC _come_ PRF (Non per firmare)

Il fatto che HMAC sia una PRF eccellente è il motivo per cui viene utilizzato in ambiti che non c'entrano nulla con l'autenticazione dei messaggi, ma riguardano la **generazione di chiavi**:

#### 1. HKDF (HMAC-based Key Derivation Function) - RFC 5869

Questo è l'uso più critico nell'ingegneria moderna (es. in **TLS 1.3**). HKDF usa HMAC-SHA256 non per autenticare, ma per **distillare entropia**.

- **Extract:** Usa HMAC per "pulire" una chiave di input debole (come un segreto Diffie-Hellman) in una chiave maestra uniforme pseudo-casuale.
    
- Expand: Usa HMAC in un ciclo per generare (espandere) multiple chiavi crittografiche (es. chiave AES, chiave IV, chiave MAC) da quella singola chiave maestra.
    
    $$Output_i = HMAC(Key, Output_{i-1} \mathbin{||} info \mathbin{||} counter)$$
    
    Qui, HMAC agisce esattamente come un generatore di numeri casuali.
    

#### 2. PBKDF2 (Password-Based Key Derivation)

In [[PKCS]] #5 (visto in precedenza), [[PBKDF2]] usa una PRF per iterare sulla password. La PRF scelta di default è quasi sempre **HMAC-SHA256**. L'obiettivo qui è generare una stringa di bit (la chiave derivata) che sembri casuale e non abbia pattern derivanti dalla password originale.

#### 3. HMAC_DRBG (Deterministic Random Bit Generator)

È uno standard NIST per generare numeri casuali crittograficamente sicuri (CSPRNG). Invece di usare un cifrario a blocchi (come in CTR_DRBG), usa HMAC-SHA256 per aggiornare lo stato interno e produrre bit casuali.

### Differenza Sottile: MAC vs PRF

Per un ingegnere, è utile distinguere le due "personalità" di HMAC:

|**Ruolo**|**Obiettivo**|**Proprietà Richiesta**|
|---|---|---|
|**Come MAC**|Autenticazione Messaggi|**Unforgeability:** Deve essere impossibile creare una coppia (messaggio, tag) valida senza la chiave.|
|**Come PRF**|Derivazione Chiavi / RNG|**Pseudorandomness:** L'output deve essere indistinguibile da una sequenza casuale uniforme.|

Poiché HMAC-SHA256 possiede la proprietà di _Pseudorandomness_, ottiene automaticamente (gratis) la proprietà di _Unforgeability_. Ecco perché è uno strumento così versatile.