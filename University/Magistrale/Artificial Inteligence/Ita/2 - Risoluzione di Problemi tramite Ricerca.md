# Risoluzione di Problemi tramite Ricerca (Problem Solving by Search)

**Tags:** #uni #AI #ingegneria #search #algoritmi
**Fonte:** Slide Prof. Patrizi (02-AI-Search) + Cap 3 "AI A Modern Approach"

---

## 1. Agenti Risolutori di Problemi

Un **agente risolutore di problemi** (Problem-solving agent) è un tipo di agente che decide cosa fare intraprendendo un processo di **ricerca** (search): simula sequenze di azioni nel suo modello interno per trovare un percorso che conduca a uno stato obiettivo desiderato .

Il processo operativo standard segue 4 fasi :
1. **Formulazione dell'obiettivo (Goal formulation):** L'agente adotta un obiettivo (es. arrivare a Bucarest). Questo limita le azioni da considerare.
2. **Formulazione del problema (Problem formulation):** L'agente crea una descrizione astratta degli stati e delle azioni (es. mappa stradale). L'**astrazione** è fondamentale per eliminare dettagli irrilevanti (es. il meteo o il paesaggio) e rendere il problema computabile.
3. **Ricerca (Search):** L'agente simula sequenze di azioni finché non trova una **soluzione** (una sequenza di azioni che porta dallo stato iniziale al goal).
4. **Esecuzione (Execution):** L'agente esegue le azioni nel mondo reale.

> **Nota:** In ambienti deterministici, noti e completamente osservabili, la soluzione è una sequenza fissa. L'agente può operare in **Open-loop** (ignorando le percezioni durante l'esecuzione perché sa già che la soluzione funzionerà) .

---

## 2. Definizione Formale di un Problema di Ricerca

Un problema di ricerca è definito formalmente dai seguenti 5 componenti :

