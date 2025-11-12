# **Campo di Galois (Galois Field, $GF$)**

> È una **struttura algebrica finita** con un **numero limitato di elementi** in cui è possibile definire **operazioni di somma e moltiplicazione** che soddisfano le proprietà dei campi (associativa, commutativa, esistenza dell’inverso, ecc.).  
> È molto usato in **crittografia**, **codici correttivi** e **teoria dei numeri**.

---

**Caratteristiche principali:**

1. **Numero finito di elementi:** un campo di Galois $GF(pⁿ)$ contiene esattamente ( $p^n$ ) elementi, dove:
    
    - ( $p$ ) è un numero primo (base del campo)
        
    - ( $n$ ) è un intero positivo (estensione del campo)
        
2. **Operazioni chiuse:**
    
    - Somma e moltiplicazione tra elementi del campo producono sempre elementi del campo.
        
3. **Inverso esistente:**
    
    - Ogni elemento diverso da zero ha un **[[Multiplicative Inverse|inverso moltiplicativo]]**.
        
4. **Uso in crittografia:**
    
    - In [[AES-GCM]] e [[Poly1305]], le operazioni su $GF(2¹²⁸)$ permettono di calcolare **tag di autenticazione** in modo efficiente e sicuro.
        

---

**Esempio pratico:**

- $GF(2)$ → campo con 2 elementi {0,1}, con XOR come somma e AND come moltiplicazione.
    
- $GF(2^{128})$ → campo usato in [[AES-GCM]], con 2¹²⁸ elementi, permette di rappresentare blocchi di 128 bit come polinomi.
    

---

Ecco una spiegazione concettuale, focalizzata sul perché è essenziale per la sicurezza, in particolare nell'algoritmo **AES (Advanced Encryption Standard)**.

---

## 🧐 Cos'è un Campo (Field)

Immagina un campo come un insieme di numeri in cui puoi eseguire le quattro operazioni aritmetiche fondamentali (**somma, sottrazione, moltiplicazione e divisione**) e ottenere sempre un risultato che rimane all'interno di quell'insieme.

- **Esempi di campi infiniti:**
    
    - I numeri razionali ($\mathbb{Q}$)
        
    - I numeri reali ($\mathbb{R}$)
        

## 🔢 La Natura del Campo di Galois: Finito

Il **Campo di Galois** ($GF$), dal nome del matematico Évariste Galois, è un **campo finito**. Significa che ha un **numero limitato di elementi**.

In crittografia, il campo di Galois più utilizzato è $\mathbf{GF(2^n)}$, in particolare $\mathbf{GF(2^8)}$ in AES.

### Perché è cruciale che sia Finito?

Nei computer, i dati sono gestiti in blocchi di dimensioni fisse (bit, byte, ecc.).

- Un **byte** è composto da 8 bit e può rappresentare esattamente $2^8 = 256$ valori diversi (da 0 a 255).
    
- Se usassimo l'aritmetica tradizionale (su $\mathbb{R}$), la moltiplicazione di due byte produrrebbe un numero che non è più rappresentabile in un solo byte, causando un _overflow_ o richiedendo più spazio.
    

**Il Campo di Galois risolve questo problema:** ti permette di eseguire operazioni matematiche complesse su un byte (8 bit) e di ottenere sempre come risultato un altro byte (8 bit), garantendo che l'operazione sia **chiusa** e **reversibile** (due proprietà fondamentali per la crittografia).

---

## 💡 Il Ruolo nell'AES: $\mathbf{GF(2^8)}$

L'algoritmo **AES** opera su blocchi di dati di 128 bit, trattando ogni blocco come una matrice di $4 \times 4$ byte. Tutte le operazioni chiave (come `SubBytes` e `MixColumns`) vengono eseguite utilizzando l'aritmetica nel campo **$GF(2^8)$**.

### 1. **Rappresentazione (Byte come Polinomi)**

In $GF(2^8)$, ogni byte non è trattato come un semplice numero intero, ma come un **polinomio di grado massimo 7** con coefficienti binari (0 o 1).

- Esempio: Il byte 10110010 viene interpretato come il polinomio:
    
    $$1 \cdot x^7 + 0 \cdot x^6 + 1 \cdot x^5 + 1 \cdot x^4 + 0 \cdot x^3 + 0 \cdot x^2 + 1 \cdot x^1 + 0 \cdot x^0 = x^7 + x^5 + x^4 + x$$
    

