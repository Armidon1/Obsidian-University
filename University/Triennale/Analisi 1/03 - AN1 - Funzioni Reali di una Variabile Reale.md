---
title: Funzioni Reali di una Variabile Reale
aliases:
  - AN1 — Funzioni Reali di una Variabile Reale
tags:
  - analisi-1
  - funzioni
  - funzione-inversa
  - funzioni-elementari
  - limiti-di-funzioni
  - limiti-notevoli
  - asintoti
source: Appunti di Analisi Matematica 1 di Camilli.pdf (cap. 3)
---

# Funzioni Reali di una Variabile Reale

> [!abstract]
> Il capitolo passa dalle successioni (funzioni definite su $\mathbb{N}$) alle **funzioni reali di una variabile reale**, definite su sottoinsiemi di $\mathbb{R}$. Prima costruisce gli strumenti: **operazioni** e **composizione** tra funzioni, proprietà come **iniettività/suriettività** e **funzione inversa**, **limitatezza**, **simmetria** (pari/dispari), **monotonia**, **periodicità**. Poi introduce il catalogo delle **funzioni elementari**: polinomi, funzioni razionali, **potenze ed esponenziali** (definite rigorosamente con i limiti), **funzioni iperboliche** e **circolari**. Infine definisce il **limite di una funzione** tramite le [[01 - AN1 - Successioni Numeriche|successioni]], con limiti destro/sinistro, **asintoti** e i **tre limiti notevoli**.
> Il capitolo prepara le [[04 - AN1 - Funzioni Continue|funzioni continue]] (cap. 4), dove si costruiranno le inverse di esponenziale e funzioni circolari, e la [[05 - AN1 - Calcolo Differenziale|derivata]] (cap. 5), che è un limite.
> Mappa del corso: [[MOC - Analisi 1]].

---

## Funzioni reali e grafico

> [!important] Definizione 3.1 — Funzione reale di una variabile reale
> Una funzione $f : X \subseteq \mathbb{R} \to Y \subseteq \mathbb{R}$ si dice **funzione reale di una variabile reale**.