1. **Spazio degli Stati ($S$):** L'insieme di tutti i possibili stati in cui l'ambiente può trovarsi. Può essere finito o infinito.
2. **Stato Iniziale ($s_0$):** Lo stato in cui l'agente inizia.
3. **Stati Obiettivo ($G$):** Un sottoinsieme di stati ($G \subseteq S$) o una funzione `IS-GOAL(s)` che verifica se uno stato soddisfa l'obiettivo.
4. **Azioni ($A$):** Una funzione `ACTIONS(s)` che restituisce l'insieme finito di azioni applicabili nello stato $s$.
5. **Modello di Transizione (Transition Model):** Una funzione `RESULT(s, a)` che restituisce lo stato che risulta dall'eseguire l'azione $a$ nello stato $s$.
* Questo definisce il grafo dello spazio degli stati: nodi = stati, archi = azioni.
6. **Funzione di Costo dell'Azione ($c$):** `ACTION-COST(s, a, s')` restituisce il costo numerico per passare da $s$ a $s'$ tramite $a$. Si assume che i costi siano additivi e generalmente positivi ($c \ge \epsilon > 0$).

### Esempi Classici

#### Mappa della Romania
- **Stati:** Città (es. Arad, Sibiu).
- **Azioni:** Guidare da una città all'altra.
- **Costo:** Distanza in miglia.

![[Inserire qui Immagine Figura 3.1 dal PDF]]
> *Figura 3.1: Mappa stradale semplificata della Romania. I numeri sugli archi indicano la distanza.*

#### Il Mondo dell'Aspirapolvere (Vacuum World)
- **Stati:** Posizione dell'agente e presenza di sporco. Con $n$ celle, ci sono $n \cdot 2^n$ stati.
- **Azioni:** Left, Right, Suck.

![[Inserire qui Immagine Figura 3.2 dal PDF]]
> *Figura 3.2: Grafo dello spazio degli stati per il mondo aspirapolvere a due celle.*

#### Il Gioco dell'8 (8-Puzzle)
- **Stati:** Configurazione delle tessere nella griglia $3 \times 3$.
- **Azioni:** Muovere la casella vuota (Up, Down, Left, Right).
- **Obiettivo:** Ordinare i numeri.

![[Inserire qui Immagine Figura 3.3 dal PDF]]
> *Figura 3.3: Stato iniziale e Goal state del gioco dell'8.*

---

## 3. Soluzioni e Percorsi

- **Percorso (Path):** Una sequenza di azioni e stati.
- **Soluzione:** Un percorso dallo stato iniziale a uno stato obiettivo.
- **Soluzione Ottimale:** La soluzione che ha il **costo del percorso più basso** (path cost) tra tutte le soluzioni possibili.

---

## 4. Algoritmi e Alberi di Ricerca

Un **Algoritmo di Ricerca** prende in input un problema e restituisce una soluzione o un fallimento. La maggior parte degli algoritmi lavora sovrapponendo un **Albero di Ricerca** al grafo dello spazio degli stati.

### Distinzione Fondamentale: Stato vs Nodo
- **Stato (State):** Una configurazione fisica del mondo (es. "Essere a Arad").
- **Nodo (Node):** Una struttura dati all'interno dell'albero di ricerca che contiene:
* `node.STATE`: Lo stato corrispondente.
* `node.PARENT`: Il nodo che ha generato questo nodo.
* `node.ACTION`: L'azione intrapresa per arrivare qui.
* `node.PATH-COST`: Il costo totale dal percorso radice a questo nodo ($g(n)$).

### Espansione e Frontiera
L'algoritmo procede tramite **Espansione dei Nodi**:
1. Si seleziona un nodo dalla **Frontiera** (l'insieme dei nodi generati ma non ancora espansi, talvolta chiamata *Open List*).
2. Si applicano le azioni possibili per generare i nodi figli (Successori).
3. Si aggiungono i figli alla frontiera.

La **Frontiera** separa la regione "esplorata" (nodi espansi) dalla regione "inesplorata" (stati non ancora raggiunti).

![[Inserire qui Immagine Figura 3.4 dal PDF]]
> *Figura 3.4: Tre stadi parziali dell'albero di ricerca. I nodi verdi rappresentano la frontiera.*

![[Inserire qui Immagine Figura 3.5 dal PDF]]
> *Figura 3.5: Come l'albero di ricerca copre il grafo dello spazio degli stati.*

---

## 5. Graph Search vs Tree-like Search

Un problema critico nella ricerca sono i **percorsi ridondanti** e i **cicli** (loopy paths).
* *Esempio:* Andare da Arad a Sibiu e tornare ad Arad è un ciclo. Andare ad Arad passando per Zerind è un percorso ridondante più lungo.

Gli algoritmi si dividono in due categorie:
1. **Graph Search:** Tiene traccia degli stati già visitati (usando un insieme `reached` o *Closed List*). Se si incontra uno stato già esplorato con un costo minore o uguale, lo si ignora. È necessario per spazi con molti cicli (es. griglie).
2. **Tree-like Search:** Non tiene traccia degli stati passati. Risparmia memoria ma può finire in loop infiniti o esplorare esponenzialmente gli stessi stati su percorsi diversi.

![[Inserire qui Immagine Figura 3.6 dal PDF]]
> *Figura 3.6: La proprietà di separazione. La frontiera (verde) separa l'interno (visitato) dall'esterno (non raggiunto).*

---

## 6. Best-First Search (Approccio Generale)

La maggior parte degli algoritmi di ricerca sono varianti del **Best-First Search**.
L'idea è selezionare il nodo da espandere in base a una **funzione di valutazione $f(n)$**.
* Si espande sempre il nodo con il **minimo $f(n)$**.
* La Frontiera è implementata come una **Coda con Priorità** (Priority Queue) ordinata per $f$.

```python
function BEST-FIRST-SEARCH(problem, f) returns a solution node or failure
node <- NODE(STATE=problem.INITIAL)
frontier <- priority queue ordered by f, with node as element
reached <- lookup table {problem.INITIAL: node}

while not IS-EMPTY(frontier) do
node <- POP(frontier)
if problem.IS-GOAL(node.STATE) then return node
for each child in EXPAND(problem, node) do
s <- child.STATE
if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
reached[s] <- child
add child to frontier
return failure
````

> _Figura 3.7 (pseudocodice adattato)._ 1

---

## 7. Proprietà degli Algoritmi

Per valutare un algoritmo usiamo 4 criteri 2:

1. **Completezza (Completeness):** Trova sempre una soluzione se esiste?

2. **Ottimalità (Optimality):** Trova la soluzione con il costo minore?

3. **Complessità Temporale (Time Complexity):** Quanto tempo impiega (numero di nodi generati)?

