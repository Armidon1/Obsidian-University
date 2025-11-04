![[Pasted image 20251028151619.png]]
Questo è un esempio eccellente di **distribuzione di malware** tramite email, un attacco leggermente diverso dai primi due.

L'elemento più sospetto in assoluto, in questo caso, è la **combinazione** di un allegato con specifici artefatti nel codice HTML.

---

### 🚩 1. Il Payload: L'Allegato (Header `Content-Type`)

`Content-Type: multipart/mixed;`

- **Il Problema:** Questo header non è di per sé sospetto (indica semplicemente che l'email ha più parti, come testo e un file), ma è il **vettore** principale per questo tipo di attacchi. Significa che l'email contiene un **allegato**.
    
- **Perché è Sospetto:** In un contesto di email non richiesta e con un oggetto generico, l'allegato è quasi certamente il payload malevolo (ad esempio un file `.zip`, `.html`, `.iso` o un documento Office con macro) che, se aperto, infetterà il computer della vittima.
    

---

### 🚩 2. Artefatti Tecnici (Codice HTML)

`<HTML xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vm"...>`

- **Il Problema:** L'header dell'HTML contiene _namespaces_ (xmlns) specifici di **Microsoft Office** (`...:office:office`) e VML (Vector Markup Language).
    
- **Perché è Sospetto:** Questo è un forte indicatore che l'email è stata generata programmaticamente, spesso da un **bot** o un **malware** (come un worm) che si propaga tramite email. Questi tool malevoli spesso usano le librerie di Microsoft Office presenti sul computer infetto per costruire e inviare i messaggi di posta. È un modo per "sembrare" un'email legittima inviata da Outlook o Word, ma per un analista di sicurezza è un campanello d'allarme.
    

---

### 🚩 3. Il Contesto (Mittente, Oggetto, Destinatario)

- `From: "Yan Ting" <yanting@united.com.sg>`
    
- `Subject: united scientific equipment`
    
- `Delivered-To: admin@malware-traffic-analysis.net`
    
- **Il Problema:** L'oggetto è molto generico e a tema "business" (`united scientific equipment`). Il mittente appartiene a un dominio aziendale (`united.com.sg`) che è probabilmente **compromesso** o **impersonato**.
    
- **Perché è Sospetto:** Questa è una tattica classica. L'attaccante usa un account compromesso per inviare malware ad altre aziende, sperando che l'oggetto "business-to-business" sembri legittimo.
    
- **La Prova Definitiva:** Il destinatario, `admin@malware-traffic-analysis.net`, non è una vittima casuale. Questo è un indirizzo email appartenente a un **noto sito di analisi malware** (malware-traffic-analysis.net). Questo significa che stiamo guardando un campione di malware che è stato intercettato e inviato a un analista di sicurezza o a una "honeypot" (trappola) per l'analisi.
    

---

### 🕵️‍♂️ Cosa è Successo (In Sintesi)

Si tratta di un'**email di malspam** (spam che veicola malware).

A differenza degli esempi precedenti, l'obiettivo qui non è (probabilmente) rubare le credenziali con l'ingegneria sociale (phishing), ma convincere l'utente ad **aprire l'allegato** (`multipart/mixed`).

L'attacco sfrutta un account (probabilmente compromesso) per inviare un'email dall'aspetto professionale ma generico, contenente un allegato infetto. Gli artefatti nel codice HTML (`xmlns:o...`) sono una "firma" tecnica che suggerisce la generazione automatizzata dell'email da parte di un malware.

Questo campione è stato catturato da un sistema di analisi, confermandone la natura malevola.

Vuoi forse vedere un'analisi dell'header `Received` per capire da dove è partita _realmente_ l'email?