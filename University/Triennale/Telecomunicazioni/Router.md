# Router

**Tag:** #networking #hardware #livello3 #network #internet #definizioni

---

## 📝 Definizione
Un **Router** (instradatore) è un dispositivo di rete intelligente che opera al **Livello 3 (Rete)** del modello OSI.
La sua funzione principale è collegare reti *diverse* tra loro (es. la tua LAN di casa con Internet) e decidere il percorso migliore per far viaggiare i pacchetti dati verso la loro destinazione finale.

Mentre lo [[Switch]] crea una rete, il **Router** collega le reti.

> [!abstract] Concetto Chiave: Il Navigatore GPS
> Immagina i pacchetti dati come automobili.
> Lo **Switch** è la strada locale che collega le case di uno stesso quartiere.
> Il **Router** è il navigatore GPS che ti dice: "Per andare a Parigi (destinazione remota), prendi l'autostrada A4, poi l'uscita X...".
> Se una strada è bloccata, il Router ricalcola il percorso e ti fa passare da un'altra parte.

---

## ⚙️ Funzionamento Tecnico
Il Router basa le sue decisioni sugli **Indirizzi IP** (Logici), non sui MAC Address (Fisici).

1.  **Analisi:** Quando arriva un pacchetto, il Router legge l'**IP di Destinazione**.
2.  **Routing Table:** Consulta la sua **Tabella di Routing** (una mappa interna).
    * La tabella può essere statica (scritta a mano) o dinamica (imparata parlando con altri router tramite protocolli come OSPF o BGP).
3.  **Decisione:**
    * Se la destinazione è nella rete locale, consegna il pacchetto direttamente.
    * Se la destinazione è remota (es. Google), invia il pacchetto al "Next Hop" (il prossimo router verso l'uscita), spesso usando il **Default Gateway**.

---

## 🗂️ Funzioni Chiave (Oltre l'instradamento)
I router moderni (soprattutto quelli domestici "All-in-One") fanno molto più che instradare:

* **NAT (Network Address Translation):** Permette a tutti i dispositivi di casa (con IP privati tipo `192.168.1.x`) di uscire su Internet usando un **unico** Indirizzo IP Pubblico. È essenziale per risparmiare indirizzi IPv4 e per sicurezza.
* **DHCP Server:** Assegna automaticamente gli indirizzi IP ai dispositivi che si collegano alla rete.
* **Firewalling:** Esegue un primo filtraggio dei pacchetti (ACL) per bloccare connessioni indesiderate dall'esterno.

---

## ⚔️ Router vs Switch vs Gateway

| Caratteristica | Switch | Router | Gateway |
| :--- | :--- | :--- | :--- |
| **Livello OSI** | 2 (Data Link) | 3 (Network) | Vario (fino al 7) |
| **Indirizzi** | MAC Address | IP Address | Protocolli vari |
| **Scopo** | Collegare **Dispositivi** (crea la LAN) | Collegare **Reti** (crea la WAN) | Tradurre **Linguaggi** |
| **Intelligenza** | Media (Switching veloce) | Alta (Algoritmi di percorso) | Altissima (Conversione dati) |
| **Broadcast** | Passa il broadcast | **Blocca** il broadcast | Dipende |

---

## 🛡️ Ruolo nella Sicurezza
Il Router è il "confine" del tuo castello (Rete).

* **ACL (Access Control Lists):** Regole che dicono "L'IP X non può parlare con l'IP Y".
* **Isolamento:** Poiché i router bloccano il traffico Broadcast, impediscono che problemi (o attacchi) di una rete locale si propaghino su tutta la rete aziendale o internet.
* **VPN Endpoint:** Molti router possono creare tunnel cifrati per permettere connessioni sicure da remoto.