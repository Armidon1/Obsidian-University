Si tratta di un classico e chiaro esempio di **tentativo di phishing**, che sfrutta alcune tecniche specifiche per ingannare il destinatario.

Analizziamo i punti che l'immagine evidenzia e perché sono sospetti, specialmente in un'ottica di email security.

![[Pasted image 20251028151425.png]]![[Pasted image 20251028151436.png]]![[Pasted image 20251028151500.png]]
---

### 🚩 1. Spoofing del Mittente (Header `From`)

Il segnale d'allarme più evidente è nel campo `From`:

`From: Polizia criminale <alessandro.lazzaro@uniroma1.it>`

- **Il Problema:** Il _display name_ (il nome visualizzato) è "Polizia criminale", un'entità autorevole e istituzionale. Tuttavia, l'indirizzo email effettivo è `<alessandro.lazzaro@uniroma1.it>`, che appartiene palesemente a un dominio universitario (`uniroma1.it`).
    
- **Perché è Sospetto:** È estremamente improbabile (praticamente impossibile) che un'istituzione come la Polizia utilizzi un account email universitario per comunicazioni ufficiali. Questo disallineamento è una tecnica di **spoofing** usata per dare un falso senso di autorità e urgenza, sperando che il destinatario reagisca al nome "Polizia criminale" senza controllare l'indirizzo email.
    

---

### 🚩 2. Discrepanza dei Destinatari (Header `To` vs `Bcc`)

Questo è l'aspetto tecnicamente più interessante dell'attacco:

- `To: polizia-cr@info.it`
    
- `Bcc: leonardo.querzoni@uniroma1.it` (che è il destinatario finale, come confermato da `Delivered-To`)
    
- **Il Problema:** L'email _sembra_ essere indirizzata a `polizia-cr@info.it`. Tuttavia, il destinatario reale (`leonardo.querzoni`) è stato inserito nel campo `Bcc` (Blind Carbon Copy, o Copia Carbone Nascosta).
    
- **Perché è Sospetto:** Questa è una tattica di **ingegneria sociale**. L'attaccante fa credere a Leonardo di aver ricevuto "per errore" (o in copia nascosta) una comunicazione sensibile diretta alla polizia. Questo crea un forte senso di curiosità o allarme ("Perché sono in Bcc su un'email alla polizia?"). L'obiettivo è spingere Leonardo ad aprire l'allegato (se presente, indicato da `Content-Type: multipart/mixed`) o a cliccare su un link per capire cosa stia succedendo.
    

---

### 🚩 3. Il Contesto (Subject e Altri Header)

- `Subject: RICHIESTA DI PROTEZIONE PERSONALE`: L'oggetto è allarmistico e, combinato con il mittente "Polizia criminale", è studiato per massimizzare l'urgenza e la preoccupazione.
    
- `In-Reply-To:`: La presenza di questo header suggerisce che l'email voglia spacciarsi per la _risposta_ a una conversazione esistente. Questo è spesso un tentativo di bypassare i filtri anti-spam, che sono più indulgenti con le email che sembrano far parte di un thread di conversazione (mostrando un `Message-ID` a cui si risponde) rispetto a email completamente nuove.
    

---

### 🕵️‍♂️ Cosa è Successo (In Sintesi)

Si tratta di un tentativo di **spear phishing** (un attacco mirato, dato che usa indirizzi dello stesso dominio `uniroma1.it`).

L'attaccante ha falsificato il nome del mittente (`From`) per impersonare la polizia e ha usato un trucco con i destinatari (`To` vs `Bcc`) per far credere al target reale (`leonardo.querzoni`) di essere stato segretamente messo in copia su una questione urgente e sensibile.

L'obiettivo finale è quasi certamente quello di indurre il destinatario a compiere un'azione dannosa, come aprire un allegato contenente malware o cliccare su un link che porta a una pagina di phishing per rubare credenziali.

Spero che questa analisi ti sia utile per i tuoi studi!

Posso aiutarti ad analizzare altri header di questa email, ad esempio i campi `Received` per tracciare (per quanto possibile) l'origine del server, o cosa significano SPF, DKIM e DMARC in questo contesto?