# **Replay attack (attacco di ripetizione)**

> Un attaccante **cattura** (o registra) messaggi legittimi già inviati tra entità e **li ritrasmette** successivamente per far sì che il sistema esegua nuovamente un’azione (es. autenticazione, pagamento, comando), senza dover conoscere chiavi o modificare il contenuto.

---

### **Caratteristiche principali**

- **Obiettivo:** ottenere vantaggi riusando messaggi validi (es. riautenticarsi, duplicare transazioni, riavviare comandi).
    
- **Condizione necessaria:** il sistema **non verifica la freschezza** del messaggio (non distingue messaggi nuovi da messaggi vecchi).
    
- **Livello d’accesso dell’attaccante:** spesso solo capacità di intercettare e ritrasmettere pacchetti (man‑in‑the‑middle, sniffing, accesso alla rete).
    

---

### **Esempi concreti**

- Riutilizzo di un pacchetto di login per ottenere accesso senza credenziali.
    
- Ritrasmissione di una transazione finanziaria (duplicare un pagamento).
    
- In sistemi IoT, ripetere un comando (es. “apri porta”) catturato precedentemente.
    
- Replay di token di sessione scaduti se non verificati correttamente.
    

---

### **Contromisure efficaci**

1. **Nonce (numero unico usa‑e‑getta):** includere un nonce casuale nel messaggio e verificarne unicità al server.
    
2. **Timestamps + finestra di validità:** includere marca temporale e accettare messaggi solo entro una finestra limitata (contro replay ritardati).
    
3. **Sequence numbers / sliding window:** numerare messaggi e rifiutare numeri già visti (utile in protocolli a flusso).
    
4. **Challenge–response:** il server invia una challenge (nonce) che il client deve firmare o MAC‑are; un replay senza nuova challenge fallisce.
    
5. **Autenticazione forte e AEAD:** usare AEAD (AES‑GCM, ChaCha20‑Poly1305) e verificare tag prima di eseguire azioni; associare nonce/timestamp ai dati autenticati.
    
6. **Short‑lived tokens & session management:** token che scadono rapidamente e revoca attiva.
    
7. **Logging e rilevamento anomalie:** identificare ritrasmissioni sospette e bloccare sorgenti.
    
8. **Transport security:** TLS con session resumption sicuro e anti‑replay integrato; evitare protocolli in chiaro.
    
9. **Protezione application‑level:** non fare affidamento solo sul trasporto: applicazioni critiche devono avere protezioni proprie (es. firma dei comandi con un contatore).

Guarda anche [[10 CS Lower Level - Authentication - Introduction and Attacker Models#3. Tecniche Fondamentali (Anti-Replay)]]

---

### **Buone pratiche operative**

- Non riusare nonce/IV o altri parametri che dovrebbero essere unici.
    
- Validare timestamp con attenzione (sincronizzazione clock necessaria).
    
- Per sistemi distribuiti, usare meccanismi combinati (es. nonce + sequence number).
    
- Considerare threat model: in ambienti adversariali, preferire challenge‑response e firme.
    

---

### **In breve**

> Un **replay attack** riusa messaggi legittimi per ottenere azioni non autorizzate.  
> Difesa semplice ed efficace: **garantire la freschezza** dei messaggi (nonce, timestamp, sequence numbers, challenge‑response) + **autenticazione robusta** (MAC/firma/AEAD) e gestione sicura delle sessioni.