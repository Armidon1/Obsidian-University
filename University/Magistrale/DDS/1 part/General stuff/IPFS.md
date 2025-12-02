# IPFS (InterPlanetary File System)

## 1. Definizione e Obiettivo

IPFS è un protocollo [[Peer-To-Peer (P2P)]] e una rete per l'archiviazione e la condivisione di dati in un file system distribuito.

L'obiettivo ambizioso di IPFS è rendere il web più veloce, sicuro e aperto, sostituendo potenzialmente l'[[HTTP]] (il protocollo su cui navighiamo oggi) con un sistema che non dipende da server centralizzati.

## 2. Il Cambio di Paradigma: Location vs. Content

Questa è la differenza fondamentale per capire IPFS.

### 2.1. HTTP (Location Addressing)

Il web attuale cerca i contenuti in base a **DOVE** si trovano.

- Quando digiti `https://it.wikipedia.org/wiki/Blockchain`, stai dicendo al computer: _"Vai al server di Wikipedia (Luogo) e scarica il file che si trova in quella cartella"_.
    
- **Problema:** Se quel server va offline, viene censurato o spostato, il link si rompe (Errore 404).
    

### 2.2. IPFS (Content Addressing)

IPFS cerca i contenuti in base a **COSA** sono.

- Quando chiedi un file su IPFS, stai dicendo: _"Voglio il file che ha questa specifica impronta digitale (Hash). Non mi importa chi ce l'ha, dammi la copia più vicina"_.
    
- **Soluzione:** Se il tuo vicino di casa ha quel file sul suo nodo, lo scaricherai da lui invece che da un server in America.
    

## 3. Come Funziona: L'Architettura

### 3.1. Content Identifier (CID)

Ogni file caricato su IPFS viene passato attraverso una funzione di hashing crittografica. Il risultato è una stringa alfanumerica unica chiamata **CID (Content Identifier)**.

- Se cambi anche un solo pixel di un'immagine, il CID cambia completamente.
    
- Il CID funge da indirizzo permanente del file.
    

### 3.2. Merkle DAG (Directed Acyclic Graph)

IPFS organizza i dati utilizzando una struttura chiamata **Merkle DAG**.

- È simile al **Merkle Tree** (vedi nota relativa), ma più flessibile.
    
- Permette di dividere file grandi in piccoli blocchi, ognuno con il suo CID, collegati tra loro.
    
- **Vantaggio:** Se hai due versioni di un file che differiscono poco, IPFS memorizza solo i nuovi blocchi, evitando duplicazioni (deduplicazione).
    

### 3.3. DHT (Distributed Hash Table)

Per trovare _chi_ possiede il file (il CID) che stai cercando, IPFS usa una **Tabella di Hash Distribuita**. È come un elenco telefonico gigante diviso in piccoli pezzi: ogni nodo della rete ne possiede una piccola parte e sa a chi chiedere per trovare il resto.

## 4. IPFS vs Blockchain

Spesso si fa confusione, ma **IPFS non è una Blockchain**.

|**Caratteristica**|**Blockchain**|**IPFS**|
|---|---|---|
|**Scopo**|Registrare transazioni e stati in modo sequenziale.|Archiviare e trasferire file/dati di grandi dimensioni.|
|**Immutabilità**|Assoluta (la storia non cambia).|I file non cambiano (perché cambia il CID), ma possono essere "dimenticati" se nessuno li ospita.|
|**Costo**|Molto costoso archiviare dati (es. 1MB su Ethereum costa migliaia di dollari).|Progettato per grandi volumi di dati a basso costo.|

> **Sinergia perfetta:** Le blockchain (come Ethereum) memorizzano la "prova" o il titolo di proprietà (NFT), mentre l'IPFS memorizza l'immagine o il video collegato a quell'NFT. Senza IPFS, gli NFT dipenderebbero spesso da server centralizzati (Amazon AWS), rischiando di sparire.

## 5. Limitazioni e Persistenza

### 5.1. Il problema della volatilità

IPFS non garantisce che i dati rimangano online per sempre. I nodi conservano i file solo se:

1. Li hanno visualizzati di recente (Cache).
    
2. Hanno deciso esplicitamente di conservarli (**Pinning**).
    

Se nessuno fa il "Pin" di un file, il Garbage Collector del nodo potrebbe cancellarlo per liberare spazio.

### 5.2. Filecoin e Incentive Layer

Per risolvere il problema, è stato creato **Filecoin**: una blockchain costruita sopra IPFS che incentiva economicamente i nodi a conservare i file degli altri. Paghi in Filecoin affinché qualcuno garantisca l'archiviazione dei tuoi dati su IPFS.

