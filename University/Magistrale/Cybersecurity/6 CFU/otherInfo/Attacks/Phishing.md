#  🎣 Phishing

### Definizione

Il **Phishing** è una forma di **frode informatica** che rientra nel campo dell'**Ingegneria Sociale**. L'obiettivo è **ingannare** un individuo (la vittima) per fargli divulgare informazioni sensibili, come credenziali di accesso (username e password), dettagli di carte di credito, o altre informazioni personali, **mascherando l'attaccante come un'entità fidata e legittima** in una comunicazione elettronica (principalmente via e-mail, ma anche tramite SMS o messaggistica istantanea).

Il termine, che evoca la parola "fishing" (pescare), allude all'atto di "pescare" informazioni riservate da un vasto bacino di utenti.

### Meccanismi Tecnici e Vettori di Attacco

Il Phishing sfrutta tre componenti tecnologiche primarie per avere successo:

#### 1. Falsificazione dell'Identità (Spoofing)

- **E-mail Spoofing:** L'attaccante falsifica l'indirizzo del mittente (il campo `From:` e il `Return-Path` nell'header SMTP) per far sembrare che il messaggio provenga da una fonte autorevole (es. la banca, il reparto IT, un CEO).
    
    - **Implicazione Tecnica:** Sfrutta la mancanza di autenticazione intrinseca dell'SMTP di base. La difesa primaria è l'implementazione dei protocolli **SPF, DKIM e DMARC** sul dominio del mittente.
        
- **Link Spoofing (URL Spoofing):** L'attaccante crea un URL che assomiglia a quello legittimo (es. `apple-id.com` invece di `apple.com`) o nasconde l'URL di destinazione sotto un testo di visualizzazione benigno (es. visualizza "Clicca qui per il sito della tua Banca" ma il link punta a un dominio malevolo).
    

#### 2. Vettori di Consegna

- **E-mail (Il Vettore Primario):** Il mezzo più comune. I messaggi sono spesso caratterizzati da un senso di **urgenza** ("Il tuo account sarà bloccato!") o di **opportunità** ("Hai vinto un premio!") per indurre azioni avventate.
    
- **Smishing (SMS Phishing):** L'attacco avviene tramite messaggi di testo SMS. Spesso utilizzato per ottenere credenziali bancarie o codici OTP (One-Time Password).
    
- **Vishing (Voice Phishing):** L'attaccante utilizza chiamate telefoniche, spesso con l'ausilio di _Voice over IP_ (VoIP) per falsificare il numero di telefono (spoofing del Caller ID), spacciandosi per un tecnico di supporto o un funzionario.
    

#### 3. Payload (La Pagina di Atterraggio)

- Una volta che la vittima clicca sul link nell'e-mail, viene reindirizzata a una **pagina di destinazione falsificata** (_landing page_), che è una copia esatta del sito web legittimo (es. la pagina di login di Microsoft 365).
    
- La vittima inserisce le proprie credenziali in questa pagina fasulla, che vengono **catturate istantaneamente dall'attaccante** prima che la pagina reindirizzi la vittima al sito reale (per non destare sospetti).
    

### Tipologie Specifiche di Phishing

Per un ingegnere informatico è cruciale distinguere tra i diversi livelli di sofisticazione del Phishing:

|**Tipologia**|**Descrizione**|**Obiettivo Principale**|
|---|---|---|
|**Bulk Phishing**|Attacco a larga scala e non mirato, inviato a milioni di destinatari (es. email generiche sulla Lotteria).|Basso tasso di successo, ma volume elevato.|
|**Spear Phishing**|Attacco **altamente mirato** contro un individuo specifico o un piccolo gruppo. Sfrutta informazioni personali raccolte in precedenza (es. nome del collega, progetto recente).|Aumento del tasso di successo grazie alla personalizzazione.|
|**Whaling**|Una forma di Spear Phishing mirata a "grandi pesci", cioè dirigenti di alto livello (**C-suite**) o figure aziendali critiche.|Ottenere l'accesso più privilegiato all'organizzazione (BEC - Business Email Compromise).|
|**Pharming**|Una forma più tecnica in cui l'utente viene reindirizzato a un sito malevolo **senza cliccare su un link**, attraverso la manipolazione del file `hosts` sul computer o il **DNS Cache Poisoning**.|Bypassa alcuni filtri e la consapevolezza dell'utente sui link.|

### Contromisure di Cybersecurity

La difesa contro il Phishing richiede la combinazione di tecnologia, processi e formazione:

1. **Tecnologia E-mail (Livello Dominio):** Implementazione rigorosa di **SPF, DKIM e DMARC** per prevenire l'Email Spoofing sul proprio dominio e per rifiutare messaggi non autenticati provenienti da altri domini.
    
2. **Filtri (Livello Gateway):** Utilizzo di **Gateway di Sicurezza E-mail (SEG)** e filtri antispam e anti-phishing basati su AI che analizzano il contenuto, gli header e la reputazione dell'URL per bloccare i messaggi prima che raggiungano l'utente.
    
3. **Sicurezza Account (Livello Utente):** **Implementazione obbligatoria dell'Autenticazione Multi-Fattore (MFA)**. Anche se l'attaccante ruba la password, non può accedere all'account senza il secondo fattore.
    
4. **Formazione e Simulazione (Livello Umano):** Addestramento regolare dei dipendenti per riconoscere i segnali di Phishing (grammatica scadente, indirizzo mittente incoerente, senso di urgenza, URL sospetti). Spesso si utilizzano **simulazioni di Phishing** per testare l'efficacia della formazione.
    

**Per gli ingegneri:** Sviluppare sistemi che non si basino unicamente sulla fiducia dell'utente, come l'uso di **chiavi crittografiche** o **token OAuth** anziché la digitazione diretta di password nei browser, e monitorare attivamente i log di autenticazione per rilevare tentativi di accesso anomali.