### 2. **Addizione (Semplice XOR)**

L'addizione in $GF(2^8)$ è semplicemente un **XOR bit-a-bit** (OR esclusivo).

- **Motivo:** Nel campo $GF(2^8)$, l'addizione dei coefficienti del polinomio è modulo 2. Questo significa che $1 + 1 = 0$ (che è il comportamento di XOR).
    
    - **Vantaggio Crittografico:** È estremamente veloce da implementare nell'hardware e nel software.
        

### 3. **Moltiplicazione (Aritmetica Modulo Polinomio)**

Qui sta la magia che garantisce il risultato rimanga in 8 bit:

1. Si moltiplicano i due polinomi associati ai byte.
    
2. Il risultato (che può avere grado fino a 14) viene diviso per un **polinomio irriducibile** fisso di grado 8 (in AES è $m(x) = x^8 + x^4 + x^3 + x + 1$).
    
3. Il risultato della moltiplicazione nel campo è il **resto** di questa divisione polinomiale. Poiché si divide per un polinomio di grado 8, il resto sarà sempre un polinomio di grado massimo 7, che corrisponde a un **singolo byte**.
    

> **In sintesi:**
> 
> - L'aritmetica sui campi di Galois è ciò che rende le complesse operazioni matematiche dell'AES (come la `MixColumns`) **algebricamente robuste**, **efficienti da calcolare** sui computer e, soprattutto, **perfettamente reversibili** (il che è necessario per la decifratura).
>     

In breve, il Campo di Galois ($GF(2^8)$) è come un **righello matematico** con solo 256 tacche. Qualsiasi operazione tu faccia, il risultato "avvolge" e cade sempre su una di quelle 256 tacche, mantenendo l'operazione veloce e contenuta in un singolo byte.


La funzione principale del **Campo di Galois** ($GF(2^8)$) in crittografia, specialmente in algoritmi come AES, è esattamente questa:

> **Garantire che operazioni matematiche complesse sui dati (byte) avvengano in modo efficiente, siano crittograficamente forti e producano sempre un risultato che si adatta perfettamente allo spazio di archiviazione originale (un singolo byte), prevenendo gli overflow.**

---

## 🔑 Dettagli sull'Efficienza e il Ruolo Crittografico

Ecco come il $GF(2^8)$ realizza questo obiettivo:

- ### 1. **Contenimento Spaziale (No Overflow)**
    
    Nel campo $GF(2^8)$, ci sono esattamente **256** elementi (da 0 a 255). Le operazioni di base sono definite in modo tale che, indipendentemente da quanti calcoli fai (somma o moltiplicazione), il risultato **non uscirà mai** da questo insieme di 256 valori.
    
    - **Meccanismo chiave:** Per la moltiplicazione, il "contenimento" è garantito dalla **divisione polinomiale modulo un polinomio irriducibile** di grado 8. Questo agisce come un "involucro" che riduce il risultato a un polinomio di grado 7 o inferiore, che è, per definizione, un singolo byte.
        
- ### 2. **Reversibilità (Decifratura)**
    
    In un campo, ogni elemento diverso da zero ha un **inverso moltiplicativo**. Questa è una proprietà cruciale.
    
    - **Significato in Crittografia:** Per decifrare i dati in AES, è necessario "annullare" l'operazione di moltiplicazione effettuata durante la cifratura. L'esistenza garantita di un inverso nel campo di Galois permette di definire in modo univoco le operazioni di decifratura (come la fase inversa di `MixColumns`). Senza un campo, non ci sarebbe alcuna garanzia matematica che la decifratura sia sempre possibile e corretta.
        
- ### 3. **Efficienza Computazionale (XOR)**
    
    L'addizione nel $GF(2^8)$ è implementata come una semplice operazione **XOR bit-a-bit**. Questa è una delle operazioni logiche più veloci su qualsiasi processore, contribuendo enormemente alla velocità complessiva di AES.
    

Quindi, non è solo un "trucco" per evitare l'overflow; è una **struttura matematica completa e rigorosa** che assicura che l'algoritmo AES sia **sicuro, veloce e reversibile**.