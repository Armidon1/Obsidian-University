# L'Esponenziazione Modulare: Un'Analisi Dettagliata

### Introduzione

L'esponenziazione modulare è un'operazione fondamentale nell'aritmetica modulare, con profonde implicazioni in campi come la teoria dei numeri e, in particolare, la crittografia a chiave pubblica (ad esempio, negli algoritmi RSA e Diffie-Hellman).

Il problema consiste nel calcolare il resto della divisione di un numero elevato a una grande potenza per un altro numero. Formalmente, dati tre interi:

- Una **base** `B`
    
- Un **esponente** `E`
    
- Un **modulo** `M`
    

vogliamo calcolare il valore `C` tale che:

`C ≡ B^E (mod M)`

Questo significa che `C` è il resto della divisione di `B^E` per `M`. L'operazione `mod M` (abbreviazione di "modulo M") denota proprio tale resto.


---

### Sezione 1: Fondamenti - Aritmetica Modulare e Congruenza

Prima di affrontare l'esponenziazione, è imperativo comprendere i concetti di base dell'aritmetica modulare.

#### 1.1 La Relazione di Congruenza

Dati tre interi `a`, `b` e `M` (con `M > 0`), si dice che `a` è **congruente** a `b` modulo `M`, e si scrive:

`a ≡ b (mod M)`

se `M` divide la differenza `(a - b)`. Un modo equivalente, e spesso più intuitivo, per definire la congruenza è dire che `a` e `b` hanno **lo stesso resto** quando vengono divisi per `M`.

Esempio: 10 ≡ 1 (mod 3)

Questo è vero perché:

1. La differenza `(10 - 1) = 9`, e `9` è divisibile per `3`.
    
2. Oppure, `10` diviso `3` dà `3` con resto `1`. E `1` diviso `3` dà `0` con resto `1`. Entrambi hanno resto `1`.

Nota che:
- **Uguale (`=`):** Significa che due numeri sono **esattamente la stessa identica quantità**.
    
    - Esempio: `10 = 10`. `9 + 1` è uguale a `10`.
        
- **Congruente (`≡`):** Significa che due numeri (anche se diversi) **hanno lo stesso resto** quando vengono divisi per un certo numero (il modulo `M`).
    
    - Esempio: `10 ≡ 1 (mod 3)`.
        
    - Questo **non** significa che `10` è uguale a `1`.
        
    - Significa che `10` diviso `3` dà resto `1`, e anche `1` diviso `3` dà resto `1`. Appartengono alla stessa "classe di resto".
    
#### 1.2 Chiarimento: La Divisione Intera e il Resto

Qui sorge spesso la confusione che hai menzionato. Quando calcoliamo `a mod M`, non stiamo eseguendo una divisione in virgola mobile (come `1 / 3 = 0.333...`), ma stiamo applicando l'**[[Algoritmo di Divisione Euclidea]]**.

L'algoritmo afferma che per ogni coppia di interi `a` (dividendo) e `M` (divisore, con `M > 0`), esistono e sono unici due interi `q` (quoziente) e `r` (resto) tali che:

a = q * M + r

con la condizione fondamentale che 0 ≤ r < M.

Il valore `r` è il risultato di `a mod M`.

**Applicazione ai tuoi esempi:**

1. **Caso `10 mod 3`:**
    
    - Cerchiamo `q` e `r` tali che `10 = q * 3 + r` (con `0 ≤ r < 3`).
        
    - La soluzione è `10 = 3 * 3 + 1`.
        
    - Il quoziente `q` è 3, il resto `r` è **1**.
        
    - Quindi, `10 mod 3 = 1`.
        
2. **Caso `1 mod 3`:**
    
    - Cerchiamo `q` e `r` tali che `1 = q * 3 + r` (con `0 ≤ r < 3`).
        
    - La soluzione è `1 = 0 * 3 + 1`.
        
    - Il quoziente `q` è 0, il resto `r` è **1**.
        
    - Quindi, `1 mod 3 = 1`.
        

**Conclusione:** Entrambi `10` e `1` hanno resto 1 quando divisi per 3. Per questo motivo, appartengono alla stessa "classe di resto" modulo 3 e possiamo scrivere correttamente `10 ≡ 1 (mod 3)`.

---

### Sezione 2: Proprietà dell'Aritmetica Modulare

Il calcolo modulare non sarebbe utile se non obbedisse a regole algebriche precise. Le più importanti per i nostri scopi sono le proprietà della moltiplicazione:

`(a * b) mod M = [ (a mod M) * (b mod M) ] mod M`

Questa proprietà è la chiave di volta dell'esponenziazione modulare. Ci dice che, per calcolare il modulo di un prodotto, non è necessario calcolare prima l'intero prodotto. Possiamo calcolare il modulo dei singoli fattori, moltiplicarli e _poi_ calcolare il modulo del risultato.

Generalizzazione: 

Questo si estende a potenze. Per esempio, $B^2 \bmod M$:

$B^2 \bmod M = (B * B) \bmod M = [ (B \bmod M) * (B \bmod M) ] \bmod M$

E per $B^3 \bmod M$:

$B^3 \bmod M = (B^2 * B) \bmod M = [ (B^2 \bmod M) * (B \bmod M) ] \bmod M$

---

### Sezione 3: Il Problema Computazionale dell'Esponenziazione

Consideriamo il calcolo di `C ≡ B^E (mod M)`.

#### 3.1 Il Metodo Naive (Inattuabile)

L'approccio più ovvio è:

1. Calcolare `X = B^E`.
    
2. Calcolare `C = X mod M`.
    

Questo metodo fallisce quasi immediatamente per valori non triviali. Considera `50^100 mod 7`. Il numero `50^100` è un 1 seguito da circa 170 zeri. Nessun calcolatore moderno può memorizzare questo numero in modo esplicito.

#### 3.2 Il Metodo Iterativo (Buono, ma Lento)

