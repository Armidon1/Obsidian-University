# Flussi di Rete

I flussi di rete sono record di **metadati** delle sessioni di comunicazione di rete. Pensateli come una "bolletta telefonica" per la vostra rete: mostrano _chi_ ha parlato con _chi_, per _quanto tempo_ e _quanti_ dati sono stati inviati, ma **NON il contenuto effettivo (payload)** della conversazione.

**Identificazione 5-Tupla (I Campi Chiave):**

1. Indirizzo IP Sorgente
    
2. Indirizzo IP Destinazione
    
3. Porta Sorgente
    
4. Porta Destinazione
    
5. Protocollo (es. TCP, UDP, ICMP)
    

**Dati Aggiuntivi Catturati:**

- Ora di inizio e fine (durata)
    
- Numero di Byte / Pacchetti trasferiti
    
- Flag TCP (che forniscono lo stato della sessione come SYN, ACK, FIN, RST)
    
- Numero di Autonomous System (AS) (per tracciare le connessioni esterne)
    