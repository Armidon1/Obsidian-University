# Smart Contracts

>[!Abstract] Definizione
>Uno Smart Contract ("contratto intelligente") è un programma informatico o protocollo di transazione che esegue, controlla o documenta automaticamente eventi rilevanti secondo i termini di un contratto o di un accordo.

In parole povere: è codice salvato su una blockchain che esegue automaticamente azioni ("Se succede X, allora fai Y") quando vengono soddisfatte condizioni predeterminate, senza bisogno di intermediari.

> La Metafora Perfetta: Il Distributore Automatico (Vending Machine)
> 
> Nick Szabo (l'ideatore del concetto negli anni '90) paragonò lo smart contract a un distributore automatico.
> 
> - **Contratto tradizionale:** Vai da un avvocato (intermediario), paghi, lui verifica e ti consegna il bene.
>     
> - **Smart Contract:** Inserisci la moneta nel distributore. La macchina (il codice) verifica _autonomamente_ l'importo e rilascia _automaticamente_ la lattina. Se l'importo è errato, ti restituisce i soldi. Nessun commesso, nessuna attesa, logica imparziale.
>     

## Come Funziona (Logica "If-Then")

Gli smart contract seguono la logica condizionale:

1. **Codifica:** Le regole dell'accordo vengono scritte in codice (es. in linguaggio _Solidity_ su Ethereum).
    
2. **Deployment:** Il contratto viene caricato sulla blockchain, ottenendo un indirizzo univoco. Da quel momento è immutabile.
    
3. **Trigger:** Un evento esterno o una transazione attiva il contratto.
    
4. **Esecuzione:** I nodi della rete eseguono il codice. Se le condizioni sono vere (es. "L'utente A ha inviato 5 ETH"), il contratto esegue l'azione (es. "Trasferisci il titolo di proprietà digitale all'utente A").
    

## **Caratteristiche Chiave**

- **Self-executing (Auto-eseguibili):** Non serve un amministratore per farli partire o rispettare.
    
- **Immutabili:** Una volta caricato, il codice non può essere cambiato (nemmeno dal creatore). _Nota: questo è un'arma a doppio taglio in caso di bug._
    
- **Deterministici:** Dato lo stesso input, produrranno sempre lo stesso output, ovunque vengano eseguiti.
    
- **Trustless:** Le parti non devono fidarsi l'una dell'altra, ma solo del codice (che è pubblico e verificabile).
    

## **Casi d'Uso Reali (Applicazioni)**

|**Settore**|**Applicazione**|**Esempio Pratico**|
|---|---|---|
|**DeFi (Finanza)**|Prestiti automatici|Deposito Bitcoin come garanzia e ricevo automaticamente dollari (stablecoin) in prestito. Se il valore dei Bitcoin crolla, il contratto liquida la posizione per ripagare il debito.|
|**NFT & Gaming**|Royalties|Un artista vende un'opera digitale. Lo smart contract assicura che ogni volta che l'opera viene rivenduta in futuro, il 10% del prezzo vada automaticamente all'artista originale.|
|**Assicurazioni**|Parametriche|Un'assicurazione volo collegata a dati aerei. Se il volo ritarda > 2 ore (dato fornito da un oracolo), il rimborso parte in automatico sul wallet del cliente.|
|**Supply Chain**|Pagamenti|Il pagamento al fornitore viene sbloccato automaticamente solo quando il GPS del container segnala l'arrivo in porto.|

## **Componenti Critici**

- **Gas Fees:** Per eseguire uno smart contract si paga una tassa alla rete (gas) per compensare l'energia di calcolo usata dai nodi. Codice complesso = più gas.
    
- **Oracoli (Oracles):** Gli smart contract sono "chiusi" nella blockchain e non vedono il mondo esterno (es. il prezzo del dollaro, il meteo, i risultati sportivi). Gli _Oracoli_ (come Chainlink) sono ponti che portano dati off-chain dentro la blockchain in modo sicuro per attivare i contratti.
    

## **Rischi**

- **Bugs nel codice:** Se c'è un errore nel codice (vulnerabilità), gli hacker possono svuotare il contratto. Poiché è immutabile, non si può "patchare" facilmente come un software normale.
    
- **Code is Law?** Il dilemma etico: se il codice permette un'azione non prevista ma tecnicamente valida (es. un exploit), è "legale" o è un furto?
    
