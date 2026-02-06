Basandosi sulle nuove fonti fornite (in particolare le slide sulla sicurezza DNS) e collegandosi alla nostra discussione precedente sugli attacchi DDoS, ecco una spiegazione di cosa sono le **botnet** e come vengono utilizzate nel contesto della sicurezza di rete.

### Che cos'è una Botnet

Dalle fonti emerge che una botnet è un'infrastruttura criminale costituita da un vasto numero di **host compromessi** (spesso chiamati "bot") controllati da un attaccante. Questi computer infetti, che possono essere centinaia o migliaia per un singolo dominio malevolo, agiscono all'unisono per eseguire comandi impartiti da un server centrale (Command-and-Control o C2).

Nelle slide, le botnet ricoprono due ruoli principali: quello di **arma offensiva** (per i DDoS) e quello di **scudo difensivo** (per nascondere l'infrastruttura dell'attaccante).

### 1. La Botnet come Arma: DDoS Amplification

Come abbiamo visto nella discussione precedente sul **DDoS Amplification**, la botnet è il "motore" fisico dell'attacco.

- **Il Ruolo:** Nello schema della **Slide 7**, la "Attacker controlled Botnet" è l'entità che invia fisicamente le migliaia di "Small spoofed DNS Request" verso i server Open Resolver.
- **L'Efficacia:** L'attaccante non deve usare la propria connessione internet; sfrutta la banda aggregata di migliaia di dispositivi infetti per inondare i resolver, i quali poi amplificano il traffico verso la vittima (come discusso nel fattore di amplificazione 50x-70x).

### 2. La Botnet come Scudo: DNS Fast-Fluxing

Le nuove fonti introducono un concetto avanzato chiamato **DNS Fast-Fluxing**, dove le botnet vengono usate per nascondere e proteggere i server dell'attaccante (es. server di phishing o C2) da tentativi di blocco o takedown.

In questo scenario, i bot agiscono come **reverse proxies**. Ecco come funziona:

1. **IP Rotanti:** L'attaccante associa un dominio malevolo (es. `malicious.com`) agli indirizzi IP dei computer compromessi (i bot) invece che al vero server.
2. **Proxy:** Quando una vittima (o la polizia) prova a connettersi a `malicious.com`, si connette in realtà a un bot ignaro. Il bot inoltra il traffico al server reale dell'attaccante, che rimane nascosto.
3. **Resilienza:** Grazie al DNS, l'attaccante cambia rapidissimamente (ogni pochi secondi o minuti) gli indirizzi IP associati al dominio, attingendo dal vasto bacino della botnet. Se un IP viene bloccato, il DNS ne fornisce subito un altro diverso.

### Sintesi

In questo contesto, le botnet non sono solo "computer virusati", ma una risorsa strategica che permette agli attaccanti di:

1. Saturare le vittime senza esporre il proprio IP (tramite IP Spoofing e DDoS).
2. Rendere le proprie infrastrutture "mobili" e difficili da abbattere (tramite Fast-Fluxing e proxying),.