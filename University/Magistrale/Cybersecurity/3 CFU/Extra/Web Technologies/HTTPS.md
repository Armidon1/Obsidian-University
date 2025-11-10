>[!Definzione]
>**HTTPS (Hypertext Transfer Protocol Secure)** è **[[HTTP]] incapsulato in una connessione [[TLS]] (Transport Layer Security)**. Non è un protocollo a sé stante, ma piuttosto l'applicazione del protocollo HTTP su un livello di trasporto sicuro.

Le sue caratteristiche chiave sono:

1. **Sicurezza su TLS:** Sfrutta [[TLS]] (il successore di SSL) per fornire tre garanzie di sicurezza fondamentali che mancano a [[HTTP]]:
    
    - **[[Confidentiality]] (Encryption):** Il traffico tra client e server è crittografato. Questo previene l'intercettazione (_sniffing_) dei dati, come password o cookie di sessione.
        
    - **Integrità ([[Integrity]]):** I dati non possono essere modificati in transito da un utente malintenzionato (_Man-in-the-Middle_) senza che la connessione se ne accorga e si interrompa.
        
    - **Autenticazione ([[Authentication]]):** Il client può verificare l'identità del server a cui si sta connettendo tramite **Certificati Digitali X.509** emessi da una **Certificate Authority (CA)** fidata.
        
2. **Stesso Protocollo Applicativo:** A livello 7 (applicazione), i comandi (`GET`, `POST`), gli header e i codici di stato sono **identici a quelli di HTTP**. La differenza è solo nel trasporto.
    
3. **Porta Standard:** Opera sulla porta **443** (TCP) per impostazione predefinita.