4. **Complessità Spaziale (Space Complexity):** Quanta memoria richiede (numero di nodi memorizzati)?


I parametri tipici sono:

- $b$: fattore di ramificazione (branching factor).

- $d$: profondità della soluzione più superficiale.

- $m$: lunghezza massima di un percorso nello spazio degli stati.


---

## 8. Strategie di Ricerca Non Informata (Uninformed)

Questi algoritmi non hanno informazioni sulla "distanza" dal goal. Sanno solo generare successori e verificare se sono arrivati.

### 8.1 Breadth-First Search (BFS) - Ricerca in Ampiezza

Esplora tutti i nodi a profondità $d$ prima di passare a $d+1$.

- **Strategia:** Coda FIFO. $f(n) = \text{depth}(n)$.

- **Completezza:** Sì (se $b$ è finito).

- **Ottimalità:** Sì, ma **solo se tutti i costi delle azioni sono uguali** (o 1).

- **Complessità:** $O(b^d)$ sia per tempo che per spazio.

- _Problema:_ La memoria è il collo di bottiglia critico (esponenziale).


![[Inserire qui Immagine Figura 3.8 dal PDF]]

> _Figura 3.8: Avanzamento della BFS._ 3

### 8.2 Uniform-Cost Search (Dijkstra)

Espande il nodo con il costo di percorso $g(n)$ più basso.

- **Strategia:** Coda Priorità. $f(n) = g(n)$ (costo accumulato).

- **Ottimalità:** Sì, sempre (se costi $\ge \epsilon > 0$).

- **Completezza:** Sì.

- **Complessità:** $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$. Può essere peggiore della BFS se ci sono molti passi a basso costo.


![[Inserire qui Immagine Figura 3.10 dal PDF]]

> Figura 3.10: Uniform-Cost Search sulla mappa della Romania. Espande in base al costo, non alla profondità. 4

### 8.3 Depth-First Search (DFS) - Ricerca in Profondità

Esplora ogni ramo fino in fondo prima di tornare indietro (backtracking).

- **Strategia:** Coda LIFO (Stack).

- **Completezza:** No (può bloccarsi in loop o percorsi infiniti).

- **Ottimalità:** No (restituisce la prima soluzione che trova, anche se lunga).

- **Spazio:** Molto efficiente: $O(bm)$ (lineare rispetto alla profondità).

- **Tempo:** $O(b^m)$.


![[Inserire qui Immagine Figura 3.11 dal PDF]]

> Figura 3.11: Avanzamento della DFS. Nota come la frontiera (verde) sia molto piccola rispetto ai nodi già espansi. 5

### 8.4 Depth-Limited & Iterative Deepening (IDS)

Per risolvere i problemi della DFS (non completezza) mantenendo i vantaggi (poca memoria):

1. **Depth-Limited:** DFS con un limite di profondità $l$. Incompleta se la soluzione è a $d > l$.

2. **Iterative Deepening (IDS):** Esegue Depth-Limited con $l=0$, poi $l=1$, poi $l=2$...

- **Completezza:** Sì.

- **Ottimalità:** Sì (se costi uguali).

- **Memoria:** $O(bd)$ (come DFS).

- _Nota:_ Rigenerare i nodi sembra costoso, ma in realtà il costo è dominato dall'ultimo livello (che ha $b^d$ nodi), quindi asintoticamente ha lo stesso tempo della BFS ($O(b^d)$). È l'algoritmo preferito per ricerche non informate con spazio di stati grande.67


![[Inserire qui Immagine Figura 3.13 dal PDF]]89

> _Figura 3.13: Iterative Deepening Search._ 101112

### Tabella Riassuntiva1314

![[Inserire qui Immagine Figura 3.15 dal PDF]]1516

> _Figura 3.15: Confronto delle strategie di ricerca no17n informata._ 1819

---

## 9. Strategie di Ricerca Informata (Euristica)

Queste strategie utilizzano suggerimenti specifici del dominio (conoscenza del problema) riguardo alla posizione degli obiettivi per trovare soluzioni in modo più efficiente rispetto a una strategia non informata. I suggerimenti arrivano sotto forma di una **funzione euristica $h(n)$**, che restituisce il costo stimato del percorso più economico dallo stato al nodo $n$ a uno stato obiettivo.

### 9.1 Greedy Best-First Search

