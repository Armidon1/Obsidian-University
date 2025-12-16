# NIST (National Institute of Standards and Technology)

## 1. Chi sono?

Il **NIST** è un'agenzia governativa non regolatoria dell'amministrazione degli Stati Uniti (parte del Dipartimento del Commercio).

Sebbene si occupi di tutto (dai pesi atomici alla resistenza del cemento), nel mondo dell'informatica è l'Autorità Suprema per la definizione degli standard di Crittografia e Cybersecurity.

Quando il NIST approva un algoritmo, questo diventa lo standard globale non solo per il governo USA, ma per l'industria privata (banche, web, hardware) in tutto il mondo.Shutterstock

## 2. Il "Metodo NIST": Le Competizioni Pubbliche

A differenza di enti segreti come la NSA, il NIST opera (generalmente) in modo trasparente.

Per scegliere i nuovi standard crittografici, indice delle Competizioni Internazionali aperte a crittografi di tutto il mondo.

- **Processo:** Call for proposals $\to$ Analisi pubblica $\to$ Eliminatorie $\to$ Finalisti $\to$ Vincitore.
    
- **Vantaggio:** Gli algoritmi vengono attaccati e analizzati dalla comunità scientifica globale per anni prima di diventare standard.
    
- **Esempi di Successo:**
    
    - **[[AES]] (Rijndael):** Creato da due belgi, ha vinto la competizione per sostituire il DES.
        
    - **SHA-3 (Keccak):** Creato da un team italo-belga.
        

## 3. Le Pubblicazioni (Cosa devi conoscere)

I documenti del NIST sono la "Bibbia" per gli ingegneri di sicurezza. Si dividono in due categorie principali:

### A. FIPS (Federal Information Processing Standards)

Sono norme **obbligatorie** per le agenzie governative USA e per i contractor militari.

- **FIPS 197:** Definisce lo standard **[[AES]]**.
    
- **FIPS 180:** Definisce la famiglia **SHA** (Secure Hash Algorithm).
    
- **FIPS 186:** Definisce il **DSS** (Digital Signature Standard), che include RSA e Elliptic Curves.
    
- **FIPS 140:** Lo standard per certificare i moduli hardware crittografici (HSM).
    

### B. NIST SP 800-Series (Special Publications)

Sono guide tecniche, raccomandazioni e best practices (spesso diventano standard de facto).

- **SP 800-90A:** Definisce i generatori di numeri casuali sicuri (**[[CTR_DRBG]]**, Hash_DRBG).
    
- **SP 800-57:** Linee guida sulla gestione delle chiavi (Key Management).
    
- **SP 800-63:** Linee guida sull'identità digitale e le password (es. "smettete di chiedere il cambio password ogni 3 mesi").
    

## 4. Tabella degli Standard Crittografici

|**Sigla Algoritmo**|**Tipo**|**Standard NIST di Riferimento**|
|---|---|---|
|**[[AES]]**|Cifratura Simmetrica|FIPS 197|
|**[[SHA-256]]**|Hashing|FIPS 180-4|
|**[[RSA]]**|Firma / Cifratura|FIPS 186-4|
|**[[HMAC]]**|MAC (Autenticazione)|FIPS 198-1|
|**[[CTR_DRBG]]**|Generatore Random (RNG)|SP 800-90A|

## 5. Controversie: Il caso Dual_EC_DRBG

Nonostante la reputazione, il NIST ha avuto macchie scure dovute all'influenza della **NSA**.

Il caso più famoso riguarda lo standard **SP 800-90A** (quello dei generatori random).

- Nel 2006, il NIST incluse un generatore chiamato **Dual_EC_DRBG**.
    
- Era molto lento e aveva bias statistici, ma fu spinto misteriosamente.
    
- Nel 2013 (leak di Snowden) si scoprì che la NSA aveva pagato per inserire una **Backdoor matematica** in quell'algoritmo per poter decifrare il traffico VPN.
    
- **Conseguenza:** Il NIST ha rimosso l'algoritmo e ha rivisto i processi per riguadagnare fiducia.
    

> [!tip] Exam Focus
> 
> Se un sistema o un prodotto dichiara di essere "FIPS Compliant", significa che usa solo algoritmi e implementazioni approvate dal NIST. In molti settori (bancario, sanitario, governativo) questo è un requisito legale.

---

**Vedi anche:**

- [[AES]]
    
- [[PRNG (Pseudo-Random Number Generator)]]
    
- [[CS-PRNG based by CTR_DRBG (AES)]]
    
- [[RSA]]