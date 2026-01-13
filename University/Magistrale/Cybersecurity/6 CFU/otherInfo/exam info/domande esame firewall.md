guardare sempre prima [[CS 6cfu - Domande esame]]

Certamente. Ecco l'analisi approfondita per **Firewall, Iptables e Architetture di Rete**, strutturata secondo l'**Opzione B** (Analisi approfondita basata sulle domande d'esame 2012-2025).

---

### **1. Iptables: Regole di Base e Policy**

La Domanda d'Esame:

"Scrivi le regole iptables per proteggere un server che offre solo SSH. La policy di default deve essere restrittiva." oppure "Supponi che una LAN usi whitelist come policy di default. Scrivi regole per permettere la comunicazione bidirezionale tra un host interno e uno esterno."

La Spiegazione (Il "Perché"):

Il firewall lavora su catene (INPUT, OUTPUT, FORWARD).

- **INPUT:** Traffico diretto _al_ firewall stesso.
    
- **OUTPUT:** Traffico generato _dal_ firewall.
    
- **FORWARD:** Traffico che _attraversa_ il firewall (es. da LAN a Internet).
    

La **Policy** stabilisce cosa fare se nessuna regola corrisponde.

- **Blacklisting (Default ACCEPT):** Accetto tutto tranne ciò che blocco esplicitamente. Facile ma insicuro.
    
- **Whitelisting (Default DROP):** Blocco tutto tranne ciò che permetto esplicitamente. Sicuro ma richiede di specificare ogni singolo flusso.
    

Cosa scrivere all'esame:

Per configurare una whitelist (Default DROP) e permettere SSH:

1. Imposta Policy:
    
    iptables -P INPUT DROP
    
    iptables -P OUTPUT DROP
    
    iptables -P FORWARD DROP
    
2. Permetti traffico SSH in ingresso:
    
    iptables -A INPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
    
3. Permetti traffico di risposta in uscita:
    
    iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT
    

---

### **2. Stateful Filtering (La Differenza Chiave)**

La Domanda d'Esame:

"Discuti le principali differenze fra il filtraggio stateless e stateful." oppure "Spiega il significato di -m state --state ESTABLISHED,RELATED".

**La Spiegazione (Il "Perché"):**

- **Stateless (Packet Filtering semplice):** Guarda ogni pacchetto isolatamente. "Questo pacchetto viene dall'IP X porta 80". Non sa se è una risposta a una mia richiesta o un attacco non sollecitato. Per far funzionare la navigazione web, dovrei aprire tutte le porte alte (>1023) in ingresso, esponendomi a rischi.
    
- **Stateful (Connection Tracking):** Ricorda lo stato della connessione. "Ho visto un pacchetto SYN uscire verso Google, quindi ora mi aspetto un SYN-ACK di ritorno".
    
    - `NEW`: Primo pacchetto di una connessione.
        
    - `ESTABLISHED`: Pacchetti successivi di una connessione già valida.
        
    - `RELATED`: Connessioni associate (es. errore ICMP o canale dati FTP).
        

**Cosa scrivere all'esame:**

- **Stateless:** Filtra basandosi solo sugli header del singolo pacchetto (IP, porte, flag). Veloce ma meno sicuro e difficile da configurare per protocolli complessi (FTP).
    
- **Stateful:** Mantiene una tabella di stato delle connessioni attive. Permette di creare regole intelligenti come "Accetta traffico in entrata SOLO se è una risposta a una connessione iniziata dall'interno" (`ESTABLISHED`).
    

---

### **3. Personal vs Network Firewall**

La Domanda d'Esame:

"Quando iptables è usato come personal firewall, c'è qualche caso in cui la catena FORWARD deve essere configurata?" oppure "Qual è la differenza tra personal firewall e perimeter firewall?"

**La Spiegazione (Il "Perché"):**

- **Personal Firewall:** Protegge il singolo computer su cui gira. Il traffico è diretto _al_ computer (`INPUT`) o esce _dal_ computer (`OUTPUT`).
    
    - _Eccezione:_ Se il computer fa da hotspot o gateway per altri (es. VM o condivisione connessione), allora instrada traffico e usa `FORWARD`. Altrimenti `FORWARD` è vuota/inutile.
        
- **Network Firewall (Perimeter):** Protegge un'intera rete. Il traffico principale passa _attraverso_ di esso (`FORWARD`).
    

**Cosa scrivere all'esame:**

- **Personal Firewall:** Protegge un singolo host. Usa principalmente le catene `INPUT` e `OUTPUT`. La catena `FORWARD` è rilevante solo se l'host agisce da router/gateway per altri dispositivi.
    
- **Network Firewall:** Protegge un perimetro di rete. Usa principalmente `FORWARD` per filtrare il traffico tra zone (es. LAN $\leftrightarrow$ Internet).
    

---

### **4. Regole "Panic" e Isolamento**

La Domanda d'Esame:

"L'host H è sotto attacco. Definisci regole di 'panico' per isolare l'host, permettendo solo all'amministratore di connettersi via console locale (o via SSH da un IP specifico)."

La Spiegazione (Il "Perché"):

In caso di emergenza, si vuole chiudere tutto (Drop All) eccetto una "porta di servizio" per risolvere il problema.

**Cosa scrivere all'esame:**

1. Blocco Totale:
    
    iptables -P INPUT DROP
    
    iptables -P OUTPUT DROP
    
    iptables -P FORWARD DROP (se fa da gateway)
    
2. Eccezione Amministratore (es. da 192.168.0.200):
    
    iptables -A INPUT -s 192.168.0.200 -p tcp --dport 22 -j ACCEPT
    
    iptables -A OUTPUT -d 192.168.0.200 -p tcp --sport 22 -j ACCEPT (o usare stateful ESTABLISHED).
    

---

### **5. DMZ e Bastion Host**

La Domanda d'Esame:

"Disegna uno schema per posizionare un firewall in una piccola organizzazione con Web/Mail server pubblici e una rete interna privata."

La Spiegazione (Il "Perché"):

Non puoi mettere i server pubblici nella LAN interna: se vengono bucati, l'hacker è dentro casa tua.

Non puoi metterli su Internet senza protezione.

La soluzione è la DMZ (Demilitarized Zone): una "terra di nessuno" separata.

- **Traffico Internet $\to$ DMZ:** Permesso (solo porte 80/25).
    
- **Traffico Internet $\to$ LAN:** BLOCCATO.
    
- **Traffico DMZ $\to$ LAN:** BLOCCATO (questo è cruciale!).
    
- **Traffico LAN $\to$ Internet/DMZ:** Permesso.
    

Cosa scrivere all'esame:

Bisogna disegnare un firewall con (almeno) 3 interfacce:

1. **WAN (Internet):** Insicura.
    
2. **LAN (Interna):** Sicura, contiene i PC dei dipendenti e DB interni.
    
3. DMZ (Servizi): Esposta, contiene Web Server e Mail Server.
    
    Il firewall deve bloccare le connessioni iniziate dalla DMZ verso la LAN per prevenire intrusioni in caso di compromissione del Bastion Host.
    

---

### **Sintesi Pratica per i Comandi (Cheat Sheet)**

- **Bloccare un IP:** `iptables -A INPUT -s 1.2.3.4 -j DROP`
    
- **Permettere SSH:** `-p tcp --dport 22 -j ACCEPT`
    
- **Stateful Return:** `-m state --state ESTABLISHED,RELATED -j ACCEPT` (Il "motore" che fa funzionare tutto).
    
- **Limitare Rate (DoS):** `-m limit --limit 5/s`
    
- **Interfaccia:** `-i eth0` (ingresso), `-o eth1` (uscita).
    
- **Multiport:** `-m multiport --dports 80,443` (comodo per raggruppare regole).