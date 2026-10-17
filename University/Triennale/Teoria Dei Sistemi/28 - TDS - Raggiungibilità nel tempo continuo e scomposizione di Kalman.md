---
title: Raggiungibilità nel tempo continuo e scomposizione di Kalman
aliases:
  - TDS — Raggiungibilità nel tempo continuo e scomposizione di Kalman
tags:
  - teoria-dei-sistemi
  - raggiungibilita
  - scomposizione-di-kalman
  - gramiano
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 165–171); libro Monaco et al., §6.2–6.3
---

# Raggiungibilità nel tempo continuo e scomposizione di Kalman

> [!abstract] Scopo della lezione
> 1. La **raggiungibilità nel tempo continuo**: si costruisce esplicitamente un ingresso che porta lo stato da 0 a $x_R$ in un tempo $T$ qualsiasi, e si dimostra che funziona se e solo se la [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Raggiungibilità di uno stato nel tempo discreto|matrice di raggiungibilità]] ha rango pieno, come nel discreto.
> 2. Un **esempio** numerico di scomposizione rispetto alla raggiungibilità, e il rapporto (non sempre stretto) tra raggiungibilità ed eccitabilità.
> 3. La **scomposizione di Kalman**: unendo le due proprietà lo spazio di stato si divide in quattro sottospazi (raggiungibile/non, osservabile/non), e le matrici assumono una struttura a blocchi che mostra cosa "vede" l'esterno.
>
> Segue [[29 - TDS - Esercizi sulla scomposizione di Kalman]]. Indice: [[MOC - Teoria dei Sistemi]].

## Raggiungibilità nel caso continuo

Vedi [[TDS - Raggiungibilità]].

Nel tempo continuo uno stato $x_R$ è raggiungibile partendo da $x_0$ in un istante $T$ se esiste un ingresso tale che

$$x_R(T)=\Phi(T)x_0+\int_0^TH(T-\tau)u(\tau)\,d\tau$$

Il sistema è lineare, quindi si può porre $x_0=0$:

$$x_R(T)=\int_0^TH(T-\tau)u(\tau)\,d\tau$$

Si prova con un ingresso di una forma particolare:

$$u(t)=B'e^{-A't}M$$

dove $B'$ e $A'$ sono le trasposte di $B$ e $A$ e $M$ è un vettore costante (da scegliere). Si ottiene

$$x_R(T)=\int_0^Te^{A(T-\tau)}Bu(\tau)\,d\tau=e^{AT}\underbrace{\int_0^Te^{-A\tau}BB'e^{-A'\tau}\,d\tau}_{\text{termine costante}}\,M$$

L'integrale è definito, quindi è una matrice costante. Se è **invertibile** si può porre

$$M=\left[\int_0^Te^{-A\tau}BB'e^{-A'\tau}\,d\tau\right]^{-1}e^{-AT}x_R$$

e così

$$x_R(T)=e^{AT}\int_0^Te^{-A\tau}BB'e^{-A'\tau}\,d\tau\;M=e^{AT}e^{-AT}x_R=x_R$$

Un ingresso di questo tipo funziona, a patto che l'integrale sia definito e soprattutto **invertibile**. Nell'integrale $e^{-At}B$ è una matrice $n\times p$ e $B'e^{-A't}$ è $p\times n$: il loro prodotto è $n\times n$, ma, istante per istante, ha rango al più $p$ (il minimo tra $n$ e $p$). Se queste matrici fossero costanti, con $p<n$ l'integrale non sarebbe mai invertibile; ma dipendono dal tempo, e si può studiare quando la matrice

$$G(T)=\int_0^Te^{-A\tau}BB'e^{-A'\tau}\,d\tau\tag{$\spadesuit$}$$

ha rango $n$.

> [!warning] Correzione
> Gli appunti dicono che $B'e^{-A't}$ è "una matrice $n\times p$": è $p\times n$ (la trasposta di $e^{-At}B$).

> [!quote] Dal libro — il gramiano
> La matrice $G=\int_0^Te^{-A\tau}BB'e^{-A'\tau}d\tau$ (nel libro con $t$ al posto di $\tau$) è il **gramiano di raggiungibilità**, ed è invertibile nell'ipotesi di completa raggiungibilità. "Essendo $T$ arbitrario, si usa dire che la proprietà di raggiungibilità è **differenziale** per i sistemi a tempo continuo. Ovviamente meno tempo si impiega per andare da 0 a $x_r$ più ampio è l'ingresso da applicare." _(libro, §6.2, p. 270)_

