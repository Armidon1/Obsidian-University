# L'Algoritmo di Divisione Euclidea (Teorema di Divisione)

### 1. Enunciato del Teorema

L'Algoritmo di Divisione Euclidea, noto anche più formalmente come **Teorema di Divisione**, è un pilastro fondamentale della teoria dei numeri. Esso formalizza la nozione intuitiva della "divisione con resto".

Il teorema afferma quanto segue:

> Dati due interi `a` (il **dividendo**) e `d` (il **divisore**), con `d ≠ 0`, esistono e sono **unici** due interi `q` (il **quoziente**) e `r` (il **resto**) tali che:
> 
> $$a = q \cdot d + r$$
> 
> e la condizione fondamentale sul resto è:
> 
> $$0 \le r < |d|$$
> 
> (dove |d| è il valore assoluto di d).

### 2. Analisi dei Componenti

- **`a` (Dividendo):** Il numero che deve essere diviso.
    
- **`d` (Divisore):** Il numero per cui si divide (`d` non può essere zero).
    
- **`q` (Quoziente):** Il risultato "intero" della divisione. Rappresenta quante volte `d` "sta" in `a`.
    
- **`r` (Resto):** La quantità che "avanza" dopo la divisione.
    

---

### 3. Il Cuore del Teorema: La Condizione `0 ≤ r < |d|`

L'essenza dell'algoritmo non risiede nella formula `a = q*d + r` (che è una semplice definizione algebrica), ma nella **condizione imposta al resto `r`**.

Questa condizione ha due parti:

1. **`r ≥ 0` (Il resto è non-negativo):** Questa è la convenzione matematica standard. Il resto non è mai un numero negativo. Questo è il punto che crea più confusione quando si gestiscono dividendi negativi.
    
2. **`r < |d|` (Il resto è minore del valore assoluto del divisore):** Se il resto fosse maggiore o uguale al divisore, significherebbe che potremmo "far stare" il divisore un'altra volta nel dividendo, aumentando il quoziente.
    

È questa doppia condizione che garantisce l'**unicità** di `q` e `r`. Per ogni coppia `(a, d)`, esiste _una sola_ coppia `(q, r)` che soddisfa l'equazione e la condizione.

### 4. Collegamento con l'Operatore `mod`

Il **resto `r`** ottenuto dall'Algoritmo di Divisione Euclidea è _esattamente_ il valore calcolato dall'operazione `a mod d`.

- `10 mod 3` cerca `r` in `10 = q * 3 + r`. La soluzione è `10 = 3 * 3 + 1`. Quindi `r = 1`.
    
- `1 mod 3` cerca `r` in `1 = q * 3 + r`. La soluzione è `1 = 0 * 3 + 1`. Quindi `r = 1`.
    
- `-8 mod 5` cerca `r` in `-8 = q * 5 + r`.
    
    - _Tentativo errato:_ `-8 = (-1) * 5 - 3`. Qui `r = -3`, che viola la condizione `r ≥ 0`.
        
    - _Tentativo corretto:_ Dobbiamo trovare un multiplo di 5 che sia inferiore a -8. Usiamo `q = -2`.
        
    - `-8 = (-2) * 5 + 2`. Qui `r = 2`, che soddisfa `0 ≤ 2 < 5`.
        
    - Quindi, `-8 mod 5 = 2`.
        

---

### 5. Esempi Svolti

1. **Caso Standard (a > 0, d > 0):** `a = 22, d = 5`
    
    - Cerchiamo `q` e `r` per `22 = q * 5 + r` con `0 ≤ r < 5`.
        
    - `22 / 5 = 4.4`. Prendiamo la parte intera `q = 4`.
        
    - `22 = 4 * 5 + r`
        
    - `22 = 20 + r`
        
    - `r = 2`.
        
    - La coppia unica è `(q=4, r=2)`. La condizione `0 ≤ 2 < 5` è soddisfatta.
        
2. **Caso Dividendo Minore (a > 0, d > 0):** `a = 7, d = 10`
    
    - Cerchiamo `q` e `r` per `7 = q * 10 + r` con `0 ≤ r < 10`.
        
    - Il 10 "sta" 0 volte nel 7. Quindi `q = 0`.
        
    - `7 = 0 * 10 + r`
        
    - `r = 7`.
        
    - La coppia unica è `(q=0, r=7)`. La condizione `0 ≤ 7 < 10` è soddisfatta.
        
3. **Caso Dividendo Negativo (a < 0, d > 0):** `a = -15, d = 4`
    
    - Cerchiamo `q` e `r` per `-15 = q * 4 + r` con `0 ≤ r < 4`.
        
    - Se dividiamo `-15 / 4` otteniamo `-3.75`. Molti studenti sono tentati di usare `q = -3`.
        
    - _Tentativo con `q = -3`:_ `-15 = (-3) * 4 + r` => `-15 = -12 + r` => `r = -3`. **Errato**. Viola `r ≥ 0`.
        
    - _Soluzione corretta:_ Dobbiamo "scendere" al multiplo di 4 immediatamente inferiore a -15. Dobbiamo scegliere un quoziente più negativo, `q = -4`.
        
    - `-15 = (-4) * 4 + r`
        
    - `-15 = -16 + r`
        
    - `r = 1`.
        
    - La coppia unica è `(q=-4, r=1)`. La condizione `0 ≤ 1 < 4` è soddisfatta.
        

### 6. Cenno alla Dimostrazione (Esistenza e Unicità)

La dimostrazione formale si basa sul **Principio del Buon Ordinamento** (che afferma che ogni sottoinsieme non vuoto di numeri naturali contiene un elemento minimo).

1. **Esistenza:** Si costruisce l'insieme `S` di tutti gli interi non-negativi della forma `a - k*d`, dove `k` è un intero qualsiasi. Si dimostra che `S` non è vuoto. Per il principio del buon ordinamento, `S` deve avere un elemento minimo. Questo elemento minimo è il nostro resto `r`. Si dimostra poi che `r < |d|` (se non lo fosse, `r - |d|` sarebbe un elemento più piccolo in `S`, una contraddizione).
    
2. **Unicità:** Si supponga, per assurdo, che esistano due coppie distinte `(q1, r1)` e `(q2, r2)` che soddisfano il teorema.
    
    - `a = q1*d + r1`
        
    - `a = q2*d + r2`
        
    - Eguagliando: `q1*d + r1 = q2*d + r2` => `(q1 - q2)d = r2 - r1`.
        
    - Questo significa che `d` divide la differenza `(r2 - r1)`.
        
    - Ma, per la condizione `0 ≤ r < |d|`, sappiamo che `-|d| < (r2 - r1) < |d|`.
        
    - L'unico multiplo di `d` che si trova strettamente tra `-|d|` e `|d|` è `0`.
        
    - Quindi, `r2 - r1 = 0` => `r1 = r2`.
        
    - Se `r1 = r2`, allora `(q1 - q2)d = 0`. Dato che `d ≠ 0`, deve essere `q1 - q2 = 0` => `q1 = q2`.
        
    - Le due coppie sono identiche. Questo dimostra l'unicità.
        

### 7. Distinzione Importante

L'**Algoritmo di Divisione Euclidea** (questo teorema) stabilisce _l'esistenza_ di `q` e `r`.

L'**Algoritmo Euclideo** (spesso confuso) è il _procedimento_ che usa questo teorema in modo ripetuto per trovare il Massimo Comun Divisore (MCD) tra due numeri.