# OAEP (Optimal Asymmetric Encryption Padding)

## Introduzione a OAEP

**OAEP** (anche detto **RSA-OAEP**)sta per **Optimal Asymmetric Encryption Padding** (Padding per Cifratura Asimmetrica Ottimale). Questo è lo standard PKCS#1 v2.2.

- Cos'è?
    
    OAEP è uno schema di padding sicuro progettato per essere utilizzato con la cifratura RSA. Non è un algoritmo di cifratura di per sé. Ricorda cos'è un "Cifrario Perfetto".
    
- Scopo:
    
    Il suo obiettivo è formattare il messaggio in chiaro $M$ in un modo specifico e strutturato prima che venga applicata la cifratura RSA grezza ($m^e \pmod n$). Aggiunge casualità e struttura per ottenere la sicurezza semantica (IND-CPA) e, cosa cruciale, la sicurezza contro gli attacchi a testo cifrato scelto (IND-CCA).
    
- **Caratteristiche Chiave:**
    
    - **Previene l'[[Chosen-Ciphertext Attack (CCA)]]:** Questo è il suo vantaggio principale rispetto al vecchio padding PKCS#1 v1.5.
        
    - **Cifratura Probabilistica:** Utilizza un **seed** casuale e una **Mask Generation Function (MGF1)**.
        
    - **Sicurezza Semantica:** A causa del seed casuale, cifrare lo _stesso messaggio_ più volte produrrà un _testo cifrato diverso_ ogni volta.
        
    - **Standardizzazione:** È lo standard moderno, definito in **PKCS#1 v2.2** (RFC 8017).
        
- Caso d'Uso:
    
    Il processo di cifratura completo e sicuro è:
    
    ```c
    Ciphertext = RSA_Encrypt(OAEP(message, seed)).
    ```
    
    È lo standard raccomandato per tutte le nuove applicazioni di confidenzialità basate su RSA. Questo tipo di utilizzo di RSA è riconosciuto come [[RSA-OAEP]].
    

---

## OAEP: Contesto e Obiettivi di Sicurezza

OAEP è stato introdotto da Bellare e Rogaway nel 1994 per correggere le vulnerabilità note dell'RSA "textbook" (da manuale). Vedi la risorsa originale: "Optimal Asymmetric Encryption - How to Encrypt with RSA" 1994, 1995 ([https://cseweb.ucsd.edu/~mihir/papers/oaep.pdf](https://cseweb.ucsd.edu/~mihir/papers/oaep.pdf)).

- **Oracoli Casuali:** La prova originale di sicurezza per OAEP modella le funzioni hash interne, **G** e **H**, come "oracoli casuali" (funzioni hash perfette e idealizzate). In pratica, queste sono sostituite da specifiche funzioni hash crittografiche (come SHA-256) e una Mask Generation Function (MGF).
    
- **Schema Probabilistico:** Il seed casuale assicura che la cifratura sia **probabilistica**, non deterministica, che è la prima linea di difesa contro gli attacchi.
    
- **Sicurezza CCA:** OAEP è progettato per prevenire attacchi sofisticati, come gli **Attacchi a Testo Cifrato Scelto (CCA)**, che hanno esposto le vulnerabilità del vecchio standard PKCS#1 v1.5 (ad esempio, l'attacco di Bleichenbacher).
    

### Comprendere i Livelli di Sicurezza (Attacchi "IND-")

OAEP è progettato per raggiungere il più alto livello pratico di sicurezza, IND-CCA2.

|**Notazione**|**Nome Completo**|**Capacità dell'Attaccante**|
|---|---|---|
|**IND-CPA**|Indistinguibilità sotto Attacco a Testo in Chiaro Scelto|L'attaccante può chiedere la cifratura di qualsiasi messaggio scelga. (Questa è la "sicurezza semantica" fornita da OAEP).|
|**IND-CCA1**|Indistinguibilità sotto Attacco a Testo Cifrato Scelto (non adattivo)|L'attaccante può decifrare testi cifrati _prima_ di ricevere il testo cifrato di sfida.|
|**IND-CCA2**|Indistinguibilità sotto Attacco a Testo Cifrato Scelto Adattivo|L'attaccante può decifrare _qualsiasi_ testo cifrato (prima _e dopo_ la sfida), _eccetto_ il testo cifrato di sfida stesso. Questo è il livello più forte.|

OAEP (quando implementato correttamente) fornisce sicurezza **IND-CCA2**, che è il gold standard per la crittografia a chiave pubblica.

## PPT (Probabilistic Polynomial Time)

