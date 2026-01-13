last lesson [[15 CS Lower Level - TLS and IPSec]]
In questa sezione potrebbe essere comodo consultare la tabella [[Common Ports and Protocols]]
# Firewalls

**Tags:** #ingegneria #cybersecurity #sicurezza_reti #firewall #reti_di_calcolatori

## 1. Introduzione e Architettura di Rete

Il concetto fondamentale alla base dell'utilizzo di un Firewall è la **separazione**. L'obiettivo è isolare la rete locale (considerata sicura) da Internet (considerato non sicuro).

I componenti principali di questa architettura sono:

- **Trusted hosts and networks:** La rete interna fidata (**Intranet**).
    
- **Firewall:** Il dispositivo di sicurezza centrale.
    
- **Router:** Gestisce l'instradamento del traffico verso l'esterno.
    
- **DMZ (Demilitarized Zone):** Una zona intermedia che ospita server e reti accessibili pubblicamente.
    
- **Internet:** Il mondo esterno (non fidato).
    

![[Pasted image 20260108153116.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo schema mostra il Firewall posizionato tra la Intranet (sinistra), la DMZ (basso) e il Router che porta a Internet (destra).
> 
> **Meaning:** Il Firewall agisce come unico punto di passaggio controllato. La **DMZ** è separata dalla Intranet per proteggere i dati sensibili anche se i server pubblici (web, mail) venissero compromessi.

## 2. Funzioni Principali del Firewall

Il Firewall è definito come un sistema che controlla e monitora il traffico di rete. Nella maggior parte dei casi, collega una **rete interna** al mondo esterno (**public internet**).

Le sue funzioni chiave sono:

- **Controllo del traffico:**
    
    - Limita il traffico **inbound** (in entrata) e **outbound** (in uscita).
        
    - Permette il passaggio solo al traffico autorizzato (**Authorized traffic**).
        
- **Occultamento:** Nasconde la struttura della rete interna al mondo esterno.
    
- **Accesso ai servizi:** Controlla e monitora chi accede a quali servizi.
    

### Personal Firewall

Esiste una variante chiamata **Personal firewall**, che risiede direttamente sulle macchine degli utenti finali (**end-user machines**) per proteggere il singolo dispositivo.

> [!important] Nota di Sicurezza
> 
> Il firewall stesso deve essere un sistema blindato, ovvero immune agli attacchi ("Should be immune to attacks").

## 3. Limitazioni del Firewall

Nonostante la sua importanza, il firewall non è una soluzione totale. Presenta delle limitazioni specifiche:

- **Attacchi passanti:** Non protegge dagli attacchi che riescono a passare attraverso le regole del firewall (traffico apparentemente legittimo).
    
- **Minacce interne:** Non protegge dagli attacchi originati all'interno della rete che deve proteggere (**Internal threats**).
    
- **Malware:** Non è in grado di evitare o bloccare tutti i virus e worm possibili. Questo dipende dalle troppe varianti e dalle caratteristiche specifiche dei Sistemi Operativi.
    
    - _Eccezione:_ A meno che non si utilizzi un **Personal firewall** specifico.
        

## 4. Tipologie di Firewall

I firewall sono classificati in base al livello a cui operano e alla tecnologia utilizzata:

1. **Packet-filtering router (Packet filter):**
    
    - Il filtraggio avviene ispezionando gli **header** dei pacchetti (e in alcuni casi il payload).
        
    - Tipicamente **stateless** (senza memoria di stato), ma a volte **stateful**.
        
2. **Proxy gateway:**
    
    - Tutto il traffico in entrata è diretto al firewall; tutto il traffico in uscita appare come proveniente dal firewall.
        
    - **Application-level:** Utilizza proxy separati per ogni applicazione (es. diversi proxy per SMTP, HTTP, FTP). Le regole di filtraggio sono **application-specific**.
        
    - **Circuit-level:** Indipendente dall'applicazione, agisce in modo "trasparente".
        
3. **Personal firewall:**
    
    - Utilizza regole specifiche per le applicazioni sulla macchina locale (es. "nessuna connessione telnet in uscita dal client email").
        

## 5. Packet Filtering in Dettaglio

Questa tecnica decide se permettere a un pacchetto di procedere basandosi **solo** sulle informazioni contenute nel pacchetto stesso.

- **Decisione:** Presa su base "per-packet" (singolo pacchetto).
    
- **Caratteristica Stateless:** Non esamina il contesto del pacchetto (es. non sa a quale connessione TCP appartiene o l'applicazione specifica).
    

### Informazioni utilizzate per il filtraggio

Il Packet Filter analizza:

- Indirizzi IP sorgente e destinazione.
    
- Porte (Ports).
    
- Identificativo del protocollo (TCP, UDP, ICMP, etc.).
    
- Flag TCP (SYN, ACK, RST, PSH, FIN).
    
- Tipo di messaggio ICMP.
    

Logica: Le regole si basano sul pattern-matching.

Regola di default: Solitamente esiste una regola finale implicita di accept o reject (spesso deny all).

## 6. Esempi di Regole di Packet Filtering

Di seguito sono riportate le tabelle logiche utilizzate per definire le policy di sicurezza.

### Esempio A: Blocco specifico e permesso SMTP

- **Policy:** Non ci fidiamo dell'host "SPIGOT". Permettiamo connessioni alla nostra porta email.
    

|**Action**|**Ourhost**|**Port**|**Theirhost**|**Port**|**Comment**|
|---|---|---|---|---|---|
|**block**|*|*|SPIGOT|*|we don't trust these people|
|**allow**|OUR-GW|25|*|*|connection to our SMTP port|

### Esempio B: Regola di Default

- **Policy:** Se non specificato diversamente, blocca tutto.
    

|**Action**|**Ourhost**|**Port**|**Theirhost**|**Port**|**Comment**|
|---|---|---|---|---|---|
|**block**|*|*|*|*|default|

### Esempio C: Traffico in uscita (Ingenuo)

- **Policy:** Permettiamo connessioni verso server SMTP esterni e accettiamo le risposte.
    

|**Action**|**Src**|**Port**|**Dest**|**Port**|**Flags**|**Comment**|
|---|---|---|---|---|---|---|
|**allow**|{our hosts}|*|*|25||our packets to their SMTP port|
|**allow**|*|25|*|*|ACK|their replies|

### Esempio D: Gestione traffico e porte alte

- **Policy:** Gestione delle chiamate in uscita e traffico verso porte non privilegiate.
    

|**Action**|**Src**|**Port**|**Dest**|**Port**|**Flags**|**Comment**|
|---|---|---|---|---|---|---|
|**allow**|{our hosts}|*|*|*||our outgoing calls|
|**allow**|*|*|*|*|ACK|replies to our calls|
|**allow**|*|*|*|>1024||traffic to nonservers|

## 7. Implementazione FTP Packet Filter

L'esempio seguente mostra una configurazione pratica (sintassi simile a Cisco IOS) per permettere il traffico FTP verso un server specifico (`172.168.10.12`).

**Here is the exact implementation shown in the slides:**

```
! Allows a user to FTP from any IP address to the FTP server
access-list 100 permit tcp any gt 1023 host 172.168.10.12 eq 21
access-list 100 permit tcp any gt 1023 host 172.168.10.12 eq 20

! Allows packets from any client to the FTP control and data ports
access-list 101 permit tcp host 172.168.10.12 eq 21 any gt 1023
access-list 101 permit tcp host 172.168.10.12 eq 20 any gt 1023

! Application to interfaces
interface Ethernet 0
access-list 100 in  ! Apply the first rule to inbound traffic
access-list 101 out ! Apply the second rule to outbound traffic
```

> [!abstract] Code Analysis
> 
> - **Porte FTP:** Vengono aperte sia la porta **21** (Controllo) che la porta **20** (Dati).
>     
> - **Direzione:**
>     
>     - `access-list 100` gestisce il traffico in entrata (**inbound**) verso il server.
>         
>     - `access-list 101` gestisce il traffico di risposta in uscita (**outbound**) dal server verso i client (che usano porte > 1023).
>         
> - **Implicit Deny:** "Anything not explicitly permitted by the access list is denied!" (Tutto ciò che non è esplicitamente permesso è negato).
>     

## 8. Debolezze dei Packet Filters

I Packet Filters presentano vulnerabilità significative:

1. **Nessuna protezione applicativa:**
    
    - Non prevengono attacchi specifici dell'applicazione.
        
    - _Esempio:_ Se c'è un **buffer overflow** in una routine di decodifica URL, il firewall non bloccherà la stringa dell'attacco perché guarda solo i pacchetti, non il codice applicativo.
        
2. **Mancanza di autenticazione utente:**
    
    - Non supportano meccanismi di autenticazione robusti.
        
    - Si basano solo sull'autenticazione basata sull'indirizzo (**address-based authentication**), che è soggetta a spoofing.
        
3. **Assenza di funzionalità di alto livello:**
    
    - I firewall non hanno "upper-level functionality".
        
4. **Vulnerabilità TCP/IP:**
    
    - Vulnerabili ad attacchi come lo **spoofing**.
        
    - _Soluzione parziale:_ Lista di indirizzi per ogni interfaccia (i pacchetti con indirizzi interni non dovrebbero mai provenire dall'esterno).
        
5. **Errori di configurazione:**
    
    - Brecce di sicurezza dovute a **misconfiguration** sono frequenti.
        


---

# Fragmentation Attacks & Stateful Firewall Architecture

**Tags:** #ingegneria #sicurezza #firewall #frammentazione #stateful #iptables #netfilter

## 1. Fragmentation Attacks (Attacchi di Frammentazione)

Questo attacco sfrutta la divisione dei pacchetti IP. L'attaccante invia frammenti che singolarmente sembrano innocui e passano il firewall, ma quando vengono riassemblati all'interno della rete bersaglio formano un pacchetto malevolo.

### Scenari di Evasione

1. **URL o Comandi FTP:** Si spezza una stringa vietata (es. comando `put`) in due pacchetti. Se il firewall non riassembla, non legge il comando intero e lo lascia passare.
    
2. **TCP Flag Masking:** Inviare due pacchetti `ACK`. Quando riassemblati, i bit si sovrappongono formando un pacchetto `SYN` (richiesta di connessione), bypassando le regole che bloccano le nuove connessioni dall'esterno.
    
3. **IP Fragments Overlap:** Frammenti che si sovrappongono. Alcuni sistemi operativi gestiscono male la sovrascrittura in memoria.
    
4. **ICMP Oversized:** Dividere un messaggio Ping in frammenti che, uniti, superano la dimensione massima consentita, causando Buffer Overflow o crash (DoS).
    
5. **DoS da Frammenti Incompleti:** Inviare tanti "primi pezzi" senza mai mandare l'ultimo, saturando la memoria della vittima che aspetta invano.
    

---

## 2. Limiti del Filtro Stateless

I firewall tradizionali (Stateless) hanno un problema critico con le porte dinamiche (Ephemeral Ports).

- **Server:** Usano porte note (`< 1024`, es. 80 per HTTP).
    
- **Client:** Usano porte effimere (`> 1023`) per ricevere le risposte.
    

Il Dilemma:

Senza "stato", il firewall non sa distinguere tra:

1. Una risposta legittima del server a una nostra richiesta (Destinazione: porta 1234).
    
2. Un tentativo di attacco esterno verso la porta 1234.
    

---

## 3. Stateful Inspection

La soluzione è aggiungere una memoria: la State Table (Tabella di Stato). Il firewall non guarda più i singoli pacchetti, ma le Connessioni.

### Funzionamento della State Table

Quando un client interno apre una connessione, il firewall registra i dati nella tabella:

$$\text{State Entry} = \{ \text{Source IP}, \text{Dest IP}, \text{Source Port}, \text{Dest Port}, \text{Protocol}, \text{State} \}$$

> [!abstract] Visual Analysis
> 
> What to look at: Le slide mostrano una tabella con colonne come "Connection State".
> 
> Meaning: Se arriva un pacchetto dall'esterno, il firewall cerca nella tabella. Se trova una corrispondenza ("Match"), il pacchetto passa automaticamente. Se non c'è corrispondenza, viene scartato. Non serve più aprire manualmente tutte le porte > 1023.

---

## 4. Architettura Netfilter / Iptables

Su Linux, il packet filtering è gestito dal framework Netfilter (nel kernel), configurato tramite il tool iptables.

### Le Tabelle (Tables)

Ogni tabella ha uno scopo specifico:

- **filter:** (Default) Per accettare o scartare pacchetti.
    
- **nat:** Per il Network Address Translation.
    
- **mangle:** Per modificare i pacchetti (es. header TCP).
    
- **raw:** Per configurare eccezioni prima del tracciamento delle connessioni.
    

### Le Catene (Built-in Chains)

Indicano _quando_ il pacchetto viene processato:

1. **PREROUTING:** Appena il pacchetto entra (prima del routing).
    
2. **INPUT:** Diretto al firewall stesso (processo locale).
    
3. **FORWARD:** Attraversa il firewall (da un'interfaccia all'altra).
    
4. **OUTPUT:** Generato dal firewall stesso.
    
5. **POSTROUTING:** Appena prima di uscire (dopo il routing).
    

---

## 5. Targets (Azioni)

Quando un pacchetto soddisfa una regola, il firewall esegue un Target. Ecco quelli standard definiti esplicitamente nelle slide:

1. **ACCEPT:** Lascia passare il pacchetto.
    
2. **DROP:** "Lascia cadere il pacchetto sul pavimento". Viene eliminato silenziosamente, senza avvisare il mittente.
    
3. **QUEUE:** Passa il pacchetto allo **Userspace** (spazio utente).
    
    - _Significato:_ Il pacchetto viene inviato a un software esterno per un'analisi avanzata (es. un antivirus o un sistema IDS) che deciderà cosa farne.
        
4. **RETURN:** Smette di attraversare la catena corrente e torna alla catena precedente (quella che l'aveva chiamato).
    
    - _Significato:_ Simile al `return` in una funzione di programmazione.
        

---

# Iptables: Tables, Chains and Modules

**Tags:** #ingegneria #cybersecurity #firewall #iptables #linux #netfilter

## 1. Le Tabelle di Iptables (Tables)

Iptables organizza le regole in diverse **tabelle**, ognuna dedicata a uno scopo specifico. Ogni tabella contiene delle catene (**built-in chains**) predefinite.

### Tabella Filter

È la tabella di default (**default table**).

- Contiene le seguenti catene:
    
    - **INPUT:** Per pacchetti destinati ai socket locali.
        
    - **FORWARD:** Per pacchetti che vengono instradati attraverso il box (il dispositivo).
        
    - **OUTPUT:** Per pacchetti generati localmente.
        

### Tabella Nat

Utilizzata per il **Network Address Translation**.

- Avviene **prima** del routing.
    
- Facilita la trasformazione dell'indirizzo IP di destinazione per renderlo compatibile con la tabella di routing del firewall.
    
- Utilizzata con il NAT dell'indirizzo IP di destinazione.
    
- Contiene le seguenti catene:
    
    - **PREROUTING:** Per alterare i pacchetti appena entrano (as soon as they come in).
        
    - **OUTPUT:** Per alterare i pacchetti generati localmente prima del routing.
        
    - **POSTROUTING:** Per alterare i pacchetti mentre stanno per uscire (about to go out).
        

### Tabella Mangle

Utilizzata per la modifica dell'header TCP (**TCP header modification**).

- Modifica i bit della "quality of service" del pacchetto TCP prima che avvenga il routing.
    
- Contiene le catene: PREROUTING, OUTPUT, INPUT, FORWARD, POSTROUTING.
    

### Tabella Raw

Utilizzata principalmente per configurare esenzioni dal tracciamento delle connessioni (**exemptions from connection tracking**).

- Contiene le catene:
    
    - **PREROUTING:** Alterazione pacchetti in entrata prima del routing.
        
    - **OUTPUT:** Alterazione pacchetti locali prima del routing.
        

## 2. Flusso dei Pacchetti (Packet Flow)

È fondamentale comprendere l'ordine esatto in cui un pacchetto attraversa le tabelle e le catene.

![[Pasted image 20260108174932.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Il diagramma mostra il percorso di un pacchetto ("Packet In") dalla "Network A" alla "Network B" o verso il processo locale.
> 
> **Meaning:**
> 
> 1. Il pacchetto entra e passa subito per **Mangle PREROUTING** e **Nat PREROUTING**.
>     
> 2. Segue la decisione di routing (**Routing**):
>     
>     - **Se è per il firewall:** Va a Mangle INPUT -> Filter INPUT -> Local Processing.
>         
>     - **Se NON è per il firewall:** Va a Mangle FORWARD -> Filter FORWARD -> Mangle POSTROUTING -> Nat POSTROUTING -> Uscita.
>         
> 3. I pacchetti generati localmente ("Firewall Reply") seguono un percorso diverso: Routing -> Mangle OUTPUT -> Nat OUTPUT -> Filter OUTPUT -> Mangle POSTROUTING -> Nat POSTROUTING.
>     

## 3. Moduli Estesi (Extended Modules)

Iptables può utilizzare moduli di matching estesi (**extended packet matching modules**).

**Modalità di utilizzo:**

1. **Implicitamente:** Quando viene specificato `-p` (protocollo).
    
2. **Esplicitamente:** Con l'opzione `-m` seguita dal nome del modulo (`-m module_name`).
    

Dopo aver caricato un modulo, diventano disponibili varie opzioni extra da riga di comando.

### Modulo State

Permette di filtrare in base allo stato della connessione.

**Here is the exact syntax shown in the slides:**

```
-m state [!] --state st
```

Il "!" è opzionale e significa **NEGAZIONE logica (NOT)**, quindi inverte tutto quello che c'è a destra.
`st` può essere uno dei seguenti stati:

- **INVALID**
    
- **ESTABLISHED**
    
- **NEW**
    
- **RELATED**: Una nuova connessione è "related" se è una nuova connessione ed è relazionata a una connessione già stabilita (es. FTP data channel).
    
In particolare:

#### 1. NEW (Il primo bussare)

- **Significato:** Questo stato identifica il **primo pacchetto** che tenta di creare una nuova connessione.
    
- **Esempio TCP:** È il pacchetto con la flag **SYN** (Synchronize) attiva. Nota che in questo esempio è facile perché [[TCP]] ha letteralmente un flag che dice esplicitamente lo stato della connessione, guarda [[approfondimento firewall stati delle connessioni|qui]] le differenze tra i restanti protocolli.
    
- **A cosa serve:** Serve per dire "Chi può iniziare la conversazione?".
    
    - Se vuoi che il tuo PC possa navigare su internet, devi permettere `NEW` in uscita (OUTPUT).
        
    - Se non vuoi che nessuno si colleghi al tuo PC dall'esterno, blocchi `NEW` in entrata (INPUT).
        

#### 2. ESTABLISHED (La conversazione in corso)

- **Significato:** Questo stato identifica i pacchetti che appartengono a una connessione **già avvenuta** e riconosciuta in entrambe le direzioni.
    
- **Esempio TCP:** Dopo che il primo pacchetto (SYN) è passato e l'altro ha risposto (SYN-ACK), il firewall marca la connessione come `ESTABLISHED`. Da quel momento in poi, non controlla più le regole complesse, ma lascia passare i dati velocemente perché "si fida" della conversazione già approvata.
    
- **Nelle slide:** Viene descritto come il modo per decidere se la connessione è stata originata dall'interno o dall'esterno.
    

#### 3. INVALID (Spazzatura)

- **Significato:** Questo stato identifica i pacchetti che **non appartengono a nessuna connessione** conosciuta e che non sono validi per creare una nuova connessione.
    
- **Esempio:** Un pacchetto che arriva all'improvviso con flag strane, o frammenti di dati orfani che non si riescono a ricostruire.
    
- **Cosa farne:** Solitamente si **scartano (DROP)** sempre, perché spesso sono frutto di errori di rete o tentativi di attacco.
    
#### 4. RELATED (Il "Parente" della connessione)

- **Significato:** Questo stato identifica una connessione che tecnicamente è **nuova** (inizia con un nuovo pacchetto), ma che è logicamente **correlata** a una connessione già esistente e approvata.
    
    - In termini semplici: "Non ti conosco, ma sei amico di qualcuno che conosco, quindi ti faccio entrare".
        
- **Esempio Classico (FTP):**
    
    - Quando usi l'FTP per scaricare un file, crei una connessione di comando (Porta 21) che è `ESTABLISHED`.
        
    - Quando chiedi il file, il server deve aprirne una _seconda_ per inviarti i dati (Porta 20 o random).
        
    - Per il firewall, questa seconda connessione sarebbe `NEW` (e quindi bloccata se hai una policy severa). Ma siccome il firewall "capisce" il protocollo FTP, la marca come `RELATED` alla prima e la lascia passare.
        
- **Esempio Comune (ICMP Errori):**
    
    - Se tu provi a collegarti a un server che non esiste, un router intermedio potrebbe mandarti un errore ICMP ("Destination Unreachable").
        
    - Questo errore è un pacchetto nuovo, ma è `RELATED` al tuo tentativo di connessione originale. Se non accetti `RELATED`, il tuo PC non saprà mai che la connessione è fallita e rimarrà in attesa (timeout).
        
- Come si usa nelle regole:
    
    Nelle tue slide (es. File 16_4.pdf, slide 7), vedi che spesso si accettano insieme:
    
    Bash
    
    ```
    -m state --state ESTABLISHED,RELATED -j ACCEPT
    ```
    
    Questo significa: "Lascia passare tutto ciò che fa parte di una conversazione in corso (`ESTABLISHED`) o che ne è una conseguenza logica (`RELATED`)"2222.

--- 
**Riassunto veloce delle differenze:**

- **NEW:** "Ciao, posso entrare?" (Primo contatto).
    
- **ESTABLISHED:** "Ah sei tu, stiamo già parlando." (Conversazione in corso).
    
- **RELATED:** "Vengo per conto di tizio." (Nuovo, ma invitato).
    
- **INVALID:** "%£$!&" (Incomprensibile/Errore).

### Come usarli nella pratica
#### 1. ESTABLISHED (e solitamente RELATED) $\rightarrow$ "Il Motore"

Questi li metti **praticamente sempre** e spesso come **prima regola** in alto.

- Perché? Perché costituiscono il 99% del traffico di una rete che funziona.
    
- Senza di loro, ogni pacchetto verrebbe ricontrollato da zero o bloccato.
    
- **Consiglio:** Nelle slide e nella pratica, `RELATED` si mette quasi sempre insieme a `ESTABLISHED` (`-m state --state ESTABLISHED,RELATED`). È raro voler accettare le connessioni stabilite ma bloccare gli errori di rete (ICMP) associati ad esse.
    

#### 2. NEW $\rightarrow$ "L'Interruttore"

Questo è l'unico su cui devi **ragionare caso per caso**. È qui che decidi la _policy_ di sicurezza.

- **In INPUT:** Lo metti **solo** se sei un Server (es. "Voglio offrire un sito web? Sì $\rightarrow$ Accetto NEW sulla porta 80"). Se sei un semplice PC client, qui NEW non ci va mai.
    
- **In OUTPUT:** Lo metti **solo** se vuoi navigare o uscire verso l'esterno (es. "Voglio andare su Google? Sì $\rightarrow$ Accetto NEW verso la porta 80/443").
    

#### Riassunto Visivo

- **ESTABLISHED/RELATED:** "Lascia scorrere l'acqua nei tubi già collegati". (Sempre ON).
    
- **NEW:** "Decidi quali rubinetti si possono aprire". (Dipende da te).
    

## 4. Elenco Moduli Estesi

Di seguito l'elenco dei moduli principali e le loro funzioni.

### Gestione Traffico e Indirizzi

- **account:** Contabilizza il traffico per tutti gli host in una definita rete/netmask.
    
- **addrtype:** Match dei pacchetti basato sul tipo di indirizzo (UNSPEC, UNICAST, LOCAL, BROADCAST, ANYCAST, MULTICAST...).
    
- **iprange:** Match su un range arbitrario di indirizzi IPv4.
    
- **mac:** Match dell'indirizzo MAC sorgente.
    
    - Formato: `XX:XX:XX:XX:XX:XX`.
        
    - Valido solo per pacchetti provenienti da un dispositivo Ethernet nelle catene PREROUTING, FORWARD o INPUT.
        
- **owner:** Match delle caratteristiche del creatore del pacchetto.
    
    - Valido solo per pacchetti generati localmente (**OUTPUT chain**).
        
    - Alcuni pacchetti (es. risposte ICMP ping) potrebbero non avere proprietario.
        

### Gestione Connessioni e Limiti

- **connbytes:** Match basato su quanti bytes o pacchetti una connessione ha trasferito finora (o media bytes per pacchetto).
    
- **connlimit:** Permette di restringere il numero di connessioni TCP parallele verso un server per IP client (o blocco di indirizzi).
    
- **connrate:** Match basato sul transfer rate corrente in una connessione.
    
- **conntrack:** Permette l'accesso alle informazioni di connection tracking (più dettagliato del match "state").
    
- **hashlimit:** Permette di esprimere limiti come "1000 pacchetti al secondo per ogni host" con una singola regola iptables.
    
- **quota:** Implementa quote di rete decrementando un contatore di byte a ogni pacchetto.
    

### Protocolli e Caratteristiche

- **icmp:** Permette la specifica del tipo ICMP.
    
- **length:** Match della lunghezza del pacchetto contro un valore specifico o range.
    
- **multiport:** Match di un set di porte sorgente o destinazione.
    
    - Fino a 15 porte specificabili.
        
    - Un range (porta:porta) conta come due porte.
        
    - Usabile solo con `-p tcp` o `-p udp`.
        
- **tcp:** Estensioni caricate se è specificato `--protocol tcp`.
    
- **udp:** Caricato se è specificato `--protocol udp`.
    

### Altri Moduli (Utility e Sicurezza)

- **nth:** Match di ogni 'n'-esimo pacchetto.
    
- **psd:** Tenta di rilevare scansioni di porte TCP e UDP (**port scans**). Derivato da _scanlogd_.
    
- **random:** Match casuale di una certa percentuale di pacchetti.
    
- **time:** Match se l'orario/data di arrivo del pacchetto è entro un certo range.
    
- **ttl:** Match del campo "time to live" nell'header IP.
    

## 5. Flowchart di Processamento Avanzato

Viene presentato un diagramma di flusso dettagliato (derivato da SANS FOR572) che include la tabella **security**.

![[Pasted image 20260108175937.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Il diagramma distingue nettamente tra **Incoming Packet** (Pacchetto in entrata) e **Locally-generated Packet** (Generato localmente).
> 
> **Meaning:**
> 
> - **Incoming:** Raw PREROUTING -> Connection Tracking -> Mangle PREROUTING -> Nat PREROUTING.
>     
> - **Security Table:** Nota che la tabella `security` (INPUT, FORWARD, OUTPUT) è disponibile solo quando si usano le funzionalità di sicurezza **SELinux**.
>     
> - **Priorità:** Le tabelle `raw` vengono elaborate prima del connection tracking.
>     

## 6. Sintassi dei Comandi e Regole

Iptables utilizza una sintassi specifica per comandi, parametri e opzioni.

### Opzioni Iptables

- **COMMANDS:**
    
    - `-A (--append) chain rule-specification`: Aggiunge una regola in coda.
        
    - `-L (--list) [chain]`: Lista le regole.
        
- **PARAMETERS:**
    
    - `[!] -p (--protocol) protocol`
        
    - `[!] -s (--source) address[/mask]`
        
    - `[!] -i (--in-interface) name`
        
- **OTHER:**
    
    - `-n (--numeric)`: Output numerico (IP e porte invece di nomi).
        
    - `-j (--jump) target`: Salta all'azione specificata.
        

### Struttura di una Regola (Session Filter)

Una regola completa segue questo schema logico:

**The mathematical/logical definition provided is:**

```
IPTABLES –t TABLE –A CHAIN –[I|O] IFACE –s x.y.z.w –d a.b.c.d –p PROT –m state --state STATE –j ACTION
```
Dove:

- **PACKET ADDRESS (TABLE):** `nat | filter | ...`
    
- **ORIGIN OF CONNECTION/PACKET:** `INPUT (I) | OUTPUT (O) | FORWARD (F)`
    
- **NETWORK INTERFACE (IFACE):** `eth0 | eth1 | ppp0` (network adapter)
    
- **PROTOCOL (PROT):** `tcp | icmp | udp`
    
- **STATE OF THE CONNECTION (STATE):** `NEW | ESTABLISHED | RELATED ...`
    
- **ACTION ON THE PACKET:** `DROP | ACCEPT | REJECT | DNAT | SNAT ...`
    

---

Se sei arrivato fino a qui, probabilmente come me hai il cervello fritto, sarebbe opportuno fare esercizi e ecco una nota che chiarisce (o che dovrebbe chiarire) un po' le cose: [[Esemplificazione Firewall|Premi Qui]]

---

# Firewall: Esempi Pratici con Iptables

**Tags:** #ingegneria #cybersecurity #firewall #iptables #linux #esempi_pratici

## 1. Configurazione Base e Stati 

In questo scenario, assumiamo che l'interfaccia **eth0** del router sia connessa alla **public Internet**.

### Blocco del Traffico in Ingresso

La prima regola di sicurezza consiste nel bloccare tutto il traffico in entrata non richiesto.

**Here is the exact implementation shown in the slides:**

Bash

```
iptables -A FORWARD -i eth0 -j DROP
```

> [!abstract] Code Analysis
> 
> - **DROP:** I pacchetti vengono scartati senza inviare alcuna risposta al mittente.
>     
> - **Conseguenze:**
>     
>     - Il firewall non protegge da attacchi di tipo **flooding**.
>         
>     - Non fornisce informazioni utili agli attaccanti che eseguono **port scanning** (il firewall appare "invisibile" o "morto").
>         

### Gestione delle Connessioni Stabilite

Per permettere il traffico di ritorno legittimo, si accettano i pacchetti dall'esterno solo se riferiti a una connessione TCP iniziata dall'interno della rete.

**Here is the exact implementation shown in the slides:**

```
iptables -A FORWARD -i eth0 -m state ACCEPT --state ESTABLISHED -j
```

_(Nota: La sintassi standard prevede solitamente `-j ACCEPT` alla fine, ma il blocco sopra riporta fedelmente la frammentazione della slide)_.

> [!important] Concetto Chiave: ESTABLISHED
> 
> Lo stato ESTABLISHED permette al firewall di decidere se la connessione è stata originata dall'interno o dall'esterno. Questa informazione è memorizzata direttamente nelle tabelle di stato di IPTABLES.

---

## 2. Forwarding verso Server Interno (Slide 32)

Example 1:

Configurazione per permettere al firewall di accettare pacchetti TCP per il routing verso un server specifico.

- **Ingresso:** Interfaccia `eth0` (da qualsiasi indirizzo IP).
    
- **Destinazione:** Indirizzo IP `192.168.1.58` (raggiungibile via `eth1`).
    
- **Porte:**
    
    - Porta sorgente: range **1024 a 65535**.
        
    - Porta destinazione: **80** (www/http).
        

**Here is the exact implementation shown in the slides:**

Bash

```
iptables -A FORWARD -s 0/0 -i eth0 -d 192.168.1.58 -o eth1 -p TCP --sport 1024:65535 --dport 80 -j ACCEPT
```

> [!abstract] Code Analysis
> 
> - `-s 0/0`: Accetta traffico da qualsiasi sorgente.
>     
> - `-o eth1`: Specifica l'interfaccia di uscita verso la rete interna.
>     

---

## 3. Gestione ICMP (Ping) (Slide 33)

Example 2:

Regole per permettere al firewall di inviare ping (echo-requests) e ricevere le relative risposte (echo-replies).

**Here is the exact implementation shown in the slides:**

Bash

```
iptables -A OUTPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-reply -j ACCEPT
```

---

## 4. Limitazione del Traffico (Rate Limiting) (Slide 34)

Example 3:

Uso del modulo limit per prevenire abusi.

### Limitazione Ping

Accettare al massimo 1 ping al secondo.

The mathematical definition provided is:

$$1/s$$

**Here is the exact implementation shown in the slides:**

Bash

```
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s -i eth0 -j ACCEPT
```

### Limitazione TCP SYN

Limitare l'accettazione di segmenti TCP con bit **SYN** impostato (nuove connessioni) a non più di cinque al secondo.

The mathematical definition provided is:

$$5/s$$

**Here is the exact implementation shown in the slides:**

Bash

```
iptables -A INPUT -p tcp --syn -m limit --limit 5/s -i eth0 -j ACCEPT
```

---

## 5. Forwarding Avanzato e Multiport (Slide 35)

Example 4:

Estensione dell'esempio 1. Si vuole permettere il traffico verso il server 192.168.1.58 per servizi Web (HTTP) e Sicuri (HTTPS), gestendo anche il traffico di ritorno.

- **Porte destinazione:** 80 e 443.
    
- **Ottimizzazione:** Invece di specificare le porte per il traffico di ritorno, si usa lo stato **ESTABLISHED**.
    

**Here is the exact implementation shown in the slides:**

Bash

```
iptables -A FORWARD -s 0/0 -i eth0 -d 192.168.1.58 -o eth1 -p TCP --sport 1024:65535 -m multiport --dports 80,443 -j ACCEPT

iptables -A FORWARD -d 0/0 -o eth0 -s 192.168.1.58 -i eth1 -p TCP -m state --state ESTABLISHED -j ACCEPT
```

> [!abstract] Code Analysis
> 
> - `-m multiport`: Permette di elencare più porte (80, 443) in una sola regola.
>     
> - `--state ESTABLISHED`: Permette automaticamente tutti i pacchetti di risposta dal server interno verso l'esterno, semplificando la configurazione.
>     

---

## 6. Accesso DNS (Slide 36)

Example 5:

Permettere l'accesso DNS dal firewall e verso il firewall.

- **Protocollo:** UDP.
    
- **Porta:** 53.
    
**Here is the exact implementation shown in the slides:**

```
iptables -A OUTPUT -p udp -o eth0 --dport 53 --sport 1024:65535 -j ACCEPT

iptables -A INPUT -p udp -i eth0 --sport 53 --dport 1024:65535 -j ACCEPT
```

---

## 7. Accesso ai Servizi del Firewall (Slide 37)

Example 6:

Permettere l'accesso SSH e WWW diretto al firewall stesso (non forwarded).

- **Output:** Il firewall può rispondere a connessioni stabilite o correlate.
    
- **Input:** Si accettano nuove connessioni (o stabilite) sulle porte 22 e 80.
    

**Here is the exact implementation shown in the slides:**

```
iptables -A OUTPUT -o eth0 -m state --state ESTABLISHED, RELATED -j ACCEPT

iptables -A INPUT -p tcp -i eth0 --dport 22 --sport 1024:65535 -m state --state NEW, ESTABLISHED -j ACCEPT

iptables -A INPUT -p tcp -i eth0 --dport 80 --sport 1024:65535 -m state --state NEW, ESTABLISHED -j ACCEPT
```

---

## 8. Navigazione dal Firewall (Slide 38)

Example 7:

Permettere a un utente loggato sul firewall di usare un Web browser per navigare in Internet.

- **Traffico in uscita (OUTPUT):** Permesso per connessioni **NEW**, **ESTABLISHED**, **RELATED** verso le porte 80 (HTTP) e 443 (HTTPS).
    
- **Traffico in entrata (INPUT):** Permesso solo per risposte a connessioni già esistenti (**ESTABLISHED**, **RELATED**).
    

**Here is the exact implementation shown in the slides:**

```
iptables -A OUTPUT -j ACCEPT -m state --state NEW,ESTABLISHED,RELATED -o eth0 -p tcp -m multiport --dports 80,443 --sport 1024:65535

iptables -A INPUT -j ACCEPT -m state --state ESTABLISHED, RELATED -i eth0 -p tcp
```

---

## 9. Rete Fidata (Home Network) (Slide 39)

Example 8:

Permettere l'accesso completo a una rete domestica ("Home Network") collegata all'interfaccia eth1.

- **Ipotesi:** Tutto il traffico tra questa rete (`192.168.1.0/24`) e il firewall è considerato fidato (**trusted**) e permesso.
    

**Here is the exact implementation shown in the slides:**

```
iptables -A INPUT -j ACCEPT -p all -s 192.168.1.0/24 -i eth1

iptables -A OUTPUT -j ACCEPT -p all -d 192.168.1.0/24 -o eth1
```

---

## 10. Loopback (Slide 40)

Example 9:

Abilitare il traffico sull'interfaccia di loopback (lo), essenziale per il funzionamento dei processi interni al sistema.

**Here is the exact implementation shown in the slides:**

Bash

```
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
```

---

# Amministrazione Iptables e Architetture Firewall Avanzate

**Tags:** #ingegneria #cybersecurity #firewall #iptables #bastion_host #architettura_di_rete

## 1. Amministrazione di Iptables (Slide 41)

La gestione delle regole in `iptables` presenta caratteristiche specifiche riguardanti l'applicazione e la persistenza.

- **Applicazione Immediata:** Una nuova regola viene applicata immediatamente ("a new rule immediately applies"). Non è necessario riavviare il servizio iptables.
    
- **Volatilità:** I cambiamenti vengono persi al riavvio del sistema (**lost at reboot**).
    

### Persistenza della Configurazione

Per mantenere le regole attive dopo un riavvio, è buona norma inserire la configurazione di iptables nella **boot sequence**.

**Here is the exact implementation shown in the slides:**

Bash

```
iptables-save > iptables.dat
iptables-restore < iptables.dat
```

> [!abstract] Code Analysis
> 
> - `iptables-save`: Esporta le regole correnti in un file (es. `iptables.dat`).
>     
> - `iptables-restore`: Ricarica le regole da un file salvato precedentemente.
>     
> - Questi comandi richiedono privilegi di amministrazione (need sudoer).
>     

---

## 2. Altri Approcci ai Firewall (Slide 42)

Oltre al packet filtering, esistono approcci più sofisticati basati sul livello di operatività.

### Application Level

- Utilizza un'applicazione specifica ("use a specific application").
    
- Ha accesso completo ai protocolli (**fully accesses protocols**).
    
- **Logica:** L'utente richiede un servizio -> la richiesta è accettata/negata secondo regole definite -> le richieste accettate vengono servite.
    
- **Requisito:** Necessita di un **proxy server** per ogni servizio!
    

### Circuit Level

- Stabilisce due connessioni TCP.
    
- La sicurezza è applicata limitando le connessioni autorizzate (**limiting the authorized connections**).
    

---

## 3. Circuit-Level Gateway (Slide 43)
[[Circuit-Level Gateway]]

Questo tipo di firewall opera creando un circuito virtuale tra la rete interna ed esterna.

![[Pasted image 20260110203722.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo schema mostra un "[[Gateway]]" che interpone due connessioni separate: "Outside connection" (tra host esterno e gateway) e "Inside connection" (tra gateway e host interno). All'interno del gateway ci sono moduli "Out" e "In" collegati tra loro.
> 
> **Meaning:** Il gateway unisce ("splices") e rilancia ("relays") due connessioni TCP distinte, agendo come intermediario trasparente.

### Caratteristiche Tecniche

- **Controllo:** Non esamina il contenuto dei segmenti TCP ("Does not examine the contents"). Ha meno controllo rispetto a un gateway di livello applicativo.
    
- **Validazione:** Controlla la validità delle connessioni TCP rispetto a una tabella di connessioni permesse prima di aprire una sessione.
    
- **Criteri:** Una sessione valida si basa su:
    
    - Indirizzi dest/src e porte.
        
    - Ora del giorno.
        
    - Protocollo.
        
    - Utente e password.
        
- **Efficienza:** Una volta che la sessione è permessa, non vengono effettuati ulteriori controlli ("no further checks").
    

> [!important] Adattamento Client
> 
> Le applicazioni client devono essere adattate per SOCKETS (es. SOCKS), che funge da interfaccia "Universale" per i circuit-level gateways.

---

## 4. Application-Level Gateway (Slide 44)
[[Application-Level Gateway]]

Conosciuto anche come Proxy, opera a livello applicativo esaminando il contenuto del traffico.

![[Pasted image 20260110204005.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Il Gateway contiene uno stack specifico per ogni protocollo: TELNET, FTP, SMTP, HTTP. Le connessioni esterna e interna si interrompono e vengono rigenerate a livello di questi moduli.
> 
> **Meaning:** Il firewall capisce il linguaggio dell'applicazione (es. comandi FTP o header HTTP) e agisce come intermediario intelligente.

### Funzionalità Principali

- Unisce e rilancia connessioni specifiche dell'applicazione ("Splices and relays application-specific connections").
    
- _Esempio:_ **Web browser proxy**.
    
- **Overhead:** Elevato consumo di risorse ("Big overhead"), ma permette di loggare e auditare tutte le attività.
    
- **Autenticazione:** Supporta l'autenticazione utente-gateway (username e password).
    
- **Filtraggio:** Può utilizzare regole di filtraggio granulari.
    
- **Limitazione:** Necessita di un proxy separato per ogni applicazione.
    

---

## 5. Comparazione delle Tecnologie (Slide 45)

Di seguito la tabella comparativa tra le diverse tipologie di firewall.

|**Tipo Firewall**|**Performance**|**Modify client application**|**Defends against attacks**|
|---|---|---|---|
|**Packet filter**|**Best**|No|**Worst**|
|**Session filter**||No||
|**Circuit-level gateway**||Yes (SOCKS)||
|**Application-level gateway**|**Worst**|No|**Best**|

---

## 6. Operazioni Aggiuntive e Scenari (Slide 46-47)

### Funzioni Extra

Oltre al controllo del traffico in/out, i firewall possono:

- Controllare l'uso della banda ("control band use").
    
- Nascondere le informazioni sulla rete interna.
    

### Scenario: "Fun with Outbound"

Un esempio tratto da _"The Art of Intrusion"_ mostra come i firewall personali possano essere aggirati se mal configurati:

1. **Guess:** Indovinare la password del CEO.
    
2. **Try:** Provare a scaricare tool di hacking via FTP -> Bloccato dal Personal Firewall.
    
3. **Use:** Usare l'oggetto **Internet Explorer** -> La maggior parte dei firewall permette a IE di connettersi a Internet.
    
4. **Get:** Ottenere l'accesso ("Get crackin'...").
    

---

## 7. Posizionamento e Sicurezza del Perimetro (Slide 48)

Dove posizionare il firewall è cruciale per definire il **Security Perimeter**.

![[Pasted image 20260110205349.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Un Router con Packet-filtering posto tra Internet e la Private Network.
> 
> **Meaning:** Questo è il primo livello di difesa. Tuttavia, nasce un problema strutturale.

### Il Problema dell'Accessibilità

- **Esigenza:** I server della rete protetta devono essere accessibili dall'esterno.
    
- **Soluzione Standard:** Permettere il traffico per applicazioni specifiche (es. aprire porta 25 per SMTP, 80 per HTTP).
    
- **Rischio (BUT):** Le applicazioni software possono avere bug sfruttabili. Un attaccante può prendere il controllo dei server bypassando il firewall se sfrutta una vulnerabilità dell'applicazione permessa.
    

---

## 8. Bastion Host (Slide 49-50)
[[Bastion Host]]

Per mitigare i rischi sopra descritti, si introduce il concetto di **Bastion Host**.

### Definizione e Ruolo

Il Bastion host è un sistema "indurito" (**hardened system**) che implementa un **application-level gateway** posizionato dietro un packet filter.

- Tutto il traffico fluisce attraverso il bastion host ("All traffic flows through bastion host").
    
- Il Packet router permette:
    
    - Ai pacchetti esterni di entrare **solo** se destinati al bastion host.
        
    - Ai pacchetti interni di uscire **solo** se originati dal bastion host.
        

### Caratteristiche di Sicurezza (Hardening)

Il Bastion Host è un host unico raggiungibile da Internet, quindi deve essere **massivamente protetto**:

1. **Trustable Operating Systems:** Esegue poche applicazioni e tutti i servizi non essenziali sono spenti.
    
2. **Application-specific proxies:**
    
    - Supportano solo un sottoinsieme di comandi dell'applicazione.
        
    - Traffico loggato e auditato.
        
    - Accesso al disco limitato.
        
    - Esecuzione come utente non privilegiato in directory separate.
        
3. **Secure Operating System (Trusted/Hardened):**
    
    - Nessun software non necessario (no compilatori o interpreti).
        
    - Ambiente isolato (**chrooting**).
        
    - File system in sola lettura (**read-only file system**).
        
4. **Controlli di Integrità:**
    
    - Process checker.
        
    - Integrity file system checker.
        
5. **Configurazione Minimale:**
    
    - Piccolo numero di servizi e nessun account utente (**no user accounts**).
        
    - Servizi non fidati rimossi.
        
    - **Source-routing disabled**.
        

---

# Architetture Firewall e DMZ

**Tags:** #ingegneria #cybersecurity #firewall #DMZ #network_architecture #bastion_host

## 1. DeMilitarized Zone (DMZ)

La **DeMilitarized Zone (DMZ)** è un'area speciale progettata per ospitare i server che devono essere raggiungibili dall'esterno.

- **Accessibilità dei Server:** I server che devono essere accessibili dall'esterno ("Servers that should be reachable from the outside") sono posizionati in questa area.
    
- **Controllo degli Accessi:**
    
    - Le connessioni esterne/utenti possono raggiungere questi server.
        
    - Non possono raggiungere la rete interna (**internal network**) perché è bloccata dal **Bastion host**.
        
    - Le connessioni esterne che non accedono a questi server specifici vengono scartate (**dropped**).
        
- **Struttura:** Possono esistere diversi livelli (**several levels**) di DMZ.
    

> [!important] Nota di Sicurezza
> 
> È necessario dedicare grande attenzione al traffico che entra nella DMZ: se un hacker controlla il bastion host, può entrare nella LAN interna.

## 2. Configurazioni del Bastion Host

Esistono diverse architetture per posizionare il firewall e proteggere la rete.

### Single-Homed Bastion Host

In questa configurazione, il **Bastion host** è posizionato sulla rete interna, protetto da un **Packet-filtering router**.

![[Pasted image 20260110210134.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:**
> 
> - Un **Packet-filtering router** collega Internet alla rete interna.
>     
> - Sulla rete interna si trovano il **Bastion host**, l'**Information server** e gli host della rete privata (**Private network hosts**).
>     
> 
> **Meaning:**
> 
> - Il filtraggio è demandato principalmente al router.
>     
> - **Rischio critico:** Se il packet filter viene compromesso, il traffico può fluire verso la rete interna ("If packet filter is compromised, traffic can flow to internal network").
>     

### Dual-Homed Bastion Host

Questa configurazione prevede un Bastion host con due interfacce di rete, posizionato fisicamente tra la rete esterna e quella interna.

![[Pasted image 20260110210150.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:**
> 
> - Il **Bastion host** si trova tra il router e la rete privata.
>     
> - Il traffico passa fisicamente attraverso il Bastion host per raggiungere la rete privata.
>     
> 
> **Meaning:**
> 
> - Non esiste connessione fisica tra la rete interna ed esterna (**No physical connection between internal and external networks**).
>     
> - Il Bastion host agisce come un punto di blocco fisico e logico.
>     

### Screened Subnet

Questa è l'architettura che implementa una vera [[DMZ]] isolata tramite due router.

![[Pasted image 20260110210159.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:**
> 
> - Due router: **Outside router** (verso Internet) e **Inside router** (verso la rete privata).
>     
> - Tra i due router c'è una sottorete schermata (**Screened Subnet**) che contiene il **Bastion host**, l'**Information server** e il Modem.
>     
> 
> **Meaning:**
> 
> - Solo la **screened subnet** è visibile alla rete esterna.
>     
> - La rete interna è invisibile (**internal network is invisible**).
>     

### Dual-Homed Bastion Host vs Screened Subnet
#### considering a DMZ like that, isn't actually better to, also, be sure that there is only una link to router1-bastion and another link to bastion-router2? (nell'atto pratico è identico al Dual-Homed [[Bastion Host]])

Hai avuto un'intuizione di sicurezza molto acuta. La risposta breve è: **Sì, sarebbe più sicuro, ma molto meno efficiente e scalabile.**

Quello che tu proponi (un collegamento fisico unico `Router1 -> Bastion -> Router2`) trasforma il Bastion Host in un collo di bottiglia fisico.

Analizziamo perché l'architettura nell'immagine (**Screened Subnet**) è spesso preferita rispetto alla tua idea (che somiglia più a un **Dual-Homed Gateway** in serie), e come bilanciare i due aspetti.

### 1. La tua idea: Il "Collo di Bottiglia" Sicuro

Se costringi fisicamente tutto il traffico a passare _dentro_ il Bastion Host (un cavo entra, uno esce verso il Router 2), ottieni:

- **Vantaggio (Sicurezza Assoluta):** Nessun pacchetto può raggiungere il Router interno (Inside router) senza essere processato dal Bastion. È impossibile "aggirarlo".
    
- **Svantaggio 1 (Performance):** Il Bastion Host (che è un server, non un router hardware) deve analizzare e instradare _tutto_ il traffico. Se la rete interna deve scaricare un backup da 100GB, il Bastion si satura e si blocca, interrompendo anche i servizi critici (es. Web Server).
    
- **Svantaggio 2 (Single Point of Failure):** Se il Bastion Host va in crash per un aggiornamento o un errore software, **tutta** l'azienda è isolata da Internet. I router funzionano, ma il "ponte" è crollato.
    

### 2. L'immagine: La "Screened Subnet" (DMZ)

Nell'immagine, i dispositivi (Bastion, Info Server, Modem) sono collegati a uno switch comune tra i due router.

- **Vantaggio (Scalabilità):** Puoi aggiungere 10 server nella DMZ (Web, Mail, DNS) senza dover aggiungere 10 schede di rete al Router.
    
- **Vantaggio (Resilienza):** Se il Bastion Host (usato magari solo come Proxy Web) si rompe, il server di Posta (Information Server) continua a funzionare perché ha il suo percorso verso i router.
    
- **Vantaggio (Velocità):** I Router fanno i Router (veloci), i Server fanno i Server. Non chiedi a un Server di fare il lavoro pesante di routing per tutta l'azienda.
    

### 3. Come ottenere la sicurezza che chiedi tu nell'architettura dell'immagine?

La tua preoccupazione è: _"Se sono tutti collegati insieme, un hacker non può saltare dal Router Esterno direttamente al Router Interno bypassando il Bastion?"_

La risposta sta nelle **Regole (ACL)** del **Router Interno (Inside router)**.

Per replicare la sicurezza della tua idea senza i problemi di performance, si configura l'Inside Router così:

1. **DROP ALL:** Di default, scarta tutto ciò che arriva dalla DMZ.
    
2. **ACCEPT ONLY FROM BASTION:** Accetta connessioni _solo_ se l'IP sorgente è quello del Bastion Host (e solo sulle porte necessarie, es. Proxy o SSH).
    

In questo modo ottieni una **costrizione logica** invece che fisica:

- Fisicamente i cavi permetterebbero il passaggio diretto.
    
- Logicamente, il Router Interno dice: _"Non mi interessa se sei nella DMZ, io parlo solo con il Bastion Host"_.
    

### In Sintesi

La tua idea crea un Dual-Homed Gateway (massima sicurezza, basse prestazioni, alto rischio guasto).

L'immagine mostra una Screened Subnet (ottimo bilanciamento, sicurezza gestita dalle regole dei router, alta scalabilità).

Nelle aziende reali si usa quasi sempre l'approccio dell'immagine.

## 3. Protezione degli Indirizzi e Instradamento

Il firewall deve anche gestire la visibilità della rete interna per prevenire attacchi.

- **Nascondere gli Indirizzi IP:**
    
    - Nascondere gli indirizzi IP degli host sulla rete interna (**Hide IP addresses**).
        
    - Solo i servizi destinati ad essere acceduti dall'esterno devono rivelare i loro indirizzi IP.
        
    - Mantenere gli altri indirizzi segreti serve a rendere più difficile lo **spoofing**.
        
- **NAT (Network Address Translation):**
    
    - Utilizzare il NAT per mappare gli indirizzi negli header dei pacchetti verso indirizzi interni.
        
    - Mappatura **1-to-1** o **N-to-1**.
        
- **Filtraggio degli Annunci di Route:**
    
    - Filtrare gli annunci di instradamento (**Filter route announcements**).
        
    - Non c'è bisogno di pubblicizzare le rotte verso gli host interni.
        
    - Obiettivo: Prevenire che un attaccante pubblicizzi che la rotta più breve per un host interno passa attraverso di lui.
        

## 4. Problemi Generali con i Firewall

I firewall non sono una soluzione perfetta e presentano limitazioni intrinseche.

- **Interferenza:** Interferiscono con le applicazioni di rete (**networked applications**).
    
- **Problemi non risolti:** Non risolvono i "problemi reali" come:
    
    - **Buggy software** (es. exploit di buffer overflow).
        
    - **Bad protocol design** (es. WEP in 802.11b).
        
- **Limiti di protezione:**
    
    - Generalmente non prevengono attacchi **Denial of Service** (DoS).
        
    - Hanno una prevenzione limitata contro gli attacchi interni (**insider attacks**).
        
- **Gestione:** Aumentano la complessità e il potenziale di errata configurazione (**misconfiguration**).

---
domande esame [[domande esame firewall|qui]]