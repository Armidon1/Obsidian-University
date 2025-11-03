Il **MD5 (Message-Digest Algorithm 5)** è una funzione di hash crittografica, creata da Ronald Rivest nel 1991, che ha avuto un ruolo fondamentale nella storia della sicurezza informatica. Sebbene un tempo fosse lo standard più diffuso, **oggi è considerato crittograficamente rotto e obsoleto** per la maggior parte delle applicazioni di sicurezza.

Ecco un'analisi dettagliata del suo funzionamento, utilizzo e, soprattutto, delle sue vulnerabilità.

---

## ⚙️ Funzionamento e Caratteristiche

MD5 è progettato per generare una "impronta digitale" unica e a lunghezza fissa per qualsiasi blocco di dati.

### Output e Lunghezza Fissa

- **Digest:** MD5 produce un output (chiamato _hash_ o _digest_) di **128 bit**, tipicamente rappresentato come una stringa esadecimale di **32 caratteri**.
    
- **Irreversibilità:** MD5 è una **funzione unidirezionale** (one-way function). È computazionalmente impraticabile risalire al messaggio originale a partire dal suo hash (resistenza alla preimmagine).
    
- **Sensibilità (Effetto valanga):** Anche la minima modifica nell'input (un singolo bit) genera un hash MD5 completamente diverso e imprevedibile.
    

### Struttura Algoritmica

MD5, come SHA-1 e SHA-2, utilizza la **Costruzione Merkle–Damgård** per elaborare messaggi di lunghezza arbitraria:

1. **Padding (Riempimento):** Il messaggio viene esteso (padded) aggiungendo un bit '1' seguito da tanti bit '0' quanti necessari, in modo che la sua lunghezza totale in bit sia congrua a **448 modulo 512**.
    
2. **Aggiunta della Lunghezza:** Alla fine del messaggio padded vengono aggiunti **64 bit** che rappresentano la lunghezza originale del messaggio. A questo punto, il messaggio ha una lunghezza che è un multiplo esatto di 512 bit.
    
3. **Inizializzazione:** Vengono inizializzati **quattro registri a 32 bit** ($A, B, C, D$) con valori esadecimali predefiniti (il Vettore di Inizializzazione - IV).
    
4. **Elaborazione (Compression Function):** Il messaggio, diviso in blocchi da 512 bit, viene elaborato iterativamente. Per ogni blocco, vengono eseguiti **64 cicli (round)** che mescolano i dati tramite operazioni bitwise (AND, OR, XOR), rotazioni e addizioni modulari.
    

Il valore finale dei quattro registri ($A, B, C, D$) concatenato forma il digest finale di 128 bit.

---

## 🚨 Vulnerabilità Critica: La Collisione

Nonostante i suoi principi, MD5 è **carente** nel requisito fondamentale per le funzioni di hash crittografiche moderne: la **resistenza alle collisioni**.

- **Definizione di Collisione:** Una collisione avviene quando due input diversi producono esattamente lo stesso valore hash.
    
- **Il Problema di MD5:** Con i suoi soli 128 bit di output, MD5 è vulnerabile all'**Attacco del Compleanno (Birthday Attack)**, che abbassa la complessità di trovare una collisione da $2^{128}$ (attacco a forza bruta) a circa $2^{64}$.
    
- **Rottura Pratica (2004 in poi):** Nel 2004, sono stati dimostrati i primi attacchi teorici efficaci. Da allora, la capacità di trovare collisioni è diventata pratica. Esistono strumenti che possono generare due file (ad esempio, due documenti o due eseguibili) con lo stesso hash MD5 **in pochi minuti** o persino secondi su hardware standard.
    
- **Conseguenze:** La scoperta di collisioni pratiche significa che un attaccante può creare:
    
    - Un file malevolo che ha lo stesso hash di un file legittimo (sostituzione di software).
        
    - Un certificato digitale falso che ha lo stesso hash di un certificato valido, consentendo l'impersonificazione (come dimostrato da attacchi come Flame malware).
        

---

## 🛑 Applicazioni Attuali (e Perché non Usarlo per la Sicurezza)

A causa della sua vulnerabilità alle collisioni, MD5 **non deve più essere utilizzato** per scopi in cui la sicurezza e la resistenza alle manomissioni sono fondamentali:

|**Uso Storico di MD5**|**Stato Attuale**|**Raccomandazione**|
|---|---|---|
|**Verifica di Integrità** (file scaricati, checksum)|**Accettabile, ma sconsigliato.**|Per applicazioni non critiche (dove la collisione accidentale è remota). Per la sicurezza, usare **SHA-256**.|
|**Firme Digitali**|**Assolutamente Deprecato.**|Le collisioni permettono la falsificazione. Usare **SHA-256** o superiore.|
|**Archiviazione di Password**|**Assolutamente Deprecato.**|Usare funzioni di derivazione di chiavi (Key Derivation Functions - KDF) come **Argon2** o **PBKDF2** con _salt_ e _costo di calcolo_ elevato.|

**In sintesi, MD5 è utile oggi solo come semplice checksum per l'identificazione di file o per applicazioni non crittografiche, ma è considerato insicuro per la crittografia, la verifica di integrità a prova di manomissione o le firme digitali.**

Il suo posto nella sicurezza moderna è stato preso da algoritmi più robusti della famiglia **SHA-2** (come SHA-256) e **SHA-3**.