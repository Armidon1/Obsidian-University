# 📧 Componenti Chiave del Sistema Email

### 1. MUA (Message User Agent)
[[MUA]]
- **Definizione:** Il **client** che l'utente finale utilizza per leggere, comporre e inviare messaggi di posta elettronica. È l'interfaccia con l'utente.
    
- **Esempio:** **Microsoft Outlook**, **Mozilla Thunderbird**, l'app **Mail** di un iPhone, o l'interfaccia web di **Gmail**.
    

### 2. MSA (Mail Submission Agent)
[[MSA]]
- **Definizione:** Un server specializzato che **accetta la posta in uscita** dal MUA dell'utente. Il suo compito principale è convalidare il messaggio (ad esempio, controllare l'indirizzo del mittente) prima di inoltrarlo per la consegna.
    
- **Esempio:** Il componente del server che risponde alla richiesta di invio (solitamente sulla **porta 587** o **465**) del tuo client email e verifica che tu sia un utente autenticato.
    

### 3. MTA (Mail Transfer Agent)
[[MTA]]
- **Definizione:** L'agente responsabile del **trasferimento della posta** da un server all'altro. Utilizza il protocollo **SMTP** (Simple Mail Transfer Protocol) e interroga il DNS (Domain Name System) per trovare l'MTA del destinatario.
    
- **Esempio:** Programmi come **Sendmail**, **Postfix** o **Exim**, che gestiscono l'effettivo "salto" dell'email attraverso Internet tra i domini.
    

### 4. MDA (Mail Delivery Agent)
[[MDA]]
- **Definizione:** Il componente finale che **prende la posta** dall'MTA in arrivo e la **deposita nella casella di posta locale** corretta dell'utente finale sul server di destinazione.
    
- **Esempio:** Un programma lato server come **Dovecot** o **Procmail** che si occupa di filtrare la posta in arrivo e di scriverla nel formato corretto nel file o nella directory dell'utente.
    

### 5. MS (Message Store)
[[MS]]
- **Definizione:** L'archivio fisico o logico sul server di destinazione dove i messaggi di posta elettronica vengono **memorizzati** in attesa che l'utente li scarichi o li legga.
    
- **Esempio:** Una directory sul server contenente i file in formato **Maildir** o **mbox**, accessibile tramite protocolli come **IMAP** o **POP3**.
    

---
