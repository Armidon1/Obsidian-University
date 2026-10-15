---
title: Pascal, Geometrica, Massimo e Minimo
aliases:
  - PS — Pascal, Geometrica, Massimo e Minimo
tags:
  - probabilita-e-statistica
  - distribuzioni
  - geometrica
  - pascal
  - assenza-di-memoria
source: pdf/Probabilità e Statistica Dispensa.pdf
---

# Pascal, Geometrica, Massimo e Minimo

> [!abstract]
> La [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme|binomiale]] fissa il numero di prove e conta i successi. Qui si ribalta la domanda: in un **processo di Bernoulli** (prove indipendenti tutte con la stessa $p$) si chiede **quanto bisogna aspettare**. La **geometrica** conta le prove fino al primo successo, la **Pascal** (binomiale negativa) i fallimenti prima dell'$n$-esimo successo.
> Della geometrica si studiano la proprietà di **assenza di memoria** e il fatto che il **minimo di geometriche indipendenti è ancora geometrico** — entrambi argomenti espliciti del programma e delle [[10 - PS - Formulario e Domande d'Orale#Domande d'orale|domande d'orale]].
> Mappa del corso: [[MOC - Probabilità e Statistica]].

---

## Variabili aleatorie di Pascal

Vedi [[Distribuzione di Pascal]].

La distribuzione **di Pascal** (o **binomiale negativa**) è una distribuzione discreta con due parametri, $p$ (probabilità) e $n$, che descrive il **numero di fallimenti precedenti il successo $n$-esimo** in un processo di Bernoulli di parametro $p$.

> [!note] Processo di Bernoulli
> Si dice **processo di Bernoulli** una sequenza di esperimenti di Bernoulli di uguale parametro $p$, tra loro indipendenti. Un **esperimento bernoulliano** (o prova di Bernoulli) è un esperimento aleatorio con solo due esiti possibili, che chiamiamo convenzionalmente successo e insuccesso, con probabilità $p$ e $1-p$.

Detto altrimenti, la binomiale negativa descrive il numero di prove necessarie per ottenere un certo numero di successi in una serie di prove indipendenti. La distribuzione di Pascal $NB(p,n)$ descrive la v.a. $T_n$ che conta il numero di **fallimenti** che precedono il successo numero $n$ (ovvero il numero di prove necessarie a ottenere l'$n$-esimo successo, meno $n$ stesso).

**PMF.** Ci sono esattamente $k$ fallimenti prima di ottenere $n$ successi se e solo se:
- la prova numero $k+n$ è un successo ($X_{k+n}=1$), **e**
- nelle $k+n-1$ prove precedenti ci sono esattamente $k$ fallimenti e $n-1$ successi.

Per l'indipendenza:
$$\boxed{P(T_n=k)=\binom{k+n-1}{k}p^n q^k}\qquad q=1-p,\quad k=0,1,2,\dots$$
dove il coefficiente binomiale conta le possibili combinazioni di successi e fallimenti nelle prime $k+n-1$ prove.

**Legame con la geometrica.** La v.a. $T_n$ si scompone come somma: sia $Y_i$ il numero di prove tra il successo $i-1$ e il successo $i$ (incluso). Le $Y_1,\dots,Y_n$ sono indipendenti e hanno distribuzione [[#Variabili aleatorie geometriche|geometrica]] di parametro $p$; ognuna conta anche la prova finale del successo, quindi per avere i soli fallimenti bisogna togliere 1 a ciascuna:
$$T_n=(Y_1-1)+(Y_2-1)+\dots+(Y_n-1)=Y_1+\dots+Y_n-n\qquad Y_i\sim\mathrm{Geom}(p)$$
In particolare $NB(p,1)$ coincide con la geometrica meno 1 ($\mathcal G(p)-1$), e la somma di Pascal indipendenti con lo stesso $p$ è ancora Pascal.

**Valore atteso e varianza.** Per linearità e indipendenza, usando i risultati della geometrica ($E[Y_i]=\frac1p$, $\mathrm{Var}(Y_i)=\frac q{p^2}$):
$$E[T_n]=n\Big(\frac1p-1\Big)=\boxed{\frac{nq}{p}}\qquad\qquad\mathrm{Var}(T_n)=\boxed{\frac{nq}{p^2}}$$

> [!warning] Correzione
> La dispensa (pp. 60–62), lo schema riassuntivo (p. 84) e il file `distribuzioni.pdf` scrivono:
> - $T_n=Y_1+\dots+Y_n-1$ ("$-1$ perché sottraggo l'$n$-esimo successo"): per contare i **fallimenti** bisogna invece togliere **un successo per ogni** $Y_i$, cioè $-n$;
> - $E[T_n]=\frac np$: questo è il valore atteso del numero di **prove** $Y_1+\dots+Y_n$ necessarie per $n$ successi. Per il numero di **fallimenti**, che è quello descritto dalla PMF $\binom{k+n-1}kp^nq^k$, il valore atteso è $\frac{nq}p=\frac np-n$.
>
> La varianza $\frac{nq}{p^2}$ è invece corretta in entrambe le versioni (togliere la costante $n$ non cambia la varianza). All'esame conviene dichiarare quale delle due v.a. si usa.

_(dispensa, pp. 60–62)_

---

## Variabili aleatorie geometriche

Vedi [[Distribuzione Geometrica]].

La distribuzione **geometrica** è una distribuzione discreta sui numeri naturali **senza lo 0** che segue una **progressione geometrica** (una successione in cui il rapporto tra un elemento e il precedente è costante; la costante si chiama *ragione*):

$$\boxed{P(X=k)=p(1-p)^{k-1}=q^{k-1}p}\qquad k=1,2,\dots$$

È la probabilità che il **primo successo** richieda l'esecuzione di $k$ prove indipendenti, ognuna con probabilità di successo $p$: le prime $k-1$ falliscono (fattore $q^{k-1}$) e la $k$-esima riesce (fattore $p$). Si scrive $X\sim\mathrm{Geom}(p)$ o $\mathcal G(p)$.

Esiste una seconda versione, che conta i **fallimenti** prima del primo successo (è la $NB(p,1)$ vista sopra):
$$P(Y=k)=p(1-p)^k\qquad k=0,1,2,\dots\qquad(Y=X-1)$$
In entrambi i casi la successione delle probabilità è una **serie geometrica**.

> [!note] È una PMF?
> $\displaystyle\sum_{k\ge1}pq^{k-1}=p\sum_{j\ge0}q^j=p\cdot\frac1{1-q}=1$. Questo risultato è importante: per quanto piccola sia la probabilità $p$ che un evento accada, in un processo di Bernoulli **prima o poi** accadrà (è il "teorema della scimmia instancabile").

### Valore atteso

Si usa il trucco della derivata della serie geometrica $\sum_{i\ge0}q^i=\frac1{1-q}$, valida per $0\le q<1$:

$$
\begin{aligned}
E[X]&=\sum_{i=1}^\infty i\,p(1-p)^{i-1}=p\sum_{i=1}^\infty i\,q^{i-1}=p\,\frac{d}{dq}\sum_{i=1}^\infty q^i\\
&=p\,\frac d{dq}\Big(\frac1{1-q}\Big)=p\cdot\frac1{(1-q)^2}=\frac p{p^2}=\boxed{\frac1p}
\end{aligned}
$$

(si può derivare termine a termine perché la serie di potenze converge per $|q|<1$; la costante $q^0=1$ ha derivata nulla, quindi aggiungerla o toglierla non cambia nulla). Intuitivamente: se un evento ha probabilità $\frac16$, in media servono 6 tentativi.

### Varianza

Serve $E[X^2]=\sum_ii^2p(1-p)^{i-1}$. Il trucco è scrivere $i^2=i(i-1)+i$:
$$E[X^2]=p\sum_{i=1}^\infty i(i-1)(1-p)^{i-1}+\underbrace{p\sum_{i=1}^\infty i(1-p)^{i-1}}_{E[X]}$$
Nel primo termine il caso $i=1$ è nullo; raccogliendo $(1-p)$ e riconoscendo una derivata seconda rispetto a $p$:
$$
\begin{aligned}
p\sum_{i=2}^\infty i(i-1)(1-p)^{i-1}&=p(1-p)\sum_{i=2}^\infty i(i-1)(1-p)^{i-2}=p(1-p)\frac{d^2}{dp^2}\Big(\sum_i(1-p)^i\Big)\\
&=p(1-p)\frac{d^2}{dp^2}\Big(\frac1p\Big)=p(1-p)\cdot\frac2{p^3}=\frac{2(1-p)}{p^2}
\end{aligned}
$$
Quindi $E[X^2]=\frac{2(1-p)}{p^2}+\frac1p=\frac2{p^2}-\frac1p$ e
$$\mathrm{Var}(X)=E[X^2]-E[X]^2=\frac2{p^2}-\frac1p-\frac1{p^2}=\frac1{p^2}-\frac1p=\frac{1-p}{p^2}=\boxed{\frac q{p^2}}$$

_(dispensa, pp. 63–66)_

---

## Assenza di memoria

Vedi [[Assenza di Memoria]].

La distribuzione geometrica è **priva di memoria**:

$$P(T=m+n\mid T>m)=P(T=n)$$

ed è l'**unica** distribuzione discreta con questa proprietà. **L'indipendenza delle prove** in un processo di Bernoulli implica l'assenza di memoria della distribuzione geometrica. Viceversa, ogni v.a. $T$ sui naturali priva di memoria soddisfa
$$P(T=n)=P(T=n+1\mid T>1)=\frac{P(T=n+1)}{P(T>1)}$$
e quindi ha distribuzione geometrica di parametro $P(T=1)$.

> [!note] Caratterizzazione
> Una v.a. discreta (risp. continua) $X$ possiede **mancanza di memoria** se per ogni $x,y$ naturali (risp. reali) non negativi
> $$P(X>x+y\mid X>y)=P(X>x)$$
> Sapendo che $X$ ha già superato $y$ (il tempo d'attesa è più di $y$), la probabilità che ritardi ancora di almeno $x$ è la stessa che aveva all'inizio della misurazione.
> Questo **non** vuol dire che gli eventi $(X>x+y)$ e $(X>y)$ siano indipendenti: sotto l'ipotesi di assenza di memoria, lo sono se e solo se $P(X>x)=P(X>x+y)$.

> [!important] Proposizione — mancanza di memoria della geometrica
> Sia $X\sim\mathcal G(p)$. Allora
> $$P(X>k)=(1-p)^k\qquad\qquad P(X=k+m\mid X>k)=P(X=m)$$

*Dimostrazione.*
$$P(X>k)=\sum_{i=k+1}^\infty p(1-p)^{i-1}=p(1-p)^k\sum_{i=0}^\infty(1-p)^i=p(1-p)^k\cdot\frac1{1-(1-p)}=(1-p)^k$$
(cambio indice $i\to i+k+1$ e serie geometrica). Più semplicemente: $X>k$ vuol dire che le prime $k$ prove falliscono. Poi, siccome $\{X=k+m\}\subseteq\{X>k\}$, l'intersezione dei due eventi è $\{X=k+m\}$:
$$P(X=k+m\mid X>k)=\frac{P(X=k+m)}{P(X>k)}=\frac{p(1-p)^{k+m-1}}{(1-p)^k}=p(1-p)^{m-1}=P(X=m)\qquad\square$$

> [!tip] Interpretazione
> La prima relazione motiva la definizione di v.a. geometrica; la seconda esprime il fatto che, in uno schema a prove ripetute indipendenti, **i risultati delle prime prove non influiscono sulle successive**. Così la probabilità che il 13 esca sulla ruota di Napoli **non aumenta** se il 13 non è uscito per 100 settimane di seguito: i "numeri ritardatari" non esistono.

L'assenza di memoria è una proprietà **solamente** della distribuzione geometrica (nel discreto) e di quella **esponenziale** (nel continuo).

**Funzione di ripartizione.**
$$P(X\le k)=\sum_{i=1}^kp(1-p)^{i-1}=p\sum_{i=0}^{k-1}q^i=p\cdot\frac{q^k-1}{q-1}=p\cdot\frac{(1-p)^k-1}{-p}=\boxed{1-(1-p)^k}$$
(somma geometrica finita $\sum_{i=0}^{N}x^i=\frac{x^{N+1}-1}{x-1}$ per $x\ne1$). Oppure, più rapidamente, dal complementare: $P(X\le k)=1-P(X>k)=1-(1-p)^k$. _(dispensa, pp. 66–67)_

---

## Massimo e minimo di variabili aleatorie indipendenti

Vedi [[Massimo e Minimo di Variabili Indipendenti]].

> [!important] Proposizione 2.6.4
> Siano $X_1,\dots,X_n$ v.a. reali **indipendenti** e definiamo $Z=\max(X_1,\dots,X_n)$, $W=\min(X_1,\dots,X_n)$. Allora
> $$F_Z(x)=\prod_{k=1}^nF_{X_k}(x)\qquad\qquad F_W(x)=1-\prod_{k=1}^n\big[1-F_{X_k}(x)\big]$$

*Dimostrazione.* Il massimo è $\le x$ se e solo se **tutte** le $X_k$ sono $\le x$:
$$\{Z\le x\}=\bigcap_{k=1}^n\{X_k\le x\}\quad\Longrightarrow\quad F_Z(x)=P(Z\le x)=\prod_{k=1}^nP(X_k\le x)=\prod_{k=1}^nF_{X_k}(x)$$
usando l'indipendenza. Il minimo è $>x$ se e solo se tutte le $X_k$ sono $>x$:
$$\{W>x\}=\bigcap_{k=1}^n\{X_k>x\}\quad\Longrightarrow\quad1-F_W(x)=P(W>x)=\prod_{k=1}^nP(X_k>x)=\prod_{k=1}^n\big[1-F_{X_k}(x)\big]$$

> [!tip] Trucco da ricordare
> Per il **massimo** si lavora con $P(\cdot\le x)$, per il **minimo** con la **funzione di sopravvivenza** $P(\cdot>x)$. Se le $X_i$ sono anche identicamente distribuite (somiglianti): $F_Y(y)=[F_X(y)]^n$ per il massimo e $1-F_T(t)=[1-F_X(t)]^n$ per il minimo.

### Il minimo di geometriche è geometrico

> [!example] Esempio 2.6.2
> Siano $X_1,\dots,X_n\sim\mathrm{Ge}(p)$ indipendenti. Dalla CDF della geometrica, $F_{X_i}(k)=1-(1-p)^k$, quindi:
> - **massimo**: $F_Z(k)=\big[1-(1-p)^k\big]^n$;
> - **minimo**: $F_W(k)=1-\big[(1-p)^k\big]^n=1-\big[(1-p)^n\big]^k$.
>
> L'ultima espressione coincide con la funzione di ripartizione di una geometrica di parametro $1-(1-p)^n$: infatti se $Y\sim\mathrm{Geom}(\tilde p)$ con $\tilde p=1-(1-p)^n$, allora $P(Y\le k)=1-(1-\tilde p)^k=1-\big[(1-p)^n\big]^k$. Poiché la funzione di ripartizione individua completamente la distribuzione,
> $$\boxed{W=\min(X_1,\dots,X_n)\sim\mathrm{Ge}\big(1-(1-p)^n\big)}$$

**Esempio per $n=2$.** Con $P(X=k)=p(1-p)^{k-1}$ la funzione di ripartizione è $F_X(k)=1-q^k$. Per il minimo si usa la funzione di sopravvivenza $S_X(k)=P(X>k)=1-F=q^k$:
$$S_{\min}(k)=P(\min(X,Y)>k)=P(X>k,\,Y>k)=P(X>k)P(Y>k)=q^{2k}$$
quindi $F_{\min}(k)=1-(1-p)^{2k}$: una geometrica di parametro $\tilde p$ con $1-\tilde p=q^2$, cioè $\tilde p=1-q^2$.

> [!tip] Intuizione
> Faccio partire in parallelo $n$ processi di Bernoulli indipendenti e mi fermo al primo successo di uno qualunque. A ogni "turno" fallisce tutto con probabilità $(1-p)^n$, quindi il turno ha successo con probabilità $1-(1-p)^n$: il tempo d'attesa è geometrico con questo parametro.

_(dispensa, pp. 68–69)_

> [!note] Nota — $P(X=Y)$ per v.a. indipendenti
> Date due v.a. indipendenti a valori interi,
> $$P(X=Y)=\sum_kP(X=k,\,Y=k)=\sum_kP(X=k)\,P(Y=k)$$
> dove gli estremi della sommatoria dipendono dal tipo di distribuzione delle due v.a. _(dispensa, p. 86)_

---

## Esercizi svolti

> [!example] Esercizio 1 — due geometriche indipendenti
> *$X\sim\mathrm{Geom}(\frac12)$ e $Y\sim\mathrm{Geom}(\frac14)$ indipendenti. (a) $P(X=Y)$; (b) $P(X=1\mid X+Y=3)$.*
> (a) Con la nota qui sopra:
> $$P(X=Y)=\sum_{k=1}^\infty\Big(\frac12\Big)^k\cdot\frac14\Big(\frac34\Big)^{k-1}=\frac18\sum_{k=1}^\infty\Big(\frac38\Big)^{k-1}=\frac18\cdot\frac1{1-\frac38}=\frac18\cdot\frac85=\frac15$$
> (b) $X+Y=3$ con $X,Y\ge1$ si ottiene solo con $(1,2)$ o $(2,1)$:
> $$P(X=1,Y=2)=\frac12\cdot\frac14\cdot\frac34=\frac3{32}\qquad P(X=2,Y=1)=\frac14\cdot\frac14=\frac2{32}$$
> $$P(X=1\mid X+Y=3)=\frac{3/32}{5/32}=\frac35$$
>
> > [!warning] Correzione
> > Negli esercizi (p. 17) il punto (b) è risolto sostituendo $P(X=1\mid X+Y=3)$ con $P(X=1\mid Y=2)=P(X=1)=\frac12$. Non è lecito: condizionare a $X+Y=3$ non equivale a condizionare a $Y=2$, perché $\{X+Y=3\}$ contiene anche il caso $X=2,Y=1$. Il risultato corretto è $\frac35$.

> [!example] Esercizio 2 — la sfida a scacchi
> *Albino e Ben giocano finché uno dei due vince una partita; risultati indipendenti, Albino vince con probabilità $\frac12$, Ben con $\frac13$.*
> (a) Patta: $1-\frac12-\frac13=\frac16$.
> (b) La sfida finisce alla prima partita non patta: il numero di partite $Z$ è geometrico con $p=\frac12+\frac13=\frac56$, quindi $E[Z]=\frac65$.
> (c) Albino vince se tutte le partite fino all'ultima sono patte e l'ultima la vince lui:
> $$P(\text{Albino})=\sum_{i=1}^\infty\Big(\frac16\Big)^{i-1}\frac12=\frac12\cdot\frac1{1-\frac16}=\frac35\qquad P(\text{Ben})=\frac25$$
> _(esercizi, pp. 19–20)_

> [!example] Esercizio d'esame (luglio) — Aldo e Bruno
> *Aldo e Bruno tirano con l'arco a turni finché solo uno dei due centra il bersaglio; tiri indipendenti, Aldo centra con probabilità $\frac9{10}$, Bruno con $\frac45$.*
> - $P(\text{stesso risultato in un turno})=\frac9{10}\cdot\frac45+\frac1{10}\cdot\frac15=\frac{36}{50}+\frac1{50}=\frac{37}{50}$.
> - Sapendo che al primo turno i risultati sono diversi, Aldo vince con probabilità $\frac{P(X=1,Y=0)}{P(X\ne Y)}=\frac{9/50}{13/50}=\frac9{13}$.
> - Probabilità che la sfida sia vinta da Aldo: $\sum_i\big(\frac{37}{50}\big)^{i-1}\frac9{50}=\frac{9/50}{13/50}=\frac9{13}$ — lo stesso numero, per l'**assenza di memoria**: i turni "pari" non contano.
> - Numero di turni: geometrico di parametro $\frac{13}{50}$, con valore atteso $\frac{50}{13}\approx3{,}85$.
> _(esercizi, pp. 55–57)_
