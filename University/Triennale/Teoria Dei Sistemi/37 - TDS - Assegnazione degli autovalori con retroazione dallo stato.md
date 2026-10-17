---
title: Assegnazione degli autovalori con retroazione dallo stato
aliases:
  - TDS — Assegnazione degli autovalori con retroazione dallo stato
tags:
  - teoria-dei-sistemi
  - retroazione-dallo-stato
  - assegnazione-autovalori
  - forma-canonica-raggiungibile
  - raggiungibilita
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 242–248); libro Monaco et al., §9.1–9.1.1
---

# Assegnazione degli autovalori con retroazione dallo stato

> [!abstract] Scopo della lezione
> Con la [[34 - TDS - Sistemi interconnessi#Connessione in controreazione e semplificazioni|controreazione dall'uscita]] la dinamica cambia, ma non si controlla bene **come**. Qui si fa un passo in più: si legge lo **stato** e lo si riporta all'ingresso con una matrice $F$ di guadagni, $u=Fx+v$, così che la matrice dinamica diventi $A+BF$. Si mostra che:
> 1. si possono modificare **solo** gli autovalori della parte **raggiungibile** (quelli della parte non raggiungibile sono "modi fissi");
> 2. se il sistema è in **forma canonica raggiungibile**, gli autovalori si scelgono **arbitrariamente**, e la $F$ si legge direttamente dai coefficienti dei polinomi caratteristici;
> 3. un sistema raggiungibile qualsiasi si porta in forma canonica raggiungibile con un cambio di coordinate $T$ costruito dall'ultima riga di $R^{-1}$.
>
> Segue [[38 - TDS - Formula di Ackermann]], che calcola $F$ senza passare per $T$. Indice: [[MOC - Teoria dei Sistemi]].

## Modificare la dinamica di un sistema

Vedi [[TDS - Retroazione dallo stato]].

Un sistema, in generale, è sempre formato da sistemi più "piccoli" interconnessi al suo interno, e non è mai atomico. Ora interessa **modificare** alcune caratteristiche del sistema, come i modi naturali, con un certo fine. Dato

$$\mathcal S:\begin{cases}\dot x=Ax+Bu\\y=Cx\end{cases}$$

una prima idea è provare a modificarne la dinamica. Nella connessione in controreazione si è visto che il sistema, al di là della dinamica, resta pressoché lo stesso: $B$ e $C$ non cambiano, cambia solo $A$. Ora, invece di connettere l'**uscita** all'ingresso, si legge lo **stato** $x$ e si cerca di modificare direttamente quello:

![[TDS-L37-01.png]]

Con $u=Fx+v$ il sistema diventa

$$\begin{cases}\dot x=Ax+BFx+Bv\\y=Cx\end{cases}\Longrightarrow\begin{cases}\dot x=(A+BF)x+Bv\\y=Cx\end{cases}$$

e la matrice dinamica del nuovo sistema è

$$\bar A=A+BF$$

$F$ non è uno scalare ma una matrice con tante righe quanta è la dimensione dell'ingresso e tante colonne quanta quella dello stato ($p\times n$); con $p=q=1$, $F$ è $1\times n$.

> [!warning] Correzione
> Nella figura degli appunti l'ingresso **esterno** è chiamato $u$ e quello che entra in $\mathcal S$ è chiamato $v$, mentre nel testo (e nel libro) è il contrario: $u=Fx+v$, con $u$ ingresso di $\mathcal S$ e $v$ nuovo ingresso esterno. Qui si segue il testo.

> [!quote] Dal libro — il compensatore
> Il Capitolo 9 parte da uno schema generale (Figura 9.1): un sistema $\mathcal S$ e un **compensatore** $\mathcal C$ ($\dot\zeta=L\zeta+Mm+Nv$, $u=F\zeta+Gv$) che usa le misure $m(t)$. Il caso più semplice è il compensatore **istantaneo** ($\mu=0$) che misura lo stato ($m=x$): $u=Fx+Gv$, e il sistema modificato è $\dot x=(A+BF)x+BGv$. "**Problema dell'assegnazione degli autovalori.** Sotto quali condizioni comunque assegnata una $n$-pla di numeri complessi esiste una $F$ tale che gli autovalori di $(A+BF)$ coincidono con essa? Come calcolare la matrice di guadagni in retroazione, $F$, associata a una fissata collocazione?" _(libro, §9 e §9.1, pp. 335–337)_

## Modificare un sistema non raggiungibile

C'è un problema con questo approccio: si legge lo stato e si cerca di modificare il sistema **attraverso l'ingresso**. Si sta assumendo che il sistema sia tutto **raggiungibile**: se ci fosse una parte non raggiungibile, potrebbe non essere possibile modificarlo completamente. Verifichiamo.

Si ipotizza che $\mathcal S$ non sia tutto raggiungibile: la matrice di raggiungibilità $R=(B\ AB\ \cdots\ A^{n-1}B)$ ha rango **non pieno**, $\mathrm{rank}(R)=m<n$. Si costruisce $T^{-1}$ con i vettori di base di $\mathcal R=\mathrm{Im}(R)$ e un completamento:

$$T^{-1}=\big(\text{base di }\mathcal R\ \ \ \text{completamento}\big)$$

Le matrici del sistema iniziale (non in retroazione) diventano (vedi [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Partizione del sistema secondo la raggiungibilità|lezione 27]])

$$\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix},\qquad\tilde B=\begin{pmatrix}\tilde B_1\\0\end{pmatrix}$$

