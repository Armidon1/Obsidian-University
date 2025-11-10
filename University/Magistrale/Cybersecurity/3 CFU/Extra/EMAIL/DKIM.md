# DKIM

Domain Keys Identified Mail (DKIM), come specificato nell'RFC 4871, è un protocollo che consente a un dominio (il "dominio firmatario") di rivendicare la responsabilità di un messaggio e-mail apponendo una firma crittografica. Questa firma viene allegata all'e-mail come un'intestazione (header).

I destinatari del messaggio (o i loro server di posta) possono verificare questa firma. Lo fanno interrogando il DNS (Domain Name System) del dominio firmatario per ottenere la chiave pubblica necessaria per la verifica.

DKIM è un componente fondamentale della moderna autenticazione e-mail, che lavora al fianco di [[SPF]] e [[DMARC]] per combattere lo spoofing e il phishing.

## Cosa garantisce DKIM

- **Integrità del contenuto dell'e-mail:** Assicura che le parti dell'e-mail (come il corpo e intestazioni specifiche) non siano state manomesse _dopo_ essere state firmate.
    
- **Autenticazione del dominio:** Verifica che il dominio indicato nella firma (`d=`) sia quello che ha effettivamente firmato il messaggio.
    
- **Non ripudio:** Il firmatario non può facilmente negare di aver inviato il messaggio, poiché la firma può essere creata solo con la sua chiave privata.
    

---

## Possibile implementazione di DKIM

![[Pasted image 20251028184726.png|600]]

Il diagramma illustra il flusso di un'e-mail firmata con DKIM:

1. **Rete di origine (Mail Origination Network):**
    
    - Un utente ([[MUA]] - Mail User Agent) invia un messaggio tramite SMTP.
        
    - Il messaggio arriva al Mail Submission Agent ([[MSA]]), che lo passa al **Signer (Firmatario)**.
        
    - Il Firmatario (che può essere l'[[MSA]] stesso o un modulo dell'[[MTA]]) utilizza una **chiave privata** per generare la firma e la allega all'e-mail nell'intestazione `DKIM-Signature`.
        
    - Il messaggio viene quindi inviato all'[[MTA]] (Mail Transfer Agent) in uscita.
        
2. **Rete di destinazione (Mail Delivery Network):**
    
    - L'e-mail viaggia via SMTP verso l'MTA del destinatario, che la passa al Mail Delivery Agent (MDA).
        
    - Il componente **Verifier (Verificatore)** dell'MDA (o dell'MTA in ingresso) rileva l'intestazione `DKIM-Signature`.
        
    - Esegue una **query/risposta DNS per la chiave pubblica** al server DNS del mittente.
        
    - Utilizza la chiave pubblica recuperata per validare la firma.
        
    - Se valida, il messaggio viene consegnato all'MUA del destinatario (ad esempio, tramite POP o IMAP).
        

---

## Come funziona DKIM

### 1. Generazione della firma (Processo di firma)

Quando un'e-mail viene inviata, il server di posta del mittente (o un servizio di firma) genera una firma crittografica. Questa firma si basa su parti specifiche del messaggio, come il corpo (o parte di esso) e intestazioni selezionate (ad esempio, `From`, `Subject`, `Date`).

- Questa firma viene creata utilizzando una **chiave privata** controllata solo dal dominio di invio.
    
- La firma viene quindi aggiunta all'e-mail come una nuova intestazione: l'intestazione **`DKIM-Signature`**.
    

Questa intestazione contiene diverse coppie chiave-valore (tag), tra cui:

- **`a=`:** L'algoritmo di hashing e crittografia utilizzato (es. `rsa-sha256`).
    
- **`d=`:** Il dominio che si assume la responsabilità dell'e-mail (il dominio firmatario).
    
- **`s=`:** Il **"selettore"** (selector), un nome utilizzato per trovare la chiave pubblica specifica nel DNS.
    
- **`h=`:** L'elenco delle intestazioni e-mail che sono state incluse nel calcolo della firma.
    
- **`bh=`:** L'hash (impronta digitale) del corpo del messaggio.
    
- **`b=`:** La firma crittografica vera e propria (un valore codificato in base64).
    

### 2. Chiave pubblica pubblicata nel DNS

