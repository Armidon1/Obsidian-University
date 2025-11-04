# 🚫 Mancanza di Tracciabilità (Lack of Traceability)

### Definizione

La **Mancanza di Tracciabilità** in un sistema informatico o di sicurezza si verifica quando non esiste la capacità di **collegare in modo inequivocabile e documentato** ogni azione, evento, modifica o requisito a un'origine, una causa o un risultato ben definito. In pratica, è l'incapacità di rispondere alla domanda fondamentale: "**Chi ha fatto cosa, dove, quando e perché?**"

Questo concetto è cruciale in tutte le fasi del ciclo di vita dello sviluppo del software (SDLC) e nella gestione degli incidenti di sicurezza.

### Ambiti di Rilevanza per gli Ingegneri

La tracciabilità è essenziale e la sua assenza è critica in due aree principali:

#### 1. Tracciabilità del Requisito (Requirement Traceability)

Ingegneria del Software (SDLC):

- **Definizione:** L'abilità di descrivere e seguire la vita di un requisito in entrambe le direzioni: dall'origine (es. esigenza del cliente) alle implementazioni (codice, test) e viceversa.
    

![Immagine di requirement traceability matrix](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcT6OSqps5_3fmV_L1yX2E_-JjrA29m51UZaGF2Cwv_NOIe7Zo8qzRiTbGEDbG8UYzEahBVjBbFmXR2-O4q_xkrZd_TX-BnGWk2gYuZIOePG7feQQA0)

Shutterstock

- **Implicazione in Sicurezza:** Se un requisito di sicurezza (es. "Il sistema deve supportare MFA") non è tracciabile, non è possibile:
    
    - Verificare che sia stato completamente implementato nel codice.
        
    - Assicurarsi che sia coperto da casi di test di sicurezza (SAST/DAST).
        
    - Dimostrare la _compliance_ alle normative (es. GDPR, PCI DSS).
        
- **Strumento:** Si utilizza una **Matrice di Tracciabilità dei Requisiti (RTM)**.
    

#### 2. Tracciabilità Forense e Operativa (Forensic/Operational Traceability)

Cybersecurity e Incident Response:

- **Definizione:** La capacità di ricostruire la sequenza cronologica di eventi che hanno portato a un incidente (es. una violazione, un malfunzionamento, o una modifica non autorizzata). Dipende dalla qualità dei dati di log.
    
- **Implicazione in Sicurezza:** La mancanza di tracciabilità forense (es. log mancanti, incompleti o modificati) porta a:
    
    - **Fallimento dell'Indagine:** Impossibilità di determinare la **root cause** dell'attacco, l'estensione della violazione (_extent of compromise_), e l'identità dell'aggressore.
        
    - **Incapacità di Contenimento:** Se non si traccia il percorso dell'aggressore (_lateral movement_), non si può garantire che sia stato completamente espulso dalla rete.
        
    - **Non-Repudiation:** Impossibilità di dimostrare in modo legale e tecnico che una specifica azione è stata eseguita da un utente o un'entità specifica.
        

---

### Dettagli Tecnici e Fattori Contribuenti

La mancanza di tracciabilità operativa è un difetto tecnico grave spesso dovuto ai seguenti problemi:

|**Fattore Contribuente**|**Descrizione Tecnica**|**Impatto sulla Sicurezza**|
|---|---|---|
|**Logging Inadeguato**|Il sistema non registra eventi critici (es. tentativi di accesso falliti/riusciti, modifiche ai permessi, esecuzione di comandi privilegiati).|**Punto cieco** per i team SOC/Blue Team. L'aggressore può operare indisturbato.|
|**Log Integrity Compromise**|I log non sono protetti da manipolazione. L'aggressore ha cancellato o modificato i file di log per coprire le tracce.|**Non-affidabilità** delle prove forensi. Richiede l'uso di sistemi **WORM** (Write Once, Read Many) o l'invio remoto a un SIEM protetto.|
|**Sincronizzazione Temporale Assente**|I timestamp negli eventi sui diversi sistemi non sono sincronizzati (mancanza di **NTP - Network Time Protocol**).|Impossibilità di correlare gli eventi in una sequenza temporale coerente tra diversi host durante un'indagine.|
|**Identificazione Insufficiente**|Molte azioni vengono eseguite con account di servizio generici (`service_admin`) o account condivisi, anziché da identità utente uniche.|**Violazione del principio del Least Privilege** e impossibilità di stabilire l'autore effettivo dell'azione.|

### Mitigazione e Best Practice

Per gli ingegneri, mitigare la mancanza di tracciabilità significa adottare pratiche rigorose:

1. **Standardizzazione dei Log:** Definire standard per il livello e il formato di _logging_ su tutti i sistemi. Utilizzare formati strutturati come **JSON** o **Syslog standard**.
    
2. **Centralizzazione e Protezione:** Tutti i log devono essere inoltrati in tempo reale a un sistema **SIEM (Security Information and Event Management)** o a un **Log Aggregator** centralizzato, e il SIEM deve essere protetto dall'accesso non autorizzato.
    
3. **Identità Unica:** Eliminare l'uso di account condivisi. Assicurarsi che ogni azione privilegiata sia mappata a un **singolo utente autenticato** (es. utilizzando un sistema **PAM - Privileged Access Management**).
    
4. **Time Synchronization:** Implementare e monitorare l'uso del **Network Time Protocol (NTP)** su tutti i server e gli endpoint per garantire che tutti i log siano correlabili temporalmente.
    
5. **Audit Trail:** Per i database e i sistemi critici, implementare **Audit Trail** dettagliati che registrino ogni `SELECT`, `UPDATE`, `INSERT` e `DELETE` con l'identità dell'utente.
    

La tracciabilità non è solo una _feature_ utile, ma un **requisito non funzionale critico** per la conformità normativa e la resilienza operativa in caso di cyberattacco.