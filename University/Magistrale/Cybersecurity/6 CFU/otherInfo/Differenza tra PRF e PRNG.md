# Differenza tra PRF e PRNG

## 1. Il Concetto in Breve

- **[[PRNG (Pseudo-Random Number Generator)]] (Generator):** È un "Espansore". Prende un piccolo seme e lo srotola in una **lunga sequenza** (stream) di numeri casuali. È **Stateful** (ha una memoria).
    
- **[[PRF (Pseudorandom Function)]] (Function):** È una "Mappatura". Prende una Chiave e un Input preciso, e restituisce un **singolo output** apparentemente casuale ma deterministico per quell'input. È **Stateless** (senza memoria).
    

---

## 2. PRNG (Pseudo-Random Number Generator)

Il PRNG è progettato per generare un **flusso continuo**.

- **Input:** Un **[[Seed]]** iniziale (una tantum).
    
- **Funzionamento:** Mantiene uno **stato interno**. Ogni volta che chiedi un numero, il PRNG aggiorna il suo stato e ti dà il prossimo pezzo della sequenza.
    
- **Matematica:** $G(s) \to \{b_1, b_2, b_3, \dots, b_n\}$
    
    - Dove $|output| \gg |seed|$.
        
- **Esempio:** [[CTR_DRBG]], RC4, [[ChaCha20]].
    
- **Uso:** Cifratura di interi flussi di dati (Stream Ciphers), generazione di chiavi multiple da un master secret.
    

> [!abstract] Metafora PRNG
> 
> È come un Libro di Numeri Casuali.
> 
> Il "Seed" ti dice a che pagina iniziare. Da lì in poi, leggi i numeri in sequenza, uno dopo l'altro. Devi tenere il segno (stato) di dove sei arrivato per leggere il prossimo.

---

## 3. PRF (Pseudo-Random Function)

La PRF è progettata per associare un output pseudo-casuale a uno specifico input, governato da una chiave segreta.

- **Input:** Una **Chiave ($K$)** e un **Dato ($x$)**.
    
- **Funzionamento:** Non ha memoria o storia. Se gli dai lo stesso $K$ e lo stesso $x$ oggi, domani e tra mille anni, ti darà sempre lo stesso output $y$. Se cambi anche un solo bit di $x$ (o $K$), l'output cambia completamente.
    
- **Matematica:** $F(K, x) \to y$
    
    - Dove $y$ ha una lunghezza fissa (es. 128 bit).
        
- **Esempio:** [[AES]] (un blocco cipher è una PRF/PRP), [[HMAC]], [[SHA-256]] (se usato con un segreto).
    
- **Uso:** Autenticazione messaggi, derivazione di una singola chiave, cifratura a blocchi.
    

> [!abstract] Metafora PRF
> 
> È come un Oracolo Magico.
> 
> Tu gli scrivi un bigliettino con una domanda ("Input") e lui ti risponde con una stringa incomprensibile ("Output").
> 
> Non c'è sequenza: non importa se hai fatto altre domande prima. La risposta dipende solo dalla domanda attuale e dalla magia (Chiave) dell'oracolo.

---

## 4. Tabella di Confronto

|**Caratteristica**|**PRNG (Generator)**|**PRF (Function)**|
|---|---|---|
|**Natura**|Generatore di Flusso (Stream)|Funzione Matematica (Mapping)|
|**Input Principale**|Seed iniziale|Chiave + Messaggio/Input specifico|
|**Memoria**|**Stateful** (Ha uno stato interno che evolve)|**Stateless** (Il risultato dipende solo dagli input attuali)|
|**Output**|Lunghezza variabile (quanto ne vuoi)|Lunghezza fissa (blocco)|
|**Obiettivo**|Espandere poca entropia in tanta entropia.|Creare una relazione input-output indistinguibile dal caso.|

---

## 5. La Relazione Tra i Due (Come costruire uno con l'altro)

In crittografia, spesso **costruiamo un PRNG usando una PRF**.

Il caso classico è la modalità **Counter Mode (CTR)**:

1. Prendiamo una **PRF** forte (es. [[AES]]).
    
2. Usiamo una Chiave ($K$) come Seed.
    
3. Per generare un flusso (PRNG), diamo in pasto alla PRF un contatore sequenziale ($1, 2, 3 \dots$):
    

$$\begin{align} \text{PRNG-Output}_1 &= \text{PRF}(K, 1) \\ \text{PRNG-Output}_2 &= \text{PRF}(K, 2) \\ \text{PRNG-Output}_3 &= \text{PRF}(K, 3) \end{align}$$

In questo modo, abbiamo trasformato una funzione stateless (AES) in un generatore di flusso stateful (il contatore è lo stato). Questo è esattamente come funziona [[CTR_DRBG]].

> [!tip] Exam Focus
> 
> Se il prof chiede: "AES è un PRNG o una PRF?"
> 
> - **AES (da solo)** è una **PRF** (tecnicamente una PRP - Permutation, perché invertibile). Prende input e chiave, dà output.
>     
> - **AES in modalità CTR** diventa un **PRNG**. Genera un flusso continuo.
>     

---

**Vedi anche:**

- [[PRNG (Pseudo-Random Number Generator)]]
    
- [[AES]]
    
- [[HMAC]]
    
- [[CS-PRNG based by Cipher of a Counter]]