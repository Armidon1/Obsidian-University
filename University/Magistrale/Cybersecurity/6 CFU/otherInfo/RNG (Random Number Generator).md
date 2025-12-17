# Random Number Genenerator (RNG)

**Tags:** #ingegneria #crittografia #cybersecurity #RNG #PRNG #CSPRNG

## Definizione

Un **RNG** (Generatore di Numeri Casuali) è un sistema, hardware o software, progettato per produrre una sequenza di numeri o simboli che non possiedono alcun pattern riconoscibile e che, idealmente, non possono essere previsti ragionevolmente.

In crittografia, l'RNG è il componente **fondamentale** per la sicurezza: se i numeri generati sono prevedibili, qualsiasi chiave segreta derivata da essi è compromessa.

## Le due Famiglie Principali

1. **[[TRNG (True Random Number Generator)]]:**
    
    - **Fonte:** Fenomeni fisici caotici (rumore termico, decadimento radioattivo, interruzioni hardware).
        
    - **Caratteristica:** Non deterministico. Vera entropia.
        
    - **Uso:** Generazione di chiavi master, generazione del _Seed_ per i PRNG.
        
2. **[[PRNG (Pseudo-Random Number Generator)]]:**
    
    - **Fonte:** Algoritmi matematici deterministici.
        
    - **Caratteristica:** Deterministico. Dato un input iniziale (**Seed**), la sequenza è fissa e riproducibile.
        
    - **Uso:** Simulazioni, cifrari a flusso, generazione veloce di numeri (se _Cryptographically Secure_).
        

> [!abstract] Concetto Chiave
> 
> Un RNG crittografico deve superare il Next-Bit Test: data una sequenza di bit generati, deve essere computazionalmente impossibile prevedere il bit successivo con una probabilità superiore al 50%.

---

## 1. Introduzione e Importanza della Casualità

> "La generazione di numeri casuali è troppo importante per essere lasciata al caso."
> 
> — Robert Coveyou, Oak Ridge National Laboratory

Nel contesto della sicurezza, non possiamo affidarci a una progettazione scadente o al semplice "caso". I numeri casuali sono le **fondamenta** di molti algoritmi crittografici. Se il generatore è debole, l'intero sistema di sicurezza crolla.

**Perché ne abbiamo bisogno?**

- **Chiavi di Sessione:** Chiavi temporanee per cifrare le comunicazioni (evitando che vengano indovinate).
    
- **Nonce e Salt:** Valori unici per prevenire attacchi di replay o rafforzare le password.
    
- **Generazione Chiavi:** Creazione di coppie di chiavi pubbliche/private 1.
    

> [!tip] Exam Focus
> 
> La sicurezza di un generatore si misura rispetto alla potenza computazionale dell'avversario.
> 
> Data una sequenza di chiavi di sessione passate, la probabilità di predire correttamente la prossima deve essere trascurabile 2.

---

## 2. Generatori di Casualità: TRNG vs PRNG

Esistono due metodi principali per generare numeri casuali.

### A. [[TRNG (True Random Number Generator)]]

Questi si basano su **fenomeni fisici** che si presume siano intrinsecamente casuali.

- **Esempi:** Temperatura, rumore atmosferico, decadimento radioattivo, rumore termico.
    
- **Problemi:** Possono avere bias (richiedono "whitening", sbiancamento) e la precisione di misurazione limita l'estrazione di bit di entropia 3.
    

### B. [[PRNG (Pseudo-Random Number Generator)]]

Questo è l'approccio computazionale più comune. Utilizza un **algoritmo deterministico**.

- **Meccanismo:** Dato un input iniziale (**Seed** o Seme), l'algoritmo produce una lunga sequenza di numeri che _sembrano_ casuali.
    
- **Il Paradosso:** Poiché l'algoritmo è deterministico, fornendo lo stesso Seed si ottiene l'**esatta stessa sequenza di output** 4.
    


> [!abstract] Visual Analysis
> 
> **What to look at:** Il diagramma mostra tipicamente un input (Seed) che entra in una "scatola" (Algoritmo) per produrre un flusso di numeri.
> 
> **Meaning:** La sicurezza dipende interamente dalla segretezza e dall'imprevedibilità del Seed. Secondo il Principio di Kerckhoffs, l'avversario conosce l'algoritmo; non deve conoscere il Seed.

---

## 3. La Fonte di Entropia (Il Seed)