Sfruttando la proprietà della Sezione 2, possiamo migliorare. Invece di calcolare l'intera potenza, applichiamo il modulo a ogni passo della moltiplicazione.

Possiamo definire $B^E$ come B moltiplicato per se stesso E volte.

B^E = B * B * B * ... * B (E volte)

L'algoritmo diventa:

1. Inizializza `Risultato = 1`.
    
2. Esegui un ciclo E volte:
    
    Risultato = (Risultato * B) mod M.
    
3. `Risultato` è la risposta.
    

Il punto chiave è che la variabile `Risultato` all'interno del ciclo **è già un valore ridotto modulo M** (o, più formalmente, appartiene alla classe di resto).

Analizziamo l'algoritmo passo dopo passo per calcolare, ad esempio, `B^3 mod M`.

1. **Inizio:** `Risultato = 1`.
    
2. **Ciclo 1 (per B¹):**
    
    - `Risultato = (Risultato * B) mod M = (1 * B) mod M = B mod M`
        
    - Ora `Risultato` **contiene `B mod M`**.
        
3. **Ciclo 2 (per B²):**
    
    - L'algoritmo esegue: `Risultato = (Risultato * B) mod M`.
        
    - Sostituiamo il valore di `Risultato` dal passo precedente: `Risultato = ( (B mod M) * B ) mod M`
        
    - Se ora applichiamo la _piena_ proprietà `(a*b) mod M = [(a mod M)*(b mod M)] mod M` a questa espressione, dove `a = (B mod M)` e `b = B`, otteniamo: `[ ( (B mod M) mod M) * (B mod M) ] mod M`
        
    - Ma `(B mod M) mod M` è semplicemente `B mod M`. Quindi l'espressione diventa: `[ (B mod M) * (B mod M) ] mod M`
        
    - Che è la definizione corretta di `B^2 mod M`.
        
4. **Ciclo 3 (per B³):**
    
    - L'algoritmo esegue: `Risultato = (Risultato * B) mod M`.
        
    - Il `Risultato` che stiamo usando ora contiene `B^2 mod M`.
        
    - Quindi stiamo calcolando: `( (B^2 mod M) * B ) mod M`.
        
    - Per la stessa logica di prima, questo è equivalente a `[ (B^2 mod M) * (B mod M) ] mod M`, che è la definizione corretta di `B^3 mod M`.

**Vantaggio:** In ogni passaggio, il `Risultato` non supera mai `M-1` e la moltiplicazione `(Risultato * B)` non supera `M * B`. I numeri rimangono gestibili.

**Svantaggio:** La complessità computazionale è **O(E)**. Se `E` è un numero molto grande (come un esponente crittografico a 2048 bit), questo algoritmo richiederebbe un numero di passaggi superiore al numero di atomi nell'universo.

---

### Sezione 4: Esponenziazione Rapida (Exponentiation by Squaring)

Questo è il metodo efficiente, quello a cui ti riferivi parlando di "scomporre per esponente di due". Risolve il problema della complessità O(E) riducendola a **O(log E)**, un miglioramento astronomico.

#### 4.1 Il Concetto Chiave: Scomposizione dell'Esponente

L'idea fondamentale è che **non** stai scomponendo la base `B`. Stai scomponendo l'**esponente `E`** nella sua rappresentazione binaria (somma di potenze di 2).

Ogni numero intero E può essere scritto in modo unico come somma di potenze di 2.

Esempio: E = 13

