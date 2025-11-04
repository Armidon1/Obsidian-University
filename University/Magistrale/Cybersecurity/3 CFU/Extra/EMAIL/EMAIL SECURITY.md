# Email Security
## Panoramica

Questa sezione introduce i concetti fondamentali dell'architettura e della sicurezza della posta elettronica.

### Il Sistema E-Mail su Internet

- **Architettura e funzionamento di base**
    
- **Protocolli:** [[SMTP]], [[POP]], [[IMAP]]
    
- **Estensioni:** [[MIME]]
    
- **Minacce e-mail** ([[Spoofing]], [[Phishing]], [[Spam]])
    
- **Sicurezza dell'infrastruttura:** [[SPF]], [[DKIM]], [[ARC]], [[DMARC]]
    
    - Questi meccanismi proteggono il _transito_ dei messaggi e l'autenticazione del server (server-to-server).
        
- **Sicurezza end-to-end:** [[PGP]], [[S-MIME|S/MIME]]
    
    - Questi meccanismi proteggono il _contenuto_ del messaggio per garantire la privacy e l'autenticazione dell'utente (user-to-user).
        

---

## Il Sistema Email

L'e-mail è un metodo per scambiare messaggi digitali da un autore a uno o più destinatari, operando su Internet o reti intranet.

- È uno dei **servizi Internet più antichi** (attivo dal 1971).
    
- Il **primo messaggio:** Inviato da _Ray Tomlinson_, che ha introdotto l'uso della notazione `utente@dominio` per l'indirizzamento.
    
- Si basa su un modello **store-and-forward**: i server accettano, inoltrano, archiviano e consegnano i messaggi.
    
- Questo modello è **asincrono**: gli utenti non devono essere online contemporaneamente per comunicare. I server di posta sono progettati per ritentare la consegna in caso di fallimento temporaneo, rendendo il sistema resiliente.
    
- Il funzionamento di base è descritto nel documento **RFC 5598**.
    

Sebbene non tutto Internet sia formalmente basato su standard, in pratica lo è. Le RFC (Request for Comments) contengono le specifiche per tutti i protocolli utilizzati. L'RFC 5598 descrive l'architettura di base del sistema e-mail. Questi design, sebbene semplici, si sono dimostrati incredibilmente efficaci e scalabili.

---

## Architettura E-Mail di Internet

![[Pasted image 20251028131532.png]]

L'architettura è definita dalla **RFC 5598 (2009)**.

**Componenti Chiave:**

- **MUA (Message User Agent)** — Il client di posta elettronica dell'utente (es. Outlook, Gmail, Thunderbird).
    
- **MSA (Mail Submission Agent)** — Accetta la posta dal MUA, controlla la formattazione e la policy, e la inoltra al MTA. È il primo punto di ingresso nel sistema.
    
- **MTA (Mail Transfer Agent)** — Il "postino" di Internet. Trasferisce la posta tra diversi server.
    
- **MDA (Mail Delivery Agent)** — Riceve la posta dall'MTA e la consegna nella casella di posta locale del destinatario.
    
- **MS (Message Store)** — Il database o file system dove i messaggi vengono archiviati.
    
- **Protocolli:** [[SMTP]], [[POP]], [[IMAP]].
    

Il **MUA** è il client utilizzato dall'utente e si trova al di fuori del sistema di gestione dei messaggi (MHS - Message Handling System). L'**MSA** funge da server per il MUA, autenticandolo e prendendo in carico il messaggio.

Il cuore dell'MHS è l'**MTA**, che svolge la maggior parte del lavoro di smistamento. Si tratta di un sistema distribuito. Quando un MTA riceve un messaggio, deve solo capire quale altro server contattare per inoltrarlo, basandosi sul dominio del destinatario. Questo è reso possibile dalla risoluzione dei domini (DNS) e dal sistema di routing IP.

Il protocollo usato per il trasferimento tra server è **SMTP (Simple Mail Transfer Protocol)**. Una volta che il messaggio arriva al server finale, viene passato all'**MDA**. L'utente finale utilizzerà poi i protocolli **POP/IMAP** per accedere ai messaggi archiviati nel Message Store.

