---
title: Esercizio di realizzazione e matrice di Hankel
aliases:
  - TDS — Esercizio di realizzazione e matrice di Hankel
tags:
  - teoria-dei-sistemi
  - realizzazione
  - realizzazione-minima
  - matrice-di-hankel
  - esercizi
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 205–212); libro Monaco et al., §7.4–7.5
---

# Esercizio di realizzazione e matrice di Hankel

> [!abstract] Scopo della lezione
> Un solo nucleo $K(s)$ ($p=3$, $q=2$), realizzato in **quattro modi** per confrontarli: forma canonica raggiungibile (dimensione 6), osservabile (4), **per righe** (3, da verificare) e con l'**algoritmo di Gilbert** (3, minima per costruzione). Poi:
> - la **matrice di Hankel**, che dà la dimensione della realizzazione minima **senza** costruirla;
> - la realizzazione nel **tempo discreto** (stessi algoritmi);
> - in appendice, cosa cambia se la realizzazione per righe non fosse osservabile.
>
> Riprende [[31 - TDS - Algoritmi di realizzazione e forme canoniche]] e [[32 - TDS - Realizzazioni minime e realizzazione di Gilbert]]. Segue [[34 - TDS - Sistemi interconnessi]]. Indice: [[MOC - Teoria dei Sistemi]].

## Esempio pratico di realizzazione

Vedi [[TDS - Realizzazione minima]].

$$K(s)=\begin{pmatrix}\frac1{s+1}&\frac1s&\frac1{s(s+1)}\\[1mm]\frac1s&1&0\end{pmatrix}$$

Qual è il procedimento migliore per una realizzazione minima? Il sistema ha due uscite e tre ingressi: $p=3$, $q=2$. Esplicitando il denominatore:

$$K(s)=\frac{\begin{pmatrix}s&s+1&1\\s+1&s(s+1)&0\end{pmatrix}}{s(s+1)}$$

Si vede subito che $n=2$ (grado massimo del denominatore). La funzione **non** è strettamente propria: al numeratore c'è un termine dello stesso grado del denominatore, $s(s+1)$. Si rende strettamente propria esplicitando divisione e resto:

$$K(s)=\underbrace{\frac{\begin{pmatrix}s&s+1&1\\s+1&0&0\end{pmatrix}}{s(s+1)}}_{K'(s)}+\underbrace{\begin{pmatrix}0&0&0\\0&1&0\end{pmatrix}}_{D}$$

Il termine problematico era $s(s+1)$, che diviso per il denominatore dà proprio 1: lo si separa dagli altri. La matrice costante ottenuta è $D$; quello che resta è la funzione strettamente propria su cui basare la realizzazione, $K'(s)$.

Si può scegliere fra tre algoritmi. Con la forma canonica raggiungibile la dimensione sarebbe $N=np=2\cdot3=6$; con quella osservabile $N=nq=2\cdot2=4$. Conviene la seconda, ma per scopo illustrativo si mostrano entrambe.

### Realizzazione in forma canonica raggiungibile

Si scrive $K'(s)$ esplicitando i coefficienti del numeratore e del denominatore:

$$K'(s)=\frac{\begin{pmatrix}s&s+1&1\\s+1&0&0\end{pmatrix}}{s(s+1)}=\frac{\overbrace{\begin{pmatrix}1&1&0\\1&0&0\end{pmatrix}}^{B_1}s+\overbrace{\begin{pmatrix}0&1&1\\1&0&0\end{pmatrix}}^{B_0}}{s^2+s},\qquad a_0=0,\ a_1=1$$

Ogni blocco è $3\times3$:

$$A_R=\begin{pmatrix}O&I\\-a_0I&-a_1I\end{pmatrix}=\left(\begin{array}{ccc|ccc}0&0&0&1&0&0\\0&0&0&0&1&0\\0&0&0&0&0&1\\\hline0&0&0&-1&0&0\\0&0&0&0&-1&0\\0&0&0&0&0&-1\end{array}\right),\qquad B_R=\begin{pmatrix}O\\I\end{pmatrix}$$

$$C_R=\begin{pmatrix}B_0&B_1\end{pmatrix}=\left(\begin{array}{ccc|ccc}0&1&1&1&1&0\\1&0&0&1&0&0\end{array}\right)$$

Per sapere se c'è una parte inosservabile bisognerebbe studiare l'osservabilità. In realtà si è già visto che la forma canonica osservabile porta a dimensione 4, e non 6: in questa rappresentazione ci sono sicuramente parti superflue.

### Realizzazione in forma canonica osservabile

Stavolta i blocchi hanno dimensione 2:

$$A_O=\begin{pmatrix}O&-a_0I\\I&-a_1I\end{pmatrix}=\left(\begin{array}{cc|cc}0&0&0&0\\0&0&0&0\\\hline1&0&-1&0\\0&1&0&-1\end{array}\right),\qquad B_O=\begin{pmatrix}B_0\\B_1\end{pmatrix}=\begin{pmatrix}0&1&1\\1&0&0\\1&1&0\\1&0&0\end{pmatrix},\qquad C_O=\begin{pmatrix}O&I\end{pmatrix}=\begin{pmatrix}0&0&1&0\\0&0&0&1\end{pmatrix}$$

Un sistema di dimensione 4: è la più piccola? **Non si può sapere** finché non si studia la raggiungibilità (studio che negli appunti è omesso).

> [!example] Lo studio omesso (non presente negli appunti)
> Le colonne di $B_O$ sono $c_1=(0,1,1,1)'$, $c_2=(1,0,1,0)'$, $c_3=(1,0,0,0)'$, indipendenti: rango 3. Le righe di $A_OB_O$ sono $(0,0,0)$, $(0,0,0)$, $(0,1,1)-(1,1,0)=(-1,0,1)$ e $(1,0,0)-(1,0,0)=(0,0,0)$, quindi le sue colonne sono $(0,0,-1,0)'$, $0$, $(0,0,1,0)'$; ma $(0,0,1,0)'=c_2-c_3$ sta già nello span di $B_O$, e lo stesso vale per le potenze successive. Quindi $\mathrm{rank}\,R=3<4$: lo spazio raggiungibile ha dimensione 3 e la realizzazione osservabile ha **una** dimensione superflua. Togliendola (scomposizione rispetto alla raggiungibilità) si arriva a dimensione 3, come nei due metodi seguenti.

### Realizzazione per righe

Si spera di riuscire a partizionare il sistema per righe o colonne. Scomponendo $K'(s)$ per righe si ottengono $K_1(s)$ e $K_2(s)$, con rispettivamente **due** poli e **un** polo: in tutto tre. È meno di 4, ma più di 2: bisognerà comunque verificare raggiungibilità e osservabilità.

$$K'(s)=\begin{pmatrix}\frac1{s+1}&\frac1s&\frac1{s(s+1)}\\[1mm]\frac1s&0&0\end{pmatrix}=\begin{pmatrix}K_1(s)\\K_2(s)\end{pmatrix}$$

Due uscite che individuano due sistemi distinti:

$$Y_1(s)=K_1(s)U(s)=\begin{pmatrix}\frac1{s+1}&\frac1s&\frac1{s(s+1)}\end{pmatrix}U(s),\qquad Y_2(s)=K_2(s)U(s)=\begin{pmatrix}\frac1s&0&0\end{pmatrix}U(s)$$

Ognuno ha **una** uscita: conviene la forma canonica osservabile. Per il primo:

$$K_1(s)=\frac{(1\ \ 1\ \ 0)s+(0\ \ 1\ \ 1)}{s(s+1)},\qquad A_{1O}=\begin{pmatrix}0&-a_0\\1&-a_1\end{pmatrix}=\begin{pmatrix}0&0\\1&-1\end{pmatrix},\quad B_{1O}=\begin{pmatrix}B_{1,0}\\B_{1,1}\end{pmatrix}=\begin{pmatrix}0&1&1\\1&1&0\end{pmatrix},\quad C_{1O}=\begin{pmatrix}0&1\end{pmatrix}$$

Per il secondo:

$$K_2(s)=\frac{(1\ \ 0\ \ 0)}{s}$$

$A_{2O}$ è $1\times1$ (uno scalare): si parte dalla matrice di zeri, si mette 1 sotto la diagonale (qui non c'è spazio) e si sostituisce l'ultima (e unica) colonna con $-a_0$:

$$A_{2O}=-a_0=0,\qquad B_{2O}=(B_{2,0})=\begin{pmatrix}1&0&0\end{pmatrix},\qquad C_{2O}=1$$

Unendo: $Y(s)=\begin{psmallmatrix}Y_1\\Y_2\end{psmallmatrix}=K'(s)U(s)$, con stato complessivo $x=\begin{psmallmatrix}x_1\\x_2\end{psmallmatrix}$:

$$\begin{cases}\dot x_1=A_{1O}x_1+B_{1O}u\\y_1=C_{1O}x_1+D_1u\end{cases},\quad\begin{cases}\dot x_2=A_{2O}x_2+B_{2O}u\\y_2=C_{2O}x_2+D_2u\end{cases}\Longrightarrow\begin{cases}\dot x=\begin{pmatrix}0&0&0\\1&-1&0\\0&0&0\end{pmatrix}x+\begin{pmatrix}0&1&1\\1&1&0\\1&0&0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}0&1&0\\0&0&1\end{pmatrix}x+Du\end{cases}$$

($D_1$, $D_2$ sono le righe di $D$.) Il lato negativo di questo approccio: anche se la dimensione è più piccola, si ottiene una forma **non canonica** per raggiungibilità e osservabilità, quindi vanno studiate **entrambe**.

**Raggiungibilità.** $R=(B\ \ AB\ \ A^2B)$. Il rango di $B$ è già pieno (determinante $-1$), quindi anche quello di $R$:

$$\mathrm{rank}\,R=3,\qquad\mathcal R=\mathbb R^3=\mathrm{span}\{e_1,e_2,e_3\}$$

(si è scelta la base canonica, ma va bene qualsiasi base di $\mathbb R^3$).

**Osservabilità.**

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}0&1&0\\0&0&1\\1&-1&0\\0&0&0\\-1&1&0\\0&0&0\end{pmatrix}$$

