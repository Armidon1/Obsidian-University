# Application-Level Gateway (ALG)

**Tag:** #security #firewall #networking #livello7 #proxy #deep-inspection #definizioni

---

## 📝 Definizione
Un **Application-Level Gateway** (spesso chiamato semplicemente **Proxy Firewall**) è un dispositivo di sicurezza che opera al **Livello 7 (Applicazione)** del modello OSI.

A differenza del [[Packet Filtering]] (che guarda solo gli indirizzi IP e porte) e del [[Circuit-Level Gateway]] (che guarda la sessione TCP), l'ALG "capisce" perfettamente il protocollo utilizzato (HTTP, FTP, SMTP, DNS).
Non si limita a far passare i pacchetti, ma analizza il **contenuto** dei dati (payload) e i comandi specifici dell'applicazione.

![[Pasted image 20260110204005.png]]

> [!abstract] Concetto Chiave: L'Interprete Personale
> Immagina un diplomatico straniero (Client) che vuole consegnare una lettera al Re (Server).
> * **Packet Filter:** La guardia al cancello controlla solo il passaporto del diplomatico. Se è valido, lo fa passare con la busta chiusa.
> * **Application Gateway:** È un interprete che ferma il diplomatico, **apre la busta**, legge la lettera riga per riga, controlla che non ci siano insulti o minacce, la riscrive su carta intestata reale, e la consegna lui stesso al Re.

---

## ⚙️ Funzionamento Tecnico
L'ALG agisce come un intermediario completo ("Man-in-the-Middle" benevolo).

1.  **Intercettazione:** Il Client si connette al Gateway. La connessione si ferma lì.
2.  **Analisi Profonda (DPI):** Il Gateway decodifica i comandi dell'applicazione.
    * *Esempio FTP:* Capisce la differenza tra un comando `GET` (scarica) e `PUT` (carica).
    * *Esempio HTTP:* Può leggere l'URL richiesto, gli header e il corpo della pagina.
3.  **Applicazione Policy:** Controlla se quel comando specifico o quel contenuto sono permessi.
    * "Puoi scaricare file (`GET`), ma non puoi caricarli (`PUT`)."
    * "Non puoi scaricare file che finiscono con `.exe`."
4.  **Rigenerazione:** Se approvato, il Gateway apre una nuova connessione verso il Server di destinazione e invia la richiesta per conto del Client.

---

## 🛡️ Funzionalità Avanzate

### 1. Granularità Estrema
Poiché comprende il protocollo, può applicare regole impossibili per altri firewall:
* Bloccare comandi specifici (es. `DELETE` in un database).
* Filtrare contenuti (es. bloccare siti con la parola "gambling").
* Sanitizzare l'input (rimuovere codice malevolo nascosto in un PDF).

### 2. Autenticazione Utente
Può richiedere che l'utente umano si identifichi (Username/Password) prima di lasciar passare il traffico.
* *Vantaggio:* I log non mostrano solo "L'IP 192.168.1.50 ha visitato il sito X", ma "L'utente **Mario Rossi** ha visitato il sito X".

### 3. Caching
Può salvare copie locali dei dati richiesti frequentemente (come immagini o pagine web) per velocizzare la navigazione e risparmiare banda.

---

## ⚔️ ALG vs Packet Filter vs Circuit

| Caratteristica | Packet Filter | Circuit Gateway | Application Gateway |
| :--- | :--- | :--- | :--- |
| **Livello OSI** | 3 (Network) | 4/5 (Session) | 7 (Application) |
| **Cosa guarda** | IP e Porte | Handshake TCP | Comandi e Dati (Payload) |
| **Sicurezza** | Bassa | Media | **Massima** |
| **Performance** | Altissima | Alta | **Bassa** (Alto Overhead) |
| **Complessità** | Bassa | Media | Alta (Serve un proxy per ogni protocollo) |

---

## ⚠️ Svantaggi

1.  **Collo di Bottiglia (Performance):** Aprire ogni pacchetto e leggerne il contenuto richiede molta CPU. Gli ALG sono molto più lenti dei Packet Filter e possono rallentare la rete.
2.  **Specificità:** Hai bisogno di un modulo software diverso per ogni protocollo.
    * Se inventano un nuovo protocollo domani, il tuo ALG non lo farà passare finché il venditore non rilascia un aggiornamento ("Proxy specifico").
3.  **Configurazione:** Spesso richiede configurazione esplicita sui client (es. impostare il proxy nel browser), a meno che non sia configurato in modalità "Transparent".

> [!info] Contesto Architetturale
> L'Application-Level Gateway risiede tipicamente su un **[[Bastion Host]]** nella **[[DMZ]]**. È la scelta obbligata per proteggere servizi pubblici critici come Web Server o Mail Server.