---
title: Osservatore asintotico dello stato
aliases:
  - TDS — Osservatore asintotico dello stato
tags:
  - teoria-dei-sistemi
  - osservatore
  - osservabilita
  - formula-di-ackermann
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 253–259); libro Monaco et al., §9.2–9.2.2
---

# Osservatore asintotico dello stato

> [!abstract] Scopo della lezione
> La [[37 - TDS - Assegnazione degli autovalori con retroazione dallo stato|retroazione dallo stato]] richiede di **misurare lo stato** $x$, che spesso non è accessibile: si misura solo l'uscita $y$. Qui si costruisce un sistema che **stima** lo stato:
> 1. una copia del sistema funziona solo se il sistema è stabile, e non si controlla la velocità di convergenza;
> 2. aggiungendo una correzione proporzionale all'**errore d'uscita**, $K(y-Cz)$, l'errore di stima evolve con $A-KC$: è l'**osservatore asintotico**;
> 3. si possono assegnare gli autovalori di $A-KC$ **solo** nella parte **osservabile** (problema duale della retroazione dallo stato);
> 4. la formula per $K$, duale di Ackermann: $K=p^*(A)\rho$, con $\rho$ ultima colonna di $\mathcal O^{-1}$;
> 5. la **costante di tempo** e un esempio con due serbatoi.
>
> Segue [[40 - TDS - Principio di separazione]]. Indice: [[MOC - Teoria dei Sistemi]].

## Stimare lo stato di un sistema

Vedi [[TDS - Osservatore asintotico]].

Non sempre è possibile prendere informazioni sullo stato direttamente dal sistema: non sempre si può accedere alla $x$ per fare una retroazione e modificare la dinamica. Come si può risalire allo stato senza "guardare" dentro il sistema? Del sistema si conosce la descrizione:

$$\mathcal S:\begin{cases}\dot x=Ax+Bu\\y=Cx\end{cases}$$

ma è "chiuso": non si conosce $x$ in ogni istante, né $x_0$. Un'idea è prendere un secondo sistema $\mathcal S_2$ con la stessa rappresentazione:

$$\mathcal S_2:\begin{cases}\dot z=Az+Bu\\y=Cz\end{cases}$$

![[TDS-L39-01.png]]

Si può dire che lo stato dei due sistemi coincide, $z(t)=x(t)$ per ogni $t\ge0$? Dalle forme esplicite

$$x(t)=\Phi(t)x_0+\int_0^tH(t-\tau)u(\tau)\,d\tau,\qquad z(t)=\Phi(t)z_0+\int_0^tH(t-\tau)u(\tau)\,d\tau$$

($\Phi$ e $H$ sono uguali perché lo sono $A$ e $B$) si ha

$$z(t)-x(t)=\Phi(t)(z_0-x_0)$$

Basterebbe $z_0=x_0$; ma poiché $\mathcal S$ è chiuso non si vede lo stato e non si conosce $x_0$, che servirebbe per creare un sistema identico. (E anche riuscendoci, non si potrebbe mai essere sicuri che sia **davvero** identico, perché non lo si può verificare.)

Indicando però con $e(t)$ l'errore tra $z$ e $x$,

$$e(t)=z(t)-x(t)=\Phi(t)e_0$$

si definisce un nuovo sistema con $e$ come stato:

$$\dot e=\dot z-\dot x=Az+Bu-Ax-Bu=A(z-x)=Ae$$

Se l'errore è prossimo allo zero, la differenza tra i due sistemi è minima: se il sistema in $e$ è **asintoticamente stabile** ($e(t)\to0$), per $t$ abbastanza grande l'errore è molto piccolo e i due stati sono praticamente uguali:

$$\lim_{t\to+\infty}\|e(t)\|=0\iff\lim_{t\to+\infty}\|z(t)-x(t)\|=0$$

