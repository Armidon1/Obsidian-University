---
title: Funzioni a Valori Vettoriali
aliases:
  - AN1 — Funzioni a Valori Vettoriali
tags:
  - analisi-1
  - più-variabili
  - funzioni-vettoriali
  - jacobiana
  - regola-della-catena
  - trasformazioni-di-coordinate
source: Appunti di Analisi Matematica 1 di Camilli.pdf (cap. 9)
---

# Funzioni a Valori Vettoriali

> [!abstract]
> Finora il codominio era $\mathbb{R}$; ora si considerano funzioni $f : \mathbb{R}^N \to \mathbb{R}^M$, a **valori vettoriali**. Una funzione del genere è semplicemente un vettore di $M$ funzioni reali (le **componenti**), quindi limiti, continuità, derivabilità e differenziabilità si definiscono **componente per componente** a partire dal [[08 - AN1 - Calcolo Differenziale in più Variabili|cap. 8]]. Le derivate parziali delle componenti si raccolgono nella **matrice jacobiana**, che rende la **regola della catena** un semplice prodotto di matrici.
> Il caso $M = N$ sono le **trasformazioni di coordinate**: il **teorema di invertibilità locale** dice quando si possono invertire (jacobiano non nullo), e gli esempi fondamentali sono le **coordinate polari, cilindriche e sferiche**. Il determinante jacobiano tornerà come fattore di scala nel **cambiamento di variabili** negli integrali multipli ([[10 - AN1 - Integrali Multipli|cap. 10]]).
> Mappa del corso: [[MOC - Analisi 1]].

---

## Funzioni a valori vettoriali

> [!example] Esempio motivante
> Un punto materiale si muove nello spazio nell'intervallo di tempo $[0, T]$; siano $(x(t), y(t), z(t))$ le sue coordinate al tempo $t$. Si ottiene una funzione a valori vettoriali $f : [0, T] \subset \mathbb{R} \to \mathbb{R}^3$, $f(t) = (x(t), y(t), z(t))$: la **traiettoria** del punto.

> [!important] Definizione 9.1
> Una funzione $f : X \subseteq \mathbb{R}^N \to Y \subseteq \mathbb{R}^M$ si dice **funzione a valori vettoriali**.

Definire $f : \mathbb{R}^N \to \mathbb{R}^M$ equivale a dare $M$ funzioni reali $f_i : \mathbb{R}^N \to \mathbb{R}$, $i = 1, \dots, M$ (le **componenti**): a ogni $x = (x_1, \dots, x_N)$ si associa il vettore (con $(\ldots)^T$ si indica il trasposto)
$$(y_1, \dots, y_M)^T = f(x) = \big(f_1(x_1, \dots, x_N), \dots, f_M(x_1, \dots, x_N)\big)^T \in \mathbb{R}^M.$$

Ad esempio $f : \mathbb{R}^2 \to \mathbb{R}^3$, $f(x, y) = (xy, e^{xy}, x^2)$ è data dalle tre componenti $f_1(x, y) = xy$, $f_2(x, y) = e^{xy}$, $f_3(x, y) = x^2$. Da questa identificazione segue che il **dominio** di $f$ è l'**intersezione** dei domini delle componenti.

_(dispensa, p. 133)_

### Limiti, continuità e differenziabilità

Con l'identificazione tra $f$ e le sue componenti si estendono le definizioni date per le funzioni reali di più variabili.

> [!important] Definizione 9.2 — Limite
> Siano $f : X \subseteq \mathbb{R}^N \to \mathbb{R}^M$, $x_0 \in \mathbb{R}^N$ e $l = (l_1, \dots, l_M) \in \mathbb{R}^M$. Allora
> $$\lim_{x\to x_0} f(x) = l \iff \lim_{x\to x_0} f_i(x) = l_i, \quad i = 1, \dots, M$$
> (convergenza **componente per componente**).

Dalle proprietà dei limiti delle funzioni di più variabili seguono l'**unicità del limite**, le **regole di calcolo** (poiché il codominio è uno spazio vettoriale, si hanno somma e moltiplicazione per uno scalare, componente per componente) e il **limite della funzione composta**.

> [!important] Definizioni 9.3–9.5 — Continuità, derivabilità, differenziabilità
> Sia $f : X \subset \mathbb{R}^N \to \mathbb{R}^M$ e $x_0 \in X$.
> - $f$ è **continua** in $x_0$ (punto di accumulazione) $\iff$ $\lim_{x\to x_0} f(x) = f(x_0)$ $\iff$ tutte le componenti $f_i$ sono continue in $x_0$.
> - $f$ è **derivabile** in $x_0$ $\iff$ tutte le componenti $f_i$ sono derivabili in $x_0$.
> - $f$ è **differenziabile** in $x_0$ $\iff$ tutte le componenti sono differenziabili in $x_0$, cioè
> $$f_i(x) = f_i(x_0) + Df_i(x_0) \cdot (x - x_0) + o(\|x - x_0\|) \qquad (x \to x_0),\ \forall i = 1, \dots, M.$$

