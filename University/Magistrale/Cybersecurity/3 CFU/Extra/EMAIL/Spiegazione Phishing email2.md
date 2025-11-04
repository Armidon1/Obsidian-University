Anche questo è un ottimo esempio, che utilizza tecniche diverse ma ugualmente efficaci.

Questo è un tentativo di **internal phishing** (o phishing interno), che sfrutta la fiducia che gli utenti hanno verso i mittenti dello stesso dominio.
![[Pasted image 20251028151526.png]]![[Pasted image 20251028151536.png]]![[Pasted image 20251028151544.png]]![[Pasted image 20251028151559.png]]

Analizziamo i punti sospetti evidenziati:

---

### 🚩 1. Impersonificazione del Mittente (Header `From`)

`From: "*SAPIENZA*" <gaia.fiore@uniroma1.it>`

- **Il Problema:** Come nel caso precedente, c'è un palese disallineamento. Il _display name_ è `"*SAPIENZA*"` (con tanto di asterischi per dare enfasi e un falso senso di ufficialità), ma l'indirizzo email è `gaia.fiore@uniroma1.it`, che sembra essere l'account di una persona specifica (studentessa, ricercatrice, ecc.).
    
- **Perché è Sospetto:** L'amministrazione centrale dell'università ("Sapienza") non invierebbe mai comunicazioni ufficiali dall'account personale di Gaia Fiore. Questo è un chiaro tentativo di **impersonificazione**. È probabile che:
    
    - L'account `gaia.fiore@uniroma1.it` sia stato **compromesso** (tramite un attacco precedente) e ora venga usato per inviare phishing ad altri utenti dello stesso ateneo.
        
    - Oppure, l'attaccante stia semplicemente modificando il "display name", ma in questo caso il server di invio (`mail-sor-f41.google.com`) appartiene a Google, che gestisce la posta di `uniroma1.it`. Questo rafforza l'ipotesi di un account compromesso.
        

---

### 🚩 2. Oggetto Allarmistico (Header `Subject`)

`Subject: QUESTA AZIONE È OBBLIGATORIA`

- **Il Problema:** L'oggetto crea un fortissimo e immediato **senso di urgenza**.
    
- **Perché è Sospetto:** Questa è una delle tattiche di ingegneria sociale più usate. Frasi come "Azione Obbligatoria", "Account Sospeso", "Scadenza Imminente" sono studiate per spingere l'utente ad agire d'impulso, senza analizzare criticamente l'email. Vogliono che tu clicchi subito per "risolvere il problema".
    

---

### 🚩 3. Uso di `Bcc` e `To: undisclosed-recipients`

- `To: undisclosed-recipients:;`
    
- `Bcc: leonardo.querzoni@uniroma1.it`
    
- **Il Problema:** L'email non è indirizzata direttamente a un destinatario nel campo `To`. Il destinatario reale (`leonardo.querzoni@...`) è nascosto in `Bcc` (Copia Carbone Nascosta) e il campo `To` è vuoto o riempito con un segnaposto.
    
- **Perché è Sospetto:** Questa è la tecnica standard per gli **invii massivi di spam e phishing**. L'attaccante invia la stessa email a centinaia o migliaia di persone contemporaneamente, e usa il `Bcc` per due motivi:
    
    1. Per non rivelare l'intera lista di vittime a ciascun destinatario.
        
    2. Per dare all'email un aspetto impersonale che, paradossalmente, può sembrare più "ufficiale" (come una notifica di sistema).
        

---

### 🚩 4. Il Payload (Header `Content-Type`)

`Content-Type: multipart/alternative;`

- **Il Problema:** Questo header indica che l'email contiene la stessa informazione in più formati, quasi sempre `text/plain` (testo semplice) e `text/html` (testo formattato).
    
- **Perché è Sospetto:** Di per sé non è malevolo (è lo standard per le email moderne). Tuttavia, in un contesto di phishing, il payload (l'azione dannosa) è quasi certamente nascosto nella versione `text/html`. L'attaccante inserirà un link malevolo che sarà "camuffato" da testo apparentemente legittimo (es. "Clicca qui per confermare il tuo account") o da un pulsante.
    

---

### 🚩 5. Dettaglio Tecnico (Headers `Return-Path`)

Si notano due header `Return-Path` (o "Envelope From") diversi associati a diversi passaggi (`Received`).

- `Return-Path: <gaia.fiore@uniroma1.it>` (associato all'invio iniziale)
    
- `Return-Path: <leonardo.querzoni+caf_querzoni=dis.uniroma1.it@uniroma1.it>` (associato alla consegna finale)
    

Questo indica che l'email inviata a `leonardo.querzoni@uniroma1.it` (che era in Bcc) è stata probabilmente **inoltrata** (automaticamente) a un altro indirizzo (`querzoni@dis.uniroma1.it`, come si vede in `Delivered-To`). Durante questo inoltro (gestito da un sistema `+caf...`), l'header `Return-Path` è stato riscritto. Questo è un dettaglio tecnico interessante sulla configurazione del server di posta, ma conferma che il target _originale_ dell'attacco era `leonardo.querzoni@uniroma1.it`.

---

### 🕵️‍♂️ Cosa è Successo (In Sintesi)

Un attaccante ha ottenuto l'accesso all'account `gaia.fiore@uniroma1.it` (o sta usando un servizio che gli permette di "sembrare" quell'account) e lo sta usando per inviare un'email di phishing **all'interno della stessa organizzazione**.

L'email impersona l'amministrazione centrale (`"*SAPIENZA*"`), usa un oggetto allarmistico per spaventare l'utente e lo nasconde in `Bcc` come parte di un invio massivo. L'obiettivo è costringere l'utente a cliccare un link malevolo (contenuto nella parte HTML dell'email) per rubare le sue credenziali di ateneo.

Dato che il mittente (`@uniroma1.it`) e i server di invio (Google) sono "legittimi" per quel dominio, questo tipo di attacco ha più probabilità di **superare i filtri anti-spam** (come SPF e DKIM), rendendolo particolarmente pericoloso.

Vuoi che analizziamo proprio questo? Ovvero, perché questa email, pur essendo palesemente un phishing, supererebbe un controllo SPF e DKIM?