Se un algoritmo probabilistico, che produce un output a partire da un input e da una stringa casuale, non riceve una stringa casuale, allora diventa un algoritmo deterministico. Quindi la classe di algoritmi probabilistici è più forte di quelli deterministici.

### Analisi:

> gli algoritmi probabilistici possono includere tutti gli algoritmi deterministici.

Questo è vero! Un algoritmo deterministico è solo un caso speciale di algoritmo probabilistico che "ignora" la sua stringa casuale (o usa sempre la stessa).

La tua seconda osservazione:

> anche se non usiamo il random string, noi lo consideriamo comunque un output random.

Qui c'è un piccolo malinteso.

- Se un algoritmo è _probabilistico_ (come OAEP), **deve** usare la "random string" (il _seed_ casuale) per essere sicuro. Se non la usi, l'algoritmo diventa deterministico e perde tutte le sue garanzie di sicurezza.
    
- L'output **non** è random se non usi un input random.
    

Quando diciamo che l'**Avversario** è PPT (Probabilistic Polynomial Time), intendiamo due cose:

1. **Tempo Polinomiale:** Non può impiegare un miliardo di anni per trovare la risposta. Ha un tempo di calcolo "ragionevole".
    
2. **Probabilistico:** Anche l'Avversario può "lanciare monete", cioè usare la casualità per aiutarsi nel suo attacco.
    

Spero che questo chiarisca il ruolo del Challenger e lo scenario del gioco!

Vuoi che esaminiamo perché l'algoritmo "textbook" RSA fallirebbe questo gioco?

### Spiegazione Dettagliata (Passo-Passo)

Ecco una descrizione più strutturata della fase di sfida che hai descritto:

1. **Preparazione dell'Attacco:** L'**Adversary** (l'attaccante) sonda il sistema. Ha accesso a un **oracolo di decifratura** (e talvolta di cifratura), gestito dal Challenger, e lo usa per capire come funziona il sistema.
    
2. **Produzione della Sfida:** Quando si sente pronto, l'Adversary sceglie due messaggi distinti della stessa lunghezza, $m_0$ e $m_1$, che vuole provare a distinguere. Invia entrambi questi messaggi al **Challenger**.
    
3. **Il Lancio della Moneta:** Il **Challenger** riceve $m_0$ e $m_1$. Esegue il "toss a coin": sceglie un bit $b$ in modo perfettamente casuale (o 0 o 1).
    
4. **Creazione del Testo Cifrato di Sfida:** Il Challenger seleziona il messaggio $m_b$ (quindi $m_0$ se $b=0$, oppure $m_1$ se $b=1$). Cifra _solo quel messaggio_ usando la chiave pubblica, ottenendo il "ciphertext di sfida" $c_b$.
    
5. **Invio della Sfida:** Il Challenger invia $c_b$ all'Adversary.
    

### 1. Chi è il "Challenger" (Lo Sfidante)?

Pensa al **Challenger** come all'**arbitro del gioco**.

- È un'entità teorica (un computer nel nostro esperimento) che **imposta la sfida**.
    
- **Possiede le chiavi:** È lui che genera la coppia di chiavi (pubblica e privata) all'inizio.
    
- **Rappresenta l'utente "onesto":** Si comporta come un normale utente che cifra e decifra messaggi.
    
- **Fornisce gli "oracoli":** Quando l'attaccante chiede di cifrare o decifrare qualcosa (l'oracolo), è il Challenger che esegue l'operazione usando le chiavi che possiede.
    

### 2. Chi è l'"Adversary" (L'Avversario)?

È l'**attaccante** (il "cattivo"). Il suo obiettivo è **vincere il gioco**, ovvero "rompere" la sicurezza del sistema.

### 3. Cosa sta succedendo? (Il Gioco IND-CCA2)

Il gioco che hai descritto serve a dimostrare l'**Indistinguibilità** (IND). L'obiettivo dell'Avversario è capire se riesce a **distinguere** tra la cifratura di due messaggi diversi.

Ecco i passaggi esatti:

1. **Fase di Preparazione (Fase 1 del CCA):**
    
    - L'**Avversario** può "imparare" il sistema.
        
    - Chiede all'**Oracolo** (gestito dal Challenger) di decifrare tutti i messaggi che vuole. Questa è la parte "Chosen-Ciphertext Attack" (CCA).
        
    - Il Challenger risponde onestamente a tutte le richieste.
        
2. **La Sfida (Il cuore del gioco):**
    
    - L'**Avversario** ora sceglie due messaggi qualsiasi della stessa lunghezza, $m_0$ e $m_1$. Pensa a $m_0$ = "Attacca all'alba" e $m_1$ = "Ritirata generale".
        
    - L'Avversario invia entrambi i messaggi al **Challenger**.
        
