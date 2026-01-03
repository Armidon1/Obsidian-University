# Trust On First Use (TOFU): Il Modello della Continuità

**Tags:** #ingegneria #security #tofu #ssh #trust_models #autenticazione

## 1. Definizione e Concetto Base

Il **TOFU** (Trust On First Use) è un modello di sicurezza pragmatico che si basa sulla **continuità della fiducia** piuttosto che su un garante esterno (come una CA).

L'idea fondamentale è semplice:

- La prima volta che incontri un interlocutore, **ti fidi ciecamente** (Leap of Faith) e memorizzi la sua identità.
    
- Da quel momento in poi, ti fidi solo se l'identità presentata **è identica** a quella memorizzata la prima volta.
    

> [!example] Professor's Example: SSH
> 
> L'applicazione più famosa del TOFU è il protocollo SSH (Secure Shell). Quando ti colleghi a un server remoto per la prima volta, il client ti chiede di accettare l'impronta (fingerprint) della chiave. Se domani quella chiave cambia, SSH ti blocca con un allarme rosso.

---

## 2. Il Flusso Operativo (Workflow)

Come funziona passo dopo passo la logica TOFU durante una connessione:

1. **Primo Contatto (First Contact):**
    
    - Il client si collega al server.
        
    - Il server invia la sua Chiave Pubblica.
        
    - Il client cerca nel suo database locale (`known_hosts`).
        
    - **Risultato:** Chiave non trovata.
        
    - **Azione:** Chiede all'utente: "Non conosco questo server. Ti fidi?". Se l'utente dice Sì, la chiave viene salvata.
        
2. **Contatti Successivi (Subsequent Contacts):**
    
    - Il client si collega e riceve la chiave pubblica.
        
    - Confronta la chiave ricevuta con quella salvata nel file `known_hosts`.
        
    - **Caso A (Match):** Le chiavi coincidono. Connessione stabilita silenziosamente.
        
    - **Caso B (Mismatch):** Le chiavi sono diverse.
        
    - **Azione:** **BLOCCO TOTALE**. Il sistema avvisa l'utente di un possibile attacco Man-in-the-Middle (MITM).
        

> [!abstract] Visual Analysis
> 
> What to look at: L'immagine tipica di un avviso SSH ("WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!").
> 
> Meaning: Il sistema TOFU ha rilevato una rottura della continuità. Potrebbe essere un amministratore che ha reinstallato il server, oppure un attaccante che sta intercettando la connessione. Il protocollo, per sicurezza, presume il peggio.

---

## 3. Analisi di Sicurezza: Pro e Contro

Il TOFU è un compromesso tra sicurezza e usabilità.

### Vantaggi

- **Semplicità:** Non serve nessuna infrastruttura complessa (niente CA, niente CRL, niente WoT).
    
- **Zero Costi:** Non devi pagare Verisign o DigiCert per un certificato.
    
- **Efficienza:** Ottimo per sistemi chiusi, reti interne o amministrazione di server dove gli utenti sono tecnici consapevoli.
    

### Svantaggi (Il Tallone d'Achille)

- **First-Contact MITM:** Il momento critico è la **prima connessione**. Se un attaccante si interpone _proprio la prima volta_ che ti colleghi, tu memorizzerai la chiave dell'attaccante come "fidata". Da quel momento in poi, l'attaccante sarà trasparente.
    
- **Key Rotation:** Se il server legittimo cambia chiave (es. reinstallazione), tutti gli utenti riceveranno un errore spaventoso. Bisogna "pulire" manualmente il database locale.
    
- **User Fatigue:** Gli utenti tendono a ignorare gli avvisi di sicurezza, cliccando "Yes" pur di lavorare, vanificando la protezione.
    

> [!failure] Common Pitfall
> 
> Ignorare l'avviso: Molti sviluppatori, vedendo l'errore di "chiave cambiata", cancellano semplicemente il file known_hosts senza verificare se il cambio fosse legittimo. Questo comportamento apre la porta agli attacchi MITM.

---

## 4. Confronto: TOFU vs PKI

|**Caratteristica**|**TOFU (SSH)**|**PKI (HTTPS)**|
|---|---|---|
|**Prima Connessione**|"Salto della fede" (Rischio MITM)|Verificata tramite Root CA (Sicura)|
|**Gestione Chiavi**|Decentralizzata (ogni client ha il suo DB)|Centralizzata (CA garantisce per tutti)|
|**Cost**|Nullo|Costo di gestione/acquisto certificati|
|**Rotazione Chiavi**|Problematica (avvisi errore per tutti)|Trasparente (basta rinnovare il certificato)|
|**Ambito**|Amministrazione Server, P2P (Signal/WhatsApp*)|E-commerce, Banking, Web pubblico|

> [!tip] Exam Focus
> 
> Nota: App di messaggistica come Signal o WhatsApp usano un approccio ibrido che ricorda il TOFU (chiamato TOFU+ o Trust On First Use with Persistence): la prima volta accettano la chiave silenziosamente, ma se il contatto cambia chiave (es. cambia telefono), ti avvisano in chat ("Il codice di sicurezza di Alice è cambiato").