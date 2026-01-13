guardare sempre prima [[CS 6cfu - Domande esame]]

Basandomi sulle slide che hai fornito e sull'analisi incrociata con gli esami passati (in particolare quelli dal 2022 al 2025 che sono i più rilevanti per il trend attuale), ecco cosa viene chiesto all'esame riguardo a **Data Integrity, MAC e Hashing**.

Le domande si concentrano spesso sui **limiti** dei protocolli (cosa _non_ fare) e sulle definizioni teoriche precise.

### 1. Integrità vs Autenticità (Concetti Base)

È una domanda classica introduttiva. Devi saper distinguere le due proprietà.

- **Domanda tipica:** "Illustra la differenza tra data integrity e authenticity." oppure "L'autenticità implica l'integrità?".
    
- **Risposta attesa:**
    
    - **Integrità:** Garantisce che il dato non sia stato modificato (accidentally or maliciously).
        
    - **Autenticità:** Garantisce l'integrità **PIÙ** l'origine del messaggio (chi l'ha mandato è chi dice di essere). Le slide dicono esplicitamente: _"Data integrity guarantees that the source of the information is authentic"_ e _"Authenticity is orthogonal to Secrecy"_.
        
    - **Nota:** I semplici Hash garantiscono integrità (se confrontati con un digest sicuro), i MAC garantiscono integrità e autenticità.
        

### 2. Il tallone d'Achille del CBC-MAC (Fondamentale)

Questa è forse la domanda tecnica più frequente sui MAC. Le tue slide evidenziano in grassetto che **"CBC-MAC is insecure for variable-length messages"**.

- **Domanda tipica:** "Mostra che l'uso della tecnica CBC per fornire un MAC fallisce per messaggi a lunghezza variabile".
    
- **Cosa devi saper dimostrare:**
    
    - Il CBC-MAC è sicuro solo se la lunghezza del messaggio è fissa e concordata.
        
    - **L'attacco (Extension Attack):** Se un attaccante conosce $(m, t)$ e $(m', t')$, può costruire un nuovo messaggio $m'' = m || (m'_1 \oplus t) || m'_2 \dots$ che produrrà lo stesso tag $t'$. Questo permette di forgiare un messaggio valido senza conoscere la chiave.
        

### 3. Funzioni Hash: Collision Resistance (Strong vs Weak)

Questo è l'argomento teorico numero uno per gli hash.

- **Domanda tipica:** "Definisci Strong e Weak collision resistance. Perché la Strong implica la Weak?".
    
- **Risposta attesa:**
    
    - **Weak (Second Preimage Resistance):** Dato un input $x$, è difficile trovare un $y \neq x$ tale che $H(x) = H(y)$.
        
    - **Strong (Collision Resistance):** È difficile trovare una _qualsiasi_ coppia $(x, y)$ tale che $H(x) = H(y)$.
        
    - **Implcazione:** Se non riesco a trovare _nessuna_ coppia che collide (Strong), a maggior ragione non riesco a trovarne una dove uno dei due elementi è fissato (Weak). Quindi Strong $\Rightarrow$ Weak.
        

### 4. Keyed Hashing vs Unkeyed Hashing

Spesso il prof chiede di analizzare la sicurezza di costruzioni specifiche per trasformare un Hash in un MAC.

- **Domanda tipica:** "Discuti la sicurezza dell'hashing $k|m$, $m|k$, $k|m|k$".
    
- **Analisi:**
    
    - $H(k||m)$: Insicuro a causa del _Length Extension Attack_ (tipico della costruzione Merkle-Damgård usata in SHA-1/SHA-2). Un attaccante può aggiungere dati alla fine senza conoscere $k$.
        
    - $H(m||k)$: Vulnerabile se l'hash ha collisioni interne (meno grave ma problematico).
        
    - **Soluzione:** HMAC (che usa due passaggi di hashing innestati).
        

### 5. Birthday Paradox e Lunghezza del Digest

Le domande vertono sul "perché" servono digest lunghi.

- **Domanda tipica:** "Perché vogliamo fingerprint più lunghi di 160 bit?" o "Cos'è il Birthday Attack?".
    
- **Concetto chiave:** La probabilità di collisione diventa $>50\%$ dopo circa $2^{m/2}$ tentativi (dove $m$ sono i bit del digest).
    
    - Per SHA-1 ($m=160$), la sicurezza è $2^{80}$, oggi considerata attaccabile.
        
    - Bisogna ricordare la formula $1.177 \cdot 2^{m/2}$ presente nelle tue slide.
        

### 6. Domande "Tricky" e Ragionamento

Negli ultimi esami ci sono domande che richiedono di ragionare sulle proprietà matematiche:

- **Hash di Hash:** "Se H è un hash crittografico, come si confronta il numero di collisioni di $H(H(x))$ rispetto a $H(x)$?".
    
    - _Risposta:_ Il numero di collisioni è uguale o maggiore, mai minore. Applicare la funzione due volte restringe (o mantiene uguale) l'immagine, aumentando la probabilità di collisioni (Pigeonhole principle).
        
- **Funzioni non crittografiche:** "La funzione $H(x) = x \pmod s$ o la rappresentazione binaria sono hash crittografici?".
    
    - _Risposta:_ No. Manca la proprietà di _One-Way_ (invertibilità facile) o la _Collision Resistance_ (struttura prevedibile).
        

### Schema di Studio (Priorità)

1. **Dimostrazione insicurezza CBC-MAC** su lunghezza variabile.
    
2. **Definizioni Strong/Weak collision resistance** e perché Strong $\to$ Weak.
    
3. **Birthday Paradox:** formula $2^{m/2}$ e perché rende obsoleti i digest a 64/128 bit.
    
4. **Differenza pratica** tra Keyed Hashing (autenticità) e Unkeyed (solo integrità, soggetto a man-in-the-middle).