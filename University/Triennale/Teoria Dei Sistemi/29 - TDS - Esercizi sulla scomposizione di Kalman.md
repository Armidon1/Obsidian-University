---
title: Esercizi sulla scomposizione di Kalman
aliases:
  - TDS — Esercizi sulla scomposizione di Kalman
tags:
  - teoria-dei-sistemi
  - scomposizione-di-kalman
  - raggiungibilita
  - osservabilita
  - esercizi
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 172–180); libro Monaco et al., §6.3
---

# Esercizi sulla scomposizione di Kalman

> [!abstract] Scopo della lezione
> Due esercizi completi che mettono insieme tutto il percorso:
> autovalori e autovettori → evoluzione libera → eccitabilità e osservabilità dei modi ([[06 - TDS - Modi naturali|lezione 6]]) → stabilità interna ed esterna ([[11 - TDS - Punti di equilibrio e stabilità|lezione 11]]) → spazi $\mathcal R$ e $\mathcal I$ ([[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità|lezione 27]]) → **scomposizione di Kalman** ([[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman|lezione 28]]).
> Nel primo esercizio $\mathcal R=\mathcal I$ e la funzione di trasferimento è nulla; nel secondo $\mathcal R\cap\mathcal I=\{0\}$ e c'è un autovalore doppio, che mostra i limiti della corrispondenza tra modi e sottospazi.
>
> Segue [[30 - TDS - Esercizi di riepilogo]]. Indice: [[MOC - Teoria dei Sistemi]].

## Primo esercizio

Vedi [[TDS - Scomposizione di Kalman]].

$$\begin{cases}\dot x=\begin{pmatrix}1&-3&-2\\2&-4&-2\\-1&1&0\end{pmatrix}x+\begin{pmatrix}2\\1\\0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}1&-2&-1\end{pmatrix}x\end{cases}$$

Stato di dimensione 3 ($n=3$), un ingresso ($p=1$), un'uscita ($q=1$).

### Autovalori

$$\det(A-\lambda I)=\begin{vmatrix}1-\lambda&-3&-2\\2&-4-\lambda&-2\\-1&1&-\lambda\end{vmatrix}=\lambda(-\lambda^2-3\lambda-2)\stackrel{\text{set}}{=}0\quad\Longrightarrow\quad\lambda_1=0,\ \lambda_2=-1,\ \lambda_3=-2$$

($\stackrel{\text{set}}{=}$ vuol dire "poniamo uguale a").

> [!tip] Verifica
> Sviluppando lungo la prima riga: $(1-\lambda)(\lambda^2+4\lambda+2)+3(-2\lambda-2)-2(-2-\lambda)=-\lambda^3-3\lambda^2-2\lambda=-\lambda(\lambda+1)(\lambda+2)$. Controllo con traccia ($1-4+0=-3=0-1-2$) e determinante ($\det A=0$, c'è l'autovalore nullo) ✔.

### Autovettori

Per ogni autovalore si risolve $(A-\lambda_iI)u_i=0$.

$\lambda_1=0$: $\begin{psmallmatrix}1&-3&-2\\2&-4&-2\\-1&1&0\end{psmallmatrix}u_1=0$. Si ottiene 0 sommando la prima e la seconda colonna e sottraendo la terza: le prime due componenti valgono 1 e la terza $-1$ (ci sono molti altri modi, e si possono trovare autovettori diversi):

$$u_1=\begin{pmatrix}1\\1\\-1\end{pmatrix}$$

$\lambda_2=-1$: $\begin{psmallmatrix}2&-3&-2\\2&-3&-2\\-1&1&1\end{psmallmatrix}u_2=0$. Sommando la prima colonna con l'ultima si ottiene zero:

$$u_2=\begin{pmatrix}1\\0\\1\end{pmatrix}$$

$\lambda_3=-2$: $\begin{psmallmatrix}3&-3&-2\\2&-2&-2\\-1&1&2\end{psmallmatrix}u_3=0$. Sommando le prime due colonne:

$$u_3=\begin{pmatrix}1\\1\\0\end{pmatrix}$$

> [!warning] Correzione
> Negli appunti, nel sistema per $\lambda_3$, l'incognita è scritta $u_2$: è $u_3$, come risulta subito dopo.

### Autovettori sinistri

