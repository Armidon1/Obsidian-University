# Lookup Table (LUT)

## 1. Definizione

Una **Lookup Table (LUT)** è una struttura dati (solitamente un array o una matrice) utilizzata per sostituire una calcolo a runtime con una semplice operazione di recupero dati dalla memoria.

Invece di calcolare un valore $y = f(x)$ ogni volta che serve, si pre-calcolano i risultati per tutti i possibili input $x$ e si salvano in una tabella. Quando serve il risultato, si usa $x$ come **indice** per estrarre $y$ istantaneamente.

## 2. Il Principio: Time-Memory Tradeoff

La LUT è l'esempio perfetto del **Compromesso Tempo-Memoria** (Space-Time Tradeoff) in informatica:

- **Senza LUT (Calcolo al volo):**
    
    - **Memoria:** Bassa (non devi salvare nulla).
        
    - **Tempo:** Alto (devi usare la CPU per calcolare la funzione ogni volta).
        
- **Con LUT (Precalcolo):**
    
    - **Memoria:** Alta (devi salvare tutti i risultati possibili).
        
    - **Tempo:** Bassissimo (accesso alla memoria $O(1)$).
        

> [!abstract] Esempio Matematico
> 
> Immagina di dover calcolare il seno di un angolo milioni di volte in un videogioco.
> 
> - **Approccio CPU:** `y = sin(x)` (Calcolo complesso in virgola mobile, lento).
>     
> - **Approccio LUT:** `y = SineTable[x]` (Lettura array, istantanea).
>     

## 3. Applicazioni in Crittografia

In ambito crittografico, le LUT sono onnipresenti sia per costruire algoritmi sicuri sia per attaccarli.

### A. Le [[S-Box (Substitution Boxes)]]

Algoritmi come [[AES]] e [[DES]] usano delle Lookup Table fisse chiamate S-Boxes.

Durante la cifratura, l'algoritmo prende un byte in input e lo sostituisce con un altro byte guardando nella tabella. Questo crea la proprietà di Confusione (non linearità) in modo estremamente veloce, senza dover calcolare funzioni matematiche complesse a runtime.

### B. Attacchi alle Password (Il precursore delle Rainbow Table)

Prima delle [[Rainbow Table]], l'attacco "Lookup Table" puro consisteva nel:

1. Prendere un dizionario.
    
2. Calcolare l'hash di _ogni_ parola.
    
3. Salvare la coppia `(Hash, Password)` in un file gigantesco.
    

Quando l'attaccante ruba un hash, fa una ricerca nel file:

$$\text{Password} = \text{Table}[\text{HashRubato}]$$

- **Problema:** Se la password è lunga (es. 10 caratteri casuali), la tabella diventerebbe grande quanto l'intero Internet (Petabyte/Exabyte), rendendo l'approccio impossibile per spazi di ricerca vasti.
    
- **Soluzione:** Ecco perché sono state inventate le **[[Rainbow Table]]**, che sacrificano un po' di tempo per risparmiare moltissima memoria.
    

## 4. Esempio di Codice (Logica)

Ecco come appare concettualmente la differenza.

**Senza LUT (Lento):**

```Python
def get_cube(n):
    return n * n * n  # La CPU lavora ogni volta
```

**Con LUT (Veloce ma occupa RAM):**

```Python
# Precalcolo (fatto una volta sola all'avvio)
cube_table = [0, 1, 8, 27, 64, 125, ... 1000000] 

def get_cube_fast(n):
    return cube_table[n] # Accesso istantaneo
```

## 5. Pro e Contro

|**Vantaggi**|**Svantaggi**|
|---|---|
|**Velocità:** È il metodo più veloce possibile per ottenere un risultato.|**Memoria:** Può richiedere quantità enormi di RAM o Disco se gli input possibili sono molti.|
|**Semplicità:** Il codice è banale (lettura array).|**Cache Miss:** Se la tabella è troppo grande per stare nella Cache della CPU, l'accesso alla RAM principale può diventare un collo di bottiglia.|
|**Determinismo:** Il tempo di esecuzione è costante.|**Inflessibilità:** Se la funzione cambia, devi ricalcolare tutta la tabella.|

---

**Vedi anche:**

- [[Rainbow Table]] (L'evoluzione ottimizzata della LUT per le password)
    
- [[AES]] (Usa LUT chiamate S-Box)
    
- [[Hashing]]
    
- [[Dictionary Attack]]