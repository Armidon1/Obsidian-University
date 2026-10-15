---
title: Variabili Aleatorie Discrete
aliases:
  - PS — Variabili Aleatorie Discrete
tags:
  - probabilita-e-statistica
  - variabili-aleatorie
  - distribuzioni
  - distribuzione-congiunta
source: pdf/Probabilità e Statistica Dispensa.pdf
---

# Variabili Aleatorie Discrete

> [!abstract]
> Finora abbiamo lavorato con **eventi**. Spesso però di un esperimento ci interessa un **numero**: quante teste in 10 lanci, la somma di due dadi, la vincita a un gioco. La **variabile aleatoria** è lo strumento che associa un numero a ogni esito, e permette di parlare di probabilità in termini di valori numerici.
> In questa lezione: definizione, **funzione di ripartizione**, **funzione di massa** (PMF), poi il caso di **due variabili** (distribuzione congiunta e marginali), l'**indipendenza** tra variabili e le **distribuzioni condizionali**, che trasportano alle variabili aleatorie le idee della [[02 - PS - Probabilità Condizionata e Indipendenza|lezione 2]]. I "riassunti numerici" di una variabile (media, varianza) arrivano nella [[04 - PS - Valore Atteso, Varianza e Covarianza|lezione 4]].
> Mappa del corso: [[MOC - Probabilità e Statistica]].

---

## Variabili aleatorie

Vedi [[Variabile Aleatoria]].

Il termine **variabile aleatoria** indica una quantità il cui valore è determinato dal risultato di un esperimento casuale.

> [!important] Definizione
> Una **variabile aleatoria** (v.a.) $X$ è una **funzione** definita sullo spazio campionario $S$ che associa un numero reale $X(\omega)=x$ a ogni evento elementare $\omega\in S$.
> Il dominio è $S$, il codominio è l'asse reale $\mathbb R$.

Informalmente: una v.a. è una variabile che può assumere un valore casuale tratto da un insieme di esiti. Nonostante il nome, non è né "variabile" né "aleatoria": è una funzione deterministica; la casualità sta nell'esito $\omega$ che le viene dato in ingresso.

> [!example]
> Lancio due dadi: $S=\{(i,j): i,j=1..6\}$, 36 esiti. $X(i,j)=i+j$ è la somma, $Y(i,j)=i\cdot j$ il prodotto. Lo stesso spazio campionario può portare molte v.a. diverse.

Una v.a. può essere **discreta** o **continua** a seconda dell'insieme dei suoi valori. Le v.a. con un numero **finito o numerabile** di valori possibili si dicono **discrete**: sono l'oggetto di quasi tutto il corso.

Siccome il valore di una v.a. dipende dall'esito, possiamo assegnare probabilità ai suoi valori possibili. La probabilità dell'evento $\{s\in S: X(s)=x\}$ si indica in modo compatto con

$$P(X=x)$$

_(dispensa, p. 23)_

---

## Funzione di ripartizione

Vedi [[Funzione di Ripartizione]].

> [!important] Definizione
> La **funzione di ripartizione** (o CDF, *cumulative distribution function*) $F$ di una v.a. $X$ è definita, per ogni $x\in\mathbb R$, da
> $$F(x):=P(X\le x)$$

$F(x)$ è la probabilità che $X$ assuma un valore **minore o uguale** a $x$.

Tutte le domande di probabilità che si possono fare su una v.a. ammettono una risposta in termini della sua funzione di ripartizione. Ad esempio, per calcolare $P(a<X\le b)$: l'evento $\{X\le b\}$ è l'unione dei due eventi **disgiunti** $\{X\le a\}$ e $\{a<X\le b\}$, quindi per l'assioma 3

$$P(X\le b)=P(X\le a)+P(a<X\le b)\quad\Longrightarrow\quad P(a<X\le b)=F(b)-F(a)$$

> [!note] Proprietà di una CDF
> - è **non decrescente** (se $a<b$, $\{X\le a\}\subseteq\{X\le b\}$);
> - $\lim_{x\to-\infty}F(x)=0$ e $\lim_{x\to+\infty}F(x)=1$;
> - è continua a destra.

_(dispensa, p. 24)_

---

## Distribuzione di probabilità

