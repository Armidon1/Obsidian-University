---
title: Stati inosservabili
aliases:
  - TDS — Stati inosservabili
tags:
  - teoria-dei-sistemi
  - osservabilita
  - stati-inosservabili
  - cayley-hamilton
  - cambio-di-coordinate
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 151–157); libro Monaco et al., §6.1
---

# Stati inosservabili

> [!abstract] Scopo della lezione
> Si apre lo studio delle **proprietà geometriche dello spazio di stato**. Finora l'[[06 - TDS - Modi naturali#Modi naturali non osservabili|osservabilità]] era una proprietà dei singoli modi; ora diventa una proprietà degli **stati**:
> 1. due stati iniziali sono **indistinguibili** se danno la stessa uscita; la loro differenza è uno stato **inosservabile**, a cui corrisponde un'evoluzione libera in uscita identicamente nulla;
> 2. con **Cayley-Hamilton** si dimostra che gli stati inosservabili sono il nucleo della **matrice di osservabilità** $\mathcal O=(C;\,CA;\,\dots;\,CA^{n-1})$, quindi un **sottospazio** $\mathcal I$;
> 3. la geometria: gli stati indistinguibili formano rette (o iperpiani) parallele a $\mathcal I$;
> 4. un **cambio di coordinate** che mette in evidenza $\mathcal I$ fa comparire degli zeri nelle matrici $\tilde C$ e $\tilde A$.
>
> Segue [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità]]. Indice: [[MOC - Teoria dei Sistemi]].

## Stati indistinguibili e inosservabili

Vedi [[TDS - Osservabilità]].

A parità di ingresso $u(t)$, come si comporta l'uscita quando cambia la condizione iniziale? In particolare: quando due sistemi che partono da condizioni iniziali diverse hanno la stessa evoluzione in uscita? Presi due stati distinti $x_{0a}\neq x_{0b}$, le uscite sono

$$y_a(t)=\Psi(t)x_{0a}+\int_0^tW(t-\tau)u(\tau)\,d\tau,\qquad y_b(t)=\Psi(t)x_{0b}+\int_0^tW(t-\tau)u(\tau)\,d\tau$$

Facendo la differenza termine a termine la parte forzata si cancella:

$$y_a(t)-y_b(t)=\Psi(t)x_{0a}-\Psi(t)x_{0b}\qquad\Longrightarrow\qquad y_a(t)=y_b(t)\iff\Psi(t)(x_{0a}-x_{0b})=0\quad\forall t\ge0$$

Se questo accade, i due stati si dicono **indistinguibili**. La differenza di due stati indistinguibili si chiama **stato inosservabile** $x_I$:

$$\Psi(t)(x_{0a}-x_{0b})=\Psi(t)x_I=0\quad\forall t\ge0$$

> [!tip] Perché conta
> Se due stati sono indistinguibili, guardando l'uscita (per quanto tempo si voglia, con qualsiasi ingresso) non si può capire da quale dei due sia partito il sistema: è un limite dei "sensori" $C$. Uno stato inosservabile è uno stato che, come condizione iniziale, produce un'**uscita libera identicamente nulla**: è indistinguibile dallo stato zero.

