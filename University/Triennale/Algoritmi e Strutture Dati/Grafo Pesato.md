# Grafo Pesato
### 1. Definizioni Fondamentali

Un **Grafo Pesato** è un grafo $G = (V, E)$ in cui ad ogni lato (arco) è associato un valore numerico detto **peso**.

- **Peso del Lato:** Si denota con $w(u, v)$ il peso del lato che collega i vertici $u$ e $v$.
    
- Peso del Percorso ($w(P)$): Dato un percorso $P = ((v_0, v_1), (v_1, v_2), \dots, (v_{k-1}, v_k))$, il suo peso è la somma dei pesi dei singoli lati che lo compongono:
    
    $$w(P) = \sum_{i=1}^{k} w(v_{i-1}, v_i)$$
    

![Immagine di weighted graph showing path calculation](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTST8LOoGR-qdiLjISXraTazJWAyXOQHo_jFOxZQd-eFt7bzNCUp0QwKuUqLvRdUrXPQrDoW78mWDWL8Mk3aezphBSewRNT238aPl-qq881ldQFrOE)

Shutterstock

### 2. Distanza tra Vertici

La **distanza** tra due vertici $u$ e $v$, denotata come $d(u, v)$, è definita come il peso del **percorso minimo** (shortest path) tra tutti i possibili percorsi da $u$ a $v$.

$$d(u, v) = \min \{ w(P) : P \text{ è un percorso da } u \text{ a } v \}$$

- **Irraggiungibilità:** Se non esiste alcun percorso tra $u$ e $v$, allora $d(u, v) = \infty$.
    

### 3. Gestione dei Pesi e Cicli

- **Convenzione ($w \ge 0$):** Per semplificazione e per modellare problemi reali (es. distanze stradali), consideriamo solitamente solo pesi **non negativi**.
    
- **Pesi Negativi e Cicli:** Un lato può matematicamente avere peso negativo. Tuttavia, se nel grafo esiste un **ciclo con peso totale negativo**, la distanza $d(u, v)$ diventa **non definita** (si potrebbe percorrere il ciclo infinite volte riducendo il peso all'infinito).
    

> ⚠️ **Nota:** Algoritmi come Dijkstra richiedono pesi non negativi. Per pesi negativi (senza cicli negativi) si usa Bellman-Ford.

## ⚖️ Calcolo Percorso Minimo (Grafo Pesato)
### 4. Strategie Algoritmiche

La scelta dell'algoritmo dipende dalla natura dei pesi:

| **Tipo di Pesi**                 | **Algoritmo Consigliato**           | **Note**                                                            |
| -------------------------------- | ----------------------------------- | ------------------------------------------------------------------- |
| **Pesi uniformi (tutti uguali)** | **[[BFS]]** (Breadth-First Search)  | La visita a livelli trova naturalmente il percorso con meno lati.   |
| **Pesi variabili ($\ge 0$)**     | **[[Dijkstra Algorithm]]** (Greedy) | Esplora scegliendo sempre il nodo più "vicino" non ancora visitato. |

### 5. Approccio Greedy (Goloso)

Gli algoritmi per percorsi minimi su grafi pesati (come Dijkstra) sfruttano spesso il paradigma **Greedy**:

- **Logica:** Ad ogni passo, l'algoritmo prende la decisione che sembra ottima in quel momento (ottimo locale), sperando di trovare l'ottimo globale.
    
- **Nel contesto dei cammini minimi:** "Rilassiamo" (aggiorniamo) le distanze espandendo sempre il vertice che al momento ha la distanza stimata minore.
    

---
