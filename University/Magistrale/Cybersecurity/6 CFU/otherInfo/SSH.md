# SSH (Secure Shell) e il Modello TOFU

**Tags:** #ingegneria #security #ssh #tofu #autenticazione #trust_models

## 1. Il Modello di Fiducia: TOFU

SSH non utilizza una [[Certification Authority (CA)]] centrale come avviene per il web (HTTPS). Si basa invece su un modello pragmatico chiamato **[[Trust On First Use (TOFU)]]**.

Questo approccio si fonda sulla **continuità della fiducia**:

- Non c'è un garante esterno.
    
- L'utente prende una decisione di fiducia la prima volta, e il sistema automatizza i controlli successivi.
    

---

## 2. Flusso Operativo (Workflow)

### Primo Contatto (First Connection)

Quando ti colleghi a un server SSH per la prima volta assoluta:

1. Il server presenta la sua **Chiave Pubblica**.
    
2. Il client non la conosce (non è nel database locale).
    
3. Il client chiede all'utente di accettare la chiave ("fingerprint").
    
4. **Azione:** L'utente accetta la chiave, che viene salvata localmente (solitamente nel file `known_hosts`).
    

### Connessioni Successive

Dalla seconda volta in poi:

1. Il client riceve la chiave pubblica dal server.
    
2. La confronta con quella memorizzata.
    
3. **Se combaciano:** La connessione avviene in silenzio e sicurezza.
    
4. **Se cambiano:** Il sistema lancia un **allarme critico**.
    

> [!example] Professor's Example
> 
> È come incontrare una persona che dice di chiamarsi "Mario". La prima volta ti fidi. La seconda volta, se la stessa persona ha una faccia diversa ma dice ancora di essere "Mario", ti insospettisci immediatamente.

---

## 3. Analisi di Sicurezza: Pro e Contro

### Vantaggi

- **Semplicità:** È molto facile da implementare, non richiede infrastrutture complesse o costi per certificati terzi.
    
- **Efficienza:** Funziona perfettamente in sistemi chiusi o piccoli gruppi dove gli utenti sanno cosa stanno facendo.
    

### Svantaggi e Rischi

- **First-Contact MITM:** Il tallone d'Achille è la prima connessione. Se un attaccante (Man-in-the-Middle) intercetta _proprio_ il primo collegamento, l'utente memorizzerà la chiave dell'attaccante invece di quella del server.
    
- **User Fatigue:** Gli utenti tendono a ignorare gli avvisi di sicurezza ("Warning: Remote Host Identification Has Changed"), spesso accettando la nuova chiave senza verificare, rendendo vano il sistema.
    

> [!failure] Common Pitfall
> 
> L'avviso ignorato: Se SSH ti dice che la chiave è cambiata, NON procedere ciecamente. Potrebbe essere un attacco MITM in corso. Verifica se l'amministratore del server ha effettivamente cambiato le chiavi.

---

## 4. Confronto: TOFU vs Altri Modelli

|**Caratteristica**|**TOFU (SSH)**|**PKI (X.509/HTTPS)**|**Web of Trust (PGP)**|
|---|---|---|---|
|**Trust Anchor**|Utente (alla prima connessione)|Root CA (pre-installata)|Pari (Peer-to-Peer)|
|**Scalabilità**|Limitata (difficile gestire cambi chiave)|Globale (adatta a Internet)|Non scala (complesso)|
|**Punto di Fallimento**|Utente (First Contact)|CA Centrale (se compromessa)|Soggettività dell'utente|

![[SCREEN_SSH_WARNING]]

> [!abstract] Visual Analysis
> 
> What to look at: L'immagine tipica di un avviso SSH ("WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!").
> 
> Meaning:
> 
> - **TOFU:** Semplice ma rischioso all'inizio.
>     
> - **WoT:** Decentralizzato ma complesso da gestire.
>     
> - **PKI:** Centralizzato e scalabile, ma con rischio di Single Point of Failure.
>