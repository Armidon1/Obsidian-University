## Introduzione

- Nessuna misura di protezione preventiva (come firewall, VPN o access control list) è a prova di intrusione al 100%. I sistemi di prevenzione avranno sempre delle lacune.
    
- **Nuove tecniche di attacco** emergono continuamente, creando **zero-day exploit** che le difese esistenti non possono riconoscere.
    
- **Vulnerabilità non sfruttate o _silenziose_** (bug) possono esistere nel software per anni prima di essere scoperte.
    
- **Errori di configurazione** (es. password predefinite, porte aperte, permessi impropri) e **insider malevoli** (utenti fidati con cattive intenzioni) sono rischi persistenti che aggirano le tradizionali difese perimetrali.
    
- Poiché la prevenzione _fallirà_ prima o poi, il **monitoraggio continuo** e il **rilevamento degli attacchi** sono componenti essenziali di una solida strategia di sicurezza (Difesa in Profondità).
    

---

## Rilevamento delle Intrusioni (Intrusion Detection)

> “Il processo di monitoraggio degli eventi che si verificano in un sistema informatico o in una rete e di analisi degli stessi alla ricerca di segni di intrusioni — tentativi di compromettere la riservatezza, l'integrità, la disponibilità o di aggirare i meccanismi di sicurezza.”
> 
> — Definizione NIST

---

## Attacchi

### Terminologia

- **Attacco (Attack):** Un _tentativo_ di intrusione. Può essere bloccato da un firewall o da un'altra misura preventiva e non avere alcun impatto.
    
- **Intrusione (Intrusion):** Un attacco _riuscito_. Ciò significa che l'attaccante ha aggirato le difese e ha causato un guasto operativo malevolo, indotto dall'esterno.
    

### Criteri di Classificazione

Gli attacchi possono essere classificati in base a:

- **Tipo:** L'obiettivo dell'attacco (es. DoS, compromissione).
    
- **Connessioni di rete coinvolte:** Connessione singola vs. multipla.
    
- **Origine:** Un singolo IP vs. origini multiple distribuite.
    
- **Ambiente:** Il bersaglio (es. host, rete, wireless).
    