Con la stessa $T^{-1}$, il sistema chiuso in retroazione:

$$T\bar AT^{-1}=T(A+BF)T^{-1}=\underbrace{TAT^{-1}}_{\tilde A}+\underbrace{TB}_{\tilde B}\underbrace{FT^{-1}}_{\tilde F}=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix}+\begin{pmatrix}\tilde B_1\\0\end{pmatrix}\begin{pmatrix}\tilde F_1&\tilde F_2\end{pmatrix}=\begin{pmatrix}\tilde A_{11}+\tilde B_1\tilde F_1&\tilde A_{12}+\tilde B_1\tilde F_2\\0&\tilde A_{22}\end{pmatrix}$$

($\tilde F$ si divide arbitrariamente in due parti corrispondenti ai blocchi di $\tilde B$.) La matrice resta triangolare a blocchi: gli autovalori del sistema chiuso sono quelli di $\tilde A_{22}$ e quelli di $\tilde A_{11}+\tilde B_1\tilde F_1$. Poiché $\tilde A_{22}$ è la parte di dinamica non raggiungibile, l'approccio riesce a "manipolare" **solo la parte raggiungibile** del sistema.

Non sempre è un problema: se l'obiettivo è avere tutti gli autovalori a parte reale negativa (sistema asintoticamente stabile) e quelli di $\tilde A_{22}$ lo sono già, non serve modificare quella parte. Ma è importante sapere che **non si può fare nulla** sulla parte non raggiungibile, cioè su $\tilde A_{22}$.

> [!quote] Dal libro — modi fissi e stabilizzazione
> "Al variare di $F$ possono essere spostati ad arbitrio tutti gli autovalori che competono al sottosistema raggiungibile, mentre quelli del sottosistema non raggiungibile rimangono invariati (per questo si usa dire che i modi che competono al sottosistema non raggiungibile rappresentano i **modi fissi**)." Con il test di Hautus, i modi fissi sono quelli degli autovalori $\lambda$ per cui $\mathrm{rank}(A-\lambda I\ \ B)<n$. Ne seguono due risultati: la raggiungibilità completa è condizione **necessaria e sufficiente** per assegnare **ad arbitrio** gli autovalori; e il **problema della stabilizzazione** (portare tutti gli autovalori nel semipiano sinistro) è risolubile se e solo se **i modi fissi sono stabili** (il sistema è *stabilizzabile*). Poiché $\tilde F_2$ non influenza gli autovalori, si prende $\tilde F_2=0$. _(libro, §9.1, pp. 337–338, 341)_

## Modificare un sistema in forma canonica raggiungibile

Vedi [[TDS - Forme canoniche]].

Si supponga ora il sistema **completamente raggiungibile** (altrimenti ci si concentra sulla sua parte raggiungibile): la coppia $(A_{n\times n},B_{n\times p})$ è raggiungibile e $\mathrm{rank}(R)=n$. Si vuole vedere se è davvero possibile modificarlo arbitrariamente. Si parte dall'ipotesi che sia in [[31 - TDS - Algoritmi di realizzazione e forme canoniche#Forma canonica raggiungibile|forma canonica raggiungibile]]:

$$A_R=\begin{pmatrix}0&1&&&\\&0&1&&\\&&\ddots&\ddots&\\&&&0&1\\-a_0&-a_1&-a_2&\cdots&-a_{n-1}\end{pmatrix},\qquad B_R=\begin{pmatrix}0\\0\\\vdots\\0\\1\end{pmatrix}$$

