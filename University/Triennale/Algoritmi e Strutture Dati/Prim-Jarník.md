## 🌲 Algoritmo di Prim-Jarník (MST)

### 1. Concetto Fondamentale

L'algoritmo di Prim-Jarník costruisce un **[[Albero Ricoprente Minimo]] (MST)** facendo "crescere" gradualmente un singolo albero a partire da un vertice radice arbitrario $s$.

- **La Nuvola ($C$):** Mantiene un insieme di vertici $C$ già inclusi nell'MST.
    
- **Strategia Greedy:** Ad ogni passo, aggiunge alla nuvola il vertice $v$ esterno che è collegato alla nuvola dal **lato di peso minimo** possibile.
    
- **Base Teorica:** Funziona grazie alla **Proprietà del Taglio**: il lato più leggero che attraversa il taglio tra i nodi visitati ($C$) e quelli non visitati appartiene sicuramente all'MST.
    

---

### 💻 Pseudocodice

Trascrizione formale dell'algoritmo:

Snippet di codice

```java
Algoritmo PrimJarnik(G):
    Input: Un grafo G connesso, non orientato e pesato
    Output: Un albero ricoprente minimo T per G

    // 1. Inizializzazione
    scegli un vertice s di G
    D[s] = 0
    for ogni vertice v != s do
        D[v] = infinito
    
    inizializza T = insieme vuoto
    crea una coda prioritaria Q con una voce (D[v], v) per ogni vertice v
    
    // connect(v) memorizza il lato che connette v all'albero (il "padre")
    per ogni vertice v, inizializza connect(v) = null 

    // 2. Ciclo Principale
    while Q non è vuota do
        // Estrai il vertice più "vicino" alla nuvola
        u = valore contenuto nella voce restituita da Q.removeMin()
        
        // Aggiungi il lato corrispondente all'albero (se esiste)
        if connect(u) != null then
            aggiungi connect(u) a T
        
        // 3. Aggiornamento dei vicini (Rilassamento modificato)
        for ogni lato e' = (u, v) tale che v appartenga a Q do
            
            // Controlla se questo lato connette v alla nuvola meglio di prima
            // NOTA: Qui sta la differenza con Dijkstra!
            if w(u, v) < D[v] then
                D[v] = w(u, v)      // Aggiorna con il peso del SOLO lato
                connect(v) = e'     // Salva il lato candidato
                cambia la chiave associata a v in Q: diventa D[v]

    return l'albero T
```

---

### ⚠️ Prim vs Dijkstra: Il confronto cruciale

Sebbene la struttura del codice sia quasi identica (loop `while` con `PriorityQueue`), il significato dell'etichetta $D[v]$ è diverso:

|**Algoritmo**|**Significato di D[v]**|**Formula di Update**|
|---|---|---|
|**Dijkstra**|Lunghezza del **percorso totale** da $s$ a $v$.|$D[v] = D[u] + w(u, v)$|
|**Prim**|Peso del **singolo lato** che collega $v$ alla nuvola $C$.|$D[v] = w(u, v)$|

> **In sintesi:** Dijkstra guarda "indietro" fino alla sorgente (somma accumulata). Prim guarda solo l'interfaccia immediata tra la nuvola e l'esterno (peso locale).

---

### ⏱️ Analisi della Complessità

Il costo computazionale dipende dalla struttura dati usata per la Coda Prioritaria $Q$:

1. **Heap Binario (Scelta Standard):**
    
    - Ogni vertice estratto una volta: $O(n \log n)$.
        
    - Ogni lato rilassato (aggiornamento chiave): $O(m \log n)$.
        
    - Totale: **$O(m \log n)$** (assumendo grafo connesso dove $m \ge n$).
        
2. **Array/Lista non ordinata:**
    
    - Estrazione minimo: $O(n)$ per ogni vertice $\rightarrow O(n^2)$.
        
    - Rilassamento: $O(1)$ per ogni lato $\rightarrow O(m)$.
        
    - Totale: **$O(n^2)$**.
        

> **Nota Ingegneristica:** Per grafi **sparsi** ($m \approx n$), vince l'Heap ($O(n \log n)$). Per grafi molto **densi** ($m \approx n^2$), l'implementazione semplice $O(n^2)$ potrebbe essere competitiva o migliore di $O(n^2 \log n)$.

---

## Iterazioni
![[Pasted image 20251125190602.png]]
![[Pasted image 20251125190613.png]]![[Pasted image 20251125190657.png]]![[Pasted image 20251125190705.png]]