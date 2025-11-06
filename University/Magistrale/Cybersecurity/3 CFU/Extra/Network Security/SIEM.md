# SIEM – Security Information and Event Management

>[!Definizione]
>Un **SIEM (Security Information and Event Management)** è un sistema di gestione e analisi di livello superiore che si posiziona al di sopra degli altri controlli di sicurezza. La sua funzione principale è **aggregare, unificare e correlare** i log e gli eventi provenienti da tutte le fonti (come firewall, [[IDS]], server) in un'unica interfaccia.

L'obiettivo è "distillare" l'enorme volume di dati di basso livello in **"intelligence operativa" (actionable intelligence)** di alto livello, fornendo una visione unificata per il rilevamento delle minacce, la risposta agli incidenti e la compliance.

### Differenza tra SIEM e IDS
La differenza fondamentale è nel livello di analisi e azione:

- Un **IDS (Intrusion Detection System)** è una fonte di dati. Genera un **allarme** specifico (es. "rilevata scansione di porte") che richiede una decisione immediata.
    
- Un **SIEM** è un aggregatore e correlatore. **Prende quell'allarme dall'IDS**, lo combina con altri eventi (es. log di login falliti sul firewall, log di accesso al server) e fornisce il **contesto** (actionable intelligence) per capire se si tratta di un falso positivo o di un attacco multi-fase, suggerendo come ridurre l'impatto.

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
    

Senza il SIEM, questo sarebbe solo un log criptico. Con il SIEM, ha contesto e significato.
