# Autenticazione Mutua (Mutual Authentication)

**Tags:** #engineering #cybersecurity #authentication #kerberos #network-security

---

## 1. Definizione e Concetto Generale

L'**Autenticazione Mutua** è un processo di sicurezza in cui entrambe le entità coinvolte in una transazione si identificano e si autenticano l'una con l'altra.

In un tipico scenario client-server:

- Il **Client** dimostra la propria identità al Server.
    
- Il **Server** dimostra la propria identità al Client.
    

Questo approccio garantisce che un utente non fornisca dati sensibili a un server impostore (attacco "Rogue Server") e che il server non fornisca servizi a utenti non autorizzati.

---

## 2. Implementazione in Kerberos (v4)

In Kerberos, l'autenticazione mutua avviene nell'ultima fase dello scambio (Fase AP - Application Service), quando il client contatta il server finale (es. Bob) per utilizzare una risorsa.

### Logica del Messaggio AP_REP

Quando Alice invia la sua richiesta (`AP_REQ`), può richiedere che Bob confermi la sua identità. Se Bob è autentico, risponde con un messaggio di "risposta all'applicazione":

La definizione matematica del messaggio di risposta è:

$$AP\_REP = K_{AB} \{ \text{timestamp} + 1 \}$$

> [!abstract] Math Analysis
> 
> - **$K_{AB}$**: È la chiave di sessione che solo Alice e il vero Bob conoscono (estratta rispettivamente dalla risposta del TGS e dal ticket).
>     
> - **timestamp + 1**: Il server prende il timestamp inviato da Alice, lo incrementa di 1 e lo ricifra.
>     
> - **Significato**: Dimostra che il server è stato in grado di decifrare il ticket (conoscendo la sua master key $K_B$) e di leggere la chiave di sessione $K_{AB}$.
>     

---

## 3. Il Flusso Procedurale

L'autenticazione mutua segue questi passaggi logici:

1. **Richiesta del Client**: Alice invia il Ticket e l'Authenticator cifrato con la chiave di sessione.
    
2. **Verifica del Server**: Bob decifra il ticket, ottiene la chiave di sessione e con essa decifra l'authenticator.
    
3. **Prova di Autenticità**: Bob modifica il timestamp ricevuto e lo rimanda indietro cifrato.
    

> [!abstract] Visual Analysis
> 
> What to look at: Nota la freccia di ritorno dal Server verso la Workstation dell'utente.
> 
> Meaning: Questo scambio conferma ad Alice che non sta parlando con un attaccante "Man-in-the-Middle", ma con il server legittimo che possiede le chiavi corrette.

---

## 4. Requisiti e Limiti

### Sincronizzazione Temporale

L'intero processo si basa sui timestamp. Per funzionare correttamente, Kerberos richiede un **orologio globale sincronizzato** tra tutti i partecipanti alla rete.

- Se l'orologio del server è troppo avanti o indietro rispetto a quello del client, l'authenticator risulterà invalido.
    

### Protezione contro il Replay

L'uso del timestamp incrementato ($+1$) nel messaggio di risposta serve a:

- Distinguere la risposta del server dal messaggio originale del client.
    
- Impedire che un attaccante possa semplicemente riutilizzare il pacchetto intercettato.
    

---

> [!tip] Exam Focus
> 
> Il professore spesso chiede: "Perché il server incrementa il timestamp di 1 invece di rimandarlo uguale?"
> 
> Risposta: Per evitare attacchi di riflessione o replay. Se il server rimandasse lo stesso timestamp cifrato, un attaccante potrebbe intercettare il messaggio del client e usarlo per fingersi il server senza nemmeno conoscere la chiave.

> [!failure] Common Pitfall
> 
> Non pensare che l'autenticazione mutua sia automatica in ogni connessione. È una funzione che il client deve richiedere esplicitamente nel messaggio di richiesta iniziale.

---