In questo caso il [[00 - AN1 - Concetti Fondamentali#Funzioni|grafico]]
$$G(f) = \{(x, f(x)) : x \in X\} \subset \mathbb{R}^2$$
si può disegnare nel piano $xy$: è questo che rende le funzioni reali così "visibili".

> [!example] Esempio: area del cerchio
> $A(r) :=$ area di un cerchio di raggio $r \ge 0$ definisce una funzione $A : [0, +\infty) \to \mathbb{R}$ con immagine $A([0, +\infty)) = [0, +\infty)$. Poiché $A(r) = \pi r^2$, il grafico è (parte di) una parabola.

![[AN1-p034-1.png]]

*Figura 11 — Grafico di $A(r)$.* Il ramo di parabola $A(r) = \pi r^2$ per $r \in [0, 3]$: parte da $0$ e cresce sempre più rapidamente (per $r = 3$ vale $9\pi \approx 28{,}3$). Il fatto che sia definita solo per $r \ge 0$ si vede dal grafico, che non ha la metà sinistra della parabola.

_(dispensa, p. 28)_

---

## Operazioni e Composizione tra Funzioni

### Somma, differenza, prodotto e frazione

Le operazioni algebriche si estendono dai numeri alle funzioni **punto per punto**. Se $f : X_1 \to \mathbb{R}$ e $g : X_2 \to \mathbb{R}$, su $X := X_1 \cap X_2$ (dove sono definite entrambe):

- **somma** $(f + g)(x) := f(x) + g(x)$;
- **differenza** $(f - g)(x) := f(x) - g(x)$;
- **prodotto** $(f \cdot g)(x) := f(x) \cdot g(x)$;
- **frazione** $\frac{f}{g}(x) := \frac{f(x)}{g(x)}$, ma solo su $X_0 := \{z \in X : g(z) \neq 0\}$.

### Composizione di funzioni

> [!important] Funzione composta
> Se $f : X \to Y$ e $g : Y \to Z$, la funzione
> $$g \circ f : X \to Z, \qquad (g \circ f)(x) := g(f(x))$$
> si dice **funzione composta** di $f$ e $g$ (si legge "$g$ composto $f$": si applica **prima** $f$, poi $g$).

> [!example] Esempio
> Con $f(x) = |x|$ e $g(x) = \sin(x)$:
> - $(g \circ f)(x) = \sin|x|$;
> - $(f \circ g)(x) = |\sin(x)|$.
>
> Le due funzioni sono diverse: ad esempio in $x = \frac{3\pi}{2}$ si ha $\sin\left|\frac{3\pi}2\right| = -1$, mentre $\left|\sin\left(\frac{3\pi}2\right)\right| = 1$ (la seconda non è mai negativa). In generale $f \circ g \neq g \circ f$: la composizione **non è commutativa**.

_(dispensa, p. 28)_

---

## Proprietà di Funzioni Reali

### Funzioni invertibili

Vedi [[Funzione iniettiva, suriettiva e biettiva]].

> [!important] Definizione 3.2
> $f : X \to Y$ si dice
> - **iniettiva** se per ogni $x_1, x_2 \in X$ con $x_1 \neq x_2$ si ha $f(x_1) \neq f(x_2)$, cioè se per ogni $y \in Y$ esiste **al più** un $x \in X$ con $f(x) = y$;
> - **suriettiva** se per ogni $y \in Y$ esiste **almeno** un $x \in X$ con $f(x) = y$ (cioè $f(X) = Y$);
> - **biettiva** se è iniettiva e suriettiva, cioè se per ogni $y \in Y$ esiste **un unico** $x \in X$ con $f(x) = y$.

Le proprietà dipendono non solo dalla formula, ma anche da **dominio** e **codominio**, come mostra l'esempio seguente.

> [!example] Esempio: $f_k(x) := x^2$ con domini e codomini diversi
> **(a)** $X_1 = \mathbb{R}$, $Y_1 = \mathbb{R}$:
> - per $y > 0$ ci sono due controimmagini $x_1 = -\sqrt y \neq x_2 = +\sqrt y$ con $x_1^2 = x_2^2 = y$: **non iniettiva**;
> - per $y < 0$ nessun $x$ ha $x^2 = y$: **non suriettiva**.
>
> **(b)** $X_2 = \mathbb{R}$, $Y_2 = [0, +\infty)$:
> - per $y > 0$ ancora due controimmagini $\pm\sqrt y$: **non iniettiva**;
> - per ogni $y \in Y_2$, $x := \sqrt y$ dà $f_2(x) = y$: **suriettiva**.
>
> **(c)** $X_3 = [0, +\infty)$, $Y_3 = \mathbb{R}$: per $y \ge 0$ l'unica controimmagine è $\sqrt y$, per $y < 0$ non ce ne sono: **iniettiva ma non suriettiva**.
>
> **(d)** $X_4 = [0, +\infty)$, $Y_4 = [0, +\infty)$: per ogni $y \in Y_4$, $x = \sqrt y$ è l'unico $x$ con $x^2 = y$: **biettiva**.

> [!warning] Correzione
> Nel caso (b) la dispensa scrive "$f_2(x) = x^2 = y$ e quindi $f_1$ è suriettiva": si tratta di un refuso, la funzione suriettiva è $f_2$ (la $f_1$ del caso (a) non lo è).

Sul grafico le tre proprietà si leggono con le **rette orizzontali** $y = \text{cost}$, per $y \in Y$:

| Proprietà | Ogni retta orizzontale per $y \in Y$ interseca $G(f)$ |
|---|---|
| iniettiva | **al più** una volta |
| suriettiva | **almeno** una volta |
| biettiva | **esattamente** una volta |

![[AN1-p036-1.png]]

*Figura 12 — Funzione (a) non iniettiva, non suriettiva; (b) non iniettiva ma suriettiva; (c) iniettiva ma non suriettiva; (d) iniettiva e suriettiva cioè biettiva.* I quattro grafici corrispondono ai quattro casi dell'esempio. In (a) la retta $y > 0$ taglia la parabola in due punti $x_1, x_2$ e la retta $y < 0$ non la taglia mai. In (b) il codominio è $[0, +\infty)$: la retta $y < 0$ non va più considerata, ma la retta $y > 0$ taglia ancora due volte. In (c) resta solo il ramo destro: una sola intersezione per $y > 0$, nessuna per $y < 0$. In (d) ogni retta orizzontale del codominio taglia il grafico esattamente una volta.

### Funzione inversa

Vedi [[Funzione inversa]].

- $f : X \to Y$ è biettiva **se e solo se** esiste $g : Y \to X$ con
  - $(g \circ f)(x) = g(f(x)) = x$ per ogni $x \in X$, e
  - $(f \circ g)(y) = f(g(y)) = y$ per ogni $y \in Y$.

  In tal caso $g$ è unica, si chiama **funzione inversa** di $f$ e si indica con $f^{-1} := g$. L'inversa "disfa" ciò che fa $f$.
- Poiché $f(x) = y \iff x = f^{-1}(y)$, il punto $(x, y)$ sta su $G(f)$ se e solo se $(y, x)$ sta su $G(f^{-1})$: i grafici di $f$ e $f^{-1}$ sono **simmetrici rispetto alla bisettrice** $y = x$.

> [!example] Esempio
> $f : [0, +\infty) \to [0, +\infty)$, $f(x) := x^2$ è biettiva (caso (d)), con inversa $f^{-1} : [0, +\infty) \to [0, +\infty)$, $f^{-1}(x) = \sqrt x$.

> [!warning] $f^{-1}$ non è $\frac1f$
> In particolare $f^{-1}(x) = \sqrt x \neq \frac{1}{f(x)} = \frac{1}{x^2}$. L'esponente $-1$ indica l'inversa rispetto alla **composizione**, non al prodotto.

![[AN1-p036-2.png]]

*Figura 13 — Grafico di $f(x) = x^2$ e $f^{-1}(x) = \sqrt x$.* In blu la parabola $x^2$, in rosso la radice $\sqrt x$, tratteggiata la bisettrice $y = x$. Le due curve sono una lo specchio dell'altra rispetto alla bisettrice e si incontrano sulla bisettrice nei punti $(0,0)$ e $(1,1)$.

_(dispensa, pp. 29–30)_

### Funzioni limitate

$f : X \to \mathbb{R}$ si dice
- **limitata superiormente** se esiste $M$ con $f(x) \le M$ per ogni $x \in X$;
- **limitata inferiormente** se esiste $m$ con $m \le f(x)$ per ogni $x \in X$;
- **limitata** se entrambe: $m \le f(x) \le M$ per ogni $x$.

In altre parole: l'immagine $f(X)$ è un insieme [[00 - AN1 - Concetti Fondamentali#Maggioranti ed estremo superiore|limitato]] (superiormente, inferiormente o entrambi).

> [!example] Esempi
> - $f(x) = x^2$ su $\mathbb{R}$: inferiormente limitata (da 0) ma non superiormente.
> - $f(x) = x^3$ su $\mathbb{R}$: né inferiormente né superiormente limitata.
> - $f(x) = \sin(x)$ su $\mathbb{R}$: limitata, $-1 \le \sin(x) \le 1$ (vedi le [[#Funzioni circolari|funzioni circolari]]).

### Funzioni simmetriche

Vedi [[Funzioni pari e dispari]].

Sia $X \subseteq \mathbb{R}$ **simmetrico** rispetto a $0$ ($x \in X \Rightarrow -x \in X$). $f : X \to \mathbb{R}$ si dice
- **pari** se $f(-x) = f(x)$ per ogni $x \in X$;
- **dispari** se $f(-x) = -f(x)$ per ogni $x \in X$.

Osservazioni:
- $f$ pari $\iff$ grafico **simmetrico rispetto all'asse $y$**;
- $f$ dispari $\iff$ grafico **simmetrico rispetto all'origine**;
- se $f$ è dispari e $0 \in X$, allora $f(0) = 0$ (perché $f(0) = -f(0)$);
- regole per prodotto e rapporto (p = pari, d = dispari), come per i segni $+$ e $-$:

| $f_1 \cdot f_2$ oppure $\frac{f_1}{f_2}$ | $f_1$ = p | $f_1$ = d |
|---|---|---|
| $f_2$ = p | p | d |
| $f_2$ = d | d | p |

- inoltre pari $\pm$ pari = pari e dispari $\pm$ dispari = dispari.

![[AN1-p037-1.png]]

*Figura 14 — Funzione pari e dispari.* A sinistra una funzione pari (una "W" simmetrica rispetto all'asse $y$: la metà sinistra è lo specchio della destra). A destra una funzione dispari, che passa per l'origine: ruotando il grafico di $180°$ attorno all'origine si ritrova lo stesso grafico.

> [!example] Esempi
> - $x^2$ è pari, $x^3$ è dispari. In generale $x^n$ ($n \in \mathbb{N}$) è pari $\iff$ $n$ è pari, dispari $\iff$ $n$ è dispari (da qui i nomi).
> - $f(x) = 3x^4 - 2x^2 + 4$ è pari, $g(x) = -5x^3 - 2x$ è dispari, quindi $r(x) = \frac{f(x)}{g(x)} = \frac{3x^4 - 2x^2 + 4}{-5x^3 - 2x}$ è dispari.

> [!tip] A cosa serve
> Una funzione pari o dispari si può studiare solo per $x \ge 0$ e poi completare il grafico per simmetria. Tornerà utile negli integrali su intervalli simmetrici ([[06 - AN1 - Calcolo Integrale#Integrale, definizione e prime proprietà|cap. 6]]).

### Funzioni monotone

Siano $x_1, x_2 \in X$ con $x_1 < x_2$. $f$ si dice
- **crescente** se $f(x_1) \le f(x_2)$;
- **strettamente crescente** se $f(x_1) < f(x_2)$;
- **decrescente** se $f(x_1) \ge f(x_2)$;
- **strettamente decrescente** se $f(x_1) > f(x_2)$;
- **(strettamente) monotona** se è (strettamente) crescente oppure (strettamente) decrescente.

> [!example] Esempi
> - $x^3$ su $\mathbb{R}$ è strettamente crescente.
> - $x^2$ su $\mathbb{R}$ non è monotona; $x^2$ su $(-\infty, 0]$ è decrescente.

Una funzione strettamente monotona è iniettiva (se $x_1 \neq x_2$, uno dei due è più piccolo e i valori sono diversi). Il viceversa vale per le funzioni continue su intervalli ([[04 - AN1 - Funzioni Continue#Continuità della funzione inversa|cap. 4]]).

### Funzioni periodiche

Sia $T > 0$ con $x + T \in X$ per ogni $x \in X$. $f$ si dice **periodica di periodo $T$** se $T$ è il più piccolo numero $> 0$ tale che $f(x + T) = f(x)$ per ogni $x \in X$. Ad esempio $\sin(x)$ è periodica di periodo $T = 2\pi$.

_(dispensa, pp. 30–31)_

---

## Funzioni Elementari

Segue il catalogo delle funzioni elementari usate in tutto il corso.

### Polinomi e funzioni razionali

> [!important] Polinomio
> Se $a_0, a_1, \dots, a_n \in \mathbb{R}$, l'espressione
> $$p(x) := a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0, \qquad x \in \mathbb{R},$$
> si dice **polinomio**. Se $a_n \neq 0$, $n$ è il **grado** di $p$. Un polinomio della forma $p(x) = ax^n$ si dice **monomio**.

Esempio: $p(x) = 2x^3 - 5x^2 - 6x + 1$ ha grado $3$.

> [!important] Funzione razionale
> Se $p$ e $q \neq 0$ sono polinomi di grado $n$ e $m$, l'espressione
> $$r(x) = \frac{p(x)}{q(x)}$$
> si chiama **funzione razionale** di grado $n - m$, con dominio $X = \{x \in \mathbb{R} : q(x) \neq 0\}$.

> [!example] Esempio
> $r(x) = \dfrac{2x^2 - 1}{2x^5 - 10x^3 + 8x}$ ha grado $2 - 5 = -3$. Il dominio si trova annullando il denominatore: $2x^5 - 10x^3 + 8x = 2x(x^4 - 5x^2 + 4) = 2x(x^2 - 1)(x^2 - 4)$, quindi $X = \mathbb{R} \setminus \{-2, -1, 0, 1, 2\}$.

Il grado di una funzione razionale ne determina il comportamento per $x \to \pm\infty$ (grado negativo: tende a 0), esattamente come per i rapporti di polinomi nelle [[01 - AN1 - Successioni Numeriche#Regole per il Calcolo dei Limiti|successioni]].

_(dispensa, p. 31)_

### Potenze ed esponenziali

Vedi [[Funzione esponenziale]].

> [!question] Problema
> Come si definisce $a^r$ per $a > 0$ e $r \in \mathbb{R}$? Ad esempio, quanto vale $2^\pi$?

Per $r \in \mathbb{N}$ basta moltiplicare $a$ per sé stesso $r$ volte, ma "moltiplicare $2$ per sé stesso $\pi$ volte" non ha senso. La definizione rigorosa usa i risultati del [[01 - AN1 - Successioni Numeriche|cap. 1]] in due passi.

**1° passo: $r = \frac pq \in \mathbb{Q}$** (con $p \in \mathbb{Z}$, $0 \neq q \in \mathbb{N}$). Con le radici costruite dal [[01 - AN1 - Successioni Numeriche#Il metodo di Erone|metodo di Erone]]:
$$a^r = a^{\frac pq} := (a^p)^{\frac1q} = \sqrt[q]{a^p} = \left(\sqrt[q]a\right)^p.$$
Ad esempio $a^{-\frac34} := \sqrt[4]{a^{-3}} = \left(\frac{1}{\sqrt[4]a}\right)^3$ e $2^{3{,}141} := \sqrt[1000]{2^{3141}} = \left(\sqrt[1000]2\right)^{3141}$. Per definire $\sqrt[q]a$ con $q$ pari serve $a > 0$.

**2° passo: $r \in \mathbb{R}$** (per semplicità $a > 1$ e $r > 0$; gli altri casi sono simili). Se $r = p{,}\alpha_0\alpha_1\alpha_2\ldots$, si troncano le cifre:
$$r_n := p{,}\alpha_0\alpha_1\ldots\alpha_n000\ldots = \frac{p\alpha_0\alpha_1\ldots\alpha_n}{10^{n+1}} \in \mathbb{Q}.$$
Ad esempio per $r = \pi$: $r_2 = 3{,}141 = \frac{3141}{1000}$. La successione $(r_n)$ ha queste proprietà:
- $r_n \in \mathbb{Q}$ e $r_n \in [p, p+1]$ per ogni $n$;
- $r_n \to r$, perché $0 \le r - r_n = 0{,}0\ldots0\alpha_{n+1}\alpha_{n+2}\ldots \le 10^{-n} \to 0$;
- $(r_n)$ è crescente.

Poiché $r_n \in \mathbb{Q}$, $a_n := a^{r_n}$ è definito dal 1° passo. Siccome $x \mapsto a^x$ su $\mathbb{Q}$ è crescente per $a > 1$, la successione $(a_n)$ è
- **crescente** (perché $(r_n)$ lo è), e
- **limitata** ($a_n \in [a^p, a^{p+1}]$).

Per il [[01 - AN1 - Successioni Numeriche#Successioni monotone|teorema sulle successioni monotone]] il limite esiste, e si pone
$$a^r := \lim_{n\to+\infty} a^{r_n}.$$

> [!example] Esempio numerico
> $2^\pi$ è il limite di $2^3 = 8$, $2^{3{,}1} \approx 8{,}57$, $2^{3{,}14} \approx 8{,}815$, $2^{3{,}141} \approx 8{,}821$, … $\to 2^\pi = 8{,}8249\ldots$

> [!important] Proposizione 3.3 — Regole per le potenze
> - $a^r \cdot a^s = a^{r+s}$ per ogni $a > 0$, $r, s \in \mathbb{R}$;
> - $(a^r)^s = a^{r \cdot s}$ per ogni $a > 0$, $r, s \in \mathbb{R}$;
> - $a^r \cdot b^r = (a \cdot b)^r$ per ogni $a, b > 0$, $r \in \mathbb{R}$.

Fissando la base e variando l'esponente, o viceversa, si ottengono due funzioni elementari diverse.

> [!important] Definizione 3.4 — Funzione potenza ed esponenziale
> - $f : (0, +\infty) \to \mathbb{R}$, $f(x) := x^r$ con $r \in \mathbb{R}$ fisso: **funzione potenza** di esponente $r$ (variabile alla base).
> - $g : \mathbb{R} \to \mathbb{R}$, $g(x) := a^x$ con $a > 0$ fisso: **funzione esponenziale** di base $a$ (variabile all'esponente).

Per $r \ge 0$ la potenza si estende a $[0, +\infty)$ con $0^r := 0$ (per $r > 0$). Per certi $r$ si definisce $x^r$ anche per $x < 0$: ad esempio $x^2 = x \cdot x$ oppure $(-8)^{\frac13} = \sqrt[3]{-8} = -2$.

![[AN1-p039-1.png]]

*Figura 15 — La funzione potenza.* I grafici di $x^r$ per $x > 0$ al variare di $r$. Tutti passano per $(1, 1)$, perché $1^r = 1$. Per $r > 1$ (verde) la curva cresce sempre più rapidamente; per $r = 1$ (blu) è la bisettrice; per $0 < r < 1$ (viola, es. $\sqrt x$) cresce sempre più lentamente; per $r = 0$ è la costante $1$; per $r < 0$ (rosso, es. $\frac1x$) è decrescente e tende a $+\infty$ per $x \to 0^+$.

![[AN1-p039-2.png]]

*Figura 16 — Funzione esponenziale di base $a$ e funzione esponenziale.* A sinistra $a^x$ per diverse basi: per $a > 1$ (blu) è crescente, per $0 < a < 1$ (rosso) è decrescente, per $a = 1$ (verde) è la costante $1$; tutte passano per $(0, 1)$ perché $a^0 = 1$, e sono sempre positive. Le curve di base $a$ e $\frac1a$ sono simmetriche rispetto all'asse $y$, perché $\left(\frac1a\right)^x = a^{-x}$. A destra il grafico di $e^x$, che vale $1$ in $0$ e circa $4{,}48$ in $1{,}5$.

L'esponenziale più importante è quello di base $a = e$ ([[Numero di Nepero]]), chiamato semplicemente **funzione esponenziale**: è una delle funzioni più importanti della matematica, perché è l'unica (a meno di costanti) uguale alla propria derivata ([[05 - AN1 - Calcolo Differenziale#Regole per la Derivazione|cap. 5]]).

_(dispensa, pp. 32–33)_

### Funzioni iperboliche

Vedi [[Funzioni iperboliche]].

Con l'esponenziale si definiscono tre nuove funzioni su $\mathbb{R}$:

- **coseno iperbolico**: $\cosh(x) := \dfrac{e^x + e^{-x}}{2}$;
- **seno iperbolico**: $\sinh(x) := \dfrac{e^x - e^{-x}}{2}$;
- **tangente iperbolica**: $\tanh(x) := \dfrac{\sinh(x)}{\cosh(x)}$.

![[AN1-p039-3.png]]

*Figura 17 — Le funzioni iperboliche.* A sinistra $\tanh(x)$: una curva a "S" che passa per l'origine ed è compresa tra le rette tratteggiate $y = -1$ e $y = 1$, a cui si avvicina per $x \to \mp\infty$. A destra $\cosh(x)$ (a forma di "U", con minimo $1$ in $x = 0$) e $\sinh(x)$ (crescente, passa per l'origine): per $x$ grande le due curve quasi coincidono, perché il termine $e^{-x}$ diventa trascurabile.

Osservazioni:
- $\cosh$ è **pari** e inferiormente limitata: $\cosh(x) \ge 1$, in particolare $\cosh(x) \neq 0$ per ogni $x$ (quindi $\tanh$ è definita ovunque). Il suo grafico si chiama anche **catenaria**: è la forma di una catena che pende sotto il proprio peso.

![[AN1-p039-4.png]]

*Figura 18 — La catenaria.* Una foto di una catena appesa tra due paletti: la curva che descrive è il grafico di un coseno iperbolico (opportunamente riscalato), non di una parabola come si potrebbe pensare.

- $\sinh$ è **dispari** e strettamente crescente.
- $\tanh$ è **dispari**, strettamente crescente e limitata: $-1 \le \tanh(x) \le 1$.
- Vale la relazione fondamentale
$$\cosh^2(x) - \sinh^2(x) = 1 \qquad \forall x \in \mathbb{R}.$$
(Basta sviluppare: $\frac{(e^x + e^{-x})^2 - (e^x - e^{-x})^2}{4} = \frac{4}{4} = 1$.) È l'analogo di $\cos^2 + \sin^2 = 1$: il punto $(\cosh t, \sinh t)$ percorre un ramo dell'**iperbole** $x^2 - y^2 = 1$, da cui il nome.

_(dispensa, p. 33)_

### Funzioni circolari

Vedi [[Funzioni circolari]].

Per definire le funzioni circolari bisogna prima misurare gli angoli in **radianti**.

![[AN1-p040-1.png]]

*Figura 19 — Misura di angoli in radianti.* Sulla circonferenza di raggio $1$ centrata nell'origine si parte dal punto $P = (1, 0)$ e si percorre un arco in senso antiorario fino a $Q$. La misura in radianti dell'angolo $\vartheta$ è la **lunghezza dell'arco** $x$ (in blu).

L'angolo $\vartheta = x$ (radianti), dove $x$ = lunghezza dell'arco $PQ \in [0, 2\pi)$ orientato in senso antiorario. Per $x < 0$ oppure $x \ge 2\pi$ si identifica $x$ con $x \bmod 2\pi$ (si fanno giri completi in più o in senso orario). Ad esempio
$$90° = \tfrac\pi2, \quad 180° = \pi, \quad 270° = \tfrac{3\pi}2, \quad 360° = 2\pi, \quad 3\pi \bmod 2\pi = \pi, \quad -5\pi \bmod 2\pi = \pi.$$

![[AN1-p040-2.png]]

*Figura 20 — Definizione delle funzioni circolari.* Sulla circonferenza unitaria, al punto individuato dall'arco $x$ (in blu): la sua **ascissa** è $\cos(x)$ (in viola, sull'asse $x$), la sua **ordinata** è $\sin(x)$ (in verde, il segmento verticale), e $\tan(x)$ (in rosso) è l'ordinata del punto in cui il prolungamento del raggio incontra la retta verticale tangente alla circonferenza in $(1, 0)$.

Si ottengono:
- **seno**: $\sin(x)$, $x \in \mathbb{R}$;
- **coseno**: $\cos(x)$, $x \in \mathbb{R}$;
- **tangente**: $\tan(x) = \dfrac{\sin(x)}{\cos(x)}$, $x \in \mathbb{R} \setminus \left\{\frac{2k+1}{2}\pi : k \in \mathbb{Z}\right\}$ (si escludono i punti dove $\cos(x) = 0$).

![[AN1-p040-3.png]]

*Figura 21 — Grafici di sin, cos e tan.* In alto $\sin(x)$ tra $-2\pi$ e $2\pi$: un'onda tra $-1$ e $1$, che vale $0$ nei multipli di $\pi$ e $1$ in $\frac\pi2$. In basso a sinistra $\cos(x)$: la stessa onda spostata di $\frac\pi2$ a sinistra, con massimo $1$ in $0$. A destra $\tan(x)$: rami crescenti ripetuti ogni $\pi$, separati da asintoti verticali (tratteggiati) in $\pm\frac\pi2, \pm\frac{3\pi}2, \dots$

Osservazioni:
- $\cos$ è **pari**, limitata ($-1 \le \cos(x) \le 1$) e periodica di periodo $T = 2\pi$;
- $\sin$ è **dispari**, limitata ($-1 \le \sin(x) \le 1$) e periodica di periodo $T = 2\pi$;
- $\tan$ è definita per $x \neq \frac{2k+1}{2}\pi$, è **dispari**, né inferiormente né superiormente limitata, e periodica di periodo $T = \pi$;
- valgono numerose relazioni, ad esempio
  - $\cos^2(x) + \sin^2(x) = 1$ per ogni $x$ (teorema di Pitagora nel triangolo di Figura 20, con ipotenusa $1$);
  - le **formule di prostaferesi**:
  $$\sin(x) - \sin(y) = 2\sin\left(\tfrac{x-y}{2}\right)\cos\left(\tfrac{x+y}{2}\right), \qquad \cos(x) - \cos(y) = -2\sin\left(\tfrac{x-y}{2}\right)\sin\left(\tfrac{x+y}{2}\right).$$

_(dispensa, pp. 34–35)_

---

## Limiti delle Funzioni Reali

Vedi [[Limite di funzione]].

Data $f : X \subseteq \mathbb{R} \to \mathbb{R}$ e $c \in \overline{\mathbb{R}}$:

> [!question] Problema
> Studiare il comportamento di $f(x)$ per $x$ **vicino** (ma **diverso**!) a $c$.

Se $X = \mathbb{N}$ e $c = +\infty$, $f$ è una successione $a_n = f(n)$ e il problema è proprio quello del limite di successioni: il caso generale lo estende.

### Punti di accumulazione

Prima bisogna capire in quali punti ha senso chiedersi cosa fa $f$ "vicino a $c$": servono punti di $X$ arbitrariamente vicini a $c$.

> [!important] Definizione 3.5 — Punto di accumulazione
> $c \in \overline{\mathbb{R}}$ è un **punto di accumulazione** di $X \subseteq \mathbb{R}$ se esiste una successione $(x_n)$ con
> - $x_n \in X$ per ogni $n$,
> - $x_n \neq c$ per ogni $n$,
> - $\lim_{n\to+\infty} x_n = c$.
>
> In breve: esiste $(x_n) \subset X \setminus \{c\}$ con $x_n \to c$. Cioè, restando in $X \setminus \{c\}$, ci si può avvicinare a $c$.

> [!example] Esempi
> - $c = 3$ **non** è di accumulazione per $\mathbb{N}$: non esiste $(x_n) \subset \mathbb{N} \setminus \{3\}$ con $x_n \to 3$ (i naturali sono "isolati").
> - $c = +\infty$ è l'**unico** punto di accumulazione di $\mathbb{N}$.
> - $c = -1$ **non** è di accumulazione per $[0, +\infty)$.
> - Se $I$ è un intervallo di estremi $a$ e $b$, allora $c$ è di accumulazione per $I$ $\iff$ $c \in [a, b]$ (anche gli estremi esclusi da $I$, ad esempio $0$ per $(0, 1)$).

### Definizione di limite

> [!important] Definizione 3.6 — Limite per le funzioni
> Sia $f : X \to \mathbb{R}$ e sia $c \in \overline{\mathbb{R}}$ un punto di accumulazione di $X$. Si dice che **$f$ tende a $l \in \overline{\mathbb{R}}$ per $x$ tendente a $c$** se
> $$\text{per ogni successione } (x_n) \subset X \setminus \{c\} \text{ con } x_n \to c \text{ si ha } f(x_n) \to l.$$
> Si scrive $\displaystyle\lim_{x\to c} f(x) = l$ oppure $f(x) \to l$ per $x \to c$.

È la **definizione per successioni**: il limite di $f$ in $c$ è $l$ se, comunque ci si avvicini a $c$ lungo una successione, i valori di $f$ si avvicinano a $l$. Il vantaggio è che tutti i risultati del [[01 - AN1 - Successioni Numeriche|cap. 1]] si trasferiscono subito.

Osservazioni:
- il limite, se esiste, è **unico** (lo è per ogni successione);
- scrivendo $\lim_{x\to c} f(x)$ si suppone sempre che $c$ sia di accumulazione per il dominio. Ad esempio $\lim_{x\to-1} \sqrt x$ non ha senso, perché $-1$ non è di accumulazione per $[0, +\infty)$;
- si usano solo successioni con $x_n \neq c$ perché interessa $f$ **vicino** a $c$, non **in** $c$: il valore $f(c)$ (se esiste) non conta;
- esiste anche una definizione equivalente **senza successioni** (con $\varepsilon$ e $\delta$), che però richiede casi diversi a seconda che $c$ e $l$ siano finiti o infiniti: vedi l'[[12 - AN1 - Appendice#Definizione alternativa dei Limiti per Funzioni|Appendice]].

> [!example] Esempio 1: $\lim_{x\to 0} \sin(x) = 0$
> Dal grafico delle funzioni circolari si vede che $0 \le |\sin(x)| \le |x|$ per ogni $x$. Quindi per ogni $(x_n) \subset \mathbb{R} \setminus \{0\}$ con $x_n \to 0$:
> $$\underbrace{0}_{\to 0} \le |\sin(x_n)| \le \underbrace{|x_n|}_{\to 0},$$
> e per i [[01 - AN1 - Successioni Numeriche#Teorema del confronto e dei carabinieri|carabinieri]] $\sin(x_n) \to 0$. Per definizione $\lim_{x\to0} \sin(x) = 0$.

> [!example] Esempio 2: $\lim_{x\to 0} \cos(x) = 1$
> Per la prostaferesi $1 - \cos(x) = \cos(0) - \cos(x) = 2\sin^2\left(\frac x2\right)$. Per ogni $x_n \to 0$, $x_n \neq 0$:
> $$1 - \cos(x_n) = 2\sin^2\left(\tfrac{x_n}{2}\right) \to 2 \cdot 0^2 = 0,$$
> quindi $\lim_{x\to0}(1 - \cos(x)) = 0$, cioè $\lim_{x\to0}\cos(x) = 1$.

> [!example] Esempio 3: $\lim_{x\to 0} \frac{|x|}{x}$ non esiste
> Sia $f(x) := \frac{|x|}{x}$ per $x \neq 0$:
> $$f(x) = \begin{cases} 1 & \text{se } x > 0, \\ -1 & \text{se } x < 0. \end{cases}$$
> Con $x_n := \frac{(-1)^n}{n} \to 0$ si ottiene $f(x_n) = (-1)^n$, che non ha limite. Basta **una** successione "cattiva" per dimostrare che il limite non esiste.

![[AN1-p042-1.png]]

*Figura 22 — Funzione segno.* A sinistra la definizione per casi, a destra il grafico: la semiretta $y = 1$ (verde) per $x > 0$ e la semiretta $y = -1$ (rossa) per $x < 0$. In $x = 0$ c'è un "salto": avvicinandosi da destra i valori sono $1$, da sinistra $-1$.

> [!tip] Come dimostrare che un limite non esiste
> Si trovano due successioni $x_n \to c$ e $x_n' \to c$ con $f(x_n)$ e $f(x_n')$ che tendono a valori diversi (qui $x_n = \frac1n$ dà $1$, $x_n' = -\frac1n$ dà $-1$), oppure una sola successione con $f(x_n)$ irregolare.

_(dispensa, pp. 35–36)_

### Limite destro e sinistro

Anche se $\lim_{x\to0} \frac{|x|}{x}$ non esiste, $f(x)$ tende a $+1$ avvicinandosi a $0$ **da destra** e a $-1$ **da sinistra**.

> [!important] Definizione 3.7 — Limite destro e sinistro
> - $x_n \to c$ **da destra** ($x_n \to c^+$) se $x_n \to c$ e $x_n \ge c$ definitivamente; **da sinistra** ($x_n \to c^-$) se $x_n \to c$ e $x_n \le c$ definitivamente.
> - $f(x) \to l$ per $x \to c^+$ (**limite destro**) se per ogni $(x_n) \subset X \setminus \{c\}$ con $x_n \to c^+$ si ha $f(x_n) \to l$; si scrive $\lim_{x\to c^+} f(x) = l$.
> - $f(x) \to l$ per $x \to c^-$ (**limite sinistro**) se per ogni $(x_n) \subset X \setminus \{c\}$ con $x_n \to c^-$ si ha $f(x_n) \to l$; si scrive $\lim_{x\to c^-} f(x) = l$.

> [!example] Esempi
> - $\lim_{x\to0^+} \frac{|x|}{x} = +1$, $\lim_{x\to0^-} \frac{|x|}{x} = -1$.
> - $\lim_{x\to0^+} \frac1x = \frac{1}{0^+} = +\infty$, $\lim_{x\to0^-} \frac1x = \frac{1}{0^-} = -\infty$.

> [!important] Limite e limiti laterali
> $$\lim_{x\to c} f(x) = l \iff \lim_{x\to c^+} f(x) = l = \lim_{x\to c^-} f(x).$$

Anche i limiti laterali si possono definire senza successioni, distinguendo i casi $c, l \in \mathbb{R}$ o $\pm\infty$ ([[12 - AN1 - Appendice#Definizione alternativa dei Limiti per Funzioni|Appendice]]).

_(dispensa, pp. 36–37)_

### Limiti ed asintoti

Vedi [[Asintoti]].

- Se $\lim_{x\to c^{(\pm)}} f(x) = \pm\infty$ con $c \in \mathbb{R}$, $f$ ha un **asintoto verticale** $x = c$.
- Se $\lim_{x\to\pm\infty} f(x) = l$ con $l \in \mathbb{R}$, $f$ ha un **asintoto orizzontale** $y = l$.

Un asintoto è una retta a cui il grafico si avvicina indefinitamente.

> [!example] Esempi
> - $\tan(x)$ ha asintoti verticali in $x_k = \frac{2k+1}{2}\pi$, $k \in \mathbb{Z}$ (Figura 21).
> - $\tanh(x)$ ha asintoti orizzontali $y = -1$ (per $x \to -\infty$) e $y = +1$ (per $x \to +\infty$) (Figura 17).

Gli asintoti **obliqui** verranno nello [[05 - AN1 - Calcolo Differenziale#Studio di Funzione|studio di funzione]].

_(dispensa, p. 37)_

### Regole di calcolo e ordinamento

> [!important] Regole per il calcolo dei limiti
> Se $\lim_{x\to c} f(x) = l_1$ e $\lim_{x\to c} g(x) = l_2$ con $c \in \overline{\mathbb{R}}$ e $l_1, l_2 \in \mathbb{R}$:
> - $\lim_{x\to c} (f(x) \pm g(x)) = l_1 \pm l_2$;
> - $\lim_{x\to c} (f(x) \cdot g(x)) = l_1 \cdot l_2$;
> - $\lim_{x\to c} \frac{f(x)}{g(x)} = \frac{l_1}{l_2}$ se $l_2 \neq 0$;
> - $\lim_{x\to c} f(x)^{g(x)} = l_1^{l_2}$ se $l_1 > 0$;
> - $\lim_{x\to c} |f(x)| = |l_1|$.

Seguono subito dalle [[01 - AN1 - Successioni Numeriche#Regole per il Calcolo dei Limiti|regole per le successioni]] (si applicano a $f(x_n)$ e $g(x_n)$). Valgono anche per i limiti laterali e per $l_1, l_2 \in \overline{\mathbb{R}}$ quando si ottiene una [[01 - AN1 - Successioni Numeriche#Forme determinate e indeterminate|forma determinata]]. In sostanza: le operazioni algebriche sono compatibili con il limite, e non importa se si fa prima l'operazione o prima il limite, finché tutte le forme sono determinate.

> [!important] Limiti e ordinamento
> Se $f(x) \le g(x)$ per ogni $x \in X$, $f(x) \to l_1$ e $g(x) \to l_2$ per $x \to c$:
> - $l_1 \le l_2$ (**teorema del confronto**);
> - se inoltre $f(x) \le h(x) \le g(x)$ per ogni $x$ e $l_1 = l_2$, allora $h(x) \to l_1$ (**teorema dei carabinieri**).

Come per le successioni, i carabinieri servono a "incastrare" un'espressione complicata $h(x)$ tra due più semplici con lo stesso limite.

_(dispensa, p. 37)_

### Tre limiti notevoli

Vedi [[Limiti notevoli]].

> [!important] (1) $\displaystyle\lim_{x\to0} \frac{\sin(x)}{x} = 1$

![[AN1-p044-1.png]]

*Figura 23 — Relazione tra $x$, $\sin(x)$ e $\tan(x)$.* Nel primo quadrante della circonferenza unitaria, per un angolo $x \in \left(0, \frac\pi2\right)$: il segmento verde ($\sin x$) è più corto dell'arco blu ($x$), che a sua volta è più corto del segmento rosso ($\tan x$) sulla tangente verticale. Da qui la catena di disuguaglianze scritta accanto.

**Dimostrazione.** Dalla figura, per ogni $x \in \left(0, \frac\pi2\right)$:
$$0 < \sin(x) \le x \le \tan(x) = \frac{\sin(x)}{\cos(x)}.$$
Dividendo per $\sin(x) > 0$: $1 \le \frac{x}{\sin(x)} \le \frac{1}{\cos(x)}$, e passando agli inversi
$$\underbrace{1}_{\to 1} \ge \frac{\sin(x)}{x} \ge \underbrace{\cos(x)}_{\to 1} \qquad \text{per } x \to 0^+.$$
Per i carabinieri il limite destro vale $1$. Poiché $\frac{\sin(x)}{x}$ è pari (rapporto di due dispari), anche il limite sinistro vale $1$. $\square$

> [!important] (2) $\displaystyle\lim_{x\to0} \frac{1 - \cos(x)}{x^2} = \frac12$

**Dimostrazione.** Per $x \in (-\pi, \pi) \setminus \{0\}$ (dove $1 + \cos(x) \neq 0$):
$$\frac{1 - \cos(x)}{x^2} = \frac{1 - \cos(x)}{x^2} \cdot \frac{1 + \cos(x)}{1 + \cos(x)} = \frac{\overbrace{1 - \cos^2(x)}^{= \sin^2(x)}}{x^2 (1 + \cos(x))} = \underbrace{\left(\frac{\sin(x)}{x}\right)^2}_{\to 1} \cdot \underbrace{\frac{1}{1 + \cos(x)}}_{\to \frac12} \to \frac12. \qquad \square$$

> [!important] (3) $\displaystyle\lim_{x\to0} \frac{e^x - 1}{x} = 1$

**Dimostrazione.** Si parte da $e^x = \lim_{n\to+\infty}\left(1 + \frac xn\right)^n$ (generalizzazione della definizione di $e$). Per Bernoulli
$$\left(1 + \tfrac xn\right)^n \ge 1 + n \cdot \tfrac xn = 1 + x \qquad \text{se } \tfrac xn \ge -1, \text{ cioè } n \ge -x,$$
quindi la disuguaglianza vale definitivamente e per il confronto $e^x \ge 1 + x$ per ogni $x \in \mathbb{R}$. Sostituendo $x$ con $-x$: $e^{-x} = \frac{1}{e^x} \ge 1 - x$, che è $> 0$ per $x < 1$, quindi passando agli inversi $e^x \le \frac{1}{1-x}$ per $x < 1$. In totale, per ogni $x < 1$:
$$1 + x \le e^x \le \frac{1}{1-x} \quad\Rightarrow\quad x \le e^x - 1 \le \frac{1}{1-x} - 1 = \frac{x}{1-x}.$$
Dividendo per $x \neq 0$ (attenzione al verso):
- se $0 < x < 1$: $\underbrace{1}_{\to 1} \le \frac{e^x - 1}{x} \le \underbrace{\frac{1}{1-x}}_{\to 1}$, quindi $\lim_{x\to0^+} \frac{e^x-1}{x} = 1$;
- se $x < 0$: $\underbrace{1}_{\to 1} \ge \frac{e^x - 1}{x} \ge \underbrace{\frac{1}{1-x}}_{\to 1}$, quindi $\lim_{x\to0^-} \frac{e^x-1}{x} = 1$,

per i carabinieri. $\square$

> [!tip] Come leggerli
> I tre limiti dicono che vicino a $0$: $\sin(x) \approx x$, $\cos(x) \approx 1 - \frac{x^2}{2}$, $e^x \approx 1 + x$. Sono i primi passi delle [[05 - AN1 - Calcolo Differenziale#La Formula di Taylor|formule di Taylor]] e, interpretati come rapporti incrementali, danno le derivate di $\sin$ ed $e^x$ in $0$. Un elenco più completo è nell'[[12 - AN1 - Appendice#Elenco di alcuni Limiti Notevoli|Appendice]].

_(dispensa, pp. 38–39)_

### Limiti di funzioni monotone

Anche il teorema sulle successioni monotone si generalizza alle funzioni.

> [!important] Teorema 3.8
> Se $f : X \to \mathbb{R}$ è monotona, allora i limiti laterali
> $$\lim_{x\to c^-} f(x) =: l^- \in \overline{\mathbb{R}} \qquad \text{e} \qquad \lim_{x\to c^+} f(x) =: l^+ \in \overline{\mathbb{R}}$$
> **esistono** sempre. Inoltre
> $$l^- = \sup\{f(x) : x \in X, x < c\}, \quad l^+ = \inf\{f(x) : x \in X, x > c\} \qquad \text{se } f \text{ è crescente},$$
> $$l^- = \inf\{f(x) : x \in X, x < c\}, \quad l^+ = \sup\{f(x) : x \in X, x > c\} \qquad \text{se } f \text{ è decrescente}.$$

Una funzione monotona può quindi avere al più **salti** (limiti laterali diversi), mai oscillazioni come $\sin\frac1x$ vicino a $0$.

### Limiti per le funzioni composte

> [!important] Limite di una funzione composta
> Siano $f : X \to Y$, $g : Y \to \mathbb{R}$ e $c, l, y_0 \in \overline{\mathbb{R}}$ con
> - $\lim_{x\to c} f(x) = y_0$,
> - $\lim_{y\to y_0} g(y) = l$,
> - esiste $\delta > 0$ tale che $f(x) \neq y_0$ per ogni $x \in X$ con $0 < |x - c| < \delta$.
>
> Allora $\displaystyle\lim_{x\to c} g(f(x)) = l$.

È la regola del **cambio di variabile** nei limiti: si pone $y = f(x)$ e si calcola il limite di $g$ per $y \to y_0$. La terza condizione è necessaria: il limite di $g$ in $y_0$ ignora il valore $g(y_0)$, quindi se $f$ assumesse il valore $y_0$ vicino a $c$, nella composizione entrerebbe proprio quel valore "ignorato".

> [!example] Esempio
> - $\lim_{x\to0} \sin(x) = 0$ (qui $f = \sin$, $c = 0$, $y_0 = 0$);
> - $\lim_{y\to0} \cos(y) = 1$ (qui $g = \cos$, $l = 1$);
> - $\sin(x) \neq 0$ per $0 < |x| < \pi$ (si può scegliere $\delta := \pi$).
>
> Quindi $\displaystyle\lim_{x\to0} \cos(\sin(x)) = 1$.

Con la **continuità** ([[04 - AN1 - Funzioni Continue|cap. 4]]) la terza condizione diventerà superflua: se $g$ è continua in $y_0$, il valore $g(y_0)$ coincide con il limite e non dà fastidio.

_(dispensa, p. 39)_
