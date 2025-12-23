# Kerberos: Protocollo di Autenticazione per Sistemi Distribuiti

**Tags:** #engineering #cybersecurity #kerberos #SSO #network-security

---

## 1. Introduzione e Obiettivi

**Kerberos** è un protocollo di autenticazione progettato per reti aperte e sistemi distribuiti. Il suo scopo principale è permettere a un utente di accedere a risorse di rete (stampanti, file system, database) in modo sicuro, senza dover trasmettere la propria password in chiaro.

### Caratteristiche Fondamentali

- **Autenticazione Mutua:** Sia l'utente che il server verificano reciprocamente l'identità dell'altro.
    
- **Single Sign-On (SSO):** L'utente inserisce le credenziali una sola volta all'inizio della sessione.
    
- **Basato su Ticket:** L'accesso alle risorse è mediato da "biglietti" temporanei emessi da un'autorità centrale.
    
- **Crittografia Simmetrica:** Utilizza algoritmi a chiave segreta per proteggere i messaggi.
    

---

## 2. Architettura e Componenti Core

Il sistema Kerberos ruota attorno al **KDC (Key Distribution Center)**, un'entità terza fidata che conosce le chiavi segrete di tutti i partecipanti.

### I "Principal" e le Master Key

Ogni entità registrata nel sistema è definita **Principal**.

- **Master Key:** Ogni principal condivide una chiave segreta con il KDC.
    
- **Utenti Umani:** La Master Key è derivata direttamente dalla **password** tramite una funzione di hashing.
    
- **Risorse di Sistema:** Le chiavi sono generate staticamente durante la configurazione del servizio.
    
- **Database KDC:** Contiene tutte le Master Key, a loro volta cifrate con la Master Key del KDC stesso per garantire la massima sicurezza fisica e logica.
    

---

## 3. La Logica del Ticket e dell'Authenticator

Il protocollo utilizza due strutture dati fondamentali per validare l'accesso.

### Il Ticket (T)

Il Ticket è un oggetto che "presenta" l'utente al server. È cifrato con la chiave del server di destinazione, quindi l'utente non può vederne il contenuto.

La definizione matematica del Ticket di Alice per il servizio Bob è:

$$T_{A,B} = K_B \{ K_{AB}, \text{"Alice"}, \text{Addr}, \text{Lifetime}, \text{Timestamp} \}$$

> [!abstract] Math Analysis
> 
> - $K_B$: Master Key di Bob. Solo lui può decifrare il ticket.
>     
> - $K_{AB}$: **Session Key** generata dal KDC per la comunicazione tra Alice e Bob.
>     
> - **Addr/Lifetime:** Parametri di sicurezza che indicano da dove Alice può collegarsi e per quanto tempo.
>     

### L'Authenticator

Poiché un ticket può essere intercettato e riutilizzato (replay attack), Alice deve allegare un Authenticator cifrato con la chiave di sessione:

$$\text{Authenticator} = K_{AB} \{ \text{"Alice"}, \text{Timestamp} \}$$

> [!abstract] Visual Analysis
> 
> What to look at: Lo schema mostra che il Ticket è a lungo termine, mentre l'Authenticator è valido solo per pochi minuti.
> 
> Meaning: Il Ticket prova che Alice è autorizzata, l'Authenticator prova che Alice è "viva" e presente in quel momento.

---

## 4. Il Flusso del Protocollo (Topic-by-Topic)

Il protocollo Kerberos si articola in tre fasi logiche, ognuna composta da uno scambio di messaggi (Request/Reply).

### Fase A: Login Iniziale (AS)

L'utente Alice accede alla sua workstation.

- **Azione:** La workstation chiede al **AS (Authentication Server)** un ticket per poter parlare con il resto del sistema.
    
- **Risultato:** Alice riceve un **TGT (Ticket-Granting Ticket)** e una chiave di sessione $S_A$.
    
- **Dettaglio Tecnico:** La risposta è cifrata con la chiave master dell'utente ($K_A$). Solo inserendo la password corretta Alice può decifrare il messaggio.
    

### Fase B: Richiesta del Servizio (TGS)

Alice vuole accedere a un server specifico (es. Bob).

- **Azione:** Alice invia il suo TGT al **TGS (Ticket-Granting Server)**.
    
- **Risultato:** Il TGS verifica il TGT e rilascia un ticket specifico per Bob ($T_{A,B}$).
    

### Fase C: Accesso Finale (AP)

- **Azione:** Alice presenta il ticket e l'authenticator a Bob.
    
- **Risultato:** Bob decifra il ticket, ottiene la chiave di sessione e verifica l'authenticator. Se tutto coincide, garantisce l'accesso.
    