- **Livello di automazione:** Manuale (guidato dall'uomo) vs. automatico (script/worm).
    

---
vedi di più in [[Network Attacks]]
        
## Monitoraggio degli Attacchi

Un singolo attacco può avere un impatto su più sottosistemi, lasciando una scia di prove attraverso router, firewall, proxy e workstation.

![[Pasted image 20251029134610.png]]

I dati di monitoraggio sono generati da quasi tutti i sistemi IT attraverso l'intera infrastruttura di rete.

![[Pasted image 20251029134622.png]]

### Fonti di Dati per il Monitoraggio

Ci sono tre fonti primarie di dati per il rilevamento delle intrusioni:

1. **Flussi di Rete ([[Network Flow]])**
    
2. **Log di Eventi / Sistema** ([[Event Logs]])
    
3. **Cattura Completa dei Pacchetti ([[FPC]])**
    

### 1. Flussi di Rete ([[Network Flow]])

I flussi di rete sono record di **metadati** delle sessioni di comunicazione di rete. Pensateli come una "bolletta telefonica" per la vostra rete: mostrano _chi_ ha parlato con _chi_, per _quanto tempo_ e _quanti_ dati sono stati inviati, ma **NON il contenuto effettivo (payload)** della conversazione.

**Identificazione 5-Tupla (I Campi Chiave):**

1. Indirizzo IP Sorgente
    
2. Indirizzo IP Destinazione
    
3. Porta Sorgente
    
4. Porta Destinazione
    
5. Protocollo (es. TCP, UDP, ICMP)
    

**Dati Aggiuntivi Catturati:**

- Ora di inizio e fine (durata)
    
- Numero di Byte / Pacchetti trasferiti
    
- Flag TCP (che forniscono lo stato della sessione come SYN, ACK, FIN, RST)
    
- Numero di Autonomous System (AS) (per tracciare le connessioni esterne)
    

---

### 2. Log di Eventi / Sistema ([[Event Logs]])

Questi sono record testuali delle attività generate da tutti gli asset IT, fornendo la "verità fondamentale" (ground truth) di ciò che è accaduto su un dispositivo specifico.

- **Generati da:**
    
    - Apparati di rete (firewall, router, switch)
        
    - Server (es. Log Eventi di Windows, `/var/log/syslog` di Linux)
        
    - Host (desktop, laptop)
        
    - Applicazioni (es. log di accesso del server web, log di errore del database)
        
- Contengono informazioni cruciali, come tentativi di autenticazione falliti, errori di sistema o comandi a livello di applicazione.
    

---

### 3. Cattura Completa dei Pacchetti ([[FPC]])

FPC significa catturare e archiviare l'**intero pacchetto**, incluso il **payload** (il contenuto) dei dati.

**Vantaggi:**

- È lo strumento definitivo per la **digital forensics** (informatica forense).
    
- Permette agli analisti di **ricostruire letteralmente l'attacco** passo dopo passo, analizzare i payload del malware o estrarre chiavi di crittografia.
    

**Limitazioni (Perché non è usato ovunque):**

- **Requisiti di archiviazione enormi:** Archiviare tutti i payload di un'azienda è estremamente costoso.
    
- **Overhead prestazionale:** Richiede hardware specializzato ad alta velocità per catturare il traffico al "line rate" (velocità massima della linea) senza perdere pacchetti.
    
- L'FPC è tipicamente implementato **selettivamente** (es. catturando solo i pacchetti che attivano un allarme) o su segmenti di rete ad altissimo valore e basso volume.
    

---

## Sistemi di Rilevamento delle Intrusioni (IDS)

Un [[IDS]] è un sistema che automatizza il processo di monitoraggio e analisi.

### Framework Generale

![[Pasted image 20251029135049.png]]

**Componenti Core e Flusso:**

1. **Sistema Monitorato:** La rete o l'host da proteggere.
    
2. **Sensore:** Raccoglie dati (flussi, log, pacchetti) dal sistema monitorato e genera **Eventi** (una registrazione di un'osservazione con un timestamp).
    
3. **Motore di Analisi (Analysis Engine):** Il "cervello" dell'IDS. Elabora gli eventi, li confronta con la **Knowledge Base** e genera **Allarmi** se viene rilevata una minaccia.
    
4. **Knowledge Base:** Un database di regole, firme o modelli comportamentali che definisce cosa è "normale" o "malevolo".
    
5. **Dashboard:** Un'interfaccia utente dove un operatore di sicurezza umano monitora gli allarmi.
    
6. **Componente di Risposta (Response Component):** Un modulo opzionale che può intraprendere **Azioni** (es. inviare un'email, bloccare un IP) basate su una **Configurazione** predefinita quando scatta un allarme.
    

Gli operatori di sicurezza si affidano all'output dell'IDS, ma gli IDS non sono perfetti. Gli operatori devono investigare gli allarmi (che potrebbero essere **Falsi Positivi**) guardando i log grezzi. Tuttavia, il fallimento più pericoloso è un **Falso Negativo** (un vero attacco che l'IDS non ha rilevato), motivo per cui l'affidabilità dell'IDS è fondamentale.

---

### Caratteristiche Desiderate di un IDS

Un buon IDS deve bilanciare tre caratteristiche principali:

#### 1. KPI di Rilevamento (Key Performance Indicators)

L'accuratezza di un IDS è un compromesso statistico:

- **Vero Positivo (TP):** Un vero attacco si verifica e l'IDS lancia correttamente un allarme. (Bene)
    
- **Falso Positivo (FP):** Non si verifica nessun attacco, ma l'IDS lancia erroneamente un allarme. (Male - causa "fatica da allarme").
    
- **Vero Negativo (TN):** Non si verifica nessun attacco e l'IDS resta correttamente silenzioso. (Bene)
    
- **Falso Negativo (FN):** Un vero attacco si verifica e l'IDS _non lo rileva_. (Malissimo - il fallimento di rilevamento più pericoloso).
    

**Metriche Chiave:**

- **Tasso di Rilevamento (Detection Rate, True Positive Rate, TPR):** `TP / (TP + FN)`
    
    - _Domanda:_ Di tutti gli attacchi reali, quale percentuale abbiamo catturato?
        
- **Tasso di Falsi Allarmi (False Alarm Rate, False Positive Rate, FPR):** `FP / (FP + TN)`
    
    - _Domanda:_ Di tutti gli eventi normali, quale percentuale abbiamo erroneamente segnalato come attacco? (Vogliamo che sia 0).
        
- **Accuratezza (Accuracy):** `(TP + TN) / (Eventi Totali)`
    
    - _Domanda:_ Nel complesso, quale percentuale delle decisioni dell'IDS è stata corretta?
        
- **Precisione (Precision):** `TP / (TP + FP)`
    
    - _Domanda:_ Di tutti gli allarmi lanciati, quale percentuale era un attacco reale? (Un'alta precisione significa meno tempo sprecato in falsi positivi).
        

_Nota sul mondo reale:_ Queste metriche sono difficili da misurare. In una rete reale, non si conosce mai il vero numero di "Attacchi Totali" (specialmente quelli mancati, FN). Pertanto, un IDS deve essere messo a punto (fine-tuned) per il suo ambiente specifico (es. le esigenze di un ospedale sono diverse da quelle di una banca).

Curva ROC:

La curva ROC (Receiver Operating Characteristics) visualizza il compromesso tra il Tasso di Rilevamento (TPR) e il Tasso di Falsi Allarmi (FPR).

![[Pasted image 20251029140336.png]]

- Un **IDS Perfetto** è un singolo punto nell'angolo in alto a sinistra (100% rilevamento, 0% falsi allarmi).
    
- La **Previsione Casuale** (indovinare) è la linea diagonale a 45 gradi.
    
- Un buon IDS ha una curva che si piega il più vicino possibile all'angolo in alto a sinistra. In generale, per aumentare il tasso di rilevamento (muoversi verso l'alto), spesso si deve accettare un tasso di falsi allarmi più alto (muoversi verso destra).
    

#### 2. [[Timeliness]] (Tempestività)

- Questo è il ritardo totale dall'inizio di un'intrusione alla generazione dell'allarme.
    
- Include tutto il tempo di elaborazione, il tempo di propagazione della rete e il tempo di analisi/risposta. Vogliamo che sia il più basso possibile.
    

#### 3. [[Fault Tolerance]] (Tolleranza ai Guasti)

- L'IDS stesso è un bersaglio. Un avversario sa che esiste e cercherà di renderlo inefficiente o di mandarlo in crash.
    
- L'IDS deve essere robusto contro gli attacchi e in grado di riprendersi rapidamente.
    
- **Esempio di Attacco:** Un attacco DoS all'IDS, in cui un attaccante lo inonda con un numero enorme di falsi allarmi ovvi, per nascondere un attacco reale e furtivo nel "rumore".
    

---

## Classificazione degli IDS

Gli IDS possono essere classificati in base a diverse proprietà chiave:

1. **Sistema monitorato** (Dove guarda: Host vs. Rete)
    
2. **Metodologia di rilevamento** (Come pensa: Misuse vs. Anomalia)
    
3. **Aspetti temporali** (Quando lavora: Online vs. Offline)
    
4. **Architettura** (Dove gira: Centralizzata vs. Distribuita)
    
5. **Tipo di reazione** (Cosa fa: IDS Passivo vs. IPS Attivo)
    

---

### 1. Sistema Monitorato

#### Host-Based IDS (HIDS)

Un HIDS è un agente software installato direttamente su un singolo host (un server, una workstation) che monitora eventi _interni_.

- **Monitora:**
    
    - Log di sistema (es. auth.log)
        
    - Processi in esecuzione
        
    - Accesso ai file e integrità del filesystem (es. FIM - File Integrity Monitoring)
        
    - Modifiche alla configurazione
        
    - Chiamate di sistema (System call)
        
- **Tecniche:** Analisi del codice, esecuzione in sandbox, analisi dei log.
    
- **Pro:**
    
    - **Può vedere all'interno del traffico crittografato** (gira sull'host _dopo_ la decrittografia).
        
    - Visione altamente granulare di ciò che è accaduto su quell'host specifico.
        
- **Contro:**
    
    - Può avere un impatto negativo sulle prestazioni (overhead) dell'host.
        
    - Manca di un contesto di rete più ampio (vede solo ciò che accade sul proprio host).
        

**Evoluzione Moderna (EDR):** L'evoluzione attiva degli HIDS è l'**EDR (Endpoint Detection and Response)**. I sistemi EDR non si limitano a rilevare le minacce, ma forniscono anche strumenti per _rispondere_ (es. isolare remotamente l'host dalla rete, terminare un processo malevolo o cancellare un file).

#### Network-Based IDS (NIDS)

Un NIDS è un dispositivo (fisico o virtuale) che monitora il traffico di rete su un segmento di rete specifico.

- **Monitora:** Pacchetti di rete a vari livelli:
    
    - Applicazione (HTTP, SMTP, DNS)
        
    - Trasporto/Rete (TCP, UDP, IP)
        
    - Livelli inferiori (MAC, ARP)
        
- **Implementazione:**
    
    - **Passiva:** Il NIDS monitora una _copia_ del traffico (da un TAP di rete o da una porta SPAN dello switch). È "read-only" e può solo **Rilevare**.
        
    - **Inline (In linea):** Il NIDS si trova direttamente sul percorso del traffico. Può bloccare attivamente i pacchetti malevoli, diventando un **Intrusion Prevention System (IPS)**.
        
- **Limitazione Fondamentale:** Un NIDS **non può ispezionare il traffico crittografato** (es. SSL/TLS, SSH). Il payload è illeggibile. L'unica soluzione è un **Proxy TLS** (o Intercettazione TLS), che esegue una decrittografia "man-in-the-middle", ispezione e ri-crittografia.
    

#### IDS Basato sui Log

- Un IDS specializzato che monitora solo i log di applicazioni specifiche (es. un Database Management System (DBMS), un Content Management System (CMS) o un software di contabilità).
    
- Ha un'elevata granularità per quell'applicazione ma richiede una complessa messa a punto.
    

#### Wireless IDS (WIDS)

- Monitora il mezzo wireless (802.11) per attacchi.
    
- **Sfide:**
    
    - Il mezzo broadcast è intrinsecamente meno sicuro.
        
    - È difficile localizzare fisicamente gli attaccanti.
        
    - La scansione continua di più canali richiede hardware costoso e multi-radio.
        

#### IDS Multi-Livello (IDS Correlato)

- Un sistema gerarchico che aggrega gli allarmi provenienti da molti altri livelli di IDS (HIDS, NIDS).
    
- Un motore di analisi (come un SIEM) correla questi allarmi di basso livello per trovare modelli di attacco complessi e su larga scala.
    

---

### 2. Metodologia di Rilevamento

#### Rilevamento Basato su Misuse (Signature-Based)

Questa metodologia si basa sulla conoscenza di **attacchi noti**.

- Viene definito un modello di comportamento _anormale_ (una "firma").
    
- L'IDS confronta gli eventi con questo modello. Se c'è una corrispondenza, lancia un allarme.
    
- Tutti gli altri comportamenti (qualsiasi cosa che non corrisponda a una firma "cattiva") sono considerati normali e ignorati.
    

**Tecniche:**

- **IDS Basato su Firme (Signature-based):**
    
    - Funziona come un antivirus, usando un database di "impronte digitali" di attacchi noti (es. una stringa specifica, un pattern binario).
        
    - **Strumenti:** _Snort_ o _Suricata_ (vedi anche [[Signatures (Cybersecurity)]]).
        
    - **Contro:** Incapace di rilevare attacchi nuovi (zero-day) o variazioni significative di vecchi attacchi. Il DB delle firme deve essere costantemente aggiornato.
        
- **Sistemi Basati su Regole (Rule-based):**
    
    - Usano condizioni esplicite "if...then" per catturare gli attacchi (es. "SE il pacchetto proviene da X E la porta è Y ALLORA blocca").
        
    - Possono sfruttare motori di regole ad alte prestazioni.
        
- **Analisi delle Transizioni di Stato (State transition analysis):**
    
    - Modella un attacco come una macchina a stati finiti.
        
    - Gli stati corrispondono a diversi stati di un sistema o protocollo.
        
    - Le transizioni sono innescate da eventi.
        
    - Se la macchina raggiunge uno stato contrassegnato come minaccia alla sicurezza, viene lanciato un allarme.
        
- **Basato su Machine-Learning (Supervisionato):**
    
    - Un modello viene addestrato su un enorme dataset _etichettato_ (contenente esempi di eventi "normali" e "intrusivi").
        
    - Può essere molto accurato nel rilevare attacchi noti e le loro variazioni.
        
    - **Algoritmi:** Alberi decisionali, reti neurali, Support Vector Machines (SVM).
        
    - **Problemi:**
        
        - **Marketing vs. Realtà:** Molti prodotti sono venduti come "basati su IA" ma potrebbero essere semplici euristiche.
            
        - **Spiegabilità (Explainability):** Spesso è difficile sapere _perché_ un modello complesso (come una rete neurale) ha segnalato un evento, rendendo difficile la gestione dei falsi positivi.
            
        - **Ambiguità:** Il termine "IA" (AI) è ampio e può significare qualsiasi cosa, da semplici classificatori a complessi deep learning.
            

#### Rilevamento Basato su Anomalie (Anomaly Detection)

Questa metodologia si basa sulla conoscenza del **comportamento normale del sistema**.

- Viene costruito un modello di base (baseline) di ciò che è "normale".
    
- Tutto ciò che _si discosta_ (devia) da questo modello viene segnalato come un potenziale attacco.
    
- **Pro:** Può rilevare attacchi nuovi (zero-day) e minacce inedite.
    
- **Contro:** incline ad alti tassi di falsi positivi (attività legittime ma insolite possono far scattare un allarme).
    

**Sfide:** Il rilevamento delle anomalie è molto difficile da sviluppare. Richiede la modellazione di un sistema estremamente dettagliato. Inoltre, il comportamento "normale" cambia nel tempo (**model drift**). Quando un modello finisce l'addestramento, il sistema potrebbe essere già evoluto, rendendo il modello obsoleto.

**Approcci:**

- **Programmato:** Il sistema è configurato con modelli comportamentali _fissi_.
    
    - **Default Deny:** Un modello molto accurato del comportamento "atteso". Solo gli stati modellati sono permessi.
        
    - **Statistiche Descrittive:** Usa statistiche semplici, regole e soglie (es. "L'uso della CPU non deve superare il 90% per 5 minuti").
        
- **Auto-apprendimento (Self-learning):** L'IDS costruisce automaticamente un modello che rappresenta il "normale" comportamento osservando il sistema.
    
    - **Non-serie temporali (Non-time series):** Modellazione stocastica che non considera il tempo (es. modelli statistici o basati su regole).
        
    - **Serie temporali (Time series):** Il modello _considera_ la correlazione tra gli eventi nel tempo (es. Modelli di Markov Nascosti (HMM), Reti Neurali).
        
- **Basato su Regole (per anomalia):**
    
    - Definisce il comportamento _normale_ con un set di regole (es. "Questo utente dovrebbe loggarsi solo dalle 9 alle 17").
        
    - Quando una regola viene violata, si sospetta un attacco.
        
- **Statistico:**
    
    - Monitora il comportamento misurando variabili nel tempo (es. in finestre temporali mobili).
        
    - Rileva quando le soglie vengono superate (es. 3 deviazioni standard dalla media).
        
    - **Rilevamento di Outlier (Outlier Detection):** Una tecnica chiave. I punti dati sono modellati usando una distribuzione e i punti che cadono molto al di fuori di questa distribuzione sono segnalati come outlier.
        
- **Basato sulla Distanza (Distance-based):**
    
    - Un'alternativa alla modellazione statistica.
        
    - Rileva gli outlier calcolando le distanze tra i punti dati in uno spazio multidimensionale.
        
    - Può basarsi sul **clustering** (punti lontani da qualsiasi cluster) o sulla **densità** (punti in un intorno a bassa densità).
        
- **Basato su Profili (Profiling):**
    
    - Viene generato un profilo che caratterizza l'esecuzione _normale_ di protocolli e servizi.
        
    - Qualsiasi deviazione da questo profilo (es. una richiesta HTTP che non sembra una normale richiesta web) è considerata sospetta.
        
- **Ispirato al Sistema Immunitario:**
    
    - Un metodo di profiling specifico. Vengono raccolti piccoli pattern di comportamento normale (es. sequenze di chiamate di sistema).
        
    - Se una nuova interazione presenta un pattern che non è mai stato visto prima, scatta un allarme.
        

#### Rilevamento Composito (Compound Detection)

Un approccio ibrido che basa il suo funzionamento su modelli sia per il comportamento normale che per quello anomalo.

- Gli eventi vengono confrontati con entrambi i modelli.
    
- La distanza relativa di un evento dai due modelli viene usata per classificarlo come attacco o normale.
    

### Riepilogo Metodologie di Rilevamento

![[Pasted image 20251029153606.png]]

---

### 3. Aspetti Temporali

- **Strumenti On-line (in tempo reale):**
    
    - Possono controllare flussi di dati in ingresso mentre arrivano.
        
    - Utili per rilevare tempestivamente gli attacchi e reagire prontamente (necessari per un IPS).
        
    - Richiedono forti capacità di elaborazione (es. processori di stream, motori di regole ad alte prestazioni).
        
    - Non possono lavorare facilmente su eventi prodotti fuori sincrono (come report statistici batch).
        
- **Strumenti Off-line:**
    
    - Eseguono un'analisi post-evento dei dati di audit (log, file FPC).
        
    - Ideali per il reporting o la digital forensics approfondita.
        
    - Le prestazioni sono raramente un problema, quindi possono essere eseguite analisi più complesse e complete.
        

|**Tipo**|**Descrizione**|
|---|---|
|**IDS Online**|Rilevamento in tempo reale usando l'elaborazione di stream.|
|**IDS Offline**|Analisi post-evento dei log per insight complessi.|

---

### 4. Architettura

- **Centralizzata:**
    
    - L'analisi dei dati viene eseguita in un numero fisso di posizioni (es. un server centrale), indipendentemente da quanti host vengono monitorati.
        
    - **Pro:** Semplifica la configurazione e la gestione.
        
    - **Contro:** Meno tollerante ai guasti (è un single point of failure) e meno scalabile.
        
- **Distribuita:**
    
    - L'analisi viene eseguita in molte posizioni, spesso proporzionali al numero di host (es. IDS basati su agenti).
        
    - **Pro:** Degradazione graduale in caso di guasti; più facile da personalizzare per compiti ad-hoc.
        
    - **Contro:** Configurazione e gestione complesse.
        

|**Tipo**|**Descrizione**|
|---|---|
|**Centralizzata**|Più facile da gestire, meno scalabile, single point of failure.|
|**Distribuita**|Usa più nodi di analisi, tollerante ai guasti, personalizzabile.|

---

### 5. Tipo di Reazione

Questo definisce la differenza tra un **IDS (Detection)** passivo e un **IPS (Prevention)** attivo.

- **Reazione Passiva (IDS):** Tipicamente, gli IDS si limitano a segnalare allarmi a amministratori umani o a un SIEM. La "reazione" più comune è aumentare la sensibilità del sensore per raccogliere più dati.
    
- **Reazione Attiva (IPS):** Il sistema può intraprendere azioni automatiche e non distruttive.
    

![[Pasted image 20251029154241.png]]

![[Pasted image 20251029154301.png]]

|**Azione**|**Descrizione**|**Caso d'Uso**|
|---|---|---|
|**Scartare Pacchetti Malevoli**|Impedisce a pacchetti malevoli specifici di raggiungere la destinazione.|Blocco malware, SQL injection, DDoS.|
|**Bloccare/Terminare Connessioni**|Termina connessioni sospette (es. inviando pacchetti di reset).|Stop a brute-force, port scanning.|
|**Bloccare Indirizzi IP (Blacklisting)**|Blocca tutto il traffico futuro da un indirizzo IP specifico.|Prevenire attacchi ripetuti da IP/botnet noti.|
|**Limitazione di Banda (Rate Limiting)**|Limita il rate di certi tipi di traffico (es. nuove connessioni).|Mitigare attacchi DDoS, tentativi di login brute-force.|
|**Reindirizzamento Traffico (Honeypot)**|Reindirizza il traffico malevolo verso un **honeypot** (un sistema esca).|Raccogliere intelligence sull'attacco proteggendo i sistemi critici.|
|**Modifica Payload Attacco**|Altera o neutralizza parti di payload malevoli (es. rimuovendo un comando).|Prevenire attacchi di buffer overflow.|

---


## Segmentazione della Rete e Zero Trust

### Il Modello Tradizionale: "Castello e Fossato"
[[Network Segmentation]]
- Il design di rete tipico si basa sul concetto di **"fiducia interna" (internal trust)**.
    
- Il mondo è diviso in due zone: "esterno" (non fidato) e "interno" (fidato). So the border between the trusted network and the outside needs to be setup. We can fully protect the assets inside our domain: this means that a machine inside my domain cannot be compromised even by someone inside my network. Most Attacks ignores the border but uses an already compromised PC inside the network (which is trusted). It may happen because the adversary is using my employees (who are dumb) and with a [[Phishing]] email gives the opportunity to the adversary to compromise a trusted PC in my network. 
    
- Il trasferimento di dati è possibile solo attraverso checkpoint controllati (il **firewall**, o "fossato").
    
- **Debolezza:** Questo modello ha un guscio duro ma un centro morbido. Se un attaccante viola la barriera (es. tramite un'email di phishing), **nulla gli impedisce di muoversi liberamente all'interno della rete** (questo è chiamato **movimento laterale**).
    

---

## Architettura Zero Trust
[[Zero Trust Architecture]] 
**Principio:** Un modello di sicurezza moderno che opera sul principio **"Mai fidarsi, sempre verificare" (Never trust, always verify).**  

Assume che nessun utente o dispositivo debba essere considerato fidato per impostazione predefinita, anche se si trova "all'interno" del perimetro di rete.

note that: imagine if we cannot define a phisical limit of the border:
-  imagine if there are a smart working employees
- or maybe some of things are in a cloud service
- in those cases Zero Trust helps, because we don't care about the borders, we simply say "fuck you" to every one who are not idoneo.

### Principi Fondamentali

- **Verifica Esplicita:** Convalida continuamente l'accesso per ogni richiesta usando tutti i punti dati disponibili (identità, posizione, salute del dispositivo, servizio).
    
- **Usa il Minimo Privilegio di Accesso (Least Privilege):** Limita i permessi degli utenti al _minimo_ necessario per il loro lavoro, riducendo il potenziale raggio d'azione (blast radius) se le credenziali vengono compromesse.
	- for example, my employees cannot modify particular parts of my documents.
    
- **Presupponi la Violazione (Assume Breach):** Progetta la rete per _contenere_ potenziali violazioni e minimizzarne l'impatto. Non cercare solo di tenere fuori gli attaccanti; presupponi che siano già dentro.
	- means that, even if you created a good security system, always assume that an attack may be successful: in those cases, i have to minimise the damages.  
    

### Componenti Chiave di un'Architettura Zero Trust

- **Identity and Access Management (IAM):** Gestisce le identità degli utenti e impone autenticazione e autorizzazione forti.
	- of course, i want to know who is acting in my devices
    
- **Sicurezza dei Dispositivi (Device Security):** Monitora la "salute" dei dispositivi (es. "questo dispositivo ha le patch ed ha l'antivirus attivo?").
	- i need to patch my software/hardware vulnerabilities
    
- **Segmentazione della Rete:** (Vedi sotto) Suddivide la rete in piccole zone per limitare il movimento laterale.
	- the idea is that: let's start by a border defence, if someone breaches my trusted network, then i'm fucked. So i decide to creating borders between my internal PC's. Of course i have to control each borders, so i have to control more stuff. The more borders i include in my systems, the more overhead i'll get.
    
- **Protezione dei Dati (Data Protection):** Protegge i dati stessi (es. tramite crittografia) e impone la privacy dei dati.
	- of course, it doesn't mean that my data can be shared everywhere. Reducing the risk means that we are reducing a lot the possibility to be breached.
    
- **Monitoraggio Continuo e Analisi:** Traccia il comportamento di utenti e dispositivi per rilevare anomalie.
    

### Benefici

- **Sicurezza Migliorata:** Limita l'accesso e minimizza l'impatto di una violazione.
    
- **Superficie d'Attacco Ridotta:** Non esiste un'unica rete interna "fidata" da attaccare.
    
- **Supporto per Lavoro Remoto e Cloud:** Progettato per ambienti di lavoro moderni e distribuiti.
    
- **Compliance e Privacy dei Dati:** Aiuta a soddisfare i requisiti normativi con controlli d'accesso granulari.
    

---

## Strategie di Segmentazione della Rete (Implementare la Zero Trust)
è il cuore pulsante della sicurezza di una rete: è assolutamente necessario essere esperti in questo campo. 
### Cos'è la Segmentazione della Rete?

Una strategia di sicurezza che divide una rete in domini di protezione più piccoli e isolati (segmenti). Richiede l'implementazione di controlli (come i firewall) sui confini che collegano questi segmenti.
- esempio: a humanity resources office, to communicate with the logistic ones has to respect many rules. Inside each office, is not controlled
- può succedere anche che a volte questi bound sono validi solo per un certo periodo di tempo: se un team specifico deve lavorare solo per 2 anni, allora dopo 2 anni questi bound devono sparire

**Vantaggi:**

- **Ostacola il movimento laterale** per un attaccante.
    
- **Riduce la superficie d'attacco** e limita i potenziali danni.
	- la superficie d'attacco: immagina un adversary che è fuori dalla compagnia, fa un check da fuori delle possibili vulnerabilità della compagnia ([[Probing-Scanning]]): magari studiandone i servizi prodotti da possibili macchine internet. Dopo aver studiato queste opportunità, l'adversary ha davanti la "Superficie d'attacco". Che succede se l'adversary attacca anche i laptop personali degli employees? Potrebbe scoprire che magari qualche coglione nella mia compagnia è vulnerabile ad attacchi [[Phishing]], allora lo frega con un email [[Phishing]] e scopre nuove vulnerabilità della mia compagnia: in questo modo la superficie d'attacco cresce.   
    
- **Permette un monitoraggio e una gestione più granulari** del traffico.
    
- **Aiuta a soddisfare i requisiti normativi** isolando i dati sensibili (es. un segmento PCI per le carte di credito).
	- Immagina il GDPR (dal 2018): se hai a che fare con dati sensibili, tu sei costretto a gestire correttamente questi dati. Può succedere che un controllore arrivi nella tua struttura e controlla che hai implementato tutti i best practices
    

---

### Segmentazione Fisica

- Funziona a **livello hardware**, dividendo la rete in blocchi fisicamente separati (es. switch diversi, stanze diverse).
    
- L'esempio estremo è una rete **"air-gapped"** (fisicamente isolata) senza alcuna connessione ad altre reti.
    
- **Pro:** Massima sicurezza e isolamento.
    
- **Contro:** Estremamente inflessibile, costosa e difficile da gestire.
	- che succede se devo spostare un tizio da un ufficio ad un altro? devo staccare il suo PC fisicamente dal cavo Ethernet e portare fisicamente il PC da una parte all'altra.
![[Pasted image 20251105143511.png]]
this device is a device which impone la direzione della trasmissione dati in un unica direzione.

è possibile anche lavorare con trasmissioni wireless, ma sono molto più insicure e difficili da gestire, perciò lo si ignora. Ancora di più se si parla di connessioni wireless tra più reti wireless.

Una volta che hai creato la tua architettura della rete a partire dal livello hardware, allora sai già perfettamente quale PC fa cosa e come è connesso, perciò implementare la sicurezza a livello software sarà più semplice.

### Segmentazione Logica
funziona semplicemente andando a modificare a livello software gli accessi. 

- Funziona a livello software, creando confini definiti via software su hardware condiviso.
    
- **Pro:** Molto più **flessibile** della segmentazione fisica; permette un **controllo dinamico** e **centralizzato** (es. Software-Defined Networking - SDN). questo però può essere un problema però: proprio perché è più semplice e flessibile, spesso per mancanza di attenzione si fanno errori. 
    
- **Contro:** Può essere vulnerabile a bug software che rompono le garanzie di sicurezza.
    

Esempio: VLAN, VLAN + Firewall, Micro-segmentazione
per saperne di più, vedi [[Spiegazione Segmentazione Logica|qui]]

### Micro-segmentazione

- Un approccio molto granulare che applica la segmentazione a livello della **singola applicazione o workload**.
    
- **Esempio:** Invece di un segmento "Web Server", _ogni singolo web server_ è nel proprio segmento ed è autorizzato a parlare solo con il _suo specifico database_ sulla _sua specifica porta_, e nient'altro.
    
- **Pro:** L'opzione migliore per implementare la Zero Trust; massima flessibilità; supporta ambienti ibridi e cloud.
	- Bisogna lavorare anche con i Firewall
    
- **Contro:** Può portare a una gestione complessa delle policy; potenziale overhead.
    

#### Approcci alla Micro-segmentazione

- **Basata sulla Rete (Network-Based):** Usa indirizzi IP o sottoreti.
    
- **Basata sull'Applicazione (Application-Based):** Le policy si basano su identificatori a livello di applicazione.
    
- **Basata sull'Utente (User-Based):** Controlla l'accesso a livello di utente (es. "Alice" può accedere all'app finanziaria).
    
- **Basata sul Processo (Process-Based):** Le policy si basano su _processi specifici_ all'interno di un workload (es. `apache.exe` può parlare sulla porta 80, ma `powershell.exe` no).
    

---

## VLAN (Virtual LAN)
Le VLAN si possono implementare solo grazie ai Switch. Le VLAN funzionano grazie a Router per cui una specifica porta ethernet è associata come VLAN1 mentre un altra porta ethernet è VLAN2. in questo caso, una sottorete che è collegata alla porta VLAN1 non è in grado di comunicare con una VLAN2 (da approfondire meglio). 

Le [[VLAN]] sono la tecnologia più comune per implementare la **segmentazione logica**.

- Funzionano al **Livello 2 OSI** (Data Link).
    
- Sono implementate da quasi tutti gli switch di rete commerciali.
    
- Permettono a un'unica infrastruttura fisica di rete di essere suddivisa in più domini di broadcast _logici_.
    

![[Pasted image 20251105150400.png]]
Recuperare che cos'è un [[Trunk link]]. I trunk link si possono effettuare solamente tra Router.![[Pasted image 20251105150418.png]]
Definiamo trusted i Switch ma non necessariamente i Client.
![[Pasted image 20251105150428.png]]
Notiamo che siamo a Livello 3, non possiamo lavorare solamente a Livello 2 (di collegamento). quindi la presenza di un router è necessario. 
![[Pasted image 20251105150447.png]]Come mostrato nei diagrammi, i dispositivi sulla VLAN 10 (HR) e sulla VLAN 20 (Finance) possono essere collegati allo stesso switch fisico ma non possono comunicare direttamente.

Per comunicare _tra_ VLAN (es. per far accedere l'impiegato HR al DB HR), il traffico deve passare attraverso un **dispositivo di Livello 3 (un router, ricordiamo il livello di rete)**. Questo router funge da checkpoint dove vengono applicate le Access Control List (ACL) per imporre le regole di sicurezza. 

[[spiegazione VLAN| qui la spiegazione dettagliata sulle VLAN]]

---

## SIEM – Security Information and Event Management
[[SIEM]]
### Il Problema: Sovraccarico di Dati (Data Overload)

Una rete moderna ha centinaia di dispositivi ([[Firewall]], [[IDS]], server, switch), che generano tutti migliaia di log e allarmi.

![[Pasted image 20251029134622.png]]![[Pasted image 20251105152030.png]]![[Pasted image 20251105152035.png]]![[Pasted image 20251105152040.png]]


Un singolo attacco crea una scia confusa di dati attraverso tutti questi sistemi.

![[Pasted image 20251029134610.png]]

### La Soluzione: SIEM

Un sistema **SIEM (Security Information and Event Management)** risolve questo problema.

- È un livello di gestione e analisi posizionato _sopra_ tutti i controlli di sicurezza esistenti.
    
- **Connette e unifica** le informazioni da tutti questi sistemi preesistenti, permettendo di analizzarle e **correlarle** da un'unica interfaccia.
    

### Scopo e Funzioni

L'obiettivo finale di un SIEM è "distillare" enormi quantità di informazioni di basso livello (log, flussi) in **intelligence operativa (actionable intelligence)** di alto livello.

- **Funzioni:**
    
    - **Aggregare:** Raccogliere e combinare log ed eventi da tutte le fonti.
        
    - **Correlare:** Trovare relazioni nascoste tra gli eventi (es. "un login fallito sul server, _seguito da_ una scansione di porte dallo stesso IP, _seguito da_ un login riuscito su un'altra macchina" = un attacco multi-fase).
        
    - **Supportare:** Abilitare il rilevamento degli incidenti, la risposta rapida e la reportistica di compliance.
        

### Obiettivi Chiave
![[Pasted image 20251105152010.png]]

- **Visibilità di Sicurezza Unificata:** Un unico pannello di controllo (single pane of glass) per la sicurezza dell'intera organizzazione.
    
- **Rilevamento e Risposta agli Incidenti:** Aiuta a rilevare, prioritizzare e rispondere alle minacce in tempo reale.
    
- **Compliance e Reporting:** Automatizza la raccolta dei log e la reportistica necessaria per le normative (es. PCI, HIPAA, GDPR).

Sembra proprio quello che fa un [[IDS]], però ricorda sempre cosa produce un [[IDS]]: un allarme e quindi bisogna prendere subito una decisione. Il SIEM prende quindi questo allarme e ti dice cosa dovresti fare per ridurre l'impatto dell'attacco.

### Esempio di SIEM in Azione
![[Pasted image 20251105152101.png]]

- **Log di basso livello:** `10.100.20.18 ha avviato la Copia del Database... verso l'Host 10.88.6.12`
    
- **Domanda dell'Analista:** Questo log mostra un'attività legittima o un attacco?
    
- **Il SIEM Fornisce Contesto:**
    
    - `10.100.20.18` è un server nell'ufficio "Pennsylvania".
        
    - `10.88.6.12` è un server nell'ufficio "Boston".
        
    - Le credenziali usate erano `USSaleSyncAcct`.
        
    - Quell'account appartiene a "Accounting IT".
        
    - Questo è un "processo aziendale valido" che gira ogni notte.
        
- **Risultato (Actionable Intelligence):** Questa è un'attività aziendale valida, non un attacco. (Vero Negativo).
    
**In sintesi:** Mentre un report unificato è un _output_ del SIEM, il suo _motore_ serve a trasformare **dati grezzi** e scollegati in **informazioni contestualizzate (Contestualizzate, è la parola chiave)** che permettono agli amministratori di capire _se_ e _dove_ c'è un attacco complesso in corso
Senza il SIEM, questo sarebbe solo un log criptico. Con il SIEM, ha contesto e significato.



---

## Riferimenti

- NIST SP 800-94 — _Guide to Intrusion Detection and Prevention Systems (IDPS)_, 2007
    
- Lazarevic et al., _Intrusion Detection: A Survey_, in _Managing Cyber Threats_, Springer, 2005
    
- Moore et al., _The Spread of the Sapphire/Slammer Worm_, 2003
    
- Powell & Stroud, _MAFTIA Project Deliverable D2_, IBM Zurich, 2001