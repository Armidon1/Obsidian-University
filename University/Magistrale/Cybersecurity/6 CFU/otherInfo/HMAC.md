# **HMAC (Hash-based Message Authentication Code)**

> È una forma specifica di **[[MAC]] (Message Authentication Code)** che usa una **funzione di hash crittografica** (come [[SHA]]-256 o [[SHA]]-3) combinata con una **chiave segreta** per garantire **[[Integrity]]** e **[[Authenticity]]** dei messaggi.

**Come funziona:**

1. Mittente e destinatario condividono una chiave segreta.
    
2. Il mittente calcola un valore $HMAC = Hash(chiave \oplus opad ‖ Hash(chiave \oplus ipad ‖ messaggio))$. vedi che sono [[opad e ipad]] 
    
3. Il destinatario ricalcola l’[[HMAC]] e lo confronta con quello ricevuto.
    
4. Se coincidono → il messaggio **non è stato alterato** e **proviene da una fonte autentica**.
    
 
**Garantisce:**

- ✅ **Integrità** (il messaggio non è stato modificato)
    
- ✅ **Autenticità** (solo chi conosce la chiave può generare un HMAC valido)
    

**Non garantisce:**

- ❌ **[[Confidentiality]]** (il contenuto del messaggio non è cifrato)
    

**Esempi d’uso:** [[TLS]], IPsec, JWT (JSON Web Token), autenticazione API.

vedi anche la [[differenza tra GHASH e HMAC]]

## 🎲 HMAC-SHA256 come PRF

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

In PKCS #5 (visto in precedenza), PBKDF2 usa una PRF per iterare sulla password. La PRF scelta di default è quasi sempre **HMAC-SHA256**. L'obiettivo qui è generare una stringa di bit (la chiave derivata) che sembri casuale e non abbia pattern derivanti dalla password originale.

#### 3. HMAC_DRBG (Deterministic Random Bit Generator)

È uno standard NIST per generare numeri casuali crittograficamente sicuri (CSPRNG). Invece di usare un cifrario a blocchi (come in CTR_DRBG), usa HMAC-SHA256 per aggiornare lo stato interno e produrre bit casuali.

### Differenza Sottile: MAC vs PRF

Per un ingegnere, è utile distinguere le due "personalità" di HMAC:

|**Ruolo**|**Obiettivo**|**Proprietà Richiesta**|
|---|---|---|
|**Come MAC**|Autenticazione Messaggi|**Unforgeability:** Deve essere impossibile creare una coppia (messaggio, tag) valida senza la chiave.|
|**Come PRF**|Derivazione Chiavi / RNG|**Pseudorandomness:** L'output deve essere indistinguibile da una sequenza casuale uniforme.|

Poiché HMAC-SHA256 possiede la proprietà di _Pseudorandomness_, ottiene automaticamente (gratis) la proprietà di _Unforgeability_. Ecco perché è uno strumento così versatile.