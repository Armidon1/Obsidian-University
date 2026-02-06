Basandosi sulle slide "6 - DNS Security.pdf", gli **Open Resolvers** sono **server DNS ricorsivi** che sono accessibili pubblicamente su Internet e configurati per accettare e risolvere query DNS provenienti da **qualsiasi indirizzo IP**, senza restrizioni di accesso.

Nelle fonti fornite, vengono evidenziati principalmente come una vulnerabilità infrastrutturale critica utilizzata per facilitare due tipi di attacchi:

### 1. Il Ruolo nel DDoS Amplification

Gli Open Resolvers sono il "motore" che permette l'amplificazione del traffico negli attacchi Denial of Service.

- **Meccanismo:** Come mostrato nello schema dell'attacco, l'attaccante (o una botnet) invia una richiesta DNS falsificata (spoofed) a questi server.
- **L'Effetto:** Poiché il resolver è "aperto", elabora la richiesta anche se proviene da un IP esterno non autorizzato e invia la risposta (spesso molto voluminosa) all'indirizzo IP della vittima, saturandone la banda.

### 2. Il Ruolo nel Cache Poisoning

Le slide indicano esplicitamente che la presenza di "Open resolvers reachable on the Internet" è una delle condizioni che **rendono più facile** l'attacco di DNS Cache Poisoning (avvelenamento della cache).

- Essendo esposti a chiunque, permettono a un attaccante remoto di inviare query per innescare il processo di risoluzione e tentare contestualmente di iniettare risposte false prima che arrivi quella legittima.

In sintesi, un Open Resolver è un server mal configurato (o intenzionalmente pubblico) che agisce come un amplificatore involontario per attacchi di rete e rappresenta un bersaglio facile per la compromissione dei dati DNS.