3. **Il Lancio della Moneta:**
    
    - Il **Challenger** riceve $m_0$ e $m_1$.
        
    - Fa esattamente quello che hai scritto: "toss a coin". Sceglie un bit casuale $b$ (che può essere 0 o 1).
        
    - Cifra **uno solo** dei due messaggi: $c_b = \text{Encrypt}(m_b)$.
        
    - Invia questo singolo testo cifrato, $c_b$ (chiamato il "challenge ciphertext"), all'Avversario.
        
4. **La Prova (Fase 2 del CCA):**
    
    - L'**Avversario** riceve $c_b$. Non sa se contiene $m_0$ o $m_1$.
        
    - Per scoprirlo, può continuare a fare domande all'Oracolo di decifratura (questa è la parte "adattiva" o "CCA2").
        
    - **Regola importante:** L'Avversario può chiedere di decifrare _qualsiasi cosa_, **tranne** l'esatto $c_b$ che ha appena ricevuto (sarebbe troppo facile!).
        
5. **L'Indovinello Finale:**
    
    - Alla fine, l'Avversario deve fare una scelta. Deve dire: "Il $c_b$ che mi hai mandato conteneva $m_0$ o $m_1$?"
        

### Come si vince (e cosa significa)?

- **Sistema Insicuro (es. RSA "textbook"):** L'Avversario riesce a trovare un modo per indovinare correttamente con una probabilità molto più alta del 50%. Ha trovato una falla. Il sistema **perde**.
    
- **Sistema Sicuro (come OAEP):** Non importa quanto l'Avversario studi il sistema o quante domande faccia all'oracolo, non ottiene **nessuna informazione** utile. L'unica cosa che può fare è tirare a indovinare a caso. La sua probabilità di azzeccare è esattamente del 50% (come lanciare una moneta). Il sistema **vince**.
    

In sintesi: **il Challenger è l'arbitro che testa l'Avversario** per vedere se quest'ultimo sa distinguere tra due messaggi cifrati. Se l'Avversario non sa farlo (non fa meglio che tirare a indovinare), l'algoritmo è sicuro.

---

## Lo Schema OAEP (Struttura di Feistel)

![[Pasted image 20251113160151.png]]

OAEP funziona prendendo il messaggio $m$ e un seed casuale $r$, e formattandoli usando una struttura simile a una **rete di Feistel**.

- **Parametri:**
    
    - $n$ = numero di bit nel modulo RSA (es. 2048)
        
    - $k0$ = lunghezza del seed casuale $r$ (es. 256 bit per SHA-256)
        
    - $k1$ = lunghezza del blocco di padding (es. un blocco di zeri)
        
    - $m$ = messaggio in chiaro
        
    - $G, H$ = funzioni hash crittografiche (o [[MGF]])
        
- **Processo di Cifratura (Padding):**
    
    1. **Padding del Messaggio:** Il messaggio $m$ viene riempito con $k1$ zeri fino a una lunghezza fissa.
        
    2. **Generazione del Seed:** Viene generata una stringa casuale $r$ di $k0$-bit.
        
    3. **Mascheramento del Messaggio:** Il seed $r$ viene passato attraverso la funzione hash $G$ per creare una maschera. Questa maschera viene messa in XOR con il messaggio paddato per creare il blocco $X$:
        
        - $X = (m \ || \ 00...0) \oplus G(r)$
            
    4. **Mascheramento del Seed:** Il nuovo blocco $X$ viene passato attraverso la funzione hash $H$ per creare una seconda maschera. Questa maschera viene messa in XOR con il seed $r$ per creare il blocco $Y$:
        
        - $Y = r \oplus H(X)$
            
    5. **Output:** Il messaggio paddato finale da cifrare con RSA è la concatenazione $X || Y$.
        
- **Processo di Decifratura (Unpadding):**
    
    1. **Divisione dei Blocchi:** Il blocco decifrato viene diviso nuovamente in $X$ e $Y$.
        
    2. **Recupero del Seed:** Il seed $r$ viene recuperato ricalcolando la maschera da $X$ e mettendola in XOR con $Y$:
        
        - $r = Y \oplus H(X)$
            
    3. **Recupero del Messaggio:** Il messaggio $m$ viene recuperato ricalcolando la maschera dal seed $r$ recuperato e mettendola in XOR con $X$:
        
        - $m \ || \ 00...0 = X \oplus G(r)$
            
    4. **Verifica:** Il ricevente controlla se i bit di padding $k1$ sono tutti zeri. Se non lo sono, il messaggio viene rifiutato come non valido. Questo controllo è critico per la sicurezza.
        

