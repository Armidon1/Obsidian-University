# 🕸️ Struttura Dati: Il Grafo

### 1. Definizione Formale

Un **Grafo** $G$ è una coppia ordinata $(V, E)$, dove:

- **$V$ (Vertices):** È un insieme finito di elementi chiamati **vertici** (o nodi).
    
- **$E$ (Edges):** È un insieme di coppie di elementi appartenenti a $V$, chiamate **lati** (o archi).
    

$$G = (V, E)$$

### 2. Tipologie Principali

La natura della coppia in $E$ determina il tipo di grafo:

- **Grafo Non Orientato (Undirected):**
    
    - I lati sono coppie **non ordinate** di vertici $\{u, v\}$.
        
    - La relazione è simmetrica: se $u$ è collegato a $v$, allora $v$ è collegato a $u$.
        
    - Rappresentazione: Linea semplice tra i nodi.
        
- **Grafo Orientato (Directed / Digraph):**
    
    - I lati sono coppie **ordinate** di vertici $(u, v)$.
        
    - $u$ è l'origine (coda), $v$ è la destinazione (testa).
        
    - Rappresentazione: Freccia da $u$ a $v$ ($u \to v$).
        

### 3. Terminologia Essenziale

- **Adiacenza:** Due vertici $u, v$ sono adiacenti se esiste un lato che li collega.
    
- **Incidenza:** Un lato è incidente a un vertice se quel vertice è uno degli estremi del lato.
    
- **Grado (Degree):**
    
    - In grafi non orientati: Numero di lati incidenti a un vertice.
        
    - In grafi orientati: Si distingue in **In-Degree** (lati entranti) e **Out-Degree** (lati uscenti).
        
- **Percorso (Path):** Una sequenza di vertici in cui ogni vertice consecutivo è collegato da un lato.
    
- **Ciclo:** Un percorso che inizia e finisce nello stesso vertice senza ripetere altri lati o vertici.
    

### 4. Rappresentazione in Memoria

Per un ingegnere informatico, la scelta della struttura dati impatta la complessità temporale ($T$) e spaziale ($S$):

|**Rappresentazione**|**Struttura**|**Spazio (S)**|**Verifica Adiacenza (u,v)**|**Iterazione Vicini**|
|---|---|---|---|---|
|**Lista di Adiacenza**|Array/Map di Liste|$O(V + E)$|$O(\deg(u))$|$O(\deg(u))$|
|**Matrice di Adiacenza**|Matrice 2D ($V \times V$)|$O(V^2)$|$O(1)$|$O(V)$|

> **Nota:** La **Lista di Adiacenza** è preferita per grafi _sparsi_ (pochi lati), mentre la **Matrice** è utile per grafi _densi_ o quando serve verificare rapidamente l'esistenza di un arco specifico.

---

### 🛠️ Coding Challenge: La Classe `Graph`

Per esercitarti, invece di usare librerie pronte, prova a creare la tua struttura.

**Task:** Scrivi un'interfaccia (o classe astratta) `Graph` in Java o C++ che supporti sia grafi orientati che non, con i seguenti metodi base:

1. `numVertices()`
    
2. `vertices()` (restituisce un iterabile)
    
3. `numEdges()`
    
4. `getEdge(u, v)`
    
5. `insertVertex(x)`
    
6. `insertEdge(u, v, weight)`
    