In questo caso avrebbe senso costruire un sistema "aperto" in $z$ sulla base del sistema "chiuso" in $x$. Ma restano due problemi:
- se il sistema iniziale **non è stabile**, questo approccio non funziona;
- nelle applicazioni non si può aspettare un tempo infinito: quanto bisogna aspettare dipende dalla rapidità con cui vanno a zero i modi naturali, cioè dal valore assoluto degli autovalori di $A$, che **non si possono scegliere**.

## L'osservatore asintotico

La soluzione è includere nello stato del secondo sistema l'**errore** stesso, in modo proporzionale: così si può "far comportare" $\mathcal S_2$ in modo molto simile a $\mathcal S$, basandosi sull'errore tra i due.

![[TDS-L39-02.png]]

Con $y_z$ l'uscita di $\mathcal S_2$ e $e_y=y-y_z$ l'**errore sulle uscite** (misurabile!), si introduce nello stato in $z$ il termine $Ke_y$:

$$\mathcal O:\begin{cases}\dot z=Az+Bu+Ke_y\\y_z=Cz\end{cases}$$

$$\dot z=Az+Bu+K(y-y_z)=Az+Bu+K(Cx-Cz)=(A-KC)z+Bu+KCx$$

cioè, poiché $Cx=y$ è misurata, $\dot z=(A-KC)z+Bu+Ky$: un sistema che ha in ingresso $u$ (comune ai due sistemi) e $y$ (l'uscita del primo). L'errore:

$$\dot e=\dot z-\dot x=(A-KC)z+Bu+KCx-Ax-Bu=(A-KC)z-(A-KC)x=(A-KC)(z-x)=(A-KC)e$$

Questo sistema, che rappresenta l'errore, deve tendere a zero, cioè essere asintoticamente stabile: con la matrice $K$ bisogna modificarne la dinamica in modo che **gli autovalori di $A-KC$ abbiano tutti parte reale negativa** (e, se possibile, scelti a piacere, per fissare la velocità di convergenza). Questo vale a prescindere dalla stabilità del sistema di partenza.

> [!quote] Dal libro — ricostruttore e osservatore
> "Dato il sistema $\mathcal S$, un sistema dinamico lineare $\Theta$ avente per ingressi gli ingressi e le uscite di $\mathcal S$ (ovvero $y$ e $u$) e per uscite $n$ variabili $z_1,\dots,z_n$ […] è detto **ricostruttore asintotico dello stato** se il vettore $z(t)$ tende asintoticamente a $x(t)$." Il libro distingue il **problema dell'osservatore** (ricostruire lo stato con caratteristiche di convergenza **predefinite**: autovalori di $A-KC$ assegnabili ad arbitrio) dal **problema della ricostruzione** (basta che l'errore vada a zero). Lo schema (Figura 9.2) è una copia $\mathcal{CS}$ del sistema modificata "mediante un intervento proporzionale allo scostamento tra $y=Cx$ e $\bar y=Cw$". _(libro, §9.2–9.2.1, pp. 343–346)_

## Condizioni di osservabilità

Vedi [[TDS - Osservabilità]].

Quando è possibile? Se $z$ non fosse tutto osservabile, in uscita potrebbero mancare delle informazioni; questo ricade su $e_y$, che rientra nello stato, quindi non si potrebbe modificare come si vorrebbe lo stato del sistema. Il problema è l'**osservabilità**.

