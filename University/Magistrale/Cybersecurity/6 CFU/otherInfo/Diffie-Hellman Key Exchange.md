# 🤝 Scambio di Chiavi Diffie-Hellman (DH)

### Definizione e Scopo

Il **Diffie-Hellman (DH)** è un **protocollo di accordo sulla chiave** (_key agreement protocol_). È un metodo crittografico che permette a due parti (es. Alice e Bob), che non hanno mai comunicato prima, di stabilire in modo sicuro un **segreto condiviso** (una chiave simmetrica) su un canale di comunicazione pubblico e insicuro.

**Punto Chiave:** DH _non_ è un algoritmo di cifratura. Non cifra né decifra i dati. Il suo unico scopo è generare una chiave segreta condivisa, che sarà poi utilizzata da un altro algoritmo (come AES) per la cifratura simmetrica.

La sua sicurezza si basa sulla difficoltà computazionale del **[[Discrete Logarithm (DL) Problem|Problema del Logaritmo Discreto (DLP)]]**.

---

### Il Processo Matematico (DH "Classico")

Il protocollo si basa sull'aritmetica modulare e sull'esponenziazione.

1. Parametri Pubblici (Comuni):
    
    Alice e Bob si accordano (pubblicamente, possono essere intercettati) su due numeri:
    
    - $p$: Un numero primo molto grande (il _modulo_).
        
    - $g$: Un generatore primitivo (o _base_) modulo $p$.
        
2. **Passaggi di Alice:**
    
    - Sceglie un numero segreto privato $a$ (un intero casuale).
        
    - Calcola il suo valore pubblico: $A = g^a \pmod p$.
        
    - Invia $A$ (il suo valore pubblico) a Bob.
        
3. **Passaggi di Bob:**
    
    - Sceglie un numero segreto privato $b$ (un intero casuale).
        
    - Calcola il suo valore pubblico: $B = g^b \pmod p$.
        
    - Invia $B$ (il suo valore pubblico) ad Alice.
        
4. **Creazione del Segreto Condiviso:**
    
    - Alice riceve $B$ da Bob e calcola: $S = B^a \pmod p$.
        
    - Bob riceve $A$ da Alice e calcola: $S' = A^b \pmod p$.
        

Il Risultato:

