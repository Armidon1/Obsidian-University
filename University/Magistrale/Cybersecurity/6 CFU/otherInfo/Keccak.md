# 🧼 Il Modello a Spugna: Concetti e Struttura

Il modello a spugna è un paradigma per costruire funzioni di hash crittografiche (come [[SHA-3]]) e generatori di numeri pseudocasuali a partire da una **singola funzione di permutazione** a lunghezza fissa. Il suo nome deriva dall'analogia con una spugna che **assorbe** un liquido (il messaggio) e poi può essere **strizzata** (spremuta) per rilasciare il liquido (l'hash).

### 1. Componenti Principali

La spugna opera su uno **stato interno ($S$)** di $b$ bit. Questo stato è diviso in due parti fondamentali:

- **Velocità ($r$ - Rate):** La parte dello stato che interagisce direttamente con l'input (messaggio) e l'output (hash).
    
- **Capacità ($c$ - Capacity):** La parte dello stato che rimane **nascosta** durante l'interazione con l'esterno. La sua dimensione è cruciale per la sicurezza e determina la resistenza del sistema agli attacchi.
    

$$b = r + c$$

- **Permutazione ($f$):** Una funzione crittografica a senso unico, adatta a un determinato numero di bit, che mescola l'intero stato $S$ in modo complesso. In SHA-3, questa funzione è chiamata **Keccak-f**.
    

---

## 💧 Fasi Operative: Assorbimento e Spremitura

Il funzionamento del modello a spugna si articola in due fasi principali, che operano sul messaggio $M$ suddiviso in blocchi $M_1, M_2, \dots$:

### Fase 1: Assorbimento (Input)

Questa fase consiste nell'elaborazione sequenziale del messaggio di input per aggiornare lo stato interno.

1. **Inizializzazione:** Lo stato interno $S$ viene inizializzato a zero.
    
2. **Iterazione:** Per ogni blocco di messaggio $M_i$ (di dimensione $r$):
    
    - **XOR:** Il blocco $M_i$ viene combinato (tramite **XOR**) con la parte di **Velocità ($r$)** dello stato $S$. La parte di Capacità ($c$) non viene modificata in questa operazione.
        
    - **Permutazione:** Viene applicata la **Permutazione $f$** (Keccak-f) all'intero stato $S$ (sia $r$ che $c$) per mescolare e diffondere le informazioni del blocco $M_i$ su tutto lo stato.
        
3. **Padding:** Prima dell'ultimo blocco di messaggio, viene applicato uno schema di padding (ad esempio, il padding $10\dots1$ usato da Keccak) per assicurare che la lunghezza sia un multiplo esatto della dimensione del _rate_ $r$.
    

### Fase 2: Spremitura (Output)

Una volta assorbito l'intero messaggio, la spugna inizia a produrre l'hash di output, che può avere una lunghezza arbitraria.

1. **Estrazione:** La parte di **Velocità ($r$)** dello stato $S$ viene estratta e aggiunta all'hash di output.
    
2. **Iterazione:** Se l'hash desiderato è più lungo del _rate_ $r$, lo stato $S$ viene nuovamente sottoposto alla **Permutazione $f$**.
    
3. **Output Continuo:** Viene estratta la successiva porzione di $r$ bit dall'ultima permutazione, e il processo si ripete fino a quando non viene raggiunta la lunghezza di hash richiesta.
    

---

## ✅ Sicurezza e Vantaggi

Il principale vantaggio del modello a spugna è la sua maggiore semplicità strutturale rispetto a Merkle–Damgård e la sua sicurezza intrinseca:

1. **Immunità agli Attacchi di Estensione della Lunghezza:** Poiché il messaggio originale non viene mai esposto insieme al suo hash e il processo di output è diverso da quello di input, **la spugna è immune** a questo attacco che affligge SHA-2.
    
2. **Sicurezza Garantita dalla Capacità:** La resistenza del sistema agli attacchi (come la ricerca di collisioni) è determinata dal parametro di **Capacità ($c$)**. Se l'output desiderato è di $L$ bit, si sceglie una capacità $c$ tale che $c \ge 2L$. Ad esempio, per SHA3-256 (hash a 256 bit), la capacità è di 512 bit, garantendo una resistenza alle collisioni di $2^{256}$ operazioni.
    
3. **Output a Lunghezza Estensibile (XOF):** Le funzioni di hash basate su spugna possono essere implementate come **Extended Output Functions (XOF)** (come SHAKE128 e SHAKE256 in SHA-3), permettendo di produrre un output hash di qualsiasi lunghezza desiderata, il che le rende estremamente versatili per diverse applicazioni crittografiche.
    

Il modello a spugna offre quindi una solida alternativa crittografica a Merkle–Damgård, garantendo che la sicurezza non dipenda da un singolo punto di vulnerabilità strutturale.