_(dispensa, p. 133)_

### Matrice jacobiana

Vedi [[Matrice jacobiana]].

Per riscrivere la differenziabilità in forma compatta si usa la notazione matriciale. Considerando $f$ come vettore colonna $f(x) = \begin{pmatrix} f_1(x) \\ \vdots \\ f_M(x) \end{pmatrix}$, la **matrice di Jacobi** (o **jacobiana**) di $f$ in $x_0$ è la matrice $M \times N$ che ha per righe i gradienti delle componenti:
$$J_f(x_0) = \begin{pmatrix} Df_1(x_0) \\ \vdots \\ Df_M(x_0) \end{pmatrix} = \begin{pmatrix} \frac{\partial f_1}{\partial x_1}(x_0) & \cdots & \frac{\partial f_1}{\partial x_N}(x_0) \\ \vdots & \ddots & \vdots \\ \frac{\partial f_M}{\partial x_1}(x_0) & \cdots & \frac{\partial f_M}{\partial x_N}(x_0) \end{pmatrix}_{M \times N}.$$
(Riga $i$ = componente $i$; colonna $j$ = variabile $j$.) La differenziabilità diventa
$$f(x) = f(x_0) + J_f(x_0) \cdot (x - x_0) + o(\|x - x_0\|) \qquad (x \to x_0).$$

| Caso | Oggetto | Dimensione |
|---|---|---|
| $f : \mathbb{R} \to \mathbb{R}$ | derivata $f'(x_0)$ | $1 \times 1$ |
| $f : \mathbb{R}^N \to \mathbb{R}$ | gradiente $Df(x_0)$ | $1 \times N$ |
| $f : \mathbb{R}^N \to \mathbb{R}^M$ | jacobiana $J_f(x_0)$ | $M \times N$ |

> [!example] Esempio
> Per $f(x, y) = (xy, e^{xy}, x^2)$:
> $$J_f(x, y) = \begin{pmatrix} y & x \\ ye^{xy} & xe^{xy} \\ 2x & 0 \end{pmatrix}.$$

_(dispensa, p. 134)_

### Derivata della funzione composta