Per quali $x_I$ accade? Deve essere ($\equiv$ indica che la funzione è **identicamente nulla**, cioè vale zero in tutto l'intervallo):

$$\Psi(t)x_I=Ce^{At}x_I\equiv0\quad\forall t\ge0$$

Un teorema di analisi dice che se una funzione è identicamente nulla in un intervallo, lo sono anche tutte le sue derivate:

$$Ce^{At}x_I\equiv0,\qquad CAe^{At}x_I\equiv0,\qquad CA^2e^{At}x_I\equiv0,\qquad\dots$$

Valgono per ogni $t\ge0$; in particolare in $t=0$ (dove $e^{A\cdot0}=I$):

$$Cx_I=0,\qquad CAx_I=0,\qquad CA^2x_I=0,\qquad\dots$$

> [!note] Senza il teorema di analisi
> Si arriva allo stesso risultato sviluppando l'esponenziale: $Ce^{At}x_I=\sum_{k=0}^\infty CA^kx_I\frac{t^k}{k!}\equiv0$, e una serie di potenze è identicamente nulla se e solo se tutti i suoi coefficienti $CA^kx_I$ sono nulli.

## Il teorema di Cayley-Hamilton

Sono infinite equazioni. Per ridurle si usa il **teorema di Cayley-Hamilton**: ogni matrice quadrata annulla il proprio polinomio caratteristico, $p_A(A)=0$. Esplicitamente:

$$p_A(\lambda)=\lambda^n+a_{n-1}\lambda^{n-1}+\dots+a_1\lambda+a_0\ \Longrightarrow\ p_A(A)=A^n+a_{n-1}A^{n-1}+\dots+a_1A+a_0I=0$$

$$\iff\quad A^n=-a_{n-1}A^{n-1}-\dots-a_1A-a_0I\tag{$\spadesuit$}$$

Moltiplicando per $C$ a sinistra e per $x_I$ a destra:

$$CA^nx_I=-a_{n-1}CA^{n-1}x_I-\dots-a_1CAx_I-a_0Cx_I$$

Ogni termine $CA^kx_I$ è funzione di quelli con potenze inferiori. In particolare, se valgono tutte le equazioni da $A^0$ ad $A^{n-1}$

$$Cx_I=0,\quad CAx_I=0,\quad\dots,\quad CA^{n-1}x_I=0$$

allora $CA^nx_I=-a_{n-1}\underbrace{CA^{n-1}x_I}_{=0}-\dots-a_1\underbrace{CAx_I}_{=0}-a_0\underbrace{Cx_I}_{=0}=0$.

Lo stesso vale per potenze maggiori di $A^n$: basta moltiplicare la ($\spadesuit$) per $A^i$ ($i>0$) prima di moltiplicare per $C$ e $x_I$:

$$CA^{n+i}x_I=-a_{n-1}CA^{n+i-1}x_I-\dots-a_1CA^{i+1}x_I-a_0CA^ix_I$$

e quindi $CA^{n+1}x_I=-a_{n-1}\underbrace{CA^nx_I}_{=0}-\dots-a_0\underbrace{CAx_I}_{=0}=0$, e così via. Se i termini da $Cx_I$ a $CA^{n-1}x_I$ sono tutti nulli, lo sono anche tutte le potenze successive. Il sistema non ha più infinite equazioni, ma solo $n$ equazioni $q$-dimensionali:

$$\begin{cases}Cx_I=0\\CAx_I=0\\CA^2x_I=0\\\ \ \vdots\\CA^{n-1}x_I=0\end{cases}\iff\underbrace{\begin{pmatrix}C\\CA\\CA^2\\\vdots\\CA^{n-1}\end{pmatrix}}_{\mathcal O}x_I=0\tag{$\clubsuit$}$$

e, se valgono, sono nulli anche tutti i termini successivi, quindi $\Psi(t)x_I\equiv0$ per ogni $t\ge0$.

> [!warning] Correzione
> Gli appunti dicono "solo con $n-1$ equazioni $q$-dimensionali": le equazioni vanno da $CA^0$ a $CA^{n-1}$, quindi sono **$n$** (blocchi di $q$ righe ciascuno). La matrice $\mathcal O$ ha dimensioni $nq\times n$.

Il sistema ($\clubsuit$) è **lineare omogeneo** a coefficienti costanti: ammette soluzioni diverse da zero se la matrice non ha rango pieno, e queste formano un **sottospazio lineare** (il nucleo). Quindi, nello spazio di stato (lo spazio vettoriale di tutti gli stati possibili, per esempio $\mathbb R^2$), **se ci sono stati inosservabili sono un sottospazio lineare, e quindi infiniti**.

> [!important] Spazio degli stati inosservabili
> $$\mathcal I=\left\{x\in\mathbb R^n:\ \begin{pmatrix}C\\CA\\\vdots\\CA^{n-1}\end{pmatrix}x=0\right\}=\ker\mathcal O$$
> $\mathcal O$ si chiama **matrice di osservabilità**. Il sistema è **completamente osservabile** (nessuno stato inosservabile tranne lo zero) se e solo se $\mathrm{rank}\,\mathcal O=n$. In generale $\dim\mathcal I=n-\mathrm{rank}\,\mathcal O$ (vedi [[GEO - Calcolo del nucleo e rango-nullità]]).

> [!quote] Dal libro — Teorema 6.1.1
> "La proprietà di osservabilità riguarda il comportamento stato–uscita; più precisamente questa proprietà tiene conto del fatto che tutte le informazioni in merito all'evoluzione interna nello stato siano o meno contenute nell'uscita." Il libro dimostra anche il viceversa: se esiste $x_I$ inosservabile, per ogni $x_b$ lo stato $x_a=x_b+x_I$ è indistinguibile da $x_b$. Il Teorema 6.1.1: l'insieme degli stati inosservabili $\mathcal I=\{x\in\mathbb R^n:Ce^{At}x=0,\ \forall t\ge0\}$ coincide con $\ker\begin{psmallmatrix}C\\CA\\\vdots\\CA^{n-1}\end{psmallmatrix}$, e la matrice $\mathcal O$ ($nq\times n$) si chiama **matrice di osservabilità**. _(libro, §6.1, pp. 259–262)_

## Geometria degli stati inosservabili

Si consideri uno spazio di stato su $\mathbb R^2$. La matrice $\begin{psmallmatrix}C\\CA\end{psmallmatrix}$ può avere rango pieno, e allora $\begin{psmallmatrix}C\\CA\end{psmallmatrix}x_I=0$ ha solo la soluzione nulla; oppure le soluzioni sono $\infty^1$ e stanno su un sottospazio che in $\mathbb R^2$ è una retta per l'origine:

![[TDS-L26-01.png]]

Ogni punto della retta è uno stato inosservabile $x_I$ (soluzione di ($\clubsuit$)). Dove si trovano gli stati indistinguibili? Poiché $x_a-x_b=x_I$, basta scegliere un qualsiasi $x_b\in\mathbb R^2$ e trovare $x_a=x_b+x_I$ con la somma vettoriale:

![[TDS-L26-02.png]]

Fissando $x_b$ e scegliendo diversi $x_I$, si ottiene una retta **parallela** alla retta degli stati inosservabili:

![[TDS-L26-03.png]]

Scegliendo altri $x_b$ si ottengono altre rette, sempre parallele. **Presa una qualsiasi retta parallela alla retta degli stati inosservabili, tutti i suoi punti hanno la stessa evoluzione** in uscita. L'esempio era in $\mathbb R^2$, ma in generale le soluzioni di ($\clubsuit$) formano un sottospazio, che non è per forza una retta.

> [!note] Sottospazio o no
> Solo la retta blu è un **sottospazio**, perché contiene l'origine. Le rette parallele (come quella arancione) non sono sottospazi, ma semplici insiemi (sottospazi **affini**, traslati).

In presenza di un sottospazio di stati inosservabili, lo spazio di stato si **separa** in tanti sottoinsiemi equivalenti dal punto di vista dell'osservabilità: tutti i punti di uno stesso sottoinsieme hanno la stessa evoluzione, quindi si può "cambiare" lo stato iniziale con un altro dello stesso sottoinsieme. Lo spazio degli stati inosservabili si indica con $\mathcal I$.

> [!tip] In Geometria
> I sottoinsiemi sono le **classi laterali** $x_b+\mathcal I$, e lo spazio "delle classi" è lo spazio quoziente $\mathbb R^n/\mathcal I$: ciò che l'uscita può davvero distinguere.

In generale si può scegliere in ogni sottoinsieme un **rappresentante** (un punto qualsiasi, visto che tutti danno la stessa uscita). Si può individuare un sottospazio che contiene i rappresentanti di **tutti** i sottoinsiemi:

![[TDS-L26-04.png]]

Basta prendere una direzione diversa da quella di $\mathcal I$ (la retta azzurra), e automaticamente si incrociano tutti i sottoinsiemi: la direzione si sceglie come si vuole. In altre parole: presa una base di $\mathcal I$, si aggiungono vettori indipendenti fino a descrivere tutto lo spazio di stato (un **complemento** di $\mathcal I$, vedi [[GEO - Somma diretta]]); ogni vettore aggiunto alla base di $\mathcal I$ caratterizza una selezione di stati indistinguibili.

## Cambio di coordinate dello spazio di stato

Vedi [[TDS - Cambio di coordinate nello spazio di stato]].

Come è fatto lo stato in questa nuova base? Se lo stato è descritto da $x$, il cambio di base è

$$z=Tx$$

In $\mathbb R^2$, un punto $x=\begin{psmallmatrix}\bar x_1\\\bar x_2\end{psmallmatrix}$ dello spazio di stato, scritto rispetto alla nuova base, sarà $z=\begin{psmallmatrix}\tilde z_1\\\tilde z_2\end{psmallmatrix}$:

![[TDS-L26-05.png]]

La nuova base è formata da un vettore di $\mathcal I$ (blu) e uno del complemento (azzurro). Se il punto fosse uno stato inosservabile ($x\in\mathcal I$) si avrebbe

$$x_I=\begin{pmatrix}\bar x_1\\\bar x_2\end{pmatrix}\ \longrightarrow\ Tx_I=z_I=\begin{pmatrix}\tilde z_1\\0\end{pmatrix}$$

$z_I$ ha solo le componenti relative a $\mathcal I$, mentre le altre sono nulle. Lo spazio degli stati inosservabili è

$$\mathcal I=\left\{x_I\in\mathbb R^n:\ \mathcal Ox_I=0\right\}=\mathrm{span}\{v_1,v_2,\dots,v_m\}$$

con $v_1,\dots,v_m$ vettori di base di $\mathcal I$ (il professore in questa lezione usa la lettera $s$ per la dimensione, ma poi userà $m$). Si vuole trovare $T$. Poiché $z=Tx\iff x=T^{-1}z$, e i vettori di base nelle coordinate $z$ hanno coordinate **canoniche** ($Tv_i=e_i$, l'$i$-esimo vettore della base canonica), moltiplicando $T^{-1}$ per $e_i$ si ottiene $v_i$:

$$v_1=T^{-1}\begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},\qquad v_2=T^{-1}\begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix},\qquad\dots$$

