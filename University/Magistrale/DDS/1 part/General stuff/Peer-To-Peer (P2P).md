# Architetture Peer-to-Peer (P2P)

**Tags:** #sistemi_distribuiti #p2p #architettura #networking #dht

## 1. Definizione e Cambio di Paradigma

Il **Peer-to-Peer (P2P)** è un modello di architettura distribuita in cui i nodi (chiamati _peers_) condividono risorse (potenza di calcolo, memoria, banda) senza dipendere da un server centrale.

A differenza del modello Client/Server ($C/S$), in una rete P2P pura:

- Ogni nodo agisce sia da **Client** (richiede risorse) che da **Server** (fornisce risorse).
    
- I nodi sono considerati equipotenti (_peers_ = pari).
    

### Overlay Network

Il concetto ingegneristico chiave è quello di Overlay Network.

La rete P2P crea una rete logica "sopra" la rete fisica (TCP/IP). I nodi sono collegati da link virtuali, indipendentemente dalla loro vicinanza fisica.

![[Pasted image 20251129180854.png]]

> [!abstract] Visual Analysis
> 
> Client/Server: Struttura a stella. Se il centro cade, la rete muore (Single Point of Failure).
> 
> P2P: Struttura a maglia (Mesh). Se un nodo cade, la rete si riorganizza. Resilienza elevata.

---

## 2. Analisi Comparativa: P2P vs Client/Server

Dobbiamo valutare queste architetture basandoci sulla scalabilità matematica.

### Client/Server ($C/S$)

La capacità del sistema è limitata dalla capacità del server centrale ($C_s$). All'aumentare dei client ($N$), le risorse per client diminuiscono.

$$\text{Performance}_{CS} \propto \frac{C_s}{N}$$

> [!failure] Bottleneck
> 
> Quando $N \to \infty$, le prestazioni tendono a zero. Il server diventa un collo di bottiglia.

### Peer-to-Peer ($P2P$)

Ogni nuovo nodo porta con sé nuove risorse. La capacità totale del sistema ($C_{tot}$) è la somma delle capacità dei singoli nodi ($c_i$).

$$C_{tot} = \sum_{i=1}^{N} c_i$$

> [!abstract] Scalabilità
> 
> Nel P2P, all'aumentare di $N$, aumenta anche la capacità totale del sistema. È un sistema intrinsecamente scalabile.

---

## 3. Tassonomia dei Sistemi P2P

Non tutti i P2P sono uguali. Si classificano in base a come gestiscono la **ricerca delle risorse** (Lookup).

### A. P2P Non Strutturato (Unstructured)

La rete non impone una topologia specifica. I nodi si collegano a caso.

- **Algoritmo di Ricerca:** Flooding (Inondazione).
    
- **Logica:** "Chiedo ai miei vicini, che chiedono ai loro vicini...".
    
- **Esempi:** Gnutella (v1), Bitcoin (per il gossip delle transazioni).
    
- **Pro:** Facile da gestire, resiliente al churn (nodi che entrano/escono).
    
- **Contro:** Inefficiente per la ricerca. Genera molto traffico di rete.
    

### B. P2P Strutturato (Structured) - DHT

La rete impone una topologia rigida (es. anello, ipercubo) per garantire efficienza. Utilizza le **Distributed Hash Tables (DHT)**.

- **Algoritmo di Ricerca:** Routing basato su chiavi.
    
- **Logica:** Ogni nodo è responsabile di una specifica porzione di dati (basata sull'Hash ID).
    
- **Esempi:** Chord, Kademlia (usato da BitTorrent ed Ethereum), Pastry.
    
- **Efficienza:** Il tempo di ricerca è logaritmico rispetto al numero di nodi.
    

$$T_{lookup} = O(\log N)$$

---

## 4. Implementazione Algoritmica: Kademlia (Pseudo-logica)

Kademlia è l'algoritmo P2P più diffuso (usato in Ethereum). Utilizza la distanza XOR per trovare i nodi.

Logica di Routing (distanza XOR):

La "distanza" tra due nodi $A$ e $B$ non è fisica, ma matematica:

$$d(A, B) = A \oplus B$$

_(Dove $\oplus$ è l'operatore XOR bit a bit)_.

Python

```
# Pseudocodice semplificato di una ricerca in Kademlia
def find_node(target_id, my_routing_table):
    # 1. Seleziona i k nodi più vicini al target nella mia tabella (distanza XOR)
    closest_nodes = select_k_closest(target_id, my_routing_table)
    
    while not found:
        # 2. Chiede a questi nodi se conoscono il target o nodi più vicini
        responses = query_nodes(closest_nodes, target_id)
        
        # 3. Aggiorna la lista con i nuovi nodi scoperti (più vicini)
        new_closest = update_list(responses)
        
        if target_id in responses:
            return target_contact_info
        
        # Convergenza: ci avviciniamo logaritmicamente al target
        closest_nodes = new_closest
```

> [!abstract] Code Analysis
> 
> L'algoritmo non cerca "a caso". Ad ogni passaggio, riduce la distanza verso l'obiettivo, garantendo che la risorsa venga trovata in pochi passaggi ($O(\log N)$), anche in una rete con milioni di nodi.

---

## 5. Collegamento con Blockchain

Perché studiamo il P2P in questo corso?

> [!tip] Exam Focus
> 
> La Blockchain è, essenzialmente, un database replicato sopra una rete P2P.

1. **Propagazione:** Quando fai una transazione Bitcoin, questa viene propagata via P2P (Gossip Protocol) a tutti i nodi.
    
2. **Resistenza alla Censura:** Poiché non c'è un server centrale (come visto nella nota _0. Trust Matters_), nessuno può spegnere la rete.
    
3. **Discovery:** I nodi usano protocolli P2P (come Kademlia in Ethereum) per trovarsi l'un l'altro.
    

### 💡 Next Step per lo Studente

Hai analizzato le slide sulla fiducia e sul consenso. Il prossimo passaggio logico è capire come i nodi malevoli possono attaccare questa struttura P2P.

Vuoi che crei una nota specifica sugli Attacchi alle Reti P2P/Blockchain (es. Sybil Attack, Eclipse Attack, 51% Attack)? Questo è un argomento molto richiesto agli esami.