Nota che, grazie a come la casualità è ben integrata nello schema, il risultato è molto più potente rispetto al PKCS#1 v1.5.

### Sicurezza "Tutto-o-Niente" (All-or-Nothing)

Questa struttura di Feistel crea una proprietà "tutto-o-niente".

- Per recuperare il messaggio $m$, devi avere l'_intero_ blocco $X$ e l'_intero_ blocco $Y$.
    
- Hai bisogno di $X$ per recuperare $r$ da $Y$.
    
- Hai bisogno di $r$ per recuperare $m$ da $X$.
    
- Se un attaccante modifica _anche un solo bit_ del testo cifrato, le proprietà delle funzioni hash crittografiche faranno sì che $X$ e $Y$ decifrati siano completamente rimescolati. Ciò risulterà nel padding recuperato (bit $k1$) che _non_ sarà composto da tutti zeri, e l'intera decifratura fallirà. Questo previene proprio gli attacchi "padding oracle" che affliggono lo standard v1.5.
    

---

## RSAES-OAEP: Il Processo Completo

[[RSAES-OAEP]]

**[[RSAES]] (RSA Encryption Scheme)** combina il padding OAEP con le primitive RSA.

- **Cifratura:**
    
    1. **Encode:** Dato il messaggio $M$, produrre il messaggio codificato $M'$ usando lo schema OAEP.
        
    2. **OS2IP:** Convertire l'octet-stream $M'$ in un intero $m$ ($m = \text{OS2IP}(M')$).
        
    3. **RSAEP:** Applicare la Primitiva di Cifratura RSA: $c = \text{RSAEP}((N, e), m)$, che è $c = m^e \pmod N$.
        
    4. **I2OSP:** Convertire l'intero $c$ nell'octet-stream finale del testo cifrato $C$ ($C = \text{I2OSP}(c, |N|)$).
        
- Decifratura:
    
    Questo è l'inverso simmetrico, che utilizza la Primitiva di Decifratura RSA (RSADP) e l'operazione di unpadding OAEP ($OAEP^{-1}$).
    

Questo processo completo è lo standard moderno, **PKCS#1 v2.2**.

---

## Confronto degli Schemi di Padding RSA

|**Caratteristica**|**PKCS#1 v2.2 (RSA-OAEP)**|**PKCS#1 v1.5**|
|---|---|---|
|**Randomizzazione**|Usa MGF per una randomizzazione robusta e strutturata.|Randomizzazione più debole; meno strutturata.|
|**Resistenza CCA**|**Sicuro** contro CCA adattivo (es. attacco di Bleichenbacher).|**Vulnerabile** agli attacchi CCA adattivi.|
|**Basato su Hash**|**Sì**, integra una funzione hash (es. SHA-256) nel padding.|**No**, non usa funzioni hash nel padding.|
|**Raccomandazione**|**Raccomandato per tutte le nuove implementazioni.**|**Deprecato.** Usare solo per retrocompatibilità (es. TLS < 1.3).|

### Importanza della Sicurezza Basata su Hash in OAEP

L'uso di una funzione hash (come SHA-256) in OAEP è critico.

- Aggiunge un livello extra di robustezza crittografica.
    
- Collega crittograficamente il messaggio e il seed casuale, impedendo agli attaccanti di manipolare il padding e il messaggio in modo indipendente.
    

Curiosità: in questo algoritmo [[SHA-1]] è considerato ancora utile perché in qualche modo fornisce sufficiente sicurezza.

---

## Riepilogo

- **RSA-OAEP (PKCS#1 v2.2)** offre vantaggi di sicurezza significativi e necessari rispetto al vecchio standard **PKCS#1 v1.5**.
    
- Il suo **padding randomizzato** (usando un seed e MGF) fornisce sicurezza semantica, impedendo agli attaccanti di riconoscere pattern.
    
- La sua **struttura tutto-o-niente** fornisce una resistenza dimostrabile agli **attacchi a testo cifrato scelto (CCA)**, garantendo la robustezza dei dati.
    
- È lo standard preferito e moderno per qualsiasi applicazione che richieda confidenzialità dei dati ad alta sicurezza con RSA.
    

Di nuovo: RSA non è usato per la [[Confidentiality]] (Confidenzialità) ma solo per lo Scambio di Chiavi, che dà l'opportunità di avere Confidenzialità con una [[Symmetric Encryption]] (Cifratura Simmetrica).