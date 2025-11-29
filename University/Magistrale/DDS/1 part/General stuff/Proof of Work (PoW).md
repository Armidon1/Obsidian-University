# Proof of Work (PoW)

> [!Abstract] Definizione
> Il Proof of Work (PoW), o "prova di lavoro", è un meccanismo di consenso utilizzato nelle reti blockchain per confermare le transazioni e creare nuovi blocchi. È il protocollo originale delle criptovalute, reso celebre da Bitcoin, e richiede che i partecipanti alla rete (chiamati miner) risolvano complessi problemi matematici per dimostrare di aver speso una certa quantità di energia computazionale.

## **Come Funziona (Il Meccanismo)**

1. **Il Puzzle Crittografico:** La rete propone un problema matematico complesso basato su funzioni di _hash_ (es. SHA-256 per Bitcoin).
    
2. **Mining:** I miner competono utilizzando la potenza di calcolo (hashrate) dei loro hardware per trovare una soluzione (chiamata _nonce_) che, combinata con i dati del blocco, produca un hash inferiore a un certo target di difficoltà.
    
3. **La "Prova":** Il primo miner che trova la soluzione la trasmette alla rete.
    
4. **Verifica Asimmetrica:** La soluzione è difficile da trovare (richiede molta energia e tempo) ma facilissima da verificare per gli altri nodi (richiede millesimi di secondo).
    
5. **Ricompensa:** Il miner vincente aggiunge il blocco alla blockchain e riceve in cambio una ricompensa in criptovaluta (Block Reward) più le commissioni di transazione.
    

## **Caratteristiche Chiave**

- **Sicurezza:** Rende economicamente sconveniente attaccare la rete. Per alterare la blockchain (es. "double spending"), un attaccante dovrebbe possedere più del 51% della potenza di calcolo totale della rete (attacco 51%), il che richiederebbe costi hardware ed energetici proibitivi.
    
- **Decentralizzazione:** In teoria, permette a chiunque abbia hardware di partecipare, sebbene oggi richieda attrezzature specializzate (ASIC).
    
- **Adattamento della Difficoltà:** La rete regola automaticamente la difficoltà del puzzle in base alla potenza di calcolo totale per mantenere costante il tempo di creazione dei blocchi (es. ~10 minuti per Bitcoin).
    

## **Vantaggi vs Svantaggi**

|**Vantaggi**|**Svantaggi**|
|---|---|
|**Comprovata Sicurezza:** È il meccanismo più testato e resiliente (es. la rete Bitcoin non è mai stata hackerata).|**Consumo Energetico:** Richiede enormi quantità di elettricità, sollevando preoccupazioni ambientali.|
|**Resistenza alla Censura:** Non c'è un gatekeeper centrale che decide chi può partecipare.|**Scalabilità Limitata:** I processi di calcolo rallentano la rete, gestendo poche transazioni al secondo (TPS).|
|**Obiettività:** La catena valida è sempre quella con più "lavoro" accumulato (chainwork), un criterio matematico oggettivo.|**Centralizzazione Hardware:** L'uso di ASIC costosi tende a concentrare il mining in poche "farm" o pool.|

## Differenza con Proof of Stake (PoS)

Mentre il PoW usa l'energia (lavoro computazionale) per garantire la sicurezza, il [[Proof of Stake (PoS)|PoS]] usa il capitale (monete bloccate in "staking"). Il PoW è considerato più sicuro e decentralizzato puristi, mentre il PoS è più scalabile ed ecologico.

**Esempi di utilizzo**

- **Bitcoin (BTC)**
    
- **Dogecoin (DOGE)**
    
- **Litecoin (LTC)**
    
- **Monero (XMR)** (usa un algoritmo resistente agli ASIC per favorire la decentralizzazione CPU).
    

---
