---
title: Appendice
aliases:
  - AN1 — Appendice
tags:
  - analisi-1
  - dimostrazioni
  - limiti-notevoli
  - definizione-epsilon-delta
source: Appunti di Analisi Matematica 1 di Camilli.pdf (Note e Appendice A)
---

# Appendice

> [!abstract]
> Materiale di consultazione in fondo alla dispensa: i **testi consigliati**, i **tre modi di dimostrare** un'implicazione (usati in tutto il corso, ad esempio per l'[[01 - AN1 - Successioni Numeriche#Successioni convergenti|unicità del limite]]), un **elenco di limiti notevoli** per successioni e funzioni, e la **definizione $\varepsilon$–$\delta$ dei limiti** di funzione, alternativa a quella per successioni del [[03 - AN1 - Funzioni Reali di una Variabile Reale#Definizione di limite|cap. 3]].
> Mappa del corso: [[MOC - Analisi 1]].

---

## Testi consigliati

- A. Marson, P. Baiti, F. Ancona, B. Rubino: *Corso di Analisi Matematica 1*, Carocci editore;
- C.D. Pagani, S. Salsa: *Analisi Matematica 1*, Zanichelli;
- P. Marcellini, C. Sbordone: *Esercitazioni di Matematica*, Liguori Editore;
- S. Salsa, A. Squellati: *Esercizi di Matematica*, Zanichelli.

_(dispensa, p. 158)_

---

## Tre Principali Modi di Dimostrazioni

Siano $A$ e $B$ due affermazioni e $\neg A$, $\neg B$ le loro negazioni. Sono **equivalenti**:
- $A \Rightarrow B$;
- $\neg B \Rightarrow \neg A$;
- $A$ e $\neg B$ $\Rightarrow$ $\lightning$ (contraddizione).

Quindi per dimostrare $A \Rightarrow B$ ci sono tre modi:

| Metodo | Si dimostra |
|---|---|
| **dimostrazione diretta** | $A \Rightarrow B$ |
| **dimostrazione indiretta** (per contronominale) | $\neg B \Rightarrow \neg A$ |
| **dimostrazione per assurdo** | $A$ e $\neg B$ $\Rightarrow \lightning$ |

> [!example] Esempio
> Sia $A$ = "piove" e $B$ = "la strada è bagnata". Vale $A \Rightarrow B$, ma **non** il contrario ($B \not\Rightarrow A$): se la strada è bagnata non è detto che piova (qualcuno potrebbe averla lavata). In questo esempio:
> - $A \Rightarrow B$: "se piove, la strada si bagna" (vero);
> - $\neg B \Rightarrow \neg A$: "se la strada non è bagnata, allora non piove" (vero);
> - $A$ e $\neg B$: "piove e la strada non è bagnata", che infatti è una contraddizione.

> [!tip] Dove si usano nel corso
> - **Diretta**: la maggior parte delle dimostrazioni (es. [[05 - AN1 - Calcolo Differenziale#Derivabilità e continuità|derivabile ⇒ continua]]).
> - **Contronominale**: la [[02 - AN1 - Serie Numeriche#Condizione necessaria|condizione necessaria]] per le serie si usa così: "se $a_k \not\to 0$, la serie non converge".
> - **Per assurdo**: l'[[01 - AN1 - Successioni Numeriche#Successioni convergenti|unicità del limite]], il [[00 - AN1 - Concetti Fondamentali#Paradosso di Russell|paradosso di Russell]], l'irrazionalità di $\sqrt2$.
>
> Lo stesso schema logico è alla base della dimostrazione per **induzione** ([[00 - AN1 - Concetti Fondamentali#Principio di Induzione|cap. 0]]).

_(dispensa, p. 159)_

---

## Elenco di alcuni Limiti Notevoli

Vedi [[Limiti notevoli]].

### Successioni

| Limite | Condizioni |
|---|---|
| $\displaystyle\lim_{n\to+\infty} q^n = \begin{cases} +\infty & q > 1 \\ 1 & q = 1 \\ 0 & \lvert q\rvert < 1 \\ \nexists & q \le -1 \end{cases}$ | successione geometrica |
| $\displaystyle\lim_{n\to+\infty} n^\alpha = \begin{cases} +\infty & \alpha > 0 \\ 1 & \alpha = 0 \\ 0 & \alpha < 0 \end{cases}$ | successione armonica |
| $\lim \sqrt[n]{a} = 1$ | per ogni $a > 0$ |
| $\lim \sqrt[n]{n^\alpha} = 1$ | per ogni $\alpha \in \mathbb{R}$ |
| $\lim \frac{\ln(n)}{n^\alpha} = 0$ | per ogni $\alpha > 0$ |
| $\lim \frac{n^\alpha}{q^n} = 0$ | per ogni $\alpha \in \mathbb{R}$, $q > 1$ |
| $\lim \frac{q^n}{n!} = 0$ | per ogni $q \in \mathbb{R}$ |
| $\lim \frac{n!}{n^n} = 0$ | |
| $\lim \left(1 + \frac1n\right)^n = e$ | più in generale: |
| $\lim \left(1 + \frac{a}{x_n}\right)^{x_n} = e^a$ | se $\lvert x_n\rvert \to +\infty$ |
| $\lim (a_n)^{b_n} = a^b$ | se $a_n \to a > 0$ e $b_n \to b$ |

Le prime due righe sono la [[01 - AN1 - Successioni Numeriche#Successione geometrica|successione geometrica]] e la [[01 - AN1 - Successioni Numeriche#Successione armonica|successione armonica]] del cap. 1.

> [!tip] La gerarchia degli infiniti
> Le righe centrali dicono che, per $n \to +\infty,$
> $$\ln(n) \ll n^\alpha \ll q^n \ll n! \ll n^n \qquad (\alpha > 0,\ q > 1),$$
> dove $a_n \ll b_n$ significa $\frac{a_n}{b_n} \to 0$: logaritmi, potenze, esponenziali, fattoriali, $n^n$, ciascuno "vince" su quelli prima. È la stessa scala delle [[Funzioni di crescita|funzioni di crescita]] usate per la complessità degli algoritmi. Vedi [[Gerarchia degli infiniti]].

### Funzioni

| Limite | Condizioni |
|---|---|
| $\lim_{x\to0} \frac{\sin x}{x} = 1$ | |
| $\lim_{x\to0} \frac{1 - \cos(x)}{x^2} = \frac12$ | |
| $\lim_{x\to0} \frac{e^x - 1}{x} = 1$ | più in generale: |
| $\lim_{x\to0} \frac{a^x - 1}{x} = \ln(a)$ | per ogni $a > 0$ |
| $\lim_{x\to0} \frac{\ln(1 + x)}{x} = 1$ | più in generale: |
| $\lim_{x\to0} \frac{\log_a(1 + x)}{x} = \log_a(e)$ | per ogni $0 < a \neq 1$ |
| $\lim_{x\to\pm\infty} \left(1 + \frac tx\right)^x = e^t$ | per ogni $t \in \mathbb{R}$ |
| $\lim_{x\to0} \frac{(1 + x)^r - 1}{x} = r$ | per ogni $r \in \mathbb{R}$ |
| $\lim_{x\to+\infty} \frac{\log_a(x)}{x^\alpha} = 0$ | per ogni $0 < a \neq 1$, $\alpha > 0$ |
| $\lim_{x\to0^+} x^\alpha \log_a(x) = 0$ | per ogni $0 < a \neq 1$, $\alpha > 0$ |
| $\lim_{x\to0^+} x^x = 1$ | |

I primi tre sono dimostrati nel [[03 - AN1 - Funzioni Reali di una Variabile Reale#Tre limiti notevoli|cap. 3]]; quelli con il logaritmo nel [[05 - AN1 - Calcolo Differenziale#Le Regole di de l'Hospital|cap. 5]] (de l'Hospital); $x^x \to 1$ nell'[[05 - AN1 - Calcolo Differenziale#Estremi Locali e il Teorema di Fermat|esempio $x^x$]]. Quasi tutti si leggono come primi termini di [[05 - AN1 - Calcolo Differenziale#Sviluppi di Taylor notevoli|sviluppi di Taylor]].

_(dispensa, p. 160)_

---

## Definizione alternativa dei Limiti per Funzioni

Vedi [[Limite di funzione]].

Sia $f : X \subseteq \mathbb{R} \to \mathbb{R}$ e $x_0$ un punto di accumulazione di $X$. La definizione per successioni ([[03 - AN1 - Funzioni Reali di una Variabile Reale#Definizione di limite|Definizione 3.6]]) equivale alla seguente, che però va scritta caso per caso a seconda che $x_0$ e $l$ siano finiti o infiniti. L'idea comune: "vicino a $l$" si esprime con $\varepsilon$ (se $l$ è finito) o con una soglia $M$ (se è infinito); "vicino a $x_0$" con $\delta$ (se $x_0$ è finito) o con una soglia $L$ (se è infinito).

### Limite

$\displaystyle\lim_{x\to x_0} f(x) = l \iff$

| $x_0$ | $l$ | Condizione |
|---|---|---|
| $\in \mathbb{R}$ | $\in \mathbb{R}$ | $\forall \varepsilon > 0\ \exists \delta > 0 : \lvert f(x) - l\rvert < \varepsilon\ \ \forall x \in X,\ 0 < \lvert x - x_0\rvert < \delta$ |
| $\in \mathbb{R}$ | $+\infty$ | $\forall M > 0\ \exists \delta > 0 : f(x) > M\ \ \forall x \in X,\ 0 < \lvert x - x_0\rvert < \delta$ |
| $\in \mathbb{R}$ | $-\infty$ | $\forall M < 0\ \exists \delta > 0 : f(x) < M\ \ \forall x \in X,\ 0 < \lvert x - x_0\rvert < \delta$ |
| $+\infty$ | $\in \mathbb{R}$ | $\forall \varepsilon > 0\ \exists L > 0 : \lvert f(x) - l\rvert < \varepsilon\ \ \forall x \in X,\ x > L$ |
| $-\infty$ | $\in \mathbb{R}$ | $\forall \varepsilon > 0\ \exists L < 0 : \lvert f(x) - l\rvert < \varepsilon\ \ \forall x \in X,\ x < L$ |
| $+\infty$ | $+\infty$ | $\forall M > 0\ \exists L > 0 : f(x) > M\ \ \forall x \in X,\ x > L$ |
| $+\infty$ | $-\infty$ | $\forall M < 0\ \exists L > 0 : f(x) < M\ \ \forall x \in X,\ x > L$ |
| $-\infty$ | $+\infty$ | $\forall M > 0\ \exists L < 0 : f(x) > M\ \ \forall x \in X,\ x < L$ |
| $-\infty$ | $-\infty$ | $\forall M < 0\ \exists L < 0 : f(x) < M\ \ \forall x \in X,\ x < L$ |

> [!warning] Correzione
> Nei casi con $l = \pm\infty$ e $x_0 \in \mathbb{R}$ la dispensa scrive "per ogni $\varepsilon > 0$ esiste $M > 0$ tale che $f(x) > M$ per ogni $x$ con $0 < |x - x_0| < \delta$": i ruoli sono scambiati. Si fissa la soglia $M$ (arbitraria) e si cerca il raggio $\delta$, come nella tabella sopra: "$\forall M > 0\ \exists \delta > 0$". (Lo stesso refuso compare nelle definizioni di limite destro e sinistro.)

### Limite destro e sinistro

Per i [[03 - AN1 - Funzioni Reali di una Variabile Reale#Limite destro e sinistro|limiti laterali]] si sostituisce la condizione $0 < |x - x_0| < \delta$ con una condizione da un solo lato:

| Limite | $l$ | Condizione |
|---|---|---|
| $\lim_{x\to x_0^+} f(x) = l$ | $\in \mathbb{R}$ | $\forall \varepsilon > 0\ \exists \delta > 0 : \lvert f(x) - l\rvert < \varepsilon\ \ \forall x \in X,\ 0 < x - x_0 < \delta$ |
| $\lim_{x\to x_0^+} f(x) = l$ | $+\infty$ | $\forall M > 0\ \exists \delta > 0 : f(x) > M\ \ \forall x \in X,\ 0 < x - x_0 < \delta$ |
| $\lim_{x\to x_0^-} f(x) = l$ | $\in \mathbb{R}$ | $\forall \varepsilon > 0\ \exists \delta > 0 : \lvert f(x) - l\rvert < \varepsilon\ \ \forall x \in X,\ 0 < x_0 - x < \delta$ |
| $\lim_{x\to x_0^-} f(x) = l$ | $+\infty$ | $\forall M > 0\ \exists \delta > 0 : f(x) > M\ \ \forall x \in X,\ 0 < x_0 - x < \delta$ |

(I casi $l = -\infty$ sono analoghi con $M < 0$ e $f(x) < M$.)

> [!example] Esempio: $\lim_{x\to0^+} \frac1x = +\infty$ con la definizione
> Fissato $M > 0$, si vuole $\frac1x > M$, cioè $x < \frac1M$. Basta $\delta := \frac1M$: per $0 < x < \delta$ vale $\frac1x > \frac1\delta = M$.

_(dispensa, p. 161)_

---

## Elenco delle figure

La dispensa termina con l'elenco delle 97 figure (pp. 162–164). Nelle note del corso ogni figura è inserita nel paragrafo da cui proviene, con la sua spiegazione; le immagini si trovano in `images/` con nome `AN1-pNNN-K.png`, dove `NNN` è la pagina del PDF.

_(dispensa, pp. 162–164)_
