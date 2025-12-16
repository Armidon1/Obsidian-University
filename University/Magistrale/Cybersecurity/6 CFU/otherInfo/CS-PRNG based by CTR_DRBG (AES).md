# CTR_DRBG (AES)

## 1. Definizione e Contesto

**CTR_DRBG** (Counter Mode Deterministic Random Bit Generator) è un algoritmo **[[CS-PRNG (Cryptographically Secure Pseudo-Random Number Generator)|PRNG]]** standardizzato dal **[[NIST]]** (pubblicazione speciale **SP 800-90A**).

Attualmente è considerato la Best Practice industriale per generare numeri casuali in ambito crittografico (usato in [[SSL]]/[[TLS]], SSH, Kernel Linux moderni, Windows).

Si basa sull'uso di un Cifrario a Blocchi (tipicamente [[AES]]) in modalità contatore.

> [!abstract] Evoluzione
> 
> È l'evoluzione moderna, formalizzata e sicura del concetto teorico di [[CS-PRNG based by "Cipher of a Counter"]].

## 2. Architettura Interna

Il generatore mantiene uno **Stato Interno** segreto composto da due elementi principali:

1. **Key ($K$):** Una chiave AES (es. 128 o 256 bit).
    
2. **Counter ($V$):** Un valore contatore (lungo quanto il blocco, 128 bit).
    

La sicurezza si basa sul fatto che, se la chiave $K$ è segreta, l'output di $AES_K(V)$ è indistinguibile dal rumore casuale per chiunque non possieda $K$.

## 3. L'Algoritmo (Semplificato)

Il funzionamento si divide in tre fasi: _Instanziazione_, _Generazione_ e _Aggiornamento_.

### A. Instanziazione (Seeding)

Il sistema raccoglie entropia vera (da un [[TRNG (True Random Number Generator)]]) per creare il **[[Seed]]** iniziale. Questo seed viene usato per derivare i valori iniziali di $K$ e $V$.

### B. Generazione (Generate Function)

Quando il sistema richiede bit casuali:

1. Incrementa il contatore: $V = (V + 1) \pmod {2^{128}}$.
    
2. Cifra il contatore con la chiave attuale: $\text{OutputBlock} = \text{AES}(K, V)$.
    
3. Ripete finché non ha prodotto abbastanza bit.
    
4. Alla fine, invoca la funzione di **Update** (cruciale per la sicurezza).
    

### C. Aggiornamento (Update Function)

Dopo ogni richiesta (o durante il reseeding), lo stato interno deve cambiare radicalmente per impedire che la compromissione futura riveli i dati passati.

$$K, V \leftarrow \text{Update}(K, V, \text{NewEntropy})$$

In pratica, si usa l'AES stesso per generare una nuova coppia $(K, V)$ cifrando il contatore attuale.

### Pseudocodice (dagli appunti)

```C
/* Stato Interno */
Key K
Counter V

/* Funzione Generate */
Loop until enough bits:
    V = (V + 1) mod (2^BlockSize)
    Out_Block = AES_Encrypt(K, V)
    Append Out_Block to Result

/* Funzione Update (Post-Generazione) */
Regenerate K and V by encrypting V+1, V+2... with current K
```

## 4. Proprietà di Sicurezza

Grazie alla robustezza di AES e al meccanismo di Update, CTR_DRBG garantisce:

1. **Imprevedibilità:** Senza la chiave $K$, è impossibile distinguere l'output da una sequenza casuale (Next-Bit Test).
    
2. **Backward Secrecy (Backtracking Resistance):** Se un attaccante scopre lo stato attuale ($K, V$), non può risalire agli output _precedenti_, perché la funzione di Update è One-Way (o meglio, invertire AES senza la vecchia chiave è impossibile).
    
3. **Forward Secrecy (Prediction Resistance):** Se il generatore fa **Reseeding** (inietta nuova entropia con la funzione Update), un attaccante che conosceva il vecchio stato non può più prevedere gli output _futuri_.
    

## 5. Perché è lo Standard? (Vantaggi)

|**Caratteristica**|**CTR_DRBG (AES)**|**Altri (es. BBS, Hash-DRBG)**|
|---|---|---|
|**Velocità**|**Altissima.** Le CPU moderne hanno istruzioni hardware dedicate (AES-NI) che calcolano AES in pochi cicli di clock.|Lenti (BBS) o mediamente veloci (Hash).|
|**Sicurezza**|Basata su AES (standard globale analizzato da decenni).|Basata su fattorizzazione o hash.|
|**Parallelismo**|Essendo basato su contatore, è possibile calcolare blocchi multipli in parallelo.|Spesso sequenziali.|

> [!warning] Limite di Sicurezza
> 
> Anche CTR_DRBG ha un limite: non si possono generare infiniti blocchi con la stessa chiave $K$ (limitazione teorica di AES).
> 
> Lo standard impone un Reseed obbligatorio dopo un certo numero di richieste (es. $2^{48}$ blocchi), per "rinfrescare" la chiave.

---

**Vedi anche:**

- [[CS-PRNG (Cryptographically Secure Pseudo-Random Number Generator)]]
    
- [[AES]]
    
- [[CS-PRNG based by "Cipher of a Counter"]]
    
- [[Seed]]