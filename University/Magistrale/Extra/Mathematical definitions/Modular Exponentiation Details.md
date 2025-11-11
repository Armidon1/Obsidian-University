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

Qui sorge spesso la confusione che hai menzionato. Quando calcoliamo `a mod M`, non stiamo eseguendo una divisione in virgola mobile (come `1 / 3 = 0.333...`), ma stiamo applicando l'**Algoritmo di Divisione Euclidea**.

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
    
    Risultato = (Risultato * B) mod M
    
3. `Risultato` è la risposta.
    

**Vantaggio:** In ogni passaggio, il `Risultato` non supera mai `M-1` e la moltiplicazione `(Risultato * B)` non supera `M * B`. I numeri rimangono gestibili.

**Svantaggio:** La complessità computazionale è **O(E)**. Se `E` è un numero molto grande (come un esponente crittografico a 2048 bit), questo algoritmo richiederebbe un numero di passaggi superiore al numero di atomi nell'universo.

---

### Sezione 4: Esponenziazione Rapida (Exponentiation by Squaring)

Questo è il metodo efficiente, quello a cui ti riferivi parlando di "scomporre per esponente di due". Risolve il problema della complessità O(E) riducendola a **O(log E)**, un miglioramento astronomico.

#### 4.1 Il Concetto Chiave: Scomposizione dell'Esponente

L'idea fondamentale è che **non** stai scomponendo la base `B`. Stai scomponendo l'**esponente `E`** nella sua rappresentazione binaria (somma di potenze di 2).

Ogni numero intero E può essere scritto in modo unico come somma di potenze di 2.

Esempio: E = 13

- In binario, `13` si scrive `1101₂`.
    
- Questo significa: `13 = (1 * 2³) + (1 * 2²) + (0 * 2¹) + (1 * 2⁰)`
    
- Ovvero: `13 = 8 + 4 + 1`
    

Ora, applichiamo questa scomposizione all'esponenziazione:

B^13 = B^(8 + 4 + 1)

Per le proprietà delle potenze, questo equivale a:

B^13 = B^8 * B^4 * B^1

#### 4.2 L'Efficienza dei "Quadrati Ripetuti"

Hai giustamente notato che `B^E` è `B` moltiplicato per sé stesso `E` volte. Ma il metodo "by squaring" nota che non abbiamo bisogno di calcolare `B^8` facendo `B*B*B*B*B*B*B*B`.

Possiamo ottenere tutte le potenze di 2 (`B^1`, `B^2`, `B^4`, `B^8`, `B^16`, ...) in modo molto efficiente, "quadrando" ripetutamente il risultato precedente:

- `B^1 = B`
    
- `B^2 = B^1 * B^1`
    
- `B^4 = B^2 * B^2`
    
- `B^8 = B^4 * B^4`
    
- ...e così via.
    

Per calcolare `B^13`, ci servono solo `B^1`, `B^4` e `B^8`. Possiamo ottenerli in soli 3 passaggi di quadratura (per `B^2`, `B^4`, `B^8`).

Naturalmente, applichiamo il modulo `M` ad _ogni singolo passaggio_ per mantenere i numeri piccoli.

#### 4.3 Algoritmo Pratico (Right-to-Left) e Esempio

Calcoliamo **`3^13 (mod 7)`**.

- Base `B = 3`
    
- Esponente `E = 13`
    
- Modulo `M = 7`
    

L'esponente `E = 13` in binario è `1101₂`.

L'algoritmo procede esaminando i bit di E da destra a sinistra (dal bit 0 al bit 3).

Manteniamo due variabili:

1. `Risultato`: Il prodotto finale (inizia a 1).
    
2. `Potenza`: La potenza di `B` corrente (`B^1`, `B^2`, `B^4`, ...) (inizia con `B mod M`).
    

**Inizio:**

- `Risultato = 1`
    
- `Potenza = 3 mod 7 = 3`
    

**Ciclo (basato sui bit di 1101₂):**

1. **Bit 0 (è 1):** `110**1**₂`
    
    - Il bit è 1, quindi moltiplichiamo `Risultato` per la `Potenza` attuale.
        
    - `Risultato = (Risultato * Potenza) mod 7 = (1 * 3) mod 7 = 3`
        
    - Aggiorniamo `Potenza` quadrandola per il prossimo ciclo.
        
    - `Potenza = (Potenza * Potenza) mod 7 = (3 * 3) mod 7 = 9 mod 7 = 2`
        
2. **Bit 1 (è 0):** `11**0**1₂`
    
    - Il bit è 0, quindi _non_ moltiplichiamo `Risultato`.
        
    - `Risultato = 3` (rimane invariato)
        
    - Aggiorniamo `Potenza` quadrandola.
        
    - `Potenza = (Potenza * Potenza) mod 7 = (2 * 2) mod 7 = 4`
        
3. **Bit 2 (è 1):** `1**1**01₂`
    
    - Il bit è 1, quindi moltiplichiamo `Risultato`.
        
    - `Risultato = (Risultato * Potenza) mod 7 = (3 * 4) mod 7 = 12 mod 7 = 5`
        
    - Aggiorniamo `Potenza` quadrandola.
        
    - `Potenza = (Potenza * Potenza) mod 7 = (4 * 4) mod 7 = 16 mod 7 = 2`
        
4. **Bit 3 (è 1):** `**1**101₂`
    
    - Il bit è 1, quindi moltiplichiamo `Risultato`.
        
    - `Risultato = (Risultato * Potenza) mod 7 = (5 * 2) mod 7 = 10 mod 7 = 3`
        
    - Aggiorniamo `Potenza` (anche se il ciclo finisce, per completezza).
        
    - `Potenza = (Potenza * Potenza) mod 7 = (2 * 2) mod 7 = 4`
        

Fine:

Il ciclo è terminato. Il valore finale di Risultato è 3.

Quindi, `3^13 mod 7 = 3`.

Verifica:

3^13 = 1.594.323

1.594.323 / 7 = 227.760,42...

227.760 * 7 = 1.594.320

1.594.323 - 1.594.320 = 3.

Il risultato è corretto.

Come vedi, l'algoritmo ha eseguito solo 4 cicli (uno per bit) e i numeri più grandi gestiti sono stati `5*2=10` o `4*4=16`. Non abbiamo mai avuto bisogno di calcolare `1.594.323`.

---

### Sezione 5: Riepilogo

1. **Congruenza Modulare:** `a ≡ b (mod M)` significa che `a` e `b` hanno lo stesso resto quando divisi per `M`.
    
2. **Perché `1 mod 3 = 1`:** Per l'algoritmo di divisione, `1 = (0 * 3) + 1`. Il resto è 1.
    
3. **Proprietà Chiave:** Il modulo di un prodotto è il prodotto dei moduli: `(a*b) mod M = [(a mod M)*(b mod M)] mod M`.
    
4. **Esponenziazione Rapida:** Sfrutta la **rappresentazione binaria dell'esponente `E`** per ridurre il numero di moltiplicazioni da `E` (lineare) a `log₂(E)` (logaritmico).
    
5. **Come Funziona:** Calcola solo le potenze di `B` che sono potenze di 2 (es. `B^1, B^2, B^4, B^8...`) applicando il modulo a ogni quadratura. Poi, moltiplica tra loro solo le potenze che corrispondono ai bit "1" dell'esponente `E`.


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