$$U=\begin{pmatrix}u_1&u_2&u_3\end{pmatrix}=\begin{pmatrix}1&1&1\\1&0&1\\-1&1&0\end{pmatrix},\qquad V=U^{-1}=\frac{1}{-1}\begin{pmatrix}-1&1&1\\-1&1&0\\1&-2&-1\end{pmatrix}=\begin{pmatrix}1&-1&-1\\1&-1&0\\-1&2&1\end{pmatrix}$$

(aggiunta trasposta divisa per $\det U=-1$). Gli autovettori sinistri sono le righe:

$$v_1'=(1\ \ -1\ \ -1),\qquad v_2'=(1\ \ -1\ \ 0),\qquad v_3'=(-1\ \ 2\ \ 1)$$

### Evoluzione libera

$$x_L(t)=\Phi(t)x_0=c_1\begin{pmatrix}1\\1\\-1\end{pmatrix}+c_2e^{-t}\begin{pmatrix}1\\0\\1\end{pmatrix}+c_3e^{-2t}\begin{pmatrix}1\\1\\0\end{pmatrix},\qquad c_i=v_i'x_0$$

Non serve calcolare $\Phi(t)=e^{At}$: dalla forma spettrale, $e^{At}x_0=Ue^{\Lambda t}U^{-1}x_0=\sum_ie^{\lambda_it}u_i\underbrace{v_i'x_0}_{c_i}$ (vedi [[05 - TDS - Calcolo dell'esponenziale di matrice#Evoluzione libera dello stato|lezione 5]]).

Tutti i modi naturali sono **aperiodici** (non ci sono termini complessi). Le leggi $e^{-t}$ ed $e^{-2t}$ tendono a zero, mentre il primo modo, relativo a $\lambda_1=0$, è **costante**. Per far tendere a zero l'evoluzione libera il termine costante deve essere nullo, $c_1=v_1'x_0=0$: lo stato iniziale non deve avere componente lungo $u_1$, cioè deve stare nel sottospazio generato da $u_2$ e $u_3$:

$$x_0=\alpha u_2+\beta u_3$$

### Eccitabilità e osservabilità

Primo modo, $c_1(1,1,-1)'$:

$$v_1'B=\begin{pmatrix}1&-1&-1\end{pmatrix}\begin{pmatrix}2\\1\\0\end{pmatrix}=1\ \Rightarrow\ \text{eccitabile},\qquad Cu_1=\begin{pmatrix}1&-2&-1\end{pmatrix}\begin{pmatrix}1\\1\\-1\end{pmatrix}=0\ \Rightarrow\ \text{non osservabile}$$

Per gli altri due (calcoli omessi negli appunti): $v_2'B=1$, $Cu_2=0$ → $\lambda_2=-1$ eccitabile e non osservabile; $v_3'B=0$, $Cu_3=-1$ → $\lambda_3=-2$ non eccitabile e osservabile. In termini di insiemi:

$$\Lambda_e=\{0,-1\},\qquad\Lambda_o=\{-2\},\qquad\Lambda_{e,o}=\{\}$$

### Stabilità del sistema

Gli autovalori hanno parte reale non positiva e $\lambda_1=0$ ha molteplicità geometrica 1 (non ci sono blocchi di Jordan): il sistema è **stabile semplicemente**.

> [!note] Perché serve la molteplicità
> Con molteplicità algebrica maggiore di 1 e geometrica minore, comparirebbero termini $e^{\lambda t}\big(c_1+c_2t+c_3\frac{t^2}2+\dots\big)$, che con $\lambda=0$ diventano $c_1+c_2t+\dots$ e divergono (vedi [[18 - TDS - Trasformata Zeta#Stabilità|lezione 18]]).

Per la stabilità **esterna** servono $\Psi$ limitata e $W$ convergente: gli autovalori osservabili devono avere parte reale $\le0$ e quelli osservabili ed eccitabili parte reale $<0$:

$$\begin{cases}\mathrm{Re}(\Lambda_o)\le0\\\mathrm{Re}(\Lambda_{e,o})<0\end{cases}$$

Sono soddisfatte: $\mathrm{Re}(\Lambda_o)=\mathrm{Re}(\{-2\})\le0$ e $\mathrm{Re}(\Lambda_{e,o})=\mathrm{Re}(\{\})<0$ (se l'insieme è vuoto la condizione è soddisfatta).

> [!warning] Correzione
> Negli appunti la prima condizione è scritta $\mathrm{Re}(\Lambda_e)\le0$ (e poi verificata come "$\mathrm{Re}(\Lambda_e)=\mathrm{Re}(\{-2\})$"): la condizione riguarda gli autovalori **osservabili**, $\Lambda_o=\{-2\}$, come nella definizione di [[11 - TDS - Punti di equilibrio e stabilità#Stabilità esterna|lezione 11]] e come dice la frase subito prima.

### Raggiungibilità

$$R=\begin{pmatrix}B&AB&A^2B\end{pmatrix}=\begin{pmatrix}2&-1&1\\1&0&0\\0&-1&1\end{pmatrix}$$

La prima colonna è $B$, la seconda $AB$, la terza la seconda moltiplicata a sinistra per $A$ ($A\cdot AB$). Il rango è 2 (la seconda e la terza colonna sono proporzionali), quindi $\dim\mathcal R=2$. Bastano due colonne indipendenti:

$$\mathcal R=\mathrm{span}\left\{\begin{pmatrix}2\\1\\0\end{pmatrix},\begin{pmatrix}1\\0\\1\end{pmatrix}\right\}$$

### Inosservabilità

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}1&-2&-1\\-2&4&2\\4&-8&-4\end{pmatrix}$$

La prima riga è $C$, la seconda $CA$, la terza la seconda per $A$. La seconda riga è $-2$ volte la prima, quindi anche la terza sarà dipendente ($-2$ volte la seconda): per conoscere il rango ci si poteva fermare alla seconda riga. $\mathcal O$ ha rango 1, quindi $\dim\mathcal I=2$:

$$\mathcal I=\mathrm{span}\left\{\begin{pmatrix}1\\0\\1\end{pmatrix},\begin{pmatrix}0\\1\\-2\end{pmatrix}\right\}$$

Il primo vettore si trova sommando la prima e la terza colonna (che dà zero), il secondo sommando la seconda colonna con $-2$ volte la terza.

### Sottospazi di Kalman

$\chi_1=\mathcal R\cap\mathcal I$. L'intersezione si può calcolare "a occhio" quando è facile, altrimenti algebricamente. Il vettore $(1,0,1)'$ sta in entrambi, quindi sta nell'intersezione; bisogna vedere se gli altri due sono dipendenti. Si mettono i tre vettori in una matrice e se ne calcola il rango:

$$\mathrm{rank}\begin{pmatrix}1&2&0\\0&1&1\\1&0&-2\end{pmatrix}=2$$

(oppure: il determinante è zero). I vettori rimanenti sono dipendenti, e se ne può mettere uno a scelta nell'intersezione:

$$\chi_1=\mathcal R\cap\mathcal I=\mathrm{span}\left\{\begin{pmatrix}1\\0\\1\end{pmatrix},\begin{pmatrix}0\\1\\-2\end{pmatrix}\right\}$$

> [!tip] In altre parole
> $(2,1,0)'$ soddisfa l'equazione di $\mathcal I$ ($x_1-2x_2-x_3=0$): **$\mathcal R\subseteq\mathcal I$**, e avendo la stessa dimensione $\mathcal R=\mathcal I$. Tutto ciò che l'ingresso può raggiungere è invisibile all'uscita.

$\chi_2$ è il sottospazio che, aggiunto a $\chi_1$, dà $\mathcal R$; ma $\chi_1$ è già uguale a $\mathcal R$, quindi $\chi_2$ è banale, $\chi_2=\mathrm{span}\{0\}$. Lo stesso per $\chi_3$: poiché $\chi_1=\mathcal R=\mathcal I$, $\chi_3=\mathrm{span}\{0\}$.

$\chi_4$ deve completare $\mathbb R^3$: bisogna aumentare di 1 il rango di $\chi_1$. Un vettore indipendente dai primi due è $(0,0,1)'$:

$$\chi_4=\mathrm{span}\left\{\begin{pmatrix}0\\0\\1\end{pmatrix}\right\}$$

Gli autovalori sono tutti distinti, quindi vale la corrispondenza tra autovalori eccitabili e stati raggiungibili, e tra autovalori osservabili e stati (non) inosservabili. In effetti gli autovalori eccitabili sono $\lambda_1=0$ e $\lambda_2=-1$, e $\mathcal R$ ha dimensione 2; $\lambda_3=-2$ è l'unico osservabile, gli altri due sono inosservabili e $\mathcal I$ ha dimensione 2.

$T^{-1}$ si forma mettendo in ordine le basi di $\chi_1,\chi_2,\chi_3,\chi_4$ (le prime due colonne per $\chi_1$, la terza per $\chi_4$; $\chi_2$ e $\chi_3$ sono banali):

$$T^{-1}=\begin{pmatrix}1&0&0\\0&1&0\\1&-2&1\end{pmatrix},\qquad T=\begin{pmatrix}1&0&0\\0&1&0\\-1&2&1\end{pmatrix}$$

### Matrici partizionate

La forma attesa (con le dimensioni dei blocchi $n_1=2$, $n_2=0$, $n_3=0$, $n_4=1$):

$$\tilde A=\begin{pmatrix}\boxed{\tilde A_{11}}^{2\times2}&\boxed{\tilde A_{14}}^{2\times1}\\0&\boxed{\tilde A_{44}}^{1\times1}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde B_1\\0\end{pmatrix},\qquad\tilde C=\begin{pmatrix}0&\tilde C_4\end{pmatrix}$$

(i blocchi relativi a $\chi_2$ e $\chi_3$ hanno dimensione zero e spariscono).

> [!warning] Correzione
> Nella prima scrittura delle matrici gli appunti riportano $\tilde C=(\tilde C_1\ \ 0\ \ \tilde C_3\ \ 0)$: la forma di Kalman è $\tilde C=(0\ \ \tilde C_2\ \ 0\ \ \tilde C_4)$ (nulli i blocchi degli stati inosservabili $\chi_1$ e $\chi_3$), come nella seconda scrittura degli appunti e in [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman#Struttura delle matrici nella scomposizione di Kalman|lezione 28]].

$\tilde A_{44}$ è $1\times1$: è la matrice dinamica del sottospazio degli stati né raggiungibili né inosservabili. Poiché qui eccitabilità ↔ raggiungibilità e osservabilità ↔ (non) inosservabilità corrispondono, si sa già quanto vale: l'unico autovalore non eccitabile e osservabile, $\lambda_3=-2$. Allo stesso modo $\tilde A_{11}$ ha autovalori $\lambda_1=0$ e $\lambda_2=-1$. Poiché non ci sono autovalori sia osservabili sia eccitabili, la risposta impulsiva è nulla:

$$W(t)\equiv0$$

> [!example] Calcolo esplicito (non presente negli appunti)
> $$\tilde A=TAT^{-1}=\begin{pmatrix}-1&1&-2\\0&0&-2\\0&0&-2\end{pmatrix},\qquad\tilde B=TB=\begin{pmatrix}2\\1\\0\end{pmatrix},\qquad\tilde C=CT^{-1}=\begin{pmatrix}0&0&-1\end{pmatrix}$$
> $\tilde A_{11}=\begin{psmallmatrix}-1&1\\0&0\end{psmallmatrix}$ ha autovalori $-1$ e $0$, $\tilde A_{44}=-2$, e la struttura è quella prevista. Senza un blocco $\chi_2$, l'ingresso e l'uscita non hanno alcuna parte in comune: $W(t)=\tilde Ce^{\tilde At}\tilde B=0$.

## Secondo esercizio

$$\begin{cases}\dot x=\begin{pmatrix}1&-2&2\\2&-3&2\\2&-2&1\end{pmatrix}x+\begin{pmatrix}0\\0\\1\end{pmatrix}u\\[2mm]y=\begin{pmatrix}1&0&0\end{pmatrix}x\end{cases}$$

### Raggiungibilità e osservabilità

Stavolta si parte dalle proprietà strutturali.

$$R=\begin{pmatrix}B&AB&A^2B\end{pmatrix}=\begin{pmatrix}0&2&0\\0&2&0\\1&1&1\end{pmatrix},\qquad\mathrm{rank}\,R=2,\qquad\mathcal R=\mathrm{span}\left\{\begin{pmatrix}0\\0\\1\end{pmatrix},\begin{pmatrix}2\\2\\1\end{pmatrix}\right\}$$

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}1&0&0\\1&-2&2\\1&0&0\end{pmatrix},\qquad\mathrm{rank}\,\mathcal O=2,\qquad\mathcal I=\ker\mathcal O=\mathrm{span}\left\{\begin{pmatrix}0\\1\\1\end{pmatrix}\right\}$$

(il vettore di $\mathcal I$ si trova perché sommando la seconda e la terza colonna si ottiene zero).

### Scomposizione di Kalman

Per l'intersezione di $\mathcal R$ e $\mathcal I$ si guarda se i vettori di base sono tutti indipendenti: se lo sono, l'intersezione è nulla. Si mettono i tre vettori in una matrice:

$$\det\begin{pmatrix}0&2&0\\0&2&1\\1&1&1\end{pmatrix}=2\neq0$$

Rango pieno, quindi

$$\chi_1=\mathcal R\cap\mathcal I=\mathrm{span}\{0\}$$

> [!warning] Correzione
> Gli appunti concludono "il rango della matrice è pieno e **non ci sono vettori indipendenti**": il senso è che i tre vettori **sono** tutti indipendenti, quindi non c'è nessun vettore comune ai due sottospazi.

Essendo nulla l'intersezione, $\chi_2$ (che completa $\mathcal R$ partendo da $\chi_1$) è proprio $\mathcal R$, e $\chi_3$ è $\mathcal I$:

$$\chi_2=\mathcal R=\mathrm{span}\left\{\begin{pmatrix}0\\0\\1\end{pmatrix},\begin{pmatrix}2\\2\\1\end{pmatrix}\right\},\qquad\chi_3=\mathcal I=\mathrm{span}\left\{\begin{pmatrix}0\\1\\1\end{pmatrix}\right\}$$

$\chi_2\oplus\chi_3$ è già tutto $\mathbb R^3$: non serve $\chi_4$.

### Matrici partizionate

$$T^{-1}=\begin{pmatrix}0&2&0\\0&2&1\\1&1&1\end{pmatrix}$$

con blocchi di dimensioni $n_1=0$, $n_2=2$, $n_3=1$, $n_4=0$:

$$\tilde A=\begin{pmatrix}\boxed{\tilde A_{22}}^{2\times2}&0\\0&\boxed{\tilde A_{33}}^{1\times1}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde B_2\\0\end{pmatrix},\qquad\tilde C=\begin{pmatrix}\tilde C_2&0\end{pmatrix}$$

$\tilde A_{33}$ è $1\times1$: se gli autovalori fossero distinti, essendo la matrice dinamica degli stati non raggiungibili e inosservabili, sarebbe uguale all'autovalore non eccitabile e non osservabile.

> [!example] Calcolo esplicito (non presente negli appunti)
> Senza invertire $T^{-1}$ si ottiene $\tilde A=\begin{psmallmatrix}0&1&0\\1&0&0\\0&0&-1\end{psmallmatrix}$, $\tilde B=(1,0,0)'$, $\tilde C=(0\ \ 2\ \ 0)$. Il blocco $\tilde A_{22}=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$ ha autovalori $\pm1$, e $\tilde A_{33}=-1$. Verifica: le colonne di $AT^{-1}$ sono $A(0,0,1)'=(2,2,1)'$, $A(2,2,1)'=(0,0,1)'$, $A(0,1,1)'=(0,-1,-1)'$, cioè rispettivamente la seconda colonna di $T^{-1}$, la prima, e $-1$ volte la terza: da qui $\tilde A$ (le colonne di $\tilde A$ sono le coordinate di queste immagini nella nuova base). $B=(0,0,1)'$ è la prima colonna di $T^{-1}$, quindi $\tilde B=e_1$; $\tilde C=CT^{-1}$ è la prima riga di $T^{-1}$, $(0\ \ 2\ \ 0)$. La funzione di trasferimento dipende solo da $(\tilde A_{22},\tilde B_2,\tilde C_2)$: $W(s)=(2\ \ 0)\begin{psmallmatrix}s&-1\\-1&s\end{psmallmatrix}^{-1}\begin{psmallmatrix}1\\0\end{psmallmatrix}=\frac{2s}{s^2-1}$, con poli $\pm1$ (i modi eccitabili e osservabili).

### Autovalori

$$p_A(\lambda)=\det\begin{pmatrix}1-\lambda&-2&2\\2&-3-\lambda&2\\2&-2&1-\lambda\end{pmatrix}=(1-\lambda)(1+\lambda)^2$$

$\lambda_1=1$ con $\mu_1=1$, e $\lambda_2=-1$ con molteplicità algebrica $\mu_2=2$.

### Autovettori

$\lambda_1=1$: $(A-I)u_1=\begin{psmallmatrix}0&-2&2\\2&-4&2\\2&-2&0\end{psmallmatrix}u_1=0$; sommando tutte le colonne si ottiene 0:

$$u_1=\begin{pmatrix}1\\1\\1\end{pmatrix}$$

$\lambda_2=-1$: $(A+I)u_2=\begin{psmallmatrix}2&-2&2\\2&-2&2\\2&-2&2\end{psmallmatrix}u_2=0$. È molto semplice trovare due autovettori indipendenti che descrivono il nucleo di $A+I$ (rango 1): sommando la prima e la seconda colonna si ottiene zero, ma anche sommando la seconda e la terza:

$$u_{21}=\begin{pmatrix}1\\1\\0\end{pmatrix},\qquad u_{22}=\begin{pmatrix}0\\1\\1\end{pmatrix}$$

Questi due vettori sono una base di un sottospazio (l'autospazio di $-1$, di dimensione 2: la molteplicità geometrica è 2, uguale all'algebrica, e $A$ è diagonalizzabile). Con inosservabilità e raggiungibilità si sono viste le caratteristiche del sistema da un'altra angolazione: per questi due vettori i modi potrebbero essere entrambi eccitabili o entrambi osservabili, ma **dentro** il sottospazio che generano potrebbe esserci un sottospazio non osservabile o non raggiungibile. Non si è più sicuri che ci sia corrispondenza tra non osservabilità e inosservabilità, e tra eccitabilità e raggiungibilità.

$$V=U^{-1}=\begin{pmatrix}1&1&0\\1&1&1\\1&0&1\end{pmatrix}^{-1}=\begin{pmatrix}1&-1&1\\0&1&-1\\-1&1&0\end{pmatrix}$$

$$v_1'=(1\ \ -1\ \ 1),\qquad v_2'=(0\ \ 1\ \ -1),\qquad v_3'=(-1\ \ 1\ \ 0)$$

### Eccitabilità e osservabilità

$$Cu_1=1,\quad v_1'B=1;\qquad Cu_{21}=1,\quad v_2'B=-1;\qquad Cu_{22}=0,\quad v_3'B=0$$

Il modo relativo a $\lambda_1=1$ è eccitabile e osservabile; dei modi relativi a $\lambda_2=-1$, uno è eccitabile e osservabile, l'altro non eccitabile e non osservabile.

In questo caso la corrispondenza torna: i modi eccitabili e osservabili hanno autovettori in $\chi_2$ (raggiungibili e non inosservabili: infatti $u_1=\frac12(2,2,1)'+\frac12(0,0,1)'$ e $u_{21}=\frac12(2,2,1)'-\frac12(0,0,1)'$), mentre il modo non osservabile e non eccitabile ha autovettore in $\chi_3$ ($u_{22}=(0,1,1)'$, proprio la base di $\mathcal I$). In generale però non è sempre semplice stabilirlo.

> [!tip] Il ruolo della scelta degli autovettori
> Con un'altra base dell'autospazio di $-1$, per esempio $u_{21}+u_{22}=(1,2,1)'$ e $u_{22}$, entrambi i modi di $-1$ risulterebbero "osservabili" per qualche scelta. È il problema della [[07 - TDS - Autovalori complessi coniugati#Completa osservabilità e completa eccitabilità|completa osservabilità/eccitabilità]]: con un solo ingresso e una sola uscita un autovalore di molteplicità 2 non può essere completamente eccitabile né completamente osservabile. La scomposizione di Kalman, invece, non dipende da queste scelte: $W(s)$ ha un solo polo in $-1$ (dentro $\tilde A_{22}$) e l'altra "copia" di $-1$ sta in $\tilde A_{33}$.

### Stabilità

Il sistema è **instabile**, perché $\lambda_1=1>0$. Se fosse a tempo discreto sarebbe **semplicemente stabile**: tutti gli autovalori hanno modulo $\le1$, e $\lambda_2=-1$ ha molteplicità algebrica 2 ma anche geometrica 2, quindi l'indice geometrico è 1, non compaiono termini in $t$ e il sistema non diverge.

> [!note] Precisazione
> Nel discreto anche $\lambda_1=1$ ha modulo 1 (ed è semplice): il modo $1^t$ resta costante. La stabilità è quindi solo semplice, non asintotica (vedi [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto#Stabilità interna|lezione 13]]).
