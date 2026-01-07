# NAT (Network Address Translation) e Interazione con IPsec

**Tags:** #ingegneria #reti #nat #ipv4 #ipsec #troubleshooting #pat

## 1. Il Concetto: Perché esiste il NAT?

Il **NAT** è nato come soluzione temporanea (diventata permanente) all'esaurimento degli indirizzi IPv4. Permette a un'intera rete privata (LAN) di accedere a Internet usando un **singolo** indirizzo IP Pubblico.

Funzionamento Logico:

Il router NAT agisce come un intermediario che riscrive gli header dei pacchetti in transito.

1. **Outbound (Uscita):** Sostituisce l'IP Privato (Sorgente) con l'IP Pubblico del router.
    
2. **Inbound (Entrata):** Sostituisce l'IP Pubblico (Destinazione) con l'IP Privato dell'host interno corretto.
    

> [!example] Professor's Example
> 
> Immagina un centralino aziendale.
> 
> - **Interno:** Ogni impiegato ha un numero interno (101, 102...).
>     
> - **Esterno:** L'azienda ha un solo numero pubblico.
>     
> - Il centralinista (NAT) instrada le chiamate: "Ah, questa chiamata è per l'interno 101".
>     

---

## 2. Tipologie di NAT

Esistono diverse varianti, ma una domina il mondo (e crea problemi).

### A. Static NAT (1-to-1)

Mappa un IP privato fisso su un IP pubblico fisso.

- **Uso:** Server web interni che devono essere raggiungibili dall'esterno.
    

### B. Dynamic NAT

Mappa un IP privato su un IP pubblico disponibile da un "pool" di indirizzi.

### C. PAT (Port Address Translation) / NAPT

È la forma più comune (quella del tuo router di casa). Mappa **molti** IP privati su **un solo** IP pubblico, distinguendo i flussi tramite le **Porte TCP/UDP**.

**The mapping logic:**

$$\langle \text{IP}_{priv}, \text{Port}_{priv} \rangle \leftrightarrow \langle \text{IP}_{pub}, \text{Port}_{new} \rangle$$

> [!abstract] Visual Analysis
> 
> Il router mantiene una Translation Table in memoria. Se l'utente A e l'utente B visitano lo stesso sito, il router cambia le loro porte sorgente (es. porta 1000 e porta 1001) per sapere a chi restituire la risposta.

---

## 3. Il Conflitto Critico: NAT vs IPsec

Nei documenti analizzati1, il NAT è citato come uno dei principali "Drawbacks" (Svantaggi) nell'implementazione di IPsec. Perché si odiano?

### Il Problema con AH (Authentication Header)

**AH** protegge l'integrità dell'header IP (inclusi gli indirizzi sorgente/destinazione)2222.

1. Il mittente calcola la firma digitale (ICV) basandosi sull'IP Sorgente originale.
    
2. Il NAT, per funzionare, **modifica** l'IP Sorgente.
    
3. Il destinatario ricalcola la firma e vede che non corrisponde.
    
4. **Risultato:** Il pacchetto viene scartato come "manomesso". **AH non funziona mai attraverso il NAT.**
    

### Il Problema con ESP (Encapsulating Security Payload)

**ESP** cifra il payload, che include l'header TCP/UDP3333.

1. Il **PAT** (Port Address Translation) ha bisogno di leggere e modificare le **Porte TCP/UDP** per gestire più utenti.
    
2. Con ESP, le porte sono **cifrate** e illeggibili.
    
3. Il NAT non sa a quale host interno inoltrare il pacchetto di ritorno.
    
4. **Risultato:** La connessione cade o funziona per un solo utente alla volta.
    

---

## 4. La Soluzione: NAT-Traversal (NAT-T)

Per far convivere IPsec ESP e NAT, si usa una tecnica di incapsulamento chiamata **NAT-T** (standardizzata in RFC 3948).

Il Trucco Tecnico:

Si "nasconde" il pacchetto IPsec (ESP) dentro un pacchetto UDP standard (solitamente porta 4500).

**Packet Structure with NAT-T:**

Plaintext

```
[IP Header] [UDP Header (Port 4500)] [ESP Header] [Encrypted Payload]
```

> [!abstract] Visual Analysis
> 
> 1. Il dispositivo NAT vede un normale pacchetto UDP.
>     
> 2. Può leggere e modificare la porta UDP esterna (4500 -> 4501, etc.) per fare il PAT.
>     
> 3. L'header ESP e il payload cifrato rimangono intatti all'interno.
>     
> 4. IPsec non si "accorge" del cambio di porta UDP esterna e la validazione passa.
>     

---

## 5. Sintesi Diagnostica (Troubleshooting)

|**Scenario**|**Sintomo**|**Causa Tecnica**|**Soluzione**|
|---|---|---|---|
|**IPsec AH + NAT**|Connessione fallisce sempre|NAT modifica IP $\rightarrow$ Hash AH invalido|Passare a ESP o rimuovere NAT|
|**IPsec ESP + PAT**|Connessione instabile / Drop|NAT non vede porte TCP (cifrate)|Abilitare **NAT-Traversal** (UDP 4500)|
|**TCP Checksum**|Pacchetti corrotti|NAT cambia IP ma non ricalcola Checksum TCP|Router NAT deve supportare "Checksum Offload"|

> [!tip] Exam Focus
> 
> Ricorda: Il NAT rompe il principio "End-to-End" di Internet. IPsec cerca di ripristinare la sicurezza End-to-End. Il conflitto è inevitabile perché uno vuole modificare gli header (NAT) e l'altro vuole sigillarli (IPsec).