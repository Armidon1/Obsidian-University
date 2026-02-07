# Denial of Service Attacks

**Tags:** #ingegneria #cyber_security #DoS #DDoS #sicurezza_informatica

## 1. Introduzione e Definizione (Slide 1-2)

Il corso inizia definendo il concetto fondamentale di **Denial of Service (DoS)**.

- **Definizione:** Un attacco DoS è qualsiasi attacco che **riduce o elimina la disponibilità** (availability) di un servizio.
    
- **Obiettivo:** Rendere il servizio o i dati **non disponibili** per gli utenti autorizzati.
    

> [!abstract] Esempio Reale
> 
> Viene citato il caso di una compagnia aerea colpita da 2 attacchi DDoS in 8 mesi, con conseguente impatto sulle vendite dei biglietti.

---

## 2. Il DoS nel contesto della CIA Triad (Slide 3)

La **Disponibilità** (Availability) è uno dei componenti fondamentali della triade CIA (Confidentiality, Integrity, Availability).

![[Pasted image 20260207175537.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Il triangolo della sicurezza (CIA Triad) che mostra Confidentiality, Integrity e Availability.
> 
> **Meaning:** Il DoS colpisce specificamente il vertice dell'**Availability**.

### Conseguenze e Severità

L'interruzione della disponibilità comporta conseguenze immediate:

- **Economiche.**
    
- **Operative** (es. fermo produzione).
    

L'impatto può avere diversi gradi di severità:

1. **Indisponibilità completa** (Complete unavailability).
    
2. **Degrado severo delle prestazioni** (Severe Performance degradation).
    
3. **Violazioni degli SLA** (Service Level Agreement).
    

---

## 3. Evoluzione Storica degli Attacchi DoS (Slide 4)

L'evoluzione degli attacchi è stata progressiva dagli anni '90 ad oggi:

- **1990s:** Attacchi basati su bug o limitazioni di protocollo semplici.
    
    - _Esempi:_ SYN flood, Ping of Death.
        
- **2000s:** Introduzione della distribuzione e riflessione.
    
    - _Esempi:_ Botnets, reflection attacks.
        
- **2010s:** Spostamento verso il livello applicativo.
    
    - _Esempi:_ Application-layer attacks.
        
- **2020s:** Sfruttamento massivo dell'IoT.
    
    - _Esempi:_ IoT botnets e abuso di protocolli (protocol abuse).
        

---

## 4. Threat Model per attacchi DoS (Slide 5)

Per comprendere un attacco DoS, analizziamo il modello di minaccia (Threat Model) basato su quattro pilastri:

### Attacker Goals (Obiettivi)

- **Disruption** (Interruzione).
    
- **Extortion** (Estorsione).
    
- **Distraction** (Distrazione da altre attività malevole).
    

### Attacker Capabilities (Capacità)

- **Bandwidth** (Larghezza di banda disponibile).
    
- **Bots** (Numero di dispositivi compromessi).
    
- **Exploits & tech skills** (Competenze tecniche).
    

### Victim Assets (Risorse della vittima)

- **Ingress bandwidth** (Banda in ingresso).
    
- **CPU/memory resources** (Risorse computazionali).
    
- **Stateful components** (Componenti che mantengono lo stato).
    

### Network Assumptions (Assunzioni di rete)

- Lo **Spoofing** è fattibile?
    
- Gli **Amplifiers** (amplificatori) sono apertamente disponibili?
    

---

## 5. Motivazioni dell'Attaccante (Slide 6-7)

Le motivazioni dietro un attacco DoS sono varie e spesso complesse:

### 1. Estorsione Finanziaria (Financial extortion)

- Gruppi criminali inviano note di riscatto minacciando attacchi massicci se non viene pagato un compenso (spesso in criptovalute).
    
- _Esempio:_ **DD4BC** (2014-2016). Il gruppo "DDoS-for-Bitcoin" lanciava flood dimostrativi per poi chiedere riscatti in BTC.
    

### 2. Attivismo Politico/Ideologico (Hacktivism)

- Attacchi condotti sotto bandiere ideologiche.
    
- _Esempio:_ **Operation Payback** (Dic 2010). Sotto il banner di **Anonymous**, gli hacktivisti hanno colpito Mastercard, Visa e PayPal dopo che queste avevano bloccato le donazioni a WikiLeaks.
    

### 3. Sabotaggio Competitivo (Competitive sabotage)

- Ritorsioni motivate commercialmente per proteggere interessi di business (spesso legati a hosting spam-tolerant).
    
- _Esempio:_ **Spamhaus vs. CyberBunker** (Mar 2013). Attacco massiccio contro Spamhaus dopo aver inserito in blacklist gli intervalli IP di CyberBunker.
    

### 4. Contesti Militari e Cyberwarfare

- Utilizzo del DoS come arma in conflitti geopolitici.
    
- _Esempio:_ **Ucraina** (Feb 2022). Ondate coordinate di DDoS hanno colpito portali governativi (MoD, Forze Armate) e banche (PrivatBank, Oschadbank) prima dell'invasione.
    

---

## 6. DoS Attack Surface: Network Stack (Slide 8)

La superficie di attacco viene analizzata in base ai livelli dello stack di rete (modello OSI).

![[Pasted image 20260207175255.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** La piramide dei livelli OSI (Physical -> Application) associata ai tipi di attacco.
> 
> **Meaning:** Ogni livello presenta vulnerabilità specifiche sfruttate dai DoS.

- **L3 (Network Layer):**
    
    - Obiettivo: Saturare la banda tra client e servizio (o upstream).
        
    - _Esempio:_ **UDP reflection/amplification**.
        
- **L4 (Transport Layer):**
    
    - Obiettivo: Esaurire lo "stato" su server o middlebox (firewall/NAT).
        
    - Si colpiscono: SYN backlogs, tabelle di connessione, limiti per-flow.
        
    - _Esempio:_ **TCP SYN floods**.
        
- **L7 (Application Layer):**
    
    - Obiettivo: Forzare il server a eseguire lavoro costoso.
        
    - _Esempio:_ **HTTP GET/POST floods** su percorsi non cachabili.
        

---

## 7. DoS Attack Surface: Logica e Infrastruttura (Slide 9)

Oltre allo stack di rete, la superficie di attacco si estende alla logica applicativa e alle dipendenze.

### Application Logic

Le scelte di design possono espandere o ridurre la superficie di attacco:

- Quali endpoint sono intrinsecamente costosi?
    
- Quali funzionalità fanno "fan-out" su database o API di terze parti?
    
- Quali input possono innescare una complessità _worst-case_?
    

### Shared Infrastructure

L'infrastruttura condivisa può essere usata per reflection/amplification.

- _Esempio:_ **DNS**, **Anycast/CDN**.
    

### Third-party Dependencies

Infrastrutture gestite da terze parti ma critiche per il servizio.

- _Esempio:_ Sistemi esterni di **Identity Management**.
    

---

## 8. Single-source DoS vs Distributed DoS (Slide 10)

È fondamentale distinguere tra attacchi centralizzati e distribuiti.

![[Pasted image 20260207175310.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:**
> 
> 1. **Sinistra (Single-source):** Un solo attaccante invia traffico direttamente al target.
>     
> 2. **Destra (Distributed DoS):** Un attaccante controlla una rete di "Bot/Reflector" che convergono il traffico sul target.
>     
> 
> **Meaning:** Il DDoS permette l'amplificazione della potenza di attacco e complica l'attribuzione e la mitigazione.

- **Single-source DoS:** Attacco diretto uno-a-uno.
    
- **Distributed DoS (DDoS):** Molteplici sorgenti (Botnet).
    
    - **Vantaggi per l'attaccante:** Amplificazione della potenza.
        
    - **Problemi per la difesa:** Difficoltà nell'attribuzione e nella mitigazione.
        

---

## 9. Caso Studio: MIRAI (Slide 11-12)

Il 2016 ha segnato un punto di svolta con **Mirai**, la prima botnet basata su IoT.

### L'Attacco a Brian Krebs

- **Data:** Settembre 2016.
    
- **Target:** Il sito del giornalista di security Brian Krebs.
    
- **Dimensione:** 665 Gbps (Il più grande mai visto all'epoca).
    

### Il Rilascio del Codice

Il codice sorgente è stato rilasciato gratuitamente da un utente noto come **"Anna-senpai"**.

- **Motivazione:** L'autore ha rilasciato il codice perché, dopo l'attacco a Krebs, c'era troppa attenzione sull'IoT ("lots of eyes looking at IoT now").
    
- **Impatto:** Ha democratizzato la creazione di botnet IoT, permettendo a chiunque ("skid and their mama") di avere strumenti potenti.
    

---

## 10. Evoluzione Moderna: AISURU (Slide 13)

**Aisuru** rappresenta l'evoluzione moderna (2025) delle botnet derivate da Mirai.

- **Natura:** Botnet derivata da Mirai (**TurboMIRAI**).
    
- **Modello di Business:** Opera come servizio **DDoS-for-hire**.
    
- **Target di reclutamento:** Dispositivi consumer CPE (router domestici, CCTV, DVR).
    
- **Metodo di attacco:** Flood "direct-path" usando pacchetti di medie dimensioni e porte/flag randomizzati.
    

### Record 2025

- **Q3 2025:** Cloudflare ha documentato un "carpet-bombing" UDP.
    
- **Potenza:** **29.7 Tbps**.
    
- **Durata:** ~69 secondi.
    
- **Sorgenti:** >500k indirizzi unici.
    

### Vettore di Infezione

- Sfruttamento della **supply chain** (es. server di aggiornamento firmware TotoLink).
    
- Scanning continuo per nuove vulnerabilità RCE (Remote Code Execution).

# Classificazione e Attacchi Volumetrici

**Tags:** #ingegneria #cyber_security #DoS #DDoS #volumetric_attacks

## 1. Classificazione degli Attacchi DoS (Slide 1)

Gli attacchi Denial of Service sono solitamente categorizzati in quattro tipologie principali:

- **Volumetric attacks** (Attacchi volumetrici).
    
- **Protocol attacks** (Attacchi al protocollo).
    
- **Application-layer attacks** (Attacchi a livello applicativo).
    
- **Algorithmic complexity attacks** (Attacchi alla complessità algoritmica).
    

---

## 2. Attacchi Volumetrici (Slide 2)

Gli attacchi DDoS volumetrici hanno l'obiettivo di **saturare la larghezza di banda** (bandwidth) e soffocare il percorso di rete verso il servizio.

### Caratteristiche Principali

- Rimangono la categoria di DDoS più comune.
    
- Sfruttano **botnet** noleggiabili a basso costo per generare inondazioni massicce (floods).
    
- Sono misurati in **Gbps** (Gigabit per secondo) o **Tbps** (Terabit per secondo).
    

### Evoluzione e Sintomi

- Le dimensioni degli attacchi sono cresciute esponenzialmente.
    
- Eventi recenti "iper-volumetrici" superano regolarmente 1 Tbps.
    
- **Record 2025:** Picco di **29.7 Tbps** (botnet Aisuru).
    
- **Sintomi tipici:**
    
    - High utilization (Alta utilizzazione).
        
    - Drops (Perdita di pacchetti).
        
    - Latency (Latenza).
        

---

## 3. UDP Floods (Slide 3)

Questo è un DDoS a livello di rete (Network-layer) in cui l'attaccante colpisce un target (host o firewall) con un numero enorme di pacchetti **UDP**.

### Meccanismo

- I pacchetti vengono inviati verso porte **random** o specifiche.
    
- Poiché UDP è **connectionless** (senza connessione), il target deve lavorare per verificare se c'è un'applicazione in ascolto.
    
- Se nessuna applicazione è presente, il target emette un pacchetto **ICMP 'Destination Unreachable'**.
    

### Dettagli Tecnici

- UDP è **stateless** $\rightarrow$ Semplicità nella generazione dei pacchetti.
    
- Gli attaccanti comunemente effettuano **spoofing** degli indirizzi IP sorgente per rimanere anonimi.
    

### Varianti

- **UDP fragmentation floods**.
    
- **Carpet-bombing:** Spruzzare (spray) UDP verso numerose porte su vari range per evadere filtri semplici.
    

---

## 4. ICMP Floods (Slide 4)

L'attacco ICMP flood travolge un target bombardandolo con pacchetti **ICMP Echo Request** ("ping") a un tasso di pacchetti al secondo (pps) molto elevato.

### Impatto

- La vittima consuma **CPU** per analizzare (parse) ogni richiesta.
    
- La vittima emette **Echo Replies** corrispondenti, consumando larghezza di banda in entrambe le direzioni.
    
- **Indicatori:** Picchi ingiustificati nel traffico ICMP.
    

### Varianti: Smurf Attack

- L'attaccante falsifica (forges) l'IP della vittima come sorgente.
    
- Invia **Echo Requests** all'indirizzo di **broadcast** di una rete.
    
- Ogni host su quella rete invia doverosamente **Echo Replies** alla vittima falsificata, moltiplicando il traffico per il numero di host.
    

---

## 5. Tecniche di Potenziamento: Reflection e Amplification (Slide 5-6)

I Cyber Threat Actors ricorrono a due tecniche fondamentali per rendere i DoS più efficaci.

### Reflection (Riflessione)

- L'attaccante invia richieste a server di terze parti chiamati **"reflectors"**.
    
- Falsifica l'IP sorgente inserendo l'indirizzo della **vittima** (spoofing).
    
- Ogni reflector risponde alla vittima, effettivamente "riflettendo" il traffico verso il target.
    
- **Vantaggio:** L'attaccante rimane nascosto.
    
- Comune negli attacchi basati su UDP (dove non viene mantenuto lo stato della connessione).
    

### Amplification (Amplificazione)

- L'attaccante invia piccole query ("tiny, well-formed UDP queries") a servizi esposti su Internet.
    
- Servizi usati: **DNS, NTP, SSDP, Memcached**.
    
- Effettua lo **spoofing** dell'IP sorgente con l'indirizzo della vittima.
    
- Ogni servizio risponde alla vittima con una risposta **più grande** (larger response).
    

---

## 6. Visual Analysis: Smurf Attack (Slide 7)

![[Pasted image 20260207175350.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo schema mostra due fasi distinte che coinvolgono l'Attacker, una "Reflector Network" e il "Victim Server".
> 
> **Meaning:**
> 
> 1. **Step 1:** L'attaccante invia un ping falsificato (spoofed) all'indirizzo di **broadcast** della rete riflettente (`Src=Victim IP`, `Dst=Broadcast IP`).
>     
> 2. **Step 2:** Tutti gli host nella rete riflettente rispondono all'IP della vittima (`Src=Reflector IP`, `Dst=Victim IP`), amplificando l'attacco.
>     

---

## 7. DNS Amplification (Slide 8)

Il servizio DNS è un'ottima opzione per attacchi DoS con amplificazione.

### Caratteristiche

- Basato su **UDP**.
    
- Le risposte sono spesso molto più grandi delle richieste.
    
- Ampia disponibilità di **open resolvers**.
    
- **Fattore di amplificazione:** $> 50x$.
    

### Varianti e Casi Reali

- **NXDOMAIN flood:** Gli attaccanti interrogano nomi inesistenti per forzare una ricorsione costosa e generare risposte NXDOMAIN, bypassando le cache ed esaurendo le risorse.
    
- **Caso Spamhaus (2013):** Il caso reale canonico di amplificazione DNS.
    

---

## 8. NTP Amplification (Slide 9)

Il protocollo NTP (Network Time Protocol) sincronizza gli orologi sulle macchine in rete e gira sulla porta **123/UDP**.

### Meccanismo

- Un comando oscuro, **MONLIST**, permette a un computer richiedente di ricevere informazioni sulle ultime 600 connessioni al server NTP.
    
- L'attaccante effettua lo spoofing dell'IP del target e invia il comando `monlist`.
    
- Il server NTP invia una grande quantità di informazioni al target.
    

### Impatto

- La risposta è molto più grande della richiesta.
    
- **Fattore di amplificazione:** Vicino a **200x**.
    
- **Caso Cloudflare (Feb 2014):** Mitigato un attacco che ha piccato appena sotto i 400Gbps.
    

---

## 9. Memcached Amplification (Slide 10)

**Memcached** è una cache key-value in-memory ad alte prestazioni per velocizzare le web app.

### Vulnerabilità

- Storicamente, poteva ascoltare su TCP e **UDP** (porta di default **11211**).
    
- L'attaccante individua server memcached raggiungibili via Internet che rispondono su UDP/11211.
    

### Esecuzione

1. L'attaccante esegue un **SET** di un valore grande (es. un "big blob") nel server.
    
2. L'attaccante invia una minuscola richiesta **GET** via UDP, falsificando l'IP sorgente con quello della vittima.
    

### Impatto Estremo

- **Fattore di amplificazione:** Può salire fino a **~50.000x**!!!
    
- **Caso GitHub (2018):** Colpito da un attacco memcached-based che ha raggiunto **~1.35 Tbps**.
    

---

## 10. Mitigazioni contro Attacchi Volumetrici (Slide 11)

Le strategie difensive si dividono in prevenzione lato servizio e filtraggio di rete.

### 1) Gestione dei Servizi

- Evitare di esporre servizi verso l'internet pubblico se non necessario.
    
- Imporre l'**autenticazione**.
    
- Non ascoltare su protocollo **UDP**.
    

### 2) Blocco dello Spoofing UDP (BCP-38)

- **BCP-38** è la "best practice" per il **network ingress filtering**.
    
- Usata dagli operatori per bloccare pacchetti con indirizzi IP sorgente falsificati (forged/spoofed) in uscita o entrata dai loro domini.
    
- **Concetto:** L'ISP lega ad ogni interfaccia un filtro che definisce lo spazio IP associato alla rete raggiungibile tramite quell'interfaccia.
    
- **Azione:** I pacchetti in ingresso (Incoming packed) con IP al di fuori dei range consentiti vengono scartati (**discarded**).

# Protocol & Application Layer DoS Attacks

**Tags:** #ingegneria #cyber_security #DoS #DDoS #protocol_attacks #application_attacks

## 1. Protocol Attacks (Slide 1)

Gli attacchi al protocollo (Protocol Attacks) mirano a sfruttare lo stato del protocollo (**Exploit protocol state**).

- Molti protocolli di rete/applicazione mantengono uno stato **per-connection** o **per-session**.
    
- Gli attaccanti forzano la creazione di questo stato o un'elaborazione costosa con un traffico minimo.
    
- **Impatto:** Esaurimento di memoria/CPU (**memory/CPU exhaustion**), overflow della tabella delle connessioni (**connection table overflow**).
    
- **Target:** Middleboxes o server.
    

### Asimmetria dei Costi

- Questi attacchi sfruttano la **cost asymmetry**: una richiesta minuscola può innescare un grande lavoro lato server.
    
- Spesso sono più furtivi (**stealthier**) dei flood volumetrici perché il traffico sembra "legit" (legittimo).
    

---

## 2. TCP SYN Flood (Slide 2)

L'attaccante invia una successione di richieste **TCP Synchronize (SYN)** al target.

### Meccanismo

1. Il Target risponde riconoscendo la richiesta (ACK) e **mantiene la comunicazione aperta** in attesa che il client riconosca la connessione aperta.
    
2. In un SYN Flood riuscito, l'acknowledgment del client non arriva mai.
    
3. **Risultato:** Esaurimento delle code di backlog (**Exhaustion of backlog queues**).
    

### Contromisure (Countermeasures)

- **SYN cookies:** Differiscono l'allocazione dello stato; codificano uno stato minimo nel numero di sequenza SYN-ACK e allocano risorse solo alla ricezione dell'ACK finale.
    
- **Backlog tuning:** Ottimizzazione delle code.
    
- **Per-client quotas:** Quote per singolo client.
    

---

## 3. ACK and RST Floods (Slide 3)

Questi sono attacchi DoS a livello L4 (transport-layer).

### TCP ACK Flood

L'attaccante invia grandi volumi di segmenti TCP con flag **ACK** che non appartengono a connessioni legittime.

- Bypassa le difese **SYN-centric**.
    
- Forza lookup lenti (**slow-path lookups**).
    
- **Egress amplification:** I server che ricevono ACK vaganti possono generare RST in risposta.
    

### TCP RST Flood

Invia molti segmenti con il flag **RST** impostato.

- Forza una validazione costosa su server/middleboxes.
    
- Quando possibile, **termina le connessioni esistenti**.
    

---

## 4. Fragmentation Attacks (Slide 4)

Questi attacchi sfruttano il modo in cui IP ($IPv4/IPv6$) divide i pacchetti in frammenti e come gli endpoint/middleboxes li riassemblano.

### Tipologie

- **Reassembly cache exhaustion:** Flood di primi frammenti (offset 0, $MF=1$) con ID unici per 4-tuple, o frammenti misti che non completano mai un set intero.
    
- **Tiny-fragment / header-hiding:** Divide il pacchetto in modo che il primo frammento contenga solo l'header IP e un frammento ("sliver") di payload, ma non l'header TCP/UDP (per nasconderlo ai filtri).
    
- **Overlapping fragments:** Due o più frammenti rivendicano intervalli di byte sovrapposti con dati in conflitto. Sfrutta l'ambiguità tra diversi dispositivi.
    

> [!abstract] Esempio Reale: FragmentSmack (2018)
> 
> Una falla nel kernel Linux ha esposto un algoritmo inefficiente nel percorso di riassemblaggio dei frammenti $IPv4/IPv6$.
> 
> **Impatto:** Saturazione della CPU.

---

## 5. Application-Layer Attacks (Slide 5)

L'obiettivo è esaurire la capacità di calcolo/IO (**exhaust compute/IO**) all'origine (web/app servers, API, DB, cache) usando richieste che sembrano legittime (**legit-looking requests**).

- **Cost asymmetry:** Piccole richieste $\rightarrow$ grande lavoro del server.
    
- **Common targets:** Login/auth, ricerca, report/export, rendering immagini/PDF, API di pagamento, risolutori DNS.
    
- **Sintomi Operativi:** Aumento della latenza p95/p99, saturazione di CPU/thread pool, crescita della profondità della coda (**queue depth growth**), errori 5xx/timeout, picchi nel tasso di cache miss.
    

---

## 6. HTTP Floods (Slide 6)

Un'ondata ("Surge") di richieste **GET/POST** che mirano a servizi vulnerabili.

- Colpiscono endpoint costosi (search, login, render).
    
- Bypassano le cache (parametri random, URL unici, header no-cache).
    
- Abuso delle funzionalità del protocollo: multiplexing HTTP/2, **rapid reset**, keep-alive aggressivo, pressione su handshake/rinegoziazione TLS.
    

### Variante: Keep-alive abuse

- HTTP/1.1+ mantiene una connessione TCP/TLS aperta per inviare richieste multiple senza rifare l'handshake.
    
- L'attacco apre molte connessioni keep-alive e le lascia inattive (**idle**) $\rightarrow$ consuma socket, memoria e slot thread/concurrency.
    
- Invia header/body molto lenti su connessioni persistenti (slowloris/slow POST).
    

---

## 7. Slowloris-style Attacks (Slide 7)

![[Pasted image 20260207175417.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** L'immagine di un "Slow Loris" (un primate noto per i movimenti lenti).
> 
> **Meaning:** Rappresenta metaforicamente la natura dell'attacco: lento ma inesorabile nell'esaurire le risorse.

- È un attacco "slow header" HTTP/1.x a bassa larghezza di banda (**low-bandwidth**).
    
- L'attaccante apre molte connessioni e invia header di richiesta HTTP parziali **estremamente lentamente**.
    
- Mantiene ogni connessione viva senza mai completare la richiesta.
    
- **Obiettivo:** Esaurimento del thread/connection pool, esaurimento dei File Descriptor (FD), backpressure delle code.
    
- A differenza di altri DoS, i tassi di pacchetti sono bassi (difficili da tracciare), ma l'esaurimento delle risorse è inevitabile.
    

---

## 8. Algorithmic Complexity Attacks (Slide 8)

L'attaccante crea input dall'aspetto legittimo che forzano le applicazioni in percorsi di tempo/memoria del caso peggiore (**worst-case time/memory paths**).

### Mathematical Definition

Si sfrutta la complessità computazionale:

$$O(n^2)$$

> [!abstract] Math Analysis
> 
> L'obiettivo è trasformare operazioni solitamente veloci in operazioni a complessità quadratica o esponenziale (es. backtracking esponenziale).

### Common Vectors

- **Regex DoS (ReDoS):** Pattern con backtracking catastrofico su stringhe create ad hoc.
    
- **Hash-table collision floods:** Molte chiavi POST/JSON che collidono nelle mappe $\rightarrow$ l'inserimento diventa $O(n^2)$.
    
- **Parser/decoder stress:** JSON/XML profondamente nidificati, ricorsione estrema.
    
- **Algorithm hotspots:** Endpoint costosi di grafi/ricerca/report (es. worst-case sort/merge/aggregate).
    

---

## 9. DoS Against Cryptographic Operations (Slide 9)

Abuso di percorsi crittografici costosi per esaurire CPU/memoria su gateway e origini.

- **TLS handshake floods:** Forzano ripetute validazioni ECDHE + catena di certificati.
    
- **Client-cert / signature storms:** Richieste che necessitano di verifica RSA/ECDSA/EdDSA (es. mTLS, controlli webhook/JWT).
    
- **Password hashing pressure:** Tentativi di login di massa che innescano controlli **bcrypt/scrypt/Argon2** (che hanno alti _work factors_).
    
- **PKI validation hits:** Spingono lookup OCSP/CRL o X.509 sovradimensionati/patologici.
    

---

## 10. Mitigations - Part 1 (Slide 10)

Strategie di difesa fondamentali.

### 1) Absorb upstream, not at your origin

- Usare un provider di scrubbing/CDN con **Anycast** e grande capacità all'edge.
    
- Pubblicizzare/instradare i prefissi o mettere le app dietro protezione DDoS gestita L3/L7.
    

### 2) Hide and harden the origin

- Servire via CDN/WAF; bloccare il traffico direct-to-origin (allowlist solo per i propri edge POP).
    
- Cache aggressiva (statica + API dove sicuro).
    
- Abilitare **stale-while-revalidate** per continuare a servire sotto stress.
    

### 3) Rate limit and prioritize at the edge

- Quote per-client, token buckets/leaky buckets per endpoint.
    
- Challenge/attestation per client sospetti.
    

---

## 11. Mitigations - Part 2 (Slide 11)

### 4) Protocol-aware L3/L4 controls

- **SYN cookies** e SYN proxy.
    
- Drop di pacchetti NEW-without-SYN.
    
- Limitare anomalie RST/ACK.
    
- Abilitare **uRPF/BCP-38** con l'ISP per ridurre lo spoofing.
    
- Per i frammenti: riassemblare all'edge, scartare le sovrapposizioni (**drop overlaps**).
    

### 5) Application-layer fail-fast

- Imporre limiti rigorosi (header/body size, regex timeouts, request time budgets).
    
- Autenticare/autorizzare prima del lavoro pesante.
    
- Paginare e limitare (cap) le dimensioni dei risultati.
    
- Accodare e differire task costosi.
    

### 6) Crypto-cost controls

- **TLS 1.3**, session resumption (tickets/PSK), OCSP stapling.
    
- Cachare token/chiavi verificati; verificare prima le cose "economiche".
    

---

## 12. Mitigations - Part 3 (Slide 12)

### 7) HTTP/2-HTTP/3 hygiene

- Limitare (Cap) stream concorrenti, dimensione tabella header e tassi di RST/stream-creation.
    
- Droppare velocemente connessioni che si comportano male.
    
- Guardia contro pattern stile **HTTP/2 rapid reset**.
    

### 8) Resource isolation & autoscaling

- Servizi Stateless, cap di concorrenza per-service.
    
- Autoscaling dei frontend e scale separato dei backend.
    
- Applicare **circuit breakers** e **graceful shedding** (Retry-After, serve stale).
    

### 9) Observability + early detection

- Dashboards/alerts per **SYN backlog**.