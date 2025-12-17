# MFA (Multi-Factor Authentication)

## 1. Definizione e Concetto Base

La **Multi-Factor Authentication (MFA)** è un metodo di controllo degli accessi che richiede all'utente di presentare due o più prove (**fattori**) diverse per verificare la propria identità.

L'equazione di base della sicurezza MFA è:

$$\text{Sicurezza} = \text{Fattore}_1 + \text{Fattore}_2 + \dots + \text{Fattore}_n$$

Dove ogni fattore deve appartenere a una categoria diversa.

> [!failure] Common Pitfall
> 
> Richiedere due password non è MFA. È solo "Two-Step Authentication" dello stesso fattore (Knowledge).
> 
> Per essere vero MFA, devi combinare categorie diverse (es. Password + Token).

## 2. Le Categorie di Fattori

Secondo i documenti analizzati 1, i fattori di autenticazione si dividono in:

|**Categoria**|**Descrizione**|**Esempi**|
|---|---|---|
|**What you Know**|Qualcosa che sai.|Password, PIN, Domanda segreta.|
|**What you Have**|Qualcosa che possiedi.|Smartphone, Smart Card, Token Hardware (YubiKey), Generatore OTP.|
|**Who you Are**|Qualcosa che sei (Biometria).|Impronta digitale, Volto (FaceID), Iride, Voce.|
|**Where you Are**|Dove ti trovi.|Indirizzo IP, Geolocalizzazione GPS (spesso usato come segnale di rischio implicito).|

## 3. Perché usare l'MFA? (Security Rationale)

L'MFA è la contromisura principale contro il **Furto di Credenziali**2.

L'efficacia risiede nella "Defense in Depth":

1. Se un attaccante ruba la tua password (tramite Phishing o Database Breach)...
    
2. ...non può comunque accedere all'account perché **non possiede** il tuo dispositivo fisico (secondo fattore) o la tua impronta digitale (terzo fattore).
    

> [!tip] Exam Focus
> 
> L'MFA trasforma l'attacco da "Remoto e Scalabile" (rubare password a milioni) a "Mirato e Difficile" (rubare il telefono specifico di una persona).

## 4. Tecnologie di Implementazione

### A. One-Time Passwords (OTP)

Codici numerici validi per una sola sessione o per un breve periodo di tempo3333.

- **SMS OTP:** Inviati via SMS. Considerati **deboli** (vulnerabili a _SIM Swapping_ e intercettazione SS7), ma meglio di nulla.
    
- **TOTP (Time-based OTP):** Generati da app (Google/Microsoft Authenticator). Il codice cambia ogni 30/60 secondi basandosi su un seme segreto condiviso e sul tempo corrente. Più sicuri degli SMS.
    

### B. Push Notification

L'utente riceve una notifica sul telefono: "Stai cercando di accedere? [Sì/No]".

- **Rischio:** **MFA Fatigue**. L'attaccante spamma notifiche finché l'utente, stanco, preme "Sì" per errore.
    

### C. Token Hardware (FIDO/U2F)

Chiavette fisiche (es. YubiKey) che usano crittografia asimmetrica.

- **Sicurezza Massima:** Sono resistenti al phishing perché la chiave verifica anche il dominio del sito web (protegge contro i siti clone).
    
- Menzionati nelle slide come "Hardware tokens"4.
    

## 5. Limiti e Attacchi all'MFA

L'MFA non è infallibile. Gli attaccanti evoluti usano tecniche specifiche per aggirarlo:

1. **Real-Time Phishing (Adversary-in-the-Middle):**
    
    - L'attaccante crea un sito falso che fa da proxy in tempo reale.
        
    - L'utente inserisce password e codice OTP nel sito falso.
        
    - L'attaccante gira i dati al sito vero istantaneamente, ottiene il cookie di sessione e butta fuori l'utente.
        
2. **Session Hijacking:**
    
    - Se l'attaccante infetta il PC con un malware, ruba il **Cookie di Sessione** _dopo_ che l'utente ha fatto l'MFA. L'MFA non protegge le sessioni già attive 5.
        
3. **SIM Swapping:**
    
    - L'attaccante inganna l'operatore telefonico per clonare la SIM della vittima e ricevere gli SMS OTP.
        

---

**Vedi anche:**

- [[Autenticazione: Un'Introduzione]]
    
- [[Autenticazione: Modelli di Attaccante]]
    
- [[Login Trojan Horse]]