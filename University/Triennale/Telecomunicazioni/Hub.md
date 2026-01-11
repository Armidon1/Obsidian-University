# Hub di Rete

**Tag:** #networking #hardware #livello1 #fisico #obsoleto #definizioni

---

## 📝 Definizione
Un **Hub** (letteralmente "mozzo" o "centro") è un dispositivo di rete molto semplice che opera al **Livello 1 (Fisico)** del modello OSI.
La sua funzione è quella di collegare più computer in una [[LAN]], agendo come un punto di concentrazione delle connessioni.

Tecnicamente è definito come un **Multi-port Repeater** (Ripetitore multi-porta): il suo unico scopo è rigenerare il segnale elettrico.

> [!abstract] Concetto Chiave: Il "Megafono"
> L'Hub è come una persona con un megafono in una stanza affollata.
> Quando il Computer A vuole dire qualcosa al Computer B, l'Hub prende il messaggio e lo urla a **tutti** i presenti nella stanza.
> * Solo il Computer B ascolterà il messaggio (perché riconosce il suo nome/MAC).
> * Tutti gli altri computer devono zittirsi e ignorare il messaggio.

---

## ⚙️ Funzionamento Tecnico
L'Hub non ha alcuna "intelligenza". Non legge indirizzi IP né indirizzi MAC.

1.  **Ricezione:** Un segnale elettrico (dati) arriva su una porta.
2.  **Rigenerazione:** L'Hub ripulisce e amplifica il segnale elettrico.
3.  **Broadcasting (Flooding):** L'Hub invia lo stesso segnale su **tutte** le altre porte disponibili, tranne quella da cui è arrivato.

---

## ⚠️ Limiti e Problemi
A causa della sua natura "stupida", l'Hub introduce tre grossi problemi nelle reti moderne:

### 1. Dominio di Collisione Condiviso
Tutti i dispositivi collegati a un Hub fanno parte dello stesso **Dominio di Collisione**.
* Se due computer provano a trasmettere contemporaneamente, i segnali si scontrano (collisione) e i dati vengono distrutti.
* Tutti i dispositivi devono aspettare un tempo casuale e riprovare (protocollo CSMA/CD).
* *Risultato:* Più computer colleghi, più la rete diventa lenta.

### 2. Half-Duplex
L'Hub non permette di ricevere e trasmettere contemporaneamente. Funziona come un *Walkie-Talkie*: o parli, o ascolti.

### 3. Sicurezza (Sniffing)
Poiché l'Hub invia i dati di tutti a tutti, un utente malintenzionato collegato alla rete può usare un software come **Wireshark** per intercettare (sniffare) tutto il traffico, incluse password o email destinate ad altri, mettendo la scheda di rete in *Promiscuous Mode*.

---

## ⚔️ Hub vs Switch

| Caratteristica | Hub | Switch |
| :--- | :--- | :--- |
| **Livello OSI** | 1 (Fisico) | 2 (Data Link) |
| **Trasmissione** | Broadcast (a tutti) | Unicast (solo al destinatario) |
| **Banda** | Condivisa (divisa tra i PC) | Dedicata (piena per ogni porta) |
| **Modalità** | Half-Duplex | Full-Duplex |
| **Sicurezza** | Bassa (tutti sentono tutto) | Alta (isolamento porte) |
| **Stato Attuale** | **Obsoleto** | Standard |

> [!info] Utilizzo Moderno
> Oggi gli Hub non si usano più per costruire reti. Tuttavia, sono talvolta ricercati dagli analisti di sicurezza proprio per il loro "difetto": inserire un Hub tra un router e un server permette di collegare un laptop e analizzare tutto il traffico passante senza complesse configurazioni di Port Mirroring.