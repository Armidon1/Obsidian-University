---
title: Formula di Ackermann
aliases:
  - TDS — Formula di Ackermann
tags:
  - teoria-dei-sistemi
  - retroazione-dallo-stato
  - assegnazione-autovalori
  - formula-di-ackermann
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 249–252); libro Monaco et al., §9.1.1
---

# Formula di Ackermann

> [!abstract] Scopo della lezione
> Nella [[37 - TDS - Assegnazione degli autovalori con retroazione dallo stato|lezione precedente]] la retroazione $F$ si trovava in tre passi: cambio di coordinate verso la forma canonica raggiungibile, $F_R$ dai coefficienti dei polinomi, ritorno con $F=F_RT$. Qui:
> 1. si ricava la **formula di Ackermann** $F=-\gamma'p^*(A)$, che dà $F$ in un colpo solo;
> 2. si estende al caso **non completamente raggiungibile** (si assegnano solo gli autovalori della parte raggiungibile);
> 3. un **esempio completo** di stabilizzazione di un sistema instabile non tutto raggiungibile.
>
> Segue [[39 - TDS - Osservatore asintotico dello stato]]. Indice: [[MOC - Teoria dei Sistemi]].

## Formula di Ackermann

Vedi [[TDS - Formula di Ackermann]].

Si vuole calcolare direttamente $F$ senza calcolare $F_R$ e fare il prodotto $F=F_RT$. Si è visto che

$$F_R=\begin{pmatrix}a_0-\beta_0&a_1-\beta_1&\cdots&a_{n-1}-\beta_{n-1}\end{pmatrix}$$

dove gli $a_i$ sono i coefficienti del polinomio caratteristico del sistema di partenza e i $\beta_i$ quelli del polinomio che si vuole far avere al sistema finale; e

$$T=\begin{pmatrix}\gamma'\\\gamma'A\\\gamma'A^2\\\vdots\\\gamma'A^{n-1}\end{pmatrix},\qquad\gamma'\text{ ultima riga di }R^{-1}$$

Partendo da $F_R$:

