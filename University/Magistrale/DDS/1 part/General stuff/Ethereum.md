# Ethereum

>[!Abstract] **Definizione**
Ethereum è una piattaforma open-source decentralizzata basata su blockchain che permette agli sviluppatori di costruire e distribuire applicazioni decentralizzate (**dApps**).
A differenza di Bitcoin, che è stato progettato principalmente come riserva di valore e rete di pagamento, Ethereum è progettato come un **"World Computer"** (Computer Mondiale): una rete unica e condivisa in grado di eseguire codice informatico di qualsiasi tipo.

![[Pasted image 20251130130025.png]]

## **L'Analogia Fondamentale**
- **Bitcoin** è come una **calcolatrice**: fa una cosa sola (transazioni finanziarie) e la fa in modo eccellente e sicurissimo.
- **Ethereum** è come uno **smartphone**: ha un sistema operativo su cui chiunque può installare diverse applicazioni (App per prestiti, App per l'arte, App per giochi, ecc.).

## **Componenti Chiave**
1. **Ether (ETH):** La criptovaluta nativa. Non serve solo come denaro, ma come "carburante" (vedi *Gas*) per pagare la potenza di calcolo della rete.
2. **[[Smart Contracts]]:** Il cuore di Ethereum. Sono i programmi "If-This-Then-That" che girano sulla blockchain (vedi nota specifica).
3. **EVM (Ethereum Virtual Machine):** È il motore di elaborazione. Ogni nodo della rete esegue una copia dell'EVM, che traduce gli smart contract (scritti in linguaggio *Solidity*) in istruzioni che la macchina può eseguire.
4. **Gas:** La tariffa pagata in ETH per eseguire operazioni. Più complesso è il codice, più "gas" serve. Questo previene loop infiniti e spam sulla rete.

## **Evoluzione: The Merge (2.0)**
Nel settembre 2022, Ethereum ha completato un aggiornamento storico chiamato "The Merge", passando dal meccanismo di consenso **[[Proof of Work (PoW)]]** (mining) al **[[Proof of Stake (PoS)]]** (staking).
- **Risultato:** Il consumo energetico della rete è sceso del ~99.9%, rendendola "green".

## **Standard dei Token (Il linguaggio comune)**
Ethereum ha creato degli standard che permettono a chiunque di creare i propri asset sulla sua blockchain:
- **ERC-20:** Lo standard per i **token fungibili** (es. Stablecoins come USDT, o token di governance). Ogni token è uguale all'altro.
- **ERC-721:** Lo standard per i **Non-Fungible Tokens (NFT)**. Ogni token è unico (es. arte digitale, oggetti di gioco).

## **Bitcoin vs Ethereum**

| Caratteristica | Bitcoin (BTC) | Ethereum (ETH) |
| :--- | :--- | :--- |
| **Scopo Principale** | Oro Digitale / Moneta | Piattaforma per Applicazioni (dApps) |
| **Linguaggio** | Script (limitato, non Turing-completo) | Solidity (Turing-completo, programmabile) |
| **Consenso** | Proof of Work (PoW) | Proof of Stake (PoS) |
| **Block Time** | ~10 minuti | ~12 secondi |
| **Offerta (Supply)** | Limitata (21 Milioni) | Illimitata (ma con meccanismi deflazionistici di "burning") |

## **L'Ecosistema (Cosa ci gira sopra)**
Grazie alla sua flessibilità, Ethereum ha dato vita a interi settori:
- **DeFi (Finanza Decentralizzata):** Banche senza banchieri (es. Uniswap, Aave).
- **DAO:** Organizzazioni gestite da codice e votazioni dei token holder.
- **Stablecoins:** Dollari digitali che vivono su blockchain (USDC, DAI).
- **Layer 2:** Reti costruite "sopra" Ethereum (come Arbitrum o Optimism) per renderlo più veloce ed economico.

***
