# IPsec (Internet Protocol Security): Framework Completo

**Tags:** #ingegneria #reti #sicurezza #ipsec #vpn #ike #esp #ah #layer3

## 1. Definizione e Obiettivo

IPsec è una suite di protocolli standard (IETF) che offre sicurezza crittografica al Livello 3 (Rete) del modello OSI.

A differenza di SSL/TLS (che protegge la singola applicazione), IPsec protegge i pacchetti IP "alla radice", rendendo la sicurezza trasparente per le applicazioni superiori.

**Obiettivi della Triade CIA:**

- **Confidenzialità:** Cifratura dei dati (solo ESP).
    
- **Integrità:** Garanzia che il pacchetto non sia stato modificato (AH e ESP).
    
- **Autenticazione:** Verifica dell'identità della sorgente (Peer Authentication).
    
- **Anti-Replay:** Protezione contro la reiniezione di pacchetti catturati.
    
Per saperne di più, consulta la nota [[15 CS Lower Level - TLS and IPSec#IPsec Architettura, Security Associations e Database (SAD/SPD)|15 CS IPSec]]

---

## 2. Architettura: Modalità di Trasporto

IPsec può operare in due modalità, a seconda della topologia della rete.

### A. Transport Mode (End-to-End)

Protegge solo il **Payload** del pacchetto IP originale (es. il segmento TCP/UDP). L'header IP originale rimane in chiaro.

- **Scenario:** Comunicazione diretta Host-to-Host (es. Server Admin verso Server Database).
    
- **Struttura:** `[IP Header Orig] [IPsec Header] [Payload]`
    

### B. Tunnel Mode (Site-to-Site)

Protegge l'**Intero Pacchetto IP** originale. Il pacchetto viene cifrato e incapsulato dentro un _nuovo_ pacchetto IP.

- **Scenario:** VPN tra Gateway (es. Sede Roma <-> Sede Milano).
    
- **Struttura:** `[New IP Header] [IPsec Header] [Encrypted Orig IP + Payload]`
    

![[SCREEN_SLIDE_MODES]]

> [!abstract] Visual Analysis
> 
> Meaning:
> 
> - In **Transport Mode**, IPsec si inserisce _dentro_ il pacchetto esistente.
>     
> - In **Tunnel Mode**, il pacchetto originale diventa il _contenuto_ di una nuova busta.
>     

---

## 3. I Protocolli di Sicurezza (Data Plane)

### Authentication Header (AH)

Fornisce Integrità e Autenticazione, ma **NO Confidenzialità** (i dati viaggiano in chiaro).

- **Header:** Protocollo IP 51.
    
- **Problema Critico:** Autentica anche campi dell'header IP (come l'IP Sorgente). Se c'è un **NAT**, l'IP cambia, la firma si rompe e il pacchetto viene scartato.
    
- **Stato:** Oggi quasi in disuso a favore di ESP.
    

### Encapsulating Security Payload (ESP)

Fornisce Confidenzialità (Cifratura), Integrità e Autenticazione.

- **Header:** Protocollo IP 50.
    
- **Funzionamento:** Cifra tutto ciò che segue l'header ESP.
    
- **Struttura:** Header (SPI, SeqNum) + Payload Cifrato + Trailer (Padding) + Auth Data (ICV).
    

---

## 4. Gestione delle Chiavi: IKE (Control Plane)

Gestire le chiavi manualmente è impossibile. **IKE (Internet Key Exchange)** è il protocollo (UDP 500) che negozia automaticamente le **Security Association (SA)**.

**Il Ciclo di Vita IKEv2:**

1. **IKE_SA_INIT:** Scambio in chiaro per negoziare algoritmi e fare Diffie-Hellman.
    
2. **IKE_AUTH:** Scambio cifrato per autenticare le identità e creare il primo tunnel IPsec.
    
3. **CREATE_CHILD_SA:** Per rinnovare le chiavi (Rekeying) o creare tunnel aggiuntivi.
    

> [!tip] Exam Focus
> 
> PFS (Perfect Forward Secrecy): IKE genera chiavi di sessione effimere. Se un attaccante ruba la chiave privata master oggi, non può decifrare il traffico registrato ieri.

---

## 5. Il "Cervello": Policy e Database

Come decide il router cosa cifrare? Usa due database nel kernel.

### SPD (Security Policy Database) - "Il Legislatore"

Contiene le regole di alto livello ("Cosa fare").

- **Azioni:** `Protect` (usa IPsec), `Bypass` (lascia in chiaro), `Discard` (blocca).
    
- **Selettori:** IP Sorgente/Destinazione, Porte, Protocollo.
    

### SAD (Security Association Database) - "L'Esecutore"

Contiene i parametri tecnici delle connessioni attive ("Come farlo").

- **Dati:** Chiavi AES/HMAC, SPI, Sequence Numbers, Lifetime.
    

**Processing Logic Algorithm:**

Plaintext

```
Packet Outbound:
1. Check SPD based on Selectors (IP, Port, Proto)
2. IF Action == Protect THEN
3.    Check SAD for existing SA
4.    IF SA exists -> Encrypt & Send
5.    ELSE -> Trigger IKE to negotiate new SA
```

---

## 6. Problemi Noti e Troubleshooting

### NAT vs IPsec

Il NAT modifica gli header IP e le porte, entrando in conflitto con IPsec che vuole proteggerli.

- **AH + NAT:** Fallisce sempre (Integrità rotta sul cambio IP).
    
- **ESP + PAT:** Fallisce (Porte TCP cifrate, il NAT non sa a chi inoltrare).
    
- **Soluzione:** **NAT-Traversal (NAT-T)**. Incapsula ESP dentro un pacchetto **UDP porta 4500**. Il NAT vede UDP e lavora felice.
    

### MTU e Frammentazione

IPsec aggiunge overhead (50-80 byte). Se il pacchetto originale era già 1500 byte (MTU Ethernet), ora sfora.

- **Rischio:** Frammentazione (lenta e pericolosa) o Drop (se DF bit=1).
    
- **Soluzione:** **MSS Clamping** (ridurre la dimensione dei segmenti TCP) o PMTU Discovery.
    

---

## 7. IPsec vs TLS: Sintesi Comparativa

|**Caratteristica**|**IPsec (Layer 3)**|**TLS (Layer 4/App)**|
|---|---|---|
|**Scopo**|Connettere Reti/Host (VPN)|Proteggere Applicazioni (Web)|
|**Trasparenza**|Invisibile alle App|L'App deve supportarlo|
|**Client**|Richiede software/driver (VPN Client)|Nativo nel Browser|
|**NAT**|Problematico (Serve NAT-T)|Trasparente (Nessun problema)|
|**Modello**|Machine-oriented (IP Addr)|Service-oriented (DNS Name)|