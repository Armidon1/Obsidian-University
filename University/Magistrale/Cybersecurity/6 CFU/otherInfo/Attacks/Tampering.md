# Tampering Attack (Attacco di Manomissione)

**Tags:** #ingegneria #security #attacks #integrity #tampering #mitm #cia_triad

## 1. Definizione e Concetto

Il Tampering è la modifica non autorizzata dei dati mentre sono in transito (in-flight) o a riposo (at-rest).

Rappresenta una violazione diretta del principio di Integrità della triade CIA (Confidentiality, Integrity, Availability).

**Definizione formale:**

> "Tampering = unauthorized modification of transmitted data (integrity violation)".

In questo scenario, l'attaccante non si limita ad ascoltare passivamente (Eavesdropping), ma interviene attivamente alterando il contenuto dei pacchetti per ingannare il destinatario o corrompere il sistema.

---

## 2. Come avviene l'attacco?

Il Tampering avviene quasi sempre in un contesto di **Man-in-the-Middle (MITM)**. L'attaccante si posiziona logicamente o fisicamente tra il mittente (Alice) e il destinatario (Bob).

**Il flusso logico dell'attacco:**

1. **Intercettazione:** L'attaccante cattura il messaggio originale $M$ inviato da Alice.
    
2. **Modifica:** L'attaccante altera il messaggio trasformandolo in $M'$ (oppure ne cambia l'ordine o lo ritarda).
    
3. **Inoltro:** L'attaccante invia $M'$ a Bob.
    
4. **Inganno:** Bob riceve $M'$, crede che sia il messaggio autentico di Alice ed esegue un'azione basata su dati falsi (es. un server che accetta un comando malevolo).
    

> [!failure] Common Pitfall
> 
> Confusione con lo Spoofing:
> 
> - **Spoofing:** L'attaccante falsifica la propria identità (es. IP falso) per sembrare qualcun altro.
>     
> - Tampering: L'attaccante modifica il contenuto del messaggio.
>     
>     Spesso i due attacchi avvengono insieme: modifico il messaggio (Tampering) e lo rispedisco fingendo di essere il mittente originale (Spoofing).
>     

---

## 3. Scenari di Applicazione

Il tampering è critico in due contesti principali:

### A. Traffico di Rete (Network Transit)

Riguarda la manipolazione dei pacchetti IP o dei segmenti TCP durante la trasmissione.

- **Obiettivo:** Iniettare script malevoli in pagine web (HTML injection), modificare importi in transazioni finanziarie, o alterare le risposte DNS per reindirizzare il traffico.
    
- **Rischio:** Senza controlli di integrità, il protocollo IP (Internet Protocol) di per sé non garantisce che il pacchetto ricevuto sia identico a quello inviato.
    

### B. Distribuzione Software (Software Supply Chain)

Riguarda la modifica di file eseguibili, librerie o aggiornamenti firmware prima che l'utente li installi.

- **Obiettivo:** Iniettare malware, trojan o backdoor in un software legittimo ("Malware injection").
    
- **Difesa:** Questo è il motivo per cui i sistemi operativi moderni richiedono che i driver e le applicazioni siano firmati digitalmente (Code Signing).
    

---

## 4. Contromisure Tecniche (Prevention & Detection)

La crittografia offre strumenti matematici per rendere evidente qualsiasi tentativo di manomissione. Se un bit cambia, la verifica fallisce.

### Message Authentication Codes (MAC)

Utilizzati in protocolli come TLS e IPsec per garantire l'integrità di sessione.

Il mittente calcola un tag crittografico sul messaggio usando una chiave segreta condivisa $K$.

**The verification logic:**

$$\text{Tag} = \text{HMAC}(K, \text{Messaggio})$$

> [!abstract] Math Analysis
> 
> Se l'attaccante modifica il messaggio in $M'$, non possedendo la chiave $K$, non potrà calcolare il nuovo $\text{Tag}'$ corretto. Il destinatario ricalcolerà l'HMAC sui dati ricevuti e, notando la discrepanza con il Tag ricevuto, scarterà il pacchetto come "Manomesso".

### Firme Digitali (Digital Signatures)

Utilizzate nei certificati X.509 e nel Code Signing.

- Si basa sulla crittografia asimmetrica.
    
- L'hash del file viene cifrato con la chiave privata del mittente.
    
- Chiunque (con la chiave pubblica) può decifrare l'hash e confrontarlo con quello calcolato sul file ricevuto.
    

### Protocolli Sicuri (Implementazione)

- **TLS (Transport Layer Security):** Fornisce integrità "End-to-End" per i dati scambiati tra applicazioni (es. HTTPS). Usa algoritmi AEAD (Authenticated Encryption with Associated Data) per cifrare e autenticare simultaneamente.
    
- **IPsec (AH/ESP):**
    
    - **AH (Authentication Header):** Fornisce integrità e autenticazione per l'intero pacchetto IP (ma non cifra).
        
    - **ESP (Encapsulating Security Payload):** Fornisce integrità (opzionale ma raccomandata) e cifratura del payload.