Entrambi arrivano allo stesso identico numero segreto $S$, che ora è la loro chiave simmetrica condivisa. (magari può far comodo rivedere le proprietà del [[Modular Exponentiation Details#Elenco Proprietà Fondamentali dell'Aritmetica Modulare|Modular Exponentiation]])

- Calcolo di Alice: $$S = B^a \pmod p = (g^b (\bmod p))^a \pmod p = (g^b)^a \pmod p =g^{ba} \pmod p$$
    
- Calcolo di Bob (medesimo calcolo): $$S'= A^b \pmod p = (g^a)^b \pmod p = g^{ab} \pmod p$$
- Quindi: $S = S'$
    

Un osservatore (Eve) sul canale pubblico vede $g, p, A, B$. Per trovare il segreto $S$, Eve deve calcolare $a$ (da $A=g^a$) o $b$ (da $B=g^b$). Questo è il **[[Discrete Logarithm (DL) Problem|Problema del Logaritmo Discreto]]** (cioè: *dato $A \equiv g^a \pmod p$, $a$ è il logaritmo discreto di $A$ base $g$, modulo $p$*), che è computazionalmente infattibile se i numeri sono sufficientemente grandi.

---

### Vulnerabilità Critiche del DH Classico

Il protocollo DH "da manuale" descritto sopra è efficace **solo contro un avversario passivo (che si limita ad ascoltare)**. È criticamente vulnerabile a un avversario _attivo_.

#### 1. Attacco Man-in-the-Middle (MitM)
[[Man-in-the-Middle (MITM)]]
La vulnerabilità più grave del DH classico è la **totale mancanza di autenticazione**. Alice non ha prove di star parlando con Bob, e viceversa. Un utente malintenzionato (Trent) può interporsi attivamente nella comunicazione.

**Fasi dell'attacco MitM:**

1. **Alice $\rightarrow$ Trent:** Alice (pensando di parlare con Bob) invia il suo valore pubblico $A = g^a \pmod p$. Trent lo intercetta.
    
2. **Trent $\rightarrow$ Bob:** Trent (fingendosi Alice) genera la _propria_ chiave segreta $t$ e invia il proprio valore pubblico $T = g^t \pmod p$ a Bob.
    
3. **Bob $\rightarrow$ Trent:** Bob (pensando di parlare con Alice) invia il suo valore pubblico $B = g^b \pmod p$. Trent lo intercetta.
    
4. **Trent $\rightarrow$ Alice:** Trent (fingendosi Bob) invia il suo valore pubblico $T = g^t \pmod p$ ad Alice.
    

**Effetti dell'attacco:**

- Alice calcola una chiave segreta condivisa con Trent:
    
    $K_{AT} = T^a \pmod p = (g^t)^a \pmod p = g^{ta} \pmod p$
    
- Bob calcola una chiave segreta condivisa (diversa) con Trent:
    
    $K_{BT} = T^b \pmod p = (g^t)^b \pmod p = g^{tb} \pmod p$
    
- Trent calcola **entrambe** le chiavi:
    
    - Per parlare con Alice: $K_{TA} = A^t \pmod p = (g^a)^t \pmod p = g^{at} \pmod p$
        
    - Per parlare con Bob: $K_{TB} = B^t \pmod p = (g^b)^t \pmod p = g^{bt} \pmod p$
        

Alice e Bob credono di avere un canale sicuro, ma Trent è nel mezzo, intercetta ogni messaggio, lo decifra con una chiave, lo legge/modifica e lo ricifra con l'altra chiave.

**Mitigazione:** DH **non deve mai essere usato da solo**. Deve essere **autenticato**. In pratica (come in TLS), il server "firma" i suoi parametri DH (es. $B$) usando la sua chiave privata a lungo termine (es. RSA o ECDSA) e un certificato X.509 per dimostrare la sua identità.

#### 2. Logjam Attack

Questo attacco sfrutta l'uso di numeri primi ($p$) piccoli (es. 512-bit) o, peggio, l'uso di numeri primi comuni/condivisi tra molti server. Un attaccante può eseguire un'enorme pre-computazione su un singolo primo $p$ e usarla per rompere rapidamente le connessioni DH che lo utilizzano.

**Mitigazione:** Usare primi $\ge$ 2048-bit, unici e sicuri.

---

### Proprietà Fondamentali e Varianti (PFS)

Per risolvere i problemi di sicurezza e migliorare le prestazioni, sono state introdotte delle varianti di DH.

#### Perfect Forward Secrecy (PFS)
[[Perfect Forward Secrecy (PFS)]]

- **Definizione:** Un sistema crittografico ha Perfect Forward Secrecy (PFS) se genera **chiavi pubbliche casuali e temporanee per ogni nuova sessione**.
    
- **Implicazione:** La compromissione di una singola chiave (ad esempio, la chiave privata a lungo termine di un server) **non compromette le chiavi delle sessioni _passate_ o _future_**. Se un hacker registra tutto il traffico cifrato di oggi e _domani_ ruba la chiave principale del server, _non_ potrà comunque decifrare il traffico di oggi.
    

#### Static DH vs. Ephemeral DH (DHE)
[[Ephemeral DH (DHE)]]
Il concetto di PFS ci porta a una distinzione fondamentale:

|**Caratteristica**|**Static Diffie-Hellman**|**Ephemeral Diffie-Hellman (DHE)**|
|---|---|---|
|**Durata Chiave**|Utilizza una coppia di chiavi fissa e a lungo termine (tipicamente lato server).|Genera una **nuova coppia di chiavi temporanea** per **ogni** sessione.|
|**PFS**|**NON FORNISCE** Perfect Forward Secrecy.|**FORNISCE** Perfect Forward Secrecy.|
|**Rischio**|Se la chiave DH statica viene compromessa, tutte le sessioni passate e future sono compromesse.|La compromissione di una chiave di sessione non ha impatto su nessun'altra sessione.|
|**Uso**|Scenari specifici (oggi rari) in cui è richiesta la gestione di chiavi a lungo termine.|Lo **standard** per la comunicazione sicura moderna (es. TLS 1.3).|

---

### Varianti Moderne: Elliptic Curve Diffie-Hellman (ECDH)
[[ECDH]]
Il concetto di Diffie-Hellman può essere applicato a qualsiasi gruppo matematico in cui il problema del logaritmo discreto è difficile.

- **ECDH (Elliptic Curve Diffie-Hellman):** È una variante moderna e altamente efficiente di DH che utilizza il gruppo di punti su una **curva ellittica**.
    
- **Flusso Identico:** Il protocollo (scambio di chiavi pubbliche, calcolo del segreto) è identico, ma la matematica sottostante è diversa.
    
- **Vantaggio Enorme:** Fornisce lo stesso livello di sicurezza di DH ma con **chiavi molto più piccole**.
    
    - Esempio: una chiave ECDH a 256 bit è circa equivalente in forza a una chiave DH a 3072 bit.
        
- Questo rende ECDH molto più veloce, con un minore carico computazionale, ed è la scelta preferita per i dispositivi mobili e moderni.
    
- La versione effimera, **[[ECDHE]]**, è la combinazione di [[Elliptic Curve Cryptography - ECC]] + Ephemeral DH, ed è la base della maggior parte delle connessioni web sicure ([[HTTPS]]) oggi.