---

## Spiegazione dei Componenti

### [[MUA]] (Message User Agent)

Utilizzato dagli utenti finali per comporre, inviare, ricevere e gestire le e-mail. È l'interfaccia dell'utente con il sistema di posta.

### [[MSA]] (Mail Submission Agent)

- Riceve i messaggi in uscita dal MUA (spesso sulla porta 587).
    
- È il primo "guardiano": autentica l'utente e si assicura che il messaggio sia conforme agli standard (formato, policy anti-spam).
    
- Collabora con l'MTA per l'inoltro.
    

### [[MTA]] (Mail Transfer Agent)

- Trasferisce i messaggi tra server utilizzando **[[SMTP]]** (sulla porta 25).
    
- Agisce sia come **client** (quando invia un messaggio a un altro MTA) sia come **server** (quando riceve un messaggio).
    
- Utilizza i record **MX (Mail Exchange)** del DNS per trovare l'MTA del dominio destinatario.
    

### [[MDA]] (Mail Delivery Agent)

- Gestisce la consegna finale nella casella di posta (mailbox) del destinatario.
    
- Archivia il messaggio localmente nel Message Store.
    
- Può anche essere responsabile dell'applicazione di filtri lato server (es. filtri anti-spam, regole di smistamento in cartelle).
    

---

## Scambio di Email

**Protocollo:** [[SMTP]] (Simple Mail Transfer Protocol) (RFC 821 → RFC 5321)

- **Busta (Envelope):** Contiene i parametri di consegna usati da SMTP (es. `MAIL FROM:`, `RCPT TO:`). Questa "busta" è separata dall'intestazione e dal corpo del messaggio.
    
- **Indirizzo:** `utente@dominio`
    
    - `utente`: la parte locale (identifica una specifica mailbox).
        
    - `dominio`: il nome di dominio completo (FQDN) che identifica il server di posta.
        

Il dominio è la parte fondamentale per il routing. L'MTA controlla il dominio: se appartiene a se stesso, la consegna è **locale** (passa all'MDA). Altrimenti, la consegna è **remota** e deve inoltrare il messaggio a un altro MTA.

Tipicamente, l'invio di un'e-mail richiede solo due passaggi (MTA mittente -> MTA destinatario). Tuttavia, in strutture complesse (come grandi aziende), possono esserci più passaggi intermedi, con MTA che fungono da gateway centrali per il filtraggio o la registrazione.

#### Importanza della Busta vs. Intestazione

È cruciale capire la differenza tra la "busta" (i comandi SMTP) e le "intestazioni" (i campi `From:`, `To:` dentro il messaggio). SMTP non controlla che il `MAIL FROM:` della busta corrisponda al `From:` dell'intestazione. Questa discrepanza è la vulnerabilità fondamentale che permette lo **spoofing** (la falsificazione del mittente).

---

## Formato del Messaggio

Definito da **RFC 5322** (formato base) ed esteso da **[[MIME]]** (RFC 2045–2049).

### Struttura:

- **Intestazione (Header):** Campi strutturati (metadati) come `From`, `To`, `CC`, `Subject`, `Date`, ecc.
    
- **Corpo (Body):** Il contenuto principale del messaggio.
    
- Intestazione e corpo sono separati da una **linea vuota**.
    

### Il ruolo di MIME

Il formato originale (RFC 5322) permetteva solo testo ASCII a 7 bit.

MIME (Multipurpose Internet Mail Extensions) estende questo formato per permettere:

- Testo in set di caratteri diversi (es. UTF-8).
    
- Contenuto HTML (e-mail formattate).
    
- Allegati (immagini, documenti, file binari).
    

---

## Intestazioni (Header)

### Struttura

Ogni campo = _Nome_ + _Valore_, separati da due punti (`:`).

- I campi possono estendersi su più righe (le righe di continuazione devono iniziare con uno spazio o un tab).
    