Una **distribuzione di probabilità** è un modello matematico che collega i valori di una variabile alle probabilità che tali valori possano essere osservati. In questo contesto la variabile di interesse è vista come v.a.

In base alla scala di misura della variabile $X$ si distinguono due tipi di distribuzioni:

1. **distribuzioni continue**, espresse da una **funzione di densità di probabilità** $f(x)$;
2. **distribuzioni discrete** (la variabile assume valori isolati, tipicamente interi), espresse da una **funzione di massa di probabilità** $p(x)$.

_(dispensa, p. 25)_

---

## Funzione di massa

Vedi [[Funzione di Massa di Probabilità]].

> [!important] Definizione
> Se $X$ è una v.a. **discreta**, la sua **funzione di massa di probabilità** (PMF, *probability mass function*) è
> $$p(a):=P(X=a)$$

$p$ è non nulla su un insieme al più numerabile di valori: se $x_1,x_2,\dots$ sono i valori possibili di $X$,

$$p(x_i)>0\quad i=1,2,\dots\qquad\qquad p(x)=0\quad\text{per tutti gli altri }x$$

Siccome $X$ deve assumere uno dei valori $x_1,x_2,\dots$, la PMF soddisfa necessariamente

$$\sum_{i=1}^{\infty}p(x_i)=1$$

Per una v.a. discreta la funzione di ripartizione si esprime tramite la PMF:

$$F(a)=\sum_{x\le a}p(x)$$

dove la somma è limitata ai soli valori possibili di $X$ minori o uguali ad $a$.

La $F$ che ne risulta è una **funzione a gradini**: se $x_1<x_2<\dots$ sono i valori possibili, $F$ è costante su ciascun intervallo $[x_{i-1},x_i)$ e in $x_i$ fa un **salto di ampiezza $p(x_i)$**, passando da $p(x_1)+\dots+p(x_{i-1})$ a $p(x_1)+\dots+p(x_i)$.

![[PS-p026-1.png]]

La Figura 4.2 mostra la CDF di una v.a. con valori $1,2,3$: $F$ vale 0 prima di 1, salta a $\frac12$ in $x=1$, a $\frac56$ in $x=2$ e a $1$ in $x=3$. Dai salti si legge la PMF: $p(1)=\frac12$, $p(2)=\frac56-\frac12=\frac13$, $p(3)=1-\frac56=\frac16$. _(dispensa, pp. 25–26)_

> [!example] Esercizio svolto — somma e prodotto di due dadi
> *Si lanciano due dadi equilibrati; $X$ è il prodotto dei due risultati. Calcolare $P(X=i)$.*
> Gli esiti sono 36 equiprobabili; basta contare le coppie: $P(X=1)=\frac1{36}$ (solo (1,1)), $P(X=2)=\frac2{36}$ ((1,2),(2,1)), $P(X=3)=\frac2{36}$, $P(X=4)=\frac3{36}$ ((1,4),(4,1),(2,2)), $P(X=6)=\frac4{36}$ ((1,6),(6,1),(2,3),(3,2)), $P(X=12)=\frac4{36}$, … e così via fino a $P(X=36)=\frac1{36}$. Controllo: la somma di tutte deve fare 1. _(esercizi, p. 4)_

---

## Variabili aleatorie bidimensionali

Vedi [[Distribuzione Congiunta e Marginali]].

Per descrivere la relazione tra due v.a. $X$ e $Y$ il punto di partenza è estendere il concetto di funzione di ripartizione.

> [!important] Definizione
> Siano $X$ e $Y$ due v.a. relative allo **stesso** esperimento casuale. Si dice **funzione di ripartizione congiunta** di $X$ e $Y$ la funzione di due variabili
> $$F(x,y):=P(X\le x,\;Y\le y)$$
> dove la virgola denota l'**intersezione** tra eventi.

La conoscenza di $F$ permette di calcolare le probabilità di tutti gli eventi che dipendono, singolarmente o congiuntamente, da $X$ e $Y$. Ad esempio la funzione di ripartizione di $X$ da sola, $F_X$, si ottiene così:

$$F_X(x):=P(X\le x)=P(X\le x,\,Y<\infty)=F(x,\infty)$$

perché $Y<\infty$ è sempre vero (nel senso del limite $\lim_{y\to\infty}F(x,y)$). Analogamente $F_Y(y)=F(\infty,y)$. _(dispensa, p. 27)_