La regola per la jacobiana di una funzione composta generalizza la [[05 - AN1 - Calcolo Differenziale#Derivazione delle funzioni composte|regola della catena]].

> [!important] Teorema 9.6 — Regola della catena
> Sia $f : X \subseteq \mathbb{R}^N \to Y \subseteq \mathbb{R}^M$ differenziabile in $x_0 \in X$ e $g : Y \subseteq \mathbb{R}^M \to \mathbb{R}^K$ differenziabile in $y_0 := f(x_0)$. Allora $g \circ f : X \to \mathbb{R}^K$ è differenziabile in $x_0$ con
> $$J_{g\circ f}(x_0) = J_g(f(x_0)) \cdot J_f(x_0).$$

Le dimensioni tornano: $(K \times M) \cdot (M \times N) = K \times N$. Per $N = M = K = 1$ si ritrova la regola della catena per le funzioni di una variabile.

> [!example] Esempio
> $f : \mathbb{R} \to \mathbb{R}^2$, $g : \mathbb{R}^2 \to \mathbb{R}$, quindi $g \circ f : \mathbb{R} \to \mathbb{R}$, $(g \circ f)(s) = g(f_1(s), f_2(s))$ e
> $$(g \circ f)'(s) = \left(\frac{\partial g}{\partial x}(f_1(s), f_2(s)),\ \frac{\partial g}{\partial y}(f_1(s), f_2(s))\right) \cdot \begin{pmatrix} f_1'(s) \\ f_2'(s) \end{pmatrix} = \frac{\partial g}{\partial x}(f(s))\, f_1'(s) + \frac{\partial g}{\partial y}(f(s))\, f_2'(s).$$
> Interpretazione: se $g$ è la temperatura in un punto del piano e $f(s)$ la posizione di un oggetto al tempo $s$, la variazione di temperatura percepita dall'oggetto è $Dg \cdot f'(s)$, la [[08 - AN1 - Calcolo Differenziale in più Variabili#Derivate direzionali|derivata direzionale]] lungo la velocità.

_(dispensa, p. 134)_

---

## Trasformazioni Regolari di Coordinate

Vedi [[Trasformazione regolare di coordinate]].

Un caso particolarmente importante è quello in cui spazio di partenza e di arrivo coincidono, $M = N$.

> [!important] Definizione 9.7
> Una funzione $f : X \subseteq \mathbb{R}^N \to Y \subseteq \mathbb{R}^N$ si dice **trasformazione di coordinate**.

Un esempio è l'**applicazione lineare** $f(x) = A \cdot x$ con $A$ matrice $N \times N$ (corso di Geometria). Se $\det(A) \neq 0$, $f$ si inverte: $f^{-1}(y) = A^{-1} y$, con $f^{-1}(f(x)) = x$ e $f(f^{-1}(y)) = y$ per ogni $x, y$ (vedi [[Invertible Matrix]], Geometria).

> [!question] Problema
> Data una trasformazione di coordinate $f : X \subseteq \mathbb{R}^N \to Y \subseteq \mathbb{R}^N$, sotto quali condizioni si può invertire, cioè esiste $f^{-1} : Y \to X$?

> [!important] Definizione 9.8 — Trasformazione regolare
> Una trasformazione di coordinate $f : X \subseteq \mathbb{R}^N \to \mathbb{R}^N$ si dice **regolare** se $f \in C^1(X)$ (derivate parziali esistenti e continue) e $\det(J_f(x)) \neq 0$ eccetto al più "alcuni punti", detti **punti singolari** della trasformazione.

("Alcuni punti" andrebbe precisato con una misura su $\mathbb{R}^N$; basta sapere che va bene se i punti singolari formano un insieme di dimensione $N - 1$, ad esempio una retta nel piano o un asse nello spazio.)

Se $\det(J_f(x_0)) \neq 0$, $J_f(x_0)$ è una matrice invertibile, e vale:

> [!important] Teorema 9.9 — Invertibilità locale
> Sia $f : X \subseteq \mathbb{R}^N \to \mathbb{R}^N$ una trasformazione regolare e $x_0 \in X$ con $\det(J_f(x_0)) \neq 0$. Allora esistono un intorno $U(x_0)$ di $x_0$ e un intorno $V(y_0)$ di $y_0 = f(x_0)$ tali che $f : U(x_0) \to V(y_0)$ è **invertibile**. Inoltre l'inversa $f^{-1} : V(y_0) \to U(x_0)$ è una trasformazione regolare e
> $$J_{f^{-1}}(y) = J_f^{-1}(x) \qquad \forall y \in V(y_0),$$
> dove $J_f^{-1}$ è l'inversa della jacobiana di $f$ e $f(x) = y$.

La formula generalizza la [[05 - AN1 - Calcolo Differenziale#Derivazione delle funzioni inverse|derivata della funzione inversa]] $(f^{-1})'(y_0) = \frac{1}{f'(x_0)}$, a cui si riduce per $N = 1$; la condizione $\det J_f(x_0) \neq 0$ corrisponde a $f'(x_0) \neq 0$. L'invertibilità è solo **locale**: ad esempio le coordinate polari non sono globalmente iniettive se si permette a $\vartheta$ di variare su tutto $\mathbb{R}$.

> [!example] Esempio: trasformazioni lineari
> Per $A = (a_{ij})_{N \times N}$, $f(x) = A \cdot x = (a_{11}x_1 + \ldots + a_{1N}x_N, \dots, a_{N1}x_1 + \ldots + a_{NN}x_N)^T$. Allora $J_f(x) = A$ per ogni $x$, e $\det J_f(x_0) \neq 0 \iff \det(A) \neq 0$: si ritrova il risultato noto, la trasformazione è invertibile se e solo se $A$ non è degenere; in questo caso l'inversa è definita **globalmente** su $\mathbb{R}^N$.

_(dispensa, pp. 134–135)_

### Coordinate polari

Vedi [[Coordinate polari]].

Le coordinate polari, già usate per i [[07 - AN1 - Funzioni di più Variabili - Limiti e Continuità#Coordinate polari e esistenza del limite|limiti]], sono una trasformazione di coordinate.

![[AN1-p141-1.png]]

*Figura 81 — Coordinate polari.* Il punto di coordinate cartesiane $(x, y)$ (in rosso) individuato dalla distanza $\rho$ dall'origine e dall'angolo $\vartheta$ con l'asse $x$ (in blu).

$$f : [0, \infty) \times [0, 2\pi) \to \mathbb{R}^2, \qquad (\rho, \vartheta) \mapsto (\rho\cos\vartheta, \rho\sin\vartheta)^T.$$
La jacobiana (colonne: derivate rispetto a $\rho$ e a $\vartheta$) è
$$J_f(\rho, \vartheta) = \begin{pmatrix} \cos\vartheta & -\rho\sin\vartheta \\ \sin\vartheta & \rho\cos\vartheta \end{pmatrix}, \qquad \det J_f(\rho, \vartheta) = \rho\cos^2\vartheta + \rho\sin^2\vartheta = \rho.$$
L'unico punto singolare è l'**origine** ($\rho = 0$): lì l'angolo $\vartheta$ non è determinato, e tutti i $(0, \vartheta)$ vanno nello stesso punto. Le coordinate polari sono una trasformazione regolare.

### Coordinate cilindriche

Vedi [[Coordinate cilindriche e sferiche]].

In $\mathbb{R}^3$, le **coordinate cilindriche** sono la terna $(\rho, \vartheta, t) \in [0, \infty) \times [0, 2\pi) \times \mathbb{R}$: coordinate polari nel piano $xy$ più l'altezza.

![[AN1-p142-1.png]]

*Figura 82 — Coordinate cilindriche.* Il punto $P = (x, y, z)$ si proietta sul piano $xy$; la proiezione è descritta in coordinate polari da $\rho$ (segmento rosso) e $\vartheta$ (angolo rosso), e l'altezza è $z = t$. Il cilindro tratteggiato verde è l'insieme dei punti con lo stesso $\rho$: le coordinate cilindriche sono naturali per oggetti con simmetria attorno all'asse $z$.

$$\begin{cases} x = \rho\cos\vartheta \\ y = \rho\sin\vartheta \\ z = t \end{cases} \qquad f : [0, \infty) \times [0, 2\pi) \times \mathbb{R} \to \mathbb{R}^3, \quad (\rho, \vartheta, t) \mapsto (\rho\cos\vartheta, \rho\sin\vartheta, t)^T.$$
$$J_f(\rho, \vartheta, t) = \begin{pmatrix} \cos\vartheta & -\rho\sin\vartheta & 0 \\ \sin\vartheta & \rho\cos\vartheta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \det J_f = \rho.$$
I punti singolari ($\rho = 0$) formano l'**asse $z$**: le coordinate cilindriche sono una trasformazione regolare.

### Coordinate sferiche

Le **coordinate sferiche** sono la terna $(\rho, \vartheta, \varphi) \in [0, \infty) \times [0, 2\pi) \times [0, \pi]$: distanza dall'origine, "longitudine" $\vartheta$ e angolo $\varphi$ dall'asse $z$ (la "colatitudine").

![[AN1-p143-1.png]]

*Figura 83 — Coordinate sferiche.* Il punto $P$ è a distanza $\rho$ dall'origine (segmento rosso); $\varphi$ è l'angolo tra il segmento $OP$ e l'asse $z$, $\vartheta$ l'angolo tra la proiezione di $OP$ sul piano $xy$ e l'asse $x$. La sfera tratteggiata verde è l'insieme dei punti con lo stesso $\rho$: sono le coordinate di latitudine e longitudine sul globo, più il raggio.

$$\begin{cases} x = \rho\sin\varphi\cos\vartheta \\ y = \rho\sin\varphi\sin\vartheta \\ z = \rho\cos\varphi \end{cases} \qquad f : [0, \infty) \times [0, \pi] \times [0, 2\pi) \to \mathbb{R}^3, \quad (\rho, \varphi, \vartheta) \mapsto (\rho\sin\varphi\cos\vartheta, \rho\sin\varphi\sin\vartheta, \rho\cos\varphi)^T.$$
$$J_f(\rho, \varphi, \vartheta) = \begin{pmatrix} \sin\varphi\cos\vartheta & \rho\cos\varphi\cos\vartheta & -\rho\sin\varphi\sin\vartheta \\ \sin\varphi\sin\vartheta & \rho\cos\varphi\sin\vartheta & \rho\sin\varphi\cos\vartheta \\ \cos\varphi & -\rho\sin\varphi & 0 \end{pmatrix}, \qquad \det J_f(\rho, \varphi, \vartheta) = \rho^2\sin\varphi.$$
I punti singolari ($\rho = 0$ oppure $\sin\varphi = 0$, cioè $\varphi \in \{0, \pi\}$) formano l'**asse $z$**: le coordinate sferiche sono una trasformazione regolare.

> [!summary] Determinanti jacobiani da ricordare
> | Coordinate | Trasformazione | $\det J_f$ |
> |---|---|---|
> | polari | $(\rho\cos\vartheta, \rho\sin\vartheta)$ | $\rho$ |
> | cilindriche | $(\rho\cos\vartheta, \rho\sin\vartheta, t)$ | $\rho$ |
> | sferiche | $(\rho\sin\varphi\cos\vartheta, \rho\sin\varphi\sin\vartheta, \rho\cos\varphi)$ | $\rho^2\sin\varphi$ |
>
> Sono i fattori che compaiono negli integrali multipli: $dA = \rho\,d\rho\,d\vartheta$, $dV = \rho^2\sin\varphi\,d\rho\,d\varphi\,d\vartheta$ ([[10 - AN1 - Integrali Multipli#Cambiamento di Variabili negli Integrali Doppi|cap. 10]]).

_(dispensa, pp. 135–137)_