---

## 5. Meccanismi di Sicurezza Avanzati

### Sincronizzazione Temporale

Kerberos richiede che tutti gli orologi della rete siano sincronizzati (Global Synchronous Clock).

- **Motivazione:** Gli authenticator usano i timestamp per evitare i **Replay Attack**.
    
- **Tolleranza:** Solitamente è ammesso uno scarto massimo di 5 minuti.
    

> [!failure] Common Pitfall
> 
> Se l'orologio di un client è sfasato rispetto a quello del KDC o del Server, l'autenticazione fallirà sistematicamente anche se la password è corretta.

### Scalabilità e Realms

In sistemi molto vasti, Kerberos divide la rete in **Realms** (domini amministrativi).

- Ogni Realm ha il proprio Master KDC.
    
- È possibile l'autenticazione **Inter-Realm**: un KDC può fidarsi di un altro KDC scambiandosi una chiave segreta cross-domain.
    

---

## 6. Evoluzione: Versione 4 vs Versione 5

Sebbene la filosofia originale (v4) rimanga il pilastro didattico, la versione 5 ha introdotto miglioramenti critici:

|**Funzionalità**|**Kerberos v4**|**Kerberos v5**|
|---|---|---|
|**Crittografia**|Principalmente DES (debole)|AES e altri algoritmi multipli|
|**Delegation**|Non supportata|Supportata (Alice delega diritti a Bob)|
|**Flessibilità**|Campi fissi|Encoding ASN.1 flessibile|
|**Sicurezza**|Solo Timestamps|Timestamps + Nonce (numeri casuali)|

> [!tip] Exam Focus
> 
> Ricorda che il TGT è l'elemento che abilita il Single Sign-On. Senza TGT, l'utente dovrebbe digitare la password per ogni singola risorsa richiesta durante la giornata.

---

**Vuoi che approfondisca lo schema dei messaggi specifici (AS_REQ, TGS_REQ) o che ti crei una tabella di confronto tra le chiavi utilizzate?**

# Kerberos: Altre informazioni
## 1. Visione d'Insieme

**Kerberos** è un protocollo di autenticazione per **sistemi distribuiti** che permette a un utente di dimostrare la propria identità a un servizio (e viceversa) attraverso una rete non sicura.

I pilastri del protocollo sono:

- **Single Sign-On (SSO):** L'utente inserisce la password una sola volta.
    
- **Terza Parte Fidata:** Si basa sul **KDC (Key Distribution Center)**, un server sicuro che conosce le chiavi di tutti.
    
- **Crittografia Simmetrica:** Utilizza chiavi condivise per cifrare i messaggi.
    
- **Basato su Ticket:** L'accesso alle risorse è mediato da "biglietti" temporanei.
    

---

## 2. Componenti dell'Architettura

In Kerberos, ogni entità (utente o servizio) è chiamata **Principal**. L'infrastruttura centrale (KDC) è divisa logicamente in due parti:

- **Authentication Server (AS):** Gestisce il login iniziale e verifica l'identità dell'utente.
    
- **Ticket-Granting Server (TGS):** Rilascia i ticket per i servizi specifici (es. mail, file system).
    
- **Database:** Il KDC conserva tutte le **Master Key** dei principal, cifrate con la chiave master del KDC stesso.
    

> [!important] Definizione di Master Key
> 
> Per un utente umano, la Master Key è derivata direttamente dalla sua password. Per un servizio, è definita durante la configurazione dell'applicazione.

---

## 3. Logica Matematica dei Ticket

Il cuore della sicurezza di Kerberos risiede nella struttura dei ticket e degli authenticator.

### Il Ticket (T)

Il ticket serve a trasportare la Session Key in modo sicuro verso il server di destinazione.

La struttura logica di un ticket per il servizio B è:

$$T_{A,B} = K_{B} \{ K_{AB}, \text{Alice}, \text{Addr}, \text{Lifetime}, \text{Timestamp} \}$$

> [!abstract] Math Analysis
> 
> - $K_B$: Chiave segreta del server di destinazione. Solo lui può "aprire" il ticket.
>     
> - $K_{AB}$: Nuova chiave di sessione generata dal KDC per la comunicazione tra A e B.
>     
> - **Lifetime:** Indica per quanto tempo il ticket è considerato valido (solitamente multipli di 5 minuti).
>     

### L'Authenticator (A)

Poiché un ticket può essere intercettato, Alice deve dimostrare di essere la vera proprietaria inviando un Authenticator:

$$Authenticator = K_{AB} \{ \text{Alice}, \text{timestamp} \}$$

