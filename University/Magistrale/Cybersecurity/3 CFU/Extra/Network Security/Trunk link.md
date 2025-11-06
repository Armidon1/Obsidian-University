Quando si parla di **"Trunk Link per la segmentazione"** in combinazione con un **"Router"**, è molto probabile che ci si riferisca a una configurazione specifica chiamata **"Router-on-a-Stick" (ROAS)**.

È meno comune definire "trunk" un link standard tra due router (quello è tipicamente un link "routed" o di Livello 3). Un trunk (basato su standard IEEE 802.1Q) è quasi sempre un link di Livello 2 che trasporta il traffico di **multiple VLAN** (Virtual LAN).

Ecco la scomposizione esatta.

### Cos'è il "Router-on-a-Stick"?

In breve, è una tecnica in cui **un singolo link fisico** tra uno switch e un router viene utilizzato per trasportare il traffico di _più_ VLAN (e quindi di più sottoreti IP).

1. **Lo Switch (Livello 2):** Lo switch gestisce le VLAN (es. VLAN 10 per gli "Utenti" e VLAN 20 per i "Server"). La porta dello switch che si collega al router è configurata come **Trunk Link**. Questo significa che invia i frame Ethernet "etichettati" (tagged) con il loro ID VLAN (10 o 20).
    
2. **Il Router (Livello 3):** Il router riceve questo flusso di traffico "taggato" sulla sua singola interfaccia fisica. Su questa interfaccia, l'ingegnere crea delle **sub-interfacce virtuali**, una per ogni VLAN (es. `GigabitEthernet0/1.10` per VLAN 10 e `GigabitEthernet0/1.20` per VLAN 20).
    
3. **L'Instradamento:** Ogni sub-interfaccia viene configurata con un indirizzo IP e agisce come **default gateway** per la sua specifica sottorete/VLAN.
    

![Immagine di Router-on-a-Stick network diagram](https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcRRaODtkRGhUGmaYyBYlil3A7BDpXXN57JRGIrAfoSTZ4J6lKCY7GXJBEpVdN0DbPYNHhrx19Blsm4dkwekQN-WTT-7yhH8jkjMn6y1SFBwdCPS1f4)

Shutterstock

Quando un PC nella VLAN 10 vuole comunicare con un server nella VLAN 20, accade questo:

1. Il PC invia il pacchetto al suo gateway (la sub-interfaccia .10 del router).
    
2. Il traffico viaggia sullo switch, viene "taggato" come VLAN 10 e inviato sul trunk al router.
    
3. Il router riceve il pacchetto sulla sub-interfaccia .10.
    
4. Il router _prende una decisione di routing_ e capisce che la destinazione è nella rete della sub-interfaccia .20.
    
5. Il router "ri-tagga" il pacchetto per la VLAN 20 e lo invia _indietro_ sullo stesso trunk link allo switch.
    
6. Lo switch riceve il pacchetto taggato VLAN 20 e lo inoltra alla porta corretta del server.
    

---

### 🛡️ Perché è Fondamentale per la Cybersecurity?

Questa configurazione è la base della **segmentazione della rete** e il tuo pane quotidiano in ambito cybersecurity. Il router (o, più modernamente, un firewall o uno switch L3) che gestisce questo traffico è il tuo **punto di controllo (chokepoint)**.

1. **Isolamento (Isolation):** L'obiettivo principale. Le VLAN separano i domini di broadcast (Livello 2). Senza un router, la VLAN 10 e la VLAN 20 sono _completamente isolate_. Non possono comunicare. Questo significa che un attacco (es. ARP spoofing) o un malware (es. un worm) che si diffonde nella VLAN "Utenti" non può raggiungere automaticamente la VLAN "Server".
    
2. **Controllo degli Accessi (Access Control):** Il router è il "doganiere". Poiché _tutto_ il traffico che vuole passare da una VLAN all'altra (traffico _inter-VLAN_) deve obbligatoriamente passare attraverso il router, è il punto perfetto per applicare le **Access Control Lists (ACL)** o le regole del firewall.
    
    - **Esempio:** Puoi creare una regola che dice: "Permetti alla VLAN 10 di parlare con la VLAN 20 solo sulla porta TCP 443 (HTTPS), e blocca tutto il resto (come RDP o SSH)".
        
3. **Riduzione della Superficie d'Attacco:** Segmentando la rete (es. Utenti, Server, Ospiti, IoT), limiti il "blast radius". Se un aggressore compromette un PC "Utente", la sua visibilità e capacità di movimento laterale (lateral movement) sono confinate a quella singola VLAN. Non può fare una scansione di rete e trovare i tuoi domain controller, a meno che tu non glielo permetta esplicitamente tramite una regola sul router.
    
4. **Monitoraggio e Ispezione:** Essendo un "collo di bottiglia" obbligato, il router è il luogo ideale per analizzare il traffico inter-VLAN. Puoi abilitare il logging, inviare i flussi di dati (es. NetFlow) a un SIEM o persino inoltrare il traffico a un **IDS/IPS (Intrusion Detection/Prevention System)** per un'ispezione approfondita (Deep Packet Inspection).
    

---

### Alternativa Moderna: Lo Switch Multistrato (L3)

Il "Router-on-a-Stick" è un concetto didattico fondamentale, ma ha un collo di bottiglia: tutto il traffico (anche tra due VLAN sullo stesso switch) deve salire al router e tornare giù.

Nelle reti moderne, questa funzione di routing tra VLAN viene spesso eseguita da uno **Switch Multistrato (Layer 3 Switch)**.

- Invece di sub-interfacce su un router esterno, si creano **Interfacce Virtuali dello Switch (SVI)** per ogni VLAN.
    
- Lo switch esegue il routing tra le SVI internamente, a velocità hardware (molto più veloce).
    
- Dal punto di vista della **cybersecurity, il principio è identico**: lo switch L3 diventa il tuo punto di controllo dove applichi le ACL (spesso chiamate VACL o RACL) per filtrare il traffico tra i segmenti di rete.
    

Spero sia chiaro! Ti interessa approfondire come si configurano le ACL per questo tipo di segmentazione?