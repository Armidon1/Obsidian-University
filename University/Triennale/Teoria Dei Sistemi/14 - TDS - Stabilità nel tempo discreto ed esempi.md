---
title: Stabilità nel tempo discreto ed esempi
aliases:
  - TDS — Stabilità nel tempo discreto ed esempi
tags:
  - teoria-dei-sistemi
  - stabilita
  - tempo-discreto
  - criterio-di-jury
  - criterio-di-lyapunov
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 60–69); libro Monaco et al., §1.2.2, §3.8–3.8.3
---

# Stabilità nel tempo discreto ed esempi

> [!abstract] Scopo della lezione
> Nella [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto#Stabilità dei sistemi lineari a tempo discreto|lezione precedente]] si è visto che nel tempo discreto la stabilità dipende dal **modulo** degli autovalori ($|\lambda_i|<1$), e che il criterio di Routh non si applica direttamente. Qui:
> 1. **condizioni necessarie** sul polinomio caratteristico e il **criterio di Jury**, l'analogo discreto di Routh;
> 2. la **trasformazione bilineare** che porta il cerchio unitario nel semipiano sinistro, per poter riusare Routh;
> 3. **linearizzazione** e **criterio di Lyapunov** nel tempo discreto;
> 4. tre modelli semplici: un **modello economico** (prezzo), un modello **preda-predatore** e la **popolazione studentesca**.
>
> Con questa lezione si chiude lo studio nel dominio del tempo; dalla [[15 - TDS - Trasformata di Laplace|prossima]] si passa al dominio complesso. Indice: [[MOC - Teoria dei Sistemi]].

## Condizioni necessarie per la stabilità nel tempo discreto

Vedi [[TDS - Criterio di Jury]].

Nel tempo discreto si ha stabilità semplice se $|\lambda_i|\le1$ per ogni autovalore (regolare se $|\lambda_i|=1$) e asintotica se $|\lambda_i|<1$. Si potrebbero calcolare gli autovalori, ma spesso è complicato, tanto più se i coefficienti contengono parametri. Cerchiamo un algoritmo, partendo dal polinomio caratteristico fattorizzato:

$$p(\lambda)=a_n\lambda^n+a_{n-1}\lambda^{n-1}+\dots+a_1\lambda+a_0=a_n(\lambda-\lambda_1)(\lambda-\lambda_2)\cdots(\lambda-\lambda_n)$$

Supponiamo che tutte le radici abbiano $|\lambda_i|<1$.

- **In $\lambda=1$**: ogni fattore $1-\lambda_i$ è positivo (per una radice reale $\lambda_i<1$), quindi $p(1)$ ha lo stesso segno di $a_n$:
  $$\mathrm{sign}\,p(1)=\mathrm{sign}\,a_n$$
- **In $\lambda=-1$**: ogni fattore $-1-\lambda_i$ è negativo, e a ogni prodotto il segno cambia:
  $$\mathrm{sign}\,p(-1)=(-1)^n\,\mathrm{sign}(a_n)$$
- **In $\lambda=0$**: $p(0)=a_n(-\lambda_1)\cdots(-\lambda_n)=a_n\prod_i(-\lambda_i)$, e in modulo
  $$|p(0)|=|a_n|\prod_{i=1}^n|\lambda_i|<|a_n|\cdot\prod_{i=1}^n1=|a_n|$$
  Ma $p(0)=a_0$, quindi $|a_0|<|a_n|$.

Si hanno tre **condizioni necessarie** perché le radici abbiano modulo minore di uno:

$$\begin{cases}\mathrm{sign}\,p(1)=\mathrm{sign}(a_n)\\\mathrm{sign}\,p(-1)=(-1)^n\,\mathrm{sign}(a_n)\\|a_0|<|a_n|\end{cases}$$

Se una non è soddisfatta, le radici **non** hanno tutte modulo minore di 1. Se sono tutte soddisfatte, non si può ancora concludere nulla: serve un algoritmo, più semplice di quello del continuo.

> [!quote] Dal libro — anche con radici complesse
> Il libro (con $a_n>0$) scrive le condizioni come $p(1)>0$, $(-1)^np(-1)>0$, $|a_0|<|a_n|$, e mostra che il ragionamento vale anche per le coppie complesse: $(\lambda-\lambda_i)(\lambda-\lambda_i^*)=\lambda^2-2|\lambda_i|\cos\varphi_{\lambda_i}\lambda+|\lambda_i|^2$, che per $\lambda=1$ è maggiore di $(1-|\lambda_i|)^2>0$. _(libro, §3.8, p. 148)_

## Criterio di Jury

> [!note] Annotazione di Simone
> Sopra il titolo, a mano in verde: **"ALGORITMO DA STAMPARSI IN MENTE"**.

Si scrivono i coefficienti del polinomio da $a_0$ ad $a_n$ e, sotto, gli stessi in **ordine inverso**:

| | | | | | |
|---|---|---|---|---|---|
| $a_0$ | $a_1$ | $a_2$ | $\cdots$ | $a_{n-1}$ | $a_n$ |
| $a_n$ | $a_{n-1}$ | $a_{n-2}$ | $\cdots$ | $a_1$ | $a_0$ |
| $b_0$ | $b_1$ | $b_2$ | $\cdots$ | $b_{n-1}$ | |

La terza riga si costruisce con determinanti $2\times2$. **La prima colonna** del determinante è sempre la stessa: i **primi** elementi delle due righe precedenti ($a_0$, $a_n$). **La seconda colonna** parte dagli **ultimi** elementi delle due righe e si sposta verso sinistra a ogni nuovo termine:

$$b_0=\begin{vmatrix}a_0&a_n\\a_n&a_0\end{vmatrix},\qquad b_1=\begin{vmatrix}a_0&a_{n-1}\\a_n&a_1\end{vmatrix},\qquad\dots,\qquad b_{n-1}=\begin{vmatrix}a_0&a_1\\a_n&a_{n-1}\end{vmatrix}$$

cioè $b_i=\begin{vmatrix}a_0&a_{n-i}\\a_n&a_i\end{vmatrix}$. Finita la riga, la successiva è la **stessa riga invertita**, e da queste due si calcola la riga dei $c$ nello stesso modo (prima colonna $\begin{psmallmatrix}b_0\\b_{n-1}\end{psmallmatrix}$, seconda colonna che parte da $\begin{psmallmatrix}b_{n-1}\\b_0\end{psmallmatrix}$ e va all'indietro):

| | | | | | |
|---|---|---|---|---|---|
| $a_0$ | $a_1$ | $\cdots$ | $a_{n-2}$ | $a_{n-1}$ | $a_n$ |
| $a_n$ | $a_{n-1}$ | $\cdots$ | $a_2$ | $a_1$ | $a_0$ |
| $b_0$ | $b_1$ | $\cdots$ | $b_{n-2}$ | $b_{n-1}$ | |
| $b_{n-1}$ | $b_{n-2}$ | $\cdots$ | $b_1$ | $b_0$ | |
| $c_0$ | $c_1$ | $\cdots$ | $c_{n-2}$ | | |
| $c_{n-2}$ | $c_{n-3}$ | $\cdots$ | $c_0$ | | |
| $\vdots$ | | | | | |
| $\mu_0$ | $\mu_1$ | $\mu_2$ | | | |

Ogni coppia di righe ne produce una più corta di un elemento; ci si ferma quando si arriva a una riga con **tre** elementi. Poi si guarda la **prima colonna** a coppie di righe:

> [!important] Criterio di Jury
> Le radici di $p(\lambda)$ hanno tutte modulo minore di 1 (stabilità asintotica) se e solo se, oltre alle tre condizioni necessarie, valgono
> $$|b_{n-1}|<|b_0|,\quad|c_{n-2}|<|c_0|,\quad|d_{n-3}|<|d_0|,\quad\dots,\quad|\mu_2|<|\mu_0|$$

Attenzione: la condizione necessaria $|a_0|<|a_n|$ è "al contrario" rispetto alle altre (lì l'elemento grande è l'ultimo, $a_n$; nelle altre è il primo). Questo criterio esclude a priori tutte le soluzioni con modulo **uguale** a 1: dice solo se il sistema è asintoticamente stabile.

> [!example] Dal libro — Esempi 3.8.1 e 3.8.2
> - $p(\lambda)=\lambda^2+\lambda+0{,}5$: $p(1)=2{,}5>0$, $(-1)^2p(-1)=0{,}5>0$, $|0{,}5|<1$. Con tre soli coefficienti la tabella è inutile: le radici hanno modulo minore di 1 (infatti sono $-\frac12\pm\frac j2$, di modulo $\frac{\sqrt2}{2}$).
> - $p(\lambda)=\lambda^4-1{,}6\lambda^3+0{,}38\lambda^2+0{,}4\lambda-0{,}1575$: condizioni necessarie verificate ($p(1)=0{,}0225$, $p(-1)=2{,}4225$, $|-0{,}1575|<1$); la tabella dà $b_0=-0{,}9752$, $b_3=-0{,}1480$, $c_0=-0{,}9291$, $c_2=-0{,}6565$, e $|b_3|<|b_0|$, $|c_2|<|c_0|$: radici tutte di modulo minore di 1.
>
> "A differenza della tabella di Routh, la costruzione della tabella di Jury non presenta mai impedimenti." _(libro, §3.8.1, pp. 149–150)_

## Passaggio da un criterio all'altro

Vedi [[TDS - Stabilità]].

Nel tempo continuo, con Routh, la regione "buona" del piano complesso è il **semipiano sinistro** $\mathrm{Re}(\lambda)<0$:

![[TDS-L14-01.png]]

Nel tempo discreto è invece l'**interno del cerchio di raggio 1**, $|\lambda|<1$:

![[TDS-L14-02.png]]

Si può scrivere una relazione che trasforma il cerchio nel semipiano e viceversa, così da applicare uno dei due criteri anche nell'altro caso: per esempio usare Routh per un sistema discreto. Se $z$ è un punto del piano del cerchio, il punto corrispondente $s$ del semipiano è

$$s=\frac{z-1}{z+1}\qquad\Longleftrightarrow\qquad z=\frac{1+s}{1-s}$$

(è la cosiddetta **trasformazione bilineare**).

**La circonferenza va sull'asse immaginario.** Un punto della circonferenza unitaria si scrive in forma modulo-fase $z=e^{j\theta}$ (il modulo è sempre 1, la fase è l'angolo con l'asse reale):

$$s=\frac{e^{j\theta}-1}{e^{j\theta}+1}=\frac{e^{j\frac\theta2}\big(e^{j\frac\theta2}-e^{-j\frac\theta2}\big)}{e^{j\frac\theta2}\big(e^{j\frac\theta2}+e^{-j\frac\theta2}\big)}=\frac{j\,\frac{e^{j\frac\theta2}-e^{-j\frac\theta2}}{2j}}{\frac{e^{j\frac\theta2}+e^{-j\frac\theta2}}{2}}=\frac{j\sin\frac\theta2}{\cos\frac\theta2}=j\tan\frac\theta2$$

Con $\theta\in[-\pi,\pi]$, $j\tan\frac\theta2$ ha parte reale nulla e percorre tutto l'asse immaginario, da $-\infty$ a $+\infty$.

**L'interno del cerchio va nel semipiano sinistro.** Con $z=\alpha+j\omega$, razionalizzando:

$$s=\frac{(\alpha-1)+j\omega}{(\alpha+1)+j\omega}\cdot\frac{(\alpha+1)-j\omega}{(\alpha+1)-j\omega}=\frac{\alpha^2+\omega^2-1}{(\alpha+1)^2+\omega^2}+j\,\frac{2\omega}{(\alpha+1)^2+\omega^2}$$

Interessa la parte reale: il denominatore è sempre positivo, il numeratore è negativo se e solo se $\alpha^2+\omega^2<1$. Quindi i punti nel cerchio ($\sqrt{\alpha^2+\omega^2}<1$) vanno nella zona con $\mathrm{Re}(s)<0$.

> [!tip] Come si usa in pratica
> Per sapere se $p(\lambda)$ ha tutte le radici con $|\lambda|<1$: si sostituisce $\lambda=\frac{1+s}{1-s}$, si moltiplica per $(1-s)^n$ per togliere i denominatori, e si applica Routh al polinomio in $s$ ottenuto.

> [!example] Dal libro — Esempio 3.8.3
> $p(\lambda)=\lambda^3-0{,}8\lambda^2-0{,}25\lambda+0{,}2$. Con $\lambda=\frac{1+s}{1-s}$:
> $$(1+s)^3-0{,}8(1+s)^2(1-s)-0{,}25(1+s)(1-s)^2+0{,}2(1-s)^3=1{,}35s^3+4{,}65s^2+1{,}85s+0{,}15$$
> Tabella di Routh: $1{,}35;\ 4{,}65;\ 1{,}8065;\ 0{,}15$, nessuna variazione: tutte le radici in $s$ hanno parte reale negativa, quindi tutte quelle in $\lambda$ hanno modulo minore di 1. _(libro, §3.8.2, pp. 151–152)_

Il professore ha però detto di non aver mai visto nessuno fare questo procedimento con carta e penna nelle applicazioni: è più comodo ricordare sia Routh che Jury.

## Approssimazione di sistemi non lineari a tempo discreto

Vedi [[TDS - Linearizzazione]].

Dato un sistema discreto non lineare $x(t+1)=f\big(x(t),u(t)\big)$ e un suo equilibrio $x_e$, con $f(x_e,0)=x_e$, si costruisce l'approssimazione lineare con lo sviluppo di Taylor al primo ordine:

$$f\big(x(t),u(t)\big)\approx f(x_e,0)+\underbrace{\left.\frac{\partial f}{\partial x}\right|_{\substack{x=x_e\\u=0}}}_{A}(x(t)-x_e)+\underbrace{\left.\frac{\partial f}{\partial u}\right|_{\substack{x=x_e\\u=0}}}_{B}u\quad\Longrightarrow\quad x(t+1)=f(x_e,0)+A(x(t)-x_e)+Bu(t)$$

Trascurando l'ingresso resta $f(x_e,0)\neq0$, quindi l'espressione di $x(t+1)$ **non è lineare** (c'è un termine costante). Ma con $z(t)=x(t)-x_e$ si ha $z(t+1)=x(t+1)-x_e$ e, poiché $f(x_e,0)=x_e$:

$$x(t+1)=z(t+1)+x_e=\underbrace{f(x_e,0)}_{x_e}+A(x(t)-x_e)\quad\Longrightarrow\quad z(t+1)=Az(t)$$

Vale lo stesso risultato del continuo: se il linearizzato è asintoticamente stabile lo è anche il non lineare, se è instabile lo è anche il non lineare, e per la stabilità semplice non si può dire nulla.

## Criterio di Lyapunov per tempo discreto

Vedi [[TDS - Criterio di Lyapunov]].

> [!note] Annotazione di Simone
> A margine, a mano in verde: **"Unica differenza"**.

Il criterio è simile a quello del continuo: si prende $V(x(t))>0$, ma invece della derivata (che nel discreto non ha senso) si usa la **differenza prima**

$$\Delta V(x(t))=V(x(t+1))-V(x(t))=V\big(f(x(t),0)\big)-V(x(t))$$

Se $\Delta V$ è **definita negativa** l'equilibrio è asintoticamente stabile (localmente); se è **semidefinita negativa** è semplicemente stabile (localmente). Come nel continuo, se $V$ è radialmente illimitata ($V\to+\infty$ per $\|x\|\to+\infty$) il risultato vale globalmente. E se non si trova una $V$ adatta, non si può concludere nulla.

**Caso lineare.** Con $x(t+1)=Ax(t)$ si prova una funzione quadratica $V(x(t))=x'(t)Qx(t)$ con $Q>0$ simmetrica:

$$\Delta V=V(Ax(t))-V(x(t))=(Ax(t))'QAx(t)-x'(t)Qx(t)=x'(t)\big[A'QA-Q\big]x(t)$$

È definita negativa se $A'QA-Q$ lo è, cioè

$$A'QA-Q=-P$$

con $P$ simmetrica e definita positiva. Nel caso lineare la condizione è **necessaria e sufficiente**: l'equilibrio è asintoticamente stabile se e solo se, fissata $P>0$ simmetrica, l'equazione ha una soluzione $Q>0$ simmetrica (unica). Questa soluzione è

$$Q=\sum_{t=0}^{\infty}(A')^tPA^t$$

del tutto analoga al continuo ($\int\leftrightarrow\sum$, $e^{At}\leftrightarrow A^t$). È definita positiva perché, con $y=A^tz$,

$$z'Qz=\sum_{t=0}^{\infty}\big(z'(A')^t\big)P\big(A^tz\big)=\sum_{t=0}^{\infty}y'Py>0$$

ed è soluzione perché, spostando l'indice ($\tau=t+1$):

$$A'QA-Q=\sum_{t=0}^{\infty}(A')^{t+1}PA^{t+1}-\sum_{t=0}^{\infty}(A')^tPA^t=\sum_{\tau=1}^{\infty}(A')^\tau PA^\tau-\Big[(A')^0PA^0+\sum_{t=1}^{\infty}(A')^tPA^t\Big]=-P$$

> [!warning] Correzione
> Negli appunti si legge che $Q>0$ vuol dire che "i determinanti dei minori principali sono tutti **maggiori di 1**": la condizione (criterio di Sylvester) è che siano **maggiori di 0**. Inoltre "$A'QA-Q<0\iff$ il punto di equilibrio è stabile" va letto come stabilità **asintotica**, con $Q>0$.

> [!quote] Dal libro
> "La formulazione segue quella enunciata nel caso a tempo continuo con la differenza che, definita una funzione di Lyapunov $V(x)$ occorre introdurre la funzione **differenza prima** […] in luogo della sua derivata." _(libro, §3.8.3, p. 152)_

## Semplice modello economico (tempo discreto)

Ora si vede come tutto questo aiuta ad analizzare i sistemi e a metterne in evidenza le caratteristiche qualitative senza troppi calcoli. Un modello economico di base lega domanda, offerta e prezzo di una merce. La **domanda** $d$ è una "domanda base" $d_0$ (quella che ci sarebbe se tutti potessero permettersi la merce) **meno** una quantità che dipende dal prezzo $p$; la **produzione** $m$ è la quantità $m_0$ necessaria per la domanda più una quantità "in eccesso" che dipende anch'essa dal prezzo:

$$d=d_0-ap,\qquad m=m_0+bp$$

Il tempo entra così: la domanda al ciclo di vendite successivo (per esempio l'anno dopo) dipende da quanto costerà la merce in quel momento, mentre chi produce si regola su quello che vende **adesso**:

$$d(t+1)=d_0-ap(t+1),\qquad m(t+1)=m_0+bp(t)$$

Nel mercato ideale la domanda è uguale all'offerta, $d_0-ap(t+1)=m_0+bp(t)$, e si ottiene un sistema a tempo discreto con stato il prezzo:

$$p(t+1)=-\frac bap(t)+\frac{d_0-m_0}{a}$$

L'equilibrio:

$$p_e=-\frac bap_e+\frac{d_0-m_0}{a}\quad\Longrightarrow\quad p_e=\frac{d_0-m_0}{a+b}$$

Il prezzo dipende da $m_0$, $d_0$, $a$ e $b$. Fisicamente $a$ fa diminuire la domanda: è la "**propensione al risparmio**", quanto l'acquirente è attento al prezzo; $b$ è quanto il produttore vuole guadagnare. Il prezzo di equilibrio diminuisce sia quando aumenta l'"avidità" $b$, sia quando aumenta la propensione al risparmio $a$.

**Stabilità.** $A$ è uno scalare, con un solo autovalore $\lambda=-\frac ba$. L'equilibrio è stabile se

$$|\lambda|=\left|-\frac ba\right|<1\iff b<a$$

"La voglia di guadagnare deve essere inferiore a quanto l'acquirente è disposto a spendere": se il produttore diventa troppo avido, l'equilibrio diventa instabile e il prezzo varia.

> [!tip] Il modello "a ragnatela"
> L'autovalore $-\frac ba$ è **negativo**: il modo è **alternante** (vedi [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Calcolo di $A^t$ e modi naturali|lezione 9]]). Il prezzo oscilla sopra e sotto $p_e$ un anno sì e uno no: un anno di prezzo alto spinge a produrre molto, il che fa crollare il prezzo l'anno dopo, e così via. Le oscillazioni si smorzano se $b<a$ e si amplificano se $b>a$. Il libro presenta lo stesso modello come "la dinamica del prezzo in condizioni di equilibrio tra domanda e offerta in assenza di concorrenza". _(libro, §1.2.2, pp. 11–12)_

## Modello semplice preda-predatore (tempo continuo)

Nel mondo ci sono due specie. La specie $x$ ha tutto quello che le serve e si riproduce senza limiti: $\dot x(t)=ax(t)$. Arriva una seconda specie $y$ che per nutrirsi mangia la $x$: la $y$ cresce con gli incontri ($\dot y=mxy$) e la $x$ diminuisce ($\dot x=ax-nxy$). I coefficienti $m$ e $n$ sono diversi perché, per esempio, un esemplare di $y$ può mangiare più esemplari di $x$. Se non mangia, la specie $y$ muore con coefficiente $b$:

$$\begin{cases}\dot x(t)=ax(t)-nx(t)y(t)\\\dot y(t)=mx(t)y(t)-by(t)\end{cases}$$

Il sistema non è lineare. Equilibri: scartato quello banale $(0,0)$,

$$\begin{cases}ax_e-nx_ey_e=0\\mx_ey_e-by_e=0\end{cases}\iff\begin{cases}x_e(a-ny_e)=0\\y_e(mx_e-b)=0\end{cases}\quad\Longrightarrow\quad y_e=\frac an,\quad x_e=\frac bm$$

> [!example] Un caso reale
> Anni fa in America furono importate piante dall'Australia alla California; con le piante arrivarono dei parassiti che, senza predatori, prosperavano distruggendo le piante (la specie $x$). Si decise di importare anche gli insetti predatori dei parassiti (la specie $y$), raggiungendo l'equilibrio trovato. Anni dopo si usarono insetticidi sulle piante per ridurre la specie $x$, causando la morte sia di $x$ (coefficiente $h$) sia di $y$ (coefficiente $k$):
> $$\begin{cases}\dot x=ax-nxy-hx\\\dot y=mxy-by-ky\end{cases}\iff\begin{cases}x_e(a-ny_e-h)=0\\y_e(mx_e-b-k)=0\end{cases}\Longrightarrow\ y_e=\frac{a-h}{n},\quad x_e=\frac{b+k}{m}$$
> Rispetto a prima è **diminuita** la specie $y$ (che erano i "buoni") ed è **aumentata** la specie $x$, che si voleva ridurre: l'insetticida ha ottenuto l'effetto opposto.

> [!note] Collegamento
> Il libro tratta lo stesso modello (Lotka-Volterra) anche linearizzandolo: l'origine risulta instabile, mentre nell'equilibrio non banale lo jacobiano ha "una coppia di autovalori a parte reale nulla che non consente di trarre alcuna conclusione sulla stabilità" (vedi [[12 - TDS - Criterio di Routh e linearizzazione#Approssimazione di sistemi non lineari|lezione 12]]). Se si aggiunge un limite alle risorse della preda (termine $-kx^2$), compare un equilibrio che, perturbato, dà oscillazioni che convergono. _(libro, §3.5.2, pp. 136–137)_

## Popolazione studentesca del triennio di ingegneria

Un modello semplice: $x_1$ studenti del primo anno, $x_2$ del secondo, $x_3$ del terzo. Il sistema va di anno in anno, quindi il tempo è discreto. Se $p$ è la probabilità di superare tutti gli esami e passare all'anno successivo, $1-p$ è quella di restare all'anno attuale; $I(t)$ sono i nuovi immatricolati:

$$\begin{cases}x_1(t+1)=(1-p)x_1(t)+I(t)\\x_2(t+1)=px_1(t)+(1-p)x_2(t)\\x_3(t+1)=px_2(t)+(1-p)x_3(t)\end{cases}$$

> [!warning] Correzione
> Negli appunti "$x_3$ quelli del **secondo** anno": sono quelli del **terzo** anno.

Se gli anni hanno difficoltà diverse, $p_1$ e $p_2$ sono le probabilità di superare il primo e il secondo anno e $l$ quella di laurearsi:

$$x(t+1)=\begin{pmatrix}1-p_1&0&0\\p_1&1-p_2&0\\0&p_2&1-l\end{pmatrix}x(t)+\begin{pmatrix}1\\0\\0\end{pmatrix}u(t),\qquad u(t)=I(t)$$

$A$ è triangolare, quindi gli autovalori sono sulla diagonale: $\lambda_1=1-p_1$, $\lambda_2=1-p_2$, $\lambda_3=1-l$. Poiché $p_1,p_2,l$ sono probabilità comprese tra 0 e 1, tutti gli autovalori hanno $|\lambda_i|<1$, a meno che nessuno studente riesca a passare all'anno successivo o a laurearsi ($p_1$, $p_2$ o $l$ nulli): il sistema è asintoticamente stabile e, **senza ingresso**, tende a 0 (nessuno studente). Con l'unico equilibrio $x_e=0$.

> [!warning] Correzione
> Gli appunti giustificano l'unicità dell'equilibrio con "il rango della matrice è pieno". Nel tempo discreto gli equilibri risolvono $(A-I)x_e=0$ ([[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto#Stabilità interna|lezione 13]]), quindi conta il rango di $A-I$, che ha diagonale $-p_1,-p_2,-l$: è pieno se $p_1,p_2,l\neq0$, cioè se $1$ non è autovalore.

Ma ci sono sempre nuovi immatricolati, e qui l'ingresso è fondamentale: invece di $x_e=Ax_e$ si cerca $x_e=Ax_e+Bu_e$, con un numero costante $I_e$ di immatricolati:

$$\begin{cases}(1-p_1)x_{e1}+I_e=x_{e1}\\p_1x_{e1}+(1-p_2)x_{e2}=x_{e2}\\p_2x_{e2}+(1-l)x_{e3}=x_{e3}\end{cases}\quad\Longrightarrow\quad x_e=\begin{pmatrix}I_e/p_1\\I_e/p_2\\I_e/l\end{pmatrix}$$

Bisognerà poi studiare la stabilità di questo equilibrio, tenendo presente che $u\neq0$.

> [!tip] Interpretazione
> Ogni anno di corso ha in media $I_e/p$ studenti: se il primo anno si supera con probabilità $p_1=0{,}5$, ci sono il doppio degli studenti degli immatricolati. La stabilità di questo equilibrio è la stessa del sistema senza ingresso (la matrice dinamica è sempre $A$), quindi è asintotica: qualunque sia la situazione iniziale, la popolazione tende a $x_e$.
