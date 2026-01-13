guardare sempre prima [[CS 6cfu - Domande esame]]

Ecco i concetti chiave dell'**Autenticazione Password-Based** spiegati nel dettaglio, basati rigorosamente sulle domande d'esame reali (2012-2025).

---

### 1. Il Protocollo Challenge-Response (Design & Reflection Attack)

La Domanda d'Esame:

"Progetta un protocollo di autenticazione password-based sicuro su canale insicuro che prevenga Replay e Reflection." oppure "Perché il protocollo X è vulnerabile al Reflection Attack?"

La Spiegazione (Il "Perché"):

Il problema fondamentale è che non puoi mandare la password in chiaro. La soluzione ingenua è mandare l'hash della password. Ma se mandi sempre lo stesso hash, un attaccante lo intercetta e lo riusa domani (Replay Attack).

Per risolvere il Replay, usi una "sfida" (Challenge/Nonce) che cambia sempre.

Il server dice: "Ciframi questo numero casuale $N$". Tu lo cifri. Il server pensa: "Solo chi ha la password poteva cifrare $N$ correttamente".

Il Problema della Riflessione (Reflection):

Se il protocollo è simmetrico (cioè Alice e Bob fanno le stesse identiche operazioni e condividono la stessa chiave/password), Trudy può fregare Bob.

Se Bob sfida Trudy con un Nonce $N$, Trudy (che non sa la password) apre una seconda connessione verso Bob e gli manda lo stesso Nonce $N$. Bob, essendo onesto, lo cifra e lo rimanda a Trudy. Trudy prende la risposta e la usa per chiudere la prima connessione.

La Soluzione "Blindata":

Per impedire la riflessione, devi rompere la simmetria. La risposta di Alice deve essere diversa da quella di Bob.

Come? Inserendo l'identità ("Alice" o "Server") dentro la crittografia.

**Cosa scrivere all'esame (Il Protocollo Sicuro):**

1. **Client $\to$ Server:** `Hello, sono Alice`
    
2. **Server $\to$ Client:** `Nonce_S` (Numero casuale)
    
3. **Client $\to$ Server:** $H(\text{Password}, \text{Nonce}_S, \text{"Alice"})$
    

_Spiegazione:_

- Il `Nonce_S` cambia ogni volta $\to$ Previene **Replay**.
    
- La stringa `"Alice"` dentro l'hash $\to$ Previene **Reflection** (perché se il server dovesse autenticarsi, userebbe la stringa "Server", quindi le due risposte non sono intercambiabili).
    

---

### 2. Salt e Rainbow Tables

La Domanda d'Esame:

"Cosa sono le Rainbow Tables? Cos'è il Salting e perché si usa?"

La Spiegazione (Il "Perché"):

Le funzioni di Hash (come SHA-256) sono deterministiche.

$$H(\text{"password123"}) = \text{ef92b...}$$

Sarà sempre così.

- **Rainbow Tables:** Un attaccante furbo non ricalcola l'hash ogni volta. Si pre-calcola (o scarica) una tabella gigante con miliardi di password comuni e i loro hash. Quando ruba il tuo database, cerca il tuo hash nella tabella. Se lo trova, ha la password in un istante (Time-Memory Tradeoff).
    
- Il Salt (Sale): È l'antidoto. Aggiungiamo una stringa casuale pubblica ($S$) alla password prima di fare l'hash.
    
    $$H(\text{"password123"} + \text{SaltUnico})$$
    
    Ora, due utenti con la stessa password "password123" avranno due hash completamente diversi perché hanno due Salt diversi.
    

**Cosa scrivere all'esame:**

- **Rainbow Tables:** Tabelle precalcolate di catene di hash che permettono di invertire l'hashing in tempo costante (O(1)).
    