Il dominio di invio pubblica la chiave pubblica corrispondente alla chiave privata utilizzata per la firma.

- Questa viene pubblicata nel DNS (Domain Name System) come un **record TXT**.
    
- La chiave pubblica viene utilizzata dai destinatari per **verificare l'autenticità della firma**.
    
- La posizione del record DNS è specifica, combinando il selettore (`s=`) e il dominio (`d=`). Ad esempio: `selettore._domainkey.dominio.it`. (Nell'esempio `google._domainkey.uniroma1.it`).
    
- Il selettore consente a un dominio di avere più chiavi pubbliche, il che è utile per la rotazione delle chiavi (cambiandole periodicamente per sicurezza) o per consentire a servizi di terze parti (come una piattaforma di newsletter) di inviare per conto del dominio.
    

Ecco un esempio di query per una chiave pubblica DKIM:

> `dig +noall +answer google._domainkey.uniroma1.it txt`
> 
> `google._domainkey.uniroma1.it. 21600 IN TXT "v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzMa8wGDtu7DVjVP1JwVzMym/KktdVSBhvtMbgpolQTWqKxRHejICsUvvFv6WGP7kKQnVA5" "2JtFU9LVGvTfkNF5J/x/9wU1BSQMCwGc4IXNdgA5fcn/49fV+YY1RFY44PhoTSWTQnKp7axDRF03Uo05uFXS100nNo0Gd/" "tnDRG538tnM8VzZIF+jjS76GkV/iZT2tcDSBMsWjZTR" "tk7eG/GDVS8pbD14CX/bf7RTf1t3sTiwcp3YUn5T66ioCmc7PIu5CCKfTcW7i7E246Ef4hz+6CySyNRxipnrK6BrXGoraod5U66K6boXVWojDKHRflvdoeQ49hW8N5PHFqJKebwIDAQAB"`

### 3. Processo di verifica

Quando un server di posta ricevente riceve un'e-mail, esegue i seguenti passaggi:

- Cerca l'intestazione `DKIM-Signature` per trovare il dominio firmatario (`d=`) e il selettore (`s=`).
    
- Interroga il DNS per quel dominio e selettore per recuperare la chiave pubblica.
    
- Il server ricalcola l'hash del contenuto del messaggio ricevuto (utilizzando le intestazioni elencate in `h=` e il corpo, confrontandolo con `bh=`).
    
- Utilizza la chiave pubblica per decrittografare la firma (`b=`) e confronta il risultato con l'hash che ha appena calcolato.
    

Se la firma corrisponde, conferma due cose:

1. **Integrità del messaggio:** Le parti firmate dell'e-mail non sono state alterate durante il transito.
    
2. **Autenticità:** L'e-mail è stata effettivamente autorizzata dal dominio indicato nel tag `d=`.
    

### 4. Esito positivo o negativo del controllo DKIM

- **Pass (Superato):** Se la firma è valida, il messaggio è autenticato. Il server ricevente sa che il messaggio proviene da una fonte autorizzata e non è stato manomesso.
    
- **Fail (Fallito):S** Il messaggio fallisce il controllo DKIM se la firma non corrisponde. Questo può accadere per due motivi principali:
    
    1. Il contenuto o le intestazioni firmate sono stati alterati durante il transito.
        
    2. La chiave pubblica nel DNS non corrisponde alla chiave privata che ha creato la firma (è una falsificazione).
        
- **Azione:** Un fallimento DKIM da solo di solito non causa il rifiuto di un'e-mail. L'azione finale (come il rifiuto o l'invio in spam) dipende in genere da altri fattori, in particolare dalla **policy DMARC** del dominio.
    

---

## Selettori (Selectors)

I selettori vengono utilizzati per suddividere lo spazio dei nomi delle chiavi, consentendo più chiavi pubbliche contemporanee per dominio firmatario.

- Ad esempio, i selettori potrebbero indicare le sedi degli uffici, le date di firma o persino i singoli utenti.
    
- Nella pratica moderna, i selettori sono più spesso utilizzati per delegare la capacità di firma a provider di terze parti.
    

**Casi d'uso comuni per i selettori:**

- **Delega:** Un dominio può consentire a un partner (come un fornitore di pubblicità o una piattaforma di marketing) di inviare e-mail per suo conto. Il partner ottiene il proprio selettore e la propria chiave, che il proprietario del dominio può facilmente revocare senza influenzare altri flussi di posta.
    
- **Utenti remoti:** Consentire ai viaggiatori frequenti di inviare messaggi localmente senza doversi connettere a uno specifico MSA centralizzato.
    
- **Domini di inoltro:** Utilizzati da domini "di affinità" (ad esempio, associazioni di ex-alunni) che inoltrano la posta in arrivo ma non gestiscono un MSA per la posta in uscita.
    

---

## DKIM e SPF

**Come si confronta DKIM con SPF?**

- **SPF (Sender Policy Framework):** Autentica il _server di invio_. Controlla se l'indirizzo IP del server è elencato nel record SPF del dominio come mittente autorizzato. Valida _da dove_ proviene l'e-mail.
    
- **DKIM:** Autentica il _contenuto dell'e-mail_. Verifica una firma digitale rispetto a una chiave pubblica nel DNS. Valida _cosa_ è stato inviato e _chi_ lo ha firmato.
    

**Limitazioni di DKIM:**

- **Non autentica l'indirizzo "From" visibile:** Questa è una limitazione critica. DKIM verifica solo l'autenticità del dominio nel tag `d=` della sua firma. Un utente malintenzionato può inserire `ceo@tuazienda.com` nell'intestazione `From:` _visibile_, ma firmare il messaggio con il proprio dominio dannoso (`d=dominio-malevolo.com`). Il controllo DKIM _passerà_ (per `dominio-malevolo.com`), ma l'e-mail è comunque uno spoof. Questo problema viene risolto dal controllo di "allineamento" di DMARC.
    
- **L'inoltro delle e-mail può rompere DKIM:** Se un server di inoltro altera il contenuto, anche aggiungendo un piccolo disclaimer o piè di pagina, la firma DKIM si romperà e il controllo fallirà.
    
- **Nessuna crittografia:** DKIM fornisce autenticità e integrità, ma **non** fornisce crittografia o privacy. Il contenuto del messaggio viene comunque inviato in chiaro.
    

---

## Canonicalizzazione (Canonicalization)

I server di posta e i relay spesso apportano piccole modifiche a un'e-mail in transito, che possono invalidare involontariamente una firma DKIM.

Per tenere conto di ciò, DKIM utilizza **algoritmi di canonicalizzazione** per creare una versione "normalizzata" delle intestazioni e del corpo prima di firmare e verificare.

- Le intestazioni sono soggette a un algoritmo di canonicalizzazione.
    
- Anche i corpi sono soggetti a un algoritmo di canonicalizzazione.
    
- Le scelte per l'intestazione e il corpo sono indipendenti (ad esempio, `c=relaxed/simple`).
    

I due tipi sono:

- **`simple` (rigido):** Tollera quasi nessuna modifica. Anche una modifica negli spazi bianchi può rompere la firma.
    
- **`relaxed` (tollerante):** Più robusto. Consente modifiche comuni, come cambiamenti negli spazi bianchi o nel maiuscolo/minuscolo delle intestazioni. L'uso di `relaxed/relaxed` è la pratica comune per aiutare le firme a sopravvivere all'inoltro.
    

---

## Tag di esempio dell'intestazione DKIM

Ecco una ripartizione dei tag che si trovano in un'intestazione `DKIM-Signature`:

- `v=` Versione di DKIM (di solito `1`).
    
- `a=` Algoritmo di hashing/firma (es. `rsa-sha256`).
    
- `d=` Il dominio firmatario.
    
- `s=` Il selettore utilizzato per trovare la chiave.
    
- `c=` L'algoritmo/i di canonicalizzazione per intestazione/corpo (es. `relaxed/relaxed`).
    
- `h=` Un elenco delle intestazioni incluse nella firma.
    
- `bh=` L'hash del corpo canonicalizzato.
    
- `b=` La firma stessa.
    
- `t=` Timestamp della firma (secondi dal 1/1/1970).
    
- `x=` Timestamp di scadenza (opzionale).
    
- `i=` L'identità del firmatario (meno comune).