> [!abstract] Visual Analysis
> 
> ![[SCREEN_SLIDE_TICKET_LOGIC]]
> 
> What to look at: Nota che il ticket è cifrato con la chiave del server, mentre l'authenticator è cifrato con la chiave di sessione appena creata.
> 
> Meaning: Il server decifra il ticket, ottiene $K_{AB}$, e la usa per decifrare l'authenticator. Se i dati (Alice) coincidono, l'identità è confermata.

---

## 4. Il Flusso dei Messaggi (Protocollo Completo)

Il protocollo si sviluppa in tre fasi principali, ognuna composta da una richiesta (**REQ**) e una risposta (**REP**).

### Fase 1: Richiesta TGT (Client ↔ AS)

L'utente Alice vuole loggarsi nel sistema.

1. **AS_REQ:** Alice invia il suo nome all'AS.
    
2. AS_REP: L'AS genera una chiave di sessione $S_A$ e un TGT (Ticket-Granting Ticket).
    
    Il messaggio ricevuto da Alice è:
    
    $$K_A \{ S_A, TGT \}$$
    
    dove $TGT = K_{KDC} \{ \text{Alice}, S_A \}$.
    

### Fase 2: Richiesta Servizio (Client ↔ TGS)

Alice vuole accedere a una stampante o a un server Bob.

3. TGS_REQ: Alice invia il TGT e un Authenticator cifrato con $S_A$.

4. TGS_REP: Il TGS verifica il TGT, genera $K_{AB}$ e risponde:

$$S_A \{ \text{Bob}, K_{AB}, \text{Ticket}_B \}$$

### Fase 3: Utilizzo del Servizio (Client ↔ Server Bob)

5. **AP_REQ:** Alice invia a Bob il $\text{Ticket}_B$ e un Authenticator cifrato con $K_{AB}$.
    
6. AP_REP: Bob decifra tutto, verifica l'identità e risponde per confermare (Autenticazione Mutua):
    
    $$K_{AB} \{ \text{timestamp} + 1 \}$$
    

|**Messaggio**|**Scopo**|
|---|---|
|**AS_REQ**|Richiede il TGT iniziale (Login).|
|**TGS_REQ**|Chiede il permesso di parlare con un server specifico.|
|**AP_REQ**|Presenta le credenziali al server finale.|

---

## 5. Sicurezza e Sincronizzazione

Kerberos introduce meccanismi specifici per prevenire attacchi comuni.

- **Replay Attack:** Per evitare che un attaccante riutilizzi un messaggio intercettato, Kerberos richiede un **orologio globale sincronizzato**.
    
- **Authenticator:** Scade dopo pochissimi minuti. Se il timestamp nel messaggio differisce troppo dall'orologio del server, la richiesta viene rifiutata.
    
- **Caches di Replay:** I server mantengono memoria dei timestamp recenti per scartare duplicati esatti.
    

> [!failure] Common Pitfall
> 
> Molti pensano che Kerberos invii la password in rete. Falso. La password viene usata solo localmente sulla workstation per derivare $K_A$ e decifrare la risposta dell'AS. In rete viaggia solo il TGT cifrato.

---

## 6. Scalabilità: I Realms

Un **Realm** è un dominio amministrativo (es. un dipartimento universitario). Quando il sistema diventa troppo grande, si usano più Realm.

- Ogni Realm ha il suo **Master KDC**.
    
- I KDC di Realm diversi possono stabilire una relazione di fiducia scambiandosi chiavi (**Cross-Realm**).
    
- Alice può ottenere un ticket dal suo KDC locale per parlare con il TGS di un Realm remoto e accedere alle sue risorse.
    

---

## 7. Evoluzione: Differenze tra v4 e v5

Sebbene la filosofia sia identica, la **Versione 5** ha introdotto miglioramenti fondamentali:

1. **Flessibilità Crittografica:** La v4 era legata al DES (ormai debole), la v5 supporta AES e altri algoritmi.
    
2. **Delegation:** In v5, Alice può permettere a un server di agire per suo conto per un tempo limitato.
    
3. **Nonce:** Oltre ai timestamp, si usano numeri casuali (nonce) per una protezione extra contro i replay.
    
4. **Ticket Rinnovabili:** Supporto per ticket che durano molto tempo senza dover reinserire la password.
    

---

> [!tip] Exam Focus
> 
> Il professore potrebbe chiedere perché esiste il TGT.
> 
> Risposta: Serve a evitare che l'utente debba digitare la password ogni volta che vuole accedere a un nuovo servizio. Il TGT funge da "credenziale temporanea" che scade solitamente dopo 8-10 ore.

