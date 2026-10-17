---
title: Scomposizione rispetto all'osservabilità e raggiungibilità
aliases:
  - TDS — Scomposizione rispetto all'osservabilità e raggiungibilità
tags:
  - teoria-dei-sistemi
  - osservabilita
  - raggiungibilita
  - scomposizione
  - tempo-discreto
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 158–164); libro Monaco et al., §6.1–6.2
---

# Scomposizione rispetto all'osservabilità e raggiungibilità

> [!abstract] Scopo della lezione
> 1. Si completa la [[26 - TDS - Stati inosservabili|lezione precedente]]: nelle coordinate che mettono in evidenza lo spazio inosservabile $\mathcal I$, il sistema si **spezza in due sottosistemi**, di cui solo uno arriva all'uscita (**comportamento interno** ed **esterno**); osservabilità nel **tempo discreto**; un esempio numerico.
> 2. La proprietà duale: la **raggiungibilità**. Gli stati raggiungibili sono l'immagine della **matrice di raggiungibilità** $\mathcal R=(B\ AB\ \cdots\ A^{n-1}B)$, e nelle coordinate che mettono in evidenza $\mathcal R$ l'ingresso arriva solo a una parte del sistema.
>
> Le due scomposizioni insieme danno la [[TDS - Scomposizione di Kalman|scomposizione di Kalman]]. Segue [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman]]. Indice: [[MOC - Teoria dei Sistemi]].

## Partizione del sistema secondo l'osservabilità

Vedi [[TDS - Osservabilità]].

Il sottospazio degli stati inosservabili è

$$\mathcal I=\mathrm{Sol}\left\{\begin{pmatrix}C\\CA\\\vdots\\CA^{n-1}\end{pmatrix}x_I=0\right\}=\mathrm{span}\{v_1,\dots,v_m\}$$

> [!warning] Correzione
> Negli appunti è scritto $\ker\{v_1,\dots,v_m\}$: i vettori $v_i$ sono una **base** di $\mathcal I$, quindi $\mathcal I=\mathrm{span}\{v_1,\dots,v_m\}$ (il nucleo è quello di $\mathcal O$).

Con $\mathcal O$ la matrice di osservabilità, $\mathcal I=\ker\mathcal O$ e $m=\dim\ker\mathcal O$. Uno stato inosservabile nelle coordinate $z=Tx$ ha la forma $z_I=(z_1,\dots,z_m,0,\dots,0)'$; $T^{-1}$ è formata dai vettori di base di $\mathcal I$ e da un **completamento** di $n-m$ vettori indipendenti:

$$T^{-1}=\Big(\underbrace{\text{vettori di base di }\mathcal I}_{m}\ \Big|\ \underbrace{\text{completamento}}_{n-m}\Big)$$

> [!warning] Correzione
> Gli appunti scrivono "completamento con $m-n$ vettori": sono $n-m$.

Le matrici del sistema si partizionano:

$$\tilde A=\begin{pmatrix}\overbrace{\tilde A_{11}}^{m}&\overbrace{\tilde A_{12}}^{n-m}\\0&\tilde A_{22}\end{pmatrix}\begin{matrix}\}m\\\}n-m\end{matrix},\qquad\tilde B=\begin{pmatrix}\tilde B_1\\\tilde B_2\end{pmatrix},\qquad\tilde C=\big(\underbrace{0}_{m}\ \ \underbrace{\tilde C_2}_{n-m}\big)$$

e il sistema diventa $\dot z=\tilde Az+\tilde Bu$, $y=\tilde Cz+\tilde Du$. Per mettere in evidenza le caratteristiche lo si "divide" in due parti, partizionando lo stato $z=\begin{psmallmatrix}z_1\\z_2\end{psmallmatrix}$: $z_1$ contiene le $m$ componenti relative alla base di $\mathcal I$ (stati inosservabili), $z_2$ le altre $n-m$ (completamento):

$$\dot z=\begin{pmatrix}\dot z_1\\\dot z_2\end{pmatrix}=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix}\begin{pmatrix}z_1\\z_2\end{pmatrix}+\begin{pmatrix}\tilde B_1\\\tilde B_2\end{pmatrix}u\quad\Longrightarrow\quad\begin{cases}\dot z_1=\tilde A_{11}z_1+\tilde A_{12}z_2+\tilde B_1u\\\dot z_2=\tilde A_{22}z_2+\tilde B_2u\\y=\tilde C_2z_2\end{cases}$$

