---
title: Calcolo Integrale di Funzioni di una Variabile
aliases:
  - AN1 — Calcolo Integrale
tags:
  - analisi-1
  - integrale
  - teorema-fondamentale
  - primitive
  - integrazione-per-parti
  - integrazione-per-sostituzione
  - integrali-impropri
source: Appunti di Analisi Matematica 1 di Camilli.pdf (cap. 6)
---

# Calcolo Integrale di Funzioni di una Variabile

> [!abstract]
> Il capitolo risponde a un problema geometrico: calcolare l'**area** sotto il grafico di una funzione. L'area viene approssimata con rettangoli (**somme inferiori e superiori**), e una funzione è **integrabile secondo Riemann** quando le due approssimazioni si incontrano. Seguono le proprietà dell'integrale, il **teorema della media** e il **teorema fondamentale del calcolo integrale**, che collega integrali e [[05 - AN1 - Calcolo Differenziale|derivate]]: per calcolare un integrale basta trovare una **primitiva**.
> Da qui i **metodi di integrazione** (per **parti** e per **sostituzione**, che invertono le regole del prodotto e della catena), l'integrazione delle **funzioni razionali**, le applicazioni geometriche (**aree**, **lunghezze di curve**, **volumi di rotazione**) e infine gli **integrali impropri**, con il confronto con le [[02 - AN1 - Serie Numeriche|serie]] che dimostra il comportamento dell'armonica generalizzata.
> Gli integrali si estendono a più variabili nel [[10 - AN1 - Integrali Multipli|cap. 10]].
> Mappa del corso: [[MOC - Analisi 1]].

---

## Integrale, definizione e prime proprietà

Vedi [[Integrale di Riemann]].

> [!question] Problema
> Data $f : [a, b] \to \mathbb{R}$ limitata, calcolare l'area $A$ tra il grafico di $f$ e l'asse $x$.

![[AN1-p093-1.png]]

*Figura 48 — L'area $A$.* La regione azzurra compresa tra il grafico di $f$, l'asse $x$ e le rette verticali $x = a$ e $x = b$. Per una figura con il bordo curvo non esiste una formula elementare come per i poligoni.

L'idea è approssimare $A$ **dal basso e dall'alto** (per difetto e per eccesso). Con $m := \inf f$ e $M := \sup f$ vale sicuramente
$$m(b - a) \le A \le M(b - a),$$
ma è un'approssimazione troppo grossolana (un rettangolo basso e uno alto). Per migliorarla si divide $[a, b]$ in tanti sottointervalli e si ripete lo stesso ragionamento in ciascuno.

> [!important] Definizione 6.1 — Partizione e somme
> - Un insieme $P = \{x_0, x_1, \dots, x_n\}$ si chiama **partizione** di $[a, b]$ se $a = x_0 < x_1 < \ldots < x_n = b$.
> - Se $f$ è limitata e $P$ è una partizione, per $i = 1, \dots, n$ si pongono
> $$m_i := \inf\{f(x) : x \in [x_{i-1}, x_i]\}, \qquad M_i := \sup\{f(x) : x \in [x_{i-1}, x_i]\}, \qquad \Delta x_i := x_i - x_{i-1},$$
> $$s(f, P) := \sum_{i=1}^n m_i \Delta x_i \ \ (\textbf{somma inferiore}), \qquad S(f, P) := \sum_{i=1}^n M_i \Delta x_i \ \ (\textbf{somma superiore}).$$

Per ogni partizione $P$ vale
$$s(f, P) \le A \le S(f, P):$$
le somme inferiori approssimano $A$ per difetto, quelle superiori per eccesso. Quindi più **grande** è $s(f, P)$, meglio è; più **piccola** è $S(f, P)$, meglio è.

![[AN1-p094-1.png]]

*Figura 49 — Somma inferiore $s(f, P)$ e somma superiore $S(f, P)$.* Lo stesso grafico con la partizione $a = x_0 < x_1 < \ldots < x_5 = b$. A sinistra (rosso) i rettangoli della somma inferiore: in ogni sottointervallo l'altezza è il minimo $m_i$, quindi stanno tutti sotto la curva. A destra (verde) quelli della somma superiore: l'altezza è il massimo $M_i$, quindi sporgono sopra la curva. L'area vera sta in mezzo.

Se non c'è differenza tra la migliore approssimazione dal basso (la più grande) e la migliore dall'alto (la più piccola), il problema è (teoricamente) risolto.

> [!important] Definizione 6.2 — Integrale di Riemann
> Sia $f : [a, b] \to \mathbb{R}$ limitata. Se
> $$\sup\{s(f, P) : P \text{ partizione di } [a, b]\} = \inf\{S(f, P) : P \text{ partizione di } [a, b]\} =: I,$$
> $f$ si dice **integrabile** (secondo **Riemann**). In tal caso $A = I$ e
> $$I := \int_a^b f(x)\,dx$$
> si chiama **integrale** di $f$ (la **funzione integranda**) su $[a, b]$ (il **dominio di integrazione**).

Esistono altri modi di definire l'integrale, ad esempio quello di **Lebesgue**, più generale, che si usa anche in probabilità.

Osservazioni:
- la variabile di integrazione è **muta**: $\int_a^b f(x)\,dx = \int_a^b f(s)\,ds = \int_a^b f(t)\,dt = \ldots$
- **criterio di integrabilità**: $f$ è integrabile $\iff$ per ogni $\varepsilon > 0$ esiste una partizione $P_\varepsilon$ con
$$S(f, P_\varepsilon) - s(f, P_\varepsilon) < \varepsilon.$$

![[AN1-p094-2.png]]

*Figura 50 — Criterio per l'integrabilità.* Su ogni sottointervallo la differenza tra il rettangolo superiore e quello inferiore è la striscia gialla. La somma delle aree gialle è $S - s$: $f$ è integrabile se, raffinando la partizione, si può rendere quest'area più piccola di qualsiasi $\varepsilon$ (il dischetto giallo "$< \varepsilon$").

- L'area sotto l'asse $x$ conta **negativa**: se $f(x) := -1$ su $[0, 1]$, allora $\int_0^1 f(x)\,dx = -1$.
- In un certo senso
$$\int_a^b f(x)\,dx = \lim_{\Delta x_i \to 0} \sum_{i=1}^n f(x_i) \Delta x_i,$$
il che spiega la notazione inventata da Leibniz più di 300 anni fa: $\int$ è una "S" allungata (somma) e $dx$ ricorda $\Delta x_i$.