- Limitati a **ASCII a 7 bit**. I caratteri non-ASCII (es. negli oggetti o nei nomi dei mittenti) devono essere codificati usando speciali sintassi MIME (es. Quoted-Printable o Base64).
    

### Identificatori

- **Message-ID:** Un identificatore univoco a livello globale per il messaggio (es. `<1234@example.com>`). Viene inserito dall'MSA o dal primo MTA.
    
- **ENVID:** Envelope Identifier per il tracciamento del messaggio (RFC 3885, RFC 3464).
    

### Campi Obbligatori

- `From:` Indirizzo del mittente (può essere falsificato).
    
- `To:` Destinatario/i.
    
- `Date:` Data e ora di invio (secondo il formato RFC 5322).
    
- `Message-ID:` Identificatore univoco.
    
- `Subject:` Oggetto del messaggio.
    

### Campi Opzionali

- `Cc:` (Carbon Copy) Destinatari in copia.
    
- `Bcc:` (Blind Carbon Copy) Destinatari in copia nascosta. Questi indirizzi sono presenti nella "busta" (come `RCPT TO:`) ma vengono rimossi dalle intestazioni prima della consegna finale, per renderli invisibili agli altri destinatari.
    
- `Reply-To:` Indirizzo alternativo per la risposta.
    
- `In-Reply-To:` Message-ID del messaggio a cui si sta rispondendo.
    
- `References:` Usato per raggruppare le conversazioni (threading).
    
- `Sender:` Usato quando chi invia (`From:`) è diverso da chi spedisce materialmente.
    
- `Return-Path:` Aggiunto dall'MDA finale, contiene l'indirizzo della "busta" (`MAIL FROM:`) ed è usato per i messaggi di errore (bounce).
    
- `Received:` Aggiunto da _ogni_ server (MTA) lungo il percorso di consegna.
    

Vedi [[EMAIL - Difference between receivedFrom and ReturnPath||la differenza tra Received e Return Path]].

### Esempio di intestazione

From: Michela Cellamare <michela.cellamare@uniroma1.it>

Date: ...

Come si vede, un'intestazione contiene più righe `Nome: Valore`.

Possono esserci anche intestazioni opzionali specifiche per certi provider (es. intestazioni `X-Outlook-...` o `X-Google-...`). Se un provider riceve un'intestazione che non riconosce, la ignora.

La catena di intestazioni `Received` è estremamente importante per il _debugging_ e la _forensics_, poiché traccia la cronologia dei salti che l'e-mail ha fatto tra i server. Ogni volta che un messaggio arriva a un server, questo _può_ alterare il contenuto (es. aggiungendo un disclaimer anti-virus), e questo può avere impatti sulla sicurezza (come vedremo con DKIM).

---

## Trasmissione delle Email

- **[[MUA]] → [[MSA]]:** Utilizza [[SMTP]] (sulla porta 587 o 465) per l'invio.
    
- **[[MUA]]→ Server (Ricezione):**
    
    - **[[POP]] (Post Office Protocol):** Modello "offline". Scarica le email dal server (solitamente cancellandole).
        
    - **[[IMAP]] (Internet Message Access Protocol):** Modello "online". Sincronizza le email, che restano sul server. È il protocollo moderno, usato per accedere alla stessa mailbox da più dispositivi.
        
- **Sistemi Proprietari:** Soluzioni come Microsoft Exchange o Lotus Notes usavano (o usano ancora) protocolli proprietari per la comunicazione MUA-Server, sebbene supportino anche IMAP/SMTP.
    

---

## Panoramica Operativa

![[Pasted image 20251028131610.png]]

1. **Composizione (MUA):** Alice compone un messaggio usando il suo MUA, inserisce l'indirizzo e-mail del destinatario e preme "invia".
    
2. **Invio (Submission):** Il MUA formatta il messaggio e usa una variante di SMTP (Submission Protocol, RFC 6409) per inviarlo all'MSA locale (es. smtp.a.org).
    
3. **Risoluzione DNS (MSA/MTA):** L'MSA (o l'MTA locale) analizza l'indirizzo del destinatario (b.org), interroga il DNS per i **record MX** (Mail Exchange) di b.org.
    