- In binario, `13` si scrive `1101₂` ([[Conversione Decimale, Binario, Esadecimale#Da Decimale a Binario|vedi qui]]) .
    
- Questo significa: `13 = (1 * 2³) + (1 * 2²) + (0 * 2¹) + (1 * 2⁰)`
    
- Ovvero: `13 = 8 + 4 + 1`
    

Ora, applichiamo questa scomposizione all'esponenziazione:

$B^{13} = B^{(8 + 4 + 1)}$

Per le proprietà delle potenze, questo equivale a:

$B^{13} = B^8 * B^4 * B^1$

#### 4.2 L'Efficienza dei "Quadrati Ripetuti"

Il metodo "by squaring" nota che non abbiamo bisogno di calcolare `B^8` facendo `B*B*B*B*B*B*B*B`.

Possiamo ottenere tutte le potenze di 2 (`B^1`, `B^2`, `B^4`, `B^8`, `B^16`, ...) in modo molto efficiente, "quadrando" ripetutamente il risultato precedente:

- `B^1 = B`
    
- `B^2 = B^1 * B^1`
    
- `B^4 = B^2 * B^2`
    
- `B^8 = B^4 * B^4`
    
- ...e così via.
    

Per calcolare `B^13`, ci servono solo `B^1`, `B^4` e `B^8`. Possiamo ottenerli in soli 3 passaggi di quadratura (per `B^2`, `B^4`, `B^8`).

Naturalmente, applichiamo il modulo `M` ad _ogni singolo passaggio_ per mantenere i numeri piccoli.

### 5.2 Analisi dell'Algoritmo (Implementazione "Right-to-Left")

L'algoritmo si basa sulla scomposizione binaria dell'esponente. Ricordiamo che `B^13 = B^8 * B^4 * B^1`. L'algoritmo calcola sistematicamente tutte le potenze di due di `B` (quadrando ripetutamente) e moltiplica nel risultato finale solo quelle necessarie.

Analizziamo lo pseudocodice (basato sul C fornito) per comprenderne l'eleganza.

**Pseudocodice:**
```C
Funzione fastModExp(base, esponente, modulo):
  1. risultato = 1
  2. base = base % modulo  // Pre-riduzione della base
  
  3. while (esponente > 0):
  4.   // Controlla l'ultimo bit (il bit meno significativo)
  5.   if (esponente è dispari): // (esponente & 1)
  6.     risultato = (risultato * base) % modulo
  
  7.   // Quadrato della base per il prossimo ciclo
  8.   base = (base * base) % modulo
  
  9.   // Sposta i bit dell'esponente a destra
  10.  esponente = esponente >> 1 // (divisione intera per 2)
  
  11. return risultato
```

### 5.3 Spiegazione Dettagliata dei Passaggi

L'algoritmo itera sui bit dell'esponente `E`, da destra a sinistra (dal bit 0 in su).

1. **Variabile `risultato` (riga 1, 6):** Questa è l'accumulatore. Inizia da 1 (l'identità moltiplicativa) e accumula il prodotto delle potenze di `B` necessarie.
    
2. **Variabile `base` (riga 2, 8):** Questa variabile è la più critica. Non memorizza la `B` originale. Ad ogni ciclo, viene **sempre quadrata** (riga 8).
    
    - Al ciclo 0, contiene `B^1 (mod M)`.
        
    - Al ciclo 1, contiene `B^2 (mod M)`.
        
    - Al ciclo 2, contiene `B^4 (mod M)`.
        
    - Al ciclo `k`, contiene `B^(2^k) (mod M)`.
        
3. **Variabile `esponente` (riga 3, 10):** Agisce come un "cursore" sui bit.
    
    - **`while (esponente > 0)`:** Il ciclo continua finché ci sono bit da leggere.
        
    - **`esponente >> 1` (Right Shift):** Questa è una divisione intera per 2. In termini binari, "scarta" il bit più a destra e sposta tutti gli altri bit di una posizione a destra. Questo permette di esaminare un nuovo bit a ogni ciclo.
        
4. **Il Controllo `if (esponente è dispari)` (riga 5):**
    
    - Questo è il cuore della logica. Controllare se `esponente` è dispari equivale a controllare se il suo bit più a destra (bit 0) è un `1`.
        
    - **Se il bit è 1:** Significa che la potenza di `B` corrispondente a questo ciclo (memorizzata in `base`) è _necessaria_ per il calcolo finale. Viene quindi moltiplicata nel `risultato` (riga 6).
        
    - **Se il bit è 0:** La potenza corrente non serve, e il `risultato` non viene toccato.
        

### 5.4 Esempio (Trace)

Calcoliamo **`3^13 (mod 7)`** usando questo algoritmo.

- `base` iniziale = 3, `esponente` iniziale = 13, `risultato` iniziale = 1
    
- `E = 13` in binario è `1101₂`
    

|**Ciclo while**|**esponente (Valore)**|**esponente (Binario)**|**if (esponente & 1)?**|**risultato**|**base (Potenza)**|
|---|---|---|---|---|---|
|Inizio|13|`110**1**`|-|1|3 (corrisponde a 3¹)|
|1|13|`110**1**`|**Sì (1)**|`(1 * 3) % 7 = 3`|`(3 * 3) % 7 = 2`|
|2|6|`11**0**`|No (0)|3|`(2 * 2) % 7 = 4`|
|3|3|`1**1**`|**Sì (1)**|`(3 * 4) % 7 = 5`|`(4 * 4) % 7 = 2`|
|4|1|`**1**`|**Sì (1)**|`(5 * 2) % 7 = 3`|`(2 * 2) % 7 = 4`|
|5|0|``|Fine (0 > 0 è Falso)|||

**Risultato Finale:** `3`

Questo algoritmo ha eseguito 4 cicli (il numero di bit di 13) e non ha mai gestito numeri più grandi di `(5*2)` o `(4*4)`.

---


---

### Sezione 5: Riepilogo

1. **Congruenza Modulare:** `a ≡ b (mod M)` significa che `a` e `b` hanno lo stesso resto quando divisi per `M`.
    
2. **Perché `1 mod 3 = 1`:** Per l'algoritmo di divisione, `1 = (0 * 3) + 1`. Il resto è 1.
    
3. **Proprietà Chiave:** Il modulo di un prodotto è il prodotto dei moduli: `(a*b) mod M = [(a mod M)*(b mod M)] mod M`.
    
4. **Esponenziazione Rapida:** Sfrutta la **rappresentazione binaria dell'esponente `E`** per ridurre il numero di moltiplicazioni da `E` (lineare) a `log₂(E)` (logaritmico).
    
5. **Come Funziona:** Calcola solo le potenze di `B` che sono potenze di 2 (es. `B^1, B^2, B^4, B^8...`) applicando il modulo a ogni quadratura. Poi, moltiplica tra loro solo le potenze che corrispondono ai bit "1" dell'esponente `E`.

## Elenco Proprietà Fondamentali dell'Aritmetica Modulare

L'aritmetica modulare, definita dalla relazione di congruenza, non sarebbe utile se non obbedisse a un insieme coerente di regole. Queste proprietà ci permettono di trattare le congruenze in modo algebricamente simile alle equazioni standard.

### Sezione 1: Proprietà Fondamentali (Relazione di Equivalenza)

La relazione di congruenza $a \equiv b \pmod M$ è una **relazione di equivalenza**, il che significa che possiede le seguenti tre proprietà:

1. Proprietà Riflessiva: Per ogni intero $a$:
    
    $$a \equiv a \pmod M$$
    
2. Proprietà Simmetrica: Se $a \equiv b \pmod M$, allora:
    
    $$b \equiv a \pmod M$$
    
3. Proprietà Transitiva: Se $a \equiv b \pmod M$ e $b \equiv c \pmod M$, allora:
    
    $$a \equiv c \pmod M$$
    

### Sezione 2: Compatibilità con le Operazioni Algebriche

La potenza della congruenza risiede nel fatto che è **compatibile con le operazioni aritmetiche** di addizione, sottrazione e moltiplicazione.

Se abbiamo due congruenze:

$a \equiv b \pmod M$

$c \equiv d \pmod M$

Allora valgono le seguenti proprietà:

1. Compatibilità con l'Addizione:
    
    $$a + c \equiv b + d \pmod M$$
    
    (In breve: puoi sommare le congruenze).
    
2. Compatibilità con la Sottrazione:
    
    $$a - c \equiv b - d \pmod M$$
    
    (Puoi sottrarre le congruenze).
    
3. Compatibilità con la Moltiplicazione:
    
    $$a \times c \equiv b \times d \pmod M$$
    
    (Puoi moltiplicare le congruenze).
    

### Sezione 3: Regola di Sostituzione e Potenze

Questa sezione generalizza le proprietà della Sezione 2 ed è quella che hai appena utilizzato.

1. **Moltiplicazione per una Costante:** Un corollario diretto della proprietà di moltiplicazione è che puoi moltiplicare entrambi i lati di una congruenza per lo stesso intero $k$:
    
    > Se $a \equiv b \pmod M$, allora $a \cdot k \equiv b \cdot k \pmod M$
    
2. **Esponenziazione (o Congruenza di Potenze):** Questa è la proprietà che hai invocato. Applicando ripetutamente la proprietà di moltiplicazione (Sezione 2.3) a se stessa, si ottiene:
    
    > Se $a \equiv b \pmod M$, allora per ogni intero $k \ge 1$:
    > 
    > $$a^k \equiv b^k \pmod M$$
    
    È esattamente per questo che, avendo stabilito $2^7 \equiv 1 \pmod{127}$, possiamo _immediatamente_ concludere che $(2^7)^{10} \equiv (1)^{10} \pmod{127}$.
    
3. **Principio di Sostituzione Generale (Funzioni Polinomiali):** La regola si estende a qualsiasi polinomio $P(x)$ con coefficienti interi.
    
    > Se $a \equiv b \pmod M$, allora $P(a) \equiv P(b) \pmod M$
    

### Sezione 4: Proprietà Avanzate (Cancellazione e Teoremi)

1. Legge di Cancellazione (Attenzione alla Divisione):
    
    Nell'algebra standard, se $a \cdot c = b \cdot c$ (con $c \neq 0$), si può "cancellare" $c$. Nell'aritmetica modulare, questo è falso in generale.
    
    - Esempio errato: $10 \equiv 4 \pmod 6$ (entrambi sono $\equiv 4$).
        
        $5 \cdot 2 \equiv 2 \cdot 2 \pmod 6$.
        
        Se cancellassimo il 2, otterremmo $5 \equiv 2 \pmod 6$, che è falso.
        
    
    La **legge di cancellazione corretta** richiede una condizione aggiuntiva:
    
    > Se $a \cdot c \equiv b \cdot c \pmod M$ e $\text{MCD}(c, M) = 1$ (cioè $c$ e $M$ sono coprimi),
    > 
    > allora si può cancellare $c$ e $a \equiv b \pmod M$.
    
2. **Teoremi di Riduzione dell'Esponente:** Come visto nell'esercizio, questi teoremi ci permettono di semplificare gli esponenti.
    
    - Piccolo Teorema di Fermat: Se $p$ è un numero primo e $p$ non divide $a$:
        
        $$a^{p-1} \equiv 1 \pmod p$$
        
    - Teorema di Eulero (Generalizzazione): Se $\text{MCD}(a, M) = 1$:
        
        $$a^{\phi(M)} \equiv 1 \pmod M$$
        
3. Proprietà di Riduzione dell'Esponente (Il "Perché" dell'Esercizio):
    
    Una conseguenza diretta dei teoremi di Fermat ed Eulero è la regola computazionale più importante per l'esponenziazione:
    
    > Se $\text{MCD}(a, M) = 1$, allora per qualsiasi esponente $E$:
    > 
    > $$a^E \equiv a^{E \pmod{\phi(M)}} \pmod M$$
    
    Questo è il motivo per cui, per calcolare $2^{200} \pmod{127}$, abbiamo ridotto l'esponente $200$ modulo $\phi(127) = 126$, ottenendo $2^{74}$.

# Eserciziario di Aritmetica Modulare ed Esponenziazione

Si prega lo studente di tentare una soluzione autonoma prima di consultare la sezione delle soluzioni.

### Sezione 1: Calcolo Modulare di Base

Questa sezione è volta a consolidare la comprensione della definizione di congruenza e dell'operatore modulo.

- **Esercizio 1.1:** Calcolare `15 mod 4`
    
- **Esercizio 1.2:** Calcolare `7 mod 10`
    
- **Esercizio 1.3:** Calcolare `-8 mod 5`
    

---

### Sezione 2: Proprietà della Moltiplicazione Modulare

Questi esercizi verificano la capacità di applicare la proprietà fondamentale:

(a * b) mod M = [ (a mod M) * (b mod M) ] mod M

- **Esercizio 2.1:** Calcolare `(12 * 9) mod 7` in due modi:
    
    1. Calcolando prima il prodotto `12 * 9`.
        
    2. Applicando la proprietà della moltiplicazione modulare.
        
- **Esercizio 2.2:** Calcolare `(50 * 30 * 10) mod 9`
    

---

### Sezione 3: Esponenziazione Iterativa (Metodo Lento)

Questo esercizio serve come ponte verso l'algoritmo di esponenziazione rapida, applicando la proprietà della moltiplicazione in modo iterativo.

- **Esercizio 3.1:** Calcolare `4^4 mod 5` mostrando ogni passaggio moltiplicativo.
    

---

### Sezione 4: Esponenziazione Rapida (Exponentiation by Squaring)

Questa sezione implementa l'algoritmo efficiente `O(log E)`. Si richiede di calcolare `B^E mod M` scomponendo l'esponente `E` nella sua forma binaria.

- **Esercizio 4.1:** Calcolare `5^11 mod 13`
    
- **Esercizio 4.2:** Calcolare `7^20 mod 21`
    
- **Esercizio 4.3:** Calcolare `123^32 mod 100`
    

---

---

## Soluzioni Svolte

### Sezione 1: Soluzioni (Calcolo Modulare di Base)

**Soluzione 1.1: `15 mod 4`**

- **Definizione:** Cerchiamo il resto `r` della divisione `15 = q * 4 + r`, con `0 ≤ r < 4`.
    
- **Svolgimento:** `15 = 3 * 4 + 3`.
    
- **Risultato:** Il resto `r` è 3.
    
    > `15 mod 4 = 3`
    

**Soluzione 1.2: `7 mod 10`**

- **Definizione:** Cerchiamo il resto `r` della divisione `7 = q * 10 + r`, con `0 ≤ r < 10`.
    
- **Svolgimento:** Questo è il caso in cui il dividendo è minore del divisore. L'unica soluzione è `7 = 0 * 10 + 7`.
    
- **Risultato:** Il quoziente `q` è 0 e il resto `r` è 7.
    
    > `7 mod 10 = 7`
    

**Soluzione 1.3: `-8 mod 5`**

- **Definizione:** Cerchiamo il resto `r` della divisione `-8 = q * 5 + r`, con `0 ≤ r < 5`.
    
- **Svolgimento:** Non possiamo usare `q = -1`, perché `-8 = -1 * 5 - 3`, che dà un resto negativo `-3`. Dobbiamo scegliere un quoziente `q` che produca un resto `r` nell'intervallo `[0, 4]`.
    
- Scegliamo `q = -2`.
    
- `-8 = (-2) * 5 + 2`.
    
- `r = 2` soddisfa la condizione `0 ≤ 2 < 5`.
    
- **Metodo Alternativo:** Si aggiunge il modulo al numero negativo finché non si ottiene il primo risultato positivo: `-8 + 5 = -3`. `-3 + 5 = 2`.
    
- **Risultato:**
    
    > `-8 mod 5 = 2`
    

---

### Sezione 2: Soluzioni (Proprietà della Moltiplicazione Modulare)

**Soluzione 2.1: `(12 * 9) mod 7`**

1. **Metodo Diretto:**
    
    - `12 * 9 = 108`
        
    - `108 mod 7`. Si calcola `108 = 15 * 7 + 3`.
        
    - Risultato: `3`.
        
2. **Metodo Modulare (Proprietà):**
    
    - `12 mod 7 = 5`
        
    - `9 mod 7 = 2`
        
    - `[ (12 mod 7) * (9 mod 7) ] mod 7 = (5 * 2) mod 7`
        
    - `10 mod 7 = 3`
        

- **Risultato:** Entrambi i metodi producono `3`.
    
    > `(12 * 9) mod 7 = 3`
    

**Soluzione 2.2: `(50 * 30 * 10) mod 9`**

- **Svolgimento:** Applichiamo il modulo a ogni fattore prima di moltiplicare.
    
    - `50 mod 9 = 5` (poiché `50 = 5 * 9 + 5`)
        
    - `30 mod 9 = 3` (poiché `30 = 3 * 9 + 3`)
        
    - `10 mod 9 = 1` (poiché `10 = 1 * 9 + 1`)
        
- Sostituiamo i resti nell'espressione originale:
    
    - `(5 * 3 * 1) mod 9 = 15 mod 9`
        
- Calcoliamo il risultato finale:
    
    - `15 mod 9 = 6`
        
- **Risultato:**
    
    > `(50 * 30 * 10) mod 9 = 6`
    

---

### Sezione 3: Soluzioni (Esponenziazione Iterativa)

**Soluzione 3.1: `4^4 mod 5`**

- **Svolgimento:** Calcoliamo la potenza passo dopo passo, applicando il modulo a ogni risultato intermedio.
    
    - `4^1 mod 5 = 4`
        
    - `4^2 mod 5 = (4^1 * 4) mod 5 = (4 * 4) mod 5 = 16 mod 5 = 1`
        
    - `4^3 mod 5 = (4^2 * 4) mod 5 = (1 * 4) mod 5 = 4`
        
    - `4^4 mod 5 = (4^3 * 4) mod 5 = (4 * 4) mod 5 = 16 mod 5 = 1`
        
- **Nota Aggiuntiva:** Si poteva osservare che `4 ≡ -1 (mod 5)`. Sostituendo, `4^4 mod 5 ≡ (-1)^4 mod 5 ≡ 1 mod 5`.
    
- **Risultato:**
    
    > `4^4 mod 5 = 1`
    

---

### Sezione 4: Soluzioni (Esponenziazione Rapida)

**Soluzione 4.1: `5^11 mod 13`**

- **Analisi:** Base `B = 5`, Esponente `E = 11`, Modulo `M = 13`.
    
- **Passo 1: Scomposizione Esponente**
    
    - L'esponente `11` in binario è `1011₂`.
        
    - `11 = 8 + 2 + 1`.
        
    - Quindi, `5^11 = 5^8 * 5^2 * 5^1`.
        
- **Passo 2: Algoritmo (Right-to-Left)**
    
    - Inizializziamo `Risultato = 1` e `Potenza = B mod M = 5`.
        
    - Iteriamo sui bit di `1011₂` da destra a sinistra.
        

|**Bit (da E)**|**Valore Bit**|**Azione su Risultato (se Bit=1)**|**Calcolo Potenza (per prox ciclo)**|**Risultato**|**Potenza**|
|---|---|---|---|---|---|
|(iniz.)|-|-|-|1|5|
|Bit 0|**1**|`Ris = (1 * 5) mod 13 = 5`|`Pot = (5 * 5) mod 13 = 25 mod 13 = 12`|5|12|
|Bit 1|**1**|`Ris = (5 * 12) mod 13 = 60 mod 13 = 8`|`Pot = (12 * 12) mod 13 = 144 mod 13 = 1`|8|1|
|Bit 2|**0**|_Nessuna azione_|`Pot = (1 * 1) mod 13 = 1`|8|1|
|Bit 3|**1**|`Ris = (8 * 1) mod 13 = 8`|`Pot = (1 * 1) mod 13 = 1` (non serve)|8|1|

- **Risultato:**
    
    > `5^11 mod 13 = 8`
    

**Soluzione 4.2: `7^20 mod 21`**

- **Analisi:** Base `B = 7`, Esponente `E = 20`, Modulo `M = 21`.
    
- **Passo 1: Scomposizione Esponente**
    
    - L'esponente `20` in binario è `10100₂`.
        
    - `20 = 16 + 4`.
        
    - Quindi, `7^20 = 7^16 * 7^4`.
        
- **Passo 2: Algoritmo (Right-to-Left)**
    
    - Inizializziamo `Risultato = 1` e `Potenza = B mod M = 7`.
        

|**Bit (da E)**|**Valore Bit**|**Azione su Risultato (se Bit=1)**|**Calcolo Potenza (per prox ciclo)**|**Risultato**|**Potenza**|
|---|---|---|---|---|---|
|(iniz.)|-|-|-|1|7|
|Bit 0|**0**|_Nessuna azione_|`Pot = (7 * 7) mod 21 = 49 mod 21 = 7`|1|7|
|Bit 1|**0**|_Nessuna azione_|`Pot = (7 * 7) mod 21 = 49 mod 21 = 7`|1|7|
|Bit 2|**1**|`Ris = (1 * 7) mod 21 = 7`|`Pot = (7 * 7) mod 21 = 49 mod 21 = 7`|7|7|
|Bit 3|**0**|_Nessuna azione_|`Pot = (7 * 7) mod 21 = 49 mod 21 = 7`|7|7|
|Bit 4|**1**|`Ris = (7 * 7) mod 21 = 49 mod 21 = 7`|`Pot = (7*7) mod 21 = 7` (non serve)|7|7|

- **Nota:** Si osserva che `7^2 = 49 \equiv 7 (mod 21)`. Di conseguenza, `7^n \equiv 7 (mod 21)` per ogni `n ≥ 2`. L'algoritmo lo conferma.
    
- **Risultato:**
    
    > `7^20 mod 21 = 7`
    

**Soluzione 4.3: `123^32 mod 100`**

- **Analisi:** Base `B = 123`, Esponente `E = 32`, Modulo `M = 100`.
    
- **Passo 0: Semplificazione Base**
    
    - Prima di iniziare, semplifichiamo la base: `123 mod 100 = 23`.
        
    - Il problema è equivalente a calcolare `23^32 mod 100`.
        
- **Passo 1: Scomposizione Esponente**
    
    - L'esponente `32` in binario è `100000₂`.
        
    - Questo è un caso speciale: l'esponente è una pura potenza di 2.
        
    - `32 = 32`.
        
    - `23^32 = 23^(2^5)`.
        
- **Passo 2: Algoritmo (Right-to-Left)**
    
    - Inizializziamo `Risultato = 1` e `Potenza = B' mod M = 23`.
        
    - L'algoritmo consiste nel calcolare i quadrati successivi. Il `Risultato` verrà moltiplicato solo una volta, all'ultimo bit.
        

|**Bit (da E)**|**Valore Bit**|**Azione su Risultato**|**Calcolo Potenza (Quadrati successivi)**|**Risultato**|**Potenza**|
|---|---|---|---|---|---|
|(iniz.)|-|-|-|1|23|
|Bit 0|**0**|_N/A_|`Pot = (23 * 23) mod 100 = 529 mod 100 = 29` (è 23²)|1|29|
|Bit 1|**0**|_N/A_|`Pot = (29 * 29) mod 100 = 841 mod 100 = 41` (è 23⁴)|1|41|
|Bit 2|**0**|_N/A_|`Pot = (41 * 41) mod 100 = 1681 mod 100 = 81` (è 23⁸)|1|81|
|Bit 3|**0**|_N/A_|`Pot = (81 * 81) mod 100 = 6561 mod 100 = 61` (è 23¹⁶)|1|61|
|Bit 4|**0**|_N/A_|`Pot = (61 * 61) mod 100 = 3721 mod 100 = 21` (è 23³²)|1|21|
|Bit 5|**1**|`Ris = (1 * 21) mod 100 = 21`|`Pot = (21 * 21) mod 100 = 441 mod 100 = 41`|**21**|41|

- **Risultato:** Il valore finale del `Risultato` è 21.
    
    > `123^32 mod 100 = 21`
    



---

## Sezione 6: Esercizi sull'Algoritmo Binario

Si richiede di risolvere i seguenti problemi utilizzando il metodo di esponenziazione rapida (binario). Si consiglia di produrre una tabella di _trace_ (come quella nell'Esempio 5.4) per mostrare l'evoluzione delle variabili `risultato`, `base` ed `esponente`.

### Esercizi Proposti

- **Esercizio 6.1:** Calcolare `3^10 mod 11`
    
- **Esercizio 6.2:** Calcolare `15^9 mod 17`
    
- **Esercizio 6.3:** Calcolare `7^16 mod 13` (Nota: questo è un caso particolare interessante)
    

---

---

## Soluzioni Svolte (Esercizi Sezione 6)

### Soluzione 6.1: `3^10 mod 11`

- `base` iniziale = 3, `esponente` iniziale = 10, `risultato` iniziale = 1
    
- `E = 10` in binario è `1010₂`
    

|**Ciclo while**|**esponente**|**esponente (Binario)**|**if (dispari)?**|**risultato**|**base**|
|---|---|---|---|---|---|
|Inizio|10|`101**0**`|-|1|3|
|1|10|`101**0**`|No (0)|1|`(3 * 3) % 11 = 9`|
|2|5|`10**1**`|**Sì (1)**|`(1 * 9) % 11 = 9`|`(9 * 9) % 11 = 81 % 11 = 4`|
|3|2|`1**0**`|No (0)|9|`(4 * 4) % 11 = 16 % 11 = 5`|
|4|1|`**1**`|**Sì (1)**|`(9 * 5) % 11 = 45 % 11 = 1`|`(5 * 5) % 11 = 25 % 11 = 3`|
|5|0|``|Fine|||

**Risultato Finale:** `1`

---

### Soluzione 6.2: `15^9 mod 17`

- Passo 0 (Semplificazione): 15 mod 17.
    
    Possiamo notare che 15 ≡ -2 (mod 17). Calcolare (-2)^9 mod 17 è più facile.
    
    - `(-2)^9` è negativo. `(-2)^9 = -512`.
        
    - Calcoliamo `-512 mod 17`.
        
    - `-512 = (-31) * 17 + 15`. (Oppure: `512 = 30 * 17 + 2`, quindi `512 mod 17 = 2`. Poiché `(-512) mod 17` è `(-2) mod 17`, il risultato è `17-2 = 15`).
        
- **Applichiamo l'algoritmo standard (con `B=15`):**
    
- `base` iniziale = 15, `esponente` iniziale = 9, `risultato` iniziale = 1
    
- `E = 9` in binario è `1001₂`
    

|**Ciclo while**|**esponente**|**esponente (Binario)**|**if (dispari)?**|**risultato**|**base**|
|---|---|---|---|---|---|
|Inizio|9|`100**1**`|-|1|15|
|1|9|`100**1**`|**Sì (1)**|`(1 * 15) % 17 = 15`|`(15 * 15) % 17 = 225 % 17 = 4`|
|2|4|`10**0**`|No (0)|15|`(4 * 4) % 17 = 16 % 17 = 16`|
|3|2|`1**0**`|No (0)|15|`(16 * 16) % 17 = (-1 * -1) % 17 = 1`|
|4|1|`**1**`|**Sì (1)**|`(15 * 1) % 17 = 15`|`(1 * 1) % 17 = 1`|
|5|0|``|Fine|||

**Risultato Finale:** `15`

---

### Soluzione 6.3: `7^16 mod 13`

- `base` iniziale = 7, `esponente` iniziale = 16, `risultato` iniziale = 1
    
- `E = 16` in binario è `10000₂`
    

|**Ciclo while**|**esponente**|**esponente (Binario)**|**if (dispari)?**|**risultato**|**base**|
|---|---|---|---|---|---|
|Inizio|16|`1000**0**`|-|1|7|
|1|16|`1000**0**`|No (0)|1|`(7 * 7) % 13 = 49 % 13 = 10`|
|2|8|`100**0**`|No (0)|1|`(10 * 10) % 13 = 100 % 13 = 9`|
|3|4|`10**0**`|No (0)|1|`(9 * 9) % 13 = 81 % 13 = 3`|
|4|2|`1**0**`|No (0)|1|`(3 * 3) % 13 = 9`|
|5|1|`**1**`|**Sì (1)**|`(1 * 9) % 13 = 9`|`(9 * 9) % 13 = 3`|
|6|0|``|Fine|||

Risultato Finale: 9

(Nota: L'algoritmo ha calcolato 7^1, 7^2, 7^4, 7^8, 7^16 e ha moltiplicato risultato (che era 1) solo per 7^16 (mod 13)).

---
## Esercizi di Esponenziazione Modulare con Fermat ed Eulero

Si risolvano le seguenti congruenze utilizzando, ove appropriato, il Piccolo Teorema di Fermat o il Teorema di Eulero per ridurre l'esponente, e le proprietà di congruenza per semplificare il calcolo.

### Esercizi Proposti

1. **Esercizio 1 (Fermat):** Calcolare $3^{100} \pmod{13}$
    
2. **Esercizio 2 (Fermat e Cicli Brevi):** Calcolare $7^{1002} \pmod{19}$
    
3. **Esercizio 3 (Eulero - Semplice):** Calcolare $3^{80} \pmod{20}$
    
4. **Esercizio 4 (Eulero - Complesso):** Calcolare $11^{123} \pmod{30}$
    

---

## Soluzioni Svolte

### Soluzione 1: $3^{100} \pmod{13}$

1. **Analisi:**
    
    - Base $a = 3$, Esponente $E = 100$, Modulo $M = 13$.
        
    - Il modulo 13 è un **numero primo**.
        
    - Controlliamo la coprimalità: $\text{MCD}(3, 13) = 1$.
        
    - Possiamo applicare il **Piccolo Teorema di Fermat**.
        
2. **Applicazione di Fermat:**
    
    - Il teorema afferma $a^{p-1} \equiv 1 \pmod p$.
        
    - $p-1 = 13 - 1 = 12$.
        
    - Quindi, $3^{12} \equiv 1 \pmod{13}$.
        
3. **Riduzione Esponente:**
    
    - Riduciamo l'esponente $E=100$ modulo $\phi(13)=12$.
        
    - Usiamo la divisione euclidea: $100 = q \cdot 12 + r$.
        
    - $100 = 8 \times 12 + 4$. (Poiché $8 \times 12 = 96$).
        
    - L'esponente $100$ è congruente a $4 \pmod{12}$.
        
4. **Calcolo:**
    
    - $3^{100} = 3^{(12 \times 8 + 4)} = (3^{12})^8 \times 3^4$
        
    - Applichiamo il modulo:
        
        $$\equiv (1)^8 \times 3^4 \pmod{13}$$
        
        $$\equiv 3^4 \pmod{13}$$
        
    - Ora calcoliamo $3^4$:
        
        $3^4 = 81$
        
    - Calcoliamo $81 \pmod{13}$:
        
        $81 = 6 \times 13 + 3$. (Poiché $6 \times 13 = 78$).
        
    - $81 \equiv 3 \pmod{13}$.
        

**Risultato:** $3^{100} \pmod{13} = 3$.

---

### Soluzione 2: $7^{1002} \pmod{19}$

1. **Analisi:**
    
    - Base $a = 7$, Esponente $E = 1002$, Modulo $M = 19$.
        
    - Il modulo 19 è un **numero primo**.
        
    - $\text{MCD}(7, 19) = 1$. Applichiamo Fermat.
        
2. **Applicazione di Fermat:**
    
    - $p-1 = 19 - 1 = 18$.
        
    - Quindi, $7^{18} \equiv 1 \pmod{19}$.
        
3. **Riduzione Esponente:**
    
    - Riduciamo $E=1002$ modulo $\phi(19)=18$.
        
    - $1002 \div 18$. Facciamo $18 \times 50 = 900$. Restano 102. $18 \times 5 = 90$. Restano 12.
        
    - $1002 = 18 \times 55 + 12$.
        
    - L'esponente $1002$ è congruente a $12 \pmod{18}$.
        
4. **Calcolo:**
    
    - $7^{1002} \equiv 7^{12} \pmod{19}$.
        
    - Ora dobbiamo calcolare $7^{12}$. Usiamo l'esponenziazione rapida (quadrati):
        
        - $7^1 \equiv 7$
            
        - $7^2 \equiv 49 \equiv 11 \pmod{19}$ (perché $49 = 2 \times 19 + 11$)
            
        - $7^4 \equiv (7^2)^2 \equiv 11^2 \equiv 121 \pmod{19}$.
            
            - $121 = 6 \times 19 + 7$. (perché $6 \times 19 = 114$).
                
            - $7^4 \equiv 7 \pmod{19}$.
                
        - $7^8 \equiv (7^4)^2 \equiv 7^2 \equiv 11 \pmod{19}$.
            
    - L'esponente 12 è $8 + 4$.
        
        $7^{12} = 7^8 \times 7^4$
        
        $$\equiv 11 \times 7 \pmod{19}$$
        
        $$\equiv 77 \pmod{19}$$
        
    - Calcoliamo $77 \pmod{19}$:
        
        $77 = 4 \times 19 + 1$. (Poiché $4 \times 19 = 76$).
        
    - $77 \equiv 1 \pmod{19}$.
        

**Risultato:** $7^{1002} \pmod{19} = 1$.

- Metodo Alternativo (Astuto): Se calcolando le potenze notiamo $7^2 \equiv 11$ e $7^3 \equiv 7 \times 11 \equiv 77 \equiv 1$. Abbiamo trovato un ciclo breve! $7^3 \equiv 1$.
    
    L'esponente è $1002$. $1002$ è divisibile per 3 (somma delle cifre 1+2=3).
    
    $1002 = 3 \times 334$.
    
    $7^{1002} = (7^3)^{334} \equiv (1)^{334} \equiv 1$.
    

---

### Soluzione 3: $3^{80} \pmod{20}$

1. **Analisi:**
    
    - Base $a = 3$, Esponente $E = 80$, Modulo $M = 20$.
        
    - Il modulo 20 **non** è primo. Non possiamo usare Fermat.
        
    - Controlliamo la coprimalità: $\text{MCD}(3, 20) = 1$. (3 è primo, 20 non è div. per 3).
        
    - Possiamo applicare il **Teorema di Eulero**.
        
2. **Applicazione di Eulero:**
    
    - Dobbiamo calcolare $\phi(20)$.
        
    - Fattorizzazione di 20: $20 = 2^2 \times 5$.
        
    - $\phi(20) = \phi(2^2) \times \phi(5)$
        
    - $\phi(p^k) = p^k - p^{k-1}$. $\phi(2^2) = 2^2 - 2^1 = 4 - 2 = 2$.
        
    - $\phi(p) = p-1$. $\phi(5) = 4$.
        
    - $\phi(20) = 2 \times 4 = 8$.
        
    - Il teorema afferma $a^{\phi(M)} \equiv 1 \pmod M$, quindi $3^8 \equiv 1 \pmod{20}$.
        
3. **Riduzione Esponente:**
    
    - Riduciamo $E=80$ modulo $\phi(20)=8$.
        
    - $80 \div 8 = 10$ con resto $0$.
        
    - L'esponente $80$ è congruente a $0 \pmod 8$.
        
4. **Calcolo:**
    
    - $3^{80} = 3^{(8 \times 10)} = (3^8)^{10}$
        
    - Applichiamo il modulo:
        
        $$\equiv (1)^{10} \pmod{20}$$
        
        $$\equiv 1 \pmod{20}$$
        
    - (Nota: un esponente $0$ implica il risultato $1$, poiché $a^0=1$).
        

**Risultato:** $3^{80} \pmod{20} = 1$.

---

### Soluzione 4: $11^{123} \pmod{30}$

1. **Analisi:**
    
    - Base $a = 11$, Esponente $E = 123$, Modulo $M = 30$.
        
    - Modulo 30 non è primo.
        
    - Controlliamo la coprimalità: $\text{MCD}(11, 30) = 1$.
        
    - Possiamo applicare il **Teorema di Eulero**.
        
2. **Applicazione di Eulero:**
    
    - Calcoliamo $\phi(30)$.
        
    - $30 = 2 \times 3 \times 5$.
        
    - $\phi(30) = \phi(2) \times \phi(3) \times \phi(5)$
        
    - $\phi(30) = (2-1) \times (3-1) \times (5-1) = 1 \times 2 \times 4 = 8$.
        
    - Il teorema afferma $11^8 \equiv 1 \pmod{30}$.
        
3. **Riduzione Esponente:**
    
    - Riduciamo $E=123$ modulo $\phi(30)=8$.
        
    - $123 \div 8$. $120 = 15 \times 8$.
        
    - $123 = 15 \times 8 + 3$.
        
    - L'esponente 123 è congruente a $3 \pmod 8$.
        
4. **Calcolo:**
    
    - $11^{123} \equiv 11^3 \pmod{30}$.
        
    - Ora calcoliamo $11^3$:
        
        - $11^1 \equiv 11 \pmod{30}$
            
        - $11^2 \equiv 121 \pmod{30}$. $121 = 4 \times 30 + 1$.
            
        - $11^2 \equiv 1 \pmod{30}$.
            
    - (Abbiamo trovato un ciclo breve di 2! Possiamo usarlo.)
        
        $11^3 = 11^2 \times 11^1$
        
        $$\equiv 1 \times 11 \pmod{30}$$
        
        $$\equiv 11 \pmod{30}$$
        

**Risultato:** $11^{123} \pmod{30} = 11$.