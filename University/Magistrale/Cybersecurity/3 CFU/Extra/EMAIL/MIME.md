# 📄 Multipurpose Internet Mail Extensions (MIME)

### Definizione

**MIME** (Multipurpose Internet Mail Extensions) è uno **standard Internet** che estende il formato dei messaggi di posta elettronica definiti originariamente da **RFC 822** (successivamente RFC 2822 e RFC 5322).

Il protocollo [[SMTP]] originale era limitato a trasmettere solo **testo ASCII a 7 bit**. MIME è stato sviluppato per superare queste limitazioni, consentendo ai messaggi di includere:

1. **Contenuto non-ASCII:** Caratteri internazionali (UTF-8, ecc.).
    
2. **Contenuto non-testuale:** Immagini, audio, video, documenti applicativi (es. PDF, DOCX).
    
3. **Corpi multipli:** Combinazione di diverse parti in un unico messaggio (es. testo semplice e HTML).
    
4. **Lunghezze di linea illimitate:** Non più limitato a 1000 caratteri per linea.
    

MIME non è un protocollo di trasporto (come SMTP), ma un **protocollo di formattazione del messaggio** che definisce come devono essere strutturati gli _header_ e il _corpo_ dell'e-mail per consentire ai client di posta (MUA) di interpretare correttamente il contenuto.

### Dettagli Tecnici e Cybersecurity per Ingegneri

MIME opera aggiungendo una serie di _header_ al messaggio di posta elettronica per descrivere la struttura e la codifica del contenuto.
![[Pasted image 20251028150024.png|800]]

|**Header MIME Chiave**|**Funzione**|**Esempio e Dettagli**|
|---|---|---|
|**`MIME-Version`**|Indica che il messaggio aderisce allo standard MIME (sempre 1.0).|`MIME-Version: 1.0`|
|**`Content-Type`**|Specifica il tipo di dati nel corpo del messaggio. È il componente più critico di MIME.|`Content-Type: text/plain; charset="utf-8"`|
|**`Content-Transfer-Encoding`**|Descrive il meccanismo utilizzato per codificare i dati non-ASCII/binari in una sequenza di byte ASCII a 7 bit compatibile con SMTP.|`Content-Transfer-Encoding: base64`|
|**`Content-Disposition`**|Suggerisce al client di posta come trattare la parte del messaggio (es. come allegato o inline).|`Content-Disposition: attachment; filename="documento.pdf"`|

#### 1. Tipi di Contenuto (Media Types)

Il cuore di MIME è il campo **`Content-Type`**, che utilizza una struttura _tipo/sottotipo_ (es. `text/html`). Alcuni tipi fondamentali includono:

- **`text`**: `text/plain`, `text/html`.
    
- **`image`**: `image/jpeg`, `image/png`.
    
- **`application`**: `application/pdf`, `application/octet-stream` (dati binari generici).
    
- **`multipart`**: Usato per aggregare diverse parti in un unico messaggio. Esempi chiave:
    
    - **`multipart/mixed`**: Per allegati indipendenti dal corpo principale.
        
    - **`multipart/alternative`**: Per offrire lo stesso contenuto in più formati (es. testo semplice e HTML), permettendo al MUA di scegliere il migliore.
        

#### 2. Codifiche di Trasferimento (Content-Transfer-Encoding)

