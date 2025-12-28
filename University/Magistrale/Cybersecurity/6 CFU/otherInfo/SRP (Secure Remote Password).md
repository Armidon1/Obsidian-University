# Protocollo SRP (Secure Remote Password)

Tags: #cryptography #authentication #protocols #SRP #augmented_EKE

Related: [[Protocollo EKE]], [[Diffie-Hellman]], [[Zero-Knowledge Proof]]

## 1. Che cos'è?

Il Secure Remote Password (SRP) è un protocollo avanzato di autenticazione "Augmented".

Rappresenta l'evoluzione sicura di EKE: permette di autenticarsi usando una password senza mai trasmetterla, e garantisce che nemmeno il server conosca la password (o un dato equivalente che permetta di impersonare l'utente immediatamente).

> [!TIP] Concetto Chiave
> 
> SRP è un protocollo Zero-Knowledge: Alice prova a Bob di conoscere la password senza rivelare la password stessa. Inoltre, è resistente agli attacchi a dizionario e garantisce la Perfect Forward Secrecy.

## 2. Setup e Parametri

Prima di iniziare, server e client concordano su parametri pubblici e dati specifici dell'utente.

### Variabili Globali

- **$p$:** Un numero primo grande sicuro.
    
- **$g$:** Un generatore per il gruppo modulo $p$.
    
- **$k$:** Un moltiplicatore derivato dai parametri, $k = H(p \parallel g)$.
    

### Dati dell'Utente (lato Server)

Il server (Bob) **NON** salva la password. Memorizza:

1. **Salt ($u$):** Un valore casuale univoco per utente.
    
2. Verifier ($v$): Un valore derivato dalla password che serve per la verifica ma è inutile per impersonare l'utente.
    
    $$W = H(u \parallel \text{"Alice"} \parallel \text{password})$$
    
    $$v = g^W \pmod p$$
    

---

## 3. Il Flusso del Protocollo

### Fase 1: Inizio (Alice $\rightarrow$ Bob)

Alice genera un numero casuale $a$ (effimero) e invia la sua "chiave pubblica" effimera $A$:

$$A = g^a \pmod p$$

### Fase 2: Sfida (Bob $\rightarrow$ Alice)

Bob genera un numero casuale $b$ (effimero). Calcola il valore $B$ usando il verifier $v$ e il moltiplicatore $k$ per "mascherare" la sua parte DH.

Invia ad Alice:

$$B = (k \cdot v + g^b) \pmod p$$

Invia anche il salt $u$ (se Alice non lo ha già).

### Fase 3: Calcolo della Chiave di Sessione ($K$)

A questo punto, viene introdotto un parametro di "scrambling" $r$ (o $u$ in alcune notazioni, ma qui usiamo $r$ per chiarezza come hash dei messaggi pubblici) per legare la sessione:

$$r = H(A \parallel B)$$

Ora avviene la magia matematica per calcolare il segreto condiviso $S$.

- Calcolo di Alice (Cliente):
    
    Alice deve rimuovere il componente $k \cdot v$ aggiunto da Bob. Conosce la password, quindi calcola $W$ e poi:
    
    $$S = (B - k \cdot g^W)^{a + rW} \pmod p$$
    
- Calcolo di Bob (Server):
    
    Bob usa la chiave pubblica di Alice $A$ e il verifier $v$:
    
    $$S = (A \cdot v^r)^b \pmod p$$
    

La chiave di sessione finale è $K = H(S)$.

### Fase 4: Verifica

Per confermare che tutto ha funzionato (e che Alice conosceva davvero la password):

1. Alice invia un hash di verifica $M_1 = H(A, B, K)$.
    
2. Bob controlla $M_1$ e risponde con $M_2 = H(A, M_1, K)$.
    

---

## 4. Analisi Matematica (Perché funziona?)

Perché Alice e Bob ottengono lo stesso numero $S$?

Sviluppiamo il calcolo di Bob:

$$S_{Bob} = (A \cdot v^r)^b = (g^a \cdot g^{Wr})^b = (g^{a + Wr})^b = g^{b(a + Wr)}$$

Sviluppiamo il calcolo di Alice (ricordando che $B = kv + g^b$):

$$S_{Alice} = (B - kv)^{a + rW} = (kv + g^b - kv)^{a + rW} = (g^b)^{a + rW} = g^{b(a + rW)}$$

I due valori sono identici!

---

## 5. Vantaggi Principali

1. **Augmentation:** Se un attaccante ruba il database del server (con i verifier $v$), non può impersonare Alice. Deve prima eseguire un attacco brute-force offline costoso per trovare $P$ partendo da $v$.
    
2. **No Trasmissione Password:** La password non viaggia mai sulla rete, nemmeno cifrata.
    
3. **Perfect Forward Secrecy:** Se la password viene scoperta in futuro, le sessioni passate non possono essere decifrate (perché dipendono da $a$ e $b$ che sono effimeri).