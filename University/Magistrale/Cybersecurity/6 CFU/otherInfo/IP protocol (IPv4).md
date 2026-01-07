# Protocollo IP (IPv4): Struttura dell'Header e Funzionamento

**Tags:** #ingegneria #reti #ip #ipv4 #header #layer3 #packet

## 1. Definizione e Ruolo

Il Protocollo IP (Internet Protocol) opera al Livello 3 (Rete) del modello OSI.

È un protocollo Connectionless (non c'è handshake prima di inviare dati) e Best-Effort (non garantisce la consegna, quello è compito del TCP).

La sua funzione principale è l'**instradamento (Routing)**: portare un pacchetto dalla sorgente alla destinazione attraverso una rete di router.

![[Pasted image 20260107165145.png]]

> [!abstract] Visual Analysis
> 
> What to look at: La larghezza dell'header è fissa a 32 bit (4 Byte). L'altezza minima è 20 Byte (senza opzioni).
> 
> Meaning: Ogni riga dello schema rappresenta una "word" di 32 bit processata dalla CPU del router.

---

## 2. Analisi dei Campi Critici

Analizziamo l'header riga per riga, collegandolo ai problemi di sicurezza e networking.

### A. Versione e Lunghezza (Row 1)

- **Version (4 bit):** Indica se è IPv4 (valore 4) o IPv6 (valore 6).
    
- **IHL (Header Length):** Quanto è lungo l'header? (Minimo 5, che significa $5 \times 32\text{ bit} = 20\text{ Byte}$).
    
- **Type of Service (ToS):** Usato per la QoS (Quality of Service), per dare priorità a certi pacchetti (es. VoIP).
    
- **Total Length (16 bit):** Dimensione totale del pacchetto (Header + Dati).
    
    - **Max size teorica:** $2^{16} - 1 = 65.535 \text{ Byte}$.
        

### B. Gestione della Frammentazione (Row 2)

Questa riga è cruciale per i problemi di **MTU** che abbiamo studiato.

- **Identification (16 bit):** Un ID univoco per raggruppare i frammenti di uno stesso pacchetto originale.
    
- **Flags (3 bit):**
    
    - bit 0: Riservato.
        
    - bit 1: **DF (Don't Fragment)**. Se settato a 1 e il pacchetto è troppo grande, il router lo scarta (usato per PMTU Discovery).
        
    - bit 2: **MF (More Fragments)**. "1" se seguono altri pezzi, "0" se è l'ultimo.
        
- **Fragment Offset (13 bit):** Indica la posizione esatta dei dati di questo frammento rispetto al pacchetto originale.
    

> [!failure] Common Pitfall
> 
> Attacchi di Frammentazione: Gli hacker possono manipolare l'Offset per sovrascrivere parti di memoria o eludere i firewall (che spesso controllano solo il primo frammento perché contiene le porte TCP).

### C. Vita e Protocollo (Row 3)

- **TTL (Time To Live - 8 bit):** Un contatore che viene **decrementato di 1** da ogni router che attraversa.
    
    - **Scopo:** Evitare che i pacchetti girino all'infinito in loop di routing. Quando arriva a 0, il pacchetto muore.
        
    - **Impatto su IPsec AH:** Poiché il TTL cambia ad ogni salto, è un **campo mutabile**. AH deve ignorarlo (metterlo a zero) per calcolare la firma, altrimenti l'hash cambierebbe ad ogni router.
        
- **Protocol (8 bit):** Dice al destinatario a chi consegnare il payload.
    
    - `6` = TCP
        
    - `17` = UDP
        
    - `50` = **ESP** (IPsec)
        
    - `51` = **AH** (IPsec)
        
- **Header Checksum (16 bit):** Controllo errore _solo_ sull'header (non sui dati). Anche questo cambia ad ogni salto (perché cambia il TTL).
    

### D. Indirizzamento (Row 4 & 5)

- **Source IP (32 bit):** Chi invia.
    
- **Destination IP (32 bit):** Chi deve ricevere.
    

> [!tip] Exam Focus
> 
> NAT vs IPsec: Il NAT (Network Address Translation) modifica il campo Source IP (e ricalcola il Checksum).
> 
> - **Conseguenza:** Se usi **AH**, la firma di integrità (che copre l'IP sorgente) non corrisponderà più. Il pacchetto verrà scartato. Questo è il motivo per cui AH è incompatibile con NAT.
>     

---

## 3. Matematica dell'Header

Le dimensioni sono fisse e vincolanti per il calcolo dell'overhead.

**Standard Header Size Calculation:**

$$\text{Header IPv4 Min} = 20 \text{ Byte}$$

**Address Space Calculation:**

$$\text{Max Indirizzi IPv4} = 2^{32} \approx 4.29 \text{ Miliardi}$$

(Oggi esauriti, motivo per cui usiamo il NAT o IPv6).