Lo schema:

![[TDS-L27-01.png]]

L'ingresso arriva a entrambi i blocchi, $z_2$ influenza $z_1$ (la freccia verso l'alto), ma solo $z_2$ arriva all'uscita: anche se c'è dinamica sia in $z_1$ sia in $z_2$, esternamente si vede solo quella di $z_2$, mentre quella di $z_1$ (tratteggiato) non "perviene". Con questa partizione si ha una chiara distinzione tra **comportamento interno** (c'è tutto $z$) ed **esterno** (è come se ci fosse solo $z_2$).

Si vede anche calcolando $\tilde\Psi$ (la matrice esponenziale di una triangolare a blocchi è triangolare a blocchi, con gli esponenziali dei blocchi diagonali):

$$\tilde\Psi(t)=\tilde Ce^{\tilde At}=\begin{pmatrix}0&\tilde C_2\end{pmatrix}\begin{pmatrix}e^{\tilde A_{11}t}&\star\\0&e^{\tilde A_{22}t}\end{pmatrix}=\begin{pmatrix}0&\tilde C_2e^{\tilde A_{22}t}\end{pmatrix}$$

In uscita compaiono solo i modi naturali presenti in $\tilde A_{22}$: coerentemente con la definizione, gli autovalori che non stanno in $\Psi$ (cioè quelli di $\tilde A_{11}$) sono proprio quelli **inosservabili**.

> [!note] Precisazione sugli autovalori multipli
> Le definizioni sono chiare quando $A$ è diagonalizzabile, più "confuse" con i blocchi di Jordan. Nel caso regolare i modi osservabili sono proprio quelli degli autovalori di $\tilde A_{22}$. Ma se un autovalore $\lambda_i$ ha molteplicità $\mu_i>1$ può comparire sia in $\tilde A_{11}$ sia in $\tilde A_{22}$; per questo la definizione si limita al caso in cui ogni autovalore ha molteplicità 1.

Tutti questi ragionamenti riguardano la parte **libera**; la parte forzata è identica nei due sistemi di riferimento: $\tilde W(t)=\tilde\Psi(t)\tilde B=W(t)$ (il legame ingresso-uscita non dipende dalle coordinate).

> [!quote] Dal libro — Figura 6.1
> "Entrambi i sottosistemi sono influenzati da $u$, il sottosistema $S_2$ non è influenzato da $S_1$, mentre vale il viceversa, e l'uscita è caratterizzata dal solo sottosistema $S_2$. In questa forma è evidente che il sottosistema $S_1$ non influenza $y$ né direttamente né indirettamente tramite $S_2$." Il legame forzato è caratterizzato dal solo sottosistema osservabile: $W(t)=Ce^{At}B=(0\ \ C_2)\begin{psmallmatrix}e^{A_{11}t}&\star\\0&e^{A_{22}t}\end{psmallmatrix}\begin{psmallmatrix}B_1\\B_2\end{psmallmatrix}=C_2e^{A_{22}t}B_2$. "Si può dimostrare che se un sistema $S$ è tutto osservabile allora, e solo allora, tutti i modi sono osservabili."
>
> Esempio 6.1.1: $A=\begin{psmallmatrix}-2&0\\1&-1\end{psmallmatrix}$, $C=(1\ 0)$: $\mathcal O=\begin{psmallmatrix}1&0\\-2&0\end{psmallmatrix}$, $\mathcal I=\mathrm{gen}\{(0,1)'\}$; con $T^{-1}=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$ le matrici assumono la forma a blocchi. _(libro, §6.1, pp. 265–266)_

## Osservabilità nel tempo discreto

Ripartendo dal ragionamento della scorsa volta, nel tempo discreto: con due condizioni iniziali distinte $x_{0a}$ e $x_{0b}$,

$$y_a(t)=\Psi(t)x_{0a}+\sum_{\tau=0}^{t-1}W(t-\tau)u(\tau),\qquad y_b(t)=\Psi(t)x_{0b}+\sum_{\tau=0}^{t-1}W(t-\tau)u(\tau)$$

Ponendole uguali per ogni $t\ge0$ e sottraendo: $\Psi(t)(x_{0a}-x_{0b})=0$, che nel discreto vale se e solo se

$$CA^tx_I\equiv0\quad\forall t\ge0$$

La condizione non cambia rispetto al continuo: se $Cx_I=0,\ CAx_I=0,\dots,CA^{n-1}x_I=0$, per Cayley-Hamilton vale anche $CA^kx_I=0$ per ogni $k\ge n$, quindi $CA^tx_I\equiv0$. Si ha sempre

$$\Psi(t)(x_{0a}-x_{0b})=0\iff\mathcal Ox_I=0$$

Il resto è del tutto analogo al continuo; l'unica differenza è $z(t+1)$ al posto di $\dot z(t)$.

> [!tip] Più diretto che nel continuo
> Nel discreto non serve nemmeno il teorema sulle derivate: $CA^tx_I=0$ per $t=0,1,\dots,n-1$ **sono** le righe di $\mathcal Ox_I=0$. Osservando l'uscita libera per $n$ passi si ricostruiscono esattamente le informazioni che $\mathcal O$ contiene.

## Esempio pratico

$$\begin{cases}\dot x=\begin{pmatrix}0&1&1\\0&1&2\\0&0&-1\end{pmatrix}x+\begin{pmatrix}1\\1\\0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}1&-1&0\end{pmatrix}x\end{cases}$$

Si calcola $\mathcal O$ e si trova $\mathcal I=\ker\mathcal O$:

$$\mathcal O=\begin{pmatrix}C\\CA\\CA^2\end{pmatrix}=\begin{pmatrix}1&-1&0\\0&0&-1\\0&0&1\end{pmatrix}$$

Ogni riga, a parte la prima ($C$), è la riga precedente per $A$: $CA^2=CA\cdot A=(0\ 0\ -1)A=(0\ 0\ 1)$, senza calcolare $A^2$. $\mathcal O$ ha rango 2, quindi il nucleo ha dimensione $m=1$:

$$\mathcal I=\ker\mathcal O=\mathrm{span}\left\{\begin{pmatrix}1\\1\\0\end{pmatrix}\right\}$$

Cambio di coordinate $z=Tx$: $T^{-1}$ ha $m=1$ vettore di base di $\mathcal I$ e altri 2 indipendenti (arbitrari, purché i tre siano indipendenti):

$$T^{-1}=\left(\begin{matrix}1\\1\\0\end{matrix}\ \middle|\ \begin{matrix}0&0\\1&0\\0&1\end{matrix}\right),\qquad T=\begin{pmatrix}1&0&0\\-1&1&0\\0&0&1\end{pmatrix}$$

Le matrici del sistema risultano partizionate come previsto:

$$\tilde A=TAT^{-1}=\begin{pmatrix}1&0&0\\-1&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}0&1&1\\0&1&2\\0&0&-1\end{pmatrix}\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}=\begin{pmatrix}\boxed{1}&1&1\\0&0&1\\0&0&-1\end{pmatrix}=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix}$$

