# Switch di Rete

**Tag:** #networking #hardware #livello2 #datalink #lan #definizioni

---

## 📝 Definizione
Uno **Switch** (commutatore) è un dispositivo di rete intelligente che opera al **Livello 2 (Data Link)** del modello OSI.
Il suo scopo principale è collegare dispositivi (PC, stampanti, server) all'interno della stessa rete locale ([[LAN]]), gestendo il flusso dei dati in modo efficiente.

Tecnicamente, lo Switch è un **Multi-port Bridge** (Ponte multi-porta) realizzato in hardware (ASIC), capace di gestire centinaia di connessioni simultanee ad alta velocità.

> [!abstract] Concetto Chiave: Il Centralino Telefonico
> A differenza dell'[[Hub]] (che urla a tutti), lo Switch agisce come un centralinista privato.
> Quando il Computer A vuole parlare con il Computer B:
> 1. Lo Switch crea un collegamento diretto ed esclusivo ("circuito virtuale") tra la porta di A e la porta di B.
> 2. I due si scambiano dati alla massima velocità.
> 3. Gli altri computer (C, D, E) non sentono nulla e possono avere le loro conversazioni private contemporaneamente.

---

## ⚙️ Funzionamento Tecnico
Lo Switch basa le sue decisioni sugli indirizzi fisici (**MAC Address**).

1.  **Learning (Apprendimento):** Appena accendi la rete, lo Switch è "vuoto". Quando un PC trasmette, lo Switch legge il suo *MAC Sorgente* e si segna nella sua memoria (**CAM Table**): "Il MAC `AA:BB:CC` si trova sulla Porta 1".
2.  **Forwarding (Inoltro):** Quando arriva un pacchetto destinato a `AA:BB:CC`, lo Switch guarda la tabella, vede che corrisponde alla Porta 1, e invia il pacchetto *solo* lì.
3.  **Micro-segmentazione:** Ogni porta dello Switch è un **Dominio di Collisione** separato. Non ci sono scontri di dati (collisioni) come negli Hub.

---

## 🗂️ Tipologie Principali

### 1. Unmanaged Switch (Non Gestito)
* **Uso:** Casa o piccoli uffici.
* **Caratteristiche:** "Plug and Play". Non ha opzioni, non ha indirizzo IP, non si può configurare. Fa solo il suo lavoro di base.

### 2. Managed Switch (Gestito)
* **Uso:** Aziende, Data Center.
* **Caratteristiche:** Ha un indirizzo IP e un'interfaccia web/CLI. Permette di configurare **VLAN**, QoS (priorità al traffico voce), Port Mirroring (per diagnostica) e sicurezza delle porte.

### 3. Layer 3 Switch (Multilayer)
* **Ibrido:** Uno Switch che sa fare anche un po' di routing (Livello 3).
* **Funzione:** Può instradare pacchetti tra diverse [[VLAN]] alla velocità dell'hardware, senza dover passare per un [[Router]] lento.

---

## ⚔️ Switch vs Hub vs Router

| Caratteristica | Hub | Switch | Router |
| :--- | :--- | :--- | :--- |
| **Livello OSI** | 1 (Fisico) | 2 (Data Link) | 3 (Network) |
| **Banda** | Condivisa (es. 100Mb diviso 10 PC) | Dedicata (100Mb **per ogni** PC) | Dipende dall'uscita |
| **Modalità** | Half-Duplex (Parla O Ascolta) | Full-Duplex (Parla E Ascolta) | Full-Duplex |
| **Broadcast** | Sempre | Solo se necessario (ARP) | Blocca il broadcast |
| **Intelligenza** | Nessuna | MAC Address Table | Routing Table (IP) |



---

## 🛡️ Funzionalità di Sicurezza
In un ambiente aziendale, lo Switch è la prima linea di difesa (Network Access Control):

* **VLAN (Virtual LAN):** Permette di separare logicamente i dipartimenti (es. Amministrazione vs Ospiti) anche se usano gli stessi cavi fisici.
* **Port Security:** Puoi dire allo Switch: "Su questa presa a muro può collegarsi *solo* il PC con questo MAC Address". Se un hacker stacca il cavo e collega il suo laptop, la porta si spegne.
* **ARP Inspection:** Protegge dagli attacchi "Man in the Middle" all'interno della LAN.