con polinomio caratteristico $p_{A_R}(\lambda)=\lambda^n+a_{n-1}\lambda^{n-1}+\dots+a_1\lambda+a_0$. In retroazione dallo stato:

$$A_R+B_RF=A_R+\begin{pmatrix}0\\\vdots\\0\\1\end{pmatrix}\begin{pmatrix}f_1&\cdots&f_n\end{pmatrix}=A_R+\begin{pmatrix}0&0&\cdots&0\\\vdots&&&\vdots\\0&0&\cdots&0\\f_1&f_2&\cdots&f_n\end{pmatrix}=\begin{pmatrix}0&1&&\\&\ddots&\ddots&\\&&0&1\\-a_0+f_1&-a_1+f_2&\cdots&-a_{n-1}+f_n\end{pmatrix}$$

$F$ modifica **solo l'ultima riga**, e la matrice resta in forma compagna. Siccome l'ultima riga contiene i coefficienti del polinomio caratteristico (cambiati di segno), questo è

$$p_{\bar A}(\lambda)=\lambda^n+(a_{n-1}-f_n)\lambda^{n-1}+(a_{n-2}-f_{n-1})\lambda^{n-2}+\dots+(a_1-f_2)\lambda+(a_0-f_1)$$

Per avere autovalori $\lambda_1,\dots,\lambda_n$ arbitrari, il polinomio caratteristico desiderato è

$$p^*(\lambda)=(\lambda-\lambda_1)(\lambda-\lambda_2)\cdots(\lambda-\lambda_n)=\lambda^n+\beta_{n-1}\lambda^{n-1}+\dots+\beta_1\lambda+\beta_0$$

e basta porre $\beta_i=a_i-f_{i+1}$, cioè

$$f_i=a_{i-1}-\beta_{i-1}$$

> [!important] Assegnazione in forma canonica raggiungibile
> Se il sistema è tutto raggiungibile e in forma canonica raggiungibile, con coefficienti $a_0,\dots,a_{n-1}$ del polinomio caratteristico, la retroazione
> $$F=\begin{pmatrix}f_1&f_2&\cdots&f_n\end{pmatrix}=\begin{pmatrix}a_0-\beta_0&a_1-\beta_1&\cdots&a_{n-1}-\beta_{n-1}\end{pmatrix}$$
> assegna come autovalori le radici di $p^*(\lambda)$. Con opportuni $\beta_i$ la dinamica si modifica **in modo del tutto arbitrario**.

> [!note] Autovalori complessi
> "Arbitrari" va inteso con un vincolo: $F$ è reale, quindi $p^*$ deve avere coefficienti reali, e gli autovalori complessi vanno assegnati a **coppie coniugate**.

> [!example] Esempio (non presente negli appunti)
> $A_R=\begin{psmallmatrix}0&1\\2&1\end{psmallmatrix}$ ($p=\lambda^2-\lambda-2=(\lambda-2)(\lambda+1)$, instabile: $a_0=-2$, $a_1=-1$). Si vogliono autovalori $-1$ e $-2$: $p^*=\lambda^2+3\lambda+2$, $\beta_0=2$, $\beta_1=3$. Allora $F=(a_0-\beta_0\ \ a_1-\beta_1)=(-4\ \ -4)$ e $A_R+B_RF=\begin{psmallmatrix}0&1\\-2&-3\end{psmallmatrix}$, con polinomio $\lambda^2+3\lambda+2$ ✔.

## Portare un sistema in forma canonica raggiungibile

Se il sistema è raggiungibile e si riesce a portarlo in forma canonica raggiungibile, se ne modifica la dinamica come appena visto. Serve un cambio di coordinate $T$ che porti $\dot x=Ax+Bu$ in forma canonica raggiungibile. La nuova matrice degli ingressi $\tilde B=TB$, per essere quella della forma canonica, deve essere

$$\tilde B=TB=\begin{pmatrix}0\\0\\\vdots\\0\\1\end{pmatrix}$$

### Costruzione di $T$

Si parte dalla matrice $R=(B\ AB\ A^2B\ \cdots\ A^{n-1}B)$, che, essendo il sistema completamente raggiungibile, ha rango pieno ed è invertibile. Della sua inversa interessa solo l'**ultima riga**, che si chiama $\gamma'$:

$$R^{-1}=\begin{pmatrix}\star\\\vdots\\\star\\\gamma'\end{pmatrix}$$

Il motivo: $R^{-1}R=I$, e in particolare l'ultima riga del prodotto è

