# Mask Generation Function (MGF)

**Tags:** #crittografia #RSA #primitive #PKCS1 #hash #OAEP #PSS #sicurezza

## 1. Definizione e Concetto Intuitivo

Una **Mask Generation Function (MGF)** è una primitiva crittografica fondamentale che funge da "ponte" tra le funzioni hash a lunghezza fissa e la necessità di chiavi o maschere a lunghezza variabile.

In termini semplici, è un algoritmo usato per **"allungare" (stretch)** un input relativamente corto (chiamato _seed_) trasformandolo in un output pseudocasuale di **lunghezza arbitraria e desiderata**.

### Definizione Formale

Matematicamente, è una funzione deterministica definita come:

$$\text{MGF}(seed, length) \rightarrow mask$$

Dove:

- **seed:** Una stringa di input di lunghezza qualsiasi.
    
- **length:** La lunghezza in byte desiderata per l'output.
    
- **mask:** La stringa di output generata.
    

---

## 2. Il Problema: Perché ci serve?

Le funzioni hash crittografiche standard (come [[SHA-256]]) hanno un limite strutturale per certi usi:

- **Input:** Qualsiasi dimensione.
    
- **Output:** Dimensione **fissa** (es. sempre e solo 256 bit / 32 byte).
    

Lo Scenario RSA (OAEP/PSS):

Quando cifriamo o firmiamo con RSA, lavoriamo con blocchi molto grandi (es. 2048 o 4096 bit).

Per proteggere questi dati, dobbiamo applicare una maschera tramite operazione [[XOR]].

- Non possiamo usare un hash da 256 bit per mascherare un messaggio da 2000 bit.
    
- Abbiamo bisogno di un modo sicuro per espandere quei 256 bit fino a coprire tutti i 2000 bit necessari.
    

> [!abstract] Visual Metaphor
> 
> Pensa all'MGF come a un "rullo compressore al contrario": prende una pallina di materiale (il seed) e la stira fino a farla diventare un foglio sottile lungo esattamente quanto serve per coprire l'oggetto (il messaggio).

---

## 3. Lo Standard: MGF1

L'algoritmo standard più diffuso, definito in [[PKCS#1]], è MGF1.

Non è una funzione nuova, ma un "meta-algoritmo" costruito sopra una funzione hash esistente (es. SHA-256, SHA-1) usata come motore interno.

### Algoritmo Passo-Passo

Per generare una maschera di lunghezza $L$ a partire da un seed $Z$:

1. **Inizializzazione:** Si imposta un contatore $C = 0$ (un intero a 32 bit).
    
2. **Ciclo di Hashing:** Si concatena il seed con il contatore e si calcola l'hash.
    
3. **Accumulo:** Si uniscono i risultati dei vari hash in una lunga catena.
    
4. **Incremento:** Si aumenta il contatore e si ripete.
    

**La formula dell'iterazione è:**

$$T = T \ || \ \text{Hash}(Z \ || \ \text{I2OSP}(C, 4))$$

_(Dove $||$ è la concatenazione e [[I2OSP]] converte il contatore in 4 byte)_

**Esempio di sequenza generata:**

- `Blocco_0 = Hash(seed || 0x00000000)`
    
- `Blocco_1 = Hash(seed || 0x00000001)`
    
- `Blocco_2 = Hash(seed || 0x00000002)`
    
- ... fino a riempire la lunghezza richiesta.
    

5. **Troncamento (Taglio):** Se la stringa generata è più lunga di $L$, viene tagliata esattamente alla lunghezza desiderata.
    

---

## 4. Utilizzo negli Schemi RSA

L'MGF è il "motore nascosto" che rende sicuri gli schemi moderni.

### In [[RSAES-OAEP]] (Cifratura)

Viene usata per istanziare le due funzioni $G$ e $H$ nella **Rete di Feistel**:

1. Funzione G: Espande il seed casuale $r$ per creare una maschera lunga quanto il messaggio ($DB$).
    
    $$maskedDB = DB \oplus G(r)$$
    
2. Funzione H: Espande il messaggio mascherato per creare una maschera lunga quanto il seed.
    
    $$maskedSeed = r \oplus H(maskedDB)$$
    

### In [[RSA-PSS|RSASSA-PSS]] (Firma)

Viene usata per mascherare il blocco dati ("Data Block") che contiene il Salt e il padding.