Questo algoritmo espande per primo il nodo con il valore $h(n)$ più basso—il nodo che appare più vicino all'obiettivo—sulla base del fatto che è probabile che questo porti velocemente a una soluzione.

- **Strategia:** La funzione di valutazione è $f(n) = h(n)$.
    
- **Esempio:** Usare la distanza in linea d'aria ($h_{SLD}$) verso Bucarest come euristica per la ricerca del percorso stradale. Poiché non tiene conto dei costi reali delle strade, l'algoritmo "punta" direttamente verso la meta.
    
- **Proprietà:**
    
    - **Completezza:** È completo in spazi degli stati finiti, ma non in quelli infiniti (può finire in loop).
        
    - **Ottimalità:** **Non è ottimale**. Ad ogni iterazione, l'algoritmo cerca di avvicinarsi il più possibile all'obiettivo ("greedy", avido), ma questo può portare a risultati peggiori rispetto all'essere prudenti. Ad esempio, potrebbe scegliere un percorso che sembra portare verso la meta ma che in realtà costringe a lunghe deviazioni fisiche, risultando più costoso di un percorso che inizialmente sembrava allontanarsi.
        
- **Complessità:** La complessità temporale e spaziale nel caso peggiore è $O(|V|)$ (dove $|V|$ è il numero di vertici), ma con una buona funzione euristica, l'efficienza migliora drasticamente.
    

### 9.2 Ricerca A*

La forma più comune di ricerca informata, A* (pronunciato "A-star"), combina il costo del percorso già effettuato ($g(n)$) con il costo stimato per arrivare all'obiettivo ($h(n)$).

- **Funzione:** $f(n) = g(n) + h(n)$.
    
- **Significato:** $f(n)$ rappresenta il costo totale stimato del **miglior percorso** che passa attraverso il nodo $n$ per raggiungere l'obiettivo.
    
- **Completezza:** Sì, la ricerca A* è completa.
    
- **Ottimalità:** Sì, a condizione che $h(n)$ soddisfi certe proprietà (Ammissibilità o Consistenza).
    
- **Contorni di Ricerca (Search Contours):** La ricerca A* può essere visualizzata come il disegno di curve di livello (come in una mappa topografica). Poiché espande il nodo di frontiera con il costo $f$ più basso, la ricerca si allarga dal nodo iniziale in bande concentriche. Con una buona euristica, queste bande si allungano "a goccia" verso l'obiettivo, concentrando la ricerca lungo il percorso ottimale invece di esplorare in tutte le direzioni.
    

#### Euristica Ammissibile

Un'euristica $h(n)$ è **ammissibile** se **non sovrastima mai** il costo reale per raggiungere un obiettivo. Un'euristica ammissibile è quindi "ottimistica" (pensa che il costo sia minore o uguale a quello reale).

- **Formula:** $h(n) \le h^*(n)$ (dove $h^*$ è il vero costo ottimale per l'obiettivo).
    
- **Esempio:** La distanza in linea d'aria ($h_{SLD}$) è ammissibile perché la linea retta è la distanza fisica minima tra due punti; nessuna strada reale può essere più corta della linea d'aria.
    
- **Prova di Ottimalità:** Se $h(n)$ è ammissibile, A* restituisce solo percorsi ottimali. Se l'algoritmo stesse per terminare con una soluzione subottimale, ci sarebbe necessariamente un altro nodo non ancora espanso sul vero percorso ottimale con un valore $f$ inferiore, che verrebbe quindi scelto prima della soluzione sbagliata.
    

#### Consistenza (Condizione più Forte)

Un'euristica è **consistente** (o monotona) se, per ogni nodo $n$ e ogni suo successore $n'$ generato da un'azione $a$, la stima del costo per arrivare al goal da $n$ non è maggiore del costo del passo per andare a $n'$ più la stima da $n'$.

- **Formula:** $h(n) \le c(n, a, n') + h(n')$
    
- **Disuguaglianza Triangolare:** Questa è una forma della disuguaglianza triangolare (un lato del triangolo non può essere più lungo della somma degli altri due).
    
- **Vantaggio:** Ogni euristica consistente è anche ammissibile. Inoltre, con un'euristica consistente, la prima volta che l'algoritmo raggiunge uno stato, è garantito che lo abbia fatto attraverso il percorso ottimale. Questo semplifica l'algoritmo perché non è mai necessario riaprire nodi già chiusi (closed set).