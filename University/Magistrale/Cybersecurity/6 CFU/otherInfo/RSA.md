# **RSA (Rivest–Shamir–Adleman)**

> È un **algoritmo di cifratura asimmetrica** ([[Asymmetric Encryption]]) molto diffuso, sviluppato nel 1977 da Rivest, Shamir e Adleman.  
> Serve sia per **[[Confidentiality]] dei dati** che per **firme digitali e [[Authenticity]]**.

---
  

il meccanismo di funzionamento RSA si basa sulla generazione di un valore $N = p*q$, dove $p$ e $q$ due numeri primi molto grandi. Ma in che modo vengono usati $p$ e $q$ per la generazione della chiave privata $d$ e pubblica $e$?

![[Pasted image 20251023113341.png]]

Ecco i passaggi dettagliati che mostrano come `p` e `q` (i numeri primi segreti) vengano usati per generare `e` (l'esponente pubblico/public key) e `d` (l'esponente privato/private key).

---

### Meccanismo di Generazione delle Chiavi RSA

Il processo si basa sul fatto che `p` e `q` sono il **segreto fondamentale** dell'intero sistema.

#### Passo 1: Generazione di `p` e `q`

Come hai detto, il processo inizia scegliendo due numeri primi (`p` e `q`) distinti e molto grandi (es. 2048 bit ciascuno, in seguito verrà anche mostrato quanto i 2048 bit sono sicuri ed inoltre verranno mostrati [[RSA#1. Fattorizzazione di $N$|altri criteri di scelta di p e q]]).

- Questi numeri sono scelti casualmente e testati per la primalità.
    
- **Segretezza:** `p` e `q` devono rimanere assolutamente segreti.
    

#### Passo 2: Calcolo del Modulo `N`

Viene calcolato il modulo N (modulo perché verrà usato per $e \times d \equiv 1 \pmod{\phi(N)}$, che è la formula di base per generare le chiavi RSA), che è il prodotto dei due numeri primi:

$$N = p \times q$$

- **Pubblicità:** Questo N è pubblico insieme alla chiave pubblica $e$. Questo numero `N` farà parte sia della chiave pubblica che di quella privata.
    
- **Sicurezza:** La sicurezza di RSA si basa sul fatto che, sebbene tutti conoscano `N`, è computazionalmente impossibile (o meglio, richiede un tempo irragionevole) risalire ai fattori originali `p` e `q`. Questo è noto come il **[[Problema della Fattorizzazione]]**.
    

#### Passo 3: Calcolo del Totiente di Eulero, $\phi(N)$

Questo è il passaggio cruciale che lega `p` e `q` agli esponenti. Si calcola la **Funzione [[Euler's totient function|Totiente di Eulero]]** di `N`, indicata come $\phi(N)$ (phi di N).

- $\phi(N)$ conta quanti numeri interi positivi, minori di `N`, sono coprimi con `N`.
    
- Grazie a una proprietà della funzione totiente, poiché p e q sono primi, il calcolo è molto semplice:
    
    $$\phi(N) = \phi(p) \times \phi(q) = (p - 1) \times (q - 1)$$
    
- **Segretezza:** Il valore $\phi(N)$ è un **segreto** tanto quanto `p` e `q`. Se un attaccante riuscisse a indovinare $\phi(N)$, potrebbe calcolare la chiave privata `d`. E qui sorge una domanda: Se $N$ è pubblica, non posso calcolarmi facilmente $\phi(n)$? (che dovrebbe essere privata)
	- la risposta è NO! Ed è il cuore della sicurezza di RSA questo punto. Vedi a breve il perché (ma se hai fretta perché hai il cazzo duro guarda [[RSA#Spiegazione difficoltà calcolo $ phi(N)$|QUI]])


#### Passo 4: Scelta dell'Esponente Pubblico `e`

Ora si sceglie l'esponente pubblico `e`. Questo numero non deve essere segreto.

- `e` deve soddisfare due condizioni:
    
    1. Deve essere compreso tra $1$ e $\phi(N)$ (cioè $1 < e < \phi(N)$).
        
    2. Deve essere **coprimo** con $\phi(N)$. Questo significa che $\text{MCD}(e, \phi(N)) = 1$.
        
- Scelta Pratica: Per ragioni di efficienza, e non viene calcolato, ma scelto da una lista di valori noti. La scelta più comune al mondo è:
    
    e = 65537 (che è $2^{16} + 1$)
    
    Questo numero è primo e piccolo, rendendo l'operazione di "cifratura" (o verifica della firma) molto veloce.
    

#### Passo 5: Calcolo dell'Esponente Privato `d`

Infine, si calcola l'esponente privato `d`. Questo è il cuore matematico della creazione della chiave.

- `d` viene definito come l'**inverso moltiplicativo modulare** di `e` modulo $\phi(N)$.
    
- In altre parole, `d` è quel numero unico che, moltiplicato per `e`, dà come resto 1 se diviso per $\phi(N)$.
    
- La formula è:
    
    $$e \times d \equiv 1 \pmod{\phi(N)}$$
    
    (o, equivalentemente, $e \times d = 1 + k \times \phi(N)$ per qualche intero $k$).
    
- **Come si calcola?** `d` viene calcolato utilizzando l'**Algoritmo di Euclide Esteso**, che prende `e` e $\phi(N)$ come input e restituisce `d`.
    

---

### Riepilogo Finale

Alla fine del processo, abbiamo:

- Chiave Pubblica: La coppia (e, N). Questa viene distribuita al mondo.
    
    (Esempio: (65537, N))
    
- Chiave Privata: La coppia (d, N). Questa deve rimanere assolutamente segreta.
    
    (Esempio: (d_calcolato, N))
    

Come puoi vedere, `p` e `q` sono fondamentali:

1. `p` e `q` generano **`N`** (la parte pubblica).
    
2. `p` e `q` generano **$\phi(N)$** (il "modulo segreto" per gli esponenti).
    
3. $\phi(N)$ ed `e` (pubblico) generano **`d`** (il segreto privato).
    

Senza `p` e `q`, è impossibile calcolare $\phi(N)$ e, di conseguenza, è impossibile calcolare `d` a partire da `e` e `N`.

## Spiegazione difficoltà calcolo $\phi(N)$ 
### Il "Perché" (Il Problema della Fattorizzazione)

La tua domanda implicita è: "Ma se `N` è pubblico, non posso semplicemente _calcolare_ $\phi(N)$?"

La risposta è **NO**, e questo è _esattamente_ il motivo per cui RSA è sicuro. Il motivo si chiama **Problema della Fattorizzazione**: Non è solo "computazionalmente impossibile", ma è stato dimostrato che calcolare $\phi(N)$ è **computazionalmente equivalente a fattorizzare $N$**.

Questo significa che se tu trovassi un "trucco" magico per calcolare $\phi(N)$ velocemente senza conoscere $p$ e $q$, potresti usare quel trucco per fattorizzare $N$ (e viceversa). I due problemi sono legati a doppio filo.

Per capire il perché, analizziamo i due (e unici) modi che un attaccante ha per calcolare $\phi(N)$ conoscendo solo $N$.

### Metodo 1: La Definizione (Brute Force)

La definizione formale di $\phi(N)$ è: "Contare tutti i numeri $k$ tra $1$ e $N-1$ che sono coprimi con $N$ (cioè $\text{MCD}(k, N) = 1$)".

Un computer potrebbe provare a farlo:

1. Controlla `MCD(1, N)`. (È 1)
    
2. Controlla `MCD(2, N)`.
    
3. Controlla `MCD(3, N)`.
    
4. ...fino a `MCD(N-1, N)`.
    

- **Il problema:** Se $N$ è un numero a 2048 bit, il suo valore è circa $10^{617}$. Il computer dovrebbe eseguire questo controllo $10^{617}$ volte. Questo è un numero di operazioni così colossale da essere **infinitamente più lento** della stessa fattorizzazione. Questo metodo è fuori discussione.
    

### Metodo 2: La Scorciatoia (La Fattorizzazione)

L'unica "scorciatoia" conosciuta per calcolare $\phi(N)$ è usare la formula:

$$\phi(N) = (p - 1) \times (q - 1)$$

Ma per usare questa formula, devi prima trovare $p$ e $q$. E per trovare $p$ e $q$ da $N$, devi risolvere il **Problema della Fattorizzazione**.

Come mostra un grafico di complessità, entrambi i metodi sono "intrattabili" (linea rossa ed esponenziale), mentre le operazioni "facili" come la moltiplicazione o l'esponenziazione rapida sono "trattabili" (linea verde, tempo polinomiale).

### Conclusione

L'attaccante si trova di fronte a un vicolo cieco:

- **Non può** contare i numeri coprimi (Metodo 1), perché $N$ è troppo grande.
    
- **Non può** usare la formula (Metodo 2), perché non conosce $p$ e $q$.
    
- **Non può** trovare $p$ e $q$, perché la fattorizzazione è un problema troppo difficile.
    

Ecco perché $\phi(N)$, pur essendo un "parente stretto" del numero pubblico $N$, rimane un segreto inespugnabile.

### Analogia della Cassaforte

Pensa a `N` e $\phi(N)$ in questo modo:

- **`N` (Pubblico):** È come la **cassaforte** stessa. Puoi vederla, toccarla, misurare le sue dimensioni esterne. È lì, visibile a tutti.
    
- **`p` e `q` (Privati):** Sono i **numeri della combinazione**. Sono segreti e non sono scritti da nessuna parte sulla cassaforte.
    
- **$\phi(N)$ (Privato):** È il **meccanismo interno** della serratura. Il suo funzionamento dipende _direttamente_ dalla combinazione (`p` e `q`), ma è impossibile capirlo o calcolarlo semplicemente guardando la scatola di metallo (`N`).
    

### Tabella Riassuntiva

Questa tabella riassume cosa è pubblico e cosa è privato, e _perché_.

| **Componente**         | **È Pubblico o Privato?** | **Perché?**                                                                         |
| ---------------------- | ------------------------- | ----------------------------------------------------------------------------------- |
| `p` e `q`              | **Privato**               | I "segreti originali" scelti dal creatore.                                          |
| `N = p \times q`       | **Pubblico**              | È "facile" da calcolare (moltiplicare), ma "difficile" da invertire (fattorizzare). |
| $\phi(N) = (p-1)(q-1)$ | **Privato**               | **Impossibile** da calcolare conoscendo solo `N`. Richiede `p` e `q`.               |
| `e`                    | **Pubblico**              | Scelto (spesso 65537). Fa parte della chiave pubblica.                              |
| `d`                    | **Privato**               | Calcolato usando `e` e $\phi(N)$. È il "segreto finale".                            |
    

---
## Panoramica dell'Algoritmo RSA e delle sue Applicazioni

L'algoritmo RSA è un sistema di crittografia asimmetrica che si basa sull'uso di una coppia di chiavi: una **chiave pubblica** (che può essere condivisa con tutti) e una **chiave privata** (che deve essere tenuta segreta dal proprietario).

A seconda di quale chiave viene utilizzata per l'operazione iniziale (che chiamiamo genericamente "cifratura"), RSA può essere utilizzato per due scopi principali e distinti:

1. **Cifratura con Chiave Pubblica**: Per garantire **[[Confidentiality]]**.
    
2. **Cifratura con Chiave Privata**: Per garantire **[[Authenticity]]** e **[[Non-Repudiation]]** (la base per le firme digitali).
    

Analizziamo entrambi i casi.

---

## 1. Cifratura con Chiave Pubblica (Obiettivo: Confidenzialità)

Questo è l'uso più intuitivo di RSA.

- **Scenario**: Alice (A) vuole inviare un messaggio segreto (M) a Bob (B).
    
- **Processo**:
    
    1. Alice ottiene la **chiave pubblica** di Bob (che Bob ha reso disponibile a tutti).
        
    2. Alice "cifra" il messaggio M utilizzando la chiave pubblica di Bob.
        
    3. Solo Bob, che possiede la **chiave privata** corrispondente, può "decifrare" il messaggio e leggerlo.
        
- **Risultato**: Si ottiene la **Confidenzialità**. Chiunque può inviare un messaggio segreto a Bob, ma solo Bob può leggerlo.
    

### Problemi di questo approccio

Sebbene efficace per la confidenzialità, questo metodo non è quasi mai usato per cifrare messaggi lunghi per diversi motivi:

- **Performance**: La crittografia asimmetrica (RSA) è estremamente lenta (ordini di grandezza più lenta) rispetto alla [[Symmetric Encryption]] (come [[AES]]).
    
- **Limiti di Dimensione**: RSA opera su blocchi di numeri. Il messaggio (interpretato come un numero) deve essere più piccolo del modulo $N$ (la dimensione della chiave). Non è adatto per file di grandi dimensioni.
    
- **Sicurezza (Determinismo)**: L'RSA "textbook" (la pura formula matematica) è deterministico. Se non si usa un "padding" (uno schema di riempimento), cifrare lo stesso messaggio due volte produce lo stesso testo cifrato, il che è una vulnerabilità di sicurezza.
    
- **Consumo Energetico**: L'intensità computazionale lo rende problematico per dispositivi a bassa potenza (es. "battery draining").
    

### Soluzione: Cifratura Ibrida ([[Hybrid Encryption]])

Per questi motivi, RSA viene quasi sempre usato per la **confidenzialità** in un sistema ibrido, tipicamente per lo **scambio di chiavi**:

1. Alice vuole inviare un file lungo a Bob.
    
2. Alice genera una chiave simmetrica _nuova e casuale_ (es. una chiave AES a 256 bit).
    
3. Alice cifra il file lungo usando AES e questa chiave simmetrica (molto veloce).
    
4. Alice cifra la (piccola) chiave simmetrica usando la **chiave pubblica** di Bob (lento, ma applicato solo a pochi bit).
    
5. Alice invia a Bob il `file cifrato con AES`  + `la chiave AES cifrata con RSA`.
    
6. Bob usa la sua **chiave privata** per decifrare la chiave AES, e poi usa quest'ultima per decifrare il file.
    

**Rischio (Man-in-the-Middle)**: Una nota importante. Se un attaccante (Fran) inganna Alice e le fornisce una _falsa chiave pubblica_ sostenendo che sia di Bob, Alice cifrerà il messaggio (o la chiave simmetrica) con la chiave di Fran. Fran potrà decifrarlo, mentre Bob riceverà solo dati incomprensibili. Questo sottolinea la necessità di _autenticare_ le chiavi pubbliche (es. tramite certificati).

---

## 2. Cifratura con Chiave Privata (Obiettivo: Firma Digitale)

Questo è l'uso di RSA per [[Authentication]] e [[Non-Repudiation]].

- **Scenario**: Alice (A) vuole inviare un messaggio (M) a Bob (B) in modo che Bob sia sicuro che provenga da Alice e non sia stato modificato.
    
- **Processo**:
    
    1. Alice "cifra" il messaggio M usando la sua **chiave privata** (solo lei può farlo).
        
    2. Bob (o chiunque altro) riceve il messaggio "cifrato" e usa la **chiave pubblica** di Alice per "decifrarlo".
        
- **Risultato**:
    
    - **[[Authenticity]]**: Se la decifratura con la chiave pubblica di Alice funziona e produce un messaggio sensato, Bob sa che deve essere stata Alice a crearlo (poiché solo lei ha la chiave privata).
        
    - **[[Integrity]]**: Se il messaggio fosse stato alterato, la decifratura fallirebbe.
        
    - **Nessuna [[Confidentiality]]**: Chiunque può decifrare il messaggio usando la chiave pubblica di Alice.
        

Questo processo è la base del **[[Non-Repudiation]]**.

### Non-Ripudio

Il **non-ripudio** è la proprietà che impedisce al mittente di un messaggio di negare di averlo inviato. Fornisce una prova di origine e integrità che può essere verificata da terze parti (es. un giudice).

- **Differenza con [[HMAC]]**: Un HMAC (un MAC basato su chiave segreta) fornisce autenticazione e integrità, ma _non_ non-ripudio. In un HMAC, Alice e Bob condividono la stessa chiave segreta. Se Bob riceve un messaggio con un HMAC valido, sa che proviene da Alice. Tuttavia, Bob potrebbe aver creato lui stesso quel messaggio (dato che ha la chiave). Un giudice non può determinare chi dei due (che condividevano la chiave) abbia generato il messaggio. Con RSA, solo una persona (il proprietario della chiave privata) può "firmare".
    

### Problema: L'RSA "Textbook" non è ancora una Firma Sicura

Applicare l'RSA "puro" (chiamato "textbook RSA") per le firme ha una grave vulnerabilità chiamata **falsificazione esistenziale ([[Existential Forgery (E)]])**.

- **Notazione**: Sia $U$ la chiave pubblica di Alice e $V$ la sua chiave privata.
    
- **Processo di firma "ingenuo"**: Alice invia la coppia $(M, S)$, dove $S = E_V(M)$ (cifratura di M con chiave privata V).
    
- **Verifica "ingenua"**: Bob controlla se $E_U(S) = M$.
    

**L'attacco (Falsificazione Esistenziale):**

1. Un attaccante, Fran, non cerca di falsificare una firma per un messaggio $M$ specifico.
    
2. Fran sceglie un file binario _casuale_ $R$, sostenendolo come firma digitale di Alice.
    
3. Fran usa la chiave **pubblica** $U$ di Alice (che tutti conoscono) e calcola $D = E_U(R)$. (Ricorda: in RSA, la cifratura e la decifratura sono la stessa operazione matematica, $x^k \bmod N$, in questo caso $D=R^e \pmod N$ dove $(e,N)$ formano la chiave pubblica di Alice).
    
4. Fran invia a Bob la coppia $(D, R)$, sostenendo che sia un messaggio $(M, S)$ firmato da Alice.
    
5. Bob riceve $(D, R)$ ed esegue la verifica: controlla se $E_U(R) = D$. Cioè fa la stessa identica operazione che ha fatto Fran per generare D. 
    
6. L'uguaglianza è vera per costruzione! Bob accetta $(D, R)$ come un messaggio $D$ validamente firmato da Alice con la firma $R$.
    
7. Anche se $D$ è un file senza senso (spazzatura), Fran ha creato con successo una coppia (messaggio, firma) valida che Alice non ha mai generato.
    

### Soluzione: La Vera Firma Digitale RSA

Per risolvere questo problema (e per efficienza), **non si firma mai l'intero messaggio**. Si firma un suo **digest** (hash).

- **Processo di Firma (Alice)**:
    
    1. Alice calcola un hash crittografico del messaggio: $h = H(M)$. (Dove $H$ è una funzione come SHA-256, che è una _One-Way Function_ o OWF).
        
    2. Alice "cifra" (firma) solo l'hash con la sua chiave privata: $S = E_V(h) = E_V(H(M))$.
        
    3. Alice invia a Bob la coppia $(M, S)$.
        
- **Processo di Verifica (Bob)**:
    
    1. Bob riceve $(M, S)$.
        
    2. Bob calcola l'hash del messaggio $M$ ricevuto: $h_1 = H(M)$.
        
    3. Bob "decifra" la firma $S$ usando la chiave pubblica $U$ di Alice: $h_2 = E_U(S)$.
        
    4. Bob confronta i due hash:
        
        - Se $h_1 = h_2$, la firma è **accettata**.
            
        - Se $h_1 \neq h_2$, la firma è **rifiutata**.
            

**Perché funziona:**

- **[[Integrity]]**: L'hash $H(M)$ garantisce che il messaggio $M$ non sia stato alterato dopo la firma (se lo fosse, $h_1$ sarebbe diverso).
    
- **[[Authenticity]]**: La firma $S$ (cifrata con $V$) garantisce che provenga da Alice (altrimenti $h_2$ non corrisponderebbe).
    
- **[[Non-Repudiation]]**: Si ottiene solo se la verifica ha successo.
    
- **Sicurezza (vs [[Forgery]])**: L'attacco di Fran fallisce. Fran può ancora scegliere $R$ e calcolare $D = E_U(R)$, ma non può trovare un messaggio $M$ tale che $H(M) = D$, perché $H$ è una funzione _one-way_ (non invertibile). Proprio perché introduco un qualcosa che non è invertibile, per funzionare è strettamente necessario avere $M$ per produrre il digest $h_1$ che verrà poi criptato con la chiave pubblica.
    
- **Efficienza**: Firmare un hash (es. 256 bit) è molto più veloce che firmare un file di gigabyte.
    

_(Nota: L'uso di hash introduce il rischio teorico di collisioni (legato al "birthday bound"), ma l'uso di digest sufficientemente grandi come SHA-256 rende questo attacco impraticabile)._

---

## 3. Debolezze e Attacchi all'RSA "Textbook"

La sicurezza di RSA dipende da implementazioni attente. L'RSA "textbook" (la formula matematica di base) è vulnerabile.

### 1. Fattorizzazione di $N$

- **Attacco:** Se un attaccante può fattorizzare $N$ in $p$ e $q$, può calcolare $\varphi(N)$ e poi usare $e$ per trovare la chiave privata $d$. Fattorizzare $N$ rompe RSA.
    
- **Problema Aperto:** Sappiamo che (Fattorizzare $N$) $\implies$ (Rompere RSA). È vero il contrario? (Rompere RSA) $\implies$ (Fattorizzare $N$)? Non è noto.
    
- **Soluzione:** Usare una corretta generazione della chiave:
    
    - $p$ e $q$ devono essere **sufficientemente grandi** (ad es., $N$ dovrebbe essere di 2048 o 4096 bit).
        
    - $p$ e $q$ **non devono essere troppo vicini** tra loro.
        
    - $(p-1)$ e $(q-1)$ devono avere fattori primi grandi (per sventare l'algoritmo p-1 di Pollard).
        
- **Contesto Storico:** Le sfide di fattorizzazione hanno mostrato la difficoltà. RSA-640 (bit) è stato fattorizzato nel 2005. Nel 2008, il ransomware Gpcode utilizzava una chiave a 1024 bit e Kaspersky Labs stimò che sarebbero stati necessari 15 milioni di computer moderni per 1 anno per romperla. La chiave non è mai stata rotta, dimostrando la forza pratica delle chiavi a 1024 bit all'epoca.
    

---

### 2. Attacchi a Messaggi Semplici o Piccoli

- **Problema 1:** Se $m = 0$, $1$, o $N-1$, allora $RSA(m) = m$. Il testo cifrato è identico al testo in chiaro. Infatti, notiamo che $e$ deve essere dispari ed anche ≥ 3, quindi $(N-1)^e \pmod N ≡ N-1$, perché $(N-1)^2 \pmod N ≡ 1$
    
    - **Soluzione:** Usare un "salt" o padding (riempimento).
        
- **Problema 2:** Se sia $m$ che $e$ sono piccoli (ad es., $e = 3$) e $m$ è piccolo, potremmo avere $m^e < N$.
    
    - In questo caso, $C = m^e \pmod N = m^e$.
        
    - L'attaccante non ha bisogno di fare aritmetica modulare; calcola semplicemente la radice $e$-esima di $C$ per trovare $m$.
        
    - **Soluzione:** Aggiungere un padding (riempimento) non nullo a _tutti_ i messaggi per assicurarsi che $m$ non sia mai piccolo.
        

---

### 3. Attacchi con Esponente Basso ($e=3$)

- **Problema 1 (Messaggi Correlati):** Se un attaccante intercetta due messaggi correlati da una trasformazione nota, ad es., $c_1 = m^3 \pmod n$ e $c_2 = (m+1)^3 \pmod n$, può usare questa relazione algebrica (l'attacco di Coppersmith) per ricavare $m$:$$m = (c2 + 2 c1 - 1) / (c2 - c1 +2)$$
    
    - **Soluzione:** Scegliere un $e$ grande (come 65537) o usare il padding.
        
- **Problema 2 (Attacco del Teorema Cinese del Resto):** Se lo _stesso messaggio_ $m$ viene inviato a 3 utenti diversi (con $e=3$ e moduli diversi $n_1, n_2, n_3$), un attaccante intercetta:
    
    1. $c_1 = m^3 \pmod{n_1}$
        
    2. $c_2 = m^3 \pmod{n_2}$
        
    3. $c_3 = m^3 \pmod{n_3}$
        
    
    - Usando il Teorema Cinese del Resto (CRT), l'attaccante può combinare questi valori per trovare $m^3 \pmod{n_1n_2n_3}$.
        
    - Dato che $m < n_i$ per ogni $i$, $m^3$ sarà più piccolo del prodotto $n_1n_2n_3$. Il risultato è semplicemente $m^3$.
        
    - L'attaccante calcola la semplice radice cubica e trova $m$.
        
    - **Soluzione:** Aggiungere un padding casuale a ogni messaggio. Questo assicura che lo _stesso_ messaggio non venga mai inviato due volte.
        

---

### 4. Attacco alla Cifratura Deterministica

- **Problema:** L'RSA "da manuale" (textbook) è deterministico. Se un attaccante sa che il messaggio è $m_1$ ("SÌ") o $m_2$ ("NO"), può cifrare sia $m_1$ che $m_2$ con la chiave pubblica. Confronta i risultati con il testo cifrato intercettato per scoprire il messaggio.
    
- **Soluzione:** Aggiungere una stringa casuale (padding) al messaggio.

#### Esempio ***Attacco (Senza Padding)***

L'attaccante sa che il messaggio è "NO" o "SÌ".

1. Bob (Mittente): Cifra "NO".
    
    Cifratura_RSA("NO") -> produce sempre C1 (es: 12345)
    
2. **Fran (Attaccante):** Intercetta `C1` (`12345`).
    
3. **Lavoro di Fran:**
    
    - Testa "NO": `Cifratura_RSA("NO")` -> produce `12345`.
        
    - Testa "SÌ": `Cifratura_RSA("SÌ")` -> produce `67890`.
        
4. **Confronto:** Fran vede che `12345` (intercettato) è uguale a `12345` (calcolato). Ha la certezza che il messaggio fosse "NO".
    

#### Esempio tentativo di Attacco ***Con Padding Casuale***

Il padding è un blocco di dati, in parte casuale, che viene aggiunto al messaggio _prima_ della cifratura.

1. **Bob (Mittente):** Vuole cifrare "NO".
    
    - Genera una stringa casuale: `R1` (es: `askf98H3`)
        
    - Crea il blocco da cifrare: `M_paddato = "NO" + R1`
        
    - `Cifratura_RSA(M_paddato)` -> produce `C_A` (es: `55543`)
        
2. **Fran (Attaccante):** Intercetta `C_A` (`55543`).
    
3. **Lavoro di Fran:**
    
    - Fran non può più solo "testare NO". Deve testare "NO" _più un padding_. Ma non conosce il padding `R1` usato da Bob.
        
    - Fran prova a indovinare:
        
        - Genera la sua stringa casuale: `R2` (es: `JkL0f77s`)
            
        - Crea il suo blocco di test: `M_test = "NO" + R2`
            
        - `Cifratura_RSA(M_test)` -> produce `C_B` (es: `98712`)
            
4. **Confronto:** Fran confronta `C_A` (`55543`) con `C_B` (`98712`). **Sono diversi.**
    

**Risultato:** L'attacco fallisce. Fran non ottiene alcuna informazione. Il suo calcolo non corrisponde a quello che ha intercettato, anche se il messaggio di base ("NO") era lo stesso.

Per questo motivo, l'RSA "da manuale" (puro) non si usa mai nella pratica. Si usano **schemi di padding** standardizzati come **OAEP** (Optimal Asymmetric Encryption Padding), che sono progettati specificamente per incorporare casualità e prevenire questi e altri tipi di attacchi.

---
### 5. Messaggi troppo piccoli (si ricollega a quello precedente)

**Se lo spazio dei messaggi è piccolo, allora un avversario (adv.) può testare tutti i messaggi possibili.**
 
 - **esempio:** l'avversario conosce la codifica di `m` e sa che `m` è o `m1 = 10101010` o `m2 = 01010101`.
	 - L'avversario cifra `m1` e `m2` usando la chiave pubblica e verifica.
 
 **SOLUZIONE:** Aggiungi una stringa casuale nel messaggio.

---
### 6. Attacco del Modulo Comune

- **Problema:** Se due utenti sono configurati con lo _stesso modulo $n$_ (ma $e$ e $d$ diversi), è catastrofico. Supponiamo quindi di avere due Utenti: Utente 1 che si comporta da adversary ed Utente 2 che è la vittima:
    
- L'Utente 1 (con $e_1, d_1, n$) potrebbe usare le proprie chiavi per ricavare $p$ e $q$ (è complicato ma possibile).
    
- Una volta ottenuti $p$ e $q$, può calcolare $\varphi(N)$ e usarlo per trovare la chiave privata $d_2$ dell'Utente 2 dalla sua chiave pubblica $e_2$.
    
- **Soluzione:** Ogni persona deve generare il proprio $N$ univoco.

## Altri Attacchi a RSA

Oltre all'attacco base di fattorizzazione, ci sono molti altri modi per attaccare un'implementazione di RSA, specialmente se segue la definizione "da manuale" (textbook) senza un adeguato padding (riempimento).

- **Attacchi di Fattorizzazione:** L'attacco matematico più diretto. Se un attaccante può fattorizzare il modulo $N$ nelle sue componenti prime $p$ e $q$, può calcolare la chiave privata $d$.
    
- **Attacchi con Esponente Basso:** Usare un esponente pubblico piccolo (come $e=3$) può rendere RSA vulnerabile se lo stesso messaggio viene inviato a più destinatari (es. l'attacco broadcast di Håstad) o se il messaggio è piccolo.
    
- **Attacco del Modulo Comune:** Se lo stesso modulo $N$ è usato da utenti diversi (con coppie $(e,d)$ diverse), un utente può potenzialmente usare le proprie conoscenze per fattorizzare $N$ o decifrare messaggi inviati ad altri.
    
- **Attacco del Primo Piccolo:** Se uno dei primi ($p$ o $q$) è troppo piccolo, può essere facilmente trovato per divisione di prova (trial division) o altri metodi di fattorizzazione.
    
- **Attacchi a Canale Laterale (Side-Channel):** Questi attacchi non rompono la matematica ma sfruttano l'implementazione fisica.
    
    - **Attacchi a Tempo (Timing):** Misurando precisamente quanto tempo impiega la decifratura, un attaccante potrebbe essere in grado di dedurre i bit della chiave privata $d$.
        
    - **Attacchi sull'Energia/Potenza:** Misurare il consumo energetico di un dispositivo (come una smart card) durante la decifratura può far trapelare informazioni sulla chiave privata.
        
- **Attacchi a Iniezione di Errore (Fault-Injection):** Causare deliberatamente errori durante il calcolo crittografico (ad es. fluttuando tensione o temperatura) può a volte portare il dispositivo a produrre dati corrotti che rivelano informazioni segrete.
    

---

### Proprietà Moltiplicativa e Malleabilità

In crittografia, si dice che una funzione $f$ ha un omomorfismo moltiplicativo (o è semplicemente moltiplicativa) se:

$$f(m_1 \cdot m_2) \equiv f(m_1) \cdot f(m_2) \pmod n$$

Questo è vero per la cifratura RSA "da manuale":

$$RSA(m_1 \cdot m_2) = (m_1 \cdot m_2)^e \pmod N = (m_1^e \cdot m_2^e) \pmod N = RSA(m_1) \cdot RSA(m_2) \pmod N$$

- Questa proprietà rende RSA **malleabile**. La malleabilità significa che un attaccante può modificare un testo cifrato in un altro testo cifrato valido per un testo in chiaro correlato, senza conoscere nessuno dei due testi in chiaro.
    
- Ad esempio, se un attaccante ha il testo cifrato $C = M^e \pmod N$, può facilmente creare un testo cifrato per $2M$ calcolando $C' = C \cdot 2^e \pmod N$. Il destinatario decifrerà $C'$ come $2M$, potendo essere ingannato nell'accettare un messaggio modificato. Infatti:

	- adv. uses $C'$ as chosen ciphertext and asks the oracle for $Y = (C')^d \bmod N$, but….$$C' = (C \bmod N)\cdot(2^e \bmod N) = (M^e \bmod N)\cdot(2^e \bmod n) = (2M)^e \bmod N$$
	- thus adv. got Y = (2M)

---

### Attacchi a RSA: Sfruttare la Malleabilità

La proprietà moltiplicativa può essere generalizzata:

Se $M = M_1 \cdot M_2 \cdot \dots \cdot M_k$, allora:

$$RSA(M) = RSA(M_1) \cdot RSA(M_2) \cdot \dots \cdot RSA(M_k) \pmod N$$

Questo permette a un avversario di costruire testi cifrati per messaggi compositi se conosce i testi cifrati delle loro componenti.

**Soluzione:** Usare sempre uno schema di **padding** sicuro (come OAEP) prima di cifrare. Il padding distrugge questa struttura moltiplicativa, rendendo la cifratura non malleabile.

---

### Esempio di Attacco con Testo Cifrato Scelto (Chosen Ciphertext Attack - CCA)

Un avversario vuole decifrare un testo cifrato target $C = M^e \pmod N$.

1. L'avversario calcola un nuovo testo cifrato $X$ moltiplicando $C$ per la cifratura di un numero scelto (ad es., $2$):
    
    $$X = (C \cdot 2^e) \pmod N$$
    
2. L'avversario invia $X$ alla vittima (o a un oracolo di decifratura) e gli chiede di decifrarlo. La vittima potrebbe essere indotta a farlo se $X$ sembra un messaggio valido diverso.
    
3. La vittima decifra $X$ e restituisce il risultato $Y$:
    
    $$Y = X^d \pmod N = (C \cdot 2^e)^d \pmod N = (C^d \cdot (2^e)^d) \pmod N$$
    
    Dato che $C^d = M$ e $(2^e)^d = 2^{ed} \equiv 2^1 \pmod N$, otteniamo:
    
    $$Y = M \cdot 2 \pmod N$$
    
4. L'avversario ora ha $Y = 2M$. Può facilmente recuperare il messaggio originale $M$ calcolando:
    
    $$M = Y \cdot 2^{-1} \pmod N$$
    
    (dove $2^{-1}$ è l'inverso moltiplicativo modulare di 2 modulo $N$).
    

---

### Attacco con Testo Cifrato Scelto (Generale)

Questa è una versione più generale dell'attacco precedente.

Assumiamo che un attaccante $T$ conosca un testo cifrato target $c = M^e \pmod N$.

1. $T$ sceglie casualmente un valore $X$.
    
2. $T$ calcola un nuovo testo cifrato $c' = c \cdot X^e \pmod N$.
    
3. $T$ chiede all'oracolo di decifratura di decifrare $c'$.
    
4. L'oracolo restituisce il testo in chiaro $M' = (c')^d \pmod N$.
    
5. $T$ può ora calcolare il messaggio originale $M$:
    
    $$M' = (c')^d = (c \cdot X^e)^d = c^d \cdot (X^e)^d = M \cdot X \pmod N$$
    
    Quindi, $M = M' \cdot X^{-1} \pmod N$.
    

**Soluzione:** Il processo di decifratura deve **verificare rigorosamente la struttura** del messaggio decifrato prima di restituirlo. Se viene utilizzato uno schema di padding sicuro (come OAEP), il messaggio decifrato $M'$ avrà molto probabilmente un padding non valido e l'oracolo restituirà un errore invece del testo in chiaro grezzo, sventando l'attacco.

---

### Attacchi all'Implementazione (Side-Channel)

Questi attacchi non rompono la matematica di RSA ma sfruttano le debolezze nel modo in cui è implementato sull'hardware reale.

- **Attacchi a Tempo (Timing):** Il tempo necessario per eseguire l'esponenziazione modulare $C^d \pmod N$ può dipendere dai bit specifici della chiave privata $d$ (ad es., un bit '1' potrebbe richiedere più tempo per essere processato rispetto a un bit '0' a causa di un passo di moltiplicazione extra). Misurando queste minuscole differenze su molte decifrature, un attaccante può recuperare $d$.
    
- **Analisi dell'Energia/Potenza:** Similmente al tempo, la quantità di energia consumata da un processore (come in una smart card) può variare a seconda dell'operazione eseguita. L'Analisi Differenziale della Potenza (DPA) può essere usata per estrarre la chiave.
    
- **Soluzione:** Usare **implementazioni a tempo costante** in cui ogni decifratura richiede la stessa quantità di tempo indipendentemente dalla chiave o dall'input. Un'altra tecnica è il **blinding** (mascheramento), in cui valori casuali vengono introdotti nel calcolo per mascherare gli input effettivi, per poi essere rimossi alla fine.
    

---

## RSA - Conclusione sugli Attacchi

- **L'implementazione "da manuale" di RSA NON è sicura.** Non soddisfa i criteri di sicurezza moderni (come l'indistinguibilità sotto attacco con testo cifrato scelto, IND-CCA).
    
- È vulnerabile a molti attacchi matematici e implementativi a causa della sua natura deterministica e della sua malleabilità.
    
- **Versione Standard:** In pratica, RSA è sempre usato con uno schema di padding. Il messaggio $M$ viene pre-elaborato in un messaggio con padding $M'$ prima della cifratura.
    
    - $C = (M')^e \pmod N$
        
    - Poiché $M'$ contiene dati casuali (dallo schema di padding), la cifratura diventa probabilistica e non malleabile.

Il padding è definito dai PKCS che sono standard da seguire.

### PKCS: Lo Standard per il Padding

**[[PKCS]]** sta per **Public-Key Cryptography Standards** (Standard per la Crittografia a Chiave Pubblica). Si tratta di un insieme di standard sviluppati da RSA Laboratories per garantire l'implementazione sicura e l'interoperabilità della crittografia a chiave pubblica.

|**Standard**|**Titolo**|**Funzione / Descrizione**|
|---|---|---|
|**PKCS #1**|**RSA Cryptography Standard**|Definisce i formati corretti per la **cifratura RSA** e le **firme**, inclusi gli schemi di **padding** cruciali (come OAEP e PSS) necessari per fermare gli attacchi descritti sopra.|
|**PKCS #3**|Diffie-Hellman Key Agreement|Definisce il formato di scambio chiavi DH. (Ora ampiamente obsoleto e sostituito da standard IETF).|
|**PKCS #5**|Password-Based Cryptography|Definisce le funzioni di derivazione della chiave (PBKDF1, PBKDF2) per trasformare le password in chiavi crittografiche.|
|**PKCS #6**|Extended Certificate Syntax|Definisce le estensioni dei certificati. (Obsoleto, sostituito da X.509v3).|

---

### Parte 5: La Soluzione - PKCS (Public-Key Cryptography Standards)

**Conclusione: L'RSA "da manuale" (Textbook) NON è sicuro.**

Per essere sicuro, RSA deve essere usato con uno **schema di padding**. Gli standard per questo sono definiti da **PKCS**.

#### PKCS #1 (Vecchia Versione)

Questo standard definiva uno schema di padding per la cifratura:

`m = 0x00 || 0x02 || [almeno 8 byte casuali non zero] || 0x00 || M`

- **0x00** (primo byte): Assicura che il numero risultante sia $< N$.
    
- **0x02**: Indica la cifratura (0x01 era usato per le firme).
    
- **Byte casuali**: Questo è il padding che risolve la maggior parte delle debolezze di RSA. Rende la cifratura non deterministica e previene attacchi a messaggi piccoli o correlati.

vedi anche [[PKCS]]

Proprio perché RSA textbook è effettivamente insicuro, vediamo delle implementazioni di RSA

# Implementazione RSA

Questa sezione copre i passaggi pratici necessari per implementare l'algoritmo RSA, dalla generazione della chiave fino al processo sicuro di cifratura e decifratura.

L'algoritmo "da manuale" di base coinvolge due formule principali:

- **Cifratura (Chiave Pubblica):** $c = m^e \pmod n$
    
- **Decifratura (Chiave Privata):** $m = c^d \pmod n$
    

Tuttavia, un'implementazione _sicura_ richiede diversi passaggi aggiuntivi per essere protetta dagli attacchi.

## Proprietà Chiave (Riepilogo)

- **Unicità:** Il requisito che $\gcd(e, \phi(n)) = 1$ è cruciale. Assicura che $e$ abbia un inverso moltiplicativo modulare unico $d$, necessario affinché la decifratura funzioni.
    
- **L'Assunzione RSA:** Trovare la chiave privata $d$ è computazionalmente _facile_ se si conoscono i fattori primi $p$ e $q$. Tuttavia, trovare $d$ data solo la chiave pubblica $(n, e)$ si assume essere computazionalmente _difficile_. Questa è l'assunzione fondamentale su cui si basa la sicurezza di RSA.
    
- **Esponente Pubblico (e):** L'esponente pubblico $e$ viene _scelto_, non calcolato. Può essere piccolo per rendere la cifratura veloce.
    
    - Un valore comune è **$e=3$**, ma questo è **problematico** in quanto vulnerabile ad attacchi specifici (come attacchi a messaggi piccoli o broadcast) se non implementato con un padding adeguato.
        
    - Il valore più comune e raccomandato è **$e = 65537$** (che è $2^{16}+1$).
        
- **Prestazioni:** Sia la cifratura che la decifratura comportano l'esponenziazione modulare.
    
    - **Cifratura:** È generalmente _veloce_ perché $e$ è scelto per essere piccolo.
        
    - **Decifratura:** È significativamente più _lenta_ perché l'esponente privato $d$ viene calcolato, è tipicamente molto grande (dello stesso ordine di grandezza di $n$) e non può essere ottimizzato allo stesso modo.
        

## Costruzione di una Coppia di Chiavi RSA (Compito di Alice)

Ecco il processo passo-passo per generare le chiavi pubblica e privata:

1. **Generare Primi:** Alice sceglie casualmente due numeri primi molto grandi e distinti, $p$ e $q$. Questi devono essere crittograficamente casuali in modo che un attaccante non possa indovinarli.
    
2. **Calcolare il Modulo:** Alice calcola il modulo $n$ moltiplicando i primi: $n = p \cdot q$.
    
3. **Calcolare il Totiente:** Alice calcola la funzione totiente di Eulero $\phi(n)$: $\phi(n) = (p-1)(q-1)$.
    
4. **Scegliere l'Esponente Pubblico:** Alice _sceglie_ un esponente pubblico $e$ (ad esempio, 65537) che sia coprimo con $\phi(n)$. Questo significa $\gcd(e, \phi(n)) = 1$.
    
5. **Calcolare l'Esponente Privato:** Alice _calcola_ l'esponente privato $d$ trovando l'inverso moltiplicativo modulare di $e$ modulo $\phi(n)$. Questo è il valore che soddisfa l'equazione: $d \cdot e \equiv 1 \pmod{\phi(N)}$.
    
6. **Pubblicare/Conservare le Chiavi:**
    
    - **Chiave Pubblica:** Alice pubblica $(n, e)$. Questa viene condivisa con il mondo.
        
    - **Chiave Privata:** Alice conserva $(n, d)$ segreta.
        
    - **Segreto Cruciale:** Alice deve anche mantenere segreti $p$, $q$ e $\phi(N)$. Se uno qualsiasi di questi viene trapelato, $d$ può essere facilmente ricalcolato. I primi $p$ e $q$ sono spesso conservati segreti insieme a $d$ per consentire un processo di decifratura molto più veloce utilizzando il **Teorema Cinese del Resto (CRT)**.
        

## Dettagli di Implementazione in Tre Passaggi

### Passaggio 1. Trovare Grandi Numeri Primi

Questo è un passaggio critico per la generazione delle chiavi.

- **Algoritmo:**
    
    1. Scegliere casualmente un grande intero dispari della lunghezza in bit desiderata (es. 1024 bit).
        
    2. Testare se questo intero è primo. Questo **non** viene fatto con un test deterministico (che è troppo lento), ma con un veloce **test di primalità probabilistico** come l'algoritmo di **Miller-Rabin**.
        
    3. Se il test fallisce, ripetere con un nuovo intero casuale.
        
- **Perché funziona:** Il **Teorema dei Numeri Primi** afferma che i numeri primi sono relativamente frequenti. La distanza media tra primi vicino a un grande numero $N$ è approssimativamente $\ln(N)$. Questo significa che in media, dobbiamo testare solo circa $\ln(N)$ numeri dispari casuali per trovare un primo.
    

### Passaggio 2. Esponenziazione Modulare (Cifratura/Decifratura)

Il calcolo di $m^e \pmod n$ non viene effettuato calcolando $m^e$ e poi prendendo il resto, poiché il numero intermedio sarebbe astronomicamente grande.

- **Algoritmo:** L'operazione viene eseguita utilizzando l'**Esponenziazione mediante Quadrature Ripetute** (chiamata anche metodo binario).
    
- **Costo:** Questo algoritmo è molto efficiente, richiedendo solo $O(\log N)$ moltiplicazioni modulari.
    
- **Cifratura Veloce ($e$):**
    
    - Se **$e=3$**: $m^3 \pmod n$ è solo $(m^2 \pmod n) \cdot m \pmod n$. (2 moltiplicazioni).
        
    - Se **$e=65537 = 2^{16}+1$**: Il calcolo è $m^{2^{16}+1} \pmod n$. Questo richiede 16 quadrature (per ottenere $m^{2^{16}}$) e 1 moltiplicazione finale (per ottenere $m^{2^{16}} \cdot m$), per un totale di **17** operazioni.
        

### Passaggio 3. Calcolare $d$ (L'Algoritmo di Euclide Esteso)

Per trovare la chiave privata $d$, dobbiamo risolvere $d \cdot e \equiv 1 \pmod{\phi(N)}$. Questo viene fatto utilizzando l'**Algoritmo di Euclide Esteso (EEA)**, che trova l'inverso moltiplicativo modulare di $e$ modulo $\phi(N)$.

- **Pseudocodice:**
    
    ```c
    /*
     * Trova l'inverso moltiplicativo modulare di e modulo phi.
     * Restituisce d tale che (d * e) % phi == 1
     */
    function mod_inverse(int e, int phi) {
        int x0 = 1, x1 = 0;
        int a = e, b = phi;
    
        while (b != 0) {
            int q = a / b;
    
            // Passaggio Euclideo Standard
            int t = b;
            b = a % b;
            a = t;
    
            // Aggiorna coefficienti di Bézout
            t = x1;
            x1 = x0 - q * x1;
            x0 = t;
        }
    
        // Alla fine, x0 è l'inverso modulare.
        // Se x0 è negativo, aggiungi phi per portarlo nell'intervallo corretto.
        if (x0 < 0) {
            x0 = x0 + phi;
        }
        return x0;
    }
    ```
    

## Codifica: Collegare Testo e Numeri

Le primitive RSA (come [[RSAEP]]/[[RSADP]]) operano solo su numeri, ma i messaggi sono flussi di byte (testo, file, ecc.). Abbiamo bisogno di un modo standard per convertire tra loro.

- **[[OS2IP]] (Octet-Stream to Integer Primitive):**
    
    - Converte una stringa di $k$ byte in un singolo grande intero.
        
    - Lo fa interpretando la stringa di byte come un numero **big-endian** in base 256.
        
    - _Esempio:_ `b'\x01\x02\x03\x04'` diventa:
        
        - $1 \times 256^3 = 16,777,216$
            
        - $2 \times 256^2 = 131,072$
            
        - $3 \times 256^1 = 768$
            
        - $4 \times 256^0 = 4$
            
        - **Intero Totale:** 16,909,060
            
- **[[I2OSP]] (Integer to Octet-Stream Primitive):**
    
    - Converte un intero indietro in una stringa di $k$ byte.
        
    - $k$ è la lunghezza fissa del modulo $N$ in byte (es. $k=256$ per una chiave a 2048 bit).
        
    - _Esempio:_ Convertire l'intero 84,281,096 in una stringa di 8 byte.
        
        - Intero in hex: `0x05060708`
            
        - Riempito a 8 byte: `00 00 00 00 05 06 07 08`
            
        - **Risultato (Stringa di Ottetti):** `b'\x00\x00\x00\x00\x05\x06\x07\x08'`
            

## Lo Schema Sicuro: RSA con Padding (PKCS#1)

L'RSA "da manuale" (solo $m^e \pmod n$) è **pericolosamente insicuro**. È deterministico (lo stesso $m$ dà sempre lo stesso $c$) e malleabile (un attaccante può alterare il testo cifrato). Per essere sicuro, RSA _deve_ utilizzare uno **schema di padding**.

### RSAES-PKCS1-v1.5

Questo è lo standard di padding originale e ampiamente utilizzato.

- Formato del Padding: Un messaggio con padding $M'$ viene costruito prima della cifratura:
    
    M' = 0x00 || 0x02 || PS || 0x00 || M
    
- **Componenti:**
    
    - `0x00`: Un singolo byte, assicura che il numero finale sia minore di $N$.
        
    - `0x02`: Un singolo byte, il tipo di blocco, che indica la cifratura.
        
    - `PS`: Una stringa di padding di byte casuali, **non-zero**. Deve essere lunga almeno 8 byte.
        
    - `0x00`: Un singolo byte separatore.
        
    - `M`: Il messaggio originale.
        
- **Esempio (chiave a 2048 bit, messaggio di 100 byte):**
    
    - Dimensione Chiave/Modulo ($k$) = 256 byte.
        
    - Dimensione Messaggio = 100 byte.
        
    - Dimensione Padding = $256 - 1 \text{ (00)} - 1 \text{ (02)} - 1 \text{ (sep)} - 100 \text{ (msg)} = 153$ byte.
        
    - `M' = 0x00 || 0x02 || [153 byte casuali non-zero] || 0x00 || [messaggio di 100 byte]`
        

Questo aiuta a proteggersi da alcuni attacchi di [[Forgery]] (falsificazione).

### Processo Completo di Cifratura ([[RSAES]])

1. **Pad:** Creare il messaggio con padding $M'$ secondo lo schema v1.5.
    
2. **Convertire:** Creare l'intero $m = \text{OS2IP}(M')$.
    
3. **Cifrare (Primitiva):** Calcolare l'intero cifrato $c = m^e \pmod N$. (Questa è la **[[RSAEP]]**).
    
4. **Convertire:** Convertire l'intero $c$ indietro in byte: $C = \text{I2OSP}(c)$.
    

La decifratura (**[[RSADP]]**) è l'inverso: $C \rightarrow c \rightarrow m \rightarrow M'$. Il ricevente poi analizza $M'$ per trovare il separatore `0x00` ed estrarre il messaggio originale $M$.

### Avviso di Sicurezza: PKCS#1 v1.5

**PKCS#1 v1.5 è ora considerato insicuro e deprecato per la cifratura.** Sebbene il suo padding casuale prevenga semplici attacchi deterministici, è criticamente vulnerabile agli **[[Chosen-Ciphertext Attack (CCA)]]**, specificamente l'**attacco "padding oracle" di Bleichenbacher**. Un attaccante può decifrare messaggi inviando testi cifrati leggermente modificati e osservando se il server risponde con un "errore di padding".

## Lo Standard Moderno: [[RSA-OAEP]]

Per affrontare le gravi falle di sicurezza nella v1.5, è stato creato un nuovo schema di padding: **OAEP (Optimal Asymmetric Encryption Padding)**.

- OAEP è uno schema di padding più complesso che incorpora una funzione hash e una Mask Generation Function (MGF).
    
- Non è vulnerabile agli attacchi padding oracle.
    
- È l'attuale standard raccomandato per tutte le nuove applicazioni che utilizzano RSA per la cifratura.


# RSA: OAEP (Optimal Asymmetric Encryption Padding)

## Introduzione a OAEP

**OAEP** sta per **Optimal Asymmetric Encryption Padding** (Padding per Cifratura Asimmetrica Ottimale). Questo è lo standard PKCS#1 v2.2.

- Cos'è?
    
    OAEP è uno schema di padding sicuro progettato per essere utilizzato con la cifratura RSA. Non è un algoritmo di cifratura di per sé. Ricorda cos'è un "[[Perfect Cipher]]".
    
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
    
    È lo standard raccomandato per tutte le nuove applicazioni di confidenzialità basate su RSA. Questo tipo di utilizzo di RSA è riconosciuto come [[RSAES-OAEP]].
    

---

## OAEP: Contesto e Obiettivi di Sicurezza

[[RSA-OAEP]] è stato introdotto da Bellare e Rogaway nel 1994 per correggere le vulnerabilità note dell'RSA "textbook" (da manuale). Vedi la risorsa originale: "Optimal Asymmetric Encryption - How to Encrypt with RSA" 1994, 1995 ([https://cseweb.ucsd.edu/~mihir/papers/oaep.pdf](https://cseweb.ucsd.edu/~mihir/papers/oaep.pdf)).

- **Oracoli Casuali:** La prova originale di sicurezza per OAEP modella le funzioni hash interne, **G** e **H**, come "oracoli casuali" (funzioni hash perfette e idealizzate). In pratica, queste sono sostituite da specifiche funzioni hash crittografiche (come SHA-256) e una [[Mask Generation Function (MGF)]].
    
- **Schema Probabilistico:** Il seed casuale assicura che la cifratura sia **probabilistica**, non deterministica, che è la prima linea di difesa contro gli attacchi.
    
- **Sicurezza CCA:** OAEP è progettato per prevenire attacchi sofisticati, come gli **Attacchi a Testo Cifrato Scelto (CCA)**, che hanno esposto le vulnerabilità del vecchio standard PKCS#1 v1.5 (ad esempio, l'attacco di Bleichenbacher).
    

### Comprendere i Livelli di Sicurezza (Attacchi "IND-")

OAEP è progettato per raggiungere il più alto livello pratico di sicurezza, IND-CCA2.

| **Notazione**    | **Nome Completo**                                                     | **Capacità dell'Attaccante**                                                                                                                               |
| ---------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[IND-CPA]]**  | Indistinguibilità sotto Attacco a Testo in Chiaro Scelto              | L'attaccante può chiedere la cifratura di qualsiasi messaggio scelga. (Questa è la "sicurezza semantica" fornita da OAEP).                                 |
| **[[IND-CCA1]]** | Indistinguibilità sotto Attacco a Testo Cifrato Scelto (non adattivo) | L'attaccante può decifrare testi cifrati _prima_ di ricevere il testo cifrato di sfida.                                                                    |
| **[[IND-CCA2]]** | Indistinguibilità sotto Attacco a Testo Cifrato Scelto Adattivo       | L'attaccante può decifrare _qualsiasi_ testo cifrato (prima _e dopo_ la sfida), _eccetto_ il testo cifrato di sfida stesso. Questo è il livello più forte. |
vedi [[Differenza tra IND-CPA, IND-CCA1 e IND-CCA2]]

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

- **Parametri:** (nota che sia il mittente che il destinatario sanno perfettamente $k_0$, $k_1$ e $n$)
    
    - $n$ = numero di bit nel modulo RSA (es. 2048)
        
    - $k0$ = lunghezza del seed casuale $r$
        
    - $k1$ = lunghezza del blocco di padding (es. un blocco di zeri).
        
    - $m$ = messaggio in chiaro
        
    - $G, H$ = funzioni hash crittografiche (es. 256 bit per [[SHA-256]], esse verranno usate per implementare le [[Mask Generation Function (MGF)]])
        
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

# RSAES-OAEP: Il Processo Completo

[[RSAES-OAEP]]  combina il padding [[RSA-OAEP]] con le primitive RSA.

- **Cifratura:**
    
    1. **Encode:** Dato il messaggio $M$, produrre il messaggio codificato $M'$ usando lo schema OAEP.
        
    2. **[[OS2IP]]:** Convertire l'octet-stream $M'$ in un intero $m$ ($m = \text{OS2IP}(M')$).
        
    3. **[[RSAEP]]:** Applicare la Primitiva di Cifratura RSA: $c = \text{RSAEP}((N, e), m)$, che è $c = m^e \pmod N$.
        
    4. **[[I2OSP]]:** Convertire l'intero $c$ nell'octet-stream finale del testo cifrato $C$ ($C = \text{I2OSP}(c, |N|)$).
        
- Decifratura:
    
    Questo è l'inverso simmetrico, che utilizza la Primitiva di Decifratura RSA ([[RSADP]]) e l'operazione di unpadding OAEP ($OAEP^{-1}$).
    

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

---

# RSA per Non-Ripudio e Firma Digitale

**Tags:** #ingegneria #crittografia #RSA #firma_digitale #non_ripudio #PSS

## 1. Introduzione al Non-Ripudio

Il concetto di **Non-Ripudio** è fondamentale nella sicurezza informatica. Si riferisce alla garanzia che un soggetto non possa negare di aver compiuto una determinata azione o inviato un messaggio.

Nello specifico:

- **Obiettivo:** Assicurare paternità verificabile di messaggi e azioni.
    
- **Mezzo:** La **[[Digital Signature|Firma Digitale]]**.
    

Nel contesto RSA, la firma si ottiene "invertendo" l'uso delle chiavi rispetto alla cifratura:

1. Si **cifra** (firma) usando la **Chiave Privata** del mittente.
    
2. Chiunque può **verificare** usando la **Chiave Pubblica** del mittente.
    

> [!example] Professor's Example
> 
> Pensate alla firma autografa su un contratto cartaceo: serve a dire "l'ho scritto io e accetto le conseguenze". La firma digitale RSA fa la stessa cosa matematicamente. Se cifro con la mia chiave privata, solo io potevo generare quel dato, quindi non posso dire "non sono stato io".

---

## 2. RSA Signature Scheme: PKCS#1 v1.5 (Legacy)

Questo è lo schema "classico", ancora molto diffuso (es. [[TLS]]1.2, email [[S-MIME|S/MIME]]), ma considerato **Legacy** per le nuove applicazioni.

### Il Paradigma "Hash-then-Sign"

Non firmiamo mai tutto il messaggio (sarebbe troppo lento). Firmiamo solo l'impronta (Hash).

1. **Preprocessing:** Calcolo dell'Hash del messaggio $M$.
    
2. **Encoding:** Formattazione secondo lo standard [[EMSA-PKCS1-v1_5]].
    
3. **Firma:** Cifratura RSA.
    

### Struttura dell'Encoding (EM)

Il blocco dati preparato per la firma ($EM$) ha una struttura fissa e **deterministica**:

**Struttura visuale del blocco:**

```
EM = 0x00 || 0x01 || PS || 0x00 || T
```

- **0x00**: Byte iniziale (per garantire che il numero sia minore del modulo).
    
- **0x01**: Tipo di blocco (indica "Firma").
    
- **PS**: Padding String (serie di byte `0xFF` per riempire lo spazio).
    
- **0x00**: Separatore.
    
- **T**: DigestInfo (contiene l'algoritmo Hash usato + l'Hash del messaggio).
    

### Matematica della Firma

Una volta costruito $EM$, la firma $S$ si calcola con la formula RSA standard:

$$S = EM^d \pmod n$$

Dove $d$ è l'esponente privato.

> [!abstract] Visual Analysis
> 
> ![[Pasted image 20251213184149.png]]
> 
> What to look at: Nota come l'hash $H$ viene incapsulato dentro la struttura $T$ e poi dentro $EM$.
> 
> Meaning: Non stiamo firmando il messaggio "grezzo", ma una struttura complessa che dice "Questo è l'hash SHA-256 di questo messaggio".
> 
> Da notare anche che il metodo completo è chiamato [[RSASSA]] = [[RSA]] + [[EMSA (Encoding Method for Signature with Appendix)|EMSA]]

---


## 3. Verifica della Firma (v1.5)

Il ricevente, per verificare che la firma sia autentica, esegue il processo inverso.

**Passaggi Logici:**

1. Calcola autonomamente l'Hash del messaggio ricevuto: $H' = \text{Hash}(M)$.
    
2. Costruisce il blocco atteso ($EM_{expected}$) usando lo stesso formato di encoding.
    
3. Decifra la firma digitale $S$ usando la chiave pubblica $e$:
    

$$EM' = S^e \pmod N$$

4. **Confronto:** Se $EM' == EM_{expected}$, la firma è valida.
    

> [!failure] Common Pitfall
> 
> Errore comune: Pensare che la verifica decifri il messaggio originale.
> 
> Realtà: La verifica decifra solo l'impronta (Hash) e la struttura di padding. Se il messaggio originale $M$ è stato modificato anche di un solo bit, l'hash calcolato dal ricevente non corrisponderà a quello contenuto nella firma decifrata.

---

## 4. Sicurezza di PKCS#1 v1.5 vs PSS

Perché stiamo abbandonando la v1.5?

- **Determinismo:** Lo schema v1.5 è deterministico. Firmare lo stesso messaggio produce sempre la stessa firma.
    
- **Vulnerabilità:** Se implementato male, è vulnerabile ad attacchi di tipo **Padding Oracle** (simili a Bleichenbacher).
    
- **Soluzione:** Passare a **[[RSASSA-PSS]]** (detto anche RSA-PSS).
    

---

## 5. RSA-PSS (Probabilistic Signature Scheme)

Introdotto in **PKCS#1 v2.1** (RFC 8017), è lo standard raccomandato oggi.

### Caratteristiche Chiave

- **Probabilistico:** Introduce un **Salt** casuale. Due firme dello stesso messaggio saranno diverse (ma entrambe valide).
    
- **Sicurezza:** Offre una sicurezza "provabile" basata sulla difficoltà del problema RSA.
    

### Costruzione PSS (Generazione)

Il processo è più complesso e usa una maschera ([[Mask Generation Function (MGF)]]1) simile a OAEP.

Fase 1: Hashing e Salting

Si calcola l'hash del messaggio $H$. Si genera un Salt casuale. Si calcola un nuovo hash intermedio $H'$:

$$H' = \text{Hash}(0x00 \dots 00 \ || \ H \ || \ \text{salt})$$

Fase 2: Costruzione Data Block (DB)

Si crea un blocco dati contenente il padding e il salt:

```
DB = PS || 0x01 || salt
```

_(Dove PS sono byte di zeri)_

Fase 3: Mascheramento (Masking)

Si usa la [[Mask Generation Function (MGF)]]1 (Mask Generation Function) per nascondere il DB:

$$maskedDB = DB \oplus \text{MGF1}(H', \text{len}(DB))$$

Fase 4: Encoding Finale (EM)

Il messaggio codificato finale è composto da:

```
EM = maskedDB || H' || 0xbc
```

_(Nota: `0xbc` è il byte finale fisso per PSS)_

**Fase 5: Firma**

$$S = EM^d \pmod N$$

> [!abstract] Visual Analysis
> 
> ![[Pasted image 20251213184800.png]]
> 
> What to look at: Osserva l'uso dello XOR ($\oplus$) tra il DB e l'output della MGF1.
> 
> Meaning: Questo meccanismo di mascheramento lega crittograficamente il salt e l'hash del messaggio, rendendo la struttura robusta.

---

## 6. Verifica RSA-PSS

La verifica in PSS è più rigorosa.

1. **Recupero:** Si ottiene $EM$ dalla firma usando la chiave pubblica: $EM = S^e \pmod N$.
    
2. **Splitting:** Si divide $EM$ per separare il $maskedDB$ dall'hash $H'$. Si controlla che l'ultimo byte sia `0xbc`.
    
3. **Unmasking:** Si rimuove la maschera per recuperare il $DB$ originale:
    

$$DB = maskedDB \oplus \text{MGF1}(H', \text{len}(DB))$$

4. **Parsing:** Dal $DB$ "pulito", si estrae il **Salt**.
    
5. **Verifica Finale:** Il ricevente ricalcola $H'_{new}$ usando il messaggio originale, l'hash originale e il salt appena estratto. Se $H'_{new}$ coincide con l'$H'$ trovato nella firma, tutto è corretto.
    

> [!tip] Exam Focus
> 
> Il professore potrebbe chiedere: "Qual è la differenza principale tra la firma v1.5 e PSS?"
> 
> Risposta sintetica:
> 
> 1. La **v1.5 è deterministica** (niente casualità), la **PSS è probabilistica** (usa un Salt).
>     
> 2. PSS usa una struttura a maschera (MGF) più sicura.
>     
> 3. PSS ha una prova di sicurezza formale più forte.
>


vedi anche [[7 CS  Lower Level - Asymmetric encryption#RSA – the algorithm]]. 