### Distribuzione congiunta per v.a. discrete

Se $X$ e $Y$ sono discrete con valori $x_1,x_2,\dots$ e $y_1,y_2,\dots$, la funzione

$$p(x_i,y_j):=P(X=x_i,\,Y=y_j)\qquad i,j=1,2,\dots$$

è la loro **funzione di massa di probabilità congiunta**.

Le funzioni di massa individuali (dette **marginali**) si ricavano da quella congiunta. Siccome $Y$ deve assumere uno dei valori $y_j$, l'evento $\{X=x_i\}$ è l'unione, al variare di $j$, degli eventi mutuamente esclusivi $\{X=x_i,Y=y_j\}$:

$$\{X=x_i\}=\bigcup_j\{X=x_i,\,Y=y_j\}$$

e quindi, per l'assioma 3,

$$p_X(x_i)=P(X=x_i)=\sum_jP(X=x_i,\,Y=y_j)=\sum_jp(x_i,y_j)\qquad\qquad p_Y(y_j)=\sum_ip(x_i,y_j)$$

In una tabella con $X$ sulle righe e $Y$ sulle colonne, le marginali sono le **somme per riga e per colonna** (si scrivono "ai margini" della tabella, da cui il nome).

> [!warning] Il viceversa è falso
> Dalla congiunta si ricavano sempre le marginali, ma **la PMF congiunta non si può ricavare dalle singole funzioni di massa individuali**: conoscere $P(X=x_i)$ e $P(Y=y_j)$ non permette di ricavare $P(X=x_i,Y=y_j)$. Fa eccezione il caso di v.a. **indipendenti**, in cui la congiunta è il prodotto delle marginali (sezione seguente).

_(dispensa, p. 28)_

> [!example] Esercizio svolto — urna con palline rosse, bianche e verdi
> *Un'urna contiene 3 palline rosse, 2 bianche e 1 verde. Se ne estraggono 2 senza reinserimento. $R$ = numero di rosse, $B$ = numero di bianche. Densità congiunta e marginali.*
> I casi possibili sono $\binom62=15$ coppie equiprobabili. Contando:
>
> | $R\backslash B$ | 0 | 1 | 2 | $p_R$ |
> |:-:|:-:|:-:|:-:|:-:|
> | **0** | 0 | $\frac{2}{15}$ | $\frac1{15}$ | $\frac3{15}$ |
> | **1** | $\frac3{15}$ | $\frac6{15}$ | 0 | $\frac9{15}$ |
> | **2** | $\frac3{15}$ | 0 | 0 | $\frac3{15}$ |
> | $p_B$ | $\frac6{15}$ | $\frac8{15}$ | $\frac1{15}$ | 1 |
>
> Per esempio $P(R=1,B=1)=\frac{\binom31\binom21}{15}=\frac6{15}$ e $P(R=0,B=0)=0$ (servirebbero due verdi). Le marginali sono le somme di riga e di colonna. _(esercizi, pp. 10–11)_

---

## Variabili aleatorie indipendenti

Vedi [[Variabili Aleatorie Indipendenti]].

Due v.a. sono **indipendenti** se tutti gli eventi relativi alla prima sono indipendenti da tutti quelli relativi alla seconda.

> [!important] Definizione
> Due v.a. relative allo stesso esperimento si dicono **indipendenti** se, per ogni coppia di insiemi di numeri reali $A$ e $B$,
> $$P(X\in A,\;Y\in B)=P(X\in A)\,P(Y\in B)$$
> cioè se per ogni scelta di $A$ e $B$ gli eventi $\{X\in A\}$ e $\{Y\in B\}$ sono indipendenti. In caso contrario $X$ e $Y$ si dicono **dipendenti**.

Usando gli assiomi si dimostra che la definizione equivale a chiedere che per ogni coppia di reali $a,b$

$$P(X\le a,\,Y\le b)=P(X\le a)P(Y\le b)\qquad\text{cioè}\qquad F(a,b)=F_X(a)F_Y(b)\quad\forall a,b\in\mathbb R$$

(la CDF congiunta è il prodotto delle marginali). Se le v.a. sono **discrete**, l'indipendenza equivale anche a chiedere che **la funzione di massa congiunta sia il prodotto delle marginali**:

$$p(x,y)=p_X(x)\,p_Y(y)\qquad\forall x,y\in\mathbb R$$

Il senso della definizione è che due v.a. sono indipendenti se **conoscere il valore di una non cambia la distribuzione dell'altra**.

> [!tip] Come si verifica in pratica
> Per dimostrare che due v.a. discrete **non** sono indipendenti basta trovare **una** coppia $(x,y)$ con $p(x,y)\ne p_X(x)p_Y(y)$. Nella tabella dell'urna qui sopra: $p(0,0)=0$ ma $p_R(0)p_B(0)=\frac3{15}\cdot\frac6{15}\ne0$, quindi $R$ e $B$ sono dipendenti (ovvio: se estraggo più rosse, restano meno posti per le bianche).

**Più di due variabili.** Le v.a. $X_1,\dots,X_n$ sono indipendenti se per ogni $n$-upla $A_1,\dots,A_n$ di sottoinsiemi di $\mathbb R$

$$P(X_1\in A_1,\dots,X_n\in A_n)=\prod_{i=1}^nP(X_i\in A_i)$$

il che equivale a $F(a_1,\dots,a_n)=\prod_{i=1}^nF_{X_i}(a_i)$ per ogni $n$-upla di reali. Collezioni **infinite** di v.a. si dicono indipendenti se ogni loro sottogruppo finito è formato da v.a. indipendenti. _(dispensa, pp. 29–30)_

> [!note] Indipendenza per trasformazioni (dal programma)
> Il programma del corso cita anche l'indipendenza **per trasformazioni** di v.a. (la dispensa la segna "da cercare"): se $X$ e $Y$ sono indipendenti, anche $g(X)$ e $h(Y)$ lo sono, per qualunque funzione $g,h$. Infatti $\{g(X)\in A\}=\{X\in g^{-1}(A)\}$ e $\{h(Y)\in B\}=\{Y\in h^{-1}(B)\}$, e si applica la definizione con gli insiemi $g^{-1}(A)$ e $h^{-1}(B)$. Questo risultato è implicito in molti esercizi (es. $X^2$ e $Y^2$ indipendenti se lo sono $X$ e $Y$).

---

## Distribuzioni condizionali

Vedi [[Distribuzione Condizionale]].

Le relazioni tra due v.a. si chiariscono studiando la **distribuzione condizionale** di una delle due, dato il valore dell'altra. Ricordiamo che, presi due eventi $E$ e $F$ con $P(F)>0$,

$$P(E\mid F)=\frac{P(E\cap F)}{P(F)}$$

È naturale applicare questo schema alle v.a. discrete.

> [!important] Definizione
> Siano $X$ e $Y$ discrete con PMF congiunta $p(\cdot,\cdot)$. La **funzione di massa di probabilità condizionata di $X$ dato $Y$** è la funzione di due variabili
> $$p_{X|Y}(x\mid y):=P(X=x\mid Y=y)=\frac{P(X=x,\,Y=y)}{P(Y=y)}=\frac{p(x,y)}{p_Y(y)}\qquad\forall x,\;\forall y\text{ con }p_Y(y)>0$$
> Al numeratore c'è la PMF **congiunta**, al denominatore la PMF **marginale**. Se $P(Y=y)=0$ la quantità non è definita.

Per ogni $y$ fissato, $x\mapsto p_{X|Y}(x\mid y)$ è una PMF a tutti gli effetti (valori non negativi, somma 1): nella tabella congiunta corrisponde a prendere la **colonna** $Y=y$ e dividerla per la sua somma.

> [!example]
> Nell'urna di prima, la distribuzione di $R$ sapendo che $B=1$: la colonna $B=1$ è $(\frac2{15},\frac6{15},0)$ con somma $\frac8{15}$, quindi $P(R=0\mid B=1)=\frac14$, $P(R=1\mid B=1)=\frac34$, $P(R=2\mid B=1)=0$.

Se $X$ e $Y$ sono indipendenti, $p_{X|Y}(x\mid y)=\frac{p_X(x)p_Y(y)}{p_Y(y)}=p_X(x)$: condizionare non cambia nulla. Da qui partirà il [[04 - PS - Valore Atteso, Varianza e Covarianza#Valore atteso condizionato|valore atteso condizionato]]. _(dispensa, p. 30)_
