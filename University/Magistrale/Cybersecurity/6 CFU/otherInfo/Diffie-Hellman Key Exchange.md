# 🤝 Diffie-Hellman Key Exchange

### Definizione

Il **Diffie-Hellman (DH)** è un **protocollo di accordo sulla chiave** (_key agreement protocol_). È un metodo crittografico che permette a due parti (es. Alice e Bob), che non hanno mai comunicato prima, di stabilire in modo sicuro un **segreto condiviso** (una chiave simmetrica) su un canale di comunicazione pubblico e insicuro.

**Punto Chiave:** DH _non_ è un algoritmo di cifratura. Non cifra né decifra i dati. Il suo unico scopo è generare una chiave segreta condivisa, che sarà poi utilizzata da un altro algoritmo (come AES) per la cifratura simmetrica.

La sua sicurezza si basa sulla difficoltà computazionale del **Problema del Logaritmo Discreto (DLP)**.

### Il Processo Matematico (per Ingegneri)

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

Entrambi arrivano allo stesso identico numero segreto $S$.

- Calcolo di Alice: $S = (g^b)^a \pmod p = g^{ba} \pmod p$
    
- Calcolo di Bob: $S' = (g^a)^b \pmod p = g^{ab} \pmod p$
    

Quindi, $S = S'$. Questo numero $S$ è ora la loro chiave simmetrica condivisa.

### Dettagli Tecnici e Implicazioni di Sicurezza

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Problema Difficile (DLP)**|Un osservatore (Eve) sul canale pubblico vede $g, p, A, B$. Per trovare il segreto $S$, Eve deve calcolare $a$ (da $A=g^a$) o $b$ (da $B=g^b$). Questo è il **Problema del Logaritmo Discreto**, che è computazionalmente infattibile.|
|**Vulnerabilità Critica (MitM)**|Il protocollo DH classico è **vulnerabile a un attacco Man-in-the-Middle (MitM)**. Poiché $A$ e $B$ non sono autenticati, un attaccante (Mallory) può intercettare la comunicazione, stabilire un segreto $S_1$ con Alice (fingendosi Bob) e un segreto $S_2$ con Bob (fingendosi Alice), e poi decifrare e re-cifrare tutto il traffico.|
|**Soluzione (Autenticazione)**|DH **non deve mai essere usato da solo**. Deve essere **autenticato**. In pratica (come in TLS o SSH), il server "firma" i suoi parametri DH (es. $B$) usando la sua chiave privata (es. RSA o ECDSA) per dimostrare la sua identità.|
|**Forward Secrecy (PFS)**|DH (specialmente **Ephemeral Diffie-Hellman - DHE/EDCHE**) è la base della **Perfect Forward Secrecy (PFS)**. Poiché i segreti privati $a$ e $b$ sono generati _al momento_ per ogni sessione e poi _distrutti_, anche se la chiave privata a lungo termine del server viene rubata in futuro, gli aggressori non possono decifrare le sessioni passate.|
|**Varianti (ECC)**|La versione moderna, **ECDH (Elliptic Curve Diffie-Hellman)**, usa la matematica delle curve ellittiche invece dell'esponenziazione modulare. Raggiunge lo stesso livello di sicurezza di DH con chiavi molto più piccole (es. 256 bit vs 3072 bit), rendendolo molto più veloce ed efficiente.|