# MTU (Maximum Transmission Unit) e Problemi di Frammentazione

**Tags:** #ingegneria #reti #troubleshooting #mtu #ipsec #frammentazione #mss

## 1. Il Concetto: Cos'è l'MTU?

L'**MTU** rappresenta la dimensione massima (in byte) di un pacchetto IP che può essere trasmesso su un'interfaccia di rete senza dover essere spezzato.

- **Standard Ethernet:** 1500 Byte.
    
- **Significato:** È come l'altezza massima di un tunnel. Se il camion (pacchetto) è più alto, non passa o deve essere smontato.
    

### Il Conflitto con IPsec

IPsec aggiunge intestazioni extra (ESP Header, ESP Trailer, IV, Nuovo IP Header in Tunnel Mode). Questo aggiunge un **Overhead** significativo.

**The mathematical problem is:**

$$\text{Dimensione Pacchetto} = \text{Payload Originale} + \text{Overhead IPsec}$$

Se il payload originale era già al limite (es. 1500 byte) e aggiungi 50-80 byte di IPsec, il totale supera i 1500.

> [!example] Professor's Example
> 
> Immagina di spedire una lettera in una busta standard. Se devi metterla dentro una seconda busta di sicurezza (IPsec), la busta interna deve essere necessariamente più piccola, altrimenti quella esterna non si chiude o supera le dimensioni accettate dalla cassetta postale.

---

## 2. La Frammentazione (Fragmentation)

Quando un pacchetto supera l'MTU, il router deve frammentarlo (spezzarlo in due o più pezzi).

### Perché è un problema grave?

1. **CPU Load:** Frammentare e riassemblare richiede molta CPU ai router e agli host finali.
    
2. **Firewall Drop:** Molti firewall scartano i frammenti IP (tranne il primo) perché non contengono l'header TCP/UDP (non sanno a quale porta sono destinati), rompendo la connessione.
    
3. **Inefficienza:** Se perdi anche solo _un_ frammento, l'intero pacchetto originale deve essere ritrasmesso.
    

---

## 3. Il "Black Hole" (PMTUD Failure)

Il problema più insidioso è quando la frammentazione è **vietata**.

### Il Bit DF (Don't Fragment)

I moderni sistemi operativi impostano il bit **DF = 1** nell'header IP dei pacchetti TCP. Questo dice ai router: "Non frammentare questo pacchetto! Se non passa, scartalo".

### Path MTU Discovery (PMTUD)

È il meccanismo automatico per trovare l'MTU giusto.

1. L'host invia un pacchetto grande con DF=1.
    
2. Un router intermedio (es. il gateway VPN) vede che è troppo grande.
    
3. Scarta il pacchetto.
    
4. Invia indietro un messaggio **ICMP Type 3 Code 4** ("Fragmentation Needed but DF set") dicendo: "Ehi, il mio limite è 1400, riprova con meno".
    
5. L'host riceve l'avviso e riduce la dimensione.
    

Il problema del "Buco Nero":

Se un firewall lungo il percorso blocca i messaggi ICMP (per presunta sicurezza), l'host non riceve mai l'avviso "Packet Too Big".

- L'host continua a inviare pacchetti grandi.
    
- Il router continua a scartarli silenziosamente.
    
- **Sintomo:** La connessione si stabilisce (Handshake TCP piccoli passano), ma appena provi a caricare dati (pacchetti grandi), la connessione si "congela".
    

![[SCREEN_SLIDE_MTU_DROP]]

> [!abstract] Visual Analysis
> 
> What to look at: Un diagramma dove il pacchetto grande viene scartato dal router VPN e la risposta ICMP (la "X" rossa) viene bloccata dal firewall.
> 
> Meaning: Il client aspetta in eterno (timeout), creando l'effetto Black Hole.

---

## 4. Soluzioni Tecniche

### A. MSS Clamping (Soluzione Router/Firewall)

Si manipola l'handshake TCP (SYN packet).

Il router VPN intercetta il pacchetto SYN e riscrive il valore MSS (Maximum Segment Size) annunciato dai client, abbassandolo artificialmente.

**Mathematical Logic for MSS:**

$$\text{MSS} = \text{MTU} - (\text{IP Header} + \text{TCP Header})$$

> [!tip] Exam Focus
> 
> L'MSS riguarda solo il payload TCP (livello 4), mentre l'MTU riguarda l'intero pacchetto IP (livello 3). Modificare l'MSS costringe il mittente a creare pacchetti IP più piccoli all'origine.

### B. Abbassare l'MTU dell'Interfaccia

Si configura manualmente l'interfaccia virtuale della VPN con un MTU più basso (es. 1400 o 1360 byte) per lasciare spazio all'overhead IPsec.

### C. Abilitare ICMP

Configurare i firewall per permettere il transito dei messaggi ICMP "Destination Unreachable" (Type 3, Code 4).

---

## 5. Diagnostica (Implementation)

Come scoprire se hai un problema di MTU? Usando il comando Ping con il flag "Don't Fragment".

**Here is the command for Windows:**

DOS

```
ping -f -l 1472 google.com
```

> [!abstract] Code Analysis
> 
> - `-f`: Imposta il bit Don't Fragment.
>     
> - `-l 1472`: Dimensione payload (1472 + 28 byte header = 1500).
>     
> - Se ricevi "Packet needs to be fragmented but DF set", devi abbassare il numero finché non passa (es. 1400). Quello è il tuo **Path MTU**.
>