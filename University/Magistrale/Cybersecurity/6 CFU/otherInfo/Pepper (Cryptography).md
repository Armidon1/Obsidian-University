# Pepper (Cryptography)

## 1. Definizione

Il **Pepper** (in italiano "pepe") è un valore segreto aggiuntivo che viene combinato con la password e il [[Salt (Cryptographic)]] prima di calcolare l'hash.

A differenza del Salt, che non è segreto e serve a garantire l'unicità, il Pepper agisce come una Chiave Segreta.

Il suo scopo è garantire che, se un attaccante ruba il database delle password (che contiene Hash e Salt), non possa comunque crackare le password perché gli manca il "pezzo mancante" segreto.

$$\text{HashFinale} = \text{Hash}(\text{Password} \ || \ \text{Salt} \ || \ \textbf{Pepper})$$

## 2. Differenza Fondamentale: Salt vs Pepper

Spesso confusi, hanno ruoli e modalità di conservazione opposti.

|**Caratteristica**|**Salt (Sale)**|**Pepper (Pepe)**|
|---|---|---|
|**Segretezza**|**Pubblico.** (Salvato in chiaro nel DB).|**SEGRETO.** (Mai salvato nel DB).|
|**Unicità**|**Unico per Utente.** Ogni utente ha il suo salt diverso.|**Globale.** Solitamente è unico per tutta l'applicazione (o per gruppi).|
|**Storage**|Salvato nel Database, nella stessa riga dell'hash.|Salvato nel codice sorgente, in variabili d'ambiente o (meglio) in un **HSM**.|
|**Scopo**|Difesa contro **Rainbow Tables** e collisioni tra utenti.|Difesa contro **Database Dump** e Brute Force offline.|

> [!abstract] Metafora Culinaria
> 
> - **Il Piatto:** La Password.
>     
> - **Il Sale:** Una spezia che metti _nel piatto_. Ogni piatto ne ha una dose diversa, ma se qualcuno ruba il piatto, vede che c'è il sale.
>     
> - **Il Pepe:** L'ingrediente segreto dello Chef, tenuto nella cassaforte in cucina. Anche se rubano il piatto finito, non possono replicarlo perché non sanno cosa c'è nella cassaforte.
>     

## 3. Dove si conserva il Pepper?

La regola d'oro è: Separation of Duties.

Il Pepper non deve MAI trovarsi nello stesso posto degli Hash (il Database).

1. **Variabili d'Ambiente / Config Files:** Metodo base. Il server applicativo conosce il pepper, il server database no. Se l'attaccante fa una [[SQL Injection]] e ruba la tabella utenti, non ottiene il pepper.
    
2. **HSM (Hardware Security Module) / Cloud KMS:** Metodo avanzato (Best Practice). L'applicazione invia l'hash al modulo hardware sicuro, che aggiunge il pepper ed esegue l'hash finale o la cifratura. Il pepper non lascia mai l'hardware blindato.
    

## 4. Pro e Contro

### Vantaggi (Pros)

- **Difesa in Profondità:** Rende inutile un leak del solo database. L'attaccante deve compromettere _sia_ il database _sia_ il server applicativo (o l'HSM) per iniziare un attacco brute-force.
    
- **Hardening:** Trasforma di fatto un semplice Hashing in un [[HMAC]] (Hash-based Message Authentication Code).
    

### Svantaggi (Cons)

- **Key Rotation Difficile:** Se il Pepper viene compromesso, devi cambiarlo. Ma cambiare il pepper significa che **tutte le password nel database diventano invalide** (perché l'hash matematicamente non corrisponderà più).
    
    - _Soluzione:_ Richiede una strategia di "re-hashing on login" (aggiornare la password dell'utente la prossima volta che accede con successo).
        
- **Single Point of Failure:** Se perdi il Pepper (es. cancelli per errore la config), **perdi l'accesso a tutti gli account utenti** per sempre. Non è recuperabile.
    

## 5. Implementazione Corretta

Non basta fare `Hash(Pass + Pepper)`. Bisogna combinare tutto.

L'approccio moderno raccomandato (es. NIST) è usare il Pepper come chiave per un algoritmo **HMAC** o per una cifratura aggiuntiva (Encrypt-then-Hash o Hash-then-Encrypt).

Esempio logico robusto:

1. Calcola l'hash lento (es. Argon2 o Bcrypt) con il Salt:
    
    $$H_1 = \text{Argon2}(\text{Password}, \text{Salt})$$
    
2. Cifra o Hmacca il risultato con il Pepper:
    
    $$H_{final} = \text{HMAC-SHA256}(H_1, \text{PepperKey})$$
    

---

**Vedi anche:**

- [[Salt (Cryptographic)]]
    
- [[Hashing]]
    
- [[HMAC]]
    
- [[Rainbow Table]]