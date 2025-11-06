# 💧 Data Leakage (Fuga di Dati)

### Definizione

Il **Data Leakage** (Fuga o Dispersione di Dati) si riferisce al processo in cui **dati sensibili o riservati vengono esposti, trasmessi, o resi accessibili in modo non intenzionale** a parti non autorizzate.1 A differenza del _Data Breach_ (Violazione di Dati), che è spesso il risultato di un attacco attivo, il _Data Leakage_ può verificarsi a causa di una **negligenza, di una configurazione errata, o di un errore umano o del sistema**.2

Il risultato è lo stesso: i dati finiscono dove non dovrebbero essere, compromettendo la **riservatezza** (Confidentiality) e, potenzialmente, l'**integrità** (Integrity) dell'informazione.3

### Differenza Chiave: Data Leakage vs. Data Breach

Per un ingegnere informatico, è utile distinguere i due termini, sebbene siano spesso usati in modo intercambiabile:

|**Concetto**|**Causa Tipica**|**Esempio**|
|---|---|---|
|**Data Breach (Violazione)**|**Attacco Intenzionale e Malizioso** (es. malware, exploit, accesso non autorizzato).|Un hacker sfrutta una vulnerabilità del software per entrare in un database e rubare le credenziali.|
|**Data Leakage (Fuga/Dispersione)**|**Errore, Negligenza, o Errata Configurazione** (non necessariamente maliziosa).|Un dipendente invia per sbaglio una lista di clienti a un destinatario esterno non autorizzato, o un _bucket_ di storage su cloud è configurato erroneamente come pubblico.|

---

### Dettagli Tecnici e Vettori di Leakage

Il _Data Leakage_ può avvenire attraverso diversi canali:4

#### 1. Fuga Tramite Endpoint (Dispositivi Utente)

- **Dispositivi di archiviazione rimovibili:** Salvataggio di dati riservati su chiavette USB non crittografate o dischi esterni.
    
- **Stampa:** Stampa di documenti sensibili lasciati incustoditi.
    
- **Trasmissione accidentale:** Invio per sbaglio di e-mail contenenti allegati sensibili al destinatario sbagliato (spesso causato dall'auto-completamento dell'indirizzo e-mail).
    

#### 2. Fuga Tramite Rete

- **Misconfigurazione della Rete:** Server configurati per rispondere a richieste esterne che dovrebbero essere limitate all'interno (es. API esposte pubblicamente per errore).
    
- **Protocolli non cifrati:** Trasmissione di dati sensibili su protocolli non cifrati (es. HTTP, FTP) che li rendono vulnerabili allo _sniffing_ (_traffic interception_).
    

#### 3. Fuga Tramite Cloud e Storage

- **Misconfigurazione dei Servizi Cloud:** La causa più comune di _leakage_ moderno. Esempi includono **bucket S3 di Amazon o Google Cloud Storage** erroneamente impostati su "accesso pubblico" o con politiche ACL troppo permissive.
    
    - **Implicazione Tecnica:** Invece di richiedere credenziali, chiunque conosca l'URL del _bucket_ può scaricare i dati.
        
- **Fuga nel codice sorgente:** Credenziali, chiavi API o password codificate (hardcoded) direttamente nel codice sorgente e poi pubblicate in _repository_ pubblici (es. GitHub).
    

### Misure di Prevenzione (Data Loss Prevention - DLP)

La prevenzione della fuga di dati è gestita principalmente tramite soluzioni e policy di **DLP (Data Loss Prevention)**.5 Per un ingegnere informatico, implementare un sistema DLP significa:

1. **Identificazione dei Dati Sensibili:** Classificare e identificare dove risiedono i dati sensibili (PII, dati finanziari, IP aziendale). Questo richiede l'uso di **espressioni regolari** (RegEx), **algoritmi di corrispondenza esatta** o **Machine Learning** per riconoscere i dati.
    
2. **Monitoraggio degli Endpoint:** Distribuire agent DLP sui dispositivi degli utenti per:
    
    - **Bloccare** il caricamento di file specifici su servizi cloud personali (es. Dropbox).
        
    - **Impedire** la copia di dati sensibili su USB non crittografate.
        
    - **Controllare** l'attività di stampa.
        
3. **Monitoraggio della Rete/E-mail:** Ispezionare il traffico di rete e le e-mail in uscita alla ricerca di pattern di dati sensibili. Ad esempio, un server e-mail DLP può bloccare un'e-mail se contiene più di 10 numeri di carte di credito.
    
4. **Sicurezza del Cloud (CSPM):** Utilizzare strumenti di **Cloud Security Posture Management (CSPM)** per monitorare e correggere continuamente le _misconfiguration_ (configurazioni errate) dei servizi cloud (come le politiche di accesso dei _bucket_ S3) in tempo reale.6
    
5. **Formazione:** L'implementazione di controlli tecnici deve essere affiancata dalla formazione degli utenti sull'importanza della gestione sicura dei dati (es. non condividere file sensibili tramite canali non approvati).
    

La _Data Leakage_ è una minaccia persistente e insidiosa perché sfrutta l'elemento umano e l'inevitabile complessità delle architetture cloud.

---

Hai bisogno di un approfondimento su un meccanismo specifico di difesa, come **DLP** o **CSPM**?