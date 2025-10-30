Fattorizzare un numero significa **scomporlo nel prodotto dei suoi fattori primi**. 🧐

Il risultato è espresso come:

$$n = p_1^{a_1} \cdot p_2^{a_2} \cdot \ldots \cdot p_k^{a_k}$$

dove $p_1, p_2, \ldots, p_k$ sono i numeri primi distinti che dividono $n$, e $a_1, a_2, \ldots, a_k$ sono i loro rispettivi esponenti (quante volte quel primo appare nella scomposizione).

---

## Procedura per Fattorizzare un Numero

Il modo più comune per fattorizzare un numero intero positivo ($n > 1$) è usare la **divisione per tentativi** partendo dal più piccolo numero primo.

1. **Inizia dal primo numero primo, che è 2.**
    
    - Se il numero $n$ è **pari** (termina con 0, 2, 4, 6, 8), dividilo per 2 e continua a dividere il quoziente per 2 finché non ottieni un numero dispari. Conta quante volte hai diviso per 2 e quello sarà il tuo primo esponente.
        
2. **Passa al primo numero primo successivo, che è 3.**
    
    - Se il numero (dispari) ottenuto è **divisibile per 3** (la somma delle sue cifre è un multiplo di 3), dividilo per 3 e continua finché non è più divisibile. Conta le divisioni.
        
3. **Continua con i numeri primi successivi (5, 7, 11, 13, ecc.).**
    
    - Per il **5**, il numero deve terminare con 0 o 5.
        
    - Per i numeri successivi, controlla la divisibilità.
        
4. **Quando fermarsi?** Continua questo processo finché il quoziente che ottieni è **1** oppure **un numero primo**. Se il quoziente finale è un numero primo, anche questo farà parte della tua scomposizione con esponente 1.
    
    - _Suggerimento utile:_ Devi solo provare a dividere per numeri primi fino alla **radice quadrata del numero di partenza** (o del quoziente corrente). Se non hai trovato fattori fino a quel punto, il numero rimanente è primo.
        

---

## Esempio di Fattorizzazione

Fattorizziamo il numero **$180$**.

1. **Dividi per 2:**
    
    - $180 \div 2 = 90$
        
    - $90 \div 2 = 45$ (45 è dispari, stop con il 2)
        
    - Abbiamo diviso per 2 **due volte**: $2^2$
        
2. **Dividi per 3:**
    
    - $45 \div 3 = 15$
        
    - $15 \div 3 = 5$ (5 non è divisibile per 3, stop con il 3)
        
    - Abbiamo diviso per 3 **due volte**: $3^2$
        
3. **Dividi per 5:**
    
    - Il quoziente rimasto è **5**. Poiché 5 è un numero primo, ci fermiamo.
        
    - Abbiamo diviso per 5 **una volta**: $5^1$
        

La scomposizione in fattori primi di 180 è:

$$180 = 2^2 \cdot 3^2 \cdot 5^1$$

o semplicemente:

$$180 = 2^2 \cdot 3^2 \cdot 5$$