---
title: Esercizi di riepilogo finale
aliases:
  - TDS — Esercizi di riepilogo finale
tags:
  - teoria-dei-sistemi
  - esercizi
  - scomposizione-di-kalman
  - modi-naturali
  - trasformata-di-laplace
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 265–284)
---

# Esercizi di riepilogo finale

> [!abstract] Scopo della lezione
> L'ultima lezione è tutta di esercizi, tre in tutto:
> 1. **analisi modale** e **scomposizione di Kalman** di un sistema con un autovalore doppio ma diagonalizzabile;
> 2. lo stesso sistema con un solo elemento di $A$ cambiato: l'autovalore doppio diventa **non regolare** (blocco di Jordan), i sottospazi di Kalman restano gli stessi;
> 3. un sistema dato con la sola $W(s)$: risposta forzata, regime permanente, Bode, realizzazione minima (lasciato in gran parte agli studenti).
>
> In **appendice** gli esercizi lasciati durante il corso, risolti negli appunti ("Esercizi svolti #1"): lezioni [[16 - TDS - Antitrasformate e residui|16]], [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori|17]] e [[20 - TDS - Risposta forzata nel tempo discreto|20]].
>
> Indice: [[MOC - Teoria dei Sistemi]].

## Primo esercizio

Vedi [[TDS - Scomposizione di Kalman]].

$$\begin{cases}\dot x=\begin{pmatrix}3&1&-4\\0&1&0\\2&1&-3\end{pmatrix}x+\begin{pmatrix}1\\0\\0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}-1&1&2\end{pmatrix}x\end{cases}$$

### Modi naturali

Polinomio caratteristico, con Laplace lungo la **seconda riga** (contiene due zeri, il calcolo è più immediato):

$$\det(A-\lambda I)=\det\begin{pmatrix}3-\lambda&1&-4\\0&1-\lambda&0\\2&1&-3-\lambda\end{pmatrix}=(1-\lambda)\big[-(3-\lambda)(3+\lambda)+8\big]=(1-\lambda)(\lambda^2-1)=-(\lambda-1)^2(\lambda+1)$$

> [!note] Precisazione sul segno
> Gli appunti scrivono il risultato come $(\lambda-1)^2(\lambda+1)$; il segno corretto è $-(\lambda-1)^2(\lambda+1)$, perché $(1-\lambda)(\lambda^2-1)=-(\lambda-1)(\lambda-1)(\lambda+1)$. Le radici, che sono quello che interessa, non cambiano.

$$\lambda_1=1,\ \mu_1=2;\qquad\lambda_2=-1$$

Con un autovalore di molteplicità 2 bisogna calcolare gli autovettori per vedere se $A$ è diagonalizzabile. Per $\lambda_2$ si sa già di trovare un autovettore:

$$A-\lambda_2I=\begin{pmatrix}4&1&-4\\0&2&0\\2&1&-2\end{pmatrix}\qquad\Longrightarrow\qquad u_2=\begin{pmatrix}1\\0\\1\end{pmatrix}$$

(la prima e la terza colonna sono uguali e opposte: sommandole si ottiene zero). Per $\lambda_1$ si sperano due autovettori:

$$A-\lambda_1I=\begin{pmatrix}2&1&-4\\0&0&0\\2&1&-4\end{pmatrix}$$

Le colonne sono tutte proporzionali (rango 1): si trovano sicuramente due vettori indipendenti, per esempio

$$u_{11}=\begin{pmatrix}1\\-2\\0\end{pmatrix},\qquad u_{12}=\begin{pmatrix}2\\0\\1\end{pmatrix}$$

$A$ è **diagonalizzabile**. La matrice del cambio di base mette gli autovettori in fila:

$$U=\begin{pmatrix}u_{11}&u_{12}&u_2\end{pmatrix}=\begin{pmatrix}1&2&1\\-2&0&0\\0&1&1\end{pmatrix},\qquad V=U^{-1}=\begin{pmatrix}0&-1/2&0\\1&1/2&-1\\-1&-1/2&2\end{pmatrix}=\begin{pmatrix}v_{11}'\\v_{12}'\\v_2'\end{pmatrix},\qquad\Lambda=\begin{pmatrix}1&&\\&1&\\&&-1\end{pmatrix}$$