4. **Trasferimento (MTA):** Il server DNS risponde con l'host del server di posta di b.org (es. mx.b.org). L'MTA di Alice (smtp.a.org) si collega all'MTA di Bob (mx.b.org) e gli invia il messaggio via SMTP.
    
5. **Consegna (MDA):** L'MTA mx.b.org riceve il messaggio, riconosce che è per un utente locale, e passa il messaggio all'MDA, che lo archivia nella mailbox di Bob.
    
6. **Recupero (MUA):** Bob preme "controlla posta" sul suo MUA. Il MUA si connette al server (usando POP3 o IMAP4) e scarica/sincronizza il nuovo messaggio.

vedi anche [[SMTP]], [[ESMTP]], [[MIME]]

# Email Security examples
## Email Example
![[Pasted image 20251028151405.png]]
## Email Security Challenges

- [[Spam]]
    
- [[Phishing]]
    
- [[Malware-Based Attacks]] / [[Ransomware]]
    
- [[Spoofing]]
    
- [[Lack of traceability]]
    
- [[Data leakage]]
    
- [[Man-in-the-Middle (MITM)]]
    
- [[Business Email Compromise (BEC)]]
    
- [[Email bombing]]
    

## Simple Spoofing Examples
### Example 1
![[Pasted image 20251028151425.png]]![[Pasted image 20251028151436.png]]![[Pasted image 20251028151500.png]]
[[Spiegazione Phishing email1|Spiegazione qui]]
### Example 2
![[Pasted image 20251028151526.png]]![[Pasted image 20251028151536.png]]![[Pasted image 20251028151544.png]]![[Pasted image 20251028151559.png]]
[[Spiegazione Phishing email2|Spiegazione qui]]
### Example 3
![[Pasted image 20251028151619.png]]
[[Spiegazione Phishing email3|Spiegazione qui]]

Approfondisci i meccanismi proteggono il _transito_ dei messaggi e l'autenticazione del server (server-to-server). [[SPF]], [[DKIM]], [[DMARC]],[[ARC]]

## 🔒 SICUREZZA END-TO-END (E2E)

I protocolli discussi finora ([[SPF]], [[DKIM]], [[DMARC]], [[ARC]]) si concentrano sull'**autenticazione dell'infrastruttura**: provano che un _server_ sia autorizzato a inviare per conto di un _dominio_.

Tuttavia, **non** forniscono [[Confidentiality|Riservatezza]] per il contenuto del messaggio. Anche se la connessione tra i server di posta è crittografata (tramite STARTTLS), i server stessi (inclusi quelli del mittente e del destinatario) hanno accesso al messaggio in chiaro. Questo significa che il tuo provider di posta può leggere (o analizzare) le tue e-mail.

Per un sistema di e-mail _completamente_ affidabile, che protegga l'utente finale, vorremmo le seguenti garanzie:

- **Riservatezza ([[Confidentiality]])** del contenuto del messaggio: Il messaggio deve essere illeggibile per chiunque tranne che per il destinatario designato (crittografia E2E).
    
- **Autenticazione ([[Authentication]])** del mittente: Il destinatario deve essere certo dell'identità _dell'utente_ che ha inviato il messaggio (non solo del server).
    
- **Integrità ([[Integrity]])** del messaggio: Il messaggio non deve poter essere alterato durante il transito senza che il destinatario se ne accorga.
    
- **Non ripudio ([[Non-Repudiation]])**: Il mittente non deve poter negare di aver inviato il messaggio.
    

Questo livello superiore di sicurezza, che protegge il messaggio "da un capo all'altro" (da utente a utente), si ottiene utilizzando standard di crittografia end-to-end come **[[PGP]] (Pretty Good Privacy)** e **[[S-MIME|S/MIME]]**.

--- 
Approfondisci i meccanismi che proteggono il _contenuto_ del messaggio per garantire la privacy e l'autenticazione dell'utente (user-to-user). [[PGP]] e [[S-MIME]]