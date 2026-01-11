# DMZ (Demilitarized Zone)

**Tag:** #security #networking #architecture #firewall #definizioni

---

## 📝 Definizione
La **DMZ** (Zona Demilitarizzata) è una sottorete fisica o logica che separa la rete interna sicura (LAN/Intranet) da una rete esterna non sicura (Internet).

Agisce come una "zona cuscinetto" (Buffer Zone). I servizi che devono essere accessibili dall'esterno vengono posizionati qui, mantenendo il resto dell'azienda al sicuro dietro un ulteriore livello di protezione.

> [!abstract] Concetto Chiave: La Terra di Nessuno
> Prende il nome dalla terminologia militare. È una striscia di terra neutra tra due fronti nemici.
> In informatica:
> * Se un hacker attacca il tuo sito web, entra nella DMZ.
> * Una volta lì, si trova isolato: non può "saltare" facilmente nella rete interna dove tieni i dati sensibili (Database, Progetti, Contabilità).

---

## ⚙️ Architetture Comuni

### 1. Three-Legged Firewall (Singolo Firewall)
Un unico [[Firewall]] con tre schede di rete (Interfacce):
1.  **Eth0 (WAN):** Verso Internet.
2.  **Eth1 (LAN):** Verso la rete interna.
3.  **Eth2 (DMZ):** Verso la zona server pubblici.
* **Pro:** Economico.
* **Contro:** Se il firewall cade o viene compromesso, tutta la rete è esposta (Single Point of Failure).

### 2. Screened Subnet (Doppio Firewall)
Questa è la configurazione più sicura (spesso richiesta negli esami di sicurezza).
* **Firewall Esterno (Front-End):** Protegge il perimetro. Fa entrare solo traffico web/mail verso la DMZ.
* **DMZ:** Sta in mezzo ai due firewall. Qui vivono i [[Bastion Host]].
* **Firewall Interno (Back-End):** Protegge la LAN. Blocca quasi tutto il traffico proveniente dalla DMZ.



---

## 🚦 Regole di Flusso del Traffico (Policy)

Affinché la DMZ funzioni, le regole del firewall devono essere rigorose:

| Origine | Destinazione | Azione | Motivo |
| :--- | :--- | :--- | :--- |
| **Internet** | **DMZ** | ✅ PERMETTI | Gli utenti devono vedere il sito web. |
| **Internet** | **LAN** | 🚫 BLOCCA | Nessuno da fuori tocca la rete interna. |
| **DMZ** | **LAN** | 🚫 BLOCCA | **Critico:** Se il server web è infetto, non deve infettare la LAN. |
| **LAN** | **DMZ** | ✅ PERMETTI | Gli amministratori devono aggiornare i server. |
| **LAN** | **Internet** | ✅ PERMETTI | I dipendenti possono navigare (spesso via [[Proxy]]). |

---

## 🏠 Chi abita nella DMZ?

Nella DMZ si mettono solo i servizi che **devono** essere esposti pubblicamente:
* **Web Server:** (HTTP/HTTPS).
* **Mail Server (Relay):** Per ricevere la posta.
* **DNS Pubblico:** Per risolvere i nomi del dominio.
* **[[Proxy]] / Gateway VoIP:** Per gestire le connessioni.

> [!danger] Chi NON deve stare nella DMZ
> Mai mettere qui i dati di valore.
> * **Database Server:** Devono stare nella LAN interna. Il Web Server in DMZ parlerà con il Database attraverso un buco molto stretto (pinhole) nel firewall interno.
> * **Domain Controller (AD):** Mai esporre le credenziali degli utenti.

---

## 🛡️ Vantaggi di Sicurezza
1.  **Containment (Contenimento):** Se un attaccante buca il server web, "vince" solo il controllo della macchina nella DMZ, non dell'intera azienda.
2.  **Sorveglianza:** È più facile monitorare il traffico sospetto in una zona piccola e controllata.
3.  **Segregazione:** Obbliga a separare la logica (Web App) dai dati (Database), migliorando l'architettura del software.