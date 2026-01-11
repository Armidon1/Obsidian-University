# Bastion Host

**Tag:** #security #networking #server #dmz #hardening #definizioni

---

## 📝 Definizione
Un **Bastion Host** (letteralmente "Ospite Bastione" o roccaforte) è un computer specializzato, posizionato in una rete, progettato specificamente per **resistere agli attacchi**.

Di solito ospita una singola applicazione (come un [[Proxy Server]]) ed è l'unico nodo della rete esposto direttamente al pubblico (Internet).

> [!abstract] Concetto Chiave: Il Bunker
> In una fortificazione militare, il bastione è il punto più esterno e robusto, progettato per prendere i colpi di cannone.
> Nella rete, il **Bastion Host** è la macchina sacrificabile che si prende i colpi degli hacker. Se viene compromesso, è isolato in modo che l'attaccante non possa saltare facilmente alla rete interna (Intranet).

---

## ⚙️ Caratteristiche Fondamentali
Un Bastion Host non è un computer normale. Subisce un processo chiamato **Hardening** (Indurimento):

1.  **Minimalismo:** Viene installato *solo* il sistema operativo essenziale e l'applicazione necessaria (es. solo il server SSH o solo il Proxy Web).
2.  **Rimozione Utility:** Vengono rimossi compilatori (gcc), interpreti inutili e tool di sviluppo.
    * *Motivo:* Se un hacker entra, non deve trovare strumenti per compilare i suoi virus o exploit.
3.  **Patching Aggressivo:** È sempre aggiornato all'ultima versione di sicurezza.
4.  **Logging Estremo:** Registra ogni singola attività, spesso inviando i log immediatamente a un server esterno sicuro (per evitare che l'hacker li cancelli).

---

## 📍 Posizionamento nella Rete
Il Bastion Host non risiede quasi mai nella rete interna sicura.
Si trova tipicamente nella **[[DMZ]]** (Demilitarized Zone), una terra di nessuno tra il [[Firewall]] esterno e quello interno.

* **Schema Tipico:**
  `Internet` -> `Firewall Esterno` -> `Bastion Host (DMZ)` -> `Firewall Interno` -> `Rete Aziendale`

---

## 🗂️ Tipologie e Usi Comuni

### 1. Jump Server (Il Trampolino)
È l'uso più comune oggi per l'amministrazione di sistema.
* **Problema:** Gli amministratori devono gestire server interni via SSH, ma la porta 22 non può essere aperta su internet.
* **Soluzione:** Si apre la porta 22 *solo* verso il Bastion Host. L'admin si collega al Bastion, e da lì "salta" (effettua una seconda connessione) verso i server interni.

### 2. Proxy Server (Application Gateway)
Come visto negli esami (es. *bastion host acting as application-level proxy*), il Bastion gestisce il traffico Web, FTP o SMTP.
* Analizza il traffico a livello applicativo prima di passarlo dentro.

### 3. Honeypot (Talvolta)
A volte un Bastion Host è configurato apposta per sembrare vulnerabile e attirare gli attaccanti, per studiarne le mosse (ma questo è un ruolo più avanzato).

---

## ⚠️ Differenza Bastion vs Firewall
Sebbene lavorino insieme, sono diversi:

| Caratteristica | Firewall | Bastion Host |
| :--- | :--- | :--- |
| **Natura** | Dispositivo di rete (spesso appliance) | Server (Computer con OS) |
| **Azione** | Filtra pacchetti (Passa/Blocca) | Esegue applicazioni (Interpreta/Logga) |
| **Stato** | Trasparente (Router) | Punto finale (Termina la connessione) |
| **Obiettivo** | Controllo Accessi | Interfaccia sicura e Hardening |

> [!warning] Regola d'Oro
> Mai, per nessun motivo, usare la stessa macchina sia come Bastion Host (servizi pubblici) sia come File Server interno (dati privati). La segregazione dei compiti è vitale.