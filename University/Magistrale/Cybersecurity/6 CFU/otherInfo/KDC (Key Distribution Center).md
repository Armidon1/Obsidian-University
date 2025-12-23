# KDC: Key Distribution Center

**Tags:** #engineering #cybersecurity #kerberos #authentication #server-security

---

## 1. Cos'è il KDC?

Il **Key Distribution Center (KDC)** è l'elemento centrale e più critico dell'architettura Kerberos. Agisce come una **terza parte fidata** (Trusted Third Party) che ha il compito di mediare l'autenticazione tra gli utenti (Client) e le risorse di rete (Server).

### Caratteristiche Fondamentali

- **Sicurezza Fisica:** Il KDC deve risiedere su un server fisicamente protetto e isolato.
    
- **Affidabilità:** Poiché l'intero sistema dipende dal KDC, la sua integrità è fondamentale: se il KDC viene compromesso, l'intera rete è vulnerabile.
    
- **Conoscenza Totale:** Il KDC conosce le chiavi segrete (**Master Keys**) di ogni entità registrata nel sistema, chiamate **Principals**.
    

---

## 2. Le Due Anime del KDC

Sebbene venga spesso visto come un unico blocco, il KDC è diviso logicamente in due entità distinte che intervengono in momenti diversi:

1. **Authentication Server (AS):**
    
    - Gestisce la fase di login iniziale.
        
    - Verifica l'identità dell'utente e rilascia il **TGT** (Ticket-Granting Ticket).
        
2. **Ticket-Granting Server (TGS):**
    
    - Accetta il TGT come prova dell'identità dell'utente.
        
    - Rilascia i ticket specifici per accedere ai vari servizi della rete (es. stampanti, server file).
        

> [!abstract] Visual Analysis
> 
> What to look at: Nota come le due entità, AS e TGS, attingano allo stesso database centrale delle chiavi.
> 
> Meaning: Questa separazione permette di gestire il carico e di minimizzare l'esposizione della chiave master dell'utente (usata solo con l'AS).

---

## 3. Gestione delle Master Keys

Il KDC deve memorizzare le chiavi a lungo termine di tutti i _principals_.

- **Chiavi Utente:** Derivate dalla password inserita dall'utente.
    
- **Chiavi Servizio:** Generate staticamente durante l'installazione del software del server.
    
- **Chiave Master del KDC ($K_{KDC}$):** Una chiave speciale utilizzata per cifrare l'intero database del KDC.
    

### Il Database del KDC

Tutte le informazioni sensibili sono conservate in un database cifrato.

La protezione del database segue questa logica:

$$\text{Database\_Encrypted} = K_{KDC} \{ \text{List of Principals, Master Keys, Policies} \}$$

> [!abstract] Math Analysis
> 
> Ogni volta che il KDC deve generare un ticket, deve prima "sbloccare" la chiave master del destinatario leggendola dal proprio database cifrato.

---

## 4. Performance e Disponibilità

Per evitare che il KDC diventi un collo di bottiglia (bottleneck) o un punto di fallimento unico (_Single Point of Failure_), Kerberos implementa soluzioni specifiche:

- **Replicazione:** Esistono solitamente più copie del KDC.
    
- **Master vs Slave:** Un KDC principale gestisce le modifiche (cambio password), mentre i KDC secondari (slave) servono le richieste di autenticazione per distribuire il carico.
    
- **Sincronizzazione:** Le informazioni vengono aggiornate periodicamente tra i vari KDC per mantenere la consistenza.
    

> [!tip] Exam Focus
> 
> Il professore potrebbe chiedere: "Il KDC è coinvolto in ogni singola comunicazione tra client e server?"
> 
> Risposta: No. Il KDC interviene solo per rilasciare i ticket. Una volta che Alice ha ottenuto il ticket per Bob, può parlare direttamente con lui senza interpellare ulteriormente il KDC finché il ticket è valido.

---

## 5. Il Rilascio del TGT

La funzione più importante del KDC (tramite l'AS) è la creazione del Ticket-Granting Ticket.

La formula del TGT generato dal KDC è:

$$TGT = K_{KDC} \{ \text{"Alice"}, S_A, \text{Timestamp, Lifetime} \}$$

> [!important] Nota sulla Sicurezza
> 
> Il TGT è cifrato con la chiave segreta del KDC stesso. Questo significa che il client riceve il TGT ma non può leggerlo né modificarlo, può solo "consegnarlo" al TGS quando ne ha bisogno.

---

> [!failure] Common Pitfall
> 
> Spesso si confonde il KDC con un normale database di utenti. Ricorda: il KDC non memorizza le password in chiaro, ma solo le chiavi derivate o i risultati crittografici necessari per validare le sessioni.

Vorresti che approfondissi come avviene tecnicamente la **sincronizzazione dei database** tra un Master KDC e i suoi Slave per garantire la coerenza dei dati?