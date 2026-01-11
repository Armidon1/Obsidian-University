# Packet Filtering

**Tag:** #security #firewall #networking #livello3 #iptables #stateless #definizioni

---

## 📝 Definizione
Il **Packet Filtering** (Filtraggio dei Pacchetti) è la forma più fondamentale e comune di controllo di sicurezza di rete.
Opera principalmente ai livelli **3 (Rete)** e **4 (Trasporto)** del modello OSI.

Il suo compito è analizzare ogni singolo pacchetto di dati che attraversa il dispositivo (di solito un [[Router]] o un Firewall dedicato) e decidere se lasciarlo passare (**ACCEPT**) o bloccarlo (**DROP/REJECT**) basandosi su una lista di regole predefinite.

> [!abstract] Concetto Chiave: Il Buttafuori del Club
> Il Packet Filter è come un buttafuori all'ingresso di una discoteca che controlla solo la carta d'identità.
> * Guarda la tua foto (IP Sorgente).
> * Guarda la tua età (IP Destinazione/Porta).
> * Se sei sulla lista, entri.
> * **Nota Bene:** Non controlla se hai un coltello in tasca (Payload malevolo) o se sei già ubriaco, guarda solo i dati "anagrafici" esterni.

---

## ⚙️ Funzionamento Tecnico
Il filtro prende decisioni guardando **solo l'intestazione (Header)** del pacchetto IP e TCP/UDP. Non guarda mai il contenuto dei dati (Payload).

I criteri di filtraggio standard sono:
1.  **IP Sorgente:** Chi sta mandando il pacchetto?
2.  **IP Destinazione:** A chi è diretto?
3.  **Porta Sorgente/Destinazione:** Quale servizio sta chiedendo? (es. Porta 80 = Web).
4.  **Protocollo:** Che lingua parla? (TCP, UDP, ICMP).
5.  **Interfaccia:** Da quale cavo è arrivato? (eth0, eth1).

---

## 🗂️ Tipologie: Stateless vs Stateful

Questa è la distinzione più importante (spesso chiesta agli esami).

### 1. Stateless Packet Filtering (Statico)
È il metodo più vecchio e semplice.
* **Come funziona:** Analizza ogni pacchetto come un evento isolato, senza memoria del passato.
* **Il problema:** Non sa se un pacchetto è l'inizio di una conversazione o una risposta legittima.
    * *Esempio:* Se arriva un pacchetto "ACK" (conferma) dall'esterno, il filtro Stateless lo fa passare se la porta è aperta, anche se nessuno dall'interno aveva chiesto nulla. Questo permette tecniche di scansione come l'*ACK Scan*.

### 2. Stateful Packet Filtering (Dinamico)
È l'evoluzione moderna (es. [[iptables]] con modulo `conntrack`).
* **Come funziona:** Mantiene una **State Table** (Tabella di Stato) in memoria. Ricorda le connessioni attive.
* **Stati:**
    * **NEW:** Nuova connessione (controlla le regole di sicurezza).
    * **ESTABLISHED:** Risposta a una connessione già approvata (lascia passare subito).
    * **RELATED:** Errore o traffico correlato (es. FTP Data).
    * **INVALID:** Pacchetto che non c'entra nulla con le connessioni note (Blocca).

---

## ⚔️ Packet Filter vs Application Gateway

| Caratteristica | Packet Filter | Application Gateway ([[Proxy]]) |
| :--- | :--- | :--- |
| **Livello OSI** | 3/4 (Network/Transport) | 7 (Application) |
| **Velocità** | ⭐⭐⭐ (Altissima) | ⭐ (Bassa) |
| **Costo** | Basso (integrato nei router) | Alto (server dedicato) |
| **Visibilità** | Vede solo indirizzi e porte | Vede comandi e dati |
| **Trasparenza** | Trasparente all'utente | Spesso richiede config |
| **Sicurezza** | Protegge accesso alla rete | Protegge dai contenuti (Virus) |

---

## 🛡️ Vantaggi e Svantaggi

### ✅ Vantaggi
1.  **Prestazioni:** Elaborare solo gli header è velocissimo. Introduce pochissima latenza.
2.  **Indipendenza:** Funziona con qualsiasi applicazione (basta aprire la porta giusta), non serve un modulo specifico come per i Proxy.
3.  **Economicità:** È una funzionalità base di quasi tutti i router, anche quelli domestici.

### ❌ Svantaggi
1.  **Cecità al Contenuto:** Non può bloccare attacchi a livello applicativo (es. SQL Injection o Virus inviati via email). Se la porta 80 è aperta, il pacchetto passa, anche se contiene malware.
2.  **Gestione Complessa:** Le liste di regole (ACL) possono diventare lunghissime e difficili da mantenere. L'ordine delle regole è critico (First Match Wins).
3.  **IP Spoofing:** Se non configurato bene, può essere ingannato da pacchetti con indirizzi IP falsificati.

> [!info] Esempio Pratico
> Il comando `iptables` su Linux è l'esempio per eccellenza di Packet Filter.
> * Regola: `iptables -A INPUT -p tcp --dport 22 -s 192.168.1.5 -j ACCEPT`
> * Traduzione: "Se il protocollo è TCP, la porta è 22 e l'IP è 192.168.1.5 -> Lascia entrare. Non mi interessa cosa c'è dentro il pacchetto SSH."