Già le prime tre righe hanno rango 3: il nucleo è lo spazio nullo, $\mathcal I=\{0\}$. Non ci sono parti inosservabili né irraggiungibili: non ci sono parti superflue, e **$N=3$ è la dimensione minima**.

### Realizzazione con l'algoritmo di Gilbert

Vedi [[TDS - Algoritmo di Gilbert]].

La condizione per l'algoritmo di Gilbert è che $K'(s)$ sia compatibile con una $A$ diagonale, cioè che tutte le radici del denominatore abbiano molteplicità 1: qui $s_1=0$ e $s_2=-1$, entrambe semplici. Poli e residui:

$$K'(s)=\frac{R_1}{s}+\frac{R_2}{s+1},\qquad R_1=\begin{pmatrix}0&1&1\\1&0&0\end{pmatrix},\qquad R_2=\begin{pmatrix}1&0&-1\\0&0&0\end{pmatrix}$$

$R_1$ ha rango **due** e $R_2$ rango **uno**: l'autovalore $\lambda_1=0$ (il polo di $R_1$) ha molteplicità due, e $\lambda_2=-1$ molteplicità uno. Quindi

$$A=\begin{pmatrix}\lambda_1&&\\&\lambda_1&\\&&\lambda_2\end{pmatrix}=\begin{pmatrix}0&&\\&0&\\&&-1\end{pmatrix}$$

Gli autovettori sono i vettori canonici, $u_{11}=e_1$, $u_{12}=e_2$, $u_2=e_3$, e

