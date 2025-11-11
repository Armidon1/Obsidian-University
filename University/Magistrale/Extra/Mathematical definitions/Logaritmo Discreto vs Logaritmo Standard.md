Questa è un'ottima domanda di approfondimento che va al cuore della differenza tra la matematica "classica" e quella usata in crittografia.

La parola **"discreto"** viene usata per sottolineare che stiamo lavorando all'interno di un **insieme finito e specifico di numeri interi**, (come gli interi modulo $p$), e non sull'insieme **continuo** dei numeri reali.

Ecco il confronto diretto:

---

### 🪵 Logaritmo (Standard)

- **Dominio:** Numeri reali (un insieme continuo).
    
- **Problema:** Dati $g$ e $y$ (numeri reali, $g > 0$, $g \neq 1$, $y > 0$), trovare $x$ tale che $g^x = y$.
    
- **Esempio:** $\log_2(8) = 3$ perché $2^3 = 8$. $\log_{10}(50) \approx 1.699...$ perché $10^{1.699...} = 50$.
    
- **Nota:** L'esponente $x$ può essere qualsiasi numero reale (un intero, una frazione, un numero irrazionale).
    
- **Difficoltà:** **Facile** da calcolare (il tuo computer o la tua calcolatrice lo fanno in una frazione di secondo).
    

---

### 🧩 Logaritmo Discreto

- **Dominio:** Un gruppo ciclico finito (un insieme discreto, cioè con elementi separati e contabili). L'esempio più comune sono gli **interi modulo $p$**.
    
- **Problema:** Dati $g$, $y$ e un modulo $p$ (tutti interi), trovare un intero $x$ tale che $g^x \equiv y \pmod{p}$.
    
- **Esempio:** Trovare $x$ per $3^x \equiv 13 \pmod{17}$. Ti sembra contro intuitiva questa operazione? guarda [[esempio di operazione modulo|qui]]
    
    - $3^1 = 3$
        
    - $3^2 = 9$
        
    - $3^3 = 27 \equiv 10$
        
    - $3^4 = 81 \equiv 13$
        
    - ...quindi il logaritmo discreto di 13 in base 3 (modulo 17) è **$x=4$**.
        
- **Nota:** L'esponente $x$ che cerchiamo è sempre un **numero intero**. L'aritmetica "va a capo" (wrap-around) a causa del modulo.
    
- **Difficoltà:** **Computazionalmente difficile** (infeasible) quando i numeri $p$ e $x$ sono molto grandi.
    

In sintesi, si chiama **"discreto"** perché l'intero problema è definito su un insieme discreto (i numeri interi da $0$ a $p-1$), non sulla retta continua dei numeri reali. È proprio questa natura "discreta" e "circolare" dell'aritmetica modulare a rendere il problema così difficile da risolvere, ed è per questo che è così prezioso per la crittografia.