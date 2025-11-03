# 🛡️ SHA-2 (Secure Hash Algorithm 2)

**[[SHA]]-2** è una famiglia di funzioni di hash crittografiche progettata dalla U.S. National Security Agency (NSA) e pubblicata nel 2001 come successore di SHA-1. A differenza del suo predecessore (che è rotto), **SHA-2 è attualmente considerato sicuro** e viene ampiamente utilizzato come standard globale.

La famiglia SHA-2 include diverse varianti, che si distinguono principalmente per la lunghezza dell'output (il digest) che producono:

|**Algoritmo**|**Lunghezza del Digest**|**Dimensione del Blocco**|**Parole di Stato (bit)**|**Stato Attuale**|
|---|---|---|---|---|
|**SHA-256**|256 bit (32 byte)|512 bit|32|**Sicuro e Consigliato**|
|**SHA-512**|512 bit (64 byte)|1024 bit|64|**Sicuro e Consigliato**|
|SHA-224|224 bit|512 bit|32|Sicuro|
|SHA-384|384 bit|1024 bit|64|Sicuro|

### SHA-256: Lo Standard Più Diffuso

**SHA-256** è la variante più comune di SHA-2 ed è lo standard _de facto_ per la maggior parte delle applicazioni moderne, inclusi i certificati [[TLS]]/SSL, le firme digitali e, in particolare, la **Blockchain di Bitcoin**.

---

## ⚙️ Struttura e Funzionamento

Come [[SHA-1]], anche SHA-2 utilizza la **Costruzione Merkle–Damgård**, ma con un design e operazioni interne molto più complessi e robusti.

### 1. Design Migliorato

- **Algoritmi Distinti:** SHA-256 e SHA-512 sono algoritmi fondamentalmente diversi nel loro funzionamento interno, pur condividendo principi strutturali.
    
    - **SHA-256** usa parole (word) e operazioni a **32 bit** e processa blocchi da 512 bit.
        
    - **SHA-512** usa parole (word) e operazioni a **64 bit** e processa blocchi da 1024 bit (questo lo rende più veloce su piattaforme a 64 bit).
        
- **Aumento dei Round:** Entrambi utilizzano un numero maggiore di cicli (round) rispetto a SHA-1 (SHA-256 ne usa 64, SHA-512 ne usa 80), il che aumenta la confusione e la diffusione dei dati.
    
- **Costanti Aggiuntive:** Il processo interno utilizza un set più ampio di costanti fisse (derivate dai numeri primi), riducendo ulteriormente la possibilità di attacchi differenziali.
    

### 2. Funzione di Compressione

La funzione di compressione di SHA-2 non è la semplice Davies-Meyer, ma una sua evoluzione più complessa che combina l'input del blocco di messaggio con l'output dello stato precedente ($H_{i-1}$) attraverso una serie intricata di operazioni crittografiche:

- **Rotazioni e Shift:** Vengono utilizzate diverse operazioni di **rotazione circolare** (circolarmente) e di **shift logico** (spostamento) per garantire una rapida e completa diffusione di ogni bit attraverso lo stato interno.
    
- **Funzioni Logiche:** Vengono impiegate complesse combinazioni di operatori logici (come _Majority_ e _Conditional_) per mescolare i bit.
    
- **Aggiunte Modulari:** Le operazioni di somma sono eseguite modulo $2^{32}$ (per SHA-256) o modulo $2^{64}$ (per SHA-512).
    

---

## 🚀 Punti di Forza e Sicurezza

La forza di SHA-2 risiede nel suo output più lungo e nella sua robusta struttura:

- **Resistenza alle Collisioni Superiore:** Un output di **256 bit** sposta la complessità teorica per trovare una collisione a $2^{128}$ operazioni. Questo è un numero astronomicamente grande, che rende gli attacchi a forza bruta impraticabili anche con la tecnologia attuale e futura prevedibile.
    
- **Immunità a SHA-1:** Sebbene SHA-2 utilizzi la stessa struttura Merkle–Damgård di base, il suo design interno è sufficientemente diverso e robusto da non aver subito gli stessi attacchi che hanno rotto SHA-1.
    
- **Mitigazione degli Attacchi di Estensione:** La vulnerabilità di estensione della lunghezza (tipica di Merkle–Damgård) può essere mitigata con l'uso di **HMAC (Hash-based Message Authentication Code)** o algoritmi derivati come **HKDF**, che utilizzano SHA-2 in modo sicuro (incorporando la chiave sia all'inizio che alla fine).
    

### Stato Attuale

SHA-2 è il successore riconosciuto di SHA-1 e, nonostante l'esistenza del successore **SHA-3** (che utilizza una struttura completamente diversa, la "spugna" o "sponge"), **SHA-2 continua ad essere sicuro** e lo standard più diffuso. La migrazione a SHA-3 è in corso, ma SHA-2 è ancora il cavallo di battaglia della sicurezza informatica moderna.