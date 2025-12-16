# Criptosistema ElGamal

**Tags:** #crittografia #asimmetrica #ElGamal #DLP #matematica #sicurezza #storia

## 1. Introduzione e Contesto Storico

**ElGamal** è un criptosistema a chiave pubblica progettato da **Taher Elgamal** (spesso chiamato il "padre di [[SSL]]", vedi [[Il padre di SSL 3.0|qui]]). È storicamente significativo perché definisce due metodi distinti basati sulla stessa matematica:

1. Uno schema di **Cifratura** (per la [[Confidentiality]]).
    
2. Uno schema di **[[Digital Signature]]** (per l'[[Authentication]]).
    

Entrambi i metodi sono ispirati al protocollo di scambio chiavi **[[Diffie-Hellman Key Exchange|Diffie-Hellman]]** e basano la loro sicurezza sulla difficoltà computazionale del **[[Discrete Logarithm (DL) Problem]]** su campi finiti.

> [!abstract] Visual Analysis
> 
> ![[Pasted image 20251216162938.png]]
> 
> Meaning: Il diagramma visualizza come il [[Digital Signature Standard (DSS)]] sia un'evoluzione/standardizzazione basata su ElGamal, che a sua volta affonda le radici nei principi di [[Diffie-Hellman Key Exchange]] e nella [[Modular Arithmetic]].

---

## 2. ElGamal Encryption (Cifratura)

La cifratura ElGamal è nota per essere **probabilistica**: cifrare lo stesso messaggio più volte produce testi cifrati diversi (grazie a un fattore casuale $k$). Questo la rende intrinsecamente resistente agli attacchi [[Chosen-Plaintext Attack (CPA)]]_, a differenza di RSA "textbook" che è deterministico.

### A. Generazione delle Chiavi (Setup)

Prima di iniziare, si concordano i **Parametri Pubblici**: un numero primo grande $p$ e un generatore $g$ (ma che cos'è il "generatore $g$"? guarda [[Generatore g (radice primitiva)|qui]]).

- **Chiave Privata ($x$ o $b$):** Bob sceglie un intero casuale $x \in \{1, \dots, p-2\}$.
    
- **Chiave Pubblica ($y$ o $B$):** Bob calcola $y = g^x \pmod p$.
    
- _La chiave pubblica è $(p, g, y)$. La chiave privata è $x$._
    
Notiamo che questo è esattamente identico all'algoritmo di [[Diffie-Hellman Key Exchange]] per la creazione delle chiavi, solo che qui la chiave privata è $x \in \{1, \dots, p-2\}$, anziché un valore casuale molto grande. Nota che Diffie-Hellman viene usato prevalentemente per la key exchange e non è un algoritmo di cifratura. Qui invece vediamo che Elgamal sfrutta il [[Discrete Logarithm (DL) Problem]] per cifrare e decifrare un messaggio.

### B. Algoritmo di Cifratura

Alice vuole inviare un messaggio $m$ a Bob.

1. Alice ottiene la chiave pubblica di Bob $(p, g, y)$.
    
2. Sceglie un numero **casuale $k$** (chiamato anche $y_{rand}$ o _[[Nonce]]_) per questa sessione.
    
3. Calcola la coppia di testo cifrato $(C_1, C_2)$:
    
    $$\begin{align*} C_1 &= g^k \pmod p \quad (\text{Componente casuale}) \\ C_2 &= m \cdot y^k \pmod p \quad (\text{Messaggio mascherato}) \end{align*}$$
    

> [!warning] Espansione del Messaggio
> 
> Il testo cifrato è composto da due numeri $(C_1, C_2)$.
> 
> Questo significa che il ciphertext è due volte più grande del messaggio originale $m$. Questo è uno svantaggio significativo rispetto a RSA.

### C. Algoritmo di Decifratura

Bob riceve $(C_1, C_2)$ e usa la sua chiave privata $x$.

1. Calcola il segreto condiviso (maschera): $S = C_1^x \pmod p$.
    
    (Nota: $C_1^x = (g^k)^x = g^{kx} = y^k$, che è esattamente la maschera usata da Alice).
    
2. Calcola l'inverso $S^{-1}$ e recupera il messaggio:
    
    $$m = C_2 \cdot (C_1^x)^{-1} \pmod p$$
    

come in Diffie-Hellman, la difficoltà è quella del [[Discrete Logarithm (DL) Problem]], dove è computazionalmente impossibile dato $y = g^x \pmod p$, è computazionalmente impossibile ricavarsi $x$ partendo da $y$ e $p$ se i numeri sono molto grandi. 

---

## 3. ElGamal Signature Scheme (Firma)

A differenza di RSA, dove la firma è spesso descritta come "decifratura con la chiave privata", la firma ElGamal utilizza un algoritmo dedicato che genera una coppia di valori $(r, s)$.

> [!example] Professor's Note
> 
> In RSA, per ottenere firme diverse per lo stesso documento, serve un framework esterno (padding PSS). In ElGamal, la casualità è parte integrante dell'algoritmo. Non serve pre-processing esterno per garantire l'unicità.

### A. Generazione Chiavi (Firma)

Simile alla cifratura:

- $p$: Primo grande (es. 1024+ bit).
    
- $x$: Chiave privata random in $[1, p-2]$.
    
- $y = g^x \pmod p$: Chiave pubblica.
    
ricordiamo che (g,p,y) compongono la chiave pubblica.
### B. Algoritmo di Firma

Per firmare **un hash del messaggio** (prima differenza dalla cifratura) $m = H(M)$:

1. Scegli un numero casuale $k$ tale che $MCD(k, p-1) = 1$ ($k$ e $p-1$ sono [[Coprime]]).
    
2. Calcola $r$:
    
    $$r = g^k \pmod p$$
    
3. Calcola $s$ (l'equazione della firma):
    
    $$s = (m - r \cdot x) \cdot k^{-1} \pmod{p-1}$$
    
    (Se $s=0$, ricomincia con un nuovo $k$.)
    

> [!abstract] Math Analysis
> 
> - **Pre-processing:** Notare che il calcolo di $r = g^k$ **non dipende dal messaggio** $m$. Questo permette di pre-calcolare $r$ (offline), migliorando l'efficienza durante la fase di firma in tempo reale.
>     
> - **Modulo Misto:** Il calcolo di $r$ è modulo $p$, ma l'equazione di $s$ è modulo $p-1$ (Teorema di Eulero).
>     

### C. Verifica

Il destinatario accetta la firma $(r, s)$ se:

$$0 < r < p \quad \land \quad y^r \cdot r^s \equiv g^m \pmod p$$

> [!tip] Exam Focus: Perché funziona?
> 
> L'uguaglianza regge perché:
> 
> $$y^r r^s = g^{xr} g^{ks} = g^{xr + k(m-rx)k^{-1}} = g^{xr + m - rx} = g^m$$

---

## 4. Analisi Critica e Implicazioni Ingegneristiche

### Vulnerabilità Catastrofica: Riuso di $k$

Il numero casuale $k$ (nonce) deve essere unico per ogni messaggio.

Se Alice usa lo stesso $k$ per firmare due messaggi diversi $m_1$ e $m_2$:

1. Il valore $r$ sarà identico per entrambi ($r = g^k$).
    
2. Un attaccante può mettere a sistema le due equazioni della firma.
    
3. **Risultato:** L'attaccante può calcolare facilmente la **chiave privata $x$**. Senza un [[PRNG (Pseudo-Random Number Generator)|PRNG]] sicuro, il sistema crolla.
    

### Confronto: ElGamal vs RSA

|**Feature**|**ElGamal**|**RSA**|
|---|---|---|
|**Sicurezza**|Discrete Logarithm (DLP)|Integer Factorization|
|**Cifratura**|**Probabilistica** (output diverso ogni volta)|Deterministica (senza padding OAEP)|
|**Dimensione Ciphertext**|**Doppia** (2 componenti: $C_1, C_2$)|Singola (stessa dim. del modulo)|
|**Velocità Verifica**|Lenta (esponenziazioni multiple)|Veloce (spesso $e=65537$)|
|**Firma**|Coppia $(r, s)$|Singolo valore|
|**Randomness**|**Obbligatoria** per ogni operazione|Necessaria solo nel padding (PSS/OAEP)|

> [!abstract] Visual Analysis
> 
> ![[Pasted image 20251216162823.png]]
> 
> Meaning: RSA è preferito per ambienti che richiedono verifica veloce (es. certificati SSL nei browser), mentre ElGamal (e la sua variante DSA) è utile quando si può sfruttare il pre-calcolo offline.

# In che modo Diffie-Hellman è "integrato" in ElGamal?

La risposta breve è: **ElGamal _È_ essenzialmente uno [[Diffie-Hellman Key Exchange|scambio Diffie-Hellman]] "congelato" e usato per nascondere un messaggio.**

Ecco la spiegazione passo dopo passo di come ElGamal trasforma il meccanismo di Diffie-Hellman in un sistema di cifratura.

---

### Il concetto chiave: Da "Accordo" a "Cifratura"

Nel Diffie-Hellman standard (interattivo), io e te siamo online e ci scambiamo valori in tempo reale per creare una chiave $S$.

In ElGamal, vogliamo inviare un messaggio cifrato (come una email) senza che l'altro debba rispondere subito.

Ecco come ElGamal "usa" Diffie-Hellman per farlo:

#### 1. Alice pubblica la sua "metà" (Chiave Pubblica)

Alice genera la sua coppia di chiavi esattamente come in Diffie-Hellman.

- Sceglie un segreto $a$.
    
- Calcola $A = g^a$.
    
- Pubblica $A$. Questa è la sua **Chiave Pubblica**.
    

#### 2. Bob vuole mandare un messaggio (L'intervento di Diffie-Hellman)

Bob vuole inviare un messaggio $M$ ad Alice. Per farlo, **esegue un lato di uno scambio Diffie-Hellman "effimero" (usa e getta) da solo.**

1. Bob sceglie un numero casuale $k$ (come se fosse la sua chiave privata DH per questa sessione).
    
2. Calcola la sua parte pubblica DH: $C_1 = g^k$.
    
3. Ora Bob calcola il Segreto Condiviso ($S$) usando la chiave pubblica di Alice:
    
    $$S = (A)^k$$
    
    (Nota: Questo è esattamente $g^{ak}$, lo stesso segreto che avrebbero ottenuto con un Diffie-Hellman classico).
    

#### 3. L'uso del segreto (La Cifratura)

Qui sta la differenza. Invece di usare $S$ per chattare dopo, Bob lo usa subito come una "maschera" per il messaggio.

Moltiplica il suo messaggio $M$ per il segreto condiviso $S$:

$$C_2 = M \times S$$

#### 4. L'invio

Bob invia ad Alice un pacchetto contenente due cose $(C_1, C_2)$:

1. $C_1$: La sua "metà" Diffie-Hellman (serve ad Alice per ricalcolare il segreto).
    
2. $C_2$: Il messaggio mascherato.
    

#### 5. La Decifrazione (Alice chiude il cerchio)

Alice riceve il pacchetto.

1. Prende $C_1$ (la parte DH di Bob) e usa la sua chiave privata $a$ per ricostruire il segreto $S$:
    
    $$S = (C_1)^a$$
    
    (Matematicamente è sempre $g^{ka}$).
    
2. Ora che ha $S$, "divide" $C_2$ per $S$ e ritrova il messaggio originale $M$.
    

---

### In sintesi: La differenza di ruolo

- **Diffie-Hellman puro:** Serve a generare una chiave $S$ che useremo _dopo_ per cifrare con un altro algoritmo (es. AES).
    
- **ElGamal:** Usa la matematica di Diffie-Hellman per generare una chiave $S$ che viene usata **immediatamente e una volta sola** per "nascondere" matematicamente il messaggio all'interno della formula stessa.
    

### Perché usiamo RSA (o Curve Ellittiche) e non ElGamal oggi?

Se ElGamal è così intelligente e basato sul logaritmo discreto (molto sicuro), perché sentiamo parlare sempre di RSA?

Il difetto principale di ElGamal è l'espansione del testo cifrato.

Come hai visto sopra, per inviare un messaggio $M$, Bob deve inviare sia la maschera ($C_2$) sia la sua componente Diffie-Hellman ($C_1$).

Questo significa che il messaggio cifrato è grande il doppio del messaggio originale.

- **RSA:** Se cifri 2048 bit, ottieni 2048 bit di output.
    
- **ElGamal:** Se cifri 2048 bit, ottieni 4096 bit di output (2048 per il messaggio mascherato + 2048 per la chiave effimera).
    

Oggi, però, una variante di ElGamal è onnipresente: **ECIES (Elliptic Curve Integrated Encryption Scheme)**. Funziona esattamente come ElGamal, ma usando le Curve Ellittiche invece dei numeri interi enormi, rendendo le chiavi così piccole che il "raddoppio" delle dimensioni non è più un problema grave.