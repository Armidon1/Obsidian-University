# Proxy Server

**Tag:** #networking #server #sicurezza #privacy #definizioni

---

## 📝 Definizione
Un **Proxy Server** (o semplicemente "Proxy") è un server che agisce come intermediario tra un client (come il tuo computer) e un server di destinazione (come un sito web).

Il termine "Proxy" significa "delegato" o "procuratore": qualcuno che ha l'autorità di agire per conto di un altro.

> [!abstract] Concetto Chiave: L'Intermediario
> Se navighi direttamente, è come se andassi tu di persona a ritirare un pacco.
> Se usi un **Proxy**, mandi un fattorino a ritirare il pacco per te. Il mittente vede solo il fattorino, non te.

---

## ⚙️ Funzionamento e Livello OSI
Il Proxy opera generalmente al **Livello 7 (Applicazione)** del modello OSI, il che gli permette di "capire" e manipolare il traffico (es. HTTP, FTP, SMTP).

Il processo standard è:
1.  Il Client si connette al Proxy.
2.  Il Client richiede una risorsa (es. "Voglio vedere Google.com").
3.  Il Proxy valuta la richiesta (filtri, cache, policy).
4.  Il Proxy si connette al Server di destinazione **usando il proprio IP**.
5.  Il Proxy riceve la risposta e la gira al Client originale.

---

## 🗂️ Tipologie Principali

### 1. Forward Proxy (Il "Proxy Standard")
Si trova davanti al client.
* **Chi protegge:** Il Client (rete interna).
* **Funzione:** Permette agli utenti di una rete interna (LAN) di accedere a Internet.
* **Usi:** Superare restrizioni geografiche, anonimato (nasconde l'IP del client), filtraggio contenuti (bloccare Facebook in ufficio).

### 2. Reverse Proxy
Si trova davanti al server web.
* **Chi protegge:** Il Server (Web Farm).
* **Funzione:** Accetta le richieste da Internet e le smista ai server interni.
* **Usi:** [[Load Balancing]] (distribuire il carico), protezione dagli attacchi DDoS, terminazione SSL (gestisce lui la crittografia HTTPS alleggerendo il server vero).

### 3. Transparent Proxy
* **Funzione:** Intercetta il traffico senza che l'utente debba configurare nulla nel browser. Spesso usato dagli ISP o nelle grandi aziende per il caching (risparmio di banda).

---

## ⚔️ Differenze Chiave

| Caratteristica | Proxy | Gateway | VPN |
| :--- | :--- | :--- | :--- |
| **Livello Principale** | App (L7) | Vario (L3-L7) | Network (L3) |
| **Visibilità** | Nasconde l'IP (maschera) | Traduce protocolli | Cifra tutto il tunnel |
| **Focus** | Privacy/Controllo Contenuti | Interconnessione Reti | Sicurezza Canale/Accesso Remoto |
| **Configurazione** | Spesso richiede setup su ogni App | Trasparente (Router) | Setup di sistema (Scheda di rete virtuale) |

---

## 🛡️ Ruolo nella Sicurezza
Il Proxy è un componente critico in un'architettura [[Firewall]] (spesso coincide con l'[[Application-Level Gateway]]):

* **Content Filtering:** Può leggere il traffico e bloccare parole chiave, estensioni file (.exe) o malware prima che arrivino al client.
* **Caching:** Memorizza copie dei siti web visitati. Se un altro utente chiede la stessa pagina, il proxy la serve dalla memoria (velocità istantanea, traffico internet zero).
* **Log e Audit:** Registra esattamente *chi* ha visitato *cosa* e *quando*, fondamentale per la compliance aziendale.