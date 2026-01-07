# ECDHE (Elliptic Curve Diffie-Hellman Ephemeral)
L'**ECDHE (Elliptic Curve Diffie-Hellman Ephemeral)** è una variante specifica del protocollo di scambio chiavi ECDH, progettata per fornire **[[Perfect Forward Secrecy (PFS)]]**.

La parola chiave è **"Ephemeral" (Effimero)**. Significa che, per _ogni singola sessione_ (ad esempio, ogni volta che ti connetti a un sito [[HTTPS]]), sia il client che il server **generano una coppia di chiavi [[ECDH]] completamente nuova** (una privata effimera e una pubblica effimera).

Usano queste chiavi temporanee per eseguire the[[Diffie-Hellman Key Exchange]], calcolare il segreto condiviso e derivare le chiavi di sessione. Subito dopo, **distruggono le chiavi private effimere**.

---

### 🛡️ Il Vantaggio: Perfect Forward Secrecy (PFS)

Questo approccio garantisce la **Perfect Forward Secrecy (PFS)**, o Segretezza Inoltrata Perfetta.

- **Il Problema (Senza PFS):** Se un server usa una chiave privata ECDH _statica_ (sempre la stessa) per lo scambio chiavi, e un aggressore registra tutto il traffico cifrato per un anno, tutto ciò che deve fare è rubare quella singola chiave privata statica (tramite hacking, coercizione legale, ecc.). Una volta ottenuta, può tornare indietro e **decifrare retroattivamente tutto il traffico registrato**.
    
- **La Soluzione (Con ECDHE):** Poiché le chiavi private usate per generare il segreto di sessione vengono distrutte dopo l'uso, non esistono più. Anche se un aggressore ruba la chiave privata _a lungo termine_ del server (quella usata per l'autenticazione, come la chiave RSA o ECDSA), quella chiave **non può essere usata per decifrare le sessioni passate**. Il traffico registrato rimane sicuro.
    

### Applicazione Ingegneristica

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Obiettivo**|Stabilire una chiave di sessione simmetrica condivisa.|
|**Proprietà Chiave**|**Perfect Forward Secrecy (PFS)**. Protegge le sessioni passate dalla compromissione futura della chiave a lungo termine.|
|**Processo**|1. Il server genera una chiave $d_{server\_effimera}$ e invia la parte pubblica $Q_{server\_effimera}$ (firmata con la sua chiave _statica_ per autenticazione).<br><br>  <br><br>2. Il client genera $d_{client\_effimera}$ e invia $Q_{client\_effimera}$.<br><br>  <br><br>3. Entrambi calcolano il segreto condiviso e **distruggono** le loro chiavi $d$ effimere.|
|**Uso Pratico**|È lo standard _de facto_ per lo scambio di chiavi in **TLS 1.2** e **TLS 1.3** (dove è obbligatorio). È il motivo per cui vedi `ECDHE` (come `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`) nelle _cipher suite_ moderne.|