$$\begin{pmatrix}\gamma'B&\gamma'AB&\cdots&\gamma'A^{n-1}B\end{pmatrix}=\begin{pmatrix}0&\cdots&0&1\end{pmatrix}$$

Essendo uguali termine a termine, la relazione resta vera trasponendo:

$$\begin{pmatrix}\gamma'B\\\gamma'AB\\\vdots\\\gamma'A^{n-1}B\end{pmatrix}=\begin{pmatrix}\gamma'\\\gamma'A\\\vdots\\\gamma'A^{n-1}\end{pmatrix}B=\begin{pmatrix}0\\\vdots\\0\\1\end{pmatrix}\tag{$\spadesuit$}$$

La matrice che moltiplica $B$ è proprio il cambio di base $T$ cercato:

$$T=\begin{pmatrix}\gamma'\\\gamma'A\\\gamma'A^2\\\vdots\\\gamma'A^{n-1}\end{pmatrix}$$

### Invertibilità di $T$

Bisogna verificare che $T$ sia invertibile (altrimenti non esisterebbe $T^{-1}$). Invece del determinante, si moltiplica $T$ per una matrice che si sa non singolare, $R$, e si controlla il prodotto:

$$TR=\begin{pmatrix}\gamma'\\\gamma'A\\\vdots\\\gamma'A^{n-1}\end{pmatrix}\begin{pmatrix}B&AB&\cdots&A^{n-1}B\end{pmatrix}=\begin{pmatrix}0&\cdots&0&0&1\\0&\cdots&0&1&\star\\0&\cdots&1&\star&\star\\\vdots&&&&\vdots\\1&\star&\cdots&\star&\star\end{pmatrix}$$

L'elemento $(i,j)$ è $\gamma'A^{i+j-2}B$: gli elementi con $i+j-2\le n-2$ sono nulli per la ($\spadesuit$), quelli sull'antidiagonale ($i+j-2=n-1$) valgono 1, e gli altri (segnati $\star$: $\gamma'A^nB$, $\gamma'A^{n+1}B$, …) non interessano. La matrice è triangolare rispetto alla **diagonale secondaria**, con 1 su di essa, quindi non singolare: anche $T$ è non singolare, cioè **invertibile**.