Poiché il PRNG è deterministico, la vera casualità deve provenire dal **Seed**. Dobbiamo raccogliere dati che siano difficili da replicare per un attaccante remoto.

**Fonti Comuni:**

- **Sistema/Rete:** Orologio, spazio libero su disco, numero di file, code I/O, tempi di inter-arrivo dei pacchetti.
    
- **Input Utente:** Velocità di digitazione sulla tastiera, movimenti del mouse 5.
    

> [!example] Professor's Example: Mouse Movement
> 
> Molti sistemi ti chiedono di "muovere il mouse a caso" per generare una chiave. Non è magia. Anche se un avversario ti vede muovere il mouse, non può replicare l'esatta traiettoria e il tempismo fino al millisecondo. Questa differenza di tempismo fornisce i bit di entropia necessari.

### Il Problema della "Quantità di Entropia"

Spesso abbiamo l'illusione della casualità.

- **Granularità dell'Orologio:** Usare solo i millisecondi potrebbe fornire solo ~10 bit di casualità ($2^{10} \approx 1000$ combinazioni).
    
- **Giorno/Ora:** Questi sono facilmente indovinabili da un attaccante.
    
- **Soluzione:** Mescolare diverse fonti usando funzioni crittografiche ([[Hashing]]).
    

---

## 4. Case Studies: Fallimenti Storici

Errori nell'implementazione degli RNG hanno causato vulnerabilità massicce in passato.

### Caso 1: Netscape 1.1 (1996)

Netscape utilizzava un generatore debole per le chiavi SSL. Il codice sorgente rivelò che il seed era derivato da valori prevedibili.

**Here is the exact implementation shown in the slides:**
```C
/* Netscape 1.1  seeding & key generation (1996) */

global variable seed;

RNG_CreateContext()
    (seconds, microseconds) = time of day;
    /* Time elapsed since 1970 */
    pid = process ID; ppid = parent process ID;
    a = mklcpr(microseconds);
    b = mklcpr(pid + seconds + (ppid << 12));
    seed = MD5(a, b);
    MD5 broken since 1996
    /* not cryptographically significant */
mklcpr(x)
    return ((0xDEECE66D * x + 0x2BBB62DC) >> 1);

RNG_GenerateRandomBytes()
    x = MD5(seed);
    seed = seed + 1;
    return x;
```

> [!abstract] Code Analysis
> 
> **Vulnerabilità:**
> 
> - `seconds` sono noti.
>     
> - `pid` e `ppid` erano spesso prevedibili o sequenziali sui sistemi UNIX.
>     
> - **Vettore d'Attacco:** Un attaccante poteva inviare un'email al demone `sendmail`. Il **Message-ID** della risposta conteneva il PID.
>     
> - **Risultato:** L'entropia crollava a ~47 bit. La chiave poteva essere rotta in pochi minuti.
>     

### Caso 2: Debian OpenSSL (2008)

Un bug catastrofico introdotto "ripulendo" il codice per soddisfare un debugger.

- **La Causa:** Uno sviluppatore usò **Valgrind** (strumento di debug) che avvisava dell'uso di una "Variabile non inizializzata" ("Use of uninitialized variable").
    
- **La "Fix":** Lo sviluppatore rimosse la riga `MD_Update(&m,buf,j);` che aggiungeva entropia non inizializzata al pool.
    
- **Il Risultato:** L'unica variabile rimasta era il **Process ID** (max 32.768 su Linux).
    
- **Impatto:** Qualsiasi chiave SSH/SSL generata su Debian/Ubuntu in quel periodo era banalmente indovinabile (solo ~32.000 possibilità).
    