$$U=\begin{pmatrix}u_{11}&u_{12}&u_2\end{pmatrix}=I\quad\Longrightarrow\quad U^{-1}=I=\begin{pmatrix}v_{11}'\\v_{12}'\\v_2'\end{pmatrix}$$

$$W(s)=K'(s)\ \longleftrightarrow\ e^{0t}\big(Cu_{11}v_{11}'B+Cu_{12}v_{12}'B\big)+e^{-t}Cu_2v_2'B$$

$$C(u_{11}v_{11}'+u_{12}v_{12}')B=C_1B_1=R_1,\qquad Cu_2v_2'B=C_2B_2=R_2$$

> [!warning] Correzione
> Negli appunti la prima riga è scritta "$W(s)=K(s)=e^{0t}(\dots)+e^{-t}\dots$": a sinistra ci sono funzioni di $s$, a destra di $t$. Va letto come $W(t)=\mathcal L^{-1}[K'(s)]$ (e con $K'$, non $K$, perché $D$ è stata separata).

$R_1$ ha rango 2 ed è $2\times3$: $C_1$ e $B_1$ sono $2\times r$ e $r\times3$, con $r$ il rango di $R_1$, quindi $C_1$ è $2\times2$ e $B_1$ è $2\times3$. Analogamente $C_2$ e $B_2$ sono $2\times1$ e $1\times3$, perché $\mathrm{rank}\,R_2=1$. Si cercano

$$\underset{2\times2}{C_1}\cdot\underset{2\times3}{B_1}=\begin{pmatrix}0&1&1\\1&0&0\end{pmatrix},\qquad\underset{2\times1}{C_2}\cdot\underset{1\times3}{B_2}=\begin{pmatrix}1&0&-1\\0&0&0\end{pmatrix}$$

Si possono scegliere come si vuole. Un consiglio è scegliere l'identità quando si può (cioè quando la matrice è quadrata), come per $C_1$: con $C_1=I$, $B_1=R_1$. Per $R_2$, che ha la seconda riga di soli zeri, si sceglie $C_2=\begin{psmallmatrix}1\\0\end{psmallmatrix}$ e $B_2$ uguale alla prima riga di $R_2$:

$$\underbrace{\begin{pmatrix}1&0\\0&1\end{pmatrix}}_{C_1=I}\underbrace{\begin{pmatrix}0&1&1\\1&0&0\end{pmatrix}}_{B_1}=R_1,\qquad\underbrace{\begin{pmatrix}1\\0\end{pmatrix}}_{C_2}\underbrace{\begin{pmatrix}1&0&-1\end{pmatrix}}_{B_2}=R_2$$

Le matrici complete:

$$A=\begin{pmatrix}0&0&0\\0&0&0\\0&0&-1\end{pmatrix},\qquad B=\begin{pmatrix}B_1\\B_2\end{pmatrix}=\begin{pmatrix}0&1&1\\1&0&0\\1&0&-1\end{pmatrix},\qquad C=\begin{pmatrix}C_1&C_2\end{pmatrix}=\begin{pmatrix}1&0&1\\0&1&0\end{pmatrix}$$

più la $D$ trovata all'inizio. Dimensione 3, come per righe: le due realizzazioni sono minime e differiscono per un cambio di coordinate.

| Metodo | Dimensione | Minima? |
|---|---|---|
| forma canonica raggiungibile | $np=6$ | no |
| forma canonica osservabile | $nq=4$ | no (rango di $R$ = 3) |
| per righe | $2+1=3$ | sì (verificato con $R$ e $\mathcal O$) |
| Gilbert | $\mathrm{rank}\,R_1+\mathrm{rank}\,R_2=3$ | sì, per costruzione |

## Determinare la dimensione minima tramite $k(t)$

Vedi [[TDS - Matrice di Hankel]].

Lo studio di $K(s)$ nel dominio di Laplace è molto più utile e significativo di quello del nucleo $k(t)$ nel dominio del tempo. Esiste però un algoritmo basato su $k(t)$ che, sotto certe condizioni, permette di determinare la dimensione della realizzazione minima. Si basa sulla **matrice di Hankel**:

$$H=\begin{pmatrix}H_0&H_1&H_2&H_3&\cdots\\H_1&H_2&H_3&&\\H_2&H_3&\ddots&&\\H_3&&&\ddots&\\\vdots&&&&\end{pmatrix},\qquad H_i=\left[\frac{d^i}{dt^i}k(t)\right]_{t=0}$$

(ogni antidiagonale ha lo stesso blocco). **La dimensione della realizzazione minima è il rango di $H$.** Se si ha $K(s)$, non è difficile trovare $k(t)=\mathcal L^{-1}[K(s)]$.

Il perché si costruisce $H$ così è semplice: se $k(t)=W(t)=Ce^{At}B$,

$$H_0=k(0)=CB,\qquad H_1=\left[\frac{d}{dt}Ce^{At}B\right]_{t=0}=\big[CAe^{At}B\big]_{t=0}=CAB,\qquad H_2=CA^2B,\ \dots$$

$$H=\begin{pmatrix}CB&CAB&CA^2B&\cdots\\CAB&CA^2B&&\\CA^2B&&\ddots&\\\vdots&&&\end{pmatrix}=\begin{pmatrix}C\\CA\\CA^2\\\vdots\end{pmatrix}\begin{pmatrix}B&AB&A^2B&\cdots\end{pmatrix}$$

La prima riga di $H$ è $C\cdot R$, con $R$ la matrice di raggiungibilità; la prima colonna è $\mathcal O\cdot B$, con $\mathcal O$ la matrice di osservabilità. La matrice "combina" le due proprietà e dà subito la dimensione minima, perché la realizzazione minima, provenendo direttamente da una $W(t)$, è tutta raggiungibile e tutta osservabile.

> [!tip] Perché il rango è la dimensione minima
> $H=\mathcal O\,R$ (con infinite righe e colonne, ma per Cayley-Hamilton bastano $n$ blocchi). Per una realizzazione minima $\mathcal O$ ha rango pieno di colonna e $R$ rango pieno di riga, entrambi pari a $n$: allora $\mathrm{rank}\,H=n$. Per una realizzazione non minima il prodotto "perde" le direzioni non raggiungibili o inosservabili, e il rango di $H$ resta quello minimo. $H$ dipende solo da $k(t)$, non dalla realizzazione scelta.

> [!warning] Precisazione
> Nella costruzione si assume che $k(t)$ non contenga l'impulso $D\delta(t)$: i coefficienti sono i **parametri di Markov** $CA^iB$, e $D$ non conta nella dimensione. Il libro scrive $S_i=CA^iB$, $i\ge0$.

> [!quote] Dal libro — Teorema 7.5.1
> "Un nucleo $K(t)$ di dimensione $q\times p$ che stabilisce un funzionale lineare strettamente causale tra $p$-ingressi e $q$-uscite ammette una rappresentazione con lo stato se e solo se è soddisfatta una delle seguenti quattro condizioni: (i) esistono $n$, $A$, $B$, $C$ tali che $Ce^{At}B=K(t)$; (ii) esistono due matrici di funzioni $Q(t)$ e $P(t)$ tali che $K(t-\tau)=Q(t)P(\tau)$ (**fattorizzabilità**); (iii) la matrice di Hankel associata a $K(t)$ ha **dimensione finita** [rango finito]; (iv) la trasformata $K(s)$ è una matrice di funzioni razionali strettamente proprie." E: "le realizzazioni minime hanno dimensioni pari al rango della matrice di Hankel $H$", un test che permette di calcolare la dimensione minima "senza calcolarne una realizzazione". _(libro, §7.5, pp. 307–309)_

## Realizzazione di un sistema a tempo discreto

Finora si è partiti da $k(t)\leftrightarrow K(s)$ nel tempo continuo. Nel tempo discreto:

$$y(t)=\sum_{\tau=0}^{t}k(t-\tau)u(\tau)\iff Y(z)=K(z)U(z)$$

Dato il nucleo

$$k(t)=\begin{cases}CA^{t-1}B&t\ge1\\D&t=0\end{cases}\iff K(z)=C(zI-A)^{-1}B+D$$

si cerca una soluzione $(n,A,B,C,D)$. **È tutto analogo al tempo continuo: gli algoritmi sono gli stessi.** Si può definire anche la matrice di Hankel, con $H_i=k(i)$.

> [!warning] Correzione
> Negli appunti si scrive $K(z)=C(zI-A)^{-1}B$, senza $D$ (che invece compare in $k(0)$), e la matrice di Hankel discreta è costruita da $H_0=k(0)=D$:
> $$H=\begin{pmatrix}D&CB&CAB&\cdots\\CB&CAB&&\\\vdots&&\ddots\end{pmatrix}$$
> Per la dimensione minima i coefficienti vanno presi da $t=1$: $H_i=k(i+1)=CA^iB$ (il libro scrive $S_i=K(i)$, $i=1,2,\dots$). Con $D$ in posizione $(1,1)$ il rango potrebbe risultare più grande di quello vero. Fatta questa correzione, la matrice coincide con quella del tempo continuo.

> [!quote] Dal libro — §7.4
> "Tutto quanto detto a proposito della realizzazione si estende, con il necessario cambio di notazioni, al caso dei sistemi a tempo discreto. Poiché la struttura della funzione di trasferimento non cambia le soluzioni sono esattamente le stesse, basta sostituire la variabile $z$ nelle espressioni del nucleo e nella trasformata della risposta impulsiva." _(libro, §7.4, p. 307)_

## Appendice: se la realizzazione per righe non fosse osservabile

Si prenda il sistema ottenuto con la realizzazione per righe, ma con una matrice $C$ diversa:

$$\begin{cases}\dot x=\begin{pmatrix}0&0&0\\1&-1&0\\0&0&0\end{pmatrix}x+\begin{pmatrix}0&1&1\\1&1&0\\1&0&0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}0&1&1\end{pmatrix}x\end{cases}$$

> [!warning] Correzione
> Gli appunti introducono l'appendice con "prendi il paragrafo **Realizzazione in forma canonica osservabile**", ma il sistema riportato (matrici $3\times3$) è quello del paragrafo **Realizzazione per righe**.

Il procedimento sarebbe identico, ma la matrice di osservabilità sarebbe diversa:

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}0&1&1\\1&-1&0\\-1&1&0\end{pmatrix}$$

La terza riga è un multiplo della seconda: il rango è 2 e il nucleo ha dimensione 1. Il vettore generatore si trova sommando le prime due colonne e sottraendo la terza:

$$\mathcal I=\mathrm{span}\left\{\begin{pmatrix}1\\1\\-1\end{pmatrix}\right\}$$

Essendoci una parte inosservabile ($\mathcal I$ non vuoto), il sistema **non è minimo**, e bisogna fare il cambio di coordinate rispetto all'inosservabilità. $T^{-1}$ ha come prima colonna $(1,1,-1)'$ e un completamento arbitrario (qui uno possibile):

$$T^{-1}=\left(\begin{matrix}1\\1\\-1\end{matrix}\ \middle|\ \text{completamento}\right)=\begin{pmatrix}1&0&0\\1&1&0\\-1&0&1\end{pmatrix}$$

Le matrici in queste coordinate sono

$$\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde B_1\\\tilde B_2\end{pmatrix},\qquad\tilde C=\begin{pmatrix}0&\tilde C_2\end{pmatrix}$$

e poiché $\tilde A_{11}$ e $\tilde A_{12}$ contengono parti inosservabili (vedi [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Partizione del sistema secondo l'osservabilità|lezione 27]]), il nuovo sistema avrà come matrice dinamica solo $\tilde A_{22}$, e come altre matrici $\tilde B_2$ e $\tilde C_2$.