Si fa il cambio di base che mette in evidenza la parte inosservabile ([[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Partizione del sistema secondo l'osservabilità|lezione 27]]): $T^{-1}$ ha prima i vettori di base di $\mathcal I$ (nucleo di $\mathcal O$), poi un completamento arbitrario:

$$T^{-1}=\big(\text{base di }\mathcal I\ \mid\ \text{completamento}\big),\qquad\tilde A=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix},\qquad\tilde C=\begin{pmatrix}0&\tilde C_2\end{pmatrix}$$

La parte osservabile ha matrice dinamica $\tilde A_{22}$ ($\tilde A_{11}$ è la dinamica inosservabile). Scomponendo $K$ secondo le stesse dimensioni:

$$\tilde A-\tilde K\tilde C=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}\\0&\tilde A_{22}\end{pmatrix}-\begin{pmatrix}\tilde K_1\\\tilde K_2\end{pmatrix}\begin{pmatrix}0&\tilde C_2\end{pmatrix}=\begin{pmatrix}\tilde A_{11}&\tilde A_{12}-\tilde K_1\tilde C_2\\0&\tilde A_{22}-\tilde K_2\tilde C_2\end{pmatrix}$$

Gli autovalori di $\tilde A-\tilde K\tilde C$ sono l'unione di quelli di $\tilde A_{11}$ e di $\tilde A_{22}-\tilde K_2\tilde C_2$: si possono modificare **solo** quelli di quest'ultima parte. Analogamente alla raggiungibilità e ai sistemi in retroazione, la dinamica di $\tilde A_{11}$ deve essere **accettabile** (già stabile), altrimenti non si può fare nulla.

> [!important] Osservabilità e osservatori
> - Gli autovalori di $A-KC$ si assegnano **ad arbitrio** se e solo se $(A,C)$ è **tutto osservabile**.
> - Esiste un osservatore (cioè un $K$ che rende stabile $A-KC$) se e solo se la parte **inosservabile** è asintoticamente stabile: il sistema è **rilevabile**.
>
> È esattamente il duale di raggiungibilità/stabilizzabilità della [[37 - TDS - Assegnazione degli autovalori con retroazione dallo stato#Modificare un sistema non raggiungibile|lezione 37]].

> [!quote] Dal libro — §9.2.2 Rilevabilità
> "Condizione necessaria e sufficiente affinché dato $\alpha$ esista un ricostruttore 'più rapido' di $e^{-\alpha t}$ è che gli autovalori di $A$ associati agli autovalori del sottosistema non osservabile appartengano a $\mathbb C^{-\alpha}$. […] Con $\alpha=0$, esistenza di un ricostruttore […] questa condizione è generalmente definita come **condizione di rilevabilità**." Con il test di Hautus, i modi fissi rispetto all'osservabilità sono quelli degli autovalori $\lambda$ per cui $\mathrm{rank}\begin{psmallmatrix}A-\lambda I\\C\end{psmallmatrix}<n$. _(libro, §9.2.2, pp. 346–348)_

### $K$ in forma canonica osservabile

Per trovare $K$ si usa lo stesso metodo usato per $F$. Prima si considera $\tilde A_{22}$ in [[31 - TDS - Algoritmi di realizzazione e forme canoniche#Forma canonica osservabile|forma canonica osservabile]]:

$$\tilde A_{22}-\tilde K_2\tilde C_2=\begin{pmatrix}0&&&-a_0\\1&0&&-a_1\\&\ddots&\ddots&\vdots\\&&1&-a_{n-1}\end{pmatrix}-\begin{pmatrix}k_1\\k_2\\\vdots\\k_n\end{pmatrix}\begin{pmatrix}0&\cdots&0&1\end{pmatrix}=\begin{pmatrix}0&&&-a_0-k_1\\1&0&&-a_1-k_2\\&\ddots&\ddots&\vdots\\&&1&-a_{n-1}-k_n\end{pmatrix}$$

È la forma canonica osservabile di un sistema con polinomio caratteristico di coefficienti $a_0+k_1,\dots,a_{n-1}+k_n$. Per ottenere il polinomio desiderato $p^*$ con coefficienti $\beta_0,\dots,\beta_{n-1}$ basta

$$\beta_i=a_i+k_{i+1}\iff k_i=\beta_{i-1}-a_{i-1}$$

> [!note] Precisazione
> Nella seconda matrice degli appunti le colonne nulle sono indicate con "$\cdots$" e le $k_i$ compaiono nell'**ultima** colonna (perché $\tilde C_2=(0\ \cdots\ 0\ 1)$): il prodotto $K\,\tilde C_2$ ha tutte le colonne nulle tranne l'ultima, che è $K$. È per questo che $K$ modifica solo l'ultima colonna della forma canonica osservabile.

## Trovare $K$ da un sistema generico

Vedi [[TDS - Formula di Ackermann]].

Se $\tilde A_{22}$ non è in forma canonica osservabile, il procedimento è analogo a quello della forma canonica raggiungibile: un cambio di coordinate verso la forma canonica osservabile, lì si trova $K$, e si torna indietro. Ma, tenendo presente cosa si è fatto con $F$, si può trovare direttamente l'analogo. In retroazione dallo stato

$$\sigma(A+BF)\in\mathcal D\subseteq\mathbb C^-$$

per una coppia $(A,B)$ **raggiungibile**; per l'osservatore

$$\sigma(A-KC)\in\mathcal D\subseteq\mathbb C^-$$

per una coppia $(A,C)$ **osservabile** ($\mathbb C^-$ indica i numeri complessi con parte reale negativa; $\mathbb R^-\subset\mathbb C^-$). Si passa da un caso all'altro con

$$\bar A=A^T,\qquad\bar B=C^T,\qquad\bar F=-K^T$$

Una matrice e la sua trasposta hanno gli stessi autovalori:

$$\sigma(A-KC)=\sigma\big((A-KC)^T\big)=\sigma\big(A^T-C^TK^T\big)=\sigma(\bar A+\bar B\bar F)$$

È identico al problema della retroazione dallo stato. Resta da vedere che $(\bar A,\bar B)$ sia raggiungibile:

$$\bar R=\begin{pmatrix}\bar B&\bar A\bar B&\cdots&\bar A^{n-1}\bar B\end{pmatrix}=\begin{pmatrix}C^T&A^TC^T&\cdots&(A^{n-1})^TC^T\end{pmatrix}\quad\Longrightarrow\quad\bar R^T=\begin{pmatrix}C\\CA\\\vdots\\CA^{n-1}\end{pmatrix}=\mathcal O$$

Il rango di $\bar R$ è quello di $\mathcal O$: è massimo se e solo se $(A,C)$ è osservabile, ed è proprio l'ipotesi di partenza. Con la [[38 - TDS - Formula di Ackermann|formula di Ackermann]]:

$$\bar F=-\gamma'p^*(\bar A)$$

dove $\gamma'$ è l'ultima riga di $\bar R^{-1}=(\mathcal O^T)^{-1}=(\mathcal O^{-1})^T$: equivale all'ultima **colonna** di $\mathcal O^{-1}$, che si chiama $\rho$, trasposta ($\gamma'$ è una riga, $\rho$ una colonna). Quindi $\bar F=-\rho^Tp^*(\bar A)$, e poiché $\bar F=-K^T$:

$$-K^T=-\rho^Tp^*(\bar A)\quad\Longrightarrow\quad K=\big[p^*(\bar A)\big]^T\rho$$

Ma $p^*(\bar A)=(A^T)^n+\beta_{n-1}(A^T)^{n-1}+\dots+\beta_0I=\big(A^n+\beta_{n-1}A^{n-1}+\dots+\beta_0I\big)^T=p^*(A)^T$, quindi $[p^*(\bar A)]^T=p^*(A)$:

> [!important] Formula di Ackermann per l'osservatore
> $$K=p^*(A)\,\rho,\qquad\rho=\text{ultima colonna di }\mathcal O^{-1}=\mathcal O^{-1}\begin{pmatrix}0\\\vdots\\0\\1\end{pmatrix}$$
> con $p^*$ il polinomio caratteristico desiderato per $A-KC$. Vale per una sola uscita ($q=1$) e $(A,C)$ osservabile.

> [!quote] Dal libro
> "$K'=-\eta'p^*(A')$ ove si è indicato con $\eta'$ l'ultima riga dell'inversa della matrice di raggiungibilità costruita con $A'$ e $-C'$. È semplice verificare che, a meno del segno, $\eta$ coincide con l'ultima colonna dell'inversa della matrice di osservabilità e quindi, passando ai trasposti, si ottiene $K=p^*(A)\eta$, $\eta=\mathcal O^{-1}(0,\dots,0,1)'$." _(libro, §9.2.2, p. 347)_

## Osservatore asintotico dello stato

Riassumendo: se interessa lo stato di un sistema chiuso che si può solo osservare, si crea un secondo sistema (o lo si immagina) a partire dalle matrici del sistema di partenza, che garantisca che lo stato, asintoticamente, sia uguale a quello del primo. Un sistema così si chiama **osservatore asintotico dello stato**:

$$\mathcal O:\ \dot z=(A-KC)z+Bu+Ky$$

**Scelta degli autovalori.** Per un modo naturale $e^{\lambda t}$ è $\lambda$ a determinare quanto "velocemente" va a zero al crescere di $t$. Mettendo in relazione un autovalore con il polo nella funzione di trasferimento:

$$(s-\lambda)=-\lambda\left(1+\frac{s}{-\lambda}\right)=-\lambda(1+s\tau)\qquad\Longrightarrow\qquad\lambda\leftrightarrow-\frac1\tau,\qquad e^{\lambda t}\leftrightarrow e^{-\frac t\tau}$$

La quantità $|\tau|$ si chiama **costante di tempo**, e i rapporti con $t$ sono più o meno costanti: per esempio, per $t\ge3\tau$, qualunque sia $\tau$, l'esponenziale è quasi zero ($e^{-3}\approx5\%$). In generale è utile per misurare la "rapidità" con cui un esponenziale va a zero.

> [!warning] Correzione
> Gli appunti scrivono $(s-\lambda)=-\lambda\big(1+\frac s\lambda\big)$: il fattore corretto è $1-\frac{s}{\lambda}$ (raccogliendo $-\lambda$: $s-\lambda=-\lambda\big(1-\frac s\lambda\big)$). Con $\lambda<0$ si ha $-\frac1\lambda=\tau>0$, e il risultato $\lambda\leftrightarrow-\frac1\tau$ è quello giusto (vedi la forma di Bode in [[22 - TDS - Risposta armonica e forma di Bode#Risposta armonica in forma di Bode|lezione 22]]).

> [!tip] Quanto rapido?
> Conviene scegliere gli autovalori dell'osservatore **più a sinistra** di quelli del sistema (tipicamente 3–10 volte più rapidi): così la stima converge prima che lo stato vero cambi molto. Troppo a sinistra però $K$ diventa grande e l'osservatore amplifica il rumore di misura su $y$.

## Esempio pratico

Un contenitore $\mathcal S_1$ contiene in ogni istante un volume di liquido $V_1(t)$. Il liquido passa da questo contenitore a un altro, $\mathcal S_2$, che contiene $V_2(t)$. In $\mathcal S_1$ entra dall'esterno una portata $q_1(t)$, mentre da $\mathcal S_2$ esce una portata $q_2(t)$. Si vuole conoscere $V_1(t)$ sapendo quanto vale $V_2(t)$.

![[TDS-L39-03.png]]

Si stima asintoticamente $V_1(t)$ con un osservatore. La portata versata da un contenitore è proporzionale al volume di liquido contenuto (per entrambi):

$$\begin{cases}\dot V_1=q_1-k_1V_1\\\dot V_2=k_1V_1-k_2V_2\end{cases}$$

L'uscita misurata è $q_2(t)=k_2V_2$ (o, equivalentemente, $V_2$), l'ingresso è $q_1(t)$:

$$\begin{cases}\dot V=\begin{pmatrix}-k_1&0\\k_1&-k_2\end{pmatrix}\begin{pmatrix}V_1\\V_2\end{pmatrix}+\begin{pmatrix}1\\0\end{pmatrix}u\\[2mm]y=\begin{pmatrix}0&1\end{pmatrix}V\end{cases}$$

Serve $V_1$: si costruisce un osservatore asintotico

$$\mathcal O:\ \dot z=(A-KC)z+Ky+Bu$$

**Osservabilità.**

$$\mathcal O=\begin{pmatrix}C\\CA\end{pmatrix}=\begin{pmatrix}0&1\\k_1&-k_2\end{pmatrix},\qquad\det\mathcal O=-k_1\neq0$$

Si può dire qualcosa sul sistema solo se questa matrice ha rango pieno (nucleo di dimensione zero, nulla di inosservabile). È una condizione banalmente vera: se $k_1$ fosse zero, $k_1V_1$ sarebbe zero e non ci sarebbe passaggio d'acqua dal primo contenitore al secondo (e dal secondo non si potrebbe sapere nulla del primo).

$$\mathcal O^{-1}=\begin{pmatrix}\frac{k_2}{k_1}&\frac1{k_1}\\1&0\end{pmatrix}\quad\Longrightarrow\quad\rho=\begin{pmatrix}\frac1{k_1}\\0\end{pmatrix}$$

**Autovalori dell'osservatore.** Si vuole un esponenziale che vada a zero, per esempio, dieci volte più velocemente di quelli del sistema (che sono $-k_1$ e $-k_2$). Gli appunti scelgono

$$p^*(\lambda)=(\lambda-10k_1)(\lambda-10k_2)=\lambda^2+(-10k_1-10k_2)\lambda+100k_1k_2$$

e calcolano

$$K=\big[A^2+\beta_1A+\beta_0I\big]\rho=\begin{pmatrix}11k_1^2+110k_1k_2&0\\-11k_1^2-11k_1k_2&110k_1k_2+11k_2^2\end{pmatrix}\begin{pmatrix}\frac1{k_1}\\0\end{pmatrix}=\begin{pmatrix}11k_1+110k_2\\-11k_1-11k_2\end{pmatrix}$$

> [!warning] Correzione
> Con $p^*(\lambda)=(\lambda-10k_1)(\lambda-10k_2)$ gli autovalori assegnati sono $+10k_1$ e $+10k_2$, **positivi**: l'errore $e(t)$ divergerebbe. Per un osservatore "dieci volte più rapido" servono $-10k_1$ e $-10k_2$, cioè
> $$p^*(\lambda)=(\lambda+10k_1)(\lambda+10k_2)=\lambda^2+10(k_1+k_2)\lambda+100k_1k_2$$
> Rifacendo il conto, $p^*(A)=A^2+10(k_1+k_2)A+100k_1k_2I$ ha prima colonna $\big(-9k_1^2+90k_1k_2,\ \ 9k_1^2+9k_1k_2\big)'$, e quindi
> $$K=p^*(A)\rho=\begin{pmatrix}-9k_1+90k_2\\9k_1+9k_2\end{pmatrix}$$
> Verifica: $A-KC=\begin{psmallmatrix}-k_1&-K_1\\k_1&-k_2-K_2\end{psmallmatrix}$ ha traccia $-(k_1+k_2+K_2)=-10(k_1+k_2)$ e determinante $k_1(k_2+K_2)+k_1K_1=k_1k_2+9k_1^2+9k_1k_2-9k_1^2+90k_1k_2=100k_1k_2$ ✔. Il calcolo degli appunti è corretto per il polinomio scelto, ma quel polinomio non dà un osservatore.

L'osservatore fornisce $z_1(t)\to V_1(t)$, la stima del volume nel primo contenitore, usando solo $q_1$ e la misura di $V_2$.