> [!failure] Common Pitfall
> 
> **Divulgare il Seed:** Mai includere la fonte del seed (come l'ora del giorno) in parti non cifrate del messaggio (es. header), come accaduto in alcune implementazioni 9.

---

## 5. PRNG vs. CS-PRNG

Non tutti i generatori sono adatti alla sicurezza. Dobbiamo distinguere tra PRNG standard e PRNG **Crittograficamente Sicuri** (CS-PRNG).


> [!abstract] Visual Analysis
>![[Pasted image 20251216113306.png]] 
> **What to look at:** La tabella di confronto che evidenzia "Prevedibilità" e "Proprietà di Sicurezza".
> 
> **Meaning:** I PRNG si concentrano sulla distribuzione statistica (per giochi/simulazioni). I CS-PRNG si concentrano sull'imprevedibilità (per la crittografia).

![[Pasted image 20251216113618.png]]

### Technical Logic / Math

**Challenge: Is this a PRNG or [[CS-PRNG (Cryptographically Secure PRNG)|CS-PRNG]]?**

```C
hash function H
random initial seed s
y = s
for i = 1 to n do
    y = H(y)
    output(y)
```

**Requisiti per CS-PRNG:**

1. **Next-Bit Test:** Dati $k$ bit, nessun algoritmo può prevedere il bit $(k+1)$-esimo con probabilità $> 50\%$.
    
2. **Forward Secrecy:** Se lo stato viene compromesso, le chiavi _future_ rimangono sicure.
	    
3. **Backward Secrecy:** Se lo stato viene compromesso, le chiavi _passate_ non possono essere ricostruite.
    

---

## 6. Criteri di Valutazione BSI

L'Ufficio Federale Tedesco per la Sicurezza Informatica (BSI) definisce 4 criteri per la qualità degli RNG:

- **K1:** Sequenza senza ovvi pattern ripetitivi.
    
- **K2:** Indistinguibile dal "vero random" tramite test statistici (Monobit, Poker, Runs).
    
- **K3:** Impossibile calcolare output passati/futuri o lo stato interno partendo dall'**output**.
    
- **K4 (Crypto Standard):** Impossibile calcolare output passati **anche se lo stato interno è noto** (richiede meccanismi di Forward Secrecy) 12.
    

---

## 7. Algoritmi e Soluzioni Pratiche

### A.[[CS-PRNG based by Cipher of a Counter]]

![[Pasted image 20251216122553.png]]

Usa un cifrario a blocchi (come AES) in maniera ciclica.

**Here is the exact implementation shown in the slides:**

```c
cyclic cryptography: use counter + cipher
Meyer and Matyas, 1982
crypto algorithm E
C + 1 mod N
C
master key Km
Xi = E[Km, C + 1]
```

### B. [[CS-PRNG based by RSA]]

Sfrutta la difficoltà matematica nell'invertire RSA. Provabilmente sicuro ma lento.

**Here is the exact implementation shown in the slides:**

```c
prime numbers p, q
n = p∙q
integer e s.t. GCD(e, (p-1)∙(q-1)) = 1
z = seed
loop
    zi = (zi-1)^e mod n
    i = i +1
    output:  least significant bit of zi
```

### C. [[CS-PRNG based by BBS]]

Basato sul problema dei residui quadratici.

**Here is the exact implementation shown in the slides:**

```c
choose p, q big prime s.t. p ≡ q ≡ 3 (mod 4)
n = p∙q
randomly choose s s.t. GCD(s, n) = 1
output the sequence of bits Bi

X0 = s2 mod n
for i = 1 to ∞
    Xi = (Xi-1)^2 mod n
    Bi = Xi mod 2
    return Bi
```

### D. [[CS-PRNG based by CTR_DRBG (AES)]]

Best practice attuale (NIST SP 800-90A). Usa AES in modalità Counter (CTR) con capacità di reseeding.

**Here is the exact implementation shown in the slides:**

```c
Maybe the current best (Counter mode Deterministic Random Bit Generator, 2012)
State: Key K, counter V
Block cipher: AES-128 / AES-256 in CTR mode
Generate:
    V ⟵ V + 1 (mod  2block size)
    out_block = EK(V)
    Repeat until enough bits produced
Update:  regenerate K and V by encrypting V+1, V+2, … with current K and using the output blocks to form the new state
Security: Forward & backward secure (if reseeded periodically)
```

---

## 8. Best Practices

1. **"Don't roll your own crypto":** Mai inventare il proprio generatore.
    
2. **Evitare `rand()`:** Le funzioni delle librerie standard sono per simulazioni, non per la sicurezza.
    
3. **Usare API del Sistema Operativo:** `/dev/urandom` (Linux) o `CryptGenRandom` (Windows). Queste librerie gestiscono la raccolta di entropia e l'hashing in modo sicuro.
    
4. **Riferimento:** RFC 1750 13.


**Vedi anche:**
* [[One-Time Pad (OTP)]] (Richiede generatori perfetti)
* [[RSA]] (Esempio di algoritmo che necessita di PRG sicuri per la generazione chiavi)
* [[Differenza tra PRF e PRNG]]