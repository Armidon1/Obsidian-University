---
title: Distribuzione di Poisson
aliases:
  - PS — Distribuzione di Poisson
tags:
  - probabilita-e-statistica
  - distribuzioni
  - poisson
  - eventi-rari
source: pdf/Probabilità e Statistica Dispensa.pdf
---

# Distribuzione di Poisson

> [!abstract]
> La **Poisson** è la distribuzione degli **eventi rari**: conta quante volte succede qualcosa in un intervallo di tempo (o di spazio) sapendo solo quante volte succede **in media**. Si ottiene come limite della [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Variabili aleatorie binomiali|binomiale]] con $n$ grande e $p$ piccolo, e ha proprietà molto comode: media e varianza coincidono con il parametro $\lambda$, la somma di Poisson indipendenti è Poisson, e "smistando" a caso gli eventi di una Poisson in più tipi si ottengono Poisson indipendenti. Le "proprietà della v.a. di Poisson" sono una delle [[10 - PS - Formulario e Domande d'Orale#Domande d'orale|domande d'orale]].
> Per $\lambda$ grande la Poisson sarà a sua volta approssimata dalla [[09 - PS - Distribuzione Normale e Teorema del Limite Centrale#Approssimazione normale della Poisson|normale]].
> Mappa del corso: [[MOC - Probabilità e Statistica]].

---

## Variabile aleatoria di Poisson

Vedi [[Distribuzione di Poisson]].

La distribuzione **di Poisson** è una distribuzione discreta che esprime le probabilità per il **numero di eventi** che si verificano successivamente e indipendentemente in un dato intervallo di tempo, sapendo che **mediamente** se ne verifica un numero $\lambda$. Ad esempio si usa per il numero di chiamate ricevute da un call-center in una mattinata lavorativa. È nota anche come **legge degli eventi rari**.

> [!important] Definizione
> La distribuzione di Poisson $\mathcal P_\lambda$ è data da
> $$\boxed{P(X=i)=\frac{\lambda^i}{i!}e^{-\lambda}}\qquad i\in\mathbb N=\{0,1,2,\dots\}$$
> dove $\lambda>0$ è il numero medio di eventi per intervallo di tempo e $i$ è il numero di eventi nell'intervallo (lo stesso con cui si misura $\lambda$) di cui si vuole la probabilità. Si scrive $X\sim\mathrm{Poi}(\lambda)$.

La formula permette di calcolare la probabilità che si presentino $i$ casi conoscendo il numero medio di casi $\lambda$.

**È una PMF accettabile**: dallo sviluppo in serie dell'esponenziale $e^\lambda=\sum_{n=0}^\infty\frac{\lambda^n}{n!}$ si trova $\sum_{i\ge0}\frac{\lambda^i}{i!}e^{-\lambda}=e^{\lambda}e^{-\lambda}=1$.

> [!note] Requisiti per una distribuzione di Poisson
> Suddividendo l'intervallo in un numero molto grande di sottointervalli, devono valere:
> 1. la probabilità che si verifichi un evento è **costante** in tutti i sottointervalli;
> 2. l'evento non può verificarsi **più di una volta** in ciascun sottointervallo;
> 3. eventi che si verificano in intervalli **disgiunti** sono indipendenti.
>
> Sono esattamente le ipotesi di una binomiale con tantissime prove ($n$ = numero di sottointervalli) e probabilità piccolissima per prova: per questo la Poisson è il limite della binomiale ([[#Approssimazione della binomiale con la Poisson|più sotto]]).

### Valore atteso e varianza

**Valore atteso.** Il termine $i=0$ è nullo; semplificando $i$ con $i!$ e cambiando indice:
$$E[X]=\sum_{i=0}^\infty i\frac{\lambda^i}{i!}e^{-\lambda}=\sum_{i=1}^\infty\frac{\lambda^i}{(i-1)!}e^{-\lambda}=\lambda e^{-\lambda}\sum_{i=1}^\infty\frac{\lambda^{i-1}}{(i-1)!}=\lambda e^{-\lambda}\sum_{j=0}^\infty\frac{\lambda^j}{j!}=\boxed{\lambda}$$

**Varianza.** Per $E[X^2]$ si usa ancora $i^2=i(i-1)+i$:
$$E[X^2]=\sum_{i=0}^\infty i(i-1)\frac{\lambda^i}{i!}e^{-\lambda}+\underbrace{\sum_{i=0}^\infty i\frac{\lambda^i}{i!}e^{-\lambda}}_{=\lambda}$$
Per $i=0$ e $i=1$ il primo termine si annulla; semplificando $i(i-1)$ con $i!$:
$$\sum_{i=2}^\infty\frac{\lambda^i}{(i-2)!}e^{-\lambda}+\lambda=\lambda^2e^{-\lambda}\sum_{i=2}^\infty\frac{\lambda^{i-2}}{(i-2)!}+\lambda=\lambda^2+\lambda$$
$$\mathrm{Var}(X)=\lambda^2+\lambda-\lambda^2=\boxed{\lambda}$$

> [!important]
> **Valore atteso e varianza coincidono con il parametro $\lambda$.** È una "firma" della Poisson: se in un esercizio una v.a. di conteggio ha media e varianza uguali, è un indizio che sia Poisson.

### Esempi di variabili di Poisson

Seguono con buona approssimazione la legge di Poisson, per una qualche scelta di $\lambda$:
1. il numero di refusi in una pagina (o in un insieme di pagine) di un libro;
2. il numero di individui, in una certa categoria di persone, che raggiungono i cento anni di età;
3. la quantità di numeri telefonici errati composti in una giornata;
4. il numero di transistor che si guastano nel loro primo giorno di utilizzo;
5. il numero di clienti che entrano in un ufficio postale nell'arco di una giornata;
6. la quantità di particelle alfa emesse in un periodo di tempo fissato da un campione di materiale radioattivo.

In tutti i casi ci sono moltissime "occasioni" (lettere, persone, numeri composti, …) e per ciascuna una probabilità piccola dell'evento. _(dispensa, pp. 70–72)_

---

## Approssimazione della binomiale con la Poisson

Vedi [[Approssimazione di Poisson della Binomiale]].

Per $n$ molto grande, la binomiale richiede uno sforzo di calcolo notevole (i fattoriali esplodono). Quando $p\to0$ si può approssimare la binomiale con una Poisson: la condizione $p\to0$, per cui si realizza la convergenza, definisce la Poisson come distribuzione degli eventi rari. L'ultima condizione è che il prodotto $np$ resti costante.

> [!important] Approssimazione
> Si può approssimare la binomiale di parametri $(n,p)$ con la Poisson di parametro $\lambda=np$, se $p\to0$ e $n$ è molto grande.

*Perché.* Sia $X\sim B(n,p)$ e poniamo $\lambda=np$, cioè $p=\frac\lambda n$. Allora
$$P(X=i)=\frac{n!}{(n-i)!\,i!}\Big(\frac\lambda n\Big)^i\Big(1-\frac\lambda n\Big)^{n-i}=\frac{n(n-1)\cdots(n-i+1)}{n^i}\cdot\frac{\lambda^i}{i!}\cdot\frac{(1-\lambda/n)^n}{(1-\lambda/n)^i}$$
Se $n$ è molto grande e $p$ molto piccolo valgono le approssimazioni
$$\Big(1-\frac\lambda n\Big)^n\approx e^{-\lambda}\qquad\frac{n(n-1)\cdots(n-i+1)}{n^i}\approx1\qquad\Big(1-\frac\lambda n\Big)^i\approx1$$
quindi, se $n$ è grande, $p$ piccolo e $\lambda=np$:
$$P(X=i)\approx\frac{\lambda^i}{i!}e^{-\lambda}$$

In altri termini, **il totale dei successi in un gran numero $n$ di ripetizioni indipendenti di un esperimento che ha una piccola probabilità di riuscita $p$ è una v.a. con distribuzione approssimativamente di Poisson con media $\lambda=np$.** _(dispensa, p. 73)_

> [!example] Esercizio svolto — le famiglie numerose
> *La probabilità che una famiglia abbia almeno 6 componenti è $\frac1{100}$. Si scelgono a caso 300 famiglie: probabilità che meno di 3 abbiano almeno 6 componenti?*
> Sia $Z$ il numero di famiglie con almeno 6 componenti: $Z\sim B(300,\frac1{100})$, con $n$ grande e $p$ piccolo, quindi $Z\approx\mathrm{Poi}(3)$.
> $$P(Z<3)=P(Z\le2)=e^{-3}\Big(1+3+\frac{9}{2}\Big)=8{,}5\,e^{-3}\approx0{,}423$$
>
> > [!warning] Correzione
> > Negli esercizi (pp. 32–33) si calcola $P(Z\le3)$, che include anche il caso $Z=3$ ($\approx0{,}647$). "Meno di 3" vuol dire $Z\in\{0,1,2\}$.

---

## Somma di Poisson indipendenti

Vedi [[Somma di Poisson Indipendenti]].

La distribuzione di Poisson è **riproducibile**: la somma di due poissoniane **indipendenti** è ancora una poissoniana.

> [!important] Proprietà
> Se $Y_1\sim\mathrm{Poi}(\lambda_1)$ e $Y_2\sim\mathrm{Poi}(\lambda_2)$ sono indipendenti, la loro somma $Y=Y_1+Y_2$ è $\mathrm{Poi}(\lambda_1+\lambda_2)$. Più in generale, la somma $Y=Y_1+\dots+Y_n$ di $n$ Poisson indipendenti di parametri $\lambda_1,\dots,\lambda_n$ è Poisson di parametro $\lambda=\lambda_1+\dots+\lambda_n$.

**Idea (dalla somma di binomiali).** Due Poisson di parametro $\lambda$ sono il limite, per $n\to\infty$, della binomiale $B(n,\frac\lambda n)$. Sommandole (come binomiali indipendenti con lo stesso $p$) si ottiene $B(2n,\frac\lambda n)$, che con $m=2n$ si riscrive $B(m,\frac{2\lambda}m)$ e tende alla Poisson di parametro $2\lambda$. Allo stesso modo, con parametri diversi $\lambda$ e $\mu$, si ottiene $\lambda+\mu$.

**Dimostrazione rigorosa** (direttamente sulle PMF). Siano $U\sim\mathrm{Poi}(\lambda)$ e $V\sim\mathrm{Poi}(\mu)$ indipendenti. L'evento $\{U+V=k\}$ si scompone nell'unione disgiunta di tutte le coppie di valori con somma $k$:
$$\{U+V=k\}=\bigcup_{i=0}^k\{U=i,\,V=k-i\}$$
e per l'indipendenza $P(U=i,V=k-i)=p_U(i)\,p_V(k-i)$. Quindi
$$
\begin{aligned}
P(U+V=k)&=\sum_{i=0}^ke^{-\lambda}\frac{\lambda^i}{i!}\cdot e^{-\mu}\frac{\mu^{k-i}}{(k-i)!}=e^{-(\lambda+\mu)}\sum_{i=0}^k\frac{\lambda^i\mu^{k-i}}{(k-i)!\,i!}\\
&=\frac{e^{-(\lambda+\mu)}}{k!}\sum_{i=0}^k\binom ki\lambda^i\mu^{k-i}=\frac{e^{-(\lambda+\mu)}}{k!}(\lambda+\mu)^k
\end{aligned}
$$
moltiplicando e dividendo per $k!$ per far comparire il coefficiente binomiale, e riconoscendo lo sviluppo del binomio di Newton. È la PMF di una Poisson di parametro $\lambda+\mu$. $\square$ _(dispensa, pp. 73–74)_

> [!example] Esercizio svolto — binomiali "rare" sommate
> *$X\sim B(400,\frac1{100})$ e $Y\sim B(400,\frac3{100})$ indipendenti. (a) $P(X+Y=3)$; (b) approssimazione di Poisson di $P(X+Y=k)$; (c) $E[X(X+Y)]$.*
> (a) Esatto: $P(X+Y=3)=\sum_{i=0}^3P(X=i)P(Y=3-i)$ (quattro termini, non due: anche $(0,3)$ e $(3,0)$).
> (b) $X\approx\mathrm{Poi}(4)$, $Y\approx\mathrm{Poi}(12)$, e la somma di Poisson indipendenti è $\mathrm{Poi}(16)$:
> $$P(X+Y=k)\approx\frac{16^k}{k!}e^{-16}\qquad P(X+Y=3)\approx\frac{16^3}{3!}e^{-16}\approx7{,}7\cdot10^{-5}$$
> (c) Per linearità e indipendenza: $E[X(X+Y)]=E[X^2]+E[X]E[Y]$. Con $E[X]=4$, $\mathrm{Var}(X)=400\cdot0{,}01\cdot0{,}99=3{,}96$, $E[X^2]=3{,}96+16=19{,}96$ e $E[Y]=12$:
> $$E[X(X+Y)]=19{,}96+48=67{,}96$$
>
> > [!warning] Correzione
> > Negli esercizi (p. 48) il punto (a) considera solo le coppie $(2,1)$ e $(1,2)$; mancano $(0,3)$ e $(3,0)$.

---

## Somma di un numero Poisson di Bernoulli indipendenti

Vedi [[Suddivisione di una Poisson]].

Il risultato che segue è in un certo senso l'inverso della riproducibilità. Consideriamo una situazione in cui si verifica un numero casuale $N$ di eventi, ciascuno dei quali, **indipendentemente** dagli altri (e da $N$), può essere di tipo 1 con probabilità $p$ o di tipo 2 con probabilità $1-p$. Siano $N_1$ e $N_2$ i numeri di eventi dei due tipi ($N=N_1+N_2$), e supponiamo che $N\sim\mathrm{Poi}(\lambda)$.

**PMF congiunta di $N_1$ e $N_2$.** Si condiziona al numero totale di eventi:
$$P(N_1=n,N_2=m)=P(N_1=n,\,N=n+m)=P(N_1=n\mid N=n+m)\,P(N=n+m)$$
Se ci sono in tutto $n+m$ eventi, e ciascuno è di tipo 1 con probabilità $p$ indipendentemente dagli altri, il numero di eventi di tipo 1 è binomiale $B(n+m,p)$. Di conseguenza
$$
\begin{aligned}
P(N_1=n,N_2=m)&=\binom{n+m}np^n(1-p)^m\cdot\frac{\lambda^{n+m}}{(n+m)!}e^{-\lambda}=\frac{(n+m)!}{n!\,m!}p^n(1-p)^m\frac{\lambda^{n+m}}{(n+m)!}e^{-\lambda}\\
&=\frac{(\lambda p)^n}{n!}e^{-\lambda p}\cdot\frac{\big(\lambda(1-p)\big)^m}{m!}e^{-\lambda(1-p)}
\end{aligned}
$$
spezzando $e^{-\lambda}=e^{-\lambda p}\,e^{-\lambda(1-p)}$.

**Marginali.** Sommando su $m$, il secondo fattore è la PMF di una Poisson e la sua serie fa 1:
$$P(N_1=n)=\sum_{m=0}^\infty P(N_1=n,N_2=m)=\frac{(\lambda p)^n}{n!}e^{-\lambda p}\qquad\text{e analogamente}\qquad P(N_2=m)=\frac{\big(\lambda(1-p)\big)^m}{m!}e^{-\lambda(1-p)}$$

Dal confronto tra la congiunta e le marginali (la congiunta è il **prodotto** delle marginali) segue che:

> [!important]
> **$N_1$ e $N_2$ sono v.a. indipendenti, con distribuzione di Poisson di media $\lambda p$ e $\lambda(1-p)$.**
> Più in generale: se $N$ eventi, con $N\sim\mathrm{Poi}(\lambda)$, vengono classificati nei tipi $1,2,\dots,r$ indipendentemente l'uno dall'altro con probabilità $p_1,\dots,p_r$ ($p_1+\dots+p_r=1$), allora le quantità totali di eventi dei diversi tipi sono v.a. di Poisson **indipendenti** di medie $\lambda p_1,\lambda p_2,\dots,\lambda p_r$.

Il fatto sorprendente è l'indipendenza: con un $N$ fissato, $N_1$ e $N_2$ sarebbero fortemente dipendenti ($N_2=N-N_1$); è la casualità di $N$, proprio di tipo Poisson, a renderli indipendenti. _(dispensa, p. 75)_

### Distribuzione di una Poisson condizionata alla somma di Poisson

Collegamento con la binomiale: se $Y_1,\dots,Y_n$ sono Poisson indipendenti di parametri $\lambda_1,\dots,\lambda_n$ e $Y=Y_1+\dots+Y_n\sim\mathrm{Poi}(\lambda)$ con $\lambda=\lambda_1+\dots+\lambda_n$, allora

$$Y_1\mid Y=n\;\sim\;B\Big(n,\;\frac{\lambda_1}{\lambda}\Big)$$

*Perché $p=\frac{\lambda_1}\lambda$?* $p$ è la probabilità che un singolo evento, tra gli $n$ osservati, sia "di tipo 1". Nello schema della sezione precedente, se gli eventi di tipo 1 hanno media $\lambda_1=\lambda p$ e quelli totali media $\lambda$, il rapporto delle medie è proprio $\frac{\lambda_1}{\lambda}=p$: la frazione attesa di eventi di tipo 1 ("casi favorevoli su casi totali"). In modo diretto, è lo stesso conto dell'[[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Relazione tra binomiale e ipergeometrica|esempio 5.3.3]]:
$$P(Y_1=k\mid Y=n)=\frac{P(Y_1=k)P(Y-Y_1=n-k)}{P(Y=n)}=\binom nk\Big(\frac{\lambda_1}\lambda\Big)^k\Big(1-\frac{\lambda_1}\lambda\Big)^{n-k}$$
dove $Y-Y_1\sim\mathrm{Poi}(\lambda-\lambda_1)$ è indipendente da $Y_1$.

> [!note] Intervallo di tempo su cui si è stabilito $\lambda$
> Se ho una Poisson di parametro $\lambda$ misurato su un intervallo di tempo $T$, come cambia $\lambda$ al variare di $T$? Sono **direttamente proporzionali**: $T\to\lambda$, $2T\to2\lambda$, $\frac12T\to\frac12\lambda$. (È la somma di Poisson indipendenti applicata a intervalli disgiunti.)

_(dispensa, p. 76)_

---

## Calcolo esplicito della distribuzione di Poisson

Se $X$ è Poisson di media $\lambda$:
$$\frac{P(X=i+1)}{P(X=i)}=\frac{\lambda^{i+1}e^{-\lambda}}{(i+1)!}\cdot\frac{i!}{\lambda^ie^{-\lambda}}=\frac\lambda{i+1}$$

L'equazione si usa ricorsivamente a partire da $P(X=0)=e^{-\lambda}$:
$$P(X=1)=\lambda P(X=0)\qquad P(X=2)=\frac\lambda2P(X=1)\qquad\dots\qquad\boxed{P(X=i+1)=\frac\lambda{i+1}P(X=i)}$$

È l'analogo della [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Calcolo esplicito della distribuzione binomiale|ricorsione della binomiale]]. _(dispensa, p. 77)_

> [!example] Esercizio svolto — le uova difettose
> *Un uovo presenta almeno un piccolo difetto con probabilità 0,95023; il numero di difetti di un uovo è Poisson. Calcolare la media dei difetti per uovo e la probabilità che un uovo venga scartato (più di 5 difetti).*
> $P(X=0)=1-0{,}95023=0{,}04977=e^{-\lambda}$, quindi $\lambda=-\ln0{,}04977\approx3$: $E[X]=\mathrm{Var}(X)=3$.
> Con la ricorsione: $P(0)=0{,}0498$, $P(1)=3\cdot0{,}0498=0{,}1494$, $P(2)=\frac32\cdot0{,}1494=0{,}2240$, $P(3)=0{,}2240$, $P(4)=\frac34\cdot0{,}2240=0{,}1680$, $P(5)=\frac35\cdot0{,}1680=0{,}1008$. Quindi
> $$P(X>5)=1-(0{,}0498+0{,}1494+0{,}2240+0{,}2240+0{,}1680+0{,}1008)\approx0{,}084$$
> Un lotto di 10 uova ha in tutto $Y=\sum_{i=1}^{10}X_i\sim\mathrm{Poi}(30)$ difetti (somma di Poisson indipendenti). _(esercizi, pp. 39–41)_

> [!example] Esercizio svolto — i transistor difettosi
> *Una fabbrica produce ogni giorno $N\sim\mathrm{Poi}(10^5)$ transistor; ciascuno, indipendentemente, è difettoso con probabilità $2\cdot10^{-5}$. (a) Distribuzione dei difettosi in un giorno; (b) in 7 giorni; (c) probabilità di trovare almeno un giorno, sui 7, senza transistor difettosi.*
> (a) Per la suddivisione di una Poisson, i difettosi sono $N_1\sim\mathrm{Poi}(\lambda p)=\mathrm{Poi}(10^5\cdot2\cdot10^{-5})=\mathrm{Poi}(2)$.
> (b) Giorni indipendenti → somma di 7 Poisson: $\mathrm{Poi}(14)$.
> (c) In un giorno non ci sono difettosi con probabilità $P(N_1=0)=e^{-2}\approx0{,}135$. I 7 giorni sono indipendenti, quindi
> $$P(\text{almeno un giorno senza difettosi})=1-P(\text{tutti i giorni con difettosi})=1-(1-e^{-2})^7\approx1-0{,}361=0{,}639$$
>
> > [!warning] Correzione
> > Negli esercizi (pp. 25–27) si scrive $P(Y=0)=\sum_{i=1}^7P(Y_i=0)=7\,(1-e^{-\lambda p})$ e il risultato finale $1-7(1-e^{-\lambda p})$, che è negativo ($7\cdot0{,}865>1$). Per eventi **indipendenti** la probabilità che si verifichino tutti è il **prodotto**, non la somma: $P(Y=0)=\prod_{i=1}^7P(Y_i=0)=(1-e^{-2})^7$.

> [!example] Esercizio svolto — i tre pittori
> *Tre pittori ricevono ogni mese ordini indipendenti $N_1\sim\mathrm{Poi}(\frac52)$, $N_2\sim\mathrm{Poi}(3)$, $N_3\sim\mathrm{Poi}(3)$.*
> (a) Ordini complessivi: $N\sim\mathrm{Poi}(\frac52+3+3)=\mathrm{Poi}(\frac{17}2)$.
> (b) Sapendo che gli ordini totali sono 10, quelli del primo pittore sono binomiali $B\big(10,\frac{5/2}{17/2}\big)=B(10,\frac5{17})$:
> $$P(N_1=3\mid N=10)=\binom{10}3\Big(\frac5{17}\Big)^3\Big(\frac{12}{17}\Big)^7\approx0{,}26$$
> (c) Nei primi tre mesi ognuno riceve 9 ordini: su 3 mesi i parametri si triplicano ($\frac{15}2$, 9, 9) e per l'indipendenza
> $$P=\frac{(15/2)^9e^{-15/2}}{9!}\cdot\frac{9^9e^{-9}}{9!}\cdot\frac{9^9e^{-9}}{9!}$$
> _(esercizi, pp. 30–31)_