> [!example] Esempi
> - Se $f(x) = c$ è costante, $s(f, P) = S(f, P) = c(b - a)$ già con $P = \{a, b\}$: $f$ è integrabile con $\int_a^b c\,dx = c(b - a)$.
> - La [[04 - AN1 - Funzioni Continue#Discontinuità|funzione di Dirichlet]] ($1$ sui razionali, $0$ sugli irrazionali) **non** è integrabile su $[a, b]$: ogni sottointervallo contiene razionali e irrazionali, quindi $m_i = 0$ e $M_i = 1$, e per ogni partizione
> $$s(f, P) = 0 \neq b - a = S(f, P).$$

_(dispensa, pp. 87–89)_

### Proprietà dell'integrale

Siano $f, g : [a, b] \to \mathbb{R}$ integrabili.

- **Linearità**: $\alpha f + \beta g$ è integrabile per ogni $\alpha, \beta \in \mathbb{R}$ (le funzioni integrabili formano uno **spazio vettoriale**) e
$$\int_a^b (\alpha f(x) + \beta g(x))\,dx = \alpha \int_a^b f(x)\,dx + \beta \int_a^b g(x)\,dx.$$
- **Monotonia**: se $f(x) \le g(x)$ per ogni $x \in [a, b]$, allora $\int_a^b f(x)\,dx \le \int_a^b g(x)\,dx$.
- **Disuguaglianza triangolare**: anche $|f|$ è integrabile e
$$\left|\int_a^b f(x)\,dx\right| \le \int_a^b |f(x)|\,dx.$$
- **Additività rispetto agli estremi**: per ogni $\alpha, \beta, \gamma \in [a, b]$
$$\int_\alpha^\beta f(x)\,dx + \int_\beta^\gamma f(x)\,dx = \int_\alpha^\gamma f(x)\,dx.$$

![[AN1-p095-1.png]]

*Figura 51 — Additività rispetto agli estremi di integrazione.* L'area da $\alpha$ a $\gamma$ è la somma dell'area rossa (da $\alpha$ a $\beta$) e di quella verde (da $\beta$ a $\gamma$).

Perché l'additività valga per qualsiasi ordine di $\alpha, \beta, \gamma$ si definisce
$$\int_\alpha^\alpha f(x)\,dx := 0, \qquad \int_\alpha^\beta f(x)\,dx := -\int_\beta^\alpha f(x)\,dx \quad \text{se } \alpha > \beta,$$
ad esempio $\int_1^0 f(x)\,dx := -\int_0^1 f(x)\,dx$.

> [!important] Proposizione 6.3 — Integrali di funzioni simmetriche
> Sia $f : [-a, a] \to \mathbb{R}$ integrabile. Allora
> - $\displaystyle\int_{-a}^a f(x)\,dx = 0$ se $f$ è **dispari**;
> - $\displaystyle\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$ se $f$ è **pari**.

![[AN1-p096-1.png]]

*Figura 52 — Integrazione di funzioni simmetriche.* A sinistra una funzione dispari: l'area rossa a sinistra (negativa) è lo specchio di quella verde a destra (positiva), quindi si cancellano ("rosso + verde = 0"). A destra una funzione pari: le due metà sono uguali, quindi l'integrale totale è il doppio di quello su $[0, a]$ ("rosso + verde = 2 × verde").

Le [[03 - AN1 - Funzioni Reali di una Variabile Reale#Funzioni simmetriche|simmetrie]] fanno risparmiare molti conti: ad esempio $\int_{-\pi}^{\pi} x^3 \cos(x)\,dx = 0$ senza calcolare nulla.

_(dispensa, pp. 89–90)_

### Quali funzioni sono integrabili

> [!question] Problemi
> 1. Quali funzioni sono integrabili?
> 2. Se $f$ è integrabile, come si calcola $\int_a^b f(x)\,dx$?

Per il primo problema basta il risultato seguente.

> [!important] Teorema 6.4
> Se $f : [a, b] \to \mathbb{R}$ è **limitata** e
> - ha un numero **finito di discontinuità**, oppure
> - è **monotona**,
>
> allora $f$ è integrabile. In particolare **ogni $f \in C[a, b]$ è integrabile**.

L'ultima affermazione segue dal primo punto: una funzione continua su $[a, b]$ ha zero discontinuità ed è limitata per [[04 - AN1 - Funzioni Continue#Funzioni Continue su Intervalli Chiusi e Limitati|Weierstrass]].

> [!example] Esempi di funzioni integrabili non continue
> $$f(x) := \begin{cases} 1 - \left(\frac12\right)^{n+1} & x \in \left[1 - \left(\frac12\right)^n, 1 - \left(\frac12\right)^{n+1}\right), \\ 1 & x = 1, \end{cases} \qquad g(x) := \begin{cases} e^{-x} & x \in [0, 1), \\ x^2 - 2 & x \in [1, 2), \\ \sin(2x) & x \in [2, 3], \end{cases}$$
> su $[0, 1]$ e $[0, 3]$ sono integrabili: $f$, nonostante abbia infiniti punti di discontinuità, è crescente; $g$ ha solo 2 discontinuità ($x_0 = 1$ e $x_1 = 2$).

![[AN1-p096-2.png]]

*Figura 53 — Esempi di funzioni integrabili non continue.* A sinistra $f$: una "scala" di gradini sempre più corti che salgono verso $1$ (vale $\frac12$ su $[0, \frac12)$, $\frac34$ su $[\frac12, \frac34)$, …), con infiniti salti che si accumulano in $x = 1$. A destra $g$: tre pezzi diversi (un esponenziale decrescente, un arco di parabola, un tratto di sinusoide) con due salti in $x = 1$ e $x = 2$.

_(dispensa, p. 90)_

---

## Il Teorema Fondamentale del Calcolo Integrale

Si passa al secondo problema: **calcolare** $\int_a^b f(x)\,dx$, perché con la definizione ci si riesce solo in casi molto semplici.

### Teorema della media

Vedi [[Teorema della media integrale]].

> [!important] Teorema 6.5 — Teorema della media
> Se $f \in C[a, b]$, esiste $c \in [a, b]$ con
> $$\int_a^b f(x)\,dx = f(c)(b - a).$$

![[AN1-p097-1.png]]

*Figura 54 — Teorema della media.* La linea orizzontale tratteggiata all'altezza $f(c)$ definisce un rettangolo di base $b - a$. Le parti rosse (dove la curva sta sotto il livello $f(c)$) e quelle verdi (dove sta sopra) hanno la stessa area totale: il rettangolo ha esattamente la stessa area della regione sotto la curva.

**Dimostrazione.** Per Weierstrass esistono $m := \min f$ e $M := \max f$, e
$$m(b - a) \le \int_a^b f(x)\,dx \le M(b - a) \quad\Rightarrow\quad \min f \le \underbrace{\frac{1}{b - a}\int_a^b f(x)\,dx}_{= \text{ valor medio di } f \text{ in } [a, b]} \le \max f.$$
Per il [[04 - AN1 - Funzioni Continue#Teorema dei valori intermedi|teorema dei valori intermedi]] il valor medio è assunto da $f$ in qualche $c$. $\square$

$\frac{1}{b-a}\int_a^b f$ è la **media** dei valori di $f$, l'analogo continuo della media aritmetica (e del [[Expected Value|valore atteso]] in probabilità).

### Teorema fondamentale

Vedi [[Teorema fondamentale del calcolo integrale]].

> [!important] Teorema 6.6 — Teorema fondamentale del calcolo integrale
> Sia $f \in C[a, b]$. Allora la **funzione integrale** di $f$
> $$F : [a, b] \to \mathbb{R}, \qquad F(x) := \int_a^x f(s)\,ds$$
> è derivabile con
> $$F'(x) = f(x) \qquad \forall x \in [a, b].$$

![[AN1-p098-1.png]]

*Figura 55 — La funzione integrale.* $F(x)$ è l'area gialla sotto il grafico di $f$ tra $a$ e un estremo **variabile** $x$. Spostando $x$ verso destra l'area cresce tanto più rapidamente quanto più è alta la curva in quel punto: è esattamente il contenuto del teorema, $F' = f$.

**Dimostrazione.** Per l'additività rispetto agli estremi e il teorema della media:
$$\frac{F(x + h) - F(x)}{h} = \frac{\int_a^{x+h} f(s)\,ds - \int_a^x f(s)\,ds}{h} = \frac{\int_x^{x+h} f(s)\,ds}{h} = \frac{h \cdot f(c_{x,h})}{h} = f(c_{x,h})$$
per un $c_{x,h}$ tra $x$ e $x + h$. Per $h \to 0$ si ha $c_{x,h} \to x$ e, per la continuità di $f$, $f(c_{x,h}) \to f(x)$. $\square$

### Primitive

Vedi [[Primitiva]].

- Se $G$ è derivabile con $G' = f$, $G$ si dice **primitiva** di $f$. L'insieme
$$\int f(x)\,dx := \{G : G \text{ è una primitiva di } f\}$$
si chiama **integrale indefinito** di $f$. Per distinguerlo, $\int_a^b f(x)\,dx$ (che è un **numero**) si chiama **integrale definito**.
- Se $F$ e $G$ sono due primitive di $f \in C[a, b]$, allora $(F - G)' = f - f = 0$, e per la [[05 - AN1 - Calcolo Differenziale#Caratterizzazione delle funzioni costanti|caratterizzazione delle funzioni costanti]] esiste $c \in \mathbb{R}$ con $F(x) = G(x) + c$. Per questo si scrive
$$\int f(x)\,dx = F(x) + c,$$
dove $c \in \mathbb{R}$ è una **costante arbitraria di integrazione**.

Il teorema fondamentale dice quindi che ogni funzione continua **ha** una primitiva (la funzione integrale). Ora si risolve il secondo problema.

> [!important] Corollario 6.7 — Formula fondamentale
> Se $f \in C[a, b]$ e $G$ è una primitiva di $f$ ($G' = f$), allora
> $$\int_a^b f(x)\,dx = G(b) - G(a) =: \big[G(x)\big]_a^b =: G(x)\Big|_a^b.$$

**Dimostrazione.** Sia $F$ la funzione integrale. Per il teorema fondamentale è una primitiva, quindi $F = G + c$, e
$$\int_a^b f(x)\,dx = \underbrace{\int_a^b f(x)\,dx}_{= F(b)} - \underbrace{\int_a^a f(x)\,dx}_{= 0 = F(a)} = F(b) - F(a) = (G(b) + c) - (G(a) + c) = G(b) - G(a). \quad \square$$

> [!important] In pratica
> Per calcolare $\int_a^b f(x)\,dx$ "basta" trovare una primitiva di $f$.

"Basta" è tra virgolette perché trovare una primitiva (si dice anche **integrare** $f$) in generale non è facile. Derivazione e integrazione sono operazioni **inverse**:

```mermaid
flowchart LR
    G["G (primitiva)"] -- "derivata: G' = f" --> F["f"]
    F -- "integrale: ∫ f dx = G + c" --> G
    F -- "∫ₐᵇ f dx = G(b) − G(a)" --> N["numero (area con segno)"]
```

_(dispensa, pp. 91–93)_

### Primi integrali

> [!example] Esempio: $\int_1^2 x^2\,dx$
> Poiché $\left(\frac{x^3}{3}\right)' = x^2$:
> $$\int_1^2 x^2\,dx = \frac{x^3}{3}\Big|_1^2 = \frac13(2^3 - 1^3) = \frac73.$$

![[AN1-p099-1.png]]

*Figura 56 — Area sotto il grafico.* La parabola $y = x^2$ e la regione gialla tra $x = 1$ e $x = 2$, che ha area $\frac73 \approx 2{,}33$.

> [!example] Esempio: il logaritmo
> $G(x) := \ln|x|$ per $x \neq 0$ è derivabile con
> $$G'(x) = \begin{cases} (\ln(x))' = \frac1x & x > 0, \\ (\ln(-x))' = \frac{1}{-x} \cdot (-1) = \frac1x & x < 0, \end{cases} \qquad \text{quindi} \quad \int \frac1x\,dx = \ln|x| + c.$$
> Ne segue una nuova rappresentazione del logaritmo: per $x > 0$
> $$\int_1^x \frac1s\,ds = \ln(s)\Big|_1^x = \ln(x) - \ln(1) = \ln(x).$$

![[AN1-p099-2.png]]

*Figura 57 — Il logaritmo.* Il grafico dell'iperbole $\frac1s$ e l'area gialla tra $s = 1$ e $s = x$: quest'area **è** $\ln(x)$. Si potrebbe addirittura definire il logaritmo in questo modo.

> [!summary] Integrali immediati
> | Integrale | Primitiva |
> |---|---|
> | $\int x^r\,dx$, $r \neq -1$ | $\frac{x^{r+1}}{r+1} + c$ |
> | $\int \frac1x\,dx$ | $\ln\lvert x\rvert + c$ |
> | $\int \frac{1}{1+x^2}\,dx$ | $\arctan(x) + c$ |
> | $\int e^x\,dx$ | $e^x + c$ |
> | $\int \sin(x)\,dx$ | $-\cos(x) + c$ |
> | $\int \cos(x)\,dx$ | $\sin(x) + c$ |
> | $\int \sinh(x)\,dx$ | $\cosh(x) + c$ |
> | $\int \cosh(x)\,dx$ | $\sinh(x) + c$ |

In questi esempi la primitiva era facile da indovinare perché si partiva da una funzione derivabile $G$ nota, che diventa per definizione la primitiva della sua derivata. Nelle applicazioni invece è data la funzione integranda, e la primitiva non è ovvia.

> [!question] Problema
> Come si trova una primitiva di una funzione più complicata? Ad esempio $\ln$ è continua, quindi integrabile, ma quanto vale $\int \ln(x)\,dx$?

_(dispensa, pp. 93–94)_

---

## Metodi di Integrazione

Grazie al teorema fondamentale, derivazione e integrazione sono **operazioni inverse**: se $h \in C^1$,
$$(\ast) \qquad \int h'(x)\,dx = h(x) + c.$$
Quindi **ogni regola di derivazione implica una regola di integrazione**.

### Integrazione per parti

Vedi [[Integrazione per parti]].

Se $f, g \in C^1$, anche $h := f \cdot g$ lo è, con $h' = f'g + fg'$. Da $(\ast)$:
$$\int f'(x) g(x)\,dx + \int f(x) g'(x)\,dx = \int \underbrace{\big(f'(x) g(x) + f(x) g'(x)\big)}_{= h'(x)}\,dx = \underbrace{f(x) g(x)}_{= h(x)} + c.$$

> [!important] Integrazione per parti
> $$\int f'(x) g(x)\,dx = f(x) g(x) - \int f(x) g'(x)\,dx \qquad \text{(versione indefinita)}$$
> $$\int_a^b f'(x) g(x)\,dx = f(x) g(x)\Big|_a^b - \int_a^b f(x) g'(x)\,dx \qquad \text{(versione definita)}$$

L'integrazione per parti corrisponde alla **regola del prodotto**: si "sposta" la derivata da un fattore all'altro, sperando che il nuovo integrale sia più semplice.

> [!example] Esempio: $\int x^r \ln(x)\,dx$, $r \neq -1$
> Bisogna decidere chi è $f'$ e chi è $g$. Con $f' = \ln(x)$ non si va avanti (non si conosce ancora la primitiva del logaritmo), quindi $f'(x) = x^r$ e $g(x) = \ln(x)$, cioè $f(x) = \frac{x^{r+1}}{r+1}$ e $g'(x) = \frac1x$:
> $$\int \underbrace{x^r}_{f'} \underbrace{\ln(x)}_{g}\,dx = \frac{x^{r+1}}{r+1}\ln(x) - \int \frac{x^{r+1}}{r+1} \cdot \frac1x\,dx = \frac{x^{r+1}}{r+1}\ln(x) - \frac{1}{r+1}\int x^r\,dx$$
> $$= \frac{x^{r+1}}{r+1}\ln(x) - \frac{x^{r+1}}{(r+1)^2} + c = \frac{x^{r+1}}{r+1}\left(\ln(x) - \frac{1}{r+1}\right) + c.$$
> Funziona perché $\ln$ è una funzione "complicata" con derivata $\frac1x$ "semplice": passando la derivata da $f$ a $g$, l'integrale si semplifica. Con $r = 0$ ($x^0 = 1$):
> $$\int \ln(x)\,dx = x(\ln(x) - 1) + c.$$
> Direttamente, con il **trucco del fattore 1**:
> $$\int \underbrace{1}_{f'} \cdot \underbrace{\ln(x)}_{g}\,dx = x\ln(x) - \int x \cdot \frac1x\,dx = x\ln(x) - x + c.$$

> [!example] Esempio: $\int e^x \cos(x)\,dx$ (integrale "ciclico")
> Con $f'(x) = e^x$ e $g(x) = \cos(x)$ (funzionerebbe anche il viceversa):
> $$\int e^x \cos(x)\,dx = e^x\cos(x) - \int e^x(-\sin(x))\,dx = e^x\cos(x) + \int e^x \sin(x)\,dx.$$
> Sembra che non sia cambiato molto, ma si integra un'altra volta per parti ($u' = e^x$, $v = \sin x$):
> $$\int e^x\cos(x)\,dx = e^x\cos(x) + e^x\sin(x) - \int e^x\cos(x)\,dx.$$
> Si torna all'integrale iniziale $I$, ma si è ottenuta un'**equazione** del tipo $I = E + \alpha I$ con $E$ nota e $\alpha = -1 \neq 1$ (se fosse $\alpha = 1$ l'integrale si semplificherebbe e il procedimento sarebbe inutile). Risolvendo, $I = \frac{E}{1 - \alpha}$ con $1 - \alpha = 2$:
> $$\int e^x\cos(x)\,dx = \frac{e^x(\sin(x) + \cos(x))}{2} + c.$$

> [!example] Esempio: $\int \cos^2(x)\,dx$
> Con $f' = g = \cos$, cioè $f = \sin$, $g' = -\sin$:
> $$\int \cos^2(x)\,dx = \sin(x)\cos(x) + \int \sin^2(x)\,dx.$$
> Integrare un'altra volta per parti porta solo all'identità $0 = 0$. Si usa invece $\sin^2 = 1 - \cos^2$:
> $$\int \cos^2(x)\,dx = \sin(x)\cos(x) + \int 1\,dx - \int \cos^2(x)\,dx = \sin(x)\cos(x) + x - \int \cos^2(x)\,dx,$$
> un'equazione per l'integrale con soluzione
> $$\int \cos^2(x)\,dx = \frac{\sin(x)\cos(x) + x}{2} + c.$$

_(dispensa, pp. 94–96)_

### Integrazione per sostituzione

Vedi [[Integrazione per sostituzione]].

Ora si parte dalla **regola della catena**. Sia $f \in C[a, b]$ con primitiva $F$ e sia $\varphi : [\alpha, \beta] \to [a, b]$ derivabile con continuità e con $\varphi' \neq 0$ (si usano le variabili $t \in [\alpha, \beta]$ e $x \in [a, b]$). La composta $h(t) := F(\varphi(t))$ è derivabile con
$$h'(t) = F'(\varphi(t))\varphi'(t) = f(\varphi(t))\varphi'(t).$$
Sostituendo in $(\ast)$:

> [!important] Integrazione per sostituzione
> $$\int f(\varphi(t))\varphi'(t)\,dt = F(\varphi(t)) + c \qquad \text{(versione indefinita, con } F' = f)$$
> $$\int_\alpha^\beta f(\varphi(t))\varphi'(t)\,dt = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x)\,dx \qquad \text{(versione definita)}$$

La versione definita segue dal corollario 6.7:
$$\int_\alpha^\beta f(\varphi(t))\varphi'(t)\,dt = F(\varphi(t))\Big|_{t=\alpha}^{t=\beta} = F(\varphi(\beta)) - F(\varphi(\alpha)) = F(x)\Big|_{x=\varphi(\alpha)}^{x=\varphi(\beta)} = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x)\,dx.$$

Due regole generali che ne seguono:

> [!example] Derivata logaritmica
> Con $f(x) = \frac1x$ ($F(x) = \ln|x|$) e $\varphi \in C^1$ con $\varphi(t) \neq 0$:
> $$\int \frac{\varphi'(t)}{\varphi(t)}\,dt = \ln|\varphi(t)| + c.$$
> Ad esempio
> $$\int \tan(t)\,dt = \int \frac{\sin(t)}{\cos(t)}\,dt = -\int \frac{\overbrace{-\sin(t)}^{\varphi'(t)}}{\underbrace{\cos(t)}_{\varphi(t)}}\,dt = -\ln|\cos(t)| + c.$$

> [!example] Funzione per la sua derivata
> Con $f(x) = x$ ($F(x) = \frac{x^2}{2}$) e $\varphi \in C^1$:
> $$\int \varphi(t)\varphi'(t)\,dt = \frac{\varphi(t)^2}{2} + c, \qquad \text{es. } \int \underbrace{\sin(t)}_{\varphi}\underbrace{\cos(t)}_{\varphi'}\,dt = \frac{\sin^2(t)}{2} + c.$$

> [!tip] Come si usa in pratica
> Nella funzione integranda (variabile $t$) si individua un'espressione $\varphi(t)$ che si chiama $x$: la **sostituzione** $x := \varphi(t)$. Considerando $x$ come funzione di $t$ e derivando (formalmente):
> $$\frac{dx}{dt} = \varphi'(t) \quad\Rightarrow\quad dx = \varphi'(t)\,dt.$$
> Allora
> $$\int \underbrace{f(\varphi(t))}_{= f(x)} \underbrace{\varphi'(t)\,dt}_{= dx} = \int f(x)\,dx = F(x) + c = F(\varphi(t)) + c.$$
> Per la versione definita: $t = \alpha \Rightarrow x = \varphi(\alpha)$ e $t = \beta \Rightarrow x = \varphi(\beta)$, cioè si cambiano anche gli **estremi**.
>
> Il ragionamento è puramente formale, ma mostra la forza delle notazioni di Leibniz: le derivate come rapporti $\frac{df}{dx}$ di infinitesimi e gli integrali come somme continue $\int f(x)\,dx$.

> [!example] Esempio: $\int_1^2 t\sqrt{t - 1}\,dt$
> Per far sparire la radice si pone $x := \sqrt{t - 1}$. Anche il fattore $t$ va espresso in $x$: $x^2 = t - 1 \Rightarrow t = x^2 + 1$. La relazione tra $dx$ e $dt$ si trova in due modi equivalenti:
> - derivando $x = \sqrt{t-1}$ rispetto a $t$: $\frac{dx}{dt} = \frac{1}{2\sqrt{t-1}} = \frac{1}{2x} \Rightarrow dt = 2x\,dx$;
> - derivando $t = x^2 + 1$ rispetto a $x$: $\frac{dt}{dx} = 2x \Rightarrow dt = 2x\,dx$.
>
> Estremi: $t = 1 \Rightarrow x = 0$; $t = 2 \Rightarrow x = 1$. Quindi
> $$\int_1^2 \underbrace{t}_{x^2+1} \cdot \underbrace{\sqrt{t-1}}_{x}\,\underbrace{dt}_{2x\,dx} = \int_0^1 (x^2 + 1) \cdot x \cdot 2x\,dx = 2\int_0^1 (x^4 + x^2)\,dx = 2\left[\frac{x^5}{5} + \frac{x^3}{3}\right]_0^1 = 2\left(\frac15 + \frac13\right) = \frac{16}{15}.$$

Invece di calcolare gli estremi nella nuova variabile, si può anche integrare, **tornare alla variabile iniziale** (per gli integrali indefiniti è sempre necessario) e poi sostituire gli estremi originali.

> [!example] Esempio: $\int_1^4 e^{\sqrt t}\,dt$ (sostituzione e parti insieme)
> Con $x := \sqrt t$, cioè $t = x^2$ e $dt = 2x\,dx$ (estremi indicati con "…" perché non servono subito):
> $$\int_1^4 e^{\sqrt t}\,dt = \int_\ldots^\ldots e^x \cdot 2x\,dx.$$
> È un integrale per parti con $f' = e^x$ e $g = x$ (il viceversa porterebbe a $\int x^2 e^x\,dx$, ancora più difficile):
> $$2\int x e^x\,dx = 2\left(x e^x - \int e^x\,dx\right) = 2\left[xe^x - e^x\right] \overset{x = \sqrt t}{=} 2\left[e^{\sqrt t}(\sqrt t - 1)\right]_1^4 = 2\big(e^2(2 - 1) - e(1 - 1)\big) = 2e^2.$$

> [!example] Esempio: $\int \cos(\ln(t))\,dt$
> Per far sparire il logaritmo: $x := \ln(t)$, cioè $t = e^x$ e $dt = e^x\,dx$:
> $$\int \cos(\underbrace{\ln(t)}_{x})\,\underbrace{dt}_{e^x dx} = \int \cos(x)e^x\,dx = \frac{e^x(\sin(x) + \cos(x))}{2} + c \overset{x = \ln t}{=} \frac{t\big(\sin(\ln t) + \cos(\ln t)\big)}{2} + c,$$
> usando l'integrale ciclico già calcolato. Per un integrale indefinito si deve sempre tornare alla variabile iniziale.

A volte la sostituzione giusta è difficile da trovare:

> [!example] Esempio: area del cerchio
> L'area del cerchio di raggio 1 ($x^2 + y^2 = 1$): nel primo quadrante $y = \sqrt{1 - x^2}$, e per simmetria
> $$A = 4\int_0^1 \sqrt{1 - x^2}\,dx.$$
> Con $x := \sin(t)$, cioè $t = \arcsin(x)$: $dx = \cos(t)\,dt$, $x = 0 \Rightarrow t = 0$, $x = 1 \Rightarrow t = \frac\pi2$. Per $t \in \left[0, \frac\pi2\right]$ vale $\cos(t) \ge 0$, quindi $\sqrt{1 - \sin^2 t} = \cos t$ e
> $$\int_0^1 \sqrt{1 - x^2}\,dx = \int_0^{\frac\pi2} \sqrt{1 - \sin^2(t)}\cos(t)\,dt = \int_0^{\frac\pi2} \cos^2(t)\,dt = \frac{\sin(t)\cos(t) + t}{2}\Big|_0^{\frac\pi2} = \frac\pi4.$$
> Quindi $A = 4 \cdot \frac\pi4 = \pi$. Allo stesso modo l'area del cerchio di raggio $r$ è $A(r) = \pi r^2$.

> [!example] Esempio: $\int \arctan(x)\,dx$
> Come $\ln$, $\arctan$ è "complicata" con derivata $\frac{1}{1+x^2}$ semplice: si usa il trucco del fattore 1 e poi la derivata logaritmica:
> $$\int 1 \cdot \arctan(x)\,dx = x\arctan(x) - \int \frac{x}{1 + x^2}\,dx = x\arctan(x) - \frac12\int \frac{2x}{1 + x^2}\,dx = x\arctan(x) - \frac{\ln(1 + x^2)}{2} + c.$$
> (Si poteva anche sostituire $t := 1 + x^2$.)

> [!warning] Integrare è difficile, derivare no
> Derivare è una procedura meccanica; integrare può essere impegnativo, e a volte **impossibile in forma esplicita**. Esistono funzioni continue (quindi con una primitiva, per il teorema fondamentale), composte da funzioni elementari, le cui primitive **non** si possono esprimere con funzioni elementari. Ad esempio $f(x) = e^{\pm x^2}$ è $C^\infty$, ma
> $$\int e^{x^2}\,dx \qquad \text{e} \qquad \int e^{-x^2}\,dx$$
> non si possono scrivere con le funzioni viste finora. Per $e^{-x^2}$ è un problema serio in probabilità: la densità della [[Gaussian|distribuzione normale]] non ha primitiva elementare, ed è per questo che si usano le tavole.

> [!example] Esempio: un limite con un integrale non calcolabile
> $$l := \lim_{x\to0} \frac{\int_0^x (1 - e^{s^2})\,ds}{\sin(x^3)}.$$
> L'integrale non si sa calcolare, ma non serve: con l'Hospital e il teorema fondamentale (la derivata del numeratore è l'integranda calcolata in $x$). Prima si sostituisce $\sin(x^3)$ con $x^3$, asintotica per $x \to 0$:
> $$l = \lim_{x\to0} \frac{\int_0^x (1 - e^{s^2})\,ds}{x^3} \left(= \tfrac00\right) \overset{H}{=} \lim_{x\to0} \frac{1 - e^{x^2}}{3x^2} = -\frac13 \lim_{x\to0} \frac{e^{x^2} - 1}{x^2} = -\frac13.$$

_(dispensa, pp. 96–101)_

---

## Integrazione di Funzioni Razionali

Vedi [[Integrazione di funzioni razionali]].

> [!question] Problema
> Come si integra una funzione razionale $\frac{p(x)}{q(x)}$? Ad esempio
> $$\int \frac{x^4 - 2x^2 + 10}{x^2 - 3x + 2}\,dx\ ?$$

Una soluzione esiste sempre e coinvolge solo tre integrali notevoli: quelli di $x^r$ ($r \neq -1$), $x^{-1}$ e $\frac{1}{1 + x^2}$. Si tratta di scomporre l'integranda in modo da poterli usare, in tre passi.

**1° passo: divisione.** Se $\operatorname{grado}(p) \ge \operatorname{grado}(q)$, si divide $p$ per $q$ con resto: $p = s \cdot q + r$ con $\operatorname{grado}(r) < \operatorname{grado}(q)$, cioè
$$\frac{p(x)}{q(x)} = s(x) + \frac{r(x)}{q(x)}.$$
Nell'esempio:
$$(x^4 - 2x^2 + 10) : (x^2 - 3x + 2) = x^2 + 3x + 5 \quad \text{con resto } 9x,$$
cioè $\frac{x^4 - 2x^2 + 10}{x^2 - 3x + 2} = x^2 + 3x + 5 + \frac{9x}{x^2 - 3x + 2}$. (Verifica: $(x^2 + 3x + 5)(x^2 - 3x + 2) = x^4 - 2x^2 - 9x + 10$, e sommando $9x$ si ottiene $p$.)

**2° passo: linearità.**
$$\int \frac{p(x)}{q(x)}\,dx = \underbrace{\int s(x)\,dx}_{\text{facile (polinomio)}} + \int \frac{r(x)}{q(x)}\,dx.$$
Nell'esempio: $\int (x^2 + 3x + 5)\,dx = \frac{x^3}{3} + \frac{3x^2}{2} + 5x$.

**3° passo: $\int \frac{r(x)}{q(x)}\,dx$.** Si considera solo il caso $\operatorname{grado}(q) = 2$: $q(x) = ax^2 + bx + c$, $r(x) = dx + e$. Ci sono tre casi, secondo il segno del discriminante $\Delta = b^2 - 4ac$:

| Caso | Zeri di $q$ | Scomposizione | Primitiva |
|---|---|---|---|
| (i) $\Delta > 0$ | due reali distinti $x_1, x_2$ | $\frac{A}{x - x_1} + \frac{B}{x - x_2}$ | $A\ln\lvert x - x_1\rvert + B\ln\lvert x - x_2\rvert$ |
| (ii) $\Delta = 0$ | uno doppio $x_0 = -\frac{b}{2a}$ | $\frac{A}{x - x_0} + \frac{B}{(x - x_0)^2}$ | $A\ln\lvert x - x_0\rvert - \frac{B}{x - x_0}$ |
| (iii) $\Delta < 0$ | nessuno reale | $\frac{A\,q'(x) + B}{q(x)}$ | $A\ln\lvert q(x)\rvert + B\int \frac{dx}{q(x)}$ |

In ogni caso le costanti $A, B \in \mathbb{R}$ esistono e sono uniche; si trovano **confrontando i coefficienti**.

> [!example] Caso (i): $\int \frac{9x}{x^2 - 3x + 2}\,dx$
> Zeri: $x_{1,2} = \frac{3 \pm \sqrt{9 - 8}}{2} = 1$ oppure $2$. Si cercano $A, B$ con
> $$\frac{9x}{x^2 - 3x + 2} \overset{!}{=} \frac{A}{x - 1} + \frac{B}{x - 2} = \frac{(A + B)x - (2A + B)}{(x-1)(x-2)} \iff \begin{cases} A + B = 9 \\ 2A + B = 0 \end{cases} \iff \begin{cases} A = -9 \\ B = 18 \end{cases}$$
> Quindi $\int \frac{9x}{x^2 - 3x + 2}\,dx = -9\ln|x - 1| + 18\ln|x - 2| + c$, e l'integrale di partenza vale
> $$\int \frac{x^4 - 2x^2 + 10}{x^2 - 3x + 2}\,dx = \frac{x^3}{3} + \frac{3x^2}{2} + 5x - 9\ln|x - 1| + 18\ln|x - 2| + c.$$

> [!example] Caso (ii): $\int \frac{3x}{x^2 - 2x + 1}\,dx$
> Il denominatore si annulla solo in $x_0 = \frac{2 \pm \sqrt{4 - 4}}{2} = 1$:
> $$\frac{3x}{x^2 - 2x + 1} \overset{!}{=} \frac{A}{x - 1} + \frac{B}{(x - 1)^2} = \frac{Ax + (B - A)}{(x-1)^2} \iff \begin{cases} A = 3 \\ B - A = 0 \end{cases} \iff A = B = 3.$$
> Quindi $\int \frac{3x}{x^2 - 2x + 1}\,dx = 3\ln|x - 1| - \frac{3}{x - 1} + c$.

**Caso (iii) in dettaglio.** Resta $\int \frac{dx}{q(x)} = \int \frac{dx}{ax^2 + bx + c}$. Si cercano $\alpha, \beta, \gamma$ con ("completamento del quadrato")
$$q(x) = \gamma\left(1 + \left(\tfrac{x + \alpha}{\beta}\right)^2\right),$$
e con la sostituzione $t := \frac{x + \alpha}{\beta}$, $dx = \beta\,dt$:
$$\int \frac{dx}{q(x)} = \frac\beta\gamma\int \frac{dt}{1 + t^2} = \frac\beta\gamma\arctan(t) + c = \frac\beta\gamma\arctan\left(\frac{x + \alpha}{\beta}\right) + c.$$
In totale, se $\frac{r(x)}{q(x)} = \frac{Aq'(x) + B}{q(x)}$:
$$\int \frac{r(x)}{q(x)}\,dx = A\ln|q(x)| + \frac{\beta B}{\gamma}\arctan\left(\frac{x + \alpha}{\beta}\right) + c.$$

> [!example] Caso (iii): $\int \frac{4x}{x^2 - 4x + 13}\,dx$
> $\Delta = 16 - 52 < 0$. Con $q'(x) = 2x - 4$:
> $$\frac{4x}{x^2 - 4x + 13} \overset{!}{=} \frac{A(2x - 4) + B}{x^2 - 4x + 13} = \frac{2Ax + (-4A + B)}{x^2 - 4x + 13} \iff \begin{cases} 2A = 4 \\ -4A + B = 0 \end{cases} \iff A = 2,\ B = 8,$$
> quindi $\int \frac{4x}{x^2 - 4x + 13}\,dx = 2\ln(x^2 - 4x + 13) + 8\int \frac{dx}{x^2 - 4x + 13}$. Poi
> $$x^2 - 4x + 13 = (x - 2)^2 + 9 = 9\left(1 + \left(\tfrac{x - 2}{3}\right)^2\right) \qquad (\alpha = -2,\ \beta = 3,\ \gamma = 9),$$
> e con $t := \frac{x - 2}{3}$, $dx = 3\,dt$:
> $$\int \frac{dx}{x^2 - 4x + 13} = \frac39\int \frac{dt}{1 + t^2} = \frac13\arctan\left(\frac{x - 2}{3}\right) + c.$$
> Risultato finale:
> $$\int \frac{4x}{x^2 - 4x + 13}\,dx = 2\ln(x^2 - 4x + 13) + \frac83\arctan\left(\frac{x - 2}{3}\right) + c.$$

> [!warning] Correzione
> Nell'esempio la dispensa scrive "$\alpha = 2$", ma con la convenzione $q(x) = \gamma\left(1 + \left(\frac{x + \alpha}{\beta}\right)^2\right)$ e $(x - 2)^2$ deve essere $\alpha = -2$. Il risultato finale $\arctan\left(\frac{x - 2}{3}\right)$ è comunque corretto.

> [!example] Altri esempi (con soluzione)
> - $\displaystyle\int_0^1 \frac{2}{\cosh(x)}\,dx$ (sostituzione $e^x = t$, $dx = \frac{dt}{t}$): $\frac{2}{\cosh x} = \frac{4}{e^x + e^{-x}} = \frac{4t}{t^2 + 1}$, quindi l'integrale diventa $\int_1^e \frac{4}{t^2 + 1}\,dt = 4\left(\arctan(e) - \frac\pi4\right) \approx 1{,}7$.
> - $\displaystyle\int \frac{2}{\sinh(x)}\,dx$ (sostituzione $e^x = t$): diventa $\int \frac{4}{t^2 - 1}\,dt = \int \left(\frac{2}{t - 1} - \frac{2}{t + 1}\right)dt = 2\ln\left|\frac{t - 1}{t + 1}\right| + c = 2\ln\left|\frac{e^x - 1}{e^x + 1}\right| + c$ (caso (i) delle funzioni razionali).

_(dispensa, pp. 102–105)_

---

## Calcolo di Aree Piane

Per $f : [a, b] \to \mathbb{R}$ integrabile, $\int_a^b f(x)\,dx$ è l'area tra il grafico e l'asse $x$, ma l'area **sotto** l'asse è negativa. Per calcolare l'area $A$ (geometrica, positiva) di una funzione che cambia segno si divide il dominio in sottointervalli in cui $f$ non cambia segno.

![[AN1-p111-1.png]]

*Figura 58 — Calcolo di aree.* La stessa funzione, che è positiva su $[a, c]$, negativa su $[c, d]$ e positiva su $[d, b]$. A sinistra l'integrale $I = A_1 + A_2 + A_3$ somma le tre aree **con segno** (in rosso la parte negativa). A destra l'area geometrica $A = A_1 - A_2 + A_3$ (tutta gialla): il pezzo sotto l'asse va sottratto, cioè contato con il segno cambiato.

In questo esempio
$$I = \int_a^c f + \int_c^d f + \int_d^b f = \int_a^b f(x)\,dx, \qquad \text{mentre} \qquad A = \int_a^c f - \int_c^d f + \int_d^b f = \int_a^b |f(x)|\,dx.$$

Più in generale, l'area compresa tra i grafici di due funzioni integrabili $f, g$ è
$$A = \int_a^b |f(x) - g(x)|\,dx.$$

![[AN1-p111-2.png]]

*Figura 59 — Calcolo dell'area tra due grafici.* La regione gialla tra la curva superiore $f$ e quella inferiore $g$, da $a$ a $b$: in ogni punto l'altezza della striscia è $|f(x) - g(x)|$, e l'integrale la somma.

> [!example] Esempio: area tra $x^2$ e $\sqrt x$ per $x \in [0, 1]$
> Poiché $x^2 \le \sqrt x$ su $[0, 1]$:
> $$A = \int_0^1 (\sqrt x - x^2)\,dx = \left[\frac23 x^{\frac32} - \frac{x^3}{3}\right]_0^1 = \frac23 - \frac13 = \frac13.$$

![[AN1-p112-1.png]]

*Figura 60 — Esempio: calcolo dell'area tra due grafici.* La "foglia" gialla tra $\sqrt x$ (sopra) e $x^2$ (sotto), che si incontrano in $(0, 0)$ e $(1, 1)$; la sua area è $\frac13$.

Se i grafici si **intersecano**, bisogna trovare le ascisse dei punti di intersezione e spezzare il dominio.

> [!example] Esempio: area tra $f(x) := x^3 - 2x$ e $g(x) := x^2$
> Intersezioni: $x^3 - 2x = x^2 \iff x(x^2 - x - 2) = 0 \iff x = -1, 0, 2$. Inoltre $f \ge g \iff x \in [-1, 0] \cup [2, +\infty)$. Quindi
> $$A = \int_{-1}^0 \big((x^3 - 2x) - x^2\big)\,dx + \int_0^2 \big(x^2 - (x^3 - 2x)\big)\,dx = \left[\frac{x^4}{4} - x^2 - \frac{x^3}{3}\right]_{-1}^0 + \left[\frac{x^3}{3} - \frac{x^4}{4} + x^2\right]_0^2$$
> $$= \left(0 - \left(\tfrac14 - 1 + \tfrac13\right)\right) + \left(\tfrac83 - \tfrac{16}{4} + 4\right) = \frac{5}{12} + \frac{8}{3} = \frac{37}{12}.$$

![[AN1-p112-2.png]]

*Figura 61 — Esempio: calcolo dell'area tra due grafici.* La cubica $f$ (rossa) e la parabola $g$ (verde) si incrociano in $x = -1, 0, 2$. Le due regioni gialle (una piccola a sinistra, dove sta sopra la cubica, e una grande tra $0$ e $2$, dove sta sopra la parabola) hanno area totale $\frac{37}{12}$.

_(dispensa, pp. 105–106)_

---

## Calcolo della Lunghezza di una Curva

L'idea è scomporre la curva in segmenti di lunghezza **infinitesima** e sommarli con l'integrale. Il caso generale si vede in Analisi 2; qui si considerano solo curve date dal grafico di una funzione $f \in C^1[a, b]$.

![[AN1-p113-1.png]]

*Figura 62 — Lunghezza di una curva.* Il grafico di $f$ tra $a$ e $b$; nel riquadro ingrandito un tratto piccolissimo della curva (rosso) è approssimato dall'ipotenusa di un triangolo rettangolo con cateti $dx$ e $dy$, quindi la sua lunghezza è $dl \approx \sqrt{dx^2 + dy^2}$.

Per Pitagora $dl = \sqrt{dx^2 + dy^2}$. Poiché $f'(x) = \frac{dy}{dx}$, "segue" $dy = f'(x)\,dx$ (conti puramente formali, ma che grazie a una notazione ingegnosa portano al risultato giusto), quindi
$$dl = \sqrt{dx^2 + (f'(x))^2 dx^2} = \sqrt{1 + (f'(x))^2}\,dx.$$
Sommando questi segmenti per $x$ tra $a$ e $b$:

> [!important] Lunghezza del grafico
> Per $f : [a, b] \to \mathbb{R}$ derivabile con continuità:
> $$l = \int_a^b \sqrt{1 + (f'(x))^2}\,dx.$$

> [!example] Esempio: la catenaria
> Per $f(x) = \cosh(x)$ su $[a, b]$ (la [[03 - AN1 - Funzioni Reali di una Variabile Reale#Funzioni iperboliche|catenaria]]): $1 + (f'(x))^2 = 1 + \sinh^2(x) = \cosh^2(x)$, e poiché $\cosh > 0$
> $$l = \int_a^b \sqrt{\cosh^2(x)}\,dx = \int_a^b \cosh(x)\,dx = \sinh(b) - \sinh(a).$$
> È uno dei pochi casi in cui la radice si semplifica; di solito l'integrale della lunghezza non è calcolabile esplicitamente.

_(dispensa, pp. 106–107)_

---

## Calcolo di Volumi di Corpi di Rotazione

La stessa idea (scomporre in parti infinitesime e sommarle con l'integrale) serve per calcolare **volumi**: si scompone il solido in sezioni di spessore infinitesimo. Il caso generale è nel [[10 - AN1 - Integrali Multipli#Integrali Tripli|cap. 10]]; qui si considerano solo corpi ottenuti facendo **ruotare attorno all'asse $x$** il grafico di $f : [a, b] \to \mathbb{R}$.

![[AN1-p113-2.png]]

*Figura 63 — Corpo di rotazione.* Ruotando attorno all'asse $x$ il grafico di $y = f(x)$ tra $a$ e $b$ si ottiene un solido (qui una specie di tronco di cono). La fetta scura di spessore $dx$ è un cilindretto: la sua base è un cerchio di raggio $f(x)$.

Ogni fetta è un cilindro di raggio $f(x)$ e altezza $dx$, quindi (con l'area del cerchio $\pi r^2$ calcolata sopra)
$$dV = \pi f^2(x)\,dx \qquad \Rightarrow \qquad \boxed{V = \pi\int_a^b f^2(x)\,dx}.$$

> [!example] Esempi
> - **Cono** di altezza $h$ e raggio di base $r$: $f(x) = \frac rh x$ per $x \in [0, h]$:
> $$V = \pi\int_0^h \left(\frac rh x\right)^2 dx = \pi\frac{r^2}{h^2} \cdot \frac{x^3}{3}\Big|_0^h = \frac{\pi r^2 h}{3}.$$
> - **Sfera** di raggio $r$: $f(x) = \sqrt{r^2 - x^2}$ (integranda pari):
> $$V = \pi\int_{-r}^r (r^2 - x^2)\,dx = 2\pi\left(r^2 x - \frac{x^3}{3}\right)\Big|_0^r = 2\pi\left(r^3 - \frac{r^3}{3}\right) = \frac43\pi r^3.$$

_(dispensa, pp. 107–108)_

---

## Integrali Impropri

Vedi [[Integrale improprio]].

Finora un integrale definito rappresenta un'area tra l'asse $x$ e il grafico
- di una funzione integranda **limitata**,
- su un dominio di integrazione **limitato** $[a, b]$.

Integrali come
$$\int_0^1 \frac{1}{\sqrt x}\,dx \quad (\text{integranda non limitata}) \qquad \text{oppure} \qquad \int_1^{+\infty} \frac{1}{x^2}\,dx \quad (\text{dominio } [1, +\infty) \text{ non limitato})$$
non sono ancora definiti.

![[AN1-p114-1.png]]

*Figura 64 — Integrali impropri.* A sinistra $\frac{1}{\sqrt x}$ su $(0, 1]$: la regione verde è "infinitamente alta" vicino a $x = 0$ (asintoto verticale). A destra $\frac{1}{x^2}$ su $[1, +\infty)$: la regione è "infinitamente lunga" verso destra. In entrambi i casi l'area potrebbe comunque essere finita.

Con il concetto di limite si eliminano facilmente i due vincoli.

> [!important] Definizione 6.8 — Integrale improprio
> Sia $f : [a, b) \to \mathbb{R}$ con $a \in \mathbb{R}$, $b \in \mathbb{R} \cup \{+\infty\}$, integrabile su $[a, c]$ per ogni $a < c < b$. Se converge
> $$\lim_{c\to b^-} \int_a^c f(x)\,dx =: A,$$
> si dice che l'integrale $\int_a^b f(x)\,dx := A$ (**integrale improprio** o **generalizzato**) esiste in senso improprio, o che **converge**. Analogamente per $f : (a, b] \to \mathbb{R}$ con $a \in \mathbb{R} \cup \{-\infty\}$:
> $$\int_a^b f(x)\,dx := \lim_{c\to a^+} \int_c^b f(x)\,dx.$$

Per gli integrali impropri si usa lo stesso linguaggio delle serie: **convergenza**, **divergenza**, ecc. L'idea: si integra su un intervallo "buono" $[a, c]$ e si sposta $c$ verso il punto "critico".

> [!example] Esempio: $\int_1^{+\infty} x^r\,dx$ per $r \in \mathbb{R}$
> - $r = -1$: $\int_1^c \frac1x\,dx = \ln(c) - \ln(1) \to +\infty$ per $c \to +\infty$: l'integrale $\int_1^{+\infty} \frac1x\,dx = +\infty$ **diverge**.
> - $r \neq -1$:
> $$\int_1^c x^r\,dx = \frac{x^{r+1}}{r+1}\Big|_1^c = \frac{c^{r+1}}{r+1} - \frac{1}{r+1} \xrightarrow{c\to+\infty} \begin{cases} -\frac{1}{r+1} & r + 1 < 0 \iff r < -1, \\ +\infty & r + 1 > 0 \iff r > -1. \end{cases}$$
> Quindi
> $$\int_1^{+\infty} x^r\,dx = \begin{cases} -\frac{1}{r+1} & r < -1, \\ +\infty & r \ge -1. \end{cases} \qquad \text{Es. } \int_1^{+\infty} \frac{1}{x^2}\,dx = -\frac{1}{-2 + 1} = 1.$$

![[AN1-p115-1.png]]

*Figura 65 — Integrali impropri.* A sinistra $\frac1x$ su $[1, +\infty)$: l'area rossa è infinita. A destra $\frac{1}{x^2}$: l'area verde, pur estendendosi all'infinito, vale esattamente $1$. Le due curve sembrano simili, ma $\frac{1}{x^2}$ va a zero abbastanza in fretta.

> [!example] Esempio: $\int_0^1 x^r\,dx := \lim_{c\to0^+}\int_c^1 x^r\,dx$
> (Il limite serve solo per $r < 0$, quando $x^r$ non è limitata vicino a $0$.)
> - $r = -1$: $\int_c^1 \frac1x\,dx = \ln(1) - \ln(c) \to -(-\infty) = +\infty$ per $c \to 0^+$: **diverge**.
> - $r \neq -1$:
> $$\int_c^1 x^r\,dx = \frac{1}{r+1} - \frac{c^{r+1}}{r+1} \xrightarrow{c\to0^+} \begin{cases} \frac{1}{r+1} & r > -1, \\ +\infty & r < -1. \end{cases}$$
> Quindi
> $$\int_0^1 x^r\,dx = \begin{cases} \frac{1}{r+1} & r > -1, \\ +\infty & r \le -1. \end{cases} \qquad \text{Es. } \int_0^1 \frac{1}{\sqrt x}\,dx = \frac{1}{-\frac12 + 1} = 2.$$

![[AN1-p116-1.png]]

*Figura 66 — Integrali impropri.* Su $(0, 1]$ la situazione si rovescia: l'area sotto $\frac1x$ (rossa) è infinita, quella sotto $\frac{1}{\sqrt x}$ (verde) vale $2$, perché $\frac{1}{\sqrt x}$ esplode più lentamente vicino a $0$.

> [!tip] Come ricordarlo
> | | $\int_1^{+\infty} \frac{1}{x^\alpha}\,dx$ (all'infinito) | $\int_0^1 \frac{1}{x^\alpha}\,dx$ (vicino a 0) |
> |---|---|---|
> | converge | $\alpha > 1$ | $\alpha < 1$ |
> | diverge | $\alpha \le 1$ | $\alpha \ge 1$ |
>
> $\frac1x$ è il caso limite e diverge da entrambe le parti.

_(dispensa, pp. 108–110)_

### Criterio del confronto per integrali impropri

Per $x^r$ era facile trovare una primitiva, ma integrare esplicitamente può essere difficile o impossibile.

> [!question] Problema
> Come si studia la convergenza di un integrale improprio **senza** conoscere una primitiva? (È lo stesso problema incontrato per le [[02 - AN1 - Serie Numeriche#Condizione necessaria|serie]] senza una formula per le somme parziali.) Non si chiede più il valore, solo che esista finito.

> [!important] Teorema 6.9 — Confronto per gli integrali impropri
> Siano $f, g : [a, b) \to \mathbb{R}$ con $a \in \mathbb{R}$, $b \in \mathbb{R} \cup \{+\infty\}$, integrabili su $[a, c]$ per ogni $a < c < b$. Se
> - $|f(x)| \le g(x)$ per ogni $x \in [a, b)$ ($g$ è un **maggiorante** di $|f|$), e
> - $\int_a^b g(x)\,dx$ converge,
>
> allora converge anche $\int_a^b f(x)\,dx$. Lo stesso vale per $f, g : (a, b]$ con $a \in \mathbb{R} \cup \{-\infty\}$.

> [!example] Esempio: $\int_{-\infty}^{+\infty} e^{-x^2}\,dx$ (campana di Gauss)
> Qui **entrambi** gli estremi sono "critici" (infiniti, oppure un asintoto verticale). In questi casi si spezza l'integrale in un punto intermedio; per simmetria conviene $c = 0$:
> $$\int_{-\infty}^{+\infty} e^{-x^2}\,dx := \int_{-\infty}^0 e^{-x^2}\,dx + \int_0^{+\infty} e^{-x^2}\,dx.$$
> Poiché $e^{-x^2}$ è pari, $\int_{-\infty}^{+\infty} = 2\int_0^{+\infty}$: basta studiare $[0, +\infty)$. Inoltre $\int_0^{+\infty} = \int_0^1 + \int_1^{+\infty}$, e il primo è un integrale definito (finito): basta un maggiorante per $x \ge 1$. Per $x \ge 1$:
> $$|f(x)| = e^{-x^2} \le 2x e^{-x^2} =: g(x), \qquad \int_1^c 2x e^{-x^2}\,dx = -e^{-x^2}\Big|_1^c = e^{-1} - e^{-c^2} \to e^{-1}.$$
> Quindi $\int_1^{+\infty} g$ converge, e per il confronto converge anche $\int_1^{+\infty} e^{-x^2}\,dx$, e di conseguenza $\int_{-\infty}^{+\infty} e^{-x^2}\,dx$.

![[AN1-p117-1.png]]

*Figura 67 — Integrale improprio della "Campana di Gauss".* Il grafico di $e^{-x^2}$, simmetrico con massimo $1$ in $0$, che scende rapidissimamente a zero da entrambe le parti. L'area gialla, estesa a tutta la retta, vale $\sqrt\pi$.

Si dimostrerà (con gli [[10 - AN1 - Integrali Multipli#Cambiamento di Variabili negli Integrali Doppi|integrali doppi in coordinate polari]]) che
$$\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt\pi.$$
È il risultato che fa funzionare la [[Gaussian|distribuzione normale]]: la costante $\frac{1}{\sqrt{2\pi}}$ nella sua densità serve proprio a rendere l'area totale uguale a 1.

> [!example] Esempio: $\int_0^{+\infty} \frac{\sin(x)}{x}\,dx$ converge
> Poiché $\lim_{x\to0^+} \frac{\sin x}{x} = 1$, solo l'estremo $+\infty$ è "critico": basta studiare $[1, +\infty)$. Integrando per parti ($f = \frac1x$, $g' = \sin$):
> $$\int_1^c \frac1x\sin(x)\,dx = \frac1x(-\cos(x))\Big|_1^c - \int_1^c \frac{-1}{x^2}(-\cos(x))\,dx = \underbrace{\cos(1) - \frac{\cos(c)}{c}}_{\to \cos(1)} - \int_1^c \frac{\cos(x)}{x^2}\,dx.$$
> Quindi l'integrale converge se e solo se converge $\int_1^{+\infty} \frac{\cos x}{x^2}\,dx$, e qui il maggiorante è facile:
> $$\left|\frac{\cos(x)}{x^2}\right| \le \frac{1}{x^2}, \qquad \int_1^{+\infty} \frac{1}{x^2}\,dx \text{ converge}.$$
> Era necessario
> - integrare una volta per parti (alzando il grado del denominatore da $x$ a $x^2$), perché $\int_1^{+\infty} \frac1x\,dx = +\infty$ e $\left|\frac{\sin x}{x}\right| \le \frac1x$ non basta;
> - considerare $[1, +\infty)$ e non $[0, +\infty)$, perché $\int_0^{+\infty} \frac{1}{x^2}\,dx = +\infty$ (diverge vicino a $0$).

![[AN1-p118-1.png]]

*Figura 68 — Integrale improprio convergente.* Il grafico di $\frac{\sin x}{x}$ tra $0$ e $30$: vale $1$ in $0$ e poi oscilla con ampiezza che decresce come $\frac1x$. Le aree verdi (positive) e rosse (negative) si alternano e diventano sempre più piccole: si compensano come i termini di una [[02 - AN1 - Serie Numeriche#Criterio di Leibniz|serie di Leibniz]], e il totale converge (vale $\frac\pi2$). Nota che invece $\int_0^{+\infty} \left|\frac{\sin x}{x}\right| dx = +\infty$: la convergenza non è "assoluta".

_(dispensa, pp. 110–112)_

### Integrali impropri e serie

Vedi [[Criterio integrale per le serie]].

Spesso i termini di una serie $\sum_{k=1}^{+\infty} a_k$ sono i valori di una funzione $f : [1, +\infty) \to \mathbb{R}$ negli interi: $a_k = f(k)$.

![[AN1-p119-1.png]]

*Figura 69 — Integrali impropri e serie: $f(k) = a_k$.* Il grafico di una funzione decrescente $f$; nei punti $x = 1, 2, 3, \dots$ i suoi valori sono i termini $a_1, a_2, a_3, \dots$ della serie (le frecce collegano le altezze ai termini).

Che legame c'è tra $\sum_{k=1}^{+\infty} f(k)$ e $\int_1^{+\infty} f(x)\,dx$? Interpretando la somma della serie come un'area:

> [!important] Teorema 6.10 — Criterio integrale per le serie
> Se $f : [1, +\infty) \to [0, +\infty)$ è **decrescente** e $a_k := f(k)$, allora
> $$\sum_{k=1}^{+\infty} a_k \text{ converge} \iff \int_1^{+\infty} f(x)\,dx \text{ converge}.$$

**Dimostrazione.** "$\Rightarrow$": dal grafico seguente

![[AN1-p119-2.png]]

*Figura 70 — La serie maggiora l'integrale.* Su ogni intervallo $[k, k+1]$ si disegna un rettangolo di base 1 e altezza $a_k = f(k)$ (il valore all'estremo **sinistro**). Poiché $f$ è decrescente, il rettangolo sta sopra la curva: la somma delle aree dei rettangoli (verde chiaro) supera l'area sotto la curva (verde scuro).

segue
$$F(c) := \int_1^c f(s)\,ds \le \sum_{k=1}^{+\infty} a_k \qquad \forall c \ge 1.$$
$F$ è crescente (perché $f \ge 0$) e limitata, quindi per il [[03 - AN1 - Funzioni Reali di una Variabile Reale#Limiti di funzioni monotone|teorema sui limiti delle funzioni monotone]] converge $\lim_{c\to+\infty} F(c) = \int_1^{+\infty} f(x)\,dx$.

"$\Leftarrow$": se l'integrale improprio converge, dal grafico seguente

![[AN1-p120-1.png]]

*Figura 71 — L'integrale maggiora la serie.* Ora su $[k-1, k]$ si disegna il rettangolo di altezza $a_k = f(k)$ (valore all'estremo **destro**): per la decrescenza sta sotto la curva. Quindi $a_2 + a_3 + \ldots$ è minore dell'area sotto la curva da $1$ in poi; il primo termine $a_1$ (rettangolo su $[0, 1]$) va aggiunto a parte.

segue
$$s_n := \sum_{k=1}^n a_k \le a_1 + \int_1^{+\infty} f(x)\,dx \qquad \forall n.$$
La serie è a termini positivi con somme parziali limitate, quindi converge ([[02 - AN1 - Serie Numeriche#Serie a Termini Positivi|Teorema 2.3]]). $\square$

> [!example] Serie armonica generalizzata $\sum_{k=1}^{+\infty} \frac{1}{k^\alpha}$
> Per $\alpha \le 0$ la successione $\frac{1}{k^\alpha}$ non è infinitesima, quindi la serie diverge a $+\infty$. Per $\alpha > 0$, $f(x) = x^{-\alpha}$ ($x \ge 1$) è derivabile con $f'(x) = -\alpha x^{-\alpha-1} < 0$, quindi decrescente, e per il criterio integrale
> $$\sum_{k=1}^{+\infty} \frac{1}{k^\alpha} \text{ converge} \iff \int_1^{+\infty} \frac{1}{x^\alpha}\,dx \text{ converge} \iff \alpha > 1,$$
> dove la seconda equivalenza è il calcolo di $\int_1^{+\infty} x^r\,dx$ con $r = -\alpha$. È la dimostrazione della [[02 - AN1 - Serie Numeriche#Serie armonica generalizzata|Proposizione 2.8]], lasciata in sospeso nel cap. 2.

Si può quindi definire
$$\zeta : (1, +\infty) \to \mathbb{R}, \qquad \zeta(s) := \sum_{k=1}^{+\infty} \frac{1}{k^s},$$
la **funzione zeta di Riemann**, legata all'**ipotesi di Riemann**, uno dei problemi aperti più importanti della matematica.

_(dispensa, pp. 113–114)_
