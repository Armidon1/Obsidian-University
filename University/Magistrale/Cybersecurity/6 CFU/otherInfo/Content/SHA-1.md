# 🔒 SHA-1 (Secure Hash Algorithm 1)

**[[SHA]]-1** è una **funzione di hash crittografica** progettata dalla National Security Agency (NSA) statunitense e pubblicata come standard (FIPS PUB 180-1) nel 1995. Per anni è stato uno standard fondamentale per la sicurezza digitale, ma **oggi è considerato crittograficamente rotto e deprecato** a causa delle sue vulnerabilità.

---

## ⚙️ Struttura e Funzionamento

SHA-1 è costruito utilizzando la **Costruzione Merkle–Damgård** e genera un output hash di **160 bit** (20 byte), tipicamente rappresentato da 40 caratteri esadecimali.

### 1. Elaborazione del Messaggio e Padding

- **Blocchi:** Il messaggio di input viene prima "riempito" (padded) per assicurarsi che la sua lunghezza totale sia un multiplo esatto di **512 bit**.
    
- **Inclusione della Lunghezza:** Il padding include sempre la lunghezza originale del messaggio, un passaggio cruciale per prevenire attacchi.
    
- **Stato Iniziale (IV):** Il processo inizia con un **Vettore di Inizializzazione (IV)** fisso e predefinito, composto da cinque parole a 32 bit ($H_0$ a $H_4$).
    

### 2. Funzione di Compressione

Il cuore di SHA-1 è la sua **funzione di compressione**, che elabora i blocchi del messaggio in modo iterativo.

- **Processo Iterativo:** Lo stato (output) del blocco precedente viene combinato con il blocco di messaggio corrente.
    
- **Logica Interna:** La funzione esegue una serie di **80 round** che coinvolgono complesse operazioni logiche a livello di bit (come rotazioni, operazioni booleane come XOR, AND, OR) e aggiunte modulari, garantendo un'elevata diffusione e confusione dei dati.
    
- **Output:** L'output dell'ultima funzione di compressione è il **valore hash finale (digest)** di 160 bit.
    

---

## 🚨 Vulnerabilità e Stato Attuale

La sicurezza di SHA-1 si basa sulla sua **resistenza alle collisioni** (impossibilità di trovare due input diversi che producano lo stesso hash) e sulla sua **resistenza alla preimmagine** (impossibilità di risalire al messaggio originale dall'hash).

### 1. Fallimento della Resistenza alle Collisioni (Il Pericolo Maggiore)

A causa dei progressi nella crittoanalisi e nella potenza di calcolo, la resistenza alle collisioni di SHA-1 è stata compromessa:

- **Complessità Teorica Ridotta:** La complessità teorica per trovare una collisione è stata drasticamente ridotta, ben al di sotto dei $2^{80}$ passaggi attesi per un hash a 160 bit.
    
- **Attacco SHAttered (2017):** I ricercatori di Google e CWI hanno dimostrato il **primo attacco pratico di collisione** contro SHA-1. Hanno creato due file PDF distinti che producevano lo stesso hash SHA-1. Questa dimostrazione pratica ha confermato che l'algoritmo è **crittograficamente rotto** per tutti gli scopi che richiedono resistenza alle collisioni, come le firme digitali.
    

### 2. Vulnerabilità di Estensione della Lunghezza

Essendo costruito con Merkle–Damgård, SHA-1 è vulnerabile agli **attacchi di estensione della lunghezza**.

- Un attaccante che conosce il digest $H(M)$ e la lunghezza del messaggio originale (M) può calcolare l'hash di un messaggio esteso $H(M \text{ || padding } || M')$ **senza conoscere il contenuto del messaggio originale $M$**.
    

---

## 🚫 Raccomandazione e Migrazione

A causa della scoperta di attacchi di collisione pratici, SHA-1 è stato **ufficialmente deprecato** da organizzazioni come il NIST e i principali produttori di software (browser, sistemi operativi).

- **Stato:** **Obsoleto** e non sicuro per nuove applicazioni.
    
- **Raccomandazione:** È fondamentale migrare immediatamente tutte le applicazioni che richiedono resistenza alle collisioni e integrità a lungo termine verso:
    
    - **SHA-2** (in particolare **SHA-256**)
        
    - **SHA-3** (Keccak)
        

Questi algoritmi successivi offrono output più lunghi (es. 256 o 512 bit) e strutture interne più robuste, non ereditando le debolezze di SHA-1.