Quindi $T^{-1}$ ha come prima colonna $v_1$, come seconda $v_2$, … fino alla $m$-esima, $v_m$. Considerando tutto lo spazio di stato, ai vettori di $\mathcal I$ si aggiungono altri $n-m$ vettori $v_{m+1},\dots,v_n$ arbitrari ma tutti **indipendenti**, per formare una base di tutto lo spazio:

$$T^{-1}=\Big(\underbrace{v_1\ \ v_2\ \cdots\ v_m}_{\text{vettori di }\mathcal I}\ \ \underbrace{v_{m+1}\ \cdots\ v_n}_{\text{vettori non di }\mathcal I}\Big)$$

Con questa $T$, ogni stato $x$ diventa un $z$ le cui **prime $m$ componenti** sono quelle lungo gli stati inosservabili, mentre le altre $n-m$ "stanno fuori". Se un punto $z$ ha tutti zeri nelle ultime $n-m$ componenti è sicuramente inosservabile; se c'è qualcosa di diverso da zero, non lo è (si potrebbe dire che è "osservabile").

> [!note] Convenzioni diverse
> Il libro mette gli stati inosservabili nelle **prime** $n-m$ componenti, con $m=\mathrm{rank}\,\mathcal O$: $T^{-1}=(\text{base in }\mathcal I\mid\text{completamento})$. Negli appunti $m$ indica invece $\dim\mathcal I$. Il senso è lo stesso: prima la base di $\mathcal I$, poi il completamento. _(libro, §6.1, pp. 263–264)_

