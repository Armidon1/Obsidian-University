# FTP Bounce Attack

L'FTP bounce attack è una tecnica classica ma incredibilmente affascinante, perché sfrutta un comportamento che in origine non era considerato un bug, ma una vera e propria _feature_ del protocollo documentata nella RFC 959.

Ecco come funziona nel dettaglio la meccanica di questo attacco.

### Il meccanismo base e il comando abusato

Il cuore dell'attacco risiede nell'abuso del comando **`PORT`** durante una sessione FTP in **modalità attiva** (Active Mode).

In una normale connessione FTP attiva, il client si connette al server sulla porta 21 (canale di controllo). Quando il client ha bisogno di ricevere dati (es. l'output di un `LIST` o il download di un file), invia il comando `PORT` seguito dal proprio indirizzo IP e da una porta in ascolto. Il server FTP, a quel punto, apre proattivamente una nuova connessione verso quell'IP e quella porta (canale dati) per trasmettere le informazioni.

**L'abuso:** La debolezza intrinseca del protocollo originale è che il server FTP **non verifica** se l'IP fornito nel comando `PORT` appartenga effettivamente al client che ha stabilito la connessione di controllo. Un attaccante può quindi inviare un comando `PORT` specificando l'indirizzo IP e la porta di una **terza macchina** (il bersaglio finale).

### La dinamica: cosa permette di fare

Se l'attaccante invia il comando `PORT <IP_Bersaglio>,<Porta_Bersaglio>` e poi richiede al server FTP di inviare un file o leggere una directory, accade questo:

1. È il **server FTP** (il "bouncer") ad aprire la connessione verso il bersaglio finale, non la macchina dell'attaccante.
    
2. L'attaccante può usare questo trucco per fare un **port scanning invisibile**: se il comando FTP va a buon fine (o restituisce un errore specifico di timeout), l'attaccante deduce che la porta sul bersaglio finale è aperta. Nmap implementa questa esatta tecnica con lo switch `-b`.
    
3. Se l'attaccante ha caricato un file malevolo sul server FTP, può usare il comando `PORT` per dire al server di "inviare" quel file direttamente a un servizio in ascolto sulla macchina bersaglio.
    

### Contro quale difesa è utile?

Questo attacco brilla quando l'attaccante si scontra con **Firewall rigidi e regole di Network Segmentation**.

Immagina questa topologia:

- La tua macchina (Attaccante) è su Internet.
    
- Il server FTP è in una DMZ accessibile dall'esterno.
    
- Il bersaglio finale è un server database nella rete LAN interna.
    

Il firewall bloccherà qualsiasi tentativo diretto della tua macchina di scansionare o connettersi al database interno. Tuttavia, il firewall potrebbe essere configurato per permettere al server FTP (che magari fa da ponte per dei backup) di comunicare con la rete LAN. Usando l'FTP bounce attack, tu "rimbalzi" la tua scansione o il tuo payload sul server FTP: per il firewall, la connessione in entrata verso il database sembrerà arrivare dal fidato server FTP, aggirando completamente i filtri perimetrali.

### Contromisure

Oggi questo attacco è raro perché i software e le configurazioni moderne sono stati corretti, ma per mitigarlo completamente si interviene su tre livelli:

- **Validazione dell'IP (Software-level):** Tutti i moderni demoni FTP (come `vsftpd` o `ProFTPD`) sono configurati di default per rifiutare comandi `PORT` che specificano un indirizzo IP diverso da quello del client che ha originato la connessione di controllo. In `vsftpd`, ad esempio, c'è un'apposita direttiva `port_promiscuous=NO` che blocca questo comportamento.
    
- **Disabilitare la modalità attiva:** Passare esclusivamente all'FTP in modalità passiva (`PASV`). In questa modalità è il client a dover aprire la connessione dati verso il server, rendendo impossibile per l'attaccante forzare il server a contattare terze parti.
    
- **Regole Firewall stringenti in Egress:** Un server FTP non dovrebbe avere il permesso di iniziare connessioni arbitrarie verso l'interno della rete o verso porte non standard. Le regole in uscita (egress filtering) dalla DMZ dovrebbero essere "deny by default".