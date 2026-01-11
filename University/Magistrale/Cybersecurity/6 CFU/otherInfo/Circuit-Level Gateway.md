# Circuit-Level Gateway

**Tag:** #security #firewall #networking #livello4 #socks #definizioni

---

## 📝 Definizione
Un **Circuit-Level Gateway** è un tipo di [[Firewall]] che opera al **Livello 4 (Trasporto)** o **Livello 5 (Sessione)** del modello OSI.

A differenza del [[Packet Filtering]] (che controlla i singoli pacchetti) e dell'[[Application-Level Gateway]] (che controlla il contenuto dei dati), il Circuit-Level Gateway si concentra sulla validazione delle **sessioni TCP**.
Il suo compito principale è verificare che il "circuito" (la connessione) tra il client interno e il server esterno sia legittimo prima di permettere lo scambio di dati.

![[Pasted image 20260110203722.png]]

> [!abstract] Concetto Chiave: Il Garante della Connessione
> Immagina un centralinista manuale degli anni '50.
> 1. Tu chiami il centralino e dici: "Voglio parlare col numero X".
> 2. Il centralinista controlla se sei abilitato a fare chiamate esterne.
> 3. Se sì, chiama lui il numero X per te.
> 4. Quando X risponde, il centralinista collega i due cavi.
> 5. Da quel momento, il centralinista smette di ascoltare. Non gli importa cosa dite, gli importava solo che la chiamata fosse autorizzata.

---

## ⚙️ Funzionamento Tecnico
Il meccanismo chiave è il **TCP Handshake** (La stretta di mano).

1.  **Richiesta:** Il Client interno invia un pacchetto `SYN` (richiesta di connessione) al Gateway.
2.  **Validazione:** Il Gateway non inoltra subito il pacchetto. Controlla:
    * Indirizzo IP Sorgente/Destinazione.
    * Porta.
    * Orario (Time of Day).
    * Utente/Password (se richiesto).
3.  **Splicing (Giunzione):**
    * Se la richiesta è valida, il Gateway apre una **seconda connessione** separata verso il Server di destinazione.
    * Una volta che entrambe le connessioni sono stabilite, il Gateway le unisce ("splices") logicamente.
4.  **Relay (Inoltro Cieco):** Da questo momento in poi, il Gateway copia i dati da una connessione all'altra senza ispezionarne il contenuto (Payload).

---

## 🔌 Il Protocollo SOCKS
Il protocollo standard utilizzato dai Circuit-Level Gateway è **SOCKS** (Socket Secure).
* Un client (es. browser, FTP, Chat) deve essere "SOCKS-ified" (configurato o programmato) per parlare con questo tipo di firewall.
* Il client dice al server SOCKS: "Connettimi a Google.com sulla porta 80".

---

## ⚔️ Circuit vs Application vs Packet

| Caratteristica | Packet Filter (Stateless) | Circuit-Level Gateway | Application-Level Gateway |
| :--- | :--- | :--- | :--- |
| **Livello OSI** | 3 (Network) | 4/5 (Transport/Session) | 7 (Application) |
| **Controllo** | Intestazione IP (Mittente/Destinatario) | Handshake TCP (Validità Sessione) | Contenuto (Comandi, Dati, Virus) |
| **Performance** | ⭐⭐⭐ (Velocissimo) | ⭐⭐ (Medio) | ⭐ (Lento/Pesante) |
| **Sicurezza** | Bassa (Passa tutto se IP ok) | Media (Garantisce anonimato interno) | Alta (Blocca malware specifico) |
| **Trasparenza** | Totale | Richiede Client SOCKS | Richiede Proxy config |

---

## 🛡️ Vantaggi e Svantaggi

### ✅ Vantaggi
* **Mascheramento (NAT-like):** Il mondo esterno vede solo l'IP del Gateway, mai l'IP del client interno. Protegge la topologia della rete.
* **Velocità:** Una volta stabilita la connessione, i dati passano velocemente perché non vengono disassemblati e analizzati (niente Deep Packet Inspection).
* **Semplicità:** Un singolo gateway SOCKS può gestire protocolli diversi (HTTP, FTP, Telnet) senza bisogno di un modulo specifico per ognuno (a differenza dell'Application Gateway).

### ❌ Svantaggi
* **Cecità al Contenuto:** È il suo rischio maggiore. Se un hacker stabilisce una connessione TCP valida (es. porta 80), può farci passare dentro qualsiasi cosa (virus, exploit, comandi malevoli). Il Circuit Gateway vede solo "traffico passante".
* **Modifica Client:** Ogni software client deve supportare SOCKS o essere configurato per usarlo. Non è "trasparente" come un Packet Filter.

> [!warning] Security Note
> Oggi i Circuit-Level Gateway puri sono rari. Spesso questa funzionalità è integrata nei **Firewall Stateful Inspection** moderni o nei server **[[Proxy]]** ibridi che fanno sia controllo di circuito che controllo applicativo.