## Struttura delle matrici del sistema nelle nuove coordinate

Nelle coordinate classiche $\dot x=Ax+Bu$, $y=Cx+Du$. Con $x=T^{-1}z$ (vedi [[05 - TDS - Calcolo dell'esponenziale di matrice#Considerazioni sul cambio di coordinate in un sistema|lezione 5]]):

$$\begin{cases}\dot z=TAT^{-1}z+TBu\\y=CT^{-1}z+Du\end{cases}\Longrightarrow\begin{cases}\dot z=\tilde Az+\tilde Bu\\y=\tilde Cz+\tilde Du\end{cases}$$

$\tilde A=TAT^{-1}$ è la nuova matrice dinamica, $\tilde B=TB$ la nuova matrice degli ingressi, $\tilde C=CT^{-1}$ la nuova matrice delle uscite; $\tilde D=D$ non cambia, perché "scavalca" la dinamica del sistema.

Gli stati inosservabili, prima del cambio, soddisfacevano $CA^kx_I=0$ per $k=0,\dots,n-1$. Con $x_I=T^{-1}z_I$:

$$\begin{cases}CT^{-1}z_I=0\\CAT^{-1}z_I=0\\\ \ \vdots\\CA^{n-1}T^{-1}z_I=0\end{cases}\Longrightarrow\begin{cases}CT^{-1}z_I=0\\CT^{-1}TAT^{-1}z_I=0\\\ \ \vdots\\CT^{-1}TA^{n-1}T^{-1}z_I=0\end{cases}\Longrightarrow\begin{cases}\tilde Cz_I=0\\\tilde C\tilde Az_I=0\\\ \ \vdots\\\tilde C\tilde A^{n-1}z_I=0\end{cases}$$

(inserendo $T^{-1}T=I$, e usando $TA^kT^{-1}=(TAT^{-1})^k=\tilde A^k$): le rappresentazioni sono equivalenti. Ma ora si sa com'è fatto $z_I$:

$$z_I=\begin{pmatrix}z_1\\\vdots\\z_m\\0\\\vdots\\0\end{pmatrix}$$

### Struttura di $\tilde C$

Perché valga $\tilde Cz_I=0$:

$$\tilde Cz_I=\begin{pmatrix}\tilde C_1&\cdots&\tilde C_m&\cdots&\tilde C_n\end{pmatrix}\begin{pmatrix}z_1\\\vdots\\z_m\\0\\\vdots\\0\end{pmatrix}=\tilde C_1z_1+\dots+\tilde C_mz_m=0\quad\forall z_1,\dots,z_m$$

da cui $\tilde C_1=\tilde C_2=\dots=\tilde C_m=0$: **la matrice $\tilde C$ ha le prime $m$ colonne nulle**, mentre le altre $n-m$ possono essere qualsiasi.

### Struttura di $\tilde A$

Una proprietà degli stati inosservabili, che non dipende dal sistema di coordinate: se $x_I$ è inosservabile, anche $Ax_I$ lo è (**$\mathcal I$ è invariante rispetto ad $A$**).

> [!note] Dimostrazione
> Se $x_I$ è inosservabile, $CA^kx_I=0$ per $k=0,\dots,n-1$ (e quindi, per Cayley-Hamilton, per ogni $k$). Per $Ax_I$: $CA^k(Ax_I)=CA^{k+1}x_I=0$ per ogni $k$. Quindi $Ax_I$ è inosservabile.

Quindi se $z_I$ è inosservabile anche $\tilde Az_I$ lo è. In $\mathbb R^2$, per semplicità: $z_I=\begin{psmallmatrix}z_1\\0\end{psmallmatrix}$ e anche $\tilde Az_I$ deve avere la forma $\begin{psmallmatrix}\bar z_1\\0\end{psmallmatrix}$:

$$\tilde Az_I=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\\tilde A_{21}&\tilde A_{22}\end{pmatrix}\begin{pmatrix}z_1\\0\end{pmatrix}=\begin{pmatrix}\bar z_1\\0\end{pmatrix}\Longrightarrow\begin{cases}\tilde A_{11}z_1=\bar z_1\\\tilde A_{21}z_1=0\end{cases}$$

e poiché vale per ogni $z_1$, $\tilde A_{21}=0$. Quindi $\tilde A$ ha una struttura molto particolare, **triangolare a blocchi**:

$$\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix},\qquad\tilde C=\begin{pmatrix}0&\tilde C_2\end{pmatrix}$$

Il significato di questa struttura è l'argomento della [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità|prossima lezione]].

> [!quote] Dal libro
> "Il sottospazio degli stati inosservabili è invariante rispetto ad $A$ […] ovvero il nucleo della matrice di osservabilità. Tale insieme è, infatti, non solo invariante rispetto ad $A$, ma è il più grande sottospazio dello spazio di stato invariante rispetto all'applicazione di $A$ contenuto nel kernel di $C$." Nelle coordinate indicate le matrici assumono la forma $\tilde A=\begin{psmallmatrix}A_{11}&A_{12}\\0&A_{22}\end{psmallmatrix}$, $\tilde B=\begin{psmallmatrix}B_1\\B_2\end{psmallmatrix}$, $\tilde C=(0\ \ C_2)$, e la coppia $(A_{22},C_2)$ è **tutta osservabile**. _(libro, §6.1, pp. 263–264)_
