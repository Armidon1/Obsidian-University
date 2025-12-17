# S-Box (Substitution Box)

## 1. Definizione

Una S-Box (Substitution Box) è un componente fondamentale negli algoritmi di cifratura a chiave simmetrica (come [[AES]] e DES).

È una funzione che prende un input di bit (es. 8 bit) e lo trasforma in un output di bit diverso, secondo una regola deterministica non lineare.

In termini informatici, è essenzialmente una [[Lookup Table (LUT)]] (Tabella di Consultazione):

$$S(x) = y$$

## 2. Lo Scopo: Confusione e Non-Linearità

Perché non usiamo solo operazioni semplici come XOR e rotazioni?

Se un cifrario usasse solo operazioni lineari (somme, XOR, permutazioni), l'intero algoritmo potrebbe essere ridotto a una singola equazione lineare del tipo $y = Ax + B$.

Un attaccante potrebbe risolvere questo sistema con semplice algebra lineare e rompere il codice istantaneamente.

L'**S-Box** è l'unico componente che introduce la **Non-Linearità** nel sistema.

- **Obiettivo:** Nascondere la relazione matematica tra il testo in chiaro e il testo cifrato.
    
- **Proprietà di Shannon:** Implementa il principio della **Confusione** (mentre le permutazioni implementano la _Diffusione_).
    

> [!abstract] Metafora
> 
> Immagina le operazioni lineari (XOR, Shift) come il "mescolare" un mazzo di carte: le carte cambiano posto, ma rimangono carte.
> 
> L'S-Box è come prendere una carta, strapparla, e sostituirla con un pezzo di plastica colorata secondo una regola segreta. Rompe la struttura originale dell'oggetto.

## 3. Come Funziona (Esempio AES)

Nell'algoritmo **[[AES]]**, la S-Box è una matrice $16 \times 16$ byte precalcolata.

- **Input:** 1 Byte (8 bit), ad esempio `0x9A`.
    
- **Processo:**
    
    1. Si prende la prima cifra esadecimale (`9`) come indice di **Riga**.
        
    2. Si prende la seconda cifra (`A`) come indice di **Colonna**.
        
    3. Si legge il valore all'incrocio nella tabella S-Box.
        
- **Output:** Il valore trovato (es. `0xB3`).
    

### Matematica Sottostante (Per approfondire)

Le S-Box non sono riempite con numeri a caso (sarebbe rischioso). Quella di AES è costruita matematicamente usando l'aritmetica dei Campi Finiti (Galois Fields $GF(2^8)$):

1. Si calcola l'**Inverso Moltiplicativo** dell'input in $GF(2^8)$.
    
2. Si applica una Trasformazione Affine (moltiplicazione matriciale + somma vettoriale).
    
    Questo garantisce ottime proprietà di resistenza alla crittanalisi differenziale e lineare.
    

## 4. Proprietà di Sicurezza Richieste

Una buona S-Box deve soddisfare criteri rigorosi:

1. **Effetto Valanga (Avalanche Effect):** Cambiare anche solo 1 bit in input deve cambiare circa il 50% dei bit in output.
    
2. **Bit Independence:** I bit di output non devono dipendere linearmente dai bit di input.
    
3. **Equilibrio:** Ogni possibile output deve apparire lo stesso numero di volte (per evitare bias statistici).
    

## 5. Attacchi e Vulnerabilità

Se una S-Box è progettata male (es. i primi cifrari hobbistici), un attaccante può usare:

- **Crittanalisi Lineare:** Cerca approssimazioni lineari tra input e output.
    
- **Crittanalisi Differenziale:** Analizza come le differenze in input si propagano nell'output.
    

> [!warning] Il caso DES
> 
> Le S-Box del vecchio standard DES erano avvolte nel mistero. Si scoprì poi che la NSA le aveva progettate specificamente per resistere alla crittanalisi differenziale (una tecnica nota ai servizi segreti ma ignota al pubblico negli anni '70).

---

**Vedi anche:**

- [[AES (Advanced Encryption Standard)]]
    
- [[Lookup Table]]
    
- [[Cifratura a Blocchi]]
    
- [[Confusione e Diffusione]]