$$maskedDB = DB \oplus \text{MGF}(H', \text{len}(DB))$$

---

## 5. Proprietà di Sicurezza Chiave

Perché il sistema funzioni e sia sicuro, l'MGF deve garantire due proprietà apparentemente opposte:

1. **Deterministica:**
    
    - Se fornisci lo stesso _seed_, otterrai **sempre** la stessa identica _maschera_.
        
    - _Perché serve?_ Se fosse casuale, il destinatario non potrebbe mai invertire il processo (decifrare o verificare la firma).
        
2. **Pseudocasuale (Effetto Valanga):**
    
    - L'output deve sembrare "rumore bianco" imprevedibile.
        
    - Basta cambiare **un solo bit** nel seed iniziale per cambiare completamente (circa il 50% dei bit) l'intera maschera di output.
        
    - Questo impedisce agli attaccanti di trovare correlazioni matematiche tra la maschera e il seed.
        

---

**Vedi anche:**

- [[Differenza tra MGF e MGF1]]
    
- [[RSA-OAEP]]
    
- [[Hashing]]
    
- [[PKCS#1]]

# 🎭 Che cos'è la Mask Generation Function (MGF)?

In poche parole, una **Mask Generation Function (MGF)** è un algoritmo crittografico usato per "allungare" (o "stretchare") un input (chiamato _seed_) relativamente corto e a lunghezza fissa, trasformandolo in un output (chiamato _maschera_) pseudocasuale di **lunghezza arbitraria e desiderata**.

È un "ingrediente" fondamentale, non un algoritmo di cifratura completo.

### Il Problema che Risolve

Pensa a una funzione di hash come SHA-256. Come input può prendere dati di qualsiasi dimensione, ma il suo output è _sempre_ e _solo_ di 256 bit (32 byte).

Ora, guarda lo schema di OAEP nei tuoi appunti:

- Dobbiamo mascherare (con un'operazione XOR) il blocco del messaggio.
    
- Questo blocco potrebbe essere lungo, ad esempio, 1800 bit.
    
- Non possiamo usare direttamente un hash da 256 bit per mascherare 1800 bit.
    

Abbiamo bisogno di un modo per prendere un _seed_ (come un hash o un numero casuale) e "stirarlo" in modo sicuro per produrre una maschera pseudocasuale lunga esattamente 1800 bit. **Questo è il compito dell'MGF.**

### Come Funziona (Esempio: MGF1)

Lo standard più comune è **MGF1** (definito in PKCS#1). Funziona in modo molto intelligente usando una funzione di hash (es. SHA-256) come "motore" interno.

Ecco il processo:

1. **Input:** Prende il _seed_ iniziale (ad esempio, il `seed` casuale `r` in OAEP).
    
2. **Contatore:** Inizia con un contatore a 0.
    
3. **Hashing:** Appende il contatore al seed e calcola l'hash:
    
    - `blocco_0 = Hash(seed || 0x00000000)`
        
4. **Iterazione:** Incrementa il contatore e ripete il processo:
    
    - `blocco_1 = Hash(seed || 0x00000001)`
        
    - `blocco_2 = Hash(seed || 0x00000002)`
        
    - ...e così via.
        
5. **Concatenazione:** Unisce tutti i blocchi di hash che ha generato:
    
    - `output_lungo = blocco_0 || blocco_1 || blocco_2 || ...`
        
6. **Taglio:** Continua questo processo finché `output_lungo` non è lungo almeno quanto la maschera desiderata. A quel punto, "taglia" (tronca) l'output alla lunghezza esatta di cui ha bisogno.
    

### Il suo Ruolo in OAEP e PSS

L'MGF è ciò che rende OAEP e PSS così robusti e sicuri:

- **In RSA-OAEP:** Come hai visto nello schema di Feistel, l'MGF viene usato due volte (come le funzioni `G` e `H`):
    
    1. `G(r)`: **Allunga** il _seed_ casuale `r` per creare una maschera abbastanza lunga da applicare (via XOR) al messaggio.
        
    2. H(X): Allunga il blocco X per creare una maschera abbastanza lunga da applicare (via XOR) al seed r.
        
        Questo incrocio (chiamato Feistel network) è ciò che crea la proprietà "all-or-nothing" che sconfigge gli attacchi CCA.
        
- **In RSA-PSS:** Come dicono i tuoi appunti, viene usato per "allungare" l'hash `H'` (che combina l'hash del messaggio e il _sale_ casuale) per creare una maschera. Questa maschera viene poi usata per "offuscare" il _Data Block_ (`DB`).
    

### Proprietà Chiave

In sintesi, un MGF ha due proprietà fondamentali:

1. **Deterministico:** Se gli dai lo stesso _seed_, produrrà _sempre_ la stessa identica maschera. Questo è essenziale, altrimenti chi decifra non potrebbe invertire il processo.
    
2. **Pseudocasuale:** L'output (la maschera) "sembra" perfettamente casuale. Grazie all'effetto valanga dell'hash interno, cambiare anche un solo bit nel _seed_ cambia completamente l'intera maschera.
    

Spero che questo renda più chiaro il concetto! È un "trucco" crittografico brillante per generare materiale pseudocasuale flessibile partendo da un hash rigido.

vedi anche [[Differenza tra MGF e MGF1]]