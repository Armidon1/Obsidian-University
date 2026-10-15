# Bridge di Rete

**Tag:** #networking #hardware #livello2 #datalink #definizioni

---

## 📝 Definizione
Un **Bridge** (ponte) è un dispositivo di rete che opera al **Livello 2 (Data Link)** del modello OSI.
La sua funzione principale è collegare due o più segmenti di rete (LAN) separati, facendoli funzionare logicamente come un'unica rete.

A differenza di un semplice Repeater (o [[Hub]]), il Bridge è "intelligente": analizza i dati in transito e decide se farli passare o meno.

> [!abstract] Concetto Chiave: Il Vigile del Traffico
> Immagina un ponte che collega due isole (Segmento A e Segmento B).
> Il **Bridge** è un vigile posto sul ponte che legge la targa (MAC Address) di ogni macchina.
> * Se una macchina dell'Isola A vuole andare sull'Isola A, il vigile la ferma (non serve attraversare il ponte).
> * Se una macchina dell'Isola A vuole andare sull'Isola B, il vigile alza la sbarra e la fa passare.

---

## ⚙️ Funzionamento Tecnico
Il Bridge utilizza gli indirizzi fisici (**MAC Address**) per prendere decisioni.

1.  **Learning (Apprendimento):** Il Bridge ascolta tutto il traffico. Quando riceve un frame, guarda il *MAC Sorgente* e si segna in una tabella: "L'indirizzo X si trova sulla porta 1".
2.  **Filtering (Filtraggio):** Se il Bridge riceve un frame destinato a un utente che si trova *nello stesso segmento* del mittente, **scarta** il pacchetto. Questo riduce il traffico inutile.
3.  **Forwarding (Inoltro):** Se il destinatario si trova nell'altro segmento, il Bridge **inoltra** il frame.
4.  **Flooding:** Se il Bridge non conosce il destinatario, inoltra il frame ovunque (tranne che dalla porta di provenienza).

---

## ⚔️ Bridge vs Switch vs Router

| Caratteristica | Hub | Bridge | Switch | Router |
| :--- | :--- | :--- | :--- | :--- |
| **Livello OSI** | 1 (Fisico) | 2 (Data Link) | 2 (Data Link) | 3 (Network) |
| **Intelligenza** | Nessuna (ripete tutto) | Bassa (Software) | Alta (Hardware/ASIC) | Alta (IP Logic) |
| **Domini di Collisione** | 1 (Unico) | Separati per porta | Separati per porta | Separati per porta |
| **Domini di Broadcast** | 1 (Unico) | 1 (Unico) | 1 (Unico) | Separati |
| **Porte** | Molte | Solitamente 2 | Molte (Multi-port Bridge) | Varie |

> [!info] Nota Evolutiva
> Lo [[Switch]] moderno è tecnicamente un **Multi-port Bridge** ad alta velocità. Oggi il termine "Bridge" si usa raramente per l'hardware cablato, ma è comunissimo nel wireless (es. **Wi-Fi Bridge** per collegare due edifici).

---

## 🛡️ Vantaggi Principali
* **Segmentazione:** Divide una LAN congestionata in due segmenti più piccoli, riducendo le collisioni.
* **Estensione Fisica:** Permette di superare i limiti di lunghezza dei cavi (es. unendo due cavi Ethernet lunghi).
* **Integrazione Media:** Può collegare mezzi fisici diversi (es. unire una rete **Ethernet** cablata con una rete **Wi-Fi**, agendo da ponte tra onde radio e cavo).