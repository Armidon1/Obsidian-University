# **Side‑channel attack (attacco da canale laterale)**

> Un **attacco che ricava informazioni segrete non analizzando il testo cifrato o l’algoritmo**, ma osservando **effetti collaterali fisici o temporali** del sistema: tempi di esecuzione, consumi, emissioni elettromagnetiche, rumore acustico, cache behaviour, errori indotti, ecc.

In pratica l’attaccante sfrutta _metadati fisici_ (il canale laterale) invece che una debolezza matematica dell’algoritmo.

---

### **Tipi comuni**

- **Timing attacks** — misurare il tempo di esecuzione per dedurre bit della chiave.
    
- **Power analysis (SPA / DPA)** — misurare il consumo elettrico (single / differential power analysis).
    
- **Electromagnetic (EM) eavesdropping** — captare emissioni EM generate durante l’elaborazione.
    
- **Cache attacks (Flush+Reload, Prime+Probe)** — sfruttare il comportamento della cache della CPU per vedere quali dati/instr vengono usati.
    
- **Acoustic attacks** — analizzare il rumore meccanico/sonoro (es. su tastiere o dischi).
    
- **Fault injection / glitching** — indurre errori (sovratensioni, luce, laser, EM) e usare i risultati per ricavare segreti.
    
- **Microarchitectural (Spectre/Meltdown-like)** — sfruttare esecuzione speculativa e struttura interna della CPU.
    

---

### **Esempi celebri**

- **Timing attack su RSA** (Kocher): tempo di decifratura rivela bit della chiave.
    
- **DPA su smartcard**: estrazione di chiavi private analizzando consumi ripetuti.
    
- **Cache attacks** (es. Flush+Reload) per rubare chiavi in ambienti multi-tenant.
    
- **Fault attacks su smartcard** per forzare decifrature errate e ricostruire la chiave.
    

---

### **Perché sono pericolosi**

- Possono rompere implementazioni _anche se l’algoritmo matematico è sicuro_.
    
- Spesso richiedono accesso fisico o co-locazione, ma molte varianti funzionano anche in cloud o via rete (timing, cache).
    
- Sono pratici e riproducibili contro dispositivi embedded, HSM mal configurati, VM co-residenti.
    

---

### **Contromisure pratiche**

1. **Constant‑time coding** — evitare dipendenze temporali dai segreti (branching, lookup index).
    
2. **Masking / Randomization** — randomizzare variabili interne per rompere correlazioni (utile contro DPA).
    
3. **Blinding** — es. RSA blinding prima della decifratura per eliminare timing/power leakage.
    
4. **Noise & filtering** — aggiungere rumore o ritardi casuali (attenzione: non sempre sufficiente).
    
5. **Isolamento hardware** — usare HSM, enclave o processori dedicati; disabilitare co‑locazione non trusted.
    
6. **Hardware countermeasures** — schermatura EM, protezioni contro glitch, resistori shunt, sensori di tamper.
    
7. **Evita lookup table sensibili** o usa implementazioni S‑box che non indexano direttamente con segreti.
    
8. **Compilatore / toolchain attenta** — controllare ottimizzazioni che reintroducono branching/lookup.
    
9. **Validazione degli errori** — non rivelare informazioni diverse nelle risposte d’errore (uniform error handling).
    
10. **Monitoring e intrusion detection** — rilevare attività sospette (scansione EM, accessi ripetuti, timing anomali).
    

---

### **Linee guida per sviluppatori**

- Preferire implementazioni crittografiche verificate “constant-time” (biblioteche moderne: libsodium, BoringSSL, OpenSSL con patch).
    
- Testare contro attacchi locali (fuzzing temporale, power emulation, cache probing).
    
- Usare HSM o servizi cloud KMS per proteggere chiavi sensibili.
    
- Considerare il threat model: se l’attaccante può misurare consumi/EM o è co‑locato, le contromisure hardware/software sono obbligatorie.
    

---

**In breve:**

> Un **side‑channel attack** sfrutta informazioni fisiche o temporali collaterali per recuperare segreti — non è una “rottura matematica” dell’algoritmo ma una rottura dell’**implementazione** o dell’ambiente. Difendersi richiede sia tecniche software (constant‑time, masking, blinding) sia contromisure hardware e buone pratiche operative.