> [!warning] Correzione
> Gli appunti scrivono $\det(TR)=(-1)^n$, motivando che il determinante di una matrice triangolare rispetto alla diagonale secondaria è il prodotto degli elementi su di essa moltiplicato per $(-1)^n$. Il segno corretto è $(-1)^{n(n-1)/2}$ (quello della permutazione che inverte l'ordine delle colonne): per esempio, per $n=2$ $\det\begin{psmallmatrix}0&1\\1&\star\end{psmallmatrix}=-1$, per $n=4$ vale $+1$. La conclusione ($\neq0$) non cambia.

### Verifica di $T$

Si deve verificare che il cambio di base dia la forma canonica raggiungibile, $TAT^{-1}=A_R$. È più semplice verificare l'espressione equivalente $TA=A_RT$:

$$\begin{pmatrix}\gamma'\\\gamma'A\\\vdots\\\gamma'A^{n-1}\end{pmatrix}A=A_R\begin{pmatrix}\gamma'\\\gamma'A\\\vdots\\\gamma'A^{n-1}\end{pmatrix}\iff A_R\begin{pmatrix}\gamma'\\\gamma'A\\\gamma'A^2\\\vdots\\\gamma'A^{n-1}\end{pmatrix}=\begin{pmatrix}\gamma'A\\\gamma'A^2\\\gamma'A^3\\\vdots\\\gamma'A^n\end{pmatrix}$$

Si ragiona "al contrario": come deve essere $A_R$ perché valga l'uguaglianza? Per ottenere $\gamma'A$ (primo elemento a destra) basta "scegliere" da $T$ il suo secondo elemento: la prima riga di $A_R$ è tutta di zeri tranne il secondo elemento, che vale 1. $\gamma'A$ non si può ottenere in altro modo, perché le righe di $T$ sono linearmente indipendenti ($T$ ha rango pieno). Allo stesso modo, per $\gamma'A^2$ si sceglie solo il terzo elemento di $T$, e così via fino alla penultima riga:

$$\begin{pmatrix}0&1&0&\cdots&0\\0&0&1&\cdots&0\\\vdots&&\ddots&\ddots&\vdots\\0&0&\cdots&0&1\\&&?&&\end{pmatrix}\begin{pmatrix}\gamma'\\\gamma'A\\\gamma'A^2\\\vdots\\\gamma'A^{n-1}\end{pmatrix}=\begin{pmatrix}\gamma'A\\\gamma'A^2\\\gamma'A^3\\\vdots\\\gamma'A^n\end{pmatrix}$$

All'ultima riga non c'è un termine di $T$ che dia direttamente $\gamma'A^n$. Ma per **Cayley-Hamilton**

$$p_A(A)=A^n+a_{n-1}A^{n-1}+\dots+a_2A^2+a_1A+a_0I=0\ \Longrightarrow\ A^n=-a_{n-1}A^{n-1}-\dots-a_1A-a_0I$$

e moltiplicando a sinistra per $\gamma'$:

$$\gamma'A^n=-a_{n-1}\gamma'A^{n-1}-\dots-a_2\gamma'A^2-a_1\gamma'A-a_0\gamma'$$

Il termine $\gamma'A^n$ è una combinazione lineare degli altri, e la relazione si completa:

$$\begin{pmatrix}0&1&&&\\&0&1&&\\&&\ddots&\ddots&\\&&&0&1\\-a_0&-a_1&-a_2&\cdots&-a_{n-1}\end{pmatrix}\begin{pmatrix}\gamma'\\\gamma'A\\\gamma'A^2\\\vdots\\\gamma'A^{n-1}\end{pmatrix}=\begin{pmatrix}\gamma'A\\\gamma'A^2\\\gamma'A^3\\\vdots\\\gamma'A^n\end{pmatrix}$$

La matrice ottenuta è esattamente $A_R$ (con i coefficienti del polinomio caratteristico di $A$, che il cambio di coordinate non cambia): la $T$ trovata è proprio quella giusta.

## Modificare un sistema raggiungibile qualsiasi

Se il sistema è completamente raggiungibile ma non in forma canonica raggiungibile, se ne modifica comunque la dinamica:
1. si fa il cambio di coordinate $T$, con $\gamma'$ ultima riga di $R^{-1}$:
   $$T=\begin{pmatrix}\gamma'\\\gamma'A\\\vdots\\\gamma'A^{n-1}\end{pmatrix},\qquad A_R=TAT^{-1},\quad B_R=TB,\quad z=Tx$$
2. si trova $F_R$ come nella sezione "Modificare un sistema in forma canonica raggiungibile", ottenendo la nuova matrice dinamica $\bar A=A_R+B_RF_R$;
3. si torna al sistema originale con il cambio di base inverso:
   $$T^{-1}\bar AT=T^{-1}(A_R+B_RF_R)T=T^{-1}(TAT^{-1})T+T^{-1}(TB)F_RT=A+BF_RT$$
   e la $F$ cercata è
   $$F=F_RT$$

> [!tip] Perché $F=F_RT$
> Nelle coordinate $z=Tx$ la retroazione è $u=F_Rz=F_RTx$: è la stessa legge di controllo, scritta nelle coordinate originali. Il libro lo enuncia come osservazione preliminare $O_1$: "se $F$ è la matrice di guadagni che assegna gli autovalori al sistema nelle coordinate $x$, allora $\tilde F=FT^{-1}$ assegna gli autovalori nelle coordinate $\tilde x=Tx$", perché $A+BF$ e $\tilde A+\tilde B\tilde F=T(A+BF)T^{-1}$ sono simili. _(libro, §9.1, p. 337)_

Nella [[38 - TDS - Formula di Ackermann|prossima lezione]] si vedrà come trovare direttamente $F$ senza tutti questi passaggi.

> [!quote] Dal libro — il caso generale (§9.1.1)
> Assegnato $\dot x=Ax+bu$ con $(A,b)$ raggiungibile, esiste $T_c$ non singolare tale che $T_cAT_c^{-1}=A_c$, $T_cb=b_c$ (forma canonica raggiungibile): con $\gamma=(0\ \cdots\ 0\ 1)R^{-1}$, $T_c=\begin{psmallmatrix}\gamma\\\gamma A\\\vdots\\\gamma A^{n-1}\end{psmallmatrix}$, invertibile perché $T_cR$ è triangolare secondaria. Calcolata $F_c$ per $(A_c,b_c)$, la retroazione su $(A,b)$ è $F=F_cT_c$. Il libro aggiunge la **forma canonica di Brunovsky**: con $F^0=-\gamma A^n$ si assegnano tutti gli autovalori a zero, e nelle coordinate $T_cx$ il sistema diventa una cascata di $n$ integratori. _(libro, §9.1.1, pp. 338–340)_