**Quando $G(T)$ ha rango $n$.** Si sviluppano in serie gli esponenziali:

$$\int_0^T\left(\sum_{i=0}^\infty(-1)^i\frac{A^i\tau^i}{i!}B\right)\left(B'\sum_{i=0}^\infty(-1)^i\frac{A'^i\tau^i}{i!}\right)d\tau=\int_0^T\left(\sum_{i=0}^\infty(-1)^i\frac{A^i\tau^i}{i!}B\right)\left(\sum_{i=0}^\infty(-1)^i\frac{A^i\tau^i}{i!}B\right)'d\tau$$

Il primo fattore si scrive come prodotto matriciale:

$$\sum_{i=0}^\infty(-1)^i\frac{A^i\tau^i}{i!}B=\begin{pmatrix}B&AB&\cdots&A^kB&\cdots\end{pmatrix}\begin{pmatrix}1\\-\tau\\\vdots\\(-1)^k\tau^k/k!\\\vdots\end{pmatrix}$$

La prima matrice è **costante**, la seconda varia in modo polinomiale. Il rango di $\sum_i(-1)^i\frac{A^i\tau^i}{i!}B$ (al variare di $\tau$) è pari a quello di $(B\ AB\ \cdots\ A^kB\ \cdots)$. Quindi la matrice ($\spadesuit$) è invertibile quando ha rango $n$, e questo succede quando ha rango $n$ la matrice $(B\ AB\ \cdots\ A^kB\ \cdots)$; per Cayley-Hamilton, quando ha rango pieno

$$R=\begin{pmatrix}B&AB&A^2B&\cdots&A^{n-1}B\end{pmatrix}$$

cioè quando **tutti gli stati del sistema sono raggiungibili**. Tempo continuo e discreto sono quindi analoghi.

