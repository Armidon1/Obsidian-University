## Sistemi di Rilevamento delle Intrusioni (IDS)

>[!Definizione]
>Un **IDS (Intrusion Detection System)** è un sistema che **automatizza il processo di monitoraggio e analisi** per proteggere un sistema (host o rete).

Il suo funzionamento si basa su un **Framework Generale** che prevede:

1. **Sensori** che raccolgono dati (log, pacchetti).
    
2. Un **Motore di Analisi** che elabora questi dati.
    
3. Una **Knowledge Base** (regole, firme o modelli) con cui confrontare i dati.
    
4. La generazione di **Allarmi** quando viene rilevata una potenziale minaccia, che vengono inviati a un operatore umano.
    

---

### 🗂️ Indice delle Tematiche Trattate

- **[[IDS#Framework Generale|Framework Generale dell'IDS]]**
    - Componenti Core e Flusso (Sensore, Motore di Analisi, Knowledge Base, Dashboard, Risposta)
    - Concetti di Falso Positivo e Falso Negativo
        
- **[[IDS#Caratteristiche Desiderate di un IDS|Caratteristiche Desiderate di un IDS]]**
    - 1. KPI di Rilevamento (Metriche di Performance)
        - Definizioni (TP, FP, TN, FN)
        - Metriche Chiave (Tasso di Rilevamento, Tasso di Falsi Allarmi, Accuratezza, Precisione)
        - Curva ROC (Receiver Operating Characteristics)    
    - 2. Timeliness (Tempestività)
    - 3. Fault Tolerance (Tolleranza ai Guasti)

- **[[IDS#Classificazione degli IDS|Classificazione degli IDS]]** (5 proprietà chiave)    
    - 1. Sistema Monitorato (Dove guarda)
        - Host-Based IDS (HIDS) e EDR
        - Network-Based IDS (NIDS)
        - IDS Basato sui Log
        - Wireless IDS (WIDS)
        - IDS Multi-Livello (Correlato)
            
    - 2. [[IDS#2. Metodologia di Rilevamento|Metodologia di Rilevamento]] (Come pensa)
        - Rilevamento Basato su Misuse (Basato su Firme, Regole, Transizioni di Stato, ML Supervisionato)
        - Rilevamento Basato su Anomalie (Statistico, Basato su Profili, Outlier Detection, Auto-apprendimento)
        - Rilevamento Composito (Ibrido)
            
    - 3. Aspetti Temporali (Quando lavora: Online vs. Offline)
            
    - 4. Architettura (Dove gira: Centralizzata vs. Distribuita)
            
    - 5. Tipo di Reazione (IDS Passivo vs. IPS Attivo)
            
- **[[IDS#Riepilogo Metodologie di Rilevamento|Riepilogo Metodologie di Rilevamento]]** (Grafico)

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
    

## Riepilogo Metodologie di Rilevamento

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
