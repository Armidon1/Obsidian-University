# Ethereum Swarm

## 1. Definizione

Swarm è un sistema di archiviazione e comunicazione decentralizzato [[Peer-To-Peer (P2P)]].

È stato progettato per fornire uno strato di storage persistente, resistente alla censura e privo di permessi (permissionless) per il "Computer Mondiale" (Ethereum).

Se [[Ethereum]] è la CPU (calcolo), Swarm è l'**Hard Disk** (archiviazione).

## 2. La "Santa Trinità" del Web3

Swarm è nato come uno dei tre pilastri fondamentali della visione originale del Web3 proposta da Gavin Wood (co-fondatore di Ethereum):

1. **Contratti & Calcolo:** **Ethereum** (Logica).
    
2. **Storage:** **Swarm** (Dati statici).
    
3. **Messaggistica:** **Whisper** (ora evoluto in _Waku_) per la comunicazione tra nodi.
    

L'obiettivo è creare un internet dove siti web e dApps (Applicazioni Decentralizzate) possano esistere interamente senza server centralizzati (Serverless).

## 3. Come Funziona (Architettura DISC)

Swarm non salva i file interi in un unico posto. Utilizza un concetto chiamato **DISC (Distributed Immutable Store of Chunks)**.

### 3.1. Chunks (Pezzi)

Quando carichi un file su Swarm:

1. Il file viene diviso in pezzi fissi di 4KB chiamati **Chunks**.
    
2. Ogni chunk viene "hashato" (vedi nota su _[[Merkle Trees]]_) per ottenere un indirizzo unico.
    
3. Questi pezzi vengono distribuiti tra i vari nodi della rete chiamati **Bee**.
    

### 3.2. Kademlia e Prossimità

A differenza di un semplice cloud, i nodi Swarm non salvano dati a caso. Usano una metrica di "distanza matematica" (basata sullo XOR degli hash, simile alla DHT Kademlia). Un nodo salva i chunks che sono matematicamente "vicini" al proprio indirizzo.

![Immagine di decentralized storage network diagram](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcRSL092S-eLj5233AFawLTx0FfBLSehhSkTmVYKSgGGYwQDNXWdmgXLISGUK2UBGf-iTzzpCKn4hBS6pGR6Rk3lrSgeu8IMEhgBbVQYO2J4UUJ1vAk)

Shutterstock

## 4. Incentivi Economici (La differenza con IPFS)

Questa è la caratteristica distintiva principale.

Mentre IPFS è un protocollo di trasporto dati (come HTTP) che non ha incentivi nativi (serve Filecoin sopra), Swarm ha gli incentivi integrati nel protocollo base.

- **Token BZZ:** È la valuta di Swarm.
    
- **Larghezza di banda e Storage:** I nodi che richiedono dati pagano in BZZ; i nodi che archiviano e servono dati guadagnano BZZ.
    
- **Swear and Swindle (Giura e Truffa):** Un complesso gioco di teoria dei giochi e smart contracts che garantisce che i nodi non mentano sui dati che possiedono.
    

## 5. Confronto: Swarm vs IPFS

|**Caratteristica**|**IPFS (+ Filecoin)**|**Ethereum Swarm**|
|---|---|---|
|**Natura**|Protocollo generico per il web distribuito.|Nato specificamente per integrarsi con Ethereum.|
|**Incentivi**|Separati (IPFS è gratis/volontario, Filecoin è a pagamento).|Integrati e nativi (tutto gira intorno al token BZZ).|
|**Privacy**|I dati sono pubblici di default (chi ha l'hash può vederli).|Supporta nativamente la crittografia e l'offuscamento (privacy-preserving).|
|**Stato di sviluppo**|Molto maturo, ampiamente adottato.|Più recente, tecnicamente complesso, ancora in forte sviluppo.|
|**Filosofia**|"Rendiamo il web peer-to-peer".|"Rendiamo le dApp inarrestabili".|

## 6. Perché è importante? (Censorship Resistance)

In un sistema centralizzato (Amazon AWS), se il governo o l'azienda decide di spegnere un sito, basta premere un interruttore.

Su Swarm, poiché il sito web è spezzettato in migliaia di chunk distribuiti su migliaia di computer anonimi nel mondo (e questi computer sono pagati automaticamente per tenerli online), è quasi impossibile spegnerlo o censurarlo.

---
