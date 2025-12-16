# Salt + Pepper: La Strategia Completa

## 1. Il Concetto: Difesa in Profondità

L'utilizzo congiunto di [[Salt (Cryptographic)|Salt]] e [[Pepper (Cryptography)|Pepper]] rappresenta lo stato dell'arte per la memorizzazione sicura delle password.

Questa architettura applica il principio della Defense in Depth (Difesa in Profondità): se un livello di sicurezza fallisce (es. furto del database), ce n'è un altro che protegge i dati.

### La Formula Completa

Mentre il Salt garantisce l'unicità e il Pepper garantisce la segretezza, l'hash finale salvato nel database è il risultato di:

$$\text{StoredHash} = \text{KDF}(\text{Password} \ || \ \text{Salt}, \ \text{Pepper})$$

_(Dove KDF è una funzione lenta come Argon2 o PBKDF2)_

## 2. Tabella Comparativa: Chi fa cosa?

Per capire perché servono entrambi, bisogna vedere come si completano a vicenda:

| Caratteristica | [[Salt (Cryptographic)|SALT]] (Il Sale) | [[Pepper (Cryptography)|PEPPER]] (Il Pepe) |

| :--- | :--- | :--- |

| Visibilità | Pubblico (salvato nel DB). | Segreto (salvato nell'App/HSM). |

| Unicità | Unico per Utente (Random). | Unico per Applicazione (Globale). |

| Minaccia Mitigata | Rainbow Tables (attacchi precalcolati) e collisioni di hash identici. | Database Breach (furto del solo file DB) e Brute Force offline. |

| Gestione | Generato alla creazione dell'utente. | Configurato al deploy dell'applicazione. |

| Se lo perdi... | Nessun problema (è nel DB). | Disastro: Nessuno può più fare login. |

## 3. Analisi dello Scenario di Attacco

Immaginiamo che un hacker riesca a eseguire una **[[SQL Injection]]** e scarichi l'intera tabella `users` contenente `username`, `salt` e `password_hash`.

### Scenario A: Solo Salt

1. L'hacker ha l'hash e il salt.
    
2. Può lanciare un attacco **Brute Force Offline** o a Dizionario sul suo computer potente.
    
3. Prende una parola ("password123"), aggiunge il salt che ha rubato, calcola l'hash e vede se corrisponde.
    
4. **Risultato:** Con tempo sufficiente, le password deboli vengono scoperte.
    

### Scenario B: Salt + Pepper

1. L'hacker ha l'hash e il salt dal DB.
    
2. Tenta il Brute Force: prende "password123", aggiunge il salt... **ma manca il Pepper**.
    
3. Non conoscendo il Pepper (che è rimasto sul server applicativo o nell'HSM e non nel DB), non può calcolare l'hash corretto per fare il confronto.
    
4. **Risultato:** Il database rubato è inutilizzabile (matematicamente inutile) senza compromettere anche il server delle applicazioni.
    

## 4. Architettura Ideale (Implementation Flow)

Il modo più robusto per combinare i due non è una semplice concatenazione, ma l'uso di un **[[HMAC]]**.

1. **Input:** L'utente inserisce la `Password`.
    
2. Hashing (Lento): Il sistema recupera il Salt e applica una funzione lenta (es. Bcrypt o Argon2).
    
    $$H_{temp} = \text{Bcrypt}(\text{Password}, \text{Salt})$$
    
3. Peppering (HMAC): Il sistema prende l'hash temporaneo e lo "firma" usando il Pepper come chiave segreta.
    
    $$H_{final} = \text{HMAC-SHA256}(H_{temp}, \text{PepperKey})$$
    
4. **Verifica:** Il risultato $H_{final}$ viene confrontato con quello nel database.
    

> [!warning] Il rischio del "Single Point of Failure"
> 
> Usare Salt + Pepper è molto sicuro, ma introduce un rischio operativo: La gestione del Pepper.
> 
> Se il file di configurazione con il Pepper viene cancellato o corrotto e non c'è un backup, tutti gli hash nel database diventano irreversibilmente illeggibili. Non c'è modo di recuperare gli account degli utenti se non resettando tutte le password.

---

**Vedi anche:**

- [[Salt (Cryptographic)]]
    
- [[Pepper (Cryptography)]]
    
- [[Hashing]]
    
- [[HMAC]]
    
- [[KDF (Key Derivation Function)]]