# 🐪 Criptosistema ElGamal

### Definizione

**ElGamal** è un **criptosistema asimmetrico (a chiave pubblica)** sviluppato da Taher Elgamal. È un sistema flessibile che può essere utilizzato sia per la **cifratura** (confidenzialità) sia per la **firma digitale** (autenticazione).

La sicurezza del sistema ElGamal (sia per la cifratura che per la firma) si basa sulla difficoltà computazionale del **Problema del Logaritmo Discreto (DLP)** e del relativo **Problema Computazionale di Diffie-Hellman (CDH)** su un campo finito.

### Come Funziona (Cifratura)

ElGamal è noto per la sua **cifratura probabilistica**: cifrare lo stesso testo in chiaro più volte produce testi cifrati diversi, una proprietà che aumenta la sicurezza contro certi attacchi crittanalitici (a differenza di RSA "textbook" che è deterministico).

#### 1. Parametri Comuni

Prima di tutto, la comunità (o il sistema) si accorda su due parametri pubblici:

- $p$: Un numero primo molto grande (il _modulo_).
    
- $g$: Un generatore (o _base_) del gruppo moltiplicativo modulo $p$.
    

#### 2. Generazione delle Chiavi (Es. Bob)

- **Chiave Privata $b$:** Bob sceglie un numero intero $b$ casuale e segreto.
    
- **Chiave Pubblica $B$:** Bob calcola $B = g^b \pmod p$.
    
- _La chiave pubblica di Bob è $(p, g, B)$. La sua chiave privata è $b$._
    

#### 3. Cifratura (Alice invia $M$ a Bob)

Per inviare un messaggio $M$ (rappresentato come un numero) a Bob, Alice:

1. Ottiene la chiave pubblica di Bob $(p, g, B)$.
    
2. **Sceglie un numero casuale $k$** (una chiave "effimera" o _nonce_) per questa singola sessione. Questo $k$ deve essere segreto e usato una sola volta.
    
3. Calcola due componenti per il testo cifrato, $C_1$ e $C_2$:
    
    - $C_1 = g^k \pmod p$
        
    - $C_2 = M \cdot B^k \pmod p$
        
4. Alice invia la coppia $(C_1, C_2)$ come testo cifrato.
    

#### 4. Decifratura (Bob riceve $C_1, C_2$)

Per recuperare $M$, Bob usa la sua chiave privata $b$:

1. Calcola il segreto condiviso (in stile Diffie-Hellman) usando $C_1$:
    
    - $S = C_1^b \pmod p \quad (\text{che è } (g^k)^b = g^{kb} \pmod p)$
        
2. Calcola l'**inverso moltiplicativo** $S^{-1}$ di $S$ modulo $p$.
    
3. Decifra il messaggio $M$ "rimuovendo" la maschera:
    
    - $M = C_2 \cdot S^{-1} \pmod p$
        

Perché funziona:

$C_2 \cdot (S)^{-1} \equiv (M \cdot B^k) \cdot (g^{kb})^{-1} \equiv (M \cdot (g^b)^k) \cdot (g^{kb})^{-1} \equiv M \cdot g^{bk} \cdot (g^{bk})^{-1} \equiv M \pmod p$

### Dettagli Tecnici e Implicazioni per Ingegneri

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Sicurezza**|Basata sul **Problema del Logaritmo Discreto (DLP)**. Trovare $b$ da $(g, p, B)$ è computazionalmente infattibile.|
|**Svantaggio: Dimensione**|**Espansione del Messaggio:** Il testo cifrato $(C_1, C_2)$ è **due volte più grande** del testo in chiaro originale $M$. Questo è uno svantaggio significativo rispetto a RSA.|
|**Vantaggio: Probabilistico**|Grazie all'uso del $k$ casuale, la cifratura è probabilistica. Questo previene attacchi _chosen-plaintext_ che si basano sulla ricerca di pattern nel testo cifrato.|
|**Vulnerabilità (Riuso di $k$)**|Il riutilizzo dello stesso $k$ per due messaggi diversi è **catastrofico** e porta alla compromissione totale della chiave privata. È essenziale un **RNG (Random Number Generator)** sicuro.|
|**Firma Digitale**|La variante **ElGamal Signature Scheme** (base per DSA ed ECDSA) utilizza principi simili per creare e verificare firme basate sul DLP.|