Poiché SMTP gestisce solo testo ASCII a 7 bit, i dati binari (come le immagini) o i caratteri non-ASCII (come l'UTF-8) devono essere codificati prima della trasmissione. Le codifiche più comuni sono:

- **`base64`**: Converte dati binari (3 byte) in 4 caratteri ASCII. Aumenta la dimensione del messaggio di circa il 33%. Utilizzato per allegati binari.
    
- **`quoted-printable`**: Utilizzato principalmente per testo non-ASCII con molte sequenze di caratteri ASCII. È più efficiente di base64 per messaggi in gran parte testuali con pochi caratteri speciali.
    

### Implicazioni in Cybersecurity

MIME è essenziale per la funzionalità moderna dell'e-mail, ma è anche una fonte significativa di vulnerabilità e attacchi:

1. **Vettori di Attacco degli Allegati:**
    
    - L'uso del `Content-Type: application/...` permette il trasporto di file eseguibili o script che possono sfruttare vulnerabilità nel client di posta o nel sistema operativo quando aperti.
        
    - **MIMETypes Falsi:** Un attaccante può mascherare un file eseguibile (`.exe`) con un'estensione apparentemente innocua e specificare un _Content-Type_ fuorviante, anche se i client di posta moderni sono cauti in base all'estensione del file.
        
2. **Attacchi Polymorphic e Stealth (Multipart/Mixed):**
    
    - Gli aggressori possono utilizzare la struttura `multipart/mixed` per segmentare un _payload_ maligno in più parti, o nasconderlo, sperando di eludere la scansione dei _gateway_ di sicurezza o dei filtri antispam che non ricostruiscono correttamente il messaggio MIME completo.
        
3. **Vulnerabilità nell'Interpretazione (HTML):**
    
    - L'uso estensivo di `text/html` espone gli utenti a tecniche di phishing avanzate che utilizzano HTML, CSS e persino Javascript (se il MUA lo supporta, sebbene questo sia generalmente bloccato) per tracciare gli utenti (es. tramite _web bugs_) o ingannarli visivamente.
        
4. **Overhead e Efficienza:**
    
    - Sebbene non sia una minaccia di sicurezza diretta, la codifica MIME (specialmente `base64`) introduce un overhead che, se non gestito correttamente dai server, può contribuire a problemi di congestione della rete e di latenza.
        

Per un ingegnere informatico, è cruciale comprendere come i limiti MIME possono essere aggirati e come i _gateways_ di sicurezza (come i filtri antispam e gli scanner antivirus) devono **decodificare e ispezionare ricorsivamente** la struttura MIME completa di un messaggio (inclusi tutti i livelli di _multipart_) per rilevare il contenuto maligno.

## MIME – Multipurpose Internet Mail Extensions

Extends email to support:

- Non-ASCII text
    
- Attachments (images, audio, video, etc.)
    
- Multi-part messages
    
- Complex content types
    

### Key RFCs

RFC 822, 2045, 2046, 2047, 2048, 2049

### MIME Features

- Character set support (UTF-8, ISO-8859-1, etc.)
    
- Content type labeling
    
- Binary data encoding (Base64)
    
- Compound documents
    

### Common MIME Types
![[Pasted image 20251028150803.png]]

| File  | MIME Type       | Description     |
| ----- | --------------- | --------------- |
| .txt  | text/plain      | Plain text      |
| .html | text/html       | HTML document   |
| .jpg  | image/jpeg      | JPEG image      |
| .mp3  | audio/mpeg      | MP3 audio       |
| .zip  | application/zip | Compressed file |
|       |                 |                 |
## Content-transfering Encoding
![[Pasted image 20251028150826.png]]
## MIME Scheme
![[Pasted image 20251028150005.png]]

---
## Codifiche (Encodings)

Le codifiche sono meccanismi fondamentali per l'e-mail. Il protocollo SMTP originale (RFC 821) era stato progettato per trasportare solo testo ASCII a 7 bit. Per inviare contenuti a 8 bit, come immagini, file binari o testo con caratteri speciali (es. lettere accentate), questi contenuti devono essere codificati in un formato testuale a 7 bit sicuro per il trasporto.

### Base64

![[Pasted image 20251028150317.png]]

![[Pasted image 20251028150408.png]]

- Converte dati binari (come un file) in una rappresentazione testuale ASCII sicura.
    
- È la codifica standard per gli **allegati** e-mail.
    
- Funziona raggruppando **3 byte (24 bit) di input in 4 caratteri Base64** (ognuno dei quali rappresenta 6 bit).
    
- Utilizza un set di 64 caratteri (A-Z, a-z, 0-9, +, /) che sono sicuri per il trasporto.
    
- Utilizza il padding (riempimento) con il carattere `=` alla fine, se la lunghezza dei dati di input non è un multiplo esatto di 3 byte.
    
- Lo svantaggio è che il testo codificato in Base64 non è leggibile dall'uomo e aumenta la dimensione dei dati di circa il 33%.
    

### Quoted-Printable

![[Pasted image 20251028150434.png]]

- È un'alternativa a Base64, progettata specificamente per dati che sono **prevalentemente testo ASCII**, ma con alcuni caratteri a 8 bit (come le lettere accentate).
    
- Codifica solo i caratteri a 8 bit (non-ASCII) usando `=` seguito dal loro valore esadecimale a due cifre (es. `à` diventa `=E0`).
    
- Mantiene il testo **per lo più leggibile** dall'uomo, rendendolo ideale per il corpo del testo o per le intestazioni (come `Subject:`).
    

---

## Messaggi Multipart (Multipart Messages)

Grazie a MIME (Multipurpose Internet Mail Extensions), un singolo messaggio e-mail può contenere più parti. L'intestazione `Content-Type` viene impostata su `multipart/...` e viene definito un `boundary` (un confine), ovvero una stringa di testo unica che separa le varie parti.

- **`multipart/mixed`:** È il tipo usato per i messaggi con **allegati diversi**. Le parti sono indipendenti e vengono presentate all'utente in sequenza (es. un corpo di testo e un file PDF).
    
- **`multipart/digest`:** Un tipo specializzato usato per inviare una raccolta (un "riassunto") di più messaggi di testo.
    
- **`multipart/alternative`:** Estremamente comune. Indica che le parti sono **versioni alternative dello stesso contenuto**. Il client (MUA) sceglierà quale visualizzare in base alle sue capacità. L'uso tipico è per inviare un'email sia in `text/plain` (testo semplice) che in `text/html` (formattato).
    
- **`multipart/message`:** Usato per incapsulare un intero altro messaggio e-mail, inclusa la sua intestazione (es. quando si "inoltra come allegato").
    

---

## Tipi e Sottotipi MIME (MIME types/subtypes)

L'intestazione `Content-Type` è il cuore di MIME. Definisce il tipo di dati contenuti in una parte del messaggio, permettendo al client (MUA) di interpretarlo e visualizzarlo correttamente.

![[Pasted image 20251028150955.png]]

![[Pasted image 20251028151013.png]]

- La sua struttura è `tipo/sottotipo`.
    
- **Esempi comuni:**
    
    - `text/plain`: Testo semplice.
        
    - `text/html`: Testo formattato HTML.
        
    - `image/jpeg`: Un'immagine JPEG.
        
    - `application/pdf`: Un documento PDF.
        
    - `application/octet-stream`: Dati binari generici (usato quando il tipo specifico non è noto o per forzare il download di un file).
        

---

## Plain Text vs HTML

- Le e-mail in **HTML** permettono una formattazione ricca: link ipertestuali, immagini (spesso caricate da server esterni), stili CSS, tabelle, ecc.
    
- Per garantire la compatibilità con client che non supportano l'HTML, la _best practice_ è inviare i messaggi usando `multipart/alternative`, includendo un **fallback in testo semplice (plain text)**.
    
- L'intestazione per la parte HTML è: `Content-Type: text/html`.
    
- Sebbene migliori esteticamente, l'HTML introduce anche rischi di sicurezza:
    
    - **Phishing:** I link possono essere mascherati (il testo del link è diverso dalla destinazione reale).
        
    - **Tracciamento:** L'inclusione di immagini (spesso pixel 1x1 invisibili) caricate da un server esterno permette al mittente di sapere se e quando l'email è stata aperta (tracking pixel).
        

---

## Subaddressing (Indirizzamento secondario)

È una funzionalità del server di posta (MDA/MS) che permette di creare alias "al volo" per un singolo account, molto utili per la registrazione a servizi e il filtraggio automatico della posta in arrivo.

### Subaddressing Locale (“+”)

querzoni+mastercourses@diag.uniroma1.it

→ È un alias per querzoni@diag.uniroma1.it (RFC 5233)

Questa è la forma più comune, nota come **"plus addressing"** o "aliasing con il più". Il server di posta è configurato per ignorare il `+` e tutta la stringa che segue fino al simbolo `@`, consegnando il messaggio alla mailbox principale (`querzoni`). È estremamente utile per:

- **Filtrare:** Iscriversi a siti diversi con alias diversi (es. `utente+facebook@...`, `utente+ecommerce@...`) e creare regole nel proprio client per smistare automaticamente le email in cartelle diverse.
    
- **Tracciare:** Capire chi ha venduto o condiviso il proprio indirizzo e-mail. Se si inizia a ricevere spam sull'indirizzo `utente+sitoX@...`, è chiaro quale sito sia la fonte della fuga di dati.
    

### Subaddressing di Dominio

mastercourses@querzoni.diag.uniroma1.it

→ È un alias per querzoni@diag.uniroma1.it

Questa è una configurazione meno comune e più complessa, che richiede configurazioni specifiche sia del DNS (record MX) sia del server di posta per trattare i sottodomini come alias per un account specifico.