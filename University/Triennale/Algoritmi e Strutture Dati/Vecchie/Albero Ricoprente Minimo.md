Ecco una nota strutturata per Obsidian sugli **Alberi Ricoprenti Minimi (MST)**. Ho messo in risalto la differenza concettuale rispetto ai percorsi minimi e formalizzato la "Proprietà del Taglio" che hai descritto, essenziale per capire perché gli algoritmi Greedy funzionano.

---

## 🌲 Alberi Ricoprenti Minimi (MST)

### 1. Definizione e Obiettivo

Dato un grafo pesato e connesso $G$, un **Albero Ricoprente Minimo (Minimum Spanning Tree)** è un sottografo $T$ che:

1. **È un Albero:** Non contiene cicli.
    
2. **È Ricoprente (Spanning):** Include **tutti** i vertici di $G$.
    
3. **È Minimo:** La somma dei pesi dei suoi lati è la minima possibile tra tutti gli alberi ricoprenti.
    

$$w(T) = \sum_{(u,v) \in T} w(u,v) \quad \text{è minimizzato}$$

![Immagine di Minimum Spanning Tree example](https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQTPGhTJ0ceQhw9Q_cp_rsDZ6PiGQW2GJ0W2C75CWzjqjcfRDQMH2l5Fgytjfv5xDPJ18tbckSm79FXxjmozzT5BK4SyqsyMehA35O9dWqNEB-_3U8)

Shutterstock

### ⚠️ Differenza Cruciale: MST vs Shortest Path

È fondamentale non confondere l'MST con l'Albero dei Percorsi Minimi ([[Dijkstra Algorithm]]/[[BFS]]):

- **Shortest Path Tree (SPT):** Minimizza la distanza da una _specifica sorgente_ $s$ a ogni altro nodo.
    
- **MST:** Minimizza il **peso totale** della rete (la somma di tutti i lati). Non si preoccupa della distanza tra due nodi specifici, ma del costo globale di connessione.
    

> **Esempio Ingegneristico:**
> 
> - **SPT:** Il percorso più veloce per inviare un pacchetto dati da un Server A a tutti i Client (Routing).
>     
> - **MST:** Il modo più economico per stendere i cavi in fibra ottica per collegare tutti gli edifici di un campus (Cablaggio).
>     

### 2. Algoritmi Greedy

Poiché il problema ha una sottostruttura ottima, utilizziamo approcci **Greedy** (golosi):

- **Algoritmo di Prim-Jarník:** Simile a Dijkstra, fa crescere un singolo albero da un nodo iniziale.
    
- **Algoritmo di Kruskal:** Unisce foreste disgiunte scegliendo sempre il lato più leggero disponibile.
    

### 3. La Proprietà del Taglio (Cut Property)

Questa è la base teorica che garantisce la correttezza degli algoritmi Greedy.

Enunciato:

Sia $(V_1, V_2)$ una partizione dei vertici di $G$ (un taglio che divide i vertici in due insiemi disgiunti e non vuoti).

Sia $e = (u, v)$ un lato tale che $u \in V_1$ e $v \in V_2$.

Se $e$ ha il peso minimo tra tutti i lati che attraversano il taglio (connettono $V_1$ a $V_2$), allora:

$$\exists \text{ un MST che contiene il lato } e$$

### 4. Note Importanti sui Pesi

- **Unicità:** Se tutti i pesi dei lati sono **diversi (distinti)**, allora l'MST è **unico**.
    
- **Pesi Negativi:** A differenza dei percorsi minimi (dove i cicli negativi rompono Dijkstra), la definizione e gli algoritmi per l'MST rimangono validi anche in presenza di **lati o cicli negativi**. L'obiettivo è minimizzare la somma totale, quindi un lato negativo è anzi vantaggioso.
    

---

### Proprietà fondamentale
![[Pasted image 20251125190348.png]]