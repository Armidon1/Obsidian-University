# 💼 Business Email Compromise (BEC)

### Definizione

Il **Business Email Compromise (BEC)**, noto anche come **Email Account Compromise (EAC)**, è una delle minacce informatiche più costose e sofisticate. Si tratta di una frode basata sull'**Ingegneria Sociale** e sul **Phishing** mirato (spesso _Spear Phishing_ o _Whaling_), in cui un aggressore cerca di **ottenere un guadagno finanziario** inducendo un dipendente a effettuare un trasferimento di fondi non autorizzato o a divulgare informazioni sensibili, fingendosi una figura fidata all'interno o all'esterno dell'azienda.

A differenza degli attacchi di _bulk phishing_ che cercano di ottenere credenziali generiche, il BEC mira specificamente a **transazioni finanziarie o dati riservati** sfruttando la fiducia e l'autorità.

### Tecniche e Fasi dell'Attacco BEC

Gli attacchi BEC di successo sono altamente personalizzati e seguono in genere diverse fasi:

#### 1. Ricerca (Reconnaissance)

- **Raccolta di Informazioni:** L'aggressore studia l'organizzazione e i suoi dipendenti chiave (dirigenti, contabilità, personale HR) tramite i social media (LinkedIn, ecc.), il sito web aziendale e fonti pubbliche.
    
- **Identificazione delle Vulnerabilità:** Vengono identificati i flussi di lavoro, le relazioni tra i dipendenti e, soprattutto, gli **individui autorizzati a effettuare pagamenti**.
    

#### 2. Esecuzione (Impersonation)

L'aggressore ottiene un account e-mail attendibile attraverso uno dei seguenti metodi:

- **Spoofing (Non Autenticato):** L'aggressore utilizza l'**Email Spoofing** per falsificare l'indirizzo del mittente (il campo `From:` nell'header SMTP) in modo che assomigli all'e-mail di un dirigente (es. il CEO). Questo metodo non richiede l'accesso all'account reale.
    
- **Account Compromise (Autenticato):** L'aggressore ottiene l'accesso reale alla casella di posta di un dipendente/dirigente tramite un attacco di **Spear Phishing** per le credenziali o sfruttando password deboli. Questo è il metodo più pericoloso perché le e-mail provengono da un **server di posta legittimo** e superano i controlli SPF/DKIM (a meno che non venga rilevata un'attività anomala).
    

#### 3. Inganno (Fraudulent Request)

Una volta stabilita la falsa identità, l'attaccante invia una richiesta urgente, spesso con uno di questi scenari:

|**Scenario BEC Comune**|**Descrizione**|**Obiettivo**|
|---|---|---|
|**Fattura Falsa (Vendor Email Compromise)**|L'aggressore si spaccia per un fornitore abituale dell'azienda, inviando una fattura che richiede il pagamento su un nuovo conto bancario fraudolento.|Reindirizzamento di pagamenti verso i conti dell'aggressore.|
|**Richiesta Urgente del CEO (CEO Fraud / Whaling)**|L'aggressore si spaccia per un dirigente di alto livello (CEO, CFO) e invia un'e-mail a un dipendente dell'ufficio contabilità, richiedendo un **bonifico urgente** e confidenziale per una "acquisizione segreta" o un "nuovo fornitore".|Trasferimento immediato di grandi somme di denaro.|
|**Furto di Dati HR**|L'aggressore si spaccia per un dirigente che richiede i **dati PII (Personally Identifiable Information)** dei dipendenti (es. W-2, informazioni fiscali) all'ufficio HR.|Utilizzo dei dati per ulteriori frodi o furto di identità.|

### Implicazioni Tecniche e Contromisure

Il BEC sfrutta principalmente le debolezze nell'autenticazione delle e-mail e nelle procedure aziendali.

|**Area di Debolezza**|**Mitigazione Tecnica per Ingegneri**|
|---|---|
|**Spoofing E-mail (BEC di Tipo 1)**|Implementazione rigorosa e monitoraggio di **DMARC (Domain-based Message Authentication, Reporting, and Conformance)**. Una policy DMARC ben configurata (ad esempio, con azione `p=reject`) garantisce che le e-mail spoofate che non superano SPF o DKIM vengano rifiutate.|
|**Account Compromise (BEC di Tipo 2)**|**Autenticazione Multi-Fattore (MFA)** per tutti gli account di posta elettronica. Implementazione di un **SIEM/UEBA** (User and Entity Behavior Analytics) per rilevare attività anomale (es. accesso da geolocalizzazione insolita, download massivo di e-mail).|
|**Header Falsificati/Sottili**|Utilizzo di **Gateway di Sicurezza E-mail (SEG)** avanzati che non si basano solo su SPF/DKIM, ma che analizzano la **Display Name Spoofing** (es. l'attaccante usa un indirizzo e-mail esterno ma il nome visualizzato è "John Smith CEO").|
|**Rischio Umano/Processuale**|Implementazione di procedure rigorose per i **trasferimenti di fondi**, che richiedano sempre una **verifica verbale (telefonica)** o un doppio canale di autenticazione per richieste di pagamento insolite o di modifica dei conti bancari.|

Il BEC è particolarmente difficile da rilevare per i sistemi automatici perché spesso **non contiene allegati malevoli o link dannosi**, ma si basa esclusivamente su un testo apparentemente innocuo e sull'urgenza percepita.