> [!tip] Il perché in una riga
> $G(T)$ è simmetrica e semidefinita positiva: $v'G(T)v=\int_0^T\|B'e^{-A'\tau}v\|^2d\tau$. È singolare se e solo se esiste $v\neq0$ con $v'e^{-A\tau}B\equiv0$, cioè (derivando in $\tau=0$) $v'A^kB=0$ per ogni $k$: $v$ è ortogonale a tutte le colonne di $R$. Quindi $G(T)$ è invertibile, per **qualsiasi** $T>0$, se e solo se $\mathrm{rank}\,R=n$.

> [!note] Raggiungibilità e controllabilità
> Il libro aggiunge la **controllabilità**: uno stato è controllabile a $T$ se esiste un ingresso che lo porta a **zero** al tempo $T$. Nei sistemi lineari stazionari a tempo continuo sono controllabili tutti e soli gli stati raggiungibili (perché $\mathcal R$ è $A$-invariante, anche $-e^{AT}x_T$ è raggiungibile). La proprietà di controllabilità si mantiene sotto approssimazione lineare: se il linearizzato non è controllabile, non lo è nemmeno il sistema fisico. _(libro, §6.2, p. 270)_

## Esempio pratico

$$\begin{cases}\dot x=\begin{pmatrix}-5/7&1/7&-2/7\\-2/7&6/7&2/7\\-6/7&4/7&-1/7\end{pmatrix}x+\begin{pmatrix}2\\0\\2\end{pmatrix}u\\[2mm]y=\begin{pmatrix}\frac57&-\frac17&\frac27\end{pmatrix}x\end{cases}$$

Raggiungibilità:

$$R=\begin{pmatrix}B&AB&A^2B\end{pmatrix}=\begin{pmatrix}2&-2&2\\0&0&0\\2&-2&2\end{pmatrix}$$

(infatti $AB=\frac17(-10-4,\ -4+4,\ -12-2)'=(-2,0,-2)'=-B$, e $A^2B=-AB=B$: $B$ è un autovettore di $A$ con autovalore $-1$.) Il rango è 1:

$$\mathcal R=\mathrm{span}\left\{\begin{pmatrix}2\\0\\2\end{pmatrix}\right\}$$

Tutti gli stati con questa struttura sono raggiungibili. Per metterlo in evidenza si cambia base: si vuole $z=Tx$ tale che, se $x_R$ è raggiungibile, $z_R=Tx_R=(\star,0,0)'$. Si completa il vettore di $\mathcal R$ con altri due indipendenti:

$$T^{-1}=\begin{pmatrix}2&0&0\\0&1&0\\2&0&1\end{pmatrix}\qquad\Longrightarrow\qquad T=\begin{pmatrix}1/2&0&0\\0&1&0\\-1&0&1\end{pmatrix}$$

Ci si aspetta $\tilde A=\begin{psmallmatrix}\star&\star&\star\\0&\star&\star\\0&\star&\star\end{psmallmatrix}$, $\tilde B=\begin{psmallmatrix}\star\\0\\0\end{psmallmatrix}$, $\tilde C=(\star\ \star\ \star)$. Calcolandole:

$$\tilde A=TAT^{-1}=\begin{pmatrix}-1&\frac1{14}&-\frac17\\[1mm]0&\frac67&\frac27\\[1mm]0&\frac37&\frac17\end{pmatrix},\qquad\tilde B=TB=\begin{pmatrix}1\\0\\0\end{pmatrix},\qquad\tilde C=CT^{-1}=\begin{pmatrix}2&-\frac17&\frac27\end{pmatrix}$$

Per la raggiungibilità:

$$\tilde H(t)=e^{\tilde At}\tilde B=\begin{pmatrix}e^{\tilde A_{11}t}&\star\\0&e^{\tilde A_{22}t}\end{pmatrix}\begin{pmatrix}\tilde B_1\\0\end{pmatrix}=\begin{pmatrix}e^{\tilde A_{11}t}\tilde B_1\\0\end{pmatrix}$$

Gli autovalori di $\tilde A_{11}$ caratterizzano i modi eccitabili: la legge temporale del modo relativo a $\lambda_1=-1$ è presente in $H$. Per essere sicuri che $-1$ sia eccitabile bisogna vedere se compare **anche** in $\tilde A_{22}=\begin{psmallmatrix}6/7&2/7\\3/7&1/7\end{psmallmatrix}$: in caso affermativo non si può concludere, altrimenti sì. Gli autovalori di $\tilde A_{22}$ sono $\lambda_2=1$ e $\lambda_3=0$ (traccia 1, determinante 0), quindi $\lambda_1=-1$ è relativo a un modo naturale **eccitabile**.

> [!warning] Correzione
> Gli appunti scrivono "in caso affermativo, $-1$ **non è eccitabile**, altrimenti lo è". Se $-1$ comparisse anche in $\tilde A_{22}$ non si potrebbe dire che non è eccitabile: semplicemente non si potrebbe concludere nulla da questa scomposizione, come precisa il paragrafo successivo degli appunti.

Se un autovalore compare sia in $\tilde A_{11}$ sia in $\tilde A_{22}$, non si può dire molto sulla natura del modo associato: bisogna studiare l'eccitabilità nel modo classico. **Raggiungibilità ed eccitabilità non sono sempre strettamente collegate.**

> [!quote] Dal libro — sottosistema raggiungibile e modi eccitabili
> Nelle coordinate $T^{-1}=(\text{base in }\mathcal R\mid\text{completamento})$ si ha $\tilde A=\begin{psmallmatrix}A_{11}&A_{12}\\0&A_{22}\end{psmallmatrix}$, $\tilde B=\begin{psmallmatrix}B_1\\0\end{psmallmatrix}$, $\tilde C=(C_1\ \ C_2)$, e la terna $(A_{11},B_1,C_1)$ è **tutta raggiungibile**: dal sistema $(A,B,C)_n$ si estrae una rappresentazione $(A_{11},B_1,C_1)_m$ di dimensione minore. "Si può dimostrare che, essendo il sottosistema $S_1$ tutto raggiungibile, tutti i suoi modi sono eccitabili", e il legame ingresso-uscita dipende solo da esso: $W(t)=C_1e^{A_{11}t}B_1$. Esempio 6.2.4: $A=\begin{psmallmatrix}2&-3\\0&-1\end{psmallmatrix}$, $B=\begin{psmallmatrix}1\\1\end{psmallmatrix}$, $\mathcal R=\mathrm{gen}\{(1,1)'\}$, e con $T^{-1}=\begin{psmallmatrix}1&0\\1&1\end{psmallmatrix}$ si ottiene $\tilde A=\begin{psmallmatrix}-1&-3\\0&2\end{psmallmatrix}$, $\tilde B=\begin{psmallmatrix}1\\0\end{psmallmatrix}$. _(libro, §6.2, pp. 273–276)_

> [!tip] Verifica sull'esempio
> $W(t)=\tilde C_1e^{\tilde A_{11}t}\tilde B_1=2e^{-t}$. Infatti $B$ è autovettore di $A$ con autovalore $-1$, quindi $e^{At}B=e^{-t}B$ e $W(t)=Ce^{-t}B=\big(\frac{10}7+\frac47\big)e^{-t}=2e^{-t}$ ✔.

## Scomposizione di Kalman

Vedi [[TDS - Scomposizione di Kalman]].

Studiati gli stati inosservabili e raggiungibili, si hanno i sottospazi

$$\mathcal I=\mathrm{span}\{v_1,\dots,v_s\},\qquad\mathcal R=\mathrm{span}\{w_1,\dots,w_r\}$$

Si vuole sapere se uno stato appartiene a $\mathcal I$ e/o a $\mathcal R$. Prima di tutto se appartiene a **entrambi**: l'intersezione di due sottospazi è un sottospazio, che si chiama $\chi_1$ (si legge "chi"):

$$\chi_1=\mathcal R\cap\mathcal I$$

Se uno stato non fa parte di $\chi_1$, o non è in $\mathcal R$ o non è in $\mathcal I$. Si definiscono allora i sottospazi $\chi_2$ e $\chi_3$:

$$\chi_2:\ \chi_2\oplus\chi_1=\mathcal R,\qquad\chi_3:\ \chi_3\oplus\chi_1=\mathcal I$$

cioè $\chi_2$ è il sottospazio "mancante" a $\chi_1$ per formare $\mathcal R$ (un complemento di $\chi_1$ in $\mathcal R$), e lo stesso per $\chi_3$ in $\mathcal I$. Per completezza

$$\chi_4:\ \chi_4\oplus\chi_1\oplus\chi_2\oplus\chi_3=\mathbb R^n$$

> [!note] Somma diretta
> $\oplus$ è la **somma diretta** ([[GEO - Somma diretta]]). L'unione di due sottospazi non è un sottospazio, la **somma** $+$ sì, ed è il sottospazio generato dall'unione delle basi. Se i due sottospazi non hanno nulla in comune (intersezione = vettore nullo), la somma è **diretta**. Le coppie $\chi_1,\chi_2$ e $\chi_1,\chi_3$ sono per definizione senza nulla in comune.
>
> Attenzione: la somma diretta non si può "invertire". Se $\mathcal R=\chi_1\oplus\chi_2$, **non** è vero che $\chi_2=\mathcal R-\chi_1$: la "somma" tra spazi indica l'unione delle basi e non ha nulla a che vedere con la differenza. $\chi_2$ si trova aggiungendo dimensioni (vettori indipendenti) a $\chi_1$ fino a completare $\mathcal R$, e non è unico.

| Sottospazio | Stati |
|---|---|
| $\chi_1$ | raggiungibili e inosservabili |
| $\chi_2$ | raggiungibili e non inosservabili |
| $\chi_3$ | non raggiungibili e inosservabili |
| $\chi_4$ | non raggiungibili e non inosservabili |

Questa scomposizione in sottospazi si chiama **scomposizione di Kalman**. L'obiettivo è cambiare base e partizionare uno stato $z$ in **quattro blocchi** relativi ai quattro sottospazi:

$$z=\begin{pmatrix}\boxed{z_1}\\\boxed{z_2}\\\boxed{z_3}\\\boxed{z_4}\end{pmatrix},\qquad T^{-1}=\Big(\text{base di }\chi_1\ \Big|\ \text{base di }\chi_2\ \Big|\ \text{base di }\chi_3\ \Big|\ \text{completamento}\Big)$$

Per esempio, se $z=(\boxed\star,\boxed0,\boxed0,\boxed0)'$ si sa subito che $z\in\chi_1$: raggiungibile e inosservabile. Se $z=(\boxed\star,\boxed\star,\boxed0,\boxed0)'$, $z$ è in $\chi_1\oplus\chi_2=\mathcal R$: raggiungibile (ma non si può essere certi sull'inosservabilità), e così via.

> [!note] Notazione
> $\boxed z$ indica un **blocco** di componenti, non un singolo elemento. Nell'esempio sopra, $\tilde A=\begin{psmallmatrix}\boxed{\tilde A_{11}}&\boxed{\tilde A_{12}}\\\boxed{\tilde A_{21}}&\boxed{\tilde A_{22}}\end{psmallmatrix}$ con $\tilde A_{11}=-1$, $\tilde A_{12}=\big(\frac1{14}\ -\frac17\big)$, $\tilde A_{21}=\begin{psmallmatrix}0\\0\end{psmallmatrix}$, $\tilde A_{22}=\begin{psmallmatrix}6/7&2/7\\3/7&1/7\end{psmallmatrix}$.

## Struttura delle matrici nella scomposizione di Kalman

In generale le matrici sono partizionate in quattro:

$$\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}&\tilde A_{13}&\tilde A_{14}\\\tilde A_{21}&\tilde A_{22}&\tilde A_{23}&\tilde A_{24}\\\tilde A_{31}&\tilde A_{32}&\tilde A_{33}&\tilde A_{34}\\\tilde A_{41}&\tilde A_{42}&\tilde A_{43}&\tilde A_{44}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde B_1\\\tilde B_2\\\tilde B_3\\\tilde B_4\end{pmatrix},\qquad\tilde C=\begin{pmatrix}\tilde C_1&\tilde C_2&\tilde C_3&\tilde C_4\end{pmatrix}$$

con blocchi di dimensioni $n_1,n_2,n_3,n_4$ ($n_1+n_2+n_3+n_4=n$).

**Raggiungibilità.** Uno stato raggiungibile ha la forma $z_R=(\boxed{z_1},\boxed{z_2},\boxed0,\boxed0)'$. L'immagine di $\tilde B$ deve stare nello spazio di $z_R$:

$$\tilde B=\begin{pmatrix}\tilde B_1\\\tilde B_2\\0\\0\end{pmatrix}$$

(il primo blocco è legato agli stati raggiungibili e inosservabili, il secondo ai raggiungibili e non inosservabili). Uno stato raggiungibile moltiplicato per $\tilde A$ dà uno stato raggiungibile:

$$\tilde Az_R=\tilde A\begin{pmatrix}z_1\\z_2\\0\\0\end{pmatrix}=\begin{pmatrix}z_1'\\z_2'\\0\\0\end{pmatrix}\quad\forall z_1,z_2$$

La prima e la seconda riga di $\tilde A$ possono essere qualsiasi cosa; la terza e la quarta devono dare zeri per ogni $z_1,z_2$: $\tilde A_{31}=\tilde A_{32}=\tilde A_{41}=\tilde A_{42}=0$.

**Inosservabilità.** Uno stato inosservabile ha la forma $z_I=(\boxed{z_1},\boxed0,\boxed{z_3},\boxed0)'$ e deve essere $\tilde Cz_I=0$ per ogni $z_1,z_3$:

$$\begin{pmatrix}\tilde C_1&\tilde C_2&\tilde C_3&\tilde C_4\end{pmatrix}\begin{pmatrix}z_1\\0\\z_3\\0\end{pmatrix}=0\quad\Longrightarrow\quad\tilde C_1=0,\ \tilde C_3=0,\qquad\tilde C=\begin{pmatrix}0&\tilde C_2&0&\tilde C_4\end{pmatrix}$$

Anche $\mathcal I$ è invariante rispetto ad $\tilde A$, quindi $\tilde Az_I$ è inosservabile:

$$\tilde A\begin{pmatrix}z_1\\0\\z_3\\0\end{pmatrix}=\begin{pmatrix}z_1'\\0\\z_3'\\0\end{pmatrix}\quad\forall z_1,z_3$$

Perché la seconda e la quarta componente siano sempre nulle, devono essere nulli i blocchi che moltiplicano $z_1$ e $z_3$ in quelle righe: $\tilde A_{21}=\tilde A_{23}=\tilde A_{43}=0$ (oltre a $\tilde A_{41}$, già nullo per la raggiungibilità).

> [!important] Forma di Kalman
> $$\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}&\tilde A_{13}&\tilde A_{14}\\0&\tilde A_{22}&0&\tilde A_{24}\\0&0&\tilde A_{33}&\tilde A_{34}\\0&0&0&\tilde A_{44}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde B_1\\\tilde B_2\\0\\0\end{pmatrix},\qquad\tilde C=\begin{pmatrix}0&\tilde C_2&0&\tilde C_4\end{pmatrix}$$
> $$\begin{cases}\dot z_1=\tilde A_{11}z_1+\tilde A_{12}z_2+\tilde A_{13}z_3+\tilde A_{14}z_4+\tilde B_1u\\\dot z_2=\tilde A_{22}z_2+\tilde A_{24}z_4+\tilde B_2u\\\dot z_3=\tilde A_{33}z_3+\tilde A_{34}z_4\\\dot z_4=\tilde A_{44}z_4\\y=\tilde C_2z_2+\tilde C_4z_4\end{cases}$$

Il diagramma del sistema:

![[TDS-L28-01.png]]

$z_2$ riceve l'ingresso **e** arriva in uscita (raggiungibile e osservabile); $z_4$ non riceve ingresso e non dipende dalle altre parti, ma arriva comunque in uscita (osservabile e non raggiungibile); $z_3$ è la parte non raggiungibile e inosservabile; $z_1$ è inosservabile ma raggiungibile.

> [!tip] Cosa vede l'esterno
> Il legame ingresso-uscita passa solo attraverso $z_2$: l'ingresso arriva a $z_1$ e $z_2$, l'uscita viene da $z_2$ e $z_4$, e l'unico blocco comune è $z_2$. Infatti
> $$W(t)=\tilde Ce^{\tilde At}\tilde B=\tilde C_2e^{\tilde A_{22}t}\tilde B_2$$
> La funzione di trasferimento "vede" solo gli autovalori di $\tilde A_{22}$, i modi **eccitabili e osservabili** (vedi [[06 - TDS - Modi naturali#Modi naturali non eccitabili|lezione 6]]).

> [!quote] Dal libro — §6.3 La scomposizione di Kalman
> "$S_1$ è un sottosistema tutto raggiungibile, ma non osservabile; $S_2$ è un sottosistema caratterizzato da stati raggiungibili e osservabili; il sottosistema $S_3$ non raggiungibile e non osservabile; infine, $S_4$ è un sottosistema non raggiungibile, ma osservabile." "La risposta impulsiva del sistema complessivo è la risposta del sottosistema $S_2$, che è un sistema tutto raggiungibile ed osservabile. […] La terna $(A_{22},B_2,C_2)$ ha le dimensioni più piccole tra tutte le terne di matrici che hanno risposta impulsiva fissata e uguale a $W(t)$" (vedi le [[TDS - Realizzazione minima|realizzazioni minime]]).
>
> **Esempio 6.3.1.** $A=\begin{psmallmatrix}-2&1&1\\3&-2&-3\\-3&1&2\end{psmallmatrix}$, $B=\begin{psmallmatrix}1\\0\\0\end{psmallmatrix}$, $C=(1\ -1\ -1)$: $\mathrm{rank}\,\mathcal O=1$, $\mathcal I=\mathrm{gen}\{(1,1,0)',(0,1,-1)'\}$; $\mathrm{rank}\,R=2$, $\mathcal R=\mathrm{gen}\{(1,0,0)',(-2,3,-3)'\}$. Allora $\chi_1=\mathcal R\cap\mathcal I=\mathrm{gen}\{(0,1,-1)'\}$, $\chi_2=\mathrm{gen}\{(1,0,0)'\}$, $\chi_3=\mathrm{gen}\{(1,1,0)'\}$, e poiché $n_1+n_2+n_3=n$ non serve $\chi_4$. Con $T^{-1}=\begin{psmallmatrix}0&1&1\\1&0&1\\-1&0&0\end{psmallmatrix}$:
> $$\tilde A=\begin{pmatrix}1&3&2\\0&-2&0\\0&0&-1\end{pmatrix},\quad\tilde B=\begin{pmatrix}0\\1\\0\end{pmatrix},\quad\tilde C=\begin{pmatrix}0&1&0\end{pmatrix}$$
> e $W(t)=C_2e^{A_{22}t}B_2=e^{-2t}$: il modo di $\lambda=1$ è raggiungibile e inosservabile, quello di $-2$ raggiungibile e osservabile, quello di $-1$ né raggiungibile né osservabile. _(libro, §6.3, pp. 276–282)_
