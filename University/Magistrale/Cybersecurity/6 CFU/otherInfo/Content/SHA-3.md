# 🥝 SHA-3 (Secure Hash Algorithm 3 - Keccak)

**[[SHA]]-3** è il nome della famiglia di funzioni di hash crittografiche che sono succedute a [[SHA-2]]. Non è stato sviluppato per sostituire SHA-2 perché quest'ultimo fosse rotto (come era successo con [[SHA-1]]), ma per offrire un'alternativa radicalmente diversa e resistente a qualsiasi potenziale attacco crittanalitico che potesse, in futuro, compromettere le funzioni basate sulla costruzione [[Merkle–Damgård]] (come SHA-1 e SHA-2).

SHA-3 è stato sviluppato dal team di progettisti di **Keccak** ed è stato standardizzato dal NIST (National Institute of Standards and Technology) nel 2015 dopo un concorso durato cinque anni (iniziato nel 2007).

---

## 🧠 Struttura e Funzionamento: La Costruzione a Spugna

La caratteristica più importante di SHA-3 è l'abbandono della Costruzione Merkle–Damgård in favore della **Costruzione a Spugna (Sponge Construction)**.

### Il Modello a Spugna

La "spugna" è un paradigma crittografico che assorbe (assorbe) i dati di input e li "strizza" (spreme) per produrre un output di lunghezza variabile.

- **Stato (State):** Lo stato interno della spugna è una grande matrice di bit (1600 bit in SHA-3), divisa in due parti:
    
    - **Capacità ($c$ - Capacity):** Una porzione di bit che rimane segreta durante il processo. Questa parte fornisce la sicurezza dell'algoritmo (è legata alla resistenza agli attacchi).
        
    - **Velocità ($r$ - Rate):** Una porzione di bit che viene scambiata con il messaggio.
        
- **Permutazione:** La funzione interna che mescola lo stato è una singola, grande **permutazione crittografica (Keccak-f)**, che viene applicata più volte.
    

### Fasi di Elaborazione

1. **Assorbimento (Absorbing):**
    
    - I blocchi del messaggio di input (della dimensione del _rate_ $r$) vengono combinati (tramite XOR) con la parte _rate_ dello stato interno.
        
    - Dopo ogni combinazione, l'intera matrice di stato (1600 bit) viene mescolata applicando la permutazione Keccak-f (un'operazione interna molto complessa e ripetuta 24 volte per ogni blocco).
        
2. **Spremitura (Squeezing):**
    
    - Una volta assorbito l'intero messaggio, la spugna inizia a produrre l'hash.
        
    - L'output viene estratto dalla parte _rate_ dello stato, e la permutazione Keccak-f viene riapplicata prima di estrarre il blocco successivo, fino a raggiungere la lunghezza di hash desiderata.
        

---

## 🎯 Vantaggi di SHA-3

SHA-3 non è solo un successore di SHA-2, ma rappresenta un cambiamento fondamentale nell'approccio all'hashing:

- **Immunità agli Attacchi di Estensione:** Poiché non utilizza la costruzione Merkle–Damgård, **SHA-3 è intrinsecamente immune** agli attacchi di estensione della lunghezza che affliggono SHA-1 e SHA-2.
    
- **Sicurezza Diversificata:** Offre una "rete di sicurezza" crittografica. Se un giorno venissero scoperti attacchi che rompono la struttura Merkle–Damgård di SHA-2, SHA-3, basato sulla spugna, rimarrebbe sicuro.
    
- **Output a Lunghezza Variabile:** Grazie al modello a spugna, SHA-3 può produrre output hash di **qualsiasi lunghezza desiderata** (fino alla dimensione della capacità).
    

---

## 🧩 Varianti e Applicazioni

SHA-3 è più flessibile di SHA-2 e offre le seguenti funzioni standardizzate:

|**Funzione**|**Lunghezza del Digest**|**Base Sicura (c)**|**Nota**|
|---|---|---|---|
|**SHA3-256**|256 bit|512 bit|Equivalente di sicurezza a SHA-256|
|**SHA3-512**|512 bit|1024 bit|Equivalente di sicurezza a SHA-512|
|**SHAKE128**|Output Variabile|256 bit|Funzione a lunghezza estensibile (XOF)|
|**SHAKE256**|Output Variabile|512 bit|Funzione a lunghezza estensibile (XOF)|

- **Applicazioni:** SHA-3 viene gradualmente adottato in ambiti come la crittografia post-quantistica e nuovi protocolli di sicurezza che richiedono flessibilità nella lunghezza dell'output. Nonostante questo, **SHA-256 (della famiglia SHA-2) rimane lo standard più diffuso** per la maggior parte delle applicazioni attuali per motivi di performance (SHA-2 è spesso più veloce su hardware esistente) e compatibilità.