$$\tilde C=CT^{-1}=\begin{pmatrix}1&-1&0\end{pmatrix}\begin{pmatrix}1&0&0\\1&1&0\\0&0&1\end{pmatrix}=\begin{pmatrix}0&-1&0\end{pmatrix}=\begin{pmatrix}0&\tilde C_2\end{pmatrix}$$

($\tilde B$ si tralascia, non è significativo qui.) Gli autovalori sono tre e distinti ($1$, $0$, $-1$), quindi ognuno ha molteplicità 1: il sistema ha un modo naturale **non osservabile** relativo all'autovalore $\lambda_1=1$, perché sta in $\tilde A_{11}$; gli altri due modi, relativi a $\lambda_2=0$ e $\lambda_3=-1$, sono osservabili.

> [!tip] Verifica
> $\tilde A_{22}=\begin{psmallmatrix}0&1\\0&-1\end{psmallmatrix}$, $\tilde C_2=(-1\ 0)$: la matrice di osservabilità della coppia $(\tilde A_{22},\tilde C_2)$ è $\begin{psmallmatrix}-1&0\\0&-1\end{psmallmatrix}$, di rango pieno. La parte "esterna" del sistema è tutta osservabile, come dice il libro.

Inoltre, se il modo naturale $c_1e^{\lambda_1t}u_1$ è inosservabile, $Cu_1=0$ (vedi [[06 - TDS - Modi naturali#Modi naturali non osservabili|lezione 6]]); nelle nuove coordinate vale ancora $\tilde C\tilde u_1=0$, ed essendo $\tilde C$ partizionata con una parte nulla:

$$\tilde C\tilde u_1=\begin{pmatrix}0&\tilde C_{21}&\tilde C_{22}\end{pmatrix}\begin{pmatrix}\tilde u_{11}\\\tilde u_{12}\\\tilde u_{13}\end{pmatrix}=\tilde C_{21}\tilde u_{12}+\tilde C_{22}\tilde u_{13}=0\ \Longrightarrow\ \tilde u_{12}=0,\ \tilde u_{13}=0$$

cioè $\tilde u_1=(\star,0,0)'$ ha le ultime $n-m$ componenti nulle: l'autovettore del modo inosservabile sta nel sottospazio degli stati inosservabili, $\tilde u_1\in\mathcal I$.

> [!warning] Precisazione
> Nell'esempio $\tilde C_2=(-1\ \ 0)$, cioè $\tilde C_{22}=0$: da $\tilde C\tilde u_1=0$ si ricava direttamente solo $\tilde u_{12}=0$. Che anche $\tilde u_{13}=0$ si deduce dal fatto che $\tilde u_1$ è autovettore di $\tilde A$ per $\lambda=1$, che non è autovalore di $\tilde A_{22}$: dalla terza riga, $-\tilde u_{13}=\tilde u_{13}$. Infatti $u_1=(1,1,0)'$ (base di $\mathcal I$) dà $\tilde u_1=Tu_1=(1,0,0)'$.

## Raggiungibilità di uno stato nel tempo discreto

Vedi [[TDS - Raggiungibilità]].

Fissata una condizione iniziale $x_0$, mettendo nel sistema tutti gli ingressi possibili, si riesce a far assumere a $x(t)$ qualsiasi valore? $x(t)$ copre tutto lo spazio di stato, o ci sono punti non raggiungibili qualunque sia l'ingresso? Uno stato $\hat x$ si dice **raggiungibile** all'istante $T$ partendo da $x_0$ se esiste un ingresso $u(t)$ tale che

$$\hat x(T)=\Phi(T)x_0+\sum_{\tau=0}^{T-1}H(T-\tau)u(\tau)$$

Se, fissati $x_0$ e $T$, non si raggiunge $\hat x$ con alcun ingresso, lo stato non è raggiungibile. Una semplificazione importante: se $\hat x$ è raggiungibile da $x_0=0$, è raggiungibile da qualsiasi $x_0$.

> [!note] Precisazione
> L'ultima affermazione vale nel tempo **continuo** (e nel discreto con $A$ invertibile): basta sommare all'ingresso che porta da 0 a $\hat x$ quello che porta $\Phi(T)x_0$ in zero (la **controllabilità**, vedi il libro più sotto). Nel tempo discreto con $A$ singolare raggiungibilità da zero e controllabilità a zero possono differire. Per questo, di solito, si definisce la raggiungibilità **dallo stato zero**.

Si parte dall'equazione $x(t+1)=Ax(t)+Bu(t)$ con $t_0=0$ e $x_0=0$:

$$x(1)=Ax(0)+Bu(0)=Bu(0)$$

Ci sono già stati raggiungibili: tutti quelli nell'**immagine** di $B$ (l'insieme dei valori che può assumere $Bu$, vedi [[27 - GEO - Immagine]]). Quindi se $x\in\mathrm{Im}(B)$, $x$ è sicuramente raggiungibile; lo si indica con $x_R$.

$$x(2)=Ax(1)+Bu(1)=ABu(0)+Bu(1)=\begin{pmatrix}B&AB\end{pmatrix}\begin{pmatrix}u(1)\\u(0)\end{pmatrix}$$

Agli stati in $\mathrm{Im}(B)$ si aggiungono quelli in $\mathrm{Im}(AB)$: $\mathrm{Im}(B\ \ AB)$ contiene stati tutti raggiungibili. Continuando:

$$x(3)=Ax(2)+Bu(2)=A^2Bu(0)+ABu(1)+Bu(2)$$

e $\mathrm{Im}(B\ \ AB\ \ A^2B)$ contiene stati tutti raggiungibili. Si prosegue fino a

$$\mathrm{Im}\begin{pmatrix}B&AB&A^2B&\cdots&A^{n-1}B\end{pmatrix}$$

Arrivati qui non ha senso continuare: per Cayley-Hamilton $A^n$ è combinazione lineare delle potenze precedenti, quindi le colonne di $A^nB$, $A^{n+1}B$, … sono linearmente dipendenti da quelle già presenti.

> [!important] Spazio degli stati raggiungibili
> La matrice
> $$R:=\begin{pmatrix}B&AB&A^2B&\cdots&A^{n-1}B\end{pmatrix}$$
> ($n\times np$) è la **matrice di raggiungibilità**: la sua immagine $\mathcal R$ contiene tutti e soli gli stati raggiungibili, $x_R\in\mathrm{Im}(R)=\mathcal R$. Una base di $\mathcal R$ è formata dalle **colonne indipendenti** di $R$. Il sistema è **completamente raggiungibile** se e solo se $\mathrm{rank}\,R=n$.

Si può dire anche **dopo quanti istanti** uno stato è raggiungibile: se $x_R\in\mathrm{Im}(B\ \ AB\ \ A^2B)$ ma $x_R\notin\mathrm{Im}(B\ \ AB)$, lo stato è raggiungibile per $t\ge3$.

> [!warning] Correzione
> Gli appunti scrivono $x_R\in(B\ \ AB\ \ A^2B)$: va inteso $x_R\in\mathrm{Im}(B\ \ AB\ \ A^2B)$.

## Partizione del sistema secondo la raggiungibilità

Come per l'osservabilità, conviene un cambio di coordinate che metta in evidenza la raggiungibilità. Con $z=Tx\iff x=T^{-1}z$, per la stessa logica degli stati inosservabili:

$$T^{-1}=\big(\text{vettori di base di }\mathcal R\ \big|\ \text{completamento}\big)$$

Nelle nuove coordinate

$$\tilde R=TR=\begin{pmatrix}\tilde B&\tilde A\tilde B&\tilde A^2\tilde B&\cdots&\tilde A^{n-1}\tilde B\end{pmatrix},\qquad\tilde{\mathcal R}=\mathrm{Im}(\tilde R)$$

(perché $T A^kB=TA^kT^{-1}TB=\tilde A^k\tilde B$). Ogni stato $z$ ha due "set" di componenti, quelle legate alla raggiungibilità e le altre, e ogni stato raggiungibile ha solo le prime:

$$z=\begin{pmatrix}z_1\\z_2\end{pmatrix},\qquad z_R=\begin{pmatrix}z_1\\0\end{pmatrix}$$

Poiché per ogni $t\ge1$ tutti gli elementi di $\tilde{\mathcal R}$ sono raggiungibili, in particolare per $t=1$, dove gli stati raggiunti sono $\mathrm{Im}(\tilde B)$: ogni elemento dell'immagine di $\tilde B$ deve avere la parte non legata a $\mathcal R$ nulla:

$$\mathrm{Im}(\tilde B)\subseteq\tilde{\mathcal R}\quad\Longrightarrow\quad\tilde Bv=\begin{pmatrix}\star\\0\end{pmatrix}\ \forall v\qquad\Longrightarrow\qquad\tilde B=\begin{pmatrix}\tilde B_1\\0\end{pmatrix}$$

($\tilde B_1$ è un blocco di righe, non un singolo elemento.) $\tilde C=(\tilde C_1\ \ \tilde C_2)$ invece può avere qualsiasi forma.

> [!warning] Correzione
> Gli appunti scrivono $\tilde{\mathcal R}=\mathrm{Im}(\tilde B)$: in generale vale solo l'inclusione $\mathrm{Im}(\tilde B)\subseteq\tilde{\mathcal R}$ (gli stati raggiungibili in un passo sono **alcuni** dei raggiungibili). Il ragionamento resta valido: basta che ogni colonna di $\tilde B$ stia in $\tilde{\mathcal R}$.

Anche nel caso della raggiungibilità, se $x$ è raggiungibile anche $Ax$ lo è (la dimostrazione è la stessa degli stati inosservabili): **$\mathcal R$ è invariante rispetto ad $A$**. Quindi $\tilde A$ ha la stessa struttura:

$$\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix}$$

e il sistema diventa

$$\begin{cases}\dot z_1=\tilde A_{11}z_1+\tilde A_{12}z_2+\tilde B_1u\\\dot z_2=\tilde A_{22}z_2\\y=\tilde C_1z_1+\tilde C_2z_2\end{cases}$$

![[TDS-L27-02.png]]

Nell'uscita contribuiscono sia le parti raggiungibili sia quelle non raggiungibili, e $z_2$ influenza $z_1$; ma **l'ingresso arriva solo alle parti raggiungibili**. La parte $z_2$ non influisce sul rapporto ingresso-stato; infatti

$$\tilde H=e^{\tilde At}\tilde B=\begin{pmatrix}e^{\tilde A_{11}t}&\star\\0&e^{\tilde A_{22}t}\end{pmatrix}\begin{pmatrix}\tilde B_1\\0\end{pmatrix}=\begin{pmatrix}e^{\tilde A_{11}t}\tilde B_1\\0\end{pmatrix}$$

In $\tilde H$ compaiono solo i modi degli autovalori di $\tilde A_{11}$, mentre quelli di $\tilde A_{22}$ si perdono: $\tilde A_{11}$ contiene gli autovalori **eccitabili**, $\tilde A_{22}$ quelli **non eccitabili** (sempre se $\mu_i=1$; negli altri casi la distinzione non è così immediata).

> [!important] Le due scomposizioni a confronto
> | | Osservabilità | Raggiungibilità |
> |---|---|---|
> | matrice | $\mathcal O=(C;\,CA;\,\dots;\,CA^{n-1})$ | $R=(B\ AB\ \cdots\ A^{n-1}B)$ |
> | sottospazio | $\mathcal I=\ker\mathcal O$ (inosservabili) | $\mathcal R=\mathrm{Im}\,R$ (raggiungibili) |
> | proprietà | $A$-invariante, contenuto in $\ker C$ | $A$-invariante, contiene $\mathrm{Im}\,B$ |
> | struttura | $\tilde A$ triangolare, $\tilde C=(0\ \tilde C_2)$ | $\tilde A$ triangolare, $\tilde B=(\tilde B_1;0)$ |
> | autovalori di $\tilde A_{11}$ | inosservabili | eccitabili |
> | proprietà completa | $\mathrm{rank}\,\mathcal O=n$ | $\mathrm{rank}\,R=n$ |
>
> Le due proprietà sono **duali**: $(A,C)$ è osservabile se e solo se $(A',C')$ è raggiungibile, perché $\mathcal O(A,C)'=R(A',C')$.

> [!quote] Dal libro — Teorema 6.2.1 ed esempi
> Il libro definisce la raggiungibilità nel continuo, con $\mathcal R(T)=\{x:x=\int_{t_0}^Te^{A(T-\tau)}Bu(\tau)d\tau\}$, e mostra con l'operatore aggiunto (e il lemma $\mathrm{Im}(\mathcal L)=\ker(\mathcal L^*)^\perp$) che $\mathcal R=\mathrm{Im}(B\ AB\ \cdots\ A^{n-1}B)$, la **matrice di raggiungibilità**.
> - Esempio 6.2.1: $A=\begin{psmallmatrix}1&-2\\0&3\end{psmallmatrix}$, $B=\begin{psmallmatrix}-1\\-1\end{psmallmatrix}$: $R=\begin{psmallmatrix}-1&1\\-1&-3\end{psmallmatrix}$ ha rango pieno, il sistema è tutto raggiungibile.
> - Esempio 6.2.2: stessa $A$, $B=\begin{psmallmatrix}-1\\0\end{psmallmatrix}$: $R=\begin{psmallmatrix}-1&-1\\0&0\end{psmallmatrix}$, $\mathcal R=\mathrm{gen}\{(-1,0)'\}$: sono raggiungibili tutti e soli gli stati $(\alpha,0)'$.
> - Esempio 6.2.3, il **pendolo inverso** controllato alla base: linearizzando attorno alla verticale, $A=\begin{psmallmatrix}0&1\\g/l&0\end{psmallmatrix}$, $B=\begin{psmallmatrix}0\\-1/(ml)\end{psmallmatrix}$, $R$ ha rango 2: il pendolo si può riportare in verticale (per piccoli spostamenti).
>
> Nel continuo si può raggiungere $x_R$ in un tempo $T$ **arbitrario** con $u(t)=B'e^{-A't}G^{-1}e^{-AT}x_R$, dove $G=\int_0^Te^{-A\tau}BB'e^{-A'\tau}d\tau$ (il **gramiano**); e tutti e soli gli stati raggiungibili sono anche **controllabili** (portabili a zero). _(libro, §6.2, pp. 267–272)_
