# La Costruzione Merkle–Damgård

La costruzione Merkle–Damgård (MD) è una metodologia fondamentale utilizzata per costruire funzioni di hash crittografiche (come [[MD5]], [[SHA-1]] e [[SHA-2]]) a partire da una funzione di compressione più piccola e a lunghezza fissa.

In pratica, è un modo per prendere una "ricetta" che sa come mescolare due pezzi di dati (uno stato interno e un blocco di messaggio) e usarla per "mescolare" un messaggio di qualsiasi lunghezza.

---

### Come Funziona: Il Processo Iterativo
![[Pasted image 20251015135359.png]]
Il processo, come mostrato nel diagramma, è iterativo e segue questi passaggi:

1. **Padding (Riempimento):** Il messaggio originale viene prima "riempito" (padded). Questo è necessario per due motivi:
    
    - Assicurare che la lunghezza totale del messaggio sia un multiplo esatto della dimensione del blocco (es. 512 bit).
        
    - Includere la lunghezza del messaggio originale nel padding. Questo è un passaggio di sicurezza cruciale per prevenire certi attacchi.
        
        (Come hai notato, si può progettare un proprio schema di padding, ma deve essere coerente e non ambiguo).
        
2. **Inizializzazione:** Il processo inizia con un valore fisso e predefinito, chiamato **Vettore di Inizializzazione (IV)** o "seme" (seed). Questo è lo stato iniziale $H_0$.
    
3. **Elaborazione Iterativa:** Il messaggio (ora diviso in blocchi $M_1, M_2, \dots, M_n$) viene processato un blocco alla volta.
    
    - L'output dello stato precedente ($H_{i-1}$) e il blocco di messaggio corrente ($M_i$) vengono immessi nella **funzione di compressione ($f$)**.
        
    - La funzione di compressione "mescola" questi due input e produce un nuovo valore di stato: $H_i = f(H_{i-1}, M_i)$.
        
    - Questo nuovo stato $H_i$ diventa l'input per l'iterazione successiva, insieme al blocco di messaggio $M_{i+1}$.
        
4. **Hash Finale:** L'output dell'ultima iterazione, cioè l'ultimo stato $H_n$ prodotto dopo aver processato tutti i blocchi, è il **valore hash finale** dell'intero messaggio.
    

---

### La Funzione di Compressione ($f$)

La funzione di compressione è il cuore dell'algoritmo di hash. È una funzione a senso unico (OWF) che prende due input di dimensione fissa e produce un output (generalmente della stessa dimensione di uno degli input).

- **Requisiti:** Deve comportarsi come una funzione pseudocasuale, garantendo _confusione_ e _diffusione_ (proprietà prese dai cifrari a blocchi).
    
- **Costruzione Comune (Davies-Meyer):** Come indicato nei tuoi appunti, molte funzioni di hash (incluse SHA-1 e SHA-2) usano una struttura basata su un cifrario a blocchi, come la funzione di compressione di Davies-Meyer.
    
    - La formula che hai scritto è $H_i = E_{M_i}(H_{i-1}) \oplus H_{i-1}$.
        
    - **Spiegazione:** Per calcolare il nuovo stato $H_i$:
        
        1. Si usa il blocco di messaggio $M_i$ come **chiave** per un cifrario a blocchi $E$.
            
        2. Si cifra lo stato precedente $H_{i-1}$ usando $E$ con la chiave $M_i$.
            
        3. Si prende il risultato della cifratura e si fa uno XOR (⊕) con lo stato precedente $H_{i-1}$ per produrre il nuovo stato $H_i$.
            

---

### Punti di Forza e Debolezze

Come hai giustamente riassunto:

- **Punti di Forza:**
    
    - **Semplicità e Modularità:** È una struttura relativamente semplice da implementare e analizzare.
        
    - **Dimostrazione di Sicurezza:** Merkle e Damgård hanno dimostrato (indipendentemente) che se la funzione di compressione $f$ è resistente alle collisioni, allora l'intera funzione di hash costruita con questa metodologia è anch'essa **resistente alle collisioni**.
        
- **Punti Deboli:**
    
    - **Length Extension Attack (Attacco di Estensione della Lunghezza):** Questa è la vulnerabilità principale della costruzione MD pura. Se un attaccante conosce $H(M)$ (l'hash di un messaggio $M$ che non conosce) e la lunghezza di $M$, può facilmente calcolare $H(M \text{ || padding || } M')$ per una nuova estensione $M'$ da lui scelta. In pratica, l'attaccante può "continuare" l'hash senza conoscere il messaggio originale. (Questo è il motivo per cui SHA-3 utilizza una costruzione diversa, chiamata "sponge").
        

---

### Osservazioni Finali (Padding e OpenSSL)

Le tue osservazioni finali sono estremamente pertinenti e collegano l'hash alla crittografia.

#### 1. Requisiti di Sicurezza

Per evitare attacchi basati sul **paradosso del compleanno** (che permettono di trovare collisioni più velocemente di un attacco a forza bruta), la dimensione dell'output (il digest) deve essere sufficientemente grande. Una dimensione di 160 bit (come SHA-1) è oggi considerata al limite; si preferiscono 256 bit o più (come SHA-256).

#### 2. Il Ruolo del Padding nella Decifratura (Il caso OpenSSL)

La tua domanda su come OpenSSL possa sapere se la chiave è sbagliata ("Key Wrong") è eccellente. La risposta, come hai intuito, è il **padding**.

Questo non si applica all'hashing (che non usa chiavi), ma alla **cifratura simmetrica** (es. AES in modalità CBC).

- **Come funziona:** Quando si cifra un messaggio, l'ultimo blocco deve essere riempito (paddato) secondo uno schema specifico (es. PKCS#7). In questo schema, se mancano 5 byte per completare un blocco, si aggiungono 5 byte, tutti con il valore `0x05`. Se il messaggio è già un multiplo, si aggiunge un intero blocco di padding (es. 16 byte, tutti `0x10` per un blocco da 16 byte).
    
- **La Verifica:** Quando un software come OpenSSL decifra il messaggio, usa la chiave fornita.
    
    1. **Caso A (Chiave Corretta):** La decifrazione produce il plaintext originale. Il software guarda gli ultimi byte, riconosce uno schema di padding valido (es. `... 0x05 0x05 0x05 0x05 0x05`), lo rimuove e restituisce il messaggio.
        
    2. **Caso B (Chiave Sbagliata):** Se la chiave $k'$ è sbagliata, il processo di decifrazione produce un risultato che è essenzialmente **spazzatura casuale**.
        
    3. **Il Controllo:** Il software guarda gli ultimi byte di questa "spazzatura". La probabilità che dati casuali terminino _casualmente_ con uno schema di padding valido (es. `0x03 0x03 0x03` o `0x08 0x08 ... 0x08`) è estremamente bassa.
        
    4. **Conclusione:** Il software rileva un "padding malformato" e conclude che l'operazione è fallita. Questo fallimento implica quasi certamente che **la chiave usata era sbagliata** (o che il testo cifrato è stato corrotto).
        

Quindi, OpenSSL non ha bisogno di "capire" il plaintext; usa semplicemente l'integrità strutturale del padding come un "canarino nella miniera" per verificare se la decifrazione è avvenuta correttamente.