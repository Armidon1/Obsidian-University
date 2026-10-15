# Gateway (Telecomunicazioni)

**Tag:** #networking #telecomunicazioni #hardware #sicurezza #definizioni

---

## 📝 Definizione
Un **Gateway** (dall'inglese "porta d'accesso") è un nodo di rete che agisce come punto di ingresso o di uscita verso un'altra rete.

A differenza di un semplice [[Router]] (che si limita a instradare i pacchetti tra reti simili) o di un [[Bridge]] (che collega segmenti di rete a livello 2), la caratteristica distintiva del Gateway è la capacità di **tradurre protocolli diversi**.

> [!abstract] Concetto Chiave: Il "Traduttore"
> Se il Router è un postino che smista lettere senza aprirle, il **Gateway** è un interprete che apre la lettera, la traduce in un'altra lingua e la rimette in una busta nuova prima di consegnarla.

---

## ⚙️ Funzionamento e Livello OSI
Un Gateway può operare a qualsiasi livello del **modello OSI**, ma è più comunemente associato ai livelli superiori:
	
* **Livello 4 (Trasporto):** es. [[Circuit-Level Gateway]].
* **Livello 7 (Applicazione):** es. [[Application-Level Gateway]] o Proxy.

Il Gateway esegue una **conversione di protocollo** (Protocol Converter):
1.  Riceve i dati formattati per la Rete A.
2.  Rimuove l'incapsulamento del protocollo A.
3.  Interpreta e traduce i dati.
4.  Re-incapsula i dati nel protocollo della Rete B.

---

## 🗂️ Tipologie Principali

### 1. Application-Level Gateway (ALG) / Proxy
Opera a livello 7. Comprende la logica dell'applicazione (es. HTTP, FTP, SMTP).
* **Funzione:** Interrompe la connessione tra client e server esterno, rigenerandola.
* **Pro:** Altissima sicurezza (ispezione profonda dei pacchetti).
* **Contro:** Alto overhead (consumo risorse), richiede configurazione lato client o trasparenza complessa.
* *Vedi anche:* [[Bastion Host]], [[Proxy]].

### 2. Circuit-Level Gateway
Opera a livello 4 (Sessione/Trasporto). Crea un "circuito virtuale" tra interno ed esterno.
* **Funzione:** Valida la sessione (handshake TCP) senza ispezionare il payload dei dati (il contenuto del pacchetto).
* **Tecnologia:** Spesso usa il protocollo **SOCKS**.
* **Pro:** Più veloce dell'ALG.
* **Contro:** Meno sicuro dell'ALG (se il protocollo è lecito ma il contenuto è malevolo, passa).

### 3. Media Gateway (VoIP)
Fondamentale nelle telecomunicazioni moderne.
* **Funzione:** Converte il traffico voce dalle reti telefoniche tradizionali (PSTN/Analogico) in pacchetti digitali per reti IP (VoIP/SIP) e viceversa.

---

## ⚔️ Gateway vs Router

| Caratteristica | Router | Gateway |
| :--- | :--- | :--- |
| **Funzione primaria** | Instradamento (Routing) | Traduzione (Translation) |
| **Protocolli** | Collega reti con **stessi** protocolli (es. IP su IP) | Collega reti con **diversi** protocolli/architetture |
| **Livello OSI** | Livello 3 (Network) | Fino al Livello 7 (Application) |
| **Complessità** | Minore (legge indirizzi IP) | Maggiore (decodifica dati) |

---

## 🛡️ Ruolo nella Sicurezza
In un'architettura di sicurezza (es. [[Firewall]]), il Gateway è spesso posizionato nella **DMZ** o agisce come **Bastion Host**. È il punto di strozzatura (choke point) dove si applicano le policy di sicurezza più severe, poiché è l'unica porta di comunicazione tra una rete fidata (LAN) e una non fidata (Internet).