---

Presumo tu intenda l'**Aritmetica Modulare** (o _Modulo Operator_), dato che "odular expression" sembra un refuso.

L'aritmetica modulare è il fondamento matematico invisibile che rende possibile la crittografia moderna. Senza di essa, le blockchain non potrebbero esistere. Ecco la nota Obsidian per spiegare come è integrata.

---

# Aritmetica Modulare (Modular Arithmetic)

## 1. Definizione Semplice

L'aritmetica modulare è un sistema di calcolo per numeri interi in cui i numeri "si riavvolgono" su se stessi ogni volta che raggiungono un certo valore, chiamato **modulo**.

> L'Analogia dell'Orologio
> 
> È l'esempio classico. L'orologio usa il modulo 12.
> 
> - Se sono le 10:00 e aggiungi 5 ore, non sono le 15:00, ma le 3:00.
>     
> - Matematicamente: $15 \pmod{12} = 3$.
>     
> - Il $3$ è il **resto** della divisione di $15$ per $12$.

vedi il [[Modular Exponentiation]]
## 2. Integrazione nella Blockchain

L'aritmetica modulare non è solo una curiosità matematica; è integrata profondamente in tre pilastri fondamentali delle criptovalute:

### 2.1. Creazione delle Chiavi (Crittografia a Curve Ellittiche)

Questo è l'uso più critico. Bitcoin ed Ethereum usano l'algoritmo **[[ECDSA]]** (Elliptic Curve Digital Signature Algorithm) sulla curva `secp256k1`.

L'equazione della curva sembra semplice: $y^2 = x^3 + 7$.

Tuttavia, se la usassimo sui numeri reali, sarebbe facile risalire alla chiave privata. Per renderla sicura, la usiamo su un Campo Finito definito da un numero primo gigante $p$ (il modulo).

L'equazione reale diventa:

$$y^2 \equiv x^3 + 7 \pmod{p}$$

- **L'effetto:** Invece di una linea curva liscia, il grafico diventa una "nuvola" di punti sparsi apparentemente a caso in un quadrato di dimensioni $p \times p$. Se esci dal quadrato a destra, rientri a sinistra (come nel gioco _Snake_ o _Pac-Man_).
    
- **Sicurezza:** Grazie al modulo, diventa computazionalmente impossibile fare il percorso inverso (dal punto pubblico risalire al numero segreto che lo ha generato). Questo è il **Problema del Logaritmo Discreto**.
    

### 2.2. Funzioni di Hash ([[SHA-2]]56 e [[Keccak]])

Le funzioni di hash devono produrre un output di lunghezza fissa (es. 256 bit), indipendentemente dalla lunghezza dell'input.

L'aritmetica modulare (spesso modulo $2^{32}$ o $2^{64}$ durante i calcoli interni) garantisce che i numeri non crescano all'infinito ma rimangano confinati in uno spazio fisso di bit.

- L'intero spazio degli indirizzi Bitcoin è essenzialmente un enorme cerchio modulare di numeri da $0$ a $2^{256}-1$.
    

### 2.3. Indirizzi dei Wallet

Quando crei un indirizzo Ethereum o Bitcoin, spesso l'ultimo passaggio include un checksum o una riduzione. Anche se non è sempre un "mod" puro, il concetto di mappare un numero enorme in uno spazio più piccolo e gestibile deriva da questa logica.

## 3. Perché è indispensabile? (One-Way Functions)

L'aritmetica modulare agisce come una **Trapdoor Function** (Funzione Botola):

- **Facile da calcolare in una direzione:** $A \times B \pmod C$ è immediato anche con numeri enormi.
    
- **Difficile da invertire:** Se ti do il risultato $3$ e il modulo $12$, non puoi sapere se sono partito da $15$, $27$, $39$ o $1000000003$. L'informazione originale è "nascosta" dietro l'operazione di modulo.
    

In crittografia, questa proprietà impedisce a chi vede la tua **Chiave Pubblica** (il risultato) di indovinare la tua **Chiave Privata** (il numero di partenza).

---

Sintesi visiva:

Immagina l'aritmetica modulare come il "muro" che delimita il campo da gioco della crittografia. Senza quel muro (il modulo), i numeri scapperebbero all'infinito e le chiavi sarebbero facili da calcolare al contrario.

Vuoi approfondire come questo si lega alla **Coppia di Chiavi (Pubblica/Privata)** o preferisci esplorare cos'è una **Funzione di Hash** nel dettaglio?