- **Salt:** Dati casuali concatenati alla password. Serve a:
    
    1. Rendere diversi gli hash di password uguali.
        
    2. **Rendere inutili le Rainbow Tables** (l'attaccante dovrebbe ricalcolare l'intera tabella per ogni singolo Salt usato nel database, il che è computazionalmente impossibile).
        

---

### 3. Attacco a Dizionario Offline vs Online

La Domanda d'Esame:

"Descrivi attentamente cos'è un attacco a dizionario offline."

La Spiegazione (Il "Perché"):

C'è una differenza enorme tra provare a indovinare la password sul sito web della banca e provare a indovinarla avendo rubato il file delle password della banca.

- **Online:** Devi parlare col server. Il server è lento e dopo 3 tentativi ti blocca l'account. Sei limitato dalle regole del server.
    
- **Offline:** Hai rubato il file degli hash (es. tramite SQL Injection). Te lo porti a casa. Non devi parlare col server.
    
    - Puoi provare 100 miliardi di password al secondo usando la tua scheda grafica (GPU).
        
    - Non c'è nessun blocco account.
        
    - L'unica difesa è usare una funzione di hash _lentissima_ (KDF).
        

Cosa scrivere all'esame:

L'attacco offline avviene quando l'attaccante ottiene il file delle password (hash). L'attaccante calcola localmente l'hash di milioni di parole del dizionario e le confronta con quelle rubate. È molto più veloce dell'attacco online perché non c'è latenza di rete e non ci sono meccanismi di blocco (lockout) che limitano i tentativi.

---

### 4. Key Derivation Functions (KDF)

La Domanda d'Esame:

"Cos'è una PBKDF e perché è utile?"

La Spiegazione (Il "Perché"):

Come ci difendiamo dall'attacco offline di cui sopra? Le GPU moderne sono troppo veloci. Dobbiamo rendere l'operazione di verifica della password lenta apposta.

Una KDF (come PBKDF2, bcrypt, Argon2) non fa un solo hash, ne fa 100.000 in sequenza.

$$H(H(H(...H(P)...)))$$

Per l'utente legittimo, aspettare 0.5 secondi per il login è accettabile. Per l'attaccante che deve provare 1 miliardo di password, 0.5 secondi a tentativo significano secoli.

Cosa scrivere all'esame:

Una KDF è una funzione crittografica progettata per essere computazionalmente costosa (lenta) e/o richiedere molta memoria. Serve a trasformare una password (che ha bassa entropia) in una chiave crittografica sicura, rallentando drasticamente gli attacchi di forza bruta o a dizionario offline.

---

### 5. Lamport's Hash (OTP) e Dispositivi

La Domanda d'Esame:

"Perché i server che usano Lamport hashing preferiscono che l'utente usi sempre lo stesso dispositivo?"

La Spiegazione (Il "Perché"):

Lamport usa una catena inversa.

Generazione: $x_n = H(x_{n-1})$.

Uso: Il server ha $x_{100}$. Tu gli mandi $x_{99}$. Il server fa l'hash di $x_{99}$, vede che viene $x_{100}$, e accetta. Poi si salva $x_{99}$ come nuovo riferimento. La prossima volta vuole $x_{98}$.

È un conto alla rovescia sincronizzato.

Se tu usi il PC e consumi 5 token (arrivi a $x_{95}$), il server si aspetta $x_{94}$.

Se poi prendi il Tablet (che era rimasto a $x_{100}$) e provi a loggarti, il Tablet calcolerà $x_{99}$.

Il server riceve $x_{99}$ ma lui è già a $x_{95}$! Penserà che sia un Replay Attack (un vecchio token riusato) e rifiuterà l'accesso.

Cosa scrivere all'esame:

Il protocollo Lamport si basa su una catena di hash e un contatore decrescente sincronizzato tra client e server. Se l'utente cambia dispositivo, i contatori locali dei dispositivi non saranno allineati con quello del server (uno sarà "indietro"), causando il fallimento dell'autenticazione o falsi allarmi di Replay Attack.