La differenza fondamentale tra uno **Stream Cipher** (cifrario a flusso) e un **Block Cipher** (cifrario a blocchi) risiede nell'unità di dati su cui operano e, di conseguenza, nel loro meccanismo di trasformazione.1

---

### 🔑 Differenze Chiave: Stream Cipher vs. Block Cipher

|**Caratteristica**|**Stream Cipher (Cifrario a Flusso)**|**Block Cipher (Cifrario a Blocchi)**|
|---|---|---|
|**Unità di Elaborazione**|**Bit o Byte** alla volta.|**Blocchi di dimensione fissa** (es. 64, 128 bit) alla volta.|
|**Meccanismo di Base**|Genera una **Keystream** pseudocasuale e la combina con il testo in chiaro tramite **XOR**.|Utilizza complessi cicli di **Sostituzioni** e **Permutazioni** (rete SPN) sul blocco di dati.|
|**Velocità**|**Generalmente più veloce** e con bassa latenza, ideale per dati in tempo reale.|**Generalmente più lento** a causa della complessità delle operazioni e della latenza del blocco. (Può essere velocizzato con accelerazione hardware, es. AES-NI).|
|**Parallelismo**|**Alto** (la generazione della _keystream_ può essere parallelizzata, come in AES-CTR).|**Limitato** (molte modalità richiedono l'output del blocco precedente, come in CBC).|
|**Padding (Riempimento)**|**Non richiesto**, poiché cifra bit per bit.|**Spesso richiesto** in alcune modalità (es. ECB, CBC) se il messaggio non riempie esattamente l'ultimo blocco.|
|**Vulnerabilità**|**Riuso della chiave/IV** è catastrofico: se la _keystream_ viene riusata, si rompe la sicurezza.|**Perdita di pattern** (solo in modalità insicure come ECB). Necessita di **Modalità Operative** per essere sicuro.|
|**Applicazioni Tipiche**|Crittografia di flussi di dati in tempo reale (VoIP, streaming video), hardware con risorse limitate (dispositivi IoT).|Crittografia di dati a riposo (file, dischi, database), protocolli di rete robusti (TLS/IPsec in modalità GCM).|

---

### 🛡️ Confusione e Diffusione

La differenza nel meccanismo di base si riconduce a come i due tipi di cifrari ottengono la sicurezza (come teorizzato da Claude Shannon):

- **Block Cipher**
    
    - Utilizza sia **Confusione** (rendere complessa la relazione tra la chiave e il testo cifrato, tramite Sostituzioni) che **Diffusione** (distribuire l'influenza di un singolo bit di testo in chiaro su tutto il testo cifrato, tramite Permutazioni).2
        

![Immagine di Substitution-Permutation Network Diagram](https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQo2y5Fd1zLSeE7QZSgHbi78STWB-KMqZ_N8qotsFJPRtUeZ2TtSB-pzc4_vAGmMCk60A7pesYbM0GUKLesX0VKORaed4MNZ95EzHYkdSAU-tg_c10)

Shutterstock

```
* Questo li rende robusti, ma complessi e lenti.
```

- **Stream Cipher**
    
    - Si basa quasi esclusivamente sulla **Confusione** (attraverso l'uso della _keystream_ pseudocasuale) e sull'operazione semplice **XOR**. La _keystream_ deve essere estremamente imprevedibile per garantire la sicurezza.
        

La modalità **[[CTR]] (Counter Mode)**, come discusso in precedenza, è un esempio di come un Block Cipher (**[[AES]]**) possa essere trasformato per operare come un **Stream Cipher**, combinando la robustezza dell'algoritmo AES con la velocità e il parallelismo dell'elaborazione a flusso.

Per una panoramica completa, inclusi diagrammi e spiegazioni sul perché i cifrari a flusso sono generalmente più veloci, ti consiglio di guardare questo video: Stream Cipher vs. Block Cipher - YouTube.

## Perché lo [[Stream Cipher]] è più veloce del [[Block Cipher]]
Lo **stream cipher** (cifrario a flusso) è generalmente **più veloce** di un **block cipher** (cifrario a blocchi) per diversi motivi fondamentali legati al modo in cui elaborano i dati e al tipo di operazioni che eseguono.

---

### ⚡️ Vantaggi di Velocità dello Stream Cipher

1. **Elaborazione Bit-by-Bit o Byte-by-Byte:**
    
    - Gli stream cipher cifrano i dati **un bit, un byte o una parola di computer alla volta**, combinando il dato con una sequenza di cifre pseudocasuali (keystream) generate in modo sequenziale.
        
    - I block cipher, al contrario, devono attendere che si accumuli un intero **blocco** (ad esempio 64 o 128 bit) di dati in chiaro prima di poter iniziare l'operazione di cifratura. Questa attesa introduce **latenza**.
        
2. **Operazioni Semplici e Veloci (XOR):**
    
    - L'operazione principale negli stream cipher è quasi sempre l'**XOR (OR esclusivo)** tra il bit/byte di testo in chiaro e il bit/byte della _keystream_. L'operazione XOR è estremamente **semplice** e **veloce** da eseguire nell'hardware e nel software.
        
    - I block cipher eseguono operazioni molto più **complesse**, come molteplici cicli di sostituzioni (S-boxes) e permutazioni, per ottenere _confusione_ e _diffusione_, il che aumenta significativamente il **carico computazionale**.
        
3. **Basso Overhead Computazionale:**
    
    - Negli stream cipher, la decifratura è semplicemente un'altra operazione XOR, che è l'esatto opposto dell'operazione di cifratura (XOR con la stessa _keystream_).
        
    - Nei block cipher, il processo di decifratura è più **complesso** in quanto richiede l'inversione delle molteplici fasi di cifratura.
        
4. **Ideale per Dati in Tempo Reale:**
    
    - Gli stream cipher sono particolarmente adatti per la cifratura di flussi di dati in tempo reale (come audio, video o comunicazioni di rete), dove la **bassa latenza** e l'elaborazione continua sono cruciali.
        

---

### ⚠️ Limitazioni del Block Cipher

Sebbene i block cipher (come AES) possano beneficiare dell'**accelerazione hardware** su molte CPU moderne, il loro design intrinseco impone un overhead maggiore per l'elaborazione in blocco rispetto all'elaborazione bit-by-bit:

- **Necessità di Riempimento (Padding):** Se la dimensione del testo in chiaro non è un multiplo esatto della dimensione del blocco, è necessario aggiungere un _padding_ (riempimento) al blocco finale, aggiungendo un piccolo sovraccarico.
    
- **Complessità Algoritmica:** Le complesse operazioni necessarie per garantire la sicurezza sono intrinsecamente più lente dell'unica operazione XOR.
    

In sintesi, la velocità dello stream cipher deriva principalmente dalla sua capacità di elaborare i dati in modo **sequenziale** e **continuo** (bit-by-bit) utilizzando l'operazione **XOR**, che è la più efficiente dal punto di vista computazionale.

Per una spiegazione più approfondita sulla differenza tra le due tipologie di cifrari, puoi guardare Stream Cipher vs. Block Cipher.

## Perché sono tornati di moda i [[Stream Cipher]]?

Gli **Stream Cipher** sono tornati "di moda" grazie all'emergere di **algoritmi moderni e ben progettati** come **ChaCha20** (e la sua variante autenticata **ChaCha20-Poly1305**), che hanno superato i limiti di sicurezza e performance dei vecchi cifrari a flusso come RC4.

La loro rinnovata popolarità è guidata principalmente da tre fattori: **Efficienza Software, Parallelismo e Applicazioni su Hardware Limitato.**

### 1. ⚡ Efficienza e Velocità in Software (Assenza di Hardware AES-NI)

La ragione principale è legata alle prestazioni e all'architettura dei processori:

- **Ottimizzazione Software:** I moderni stream cipher come **ChaCha20** sono progettati per funzionare in modo estremamente efficiente e veloce nelle CPU con istruzioni generiche, sfruttando operazioni semplici e presenti in abbondanza in tutti i processori, come l'**addizione, la rotazione e l'XOR (ARX)**.
    
- **Contrasto con AES-NI:** Il principale concorrente, AES (un Block Cipher), è spesso velocizzato dall'hardware specializzato chiamato **AES-NI** presente nelle CPU moderne. Tuttavia:
    
    - **Piattaforme Mobile e IoT:** Molti dispositivi (smartphone di fascia media, router, dispositivi IoT) utilizzano architetture **ARM** o non hanno l'accelerazione hardware AES-NI. Su queste piattaforme, gli stream cipher come ChaCha20 possono essere **significativamente più veloci e consumare meno batteria** rispetto a un'implementazione software di AES.
        
    - **Patch di Sicurezza:** Quando gli aggiornamenti di sicurezza devono essere applicati rapidamente, l'implementazione software di ChaCha20 è spesso più facile e veloce da distribuire.
        

### 2. 🔀 Parallelismo e Latenza

I moderni Stream Cipher, inclusa la modalità CTR che emula il loro comportamento, offrono vantaggi operativi che i Block Cipher non riescono a eguagliare in tutte le loro modalità:

- **Parallelismo Naturale:** Poiché ogni blocco della _keystream_ è generato indipendentemente dagli altri (dipende solo dal Nonce e dal Contatore), l'intera operazione di cifratura può essere facilmente **parallelizzata** su più core della CPU o in thread separati. Questo massimizza l'efficienza sui moderni processori multi-core.
    
- **Bassa Latenza:** Possono iniziare la cifratura **immediatamente** (bit-by-bit o byte-by-byte) senza dover aspettare di riempire un intero blocco (come invece accade con molte modalità di Block Cipher). Questo è cruciale per la comunicazione in tempo reale.
    
- **Nessun Padding:** Non è necessario alcun _padding_ (riempimento) per l'ultimo blocco, semplificando la gestione dei messaggi di lunghezza arbitraria e non aggiungendo _overhead_ (costo aggiuntivo in termini di dati).
    

### 3. 🌐 Adozione Diffusa nei Protocolli di Rete

La performance e la sicurezza di algoritmi come **ChaCha20-Poly1305** hanno portato a una rapida adozione nei protocolli di comunicazione chiave:

- **TLS 1.3:** Nelle versioni moderne del protocollo di sicurezza per il web (TLS 1.3), ChaCha20-Poly1305 è uno dei due unici cifrari autenticati raccomandati (l'altro è AES-GCM).
    
- **WireGuard:** Il protocollo VPN di nuova generazione, noto per la sua semplicità e velocità, utilizza esclusivamente ChaCha20-Poly1305.
    
- **Applicazioni di Messaggistica:** Molte app di messaggistica sicura utilizzano o raccomandano ChaCha20-Poly1305 per l'efficienza sui dispositivi mobili.
    

In conclusione, la rinascita degli Stream Cipher non è dovuta a un ripensamento sulla teoria dei Block Cipher, ma alla creazione di algoritmi (come ChaCha20) che offrono un **equilibrio superiore tra sicurezza e prestazioni in ambienti software e con risorse limitate**, rispondendo in modo più efficace alle esigenze del mondo moderno mobile e dell'IoT.