$$\begin{aligned}F=F_RT&=(a_0-\beta_0)\gamma'+(a_1-\beta_1)\gamma'A+\dots+(a_{n-1}-\beta_{n-1})\gamma'A^{n-1}\\&=\big(a_0\gamma'+a_1\gamma'A+\dots+a_{n-1}\gamma'A^{n-1}\big)-\big(\beta_0\gamma'+\beta_1\gamma'A+\dots+\beta_{n-1}\gamma'A^{n-1}\big)\\&=\gamma'\big(a_0I+a_1A+\dots+a_{n-1}A^{n-1}\big)-\gamma'\big(\beta_0I+\beta_1A+\dots+\beta_{n-1}A^{n-1}\big)\end{aligned}$$

Il primo termine sembra proprio il polinomio caratteristico di $A$ calcolato in $A$, $p_A(A)$; ma non è completo: manca il termine relativo a $\lambda^n$, cioè $\gamma'A^n$. Lo si aggiunge e lo si toglie, includendo il termine tolto nell'altra parentesi (quella dei $\beta_i$):

$$\begin{aligned}F&=\gamma'\big(a_0I+\dots+a_{n-1}A^{n-1}\big)-\gamma'\big(\beta_0I+\dots+\beta_{n-1}A^{n-1}\big)+\gamma'A^n-\gamma'A^n\\&=\gamma'\big(a_0I+\dots+a_{n-1}A^{n-1}+A^n\big)-\gamma'\big(\beta_0I+\dots+\beta_{n-1}A^{n-1}+A^n\big)\\&=\gamma'p_A(A)-\gamma'p^*(A)\stackrel{\text{CH}}{=}-\gamma'p^*(A)\end{aligned}$$

dove $p^*$ è il polinomio caratteristico desiderato (quello di $A+BF$) e nel passaggio CH si è usato il teorema di Cayley-Hamilton, $p_A(A)=0$.

> [!important] Formula di Ackermann
> $$F=-\gamma'\,p^*(A),\qquad\gamma'=\begin{pmatrix}0&\cdots&0&1\end{pmatrix}R^{-1}$$
> Si basa sul fatto che la coppia $(A,B)$ sia **raggiungibile**: $\gamma'$ viene dall'inversa della matrice di raggiungibilità $R$, che non sarebbe invertibile se non avesse rango pieno. Vale per un solo ingresso ($p=1$).

> [!quote] Dal libro
> "La soluzione così calcolata ammette la seguente semplice espressione $F=F_cT_c=-\gamma A^n+(\gamma A^n-\gamma p^*(A))=-\gamma p^*(A)$, dove $p^*(\lambda)$ indica il polinomio caratteristico che si desidera assegnare e $p^*(A)$ la matrice che si ottiene sostituendo in esso la matrice $A$ al posto della variabile $\lambda$." Il libro fa notare anche che i guadagni $f_i$ sono tanto più grandi quanto più gli autovalori di $A+BF$ sono lontani da quelli di $A$, che sono "inversamente proporzionali" alla controllabilità del sistema, e che guadagni grandi significano ingressi ampi e possibili **saturazioni**. Un buon compromesso è spesso collocare i poli tutti alla stessa distanza dall'origine, secondo la **configurazione Butterworth**. _(libro, §9.1.1, pp. 340–342)_

> [!example] Dal libro — Esempio 9.1.1 (pendolo invertito)
> $A=\begin{psmallmatrix}0&1\\\Omega^2&-a\end{psmallmatrix}$, $b=\begin{psmallmatrix}0\\\beta\end{psmallmatrix}$, raggiungibile per $\beta\neq0$. $R^{-1}=\begin{psmallmatrix}0&\beta\\\beta&-a\beta\end{psmallmatrix}^{-1}=\begin{psmallmatrix}\star&\star\\\frac1\beta&0\end{psmallmatrix}$, quindi $\gamma=\frac1\beta(1\ \ 0)$. Con $p^*(\lambda)=\alpha_0+\alpha_1\lambda+\lambda^2$:
> $$F=-\gamma(\alpha_0I+\alpha_1A+A^2)=\Big(-\tfrac{\Omega^2+\alpha_0}{\beta}\ \ \ \tfrac{a-\alpha_1}{\beta}\Big)$$
> _(libro, §9.1.1, pp. 341–342)_

## Sistema non completamente raggiungibile

Se il sistema originario ha parti non raggiungibili, ci si riferisce solo alla parte raggiungibile: si fa il cambio di base $T$ che individua le matrici

$$\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde B_1\\0\end{pmatrix},\qquad\tilde F=\begin{pmatrix}\tilde F_1&\tilde F_2\end{pmatrix}$$

così che il sistema chiuso abbia matrice dinamica

$$\tilde A+\tilde B\tilde F=\begin{pmatrix}\tilde A_{11}+\tilde B_1\tilde F_1&\tilde A_{12}+\tilde B_1\tilde F_2\\0&\tilde A_{22}\end{pmatrix}$$

Gli autovalori stanno solo in $\tilde A_{11}$ e $\tilde A_{22}$ (sulla diagonale); $\tilde A_{22}$, la parte non raggiungibile, non si può modificare, quindi si agisce solo su $\tilde A_{11}$, e solo $\tilde F_1$ ha un ruolo. $\tilde A_{11}$ è la matrice dinamica della parte raggiungibile, e la formula di Ackermann si applica a quella parte:

$$\tilde F_1=-\gamma'p^*(\tilde A_{11})$$

con $\gamma'$ ultima riga dell'inversa della matrice di raggiungibilità di $(\tilde A_{11},\tilde B_1)$. Per avere la $\tilde F$ completa si sceglie $\tilde F_2$ e si mettono insieme le due parti; $\tilde F_2$ è del tutto arbitraria, quindi la scelta più semplice è una $\tilde F_2$ di tutti zeri. Infine si torna alle coordinate originali:

$$F=\tilde FT$$

## Esempio pratico

Si vuole rendere stabile, con una retroazione dallo stato, il sistema

$$\dot x=\begin{pmatrix}1&-2&2\\2&-3&2\\2&-2&1\end{pmatrix}x+\begin{pmatrix}0\\1\\2\end{pmatrix}u$$

**Autovalori.**

$$\begin{vmatrix}1-\lambda&-2&2\\2&-3-\lambda&2\\2&-2&1-\lambda\end{vmatrix}=-(3+\lambda)(1-\lambda)^2+4(1-\lambda)=(1-\lambda)\big[-(3+\lambda)(1-\lambda)+4\big]=(1-\lambda)(\lambda^2+2\lambda+1)=(1-\lambda)(1+\lambda)^2$$

Gli autovalori sono $\lambda_1=1$ con molteplicità uno e $\lambda_2=-1$ con molteplicità algebrica due: il sistema per ora è **instabile**, perché $\mathrm{Re}(\lambda_1)>0$. (È la stessa $A$ del [[29 - TDS - Esercizi sulla scomposizione di Kalman#Secondo esercizio|secondo esercizio della lezione 29]], con un'altra $B$.)

**Raggiungibilità.**

$$R=\begin{pmatrix}B&AB&A^2B\end{pmatrix}=\begin{pmatrix}0&2&0\\1&1&1\\2&0&2\end{pmatrix}$$

Il rango non è pieno (la prima e la terza colonna coincidono): c'è una parte non raggiungibile. Se questa, che corrisponde ad $\tilde A_{22}$, contenesse l'autovalore $\lambda_1=+1$, non si potrebbe fare nulla per stabilizzare il sistema. Per verificarlo si costruisce $T^{-1}$ con le colonne indipendenti di $R$ e un completamento arbitrario, qui $(0,0,1)'$:

$$T^{-1}=\begin{pmatrix}0&2&0\\1&1&0\\2&0&1\end{pmatrix}\quad\Longrightarrow\quad T=\begin{pmatrix}-1/2&1&0\\1/2&0&0\\1&-2&1\end{pmatrix}$$

$$\tilde A=TAT^{-1}=\left(\begin{array}{cc|c}0&1&1\\1&0&1\\\hline0&0&-1\end{array}\right)=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix},\qquad\tilde B=TB=\begin{pmatrix}1\\0\\0\end{pmatrix}=\begin{pmatrix}\tilde B_1\\0\end{pmatrix}$$

$\tilde A_{22}$ ha come unico autovalore $-1$: l'autovalore a parte reale positiva, $1$, responsabile dell'instabilità, si trova in $\tilde A_{11}$ (che ha autovalori $\pm1$). Il sistema è **stabilizzabile**.

**Modifica della parte raggiungibile.** Si costruisce la matrice di raggiungibilità della parte raggiungibile, $\tilde R$, e se ne prende $\gamma'$:

$$\tilde R=\begin{pmatrix}\tilde B_1&\tilde A_{11}\tilde B_1\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\ \Longrightarrow\ \tilde R^{-1}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\ \Longrightarrow\ \gamma'=\begin{pmatrix}0&1\end{pmatrix}$$

$\tilde A_{11}$ ha dimensione 2: il sottosistema raggiungibile ha 2 autovalori, che in retroazione si possono scegliere a piacimento. Si vogliono $\lambda=-2$ e $\lambda=-3$ (nel sistema totale resta anche $-1$, che non si può modificare):

$$p^*(\lambda)=(\lambda+2)(\lambda+3)=\lambda^2+5\lambda+6$$

(5 e 6 sono $\beta_1$ e $\beta_0$). Per la formula di Ackermann serve $p^*(\tilde A_{11})$:

$$p^*(\tilde A_{11})=\tilde A_{11}^2+5\tilde A_{11}+6I=\begin{pmatrix}0&1\\1&0\end{pmatrix}^2+5\begin{pmatrix}0&1\\1&0\end{pmatrix}+6\begin{pmatrix}1&0\\0&1\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}+\begin{pmatrix}0&5\\5&0\end{pmatrix}+\begin{pmatrix}6&0\\0&6\end{pmatrix}=\begin{pmatrix}7&5\\5&7\end{pmatrix}$$

$$\tilde F_1=-\gamma'p^*(\tilde A_{11})=-\begin{pmatrix}0&1\end{pmatrix}\begin{pmatrix}7&5\\5&7\end{pmatrix}=\begin{pmatrix}-5&-7\end{pmatrix}$$

Lo stato del sistema di partenza ha dimensione 3, quindi per la $\tilde F$ completa serve un $\tilde F_2$ scalare ($1\times1$), che si sceglie nullo:

$$\tilde F=\begin{pmatrix}-5&-7&0\end{pmatrix}$$

**Ritorno al sistema originario.**

$$F=\tilde FT=\begin{pmatrix}-5&-7&0\end{pmatrix}\begin{pmatrix}-1/2&1&0\\1/2&0&0\\1&-2&1\end{pmatrix}=\begin{pmatrix}-1&-5&0\end{pmatrix}$$

Gli autovalori di $A+BF$ sono

$$\sigma(A+BF)=\{-1,-2,-3\}$$

Il nuovo sistema è asintoticamente stabile, perché tutti gli autovalori sono a parte reale negativa.

> [!tip] Verifica
> $A+BF=\begin{psmallmatrix}1&-2&2\\1&-8&2\\0&-12&1\end{psmallmatrix}$: traccia $-6$, somma dei minori principali $2\times2$ pari a $-6+1+16=11$, determinante $-6$. Il polinomio caratteristico è $\lambda^3+6\lambda^2+11\lambda+6=(\lambda+1)(\lambda+2)(\lambda+3)$ ✔. Anche $\tilde A_{11}+\tilde B_1\tilde F_1=\begin{psmallmatrix}-5&-6\\1&0\end{psmallmatrix}$ ha polinomio $\lambda^2+5\lambda+6$ ✔.

In un esercizio può capitare che non sia possibile trovare una $F$ che dia autovalori tutti a parte reale negativa: succede quando un autovalore instabile sta nella parte **non raggiungibile** ($\tilde A_{22}$).
