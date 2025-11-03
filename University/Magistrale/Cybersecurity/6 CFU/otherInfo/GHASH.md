## 🔐 Funzione GHASH: Componente di Autenticazione (GCM)

La funzione **GHASH** è il meccanismo chiave utilizzato dal Galois/Counter Mode (GCM) per calcolare il **Message Authentication Code ([[MAC]])**, o **Authentication Tag**, che garantisce l'[[Integrity]] e l'[[Authenticity]] dei dati.
![[Pasted image 20251103095617.png]]

### 1. Fondamenti Matematici: Campo di Galois $\mathbf{GF(2^{128})}$

GHASH opera interamente nel **Campo Finito di Galois $\mathbf{GF(2^{128})}$**.

- **Campo Finito:** Permette di eseguire operazioni complesse (come la moltiplicazione) su blocchi di **128 bit** (la dimensione standard di un blocco in AES) garantendo che il risultato sia **sempre un blocco di 128 bit** (evitando l'overflow).
    
- **Aritmetica:**
    
    - **Addizione ($\mathbf{\oplus}$):** Corrisponde all'**XOR bit-a-bit** tra due blocchi di 128 bit.
        
    - **Moltiplicazione ($\mathbf{\cdot}$):** È una **moltiplicazione "carry-less"** (senza riporto) tra polinomi in $GF(2^{128})$.
        
- Riduzione Polinomiale: Per assicurare che la moltiplicazione rimanga in 128 bit, il risultato viene ridotto utilizzando il polinomio irriducibile fisso specificato:
    
    $$P(x) = x^{128} + x^7 + x^2 + x + 1$$
    
- **Performance:** L'uso di questa moltiplicazione carry-less in $GF(2^{128})$ è fondamentale per le **alte prestazioni** del GCM.
    

---

### 2. Hash Subkey ($\mathbf{H}$)

Prima di elaborare i dati, GHASH richiede una **chiave hash monouso** (la subkey $H$).

- Derivazione: $H$ è derivata cifrando un blocco di zeri ($0^{128}$) con la chiave di cifratura simmetrica $K$ (la stessa usata per il Counter Mode):
    
    $$H = E_K(0^{128})$$
    
    Dove $E_K$ è l'algoritmo AES (o simile) con la chiave $K$.
    

---

### 3. Struttura degli Input e Padding
![[Pasted image 20251103095625.png]]

L'input totale per la funzione GHASH è una singola sequenza di dati composta da **tre parti concatenate** :

$$\text{Input: } \mathbf{AAD || \text{Ciphertext} || \text{Length Block}}$$

Per garantire che l'input sia sempre composto da blocchi di 128 bit, si applica il seguente **padding**:

1. [[GHASH#AAD|AAD]] (Dati Aggiuntivi Autenticati): Viene riempito con zeri a un multiplo di 128 bit.
    
    $$\text{AAD Padded} = (A_1, A_2, ..., A_m)$$
    
2. Ciphertext (Testo Cifrato): Viene riempito con zeri a un multiplo di 128 bit.
    
    $$\text{Ciphertext Padded} = (C_1, C_2, ..., C_n)$$
    
3. Length Block (Blocco Lunghezza): Un blocco finale di 128 bit viene aggiunto. Contiene le lunghezze originali (in bit) di AAD e Ciphertext, ciascuna codificata come un intero a 64 bit (formato big-endian).
    
    $$\text{Length Block} = (\text{len}(A) \text{ come } 64 \text{-bit}) || (\text{len}(C) \text{ come } 64 \text{-bit})$$
    

---

### 4. Algoritmo di Calcolo (Iterazione Hash)

GHASH è una funzione hash iterativa che elabora i blocchi di input $X_1, X_2, ..., X_k$ in sequenza.

- **Funzionamento:** Ad ogni passo, il risultato hash precedente viene moltiplicato per la subkey $H$, e poi viene aggiunto (XOR) il blocco di dati corrente.
    
- Formula Ricorsiva (per gli appunti): Il tuo appunto $X_i = (X_{i-1} \oplus C_i) \cdot H$ è una forma semplificata. La forma completa, che evidenzia la catena di operazioni, è la seguente:
    
    $$GHASH(X_1, X_2, ..., X_k) = ((((X_1 \cdot H) \oplus X_2) \cdot H \oplus ...) \oplus X_k) \pmod{P(x)}$$
    

Il **risultato finale** di GHASH è un valore di **128 bit** che, una volta XORato con il blocco cifrato $E_K(0^{128})$ (lo stesso $H$), produce l'**Authentication Tag** definitivo.

## AAD
È un'ottima domanda, perché il nome **AAD** (Dati Aggiuntivi Autenticati) descrive perfettamente il suo **scopo** e la sua **funzione** all'interno dei cifrari autenticati come GCM.

Il termine "AAD" deriva dall'inglese **"Additional Authenticated Data"**.

---

## 🔑 La Funzione e il Significato di AAD

Il concetto di AAD è fondamentale nei moderni schemi di crittografia come GCM (che utilizza GHASH) e si scompone in due parti principali:

### 1. **"Authenticated" (Autenticati)**

- **Scopo:** L'AAD fa parte dell'input della funzione hash (GHASH) che calcola l'**Authentication Tag** (o MAC).
    
- **Risultato:** Essendo incluso nell'hash, il destinatario può **verificare l'integrità e l'autenticità** dell'AAD. Se un attaccante modifica anche un solo bit dell'AAD, il tag calcolato non corrisponderà più a quello ricevuto, e l'autenticazione fallirà.
    

### 2. **"Additional Data" (Dati Aggiuntivi)**

- **Scopo:** L'AAD contiene dati che sono **necessari al destinatario** per elaborare correttamente il messaggio, ma che **non devono essere crittografati** (ovvero, possono viaggiare in chiaro).
    
- **Esempi Comuni:**
    
    - **Indirizzi:** Indirizzi IP, porte di destinazione, o il destinatario del messaggio (in un'intestazione di protocollo).
        
    - **Timestamp:** L'ora di invio o la validità del messaggio.
        
    - **Numero di Versione:** La versione del protocollo o dell'applicazione.
        

### 💡 Riassumendo in un Esempio

Immagina di inviare un pacchetto di rete sicuro.

- **Testo Cifrato (Ciphertext):** Il contenuto segreto (es. il testo della tua email). **Deve essere crittografato e autenticato.**
    
- **AAD:** L'intestazione del pacchetto che indica l'indirizzo IP di destinazione e il numero di porta. **Non deve essere segreto** (i router lo devono leggere per instradare il pacchetto), ma **deve essere autenticato**.
    
    - **Il rischio senza AAD:** Se un attaccante potesse modificare l'indirizzo di destinazione (l'AAD) senza che il destinatario se ne accorga, reindirizzerebbe il messaggio a sé stesso, anche se il contenuto (il ciphertext) rimane sicuro.
        

**L'AAD permette di legare in modo crittografico i dati in chiaro (intestazioni, metadati) al testo cifrato,** garantendo che non siano stati manomessi durante la trasmissione.

L'utente chiede come viene creato l'AAD (Dati Aggiuntivi Autenticati) in un protocollo come il GCM.

1. **Interpretazione della domanda:** L'utente chiede da dove provengono i dati che costituiscono l'AAD e se c'è un processo crittografico per crearli, come avviene per la chiave $H$.
    
2. **Differenza chiave AAD vs. Testo Cifrato:** L'AAD non viene _creato_ crittograficamente (come il ciphertext). È semplicemente un dato esterno, non segreto.
    
3. **Fonte di AAD:** I dati AAD provengono tipicamente dai metadati o dalle intestazioni del protocollo di comunicazione. Non è un dato generato _dall'algoritmo GCM_.
    
4. Processo di AAD in GCM: L'unico "processo" che subisce l'AAD è la preparazione per la funzione GHASH:
    
    a. Viene raccolto dal mittente.
    
    b. Viene concatenato al ciphertext (prima del blocco lunghezza).
    
    c. Viene sottoposto a padding con zeri per essere multiplo di 128 bit.
    
5. **Risposta strutturata:**
    
    - Chiarezza: L'AAD non viene generato, ma è un _input_ esterno.
        
    - Origine: Intestazioni, metadati, dati in chiaro.
        
    - Preparazione: L'unico passo "tecnico" è il padding.
        

Procedo con la risposta. L'AAD (Dati Aggiuntivi Autenticati) non viene creato dall'algoritmo crittografico (come avviene per il testo cifrato o la chiave hash), ma è un **input esterno** fornito al protocollo.

In sostanza, l'AAD è costituito da **metadati** o **dati di controllo** che sono già presenti nel sistema o nel protocollo di comunicazione.

Ecco i passaggi che definiscono l'AAD nel contesto di un cifrario autenticato come GCM:

---

## 1. Origine: Dati Esterni al Cifrario

L'AAD non viene generato, ma viene **selezionato** dal mittente. Proviene da dati che devono essere trasmessi in **chiaro** (non crittografati), ma la cui integrità deve essere garantita.

- **Esempi tipici:**
    
    - **Intestazioni di pacchetti (network):** Indirizzi IP, numeri di porta o l'identificativo della sessione. Questi dati devono essere leggibili dai nodi intermedi per instradare il messaggio, ma non devono essere modificabili.
        
    - **Timestamp o ID di messaggi:** Dati usati per tracciare o ordinare i messaggi.
        
    - **Chiave di Inizializzazione (IV/Nonce):** Anche se a volte trasmesso separatamente, può essere trattato come AAD per garantirne l'autenticità.
        

## 2. Preparazione: Formattazione per GHASH

Dopo essere stato fornito al modulo GCM, l'AAD viene preparato per essere elaborato dalla funzione hash GHASH. L'unico passaggio di "creazione" o trasformazione è il **Padding**.

1. **Raccolta:** Il mittente raccoglie la sequenza di bit o byte che costituiscono l'AAD.
    
2. **Concatenazione (Logica):** L'AAD viene concatenato idealmente al Testo Cifrato per formare il corpo principale dei dati da autenticare.
    
3. **Padding a 128 bit (Se Necessario):** La funzione GHASH elabora i dati in blocchi di 128 bit. Se l'AAD totale (prima della concatenazione con il Ciphertext) non è un multiplo esatto di 128 bit, viene **riempito con bit a zero** fino a raggiungere la dimensione del blocco successivo di 128 bit.
    

$$\text{AAD Padded} = \text{AAD Originale} \ || \ 000...$$

Questo blocco di AAD "paddato" è ciò che viene fornito come input ($A_1, A_2, ..., A_m$) alla funzione GHASH, assicurando che tutti i calcoli successivi in $GF(2^{128})$ siano eseguiti su blocchi di dimensione standard.

vedi anche la [[differenza tra GHASH e HMAC]]