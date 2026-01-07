# Protocollo IPv6: Architettura e Differenze con IPv4

**Tags:** #ingegneria #reti #ipv6 #layer3 #header #next_generation_ip

## 1. Perché IPv6? (Il problema dello spazio)

IPv4 offre circa 4,3 miliardi di indirizzi ($2^{32}$), esauriti nel 2011 (IANA).

IPv6 risolve il problema espandendo lo spazio di indirizzamento a 128 bit.

**Confronto Matematico:**

$$\text{Spazio IPv4} = 2^{32} \approx 4.29 \times 10^9$$

$$\text{Spazio IPv6} = 2^{128} \approx 3.4 \times 10^{38}$$

> [!example] Professor's Example
> 
> Se IPv4 fosse grande come una pallina da golf, IPv6 sarebbe grande come il Sole. Questo rende inutile il NAT (Network Address Translation), ripristinando la connettività End-to-End pura.

---

## 2. Struttura dell'Header: Semplificazione ed Efficienza

A differenza di IPv4 (che ha una lunghezza variabile da 20 a 60 byte a causa delle "Opzioni"), l'header IPv6 ha una **lunghezza fissa di 40 Byte**.

### Header Base (Fixed Header)

L'header è stato ripulito dai campi inutili per velocizzare il processing nei router hardware.

**Campi Rimossi (rispetto a IPv4):**

- **No Checksum:** I router non calcolano più il checksum a ogni salto (lo fanno già TCP/UDP e Ethernet). Risultato: Routing molto più veloce.
    
- **No Fragmentation:** I router **NON** frammentano più. Se un pacchetto è troppo grande, viene scartato inviando un ICMPv6 "Packet Too Big" (obbliga il mittente a usare il PMTU Discovery).
    
- **No Header Length (IHL):** Non serve, la dimensione è fissa.
    

**Campi Chiave:**

1. **Version (4 bit):** Valore 6.
    
2. **Traffic Class (8 bit):** Equivalente al ToS di IPv4 (QoS).
    
3. **Flow Label (20 bit):** _Nuovo._ Etichetta un flusso di pacchetti (es. streaming video) per garantire che seguano lo stesso percorso o abbiano la stessa QoS, senza dover guardare le porte TCP/UDP (che potrebbero essere cifrate).
    
4. **Payload Length (16 bit):** Dimensione dei dati _dopo_ l'header fisso.
    
5. **Next Header (8 bit):** Il campo più importante (vedi sotto).
    
6. **Hop Limit (8 bit):** Equivalente al TTL di IPv4.
    

---

## 3. La Rivoluzione: Extension Headers (Next Header)

In IPv4, le opzioni erano nel footer dell'header, rendendo il processing lento.

In IPv6, le opzioni sono spostate in header aggiuntivi "concatenati" tra l'header IP e il payload.

Il meccanismo "Next Header":

Ogni header dice qual è il tipo del successivo. Si crea una catena (Daisy Chain).

**Esempio di Catena Logica:**

$$[\text{IPv6 Header} | \text{NH}=43] \rightarrow [\text{Routing Ext} | \text{NH}=51] \rightarrow [\text{AH Header} | \text{NH}=6] \rightarrow [\text{TCP Segment}]$$

**Principali Extension Headers:**

- **Hop-by-Hop Options:** Informazioni che _ogni_ router deve leggere (l'unico header processato durante il transito).
    
- **Routing:** Forza il pacchetto a passare per specifici router intermedi.
    
- **Fragment:** Gestisce la frammentazione (fatta solo dal mittente, mai dai router).
    
- **ESP / AH:** Gli header di sicurezza IPsec sono trattati semplicemente come Extension Headers.
    

> [!abstract] Visual Analysis
> 
> Nei diagrammi IPsec visti (Slide 49-50 del modulo IPsec), nota come in IPv6 gli header di sicurezza (AH o ESP) si inseriscono "in mezzo" alla catena degli Extension Headers.
> 
> - **AH** protegge anche gli Extension Headers immutabili (es. Routing finale).
>     
> - **ESP** cifra tutto ciò che viene dopo di lui nella catena.
>     

---

## 4. Indirizzamento e Notazione

- **Lunghezza:** 128 bit.
    
- **Notazione:** Esadecimale, gruppi di 4 cifre separati da due punti (`:`).
    
- **Compressione:** Una sequenza di zeri può essere sostituita da `::` (una sola volta).
    

**Esempio:**

- Full: `2001:0db8:0000:0000:0000:0000:1428:57ab`
    
- Compressed: `2001:db8::1428:57ab`
    

---

## 5. Sintesi: IPv4 vs IPv6

|**Caratteristica**|**IPv4**|**IPv6**|
|---|---|---|
|**Indirizzi**|32 bit (esauriti)|128 bit (infiniti)|
|**Header Size**|Variabile (20-60 Byte)|Fisso (40 Byte)|
|**Frammentazione**|Router e Mittente|Solo Mittente|
|**Checksum**|Sì (ricalcolato a ogni hop)|No (demandato ai layer 2 e 4)|
|**Opzioni**|In coda all'header (lento)|Extension Headers (flessibile)|
|**Sicurezza**|IPsec è "appiccicato" (Add-on)|IPsec è nativo (Extension Hdr)|
|**NAT**|Necessario|Deprecato/Inutile|