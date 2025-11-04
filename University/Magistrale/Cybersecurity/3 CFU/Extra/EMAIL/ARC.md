# 🔗 AUTHENTICATED RECEIVED CHAIN (ARC)

**ARC (Authenticated Received Chain)** è uno standard progettato specificamente per risolvere il problema dell'inoltro (forwarding) e delle mailing list che "rompevano" [[DMARC]]. Aiuta a preservare lo stato di autenticazione e-mail quando un messaggio passa attraverso intermediari.

- **Preserva l'autenticazione:** Se un'e-mail supera i controlli [[SPF]], [[DKIM]] e [[DMARC]] alla fonte _originale_, ARC assicura che questo stato "superato" (pass) possa essere trasportato fino al destinatario finale, anche se [[SPF]] e [[DKIM]] falliscono lungo il percorso.
    
- **Responsabilità ([[Accountability]]):** Ogni intermediario (es. una mailing list) nel flusso di e-mail aggiunge i propri risultati di autenticazione ARC, creando una **catena verificabile** di chi ha gestito il messaggio e se lo ha alterato.
    
- **Migliore Riconsegna (Deliverability):** ARC aiuta le e-mail legittime inviate tramite mailing list o servizi di inoltro a superare i controlli DMARC che altrimenti fallirebbero, impedendo che vengano respinte o messe in spam.
    
- **Complementare a DMARC:** ARC **non sostituisce DMARC**. Funziona al suo fianco per preservare la catena di autenticazione e permettere a DMARC di prendere decisioni più accurate.
    

---

### Cosa NON fa ARC

- Non dice nulla sull'**"affidabilità"** (trustworthiness) del mittente o degli intermediari. Un server malintenzionato può comunque implementare ARC correttamente; sta al server finale decidere se _fidarsi_ di quell'intermediario.
    
- Non dice nulla sul **contenuto del messaggio**.
    
- Gli intermediari potrebbero comunque iniettare contenuti dannosi o, al contrario, rimuovere le intestazioni ARC per rompere la catena.
    

---

## Intestazioni (Header) di ARC

ARC introduce tre nuove intestazioni (header fields) che vengono aggiunte in "set" da ogni intermediario:

1. **`ARC-Authentication-Results` (AAR):** È una copia "archiviata" dell'intestazione `Authentication-Results:` che l'intermediario ha visto al momento della ricezione. Registra i risultati dei controlli (SPF, DKIM, DMARC) così come li ha visti _quell'intermediario_.
    
2. **`ARC-Message-Signature` (AMS):** È una firma in stile DKIM dell'**intero messaggio** (ad eccezione delle intestazioni `ARC-Seal`). Questa firma "fotografa" e protegge l'integrità del messaggio _dopo_ le modifiche dell'intermediario (es. l'aggiunta di un piè di pagina).
    
3. **`ARC-Seal` (AS):** È una firma crittografica in stile DKIM che verifica l'autenticità delle _altre intestazioni ARC_ (AAR e AMS) di quel set. "Sigilla" i risultati di quel passaggio, confermando che nessuno ha manomesso le intestazioni ARC precedenti nella catena.
    

L'intestazione `ARC-Seal:` contiene diversi campi:

- `i=`: Un numero di sequenza (instance) per il set di intestazioni ARC (es. `i=1` per il primo intermediario, `i=2` per il secondo). È fondamentale per ordinare la catena.
    
- `a=/d=/s=`: Campi che corrispondono ai tag DKIM (algoritmo, dominio, selettore) per la firma _dell'intermediario_. (Gli intermediari possono usare le loro normali chiavi DKIM anche per ARC).
    
- `cv=`: (Chain Validation) Indica se la catena ARC _precedente_ (es. quella di `i=1`) è stata validata con successo (`pass`) o è fallita (`fail`) quando è stata ricevuta da questo intermediario (`i=2`).
    
- `b=`: La firma crittografica di tutte le intestazioni ARC di questo set.
    

---

### Firma e Verifica ARC

#### Firma (da parte di un intermediario)

Un intermediario (come una mailing list) deve aggiungere un nuovo set di intestazioni ARC **solo se apporta modifiche che potrebbero rompere i controlli DMARC** (come modificare l'oggetto o il corpo).

1. Copia il contenuto dell'intestazione `Authentication-Results:` che ha ricevuto in una nuova intestazione `ARC-Authentication-Results:` (AAR) e la antepone al messaggio.
    
2. Calcola l'`ARC-Message-Signature:` (AMS) per il messaggio (compresa la nuova AAR e le sue modifiche) e la antepone.
    
3. Calcola l'`ARC-Seal:` (AS) per le intestazioni AAR e AMS appena create e lo antepone.
    

Il tag di sequenza `i=` è cruciale per raggruppare i set di intestazioni (AAR, AMS, AS) e ordinarli correttamente, indipendentemente dall'ordine esatto di inserimento.

#### Verifica (da parte del destinatario finale)

1. **Verificare l' `ARC-Seal`:** Controlla la firma crittografica nel sigillo (AS) più recente (es. `i=2`).
    
2. **Verificare l' `ARC-Message-Signature`:** Controlla la firma del contenuto del messaggio (AMS) di quel set.
    
3. **Controllare i Risultati di Autenticazione:** Esamina l'`ARC-Authentication-Results` (AAR) per vedere lo stato di autenticazione originale (SPF, DKIM) del primo hop (`i=1`).
    
4. **Valutare la Catena:** Continua a verificare la catena a ritroso (validando l'`AS` di `i=1`, ecc.) per mantenere l'integrità dell'intera catena.
    

Se il controllo DMARC finale fallisce (come è probabile), ma esiste una catena ARC _valida_ che mostra un DMARC _pass_ all'origine (`i=1`), il server ricevente può (a sua discrezione) **fidarsi del risultato di ARC** e consegnare il messaggio, ignorando il fallimento DMARC finale.