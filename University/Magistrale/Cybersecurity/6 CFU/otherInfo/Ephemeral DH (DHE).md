**DHE (Diffie-Hellman Ephemeral)** è una variante specifica del protocollo di scambio chiavi Diffie-Hellman (DH), progettata per fornire **Perfect Forward Secrecy (PFS)**.

La parola chiave è **"Ephemeral" (Effimero)**. Significa che, per _ogni singola sessione_ (ad esempio, ogni connessione HTTPS), sia il client che il server **generano una coppia di chiavi DH completamente nuova** (una privata effimera e una pubblica effimera).

Usano queste chiavi temporanee per eseguire lo scambio Diffie-Hellman, calcolare il segreto condiviso e derivare le chiavi di sessione. Subito dopo, **distruggono le chiavi private effimere**.

---

### 🛡️ Il Vantaggio: Perfect Forward Secrecy (PFS)

Questo approccio garantisce la **Perfect Forward Secrecy (PFS)**, o Segretezza Inoltrata Perfetta.

- **Il Problema (Senza PFS):** Se un server usa una chiave privata DH _statica_ (sempre la stessa) per lo scambio chiavi, e un aggressore registra tutto il traffico cifrato per un anno, tutto ciò che deve fare è rubare quella singola chiave privata statica. Una volta ottenuta, può tornare indietro e **decifrare retroattivamente tutto il traffico registrato**.
    
- **La Soluzione (Con DHE):** Poiché le chiavi private usate per generare il segreto di sessione vengono distrutte dopo l'uso, non esistono più. Anche se un aggressore ruba la chiave privata _a lungo termine_ del server (quella usata per l'autenticazione, come la chiave RSA), quella chiave **non può essere usata per decifrare le sessioni passate**. Il traffico registrato rimane sicuro.
    

---

### Applicazione Ingegneristica

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Obiettivo**|Stabilire una chiave di sessione simmetrica condivisa.|
|**Proprietà Chiave**|**Perfect Forward Secrecy (PFS)**. Protegge le sessioni passate dalla compromissione futura della chiave a lungo termine.|
|**Processo**|1. Il server genera una chiave $a_{effimera}$ e invia la parte pubblica $A_{effimera}$ (firmata con la sua chiave _statica_ per autenticazione).<br><br>  <br><br>2. Il client genera $b_{effimera}$ e invia $B_{effimera}$.<br><br>  <br><br>3. Entrambi calcolano il segreto condiviso e **distruggono** le loro chiavi $a$ e $b$ effimere.|
|**Uso Pratico**|È lo standard _de facto_ per lo scambio di chiavi in **TLS 1.2** (insieme a ECDHE) ed è fondamentale in **TLS 1.3**.|
|**Contro (Efficienza)**|DHE (con l'aritmetica modulare) è **computazionalmente intensivo**. Richiede la generazione di nuovi, grandi numeri primi e calcoli di esponenziazione. Per questo motivo, è stato quasi completamente sostituito dalla sua controparte a curva ellittica, **ECDHE**, che è molto più veloce.|