(la diagonale di $\Lambda$ ha gli autovalori nell'ordine in cui gli autovettori sono in $U$).

> [!warning] Correzione
> Gli appunti dicono che $\Lambda$ "conterrà sulla diagonale gli **autovettori**": sono gli **autovalori**.

L'evoluzione libera:

$$x_L(t)=e^{\lambda_1t}u_{11}v_{11}'x_0+e^{\lambda_1t}u_{12}v_{12}'x_0+e^{\lambda_2t}u_2v_2'x_0=c_{11}e^tu_{11}+c_{12}e^tu_{12}+c_2e^{-t}u_2$$

Tre modi naturali, i primi due con la stessa legge temporale (stesso autovalore).

### Eccitabilità e osservabilità

Vedi [[TDS - Eccitabilità e osservabilità dei modi]].

$$v_{11}'B=0,\qquad v_{12}'B=1,\qquad v_2'B=-1$$

$$Cu_{11}=\begin{pmatrix}-1&1&2\end{pmatrix}\begin{pmatrix}1\\-2\\0\end{pmatrix}=-3,\qquad Cu_{12}=\begin{pmatrix}-1&1&2\end{pmatrix}\begin{pmatrix}2\\0\\1\end{pmatrix}=0,\qquad Cu_2=\begin{pmatrix}-1&1&2\end{pmatrix}\begin{pmatrix}1\\0\\1\end{pmatrix}=1$$

| Modo | Eccitabile | Osservabile |
|---|---|---|
| $c_{11}e^tu_{11}$ | no | sì |
| $c_{12}e^tu_{12}$ | sì | no |
| $c_2e^{-t}u_2$ | sì | sì |

In $H(t)$ ci sono solo le leggi del secondo e del terzo modo, in $\Psi(t)$ solo quelle del primo e del terzo. Di fatto in entrambe compaiono sia termini in $e^t$ sia in $e^{-t}$, perché il primo e il secondo modo hanno la stessa legge.

> [!tip] Il ruolo della scelta degli autovettori
> Con un autovalore doppio la ripartizione "un modo eccitabile, uno osservabile" dipende dagli autovettori scelti (vedi [[07 - TDS - Autovalori complessi coniugati#Completa osservabilità e completa eccitabilità|lezione 7]]): l'autovalore 1 non è né completamente eccitabile né completamente osservabile. Quello che non dipende dalla scelta è la combinazione in $W$: $\sum Cu\,v'B$ per $\lambda=1$ vale $-3\cdot0+0\cdot1=0$, quindi il modo $e^t$ **non compare** in $W(t)$.

### Suddivisione dello spazio di stato

**Raggiungibilità.**

$$R=\begin{pmatrix}B&AB&A^2B\end{pmatrix}=\begin{pmatrix}1&3&1\\0&0&0\\0&2&0\end{pmatrix}$$

Due colonne uguali (la prima e la terza): rango 2. Una base dell'immagine è formata da colonne indipendenti:

$$\mathcal R=\mathrm{span}\left\{\begin{pmatrix}1\\0\\0\end{pmatrix},\begin{pmatrix}3\\0\\2\end{pmatrix}\right\}$$

**Inosservabilità.**

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}-1&1&2\\1&2&-2\\-1&1&2\end{pmatrix}$$

La prima e la terza colonna sono dipendenti (e la prima e la terza riga uguali): rango 2, nucleo di dimensione 1. Un vettore di base è immediato considerando la prima e la terza colonna:

$$\mathcal I=\mathrm{span}\left\{\begin{pmatrix}2\\0\\1\end{pmatrix}\right\}$$

### Scomposizione di Kalman

$\chi_1=\mathcal R\cap\mathcal I$. $\mathcal I$ ha dimensione 1 e $\mathcal R$ dimensione 2: si verifica se $\mathcal I\subseteq\mathcal R$, nel qual caso l'intersezione è proprio $\mathcal I$. Tutti i vettori di $\mathcal R$ e di $\mathcal I$ hanno la seconda componente nulla, quindi mettendoli insieme il rango non aumenta:

$$\mathrm{rank}\begin{pmatrix}1&3&2\\0&0&0\\0&2&1\end{pmatrix}=2$$

Quindi $\mathcal I\subseteq\mathcal R$ e

$$\chi_1=\mathcal R\cap\mathcal I=\mathcal I=\mathrm{span}\left\{\begin{pmatrix}2\\0\\1\end{pmatrix}\right\}$$

$\chi_2$ ($\chi_1\oplus\chi_2=\mathcal R$): basta un vettore di base di $\mathcal R$ che non stia in $\chi_1$, per esempio $(1,0,0)'$. $\chi_3$ ($\chi_1\oplus\chi_3=\mathcal I$): poiché $\chi_1=\mathcal I$, è il sottospazio banale. $\chi_4$ completa $\mathbb R^3$ con un vettore indipendente da quelli di $\mathcal R$ e $\mathcal I$:

$$\chi_2=\mathrm{span}\left\{\begin{pmatrix}1\\0\\0\end{pmatrix}\right\},\qquad\chi_3=\mathrm{span}\{0\},\qquad\chi_4=\mathrm{span}\left\{\begin{pmatrix}0\\1\\0\end{pmatrix}\right\}$$

con $\mathrm{rank}\begin{psmallmatrix}2&1&0\\0&0&1\\1&0&0\end{psmallmatrix}=3$.

**Cambio di coordinate.** $T^{-1}$ mette in ordine le basi di $\chi_1,\chi_2,\chi_3,\chi_4$:

$$T^{-1}=\begin{pmatrix}2&1&0\\0&0&1\\1&0&0\end{pmatrix}\quad\Longrightarrow\quad T=\begin{pmatrix}0&0&1\\1&0&-2\\0&1&0\end{pmatrix}$$

Le matrici attese hanno la struttura a blocchi della [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman#Struttura delle matrici nella scomposizione di Kalman|lezione 28]]. Sono **blocchi**, non elementi: la riga e la colonna $i$ di $\tilde A$ hanno dimensione pari a quella di $\chi_i$, e lo stesso vale per l'$i$-esimo blocco di $\tilde B$ e $\tilde C$. Qui $\chi_1$, $\chi_2$ e $\chi_4$ hanno dimensione 1, mentre $\chi_3$ ha dimensione 0: i blocchi relativi a $\chi_3$ (terza riga e colonna di $\tilde A$, terzo blocco di $\tilde B$ e $\tilde C$) non ci sono. La forma è

$$\tilde A=\begin{pmatrix}\tilde a_{11}&\tilde a_{12}&\tilde a_{14}\\0&\tilde a_{22}&\tilde a_{24}\\0&0&\tilde a_{44}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde b_1\\\tilde b_2\\0\end{pmatrix},\qquad\tilde C=\begin{pmatrix}0&\tilde c_2&\tilde c_4\end{pmatrix}$$

con $\tilde a_{ij},\tilde b_j,\tilde c_i$ elementi.

> [!note] Nomi dei blocchi
> Negli appunti i blocchi di $\tilde C$ sono chiamati $\tilde C_1$ e $\tilde C_2$ (e $\tilde c_1$, $\tilde c_2$), cioè numerati in ordine di comparsa; qui si usano gli indici dei sottospazi ($\tilde C_2$, $\tilde C_4$), coerentemente con la lezione 28.

Facendo i calcoli:

$$\tilde A=TAT^{-1}=\begin{pmatrix}0&0&1\\1&0&-2\\0&1&0\end{pmatrix}\begin{pmatrix}2&3&1\\0&0&1\\1&2&1\end{pmatrix}=\begin{pmatrix}1&2&1\\0&-1&-1\\0&0&1\end{pmatrix}$$

$$\tilde B=TB=\begin{pmatrix}0\\1\\0\end{pmatrix},\qquad\tilde C=CT^{-1}=\begin{pmatrix}-1&1&2\end{pmatrix}\begin{pmatrix}2&1&0\\0&0&1\\1&0&0\end{pmatrix}=\begin{pmatrix}0&-1&1\end{pmatrix}$$

(dove $AT^{-1}=\begin{psmallmatrix}2&3&1\\0&0&1\\1&2&1\end{psmallmatrix}$.) $\tilde A$ è triangolare: gli autovalori sono sulla diagonale e si vede a quale sottospazio appartiene ciascuno.
- Il primo elemento, 1, fa parte di $\tilde A_{11}$: è la matrice del sottospazio **raggiungibile e inosservabile**, e infatti c'era un modo di $\lambda_1=1$ eccitabile ma non osservabile.
- Lo stesso per l'1 in $\tilde A_{44}$, la matrice dello spazio **non raggiungibile e non inosservabile** (osservabile): è il modo osservabile e non eccitabile.
- $-1$ si trova, come prevedibile, nella parte **raggiungibile e osservabile**: il suo modo era eccitabile e osservabile.

**Funzione di trasferimento.** Vi compaiono solo i modi sia eccitabili sia osservabili (la parte raggiungibile e non inosservabile), quindi la matrice responsabile dei modi in $W(t)$ è solo $\tilde A_{22}$:

$$W(t)=\tilde Ce^{\tilde At}\tilde B=\tilde C_2e^{\tilde A_{22}t}\tilde B_2=-1\cdot e^{-t}\cdot1=-e^{-t},\qquad W(s)=\tilde C_2\big(sI-\tilde A_{22}\big)^{-1}\tilde B_2=-\frac{1}{s+1}$$

> [!tip] Verifica
> Dalla forma spettrale: $W(t)=\sum e^{\lambda t}Cu\,v'B=e^{t}(-3\cdot0+0\cdot1)+e^{-t}(1\cdot(-1))=-e^{-t}$ ✔.

## Secondo esercizio

Una variante del primo sistema, in cui cambia solo il secondo elemento di $A$ (da 1 a **2**):

$$\begin{cases}\dot x=\begin{pmatrix}3&\boxed2&-4\\0&1&0\\2&1&-3\end{pmatrix}x+\begin{pmatrix}1\\0\\0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}-1&1&2\end{pmatrix}x\end{cases}$$

### Modi naturali

Gli autovalori sono gli stessi del primo esercizio, perché sviluppando lungo la seconda riga il secondo elemento della prima riga non viene proprio considerato: $\lambda_1=1$ con $\mu_1=2$, $\lambda_2=-1$.

$$A-\lambda_2I=\begin{pmatrix}4&2&-4\\0&2&0\\2&1&-2\end{pmatrix}\ \Longrightarrow\ u_2=\begin{pmatrix}1\\0\\1\end{pmatrix},\qquad A-\lambda_1I=\begin{pmatrix}2&2&-4\\0&0&0\\2&1&-4\end{pmatrix}$$

$A-\lambda_1I$ ha rango 2: si trova **un solo** autovettore,

$$u_{11}=\begin{pmatrix}2\\0\\1\end{pmatrix}$$

> [!warning] Correzione
> Gli appunti dicono "riusciamo a trovare un solo **autovalore**": un solo **autovettore**.

$A$ **non è diagonalizzabile**: c'è un blocco di Jordan. La molteplicità algebrica di $\lambda_1$ è 2 e quella geometrica $\hat\mu=1$, quindi serve un vettore nel nucleo di $(A-\lambda_1I)^2$ (vedi [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori#Catene di autovettori|lezione 17]]):

$$(A-\lambda_1I)^2=\begin{pmatrix}2&2&-4\\0&0&0\\2&1&-4\end{pmatrix}^2=\begin{pmatrix}-4&0&8\\0&0&0\\-4&0&8\end{pmatrix}$$

Rango 1, nucleo di dimensione 2: un generatore è $u_{11}$, l'altro sarà $u_{12}$. La seconda colonna è nulla, quindi una scelta ragionevole è

$$u_{12}=\begin{pmatrix}0\\1\\0\end{pmatrix}$$

> [!tip] È proprio la catena giusta
> $(A-\lambda_1I)u_{12}=(2,0,1)'=u_{11}$: $u_{12}$ è l'autovettore generalizzato che "scende" su $u_{11}$, come richiesto dalla forma di Jordan con l'1 sopra la diagonale.

$$\Lambda=\begin{pmatrix}\lambda_1&1&\\0&\lambda_1&\\&&\lambda_2\end{pmatrix}=\begin{pmatrix}1&1&\\0&1&\\&&-1\end{pmatrix},\qquad U=\begin{pmatrix}2&0&1\\0&1&0\\1&0&1\end{pmatrix},\qquad U^{-1}=\begin{pmatrix}1&0&-1\\0&1&0\\-1&0&2\end{pmatrix}=\begin{pmatrix}v_{11}'\\v_{12}'\\v_2'\end{pmatrix}$$

Su $\lambda_2=-1$ si può concludere qualcosa con sicurezza; per $\lambda_1$ la situazione è più complicata: con i blocchi di Jordan le leggi temporali contengono, oltre agli esponenziali, anche termini polinomiali, e l'eccitabilità o l'osservabilità potrebbero non essere ben definite. L'evoluzione libera:

$$x_L(t)=Ue^{\Lambda t}U^{-1}x_0=\begin{pmatrix}u_{11}&u_{12}&u_2\end{pmatrix}\begin{pmatrix}e^t&te^t&\\0&e^t&\\&&e^{-t}\end{pmatrix}\begin{pmatrix}c_{11}\\c_{12}\\c_2\end{pmatrix}=\big(c_{11}e^t+c_{12}te^t\big)u_{11}+c_{12}e^tu_{12}+c_2e^{-t}u_2$$

> [!warning] Correzione
> Negli appunti la seconda componente del prodotto è scritta $c_{12}t$ (e quindi il termine finale $c_{12}t\,u_{12}$): dal blocco di Jordan $\begin{psmallmatrix}e^t&te^t\\0&e^t\end{psmallmatrix}$ la seconda componente è $c_{12}e^t$.

In presenza di blocchi di Jordan i modi naturali "si mischiano" e non si riescono a dedurre molte informazioni su eccitabilità e osservabilità.

### Suddivisione dello spazio di stato

$$R=\begin{pmatrix}B&AB&A^2B\end{pmatrix}=\begin{pmatrix}1&3&1\\0&0&0\\0&2&0\end{pmatrix},\ \mathrm{rank}\,R=2,\qquad\mathcal R=\mathrm{span}\left\{\begin{pmatrix}1\\0\\0\end{pmatrix},\begin{pmatrix}3\\0\\2\end{pmatrix}\right\}$$

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}-1&1&2\\1&1&-2\\-1&1&2\end{pmatrix},\ \mathrm{rank}\,\mathcal O=2,\qquad\mathcal I=\mathrm{span}\left\{\begin{pmatrix}2\\0\\1\end{pmatrix}\right\}$$

Sono gli **stessi sottospazi** del primo esercizio: con Kalman (saltato) si otterrebbe la stessa struttura delle matrici (con elementi diversi).

> [!tip] Cosa cambia allora (calcolo non presente negli appunti)
> Con la stessa $T^{-1}$ si trova $\tilde A=\begin{psmallmatrix}1&2&1\\0&-1&0\\0&0&1\end{psmallmatrix}$, $\tilde B=(0,1,0)'$, $\tilde C=(0\ \ -1\ \ 1)$: la stessa struttura del primo esercizio, che aveva $\tilde A=\begin{psmallmatrix}1&2&1\\0&-1&-1\\0&0&1\end{psmallmatrix}$. Cambia solo $\tilde a_{24}$ (da $-1$ a $0$), eppure basta: in entrambi i casi l'elemento $\tilde a_{14}=1$ collega i due autovalori 1 (uno in $\chi_1$, uno in $\chi_4$), ma nel primo esercizio $\tilde A-I=\begin{psmallmatrix}0&2&1\\0&-2&-1\\0&0&0\end{psmallmatrix}$ ha rango 1 (due autovettori), nel secondo $\begin{psmallmatrix}0&2&1\\0&-2&0\\0&0&0\end{psmallmatrix}$ ha rango 2 (blocco di Jordan). La $W(s)$ resta legata solo a $\tilde A_{22}=-1$, con $\tilde C_2\tilde B_2=-1$: il comportamento ingresso-uscita è identico a quello del primo esercizio, $W(s)=-\frac1{s+1}$, anche se dentro il sistema compare un modo $te^t$.

## Terzo esercizio

Come esercizio, data la funzione di trasferimento

$$W(s)=\frac{s^2+100}{(s+1)(s+10)(s+100)}$$

1. calcolare la risposta forzata $y_F(t)$ con gli ingressi $u(t)=\delta_{-1}(t)$, $u(t)=t-2$, $u(t)=(t-2)\,\delta(t-2)$;
2. calcolare la risposta a regime permanente $y_{RP}(t)$, se esiste, con $u(t)=\delta_{-1}(t)$ e $u(t)=\sin2t$;
3. disegnare il diagramma di Bode di $W(j\omega)$;
4. trovare una realizzazione minima.

### Punto 1

La risposta forzata esiste sempre: $y_F(t)=\mathcal L^{-1}[W(s)U(s)]$. Con il gradino:

$$Y_F(s)=\frac{s^2+100}{(s+1)(s+10)(s+100)}\cdot\frac1s=\frac{R_1}{s}+\frac{R_2}{s+1}+\frac{R_3}{s+10}+\frac{R_4}{s+100}\quad\Longrightarrow\quad y_F(t)=R_1+R_2e^{-t}+R_3e^{-10t}+R_4e^{-100t}$$

$$R_1=\lim_{s\to0}\frac{s^2+100}{(s+1)(s+10)(s+100)}=\frac1{10},\qquad R_3=\lim_{s\to-10}\frac{s^2+100}{s(s+1)(s+100)}=\frac{200}{(-10)(-9)(90)}=\frac2{81}$$

$$R_2=\lim_{s\to-1}\frac{s^2+100}{s(s+10)(s+100)}=\frac{101}{(-1)(9)(99)}=-\frac{101}{891},\qquad R_4=\lim_{s\to-100}\frac{s^2+100}{s(s+1)(s+10)}=\frac{10100}{(-100)(-99)(-90)}=-\frac{101}{8910}$$

> [!warning] Correzione
> Negli appunti $R_2=-\frac{101}{99\cdot9}=\frac{101}{891}$ (il segno meno si perde nell'ultimo passaggio: è $-\frac{101}{891}$) e $R_4=\frac1{110}$ (il valore corretto è $-\frac{101}{8910}$: al denominatore i tre fattori $-100$, $-99$, $-90$ sono tutti negativi). Verifica: $W(s)U(s)$ ha grado relativo 2, quindi $y_F(0)=0$, cioè $R_1+R_2+R_3+R_4=0$; con denominatore comune 8910: $891-1010+220-101=0$ ✔.

Gli altri ingressi del punto 1 non sono stati trattati dal professore.

> [!example]- Traccia per gli altri ingressi (non presente negli appunti)
> - $u(t)=t-2$ (per $t\ge0$) $=t\,\delta_{-1}(t)-2\delta_{-1}(t)$: per linearità $y_F=w_{-2}(t)-2w_{-1}(t)$, dove $w_{-1}$ è la risposta al gradino appena calcolata e $w_{-2}=\mathcal L^{-1}\big[\frac{W(s)}{s^2}\big]$ quella alla rampa.
> - $u(t)=(t-2)\,\delta(t-2)$: per la proprietà di campionamento dell'impulso, $(t-2)\delta(t-2)=0\cdot\delta(t-2)=0$, quindi $y_F\equiv0$. Se invece si intende la rampa ritardata $(t-2)\,\delta_{-1}(t-2)$, per la traslazione nel tempo $y_F(t)=w_{-2}(t-2)\,\delta_{-1}(t-2)$ (vedi [[20 - TDS - Risposta forzata nel tempo discreto#Sfruttare la linearità|lezione 20]]).

### Punto 2

Il regime permanente **esiste**, perché i poli di $W(s)$ sono tutti a parte reale negativa. Con il gradino:

$$y_{RP}(t)=W(s)\big|_{s=0}\,\delta_{-1}(t)=\frac1{10}\,\delta_{-1}(t)$$

Con un ingresso sinusoidale si calcolano modulo e fase di $W(j\omega)$ in $\omega=2$:

$$y_{RP}(t)=|W(j\omega)|_{\omega=2}\cdot\sin\big(2t+\angle W(j\omega)|_{\omega=2}\big)$$

> [!example] Valori numerici (non presenti negli appunti)
> $W(2j)=\frac{96}{(1+2j)(10+2j)(100+2j)}$: $|W(2j)|=\frac{96}{\sqrt5\,\sqrt{104}\,\sqrt{10004}}\approx0{,}042$, $\angle W(2j)=-(\arctan2+\arctan0{,}2+\arctan0{,}02)\approx-1{,}32$ rad. Quindi $y_{RP}(t)\approx0{,}042\sin(2t-1{,}32)$.
>
> Curiosità: il numeratore $s^2+100$ ha zeri in $\pm10j$, quindi con $u=\sin10t$ la risposta a regime è **nulla** ($W(10j)=0$): il sistema "blocca" esattamente quella frequenza (un trinomio con $\zeta=0$ al numeratore, vedi [[30 - TDS - Esercizi di riepilogo#Terzo esercizio|lezione 30]]).

I punti 3 e 4 non sono svolti negli appunti.

> [!tip] Spunti per i punti 3 e 4
> - **Bode**: in forma di Bode $W=\frac{1}{10}\cdot\frac{1+\frac{s^2}{100}}{(1+s)(1+\frac s{10})(1+\frac{s}{100})}$: guadagno $-20$ dB, poli in 1, 10, 100, e un trinomio al numeratore con $\omega_n=10$, $\zeta=0$ (una "pancia" verso $-\infty$ in $\omega=10$, salto di fase di $+\pi$).
> - **Realizzazione minima**: $p=q=1$ e $W$ irriducibile, quindi la [[31 - TDS - Algoritmi di realizzazione e forme canoniche#Forma canonica raggiungibile|forma canonica raggiungibile]] di dimensione 3 è minima: denominatore $s^3+111s^2+1110s+1000$, numeratore $s^2+0s+100$, cioè $A_R$ con ultima riga $(-1000\ \ -1110\ \ -111)$, $B_R=(0,0,1)'$, $C_R=(100\ \ 0\ \ 1)$.

## Appendice: esercizi svolti

Durante il corso il professore ha lasciato alcuni esercizi agli studenti. Gli appunti li risolvono in un post a parte; si riferiscono alla lezione 16 (trasformate di Laplace), alla lezione 17 (blocchi di Jordan) e alla lezione 20 (ingresso formato da funzioni non banali).

### Esercizio 1: trasformate di Laplace

Vedi [[16 - TDS - Antitrasformate e residui#Calcolo di $e^{At}$ con l'antitrasformata|lezione 16]].

$$\begin{cases}\dot x=\begin{pmatrix}0&1\\-2&-3\end{pmatrix}x+\begin{pmatrix}1\\0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}1&0\end{pmatrix}x\end{cases}$$

Calcolare la funzione di trasferimento $W(s)$, la risposta forzata con $u(t)=\delta_{-1}(t)$ e con $u(t)=\sin2t$.

**Autovalori.** $\det(A-\lambda I)=\lambda(3+\lambda)+2=(\lambda+1)(\lambda+2)$: $\lambda_1=-1$, $\lambda_2=-2$, entrambi a parte reale negativa; ci si aspetta che compaiano entrambi in $W$.

> [!note] Le matrici usate
> L'esercizio usa $B=(1,0)'$, come nel testo della lezione 16 (in quella nota si è osservato che, per il modello massa-molla con stato $(h,\dot h)$, la forza entrerebbe nella seconda componente). Qui si risolve il sistema così come è dato.

**Funzione di trasferimento.** $W(s)=C(sI-A)^{-1}B$ ($D=0$). Per la struttura particolare di $B$ e $C$ basta il primo elemento di $(sI-A)^{-1}$:

$$C(sI-A)^{-1}B=\begin{pmatrix}1&0\end{pmatrix}\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}=a_{11}$$

e non serve calcolare tutta l'inversa. $a_{11}$ è il complemento algebrico del primo elemento di $sI-A=\begin{psmallmatrix}s&-1\\2&s+3\end{psmallmatrix}$, cioè $s+3$, diviso per il determinante $(s+1)(s+2)$:

$$W(s)=\frac{s+3}{(s+1)(s+2)}$$

**Risposta al gradino.**

$$Y_F(s)=\frac{s+3}{(s+1)(s+2)s}=\frac{R_1}{s+1}+\frac{R_2}{s+2}+\frac{R_3}{s},\qquad R_1=\frac{2}{(1)(-1)}=-2,\quad R_2=\frac{1}{(-1)(-2)}=\frac12,\quad R_3=\frac{3}{2}$$

$$y_F(t)=-2e^{-t}+\frac12e^{-2t}+\frac32$$

**Risposta a $\sin2t$.** Gli appunti usano $\mathcal L[\sin\omega t]=\frac{s}{s^2+\omega^2}$ e ottengono

$$y_F(t)=-\frac25e^{-t}+\frac14e^{-2t}+\frac3{20}\cos2t+\frac{11}{20}\sin2t$$

> [!warning] Correzione
> $\frac{s}{s^2+\omega^2}$ è la trasformata del **coseno**; quella del seno è $\frac{\omega}{s^2+\omega^2}$ (vedi la [[15 - TDS - Trasformata di Laplace#Trasformate di alcune funzioni|tabella della lezione 15]]). Il risultato degli appunti, che è svolto correttamente per $U(s)=\frac{s}{s^2+4}$, è quindi la risposta a $u=\cos2t$. Con $u=\sin2t$, $U(s)=\frac{2}{s^2+4}$ e
> $$Y_F(s)=\frac{2(s+3)}{(s+1)(s+2)(s^2+4)},\qquad R_1=\frac{2\cdot2}{(1)(5)}=\frac45,\quad R_2=\frac{2\cdot1}{(-1)(8)}=-\frac14,\quad R_3=\frac{2(3+2j)}{(1+2j)(2+2j)(4j)}=-\frac{11+3j}{40}$$
> (con $R_3$ il residuo nel polo $2j$) e, con $R_3e^{2jt}+R_3^*e^{-2jt}=2\,\mathrm{Re}(R_3)\cos2t-2\,\mathrm{Im}(R_3)\sin2t$:
> $$y_F(t)=\frac45e^{-t}-\frac14e^{-2t}-\frac{11}{20}\cos2t+\frac3{20}\sin2t$$
> Verifica: $y_F(0)=0{,}8-0{,}25-0{,}55=0$ ✔ (grado relativo 3).

Nel procedimento degli appunti, nel calcolo di $R_1$ e $R_2$ il polo complesso si tiene nella forma $s^2+4$, e in quello di $R_3$ i primi due poli come $s^2+3s+2$; i termini complessi si ricombinano con Eulero come in [[16 - TDS - Antitrasformate e residui#Residui complessi|lezione 16]]:

$$R_3e^{2jt}+R_3^*e^{-2jt}=2R_{3a}\cos2t-2R_{3b}\sin2t$$

### Esercizio 2: blocchi di Jordan

È l'esercizio proposto in [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori#Esercizio|lezione 17]]:

$$A=\begin{pmatrix}0&1&1\\-1&-2&1\\0&0&-1\end{pmatrix}$$

calcolare $e^{At}$ in due modi e confrontare.

**1) Con la forma di Jordan.** $p_A(\lambda)=-(\lambda+1)\big[\lambda(\lambda+2)+1\big]=-(\lambda+1)^3$: un solo autovalore $\lambda_1=-1$ con $\mu_1=3$.

$$A-\lambda_1I=\begin{pmatrix}1&1&1\\-1&-1&1\\0&0&0\end{pmatrix}$$

ha rango 2: nucleo di dimensione 1, $\hat\mu=1$. $A$ non è diagonalizzabile, e servono autovettori generalizzati $u_{11},u_{12},u_{13}$ con

$$(A-\lambda_1I)u_{11}=0,\qquad(A-\lambda_1I)u_{12}=u_{11},\qquad(A-\lambda_1I)u_{13}=u_{12}$$

I nuclei crescenti:

$$\ker(A-\lambda_1I)=\mathrm{span}\left\{\begin{pmatrix}1\\-1\\0\end{pmatrix}\right\},\qquad(A-\lambda_1I)^2=\begin{pmatrix}0&0&2\\0&0&-2\\0&0&0\end{pmatrix},\quad\ker(A-\lambda_1I)^2=\mathrm{span}\left\{\begin{pmatrix}1\\-1\\0\end{pmatrix},\begin{pmatrix}0\\1\\0\end{pmatrix}\right\}$$

$$(A-\lambda_1I)^3=0,\qquad\ker(A-\lambda_1I)^3=\mathbb R^3$$

Il nucleo di $(A-\lambda_1I)^2$ contiene quello di $A-\lambda_1I$ e ne amplia la dimensione: basta trovare un vettore del nucleo successivo che non stia nei precedenti. La scelta degli autovettori avviene qui: con $u_{13}=(0,0,1)'$ (in $\ker(A-\lambda_1I)^3$ ma non in $\ker(A-\lambda_1I)^2$),

$$u_{12}=(A-\lambda I)u_{13}=\begin{pmatrix}1\\1\\0\end{pmatrix},\qquad u_{11}=(A-\lambda I)u_{12}=\begin{pmatrix}2\\-2\\0\end{pmatrix}$$

e si verifica che $(A-\lambda I)u_{11}=0$. La **matrice jordanizzante**:

$$U=\begin{pmatrix}u_{11}&u_{12}&u_{13}\end{pmatrix}=\begin{pmatrix}2&1&0\\-2&1&0\\0&0&1\end{pmatrix},\qquad U^{-1}=\begin{pmatrix}1/4&-1/4&0\\1/2&1/2&0\\0&0&1\end{pmatrix}$$

$\Lambda$ è un unico blocco di Jordan di ordine 3, con esponenziale

$$\Lambda=\begin{pmatrix}-1&1&\\&-1&1\\&&-1\end{pmatrix},\qquad e^{\Lambda t}=e^{-t}\begin{pmatrix}1&t&\frac{t^2}2\\&1&t\\&&1\end{pmatrix}$$

$$e^{At}=Ue^{\Lambda t}U^{-1}=e^{-t}\begin{pmatrix}2&2t+1&t^2+t\\-2&-2t+1&-t^2+t\\0&0&1\end{pmatrix}\begin{pmatrix}1/4&-1/4&0\\1/2&1/2&0\\0&0&1\end{pmatrix}=e^{-t}\begin{pmatrix}t+1&t&t^2+t\\-t&-t+1&-t^2+t\\0&0&1\end{pmatrix}$$

**2) Con la trasformata.** $\det(sI-A)=(-1)^3\det(A-sI)=-p_A(s)=(s+1)^3$:

$$(sI-A)^{-1}=\frac{1}{(s+1)^3}\begin{pmatrix}(s+2)(s+1)&s+1&s+3\\-(s+1)&s(s+1)&s-1\\0&0&(s+1)^2\end{pmatrix}=\frac{R_{11}}{(s+1)^3}+\frac{R_{12}}{(s+1)^2}+\frac{R_{13}}{s+1}$$

È strettamente propria. I residui (con le derivate, e dividendo per $2!$ per $R_{13}$):

$$R_{11}=\lim_{s\to-1}(\cdots)=\begin{pmatrix}0&0&2\\0&0&-2\\0&0&0\end{pmatrix},\qquad R_{12}=\lim_{s\to-1}\frac{d}{ds}(\cdots)=\lim_{s\to-1}\begin{pmatrix}2s+3&1&1\\-1&2s+1&1\\0&0&2s+2\end{pmatrix}=\begin{pmatrix}1&1&1\\-1&-1&1\\0&0&0\end{pmatrix}$$

$$R_{13}=\frac12\lim_{s\to-1}\frac{d^2}{ds^2}(\cdots)=\frac12\begin{pmatrix}2&0&0\\0&2&0\\0&0&2\end{pmatrix}=I$$

(non c'è un denominatore da derivare, perché $(s+1)^3$ si moltiplica prima e si calcola il residuo dell'espressione senza di esso.)

$$e^{At}=R_{11}\frac{t^2}2e^{-t}+R_{12}\,te^{-t}+R_{13}e^{-t}=e^{-t}\begin{pmatrix}t+1&t&t^2+t\\-t&-t+1&-t^2+t\\0&0&1\end{pmatrix}$$

Lo stesso risultato del punto 1 (e della traccia riportata in lezione 17).

> [!tip] Cosa dicono i residui
> $R_{11}=(A+I)^2$ e $R_{12}=A+I$, $R_{13}=I$: è lo sviluppo $e^{At}=e^{-t}e^{(A+I)t}=e^{-t}\big(I+(A+I)t+(A+I)^2\frac{t^2}2\big)$, perché $A+I$ è nilpotente di ordine 3.

### Esercizio 3: risposta forzata con ingressi non banali

È l'esercizio della [[20 - TDS - Risposta forzata nel tempo discreto#Esercizio|lezione 20]]: $W(s)=\frac1{s+1}$ con i due ingressi

![[TDS-L41-01.png]]

**Ingresso a triangolo.** Per $0\le t\le2$ l'ingresso è una retta di pendenza $\frac12$, $\frac12t$; per $2\le t\le4$ la pendenza si inverte, $2-\frac12t$; dopo vale 0. La trasformata di Laplace non si può esprimere solo in un intervallo di $t$, ma si usa il gradino per costruire la funzione: da 0 a 2 basta $\frac12t\,\delta_{-1}(t)$; per farla diventare $2-\frac12t$ dopo $t=2$ si somma una funzione nulla prima di 2 che dopo vale $2-t$, cioè $(2-t)\,\delta_{-1}(t-2)$ (per $t>2$: $\frac12t+2-t=2-\frac12t$); dopo $t=4$ serve una funzione che sommata alla precedente dia zero, $\big(\frac12t-2\big)\delta_{-1}(t-4)$. In tutto:

$$u(t)=\tfrac12t\,\delta_{-1}(t)+(2-t)\,\delta_{-1}(t-2)+\big(\tfrac12t-2\big)\delta_{-1}(t-4)$$

Con $\mathcal L[f(t-\alpha)\delta_{-1}(t-\alpha)]=e^{-\alpha s}\mathcal L[f(t)]$:

$$U(s)=\frac1{2s^2}+e^{-2s}\mathcal L\big[(2-(t+2))\delta_{-1}(t)\big]+e^{-4s}\mathcal L\big[\big(\tfrac12(t+4)-2\big)\delta_{-1}(t)\big]=\frac1{2s^2}-e^{-2s}\frac1{s^2}+e^{-4s}\frac1{2s^2}=\frac1{s^2}\Big(\frac12-e^{-2s}+\frac12e^{-4s}\Big)$$

$$Y_F(s)=\frac{1}{s+1}\cdot\frac1{s^2}\Big(\frac12-e^{-2s}+\frac12e^{-4s}\Big),\qquad\frac1{s^2(s+1)}=\frac{1}{s^2}-\frac1s+\frac1{s+1}$$

($R_{11}=1$, $R_{12}=-1$, $R_2=1$, come in [[16 - TDS - Antitrasformate e residui#Residui con denominatori di grado maggiore di 1|lezione 16]]). Antitrasformando:

$$y_F(t)=\Big(\tfrac12t-\tfrac12+\tfrac12e^{-t}\Big)\delta_{-1}(t)+\Big(3-t-e^{2-t}\Big)\delta_{-1}(t-2)+\Big(\tfrac12t-\tfrac52+\tfrac12e^{4-t}\Big)\delta_{-1}(t-4)$$

**Onda quadra.** Sottraendo $\delta_{-1}(t-1)$ a $\delta_{-1}(t)$ si ottiene una funzione che vale 1 in $[0,1)$ e 0 altrove; aggiungendo $\delta_{-1}(t-2)$ si torna a 1 da $t=2$, e così via:

$$u(t)=\delta_{-1}(t)-\delta_{-1}(t-1)+\delta_{-1}(t-2)-\dots=\sum_{k=0}^\infty(-1)^k\delta_{-1}(t-k),\qquad U(s)=\sum_{k=0}^\infty(-1)^k\frac{e^{-ks}}{s}$$

$$Y_F(s)=\frac1{s(s+1)}\sum_{k=0}^\infty(-1)^ke^{-ks}=\sum_{k=0}^\infty(-1)^ke^{-ks}\Big(\frac1s-\frac1{s+1}\Big)\quad\Longrightarrow\quad y_F(t)=\sum_{k=0}^\infty(-1)^k\big[1-e^{-(t-k)}\big]\delta_{-1}(t-k)$$

che coincide con la traccia data in lezione 20.
