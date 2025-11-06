# **Brute-force attack**

> Un attacco che tenta di **provare sistematicamente tutte le possibili combinazioni** (di password, chiavi crittografiche, token, ecc.) fino a trovare quella corretta. È un approccio “forza bruta”: semplice, prevedibile, ma spesso efficace se lo spazio delle possibili soluzioni è piccolo o ci sono debolezze implementative.

---

### **Caratteristiche principali**

- **Metodo:** tentativi esaustivi o semi-esaustivi (es. tutte le password possibili, o tutte le chiavi fino a N bit).
    
- **Costo:** tempo e risorse computazionali; cresce esponenzialmente con la lunghezza/entropia della chiave o password.
    
- **Automatizzabile:** gli attaccanti usano script, GPU/ASIC, botnet per parallelizzare i tentativi.
    
- **Varianti pratiche:**
    
    - **Dictionary attack:** tenta parole da una lista (dizionari, leak).
        
    - **Hybrid attack:** combina regole (sostituzioni, suffissi) su dizionari.
        
    - **Credential stuffing:** usa coppie username/password da breach su altri servizi.
        

---

### **Esempi**

- Provare tutte le chiavi AES-56 (storico) o tentare tutte le password di un account web.
    
- Usare GPU per testare miliardi di candidate password/s al secondo contro hash non rallentati.
    
- Botnet che prova combinazioni di login su servizi online (attacchi a larga scala).
    

---

### **Perché è efficace (quando lo è)**

- Password deboli, corte o comuni.
    
- Assenza di limitazioni sul numero di tentativi (no rate limiting).
    
- Hashing delle password veloce/non salato.
    
- Riutilizzo delle credenziali su più servizi.
    

---

### **Contromisure pratiche**

- **Aumentare lo spazio delle chiavi / entropia delle password:** password lunghe e casuali; usare passphrase.
    
- **KDF lenti e salati:** bcrypt, scrypt, Argon2 con salt unici per utente (e, se necessario, pepper).
    
- **Rate limiting & throttling:** limitare tentativi per IP/utente, backoff esponenziale.
    
- **MFA (Multi-Factor Authentication):** riduce fortemente successo anche se password scoperta.
    
- **Account lockout / challenge:** blocco temporaneo o CAPTCHA dopo tentativi falliti.
    
- **Protezione infrastrutturale:** WAF, bot management, IP reputation lists.
    
- **Key length sufficiente per crittografia:** usare chiavi con entropia tale da rendere impossibile la ricerca esaustiva (p.es. AES-128/256).
    
- **Monitoraggio e alerting:** rilevare picchi nei tentativi di login e anomalie.
    
- **Non riusare le credenziali:** educare gli utenti e offrire password manager.
    
- **Protezione delle chiavi private:** uso di HSM/secure enclaves per evitare estrazione tramite brute-force fisico.
    

---

### **In breve**

> **Brute-force** = provare **tutte** (o molte) le possibilità fino a trovare la corretta.  
> È semplice ma molto dipendente dall’entropia dell’obiettivo e dalla presenza di contromisure: **password forti, KDF lenti, MFA e rate limiting** rendono l’attacco praticamente impraticabile.