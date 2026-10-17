---
title: Trasformata Zeta
aliases:
  - TDS — Trasformata Zeta
tags:
  - teoria-dei-sistemi
  - forma-di-jordan
  - esempio
  - trasformata-zeta
  - tempo-discreto
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 93–98); libro Monaco et al., §4.6.1
---

# Trasformata Zeta

> [!abstract] Scopo della lezione
> 1. Un **esercizio completo** su una matrice non diagonalizzabile: catene di autovettori, forma di Jordan, $e^{At}$ calcolata nei due modi (nel tempo e con la trasformata di Laplace) e conseguenze sulla **stabilità**. Applica quanto visto in [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori]].
> 2. Si introduce la **trasformata Zeta**, l'analogo per il tempo discreto della [[15 - TDS - Trasformata di Laplace|trasformata di Laplace]]: definizione, traslazione in avanti e all'indietro, e le matrici $\Phi(z)=z(zI-A)^{-1}$ e $H(z)=(zI-A)^{-1}B$.
>
> Segue [[19 - TDS - Antitrasformata Zeta]]. Indice: [[MOC - Teoria dei Sistemi]].

## Esercizio pratico

Vedi [[TDS - Forma di Jordan]].

$$A=\begin{pmatrix}-1&1&0\\0&0&1\\0&0&0\end{pmatrix}$$

Nelle matrici triangolari gli autovalori si leggono sulla diagonale principale: $\lambda_1=-1$ con molteplicità 1 e $\lambda_2=0$ con molteplicità 2.

| | $\lambda_1=-1$ | $\lambda_2=0$ |
|---|---|---|
| molteplicità algebrica | $\mu_1=1$ | $\mu_2=2$ |
| molteplicità geometrica | $\hat\mu_1=1$ | $\hat\mu_2=\ ?$ |

Se $\hat\mu_2=\mu_2=2$ si avrebbe $\Lambda_R=\mathrm{diag}(\lambda_1,\lambda_2,\lambda_2)$; altrimenti compare il blocco di Jordan:

$$\Lambda=\begin{pmatrix}\lambda_1&&\\&\lambda_2&1\\&0&\lambda_2\end{pmatrix}$$

Per la molteplicità geometrica di $\lambda_2$ serve $\dim\ker(A-\lambda_2I)$. Si può usare Gauss, oppure risolvere direttamente $(A-\lambda_2I)u_2=0$:

$$\begin{pmatrix}-1&1&0\\0&0&1\\0&0&0\end{pmatrix}\begin{pmatrix}a\\b\\c\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}\ \Longrightarrow\ \begin{cases}-a+b=0\\c=0\end{cases}$$

> [!warning] Correzione
> Negli appunti il sistema riporta $c=1$: dalla seconda riga si ha $c=0$, coerente con l'autovettore $u_2=(1,1,0)'$ trovato subito dopo.

Il rango di $A-\lambda_2I=A$ è 2, quindi il nucleo ha dimensione 1 ($\hat\mu_2=1$): c'è un solo autovettore. Con $a=b=1$:

$$u_2=\begin{pmatrix}1\\1\\0\end{pmatrix}$$

Poiché la molteplicità algebrica è 2 ma c'è un solo autovettore, si cerca $u_{22}$ tale che

$$(A-\lambda_2I)u_{22}=u_2\qquad\text{ovvero}\qquad(A-\lambda_2I)^2u_{22}=0$$

$$A^2=\begin{pmatrix}-1&1&0\\0&0&1\\0&0&0\end{pmatrix}\begin{pmatrix}-1&1&0\\0&0&1\\0&0&0\end{pmatrix}=\begin{pmatrix}1&-1&1\\0&0&0\\0&0&0\end{pmatrix}$$

$\ker A^2$ ha dimensione 2 (rango 1): ci sono due vettori di base, e bisogna prenderne uno **indipendente** da $u_2$. Si ottiene zero sia sommando le prime due colonne di $A^2$ sia sommando le ultime due, quindi due vettori possibili sono $(1,1,0)'$ e $(0,1,1)'$. Il primo è $u_2$, quindi

$$u_{22}=\begin{pmatrix}0\\1\\1\end{pmatrix}$$

> [!note] Con il metodo di Geometria
> $A^2$ è già a scalini ridotta: $a-b+c=0$, con $b=x$, $c=y$ parametri: $\ker A^2=\left\{x\begin{psmallmatrix}1\\1\\0\end{psmallmatrix}+y\begin{psmallmatrix}-1\\0\\1\end{psmallmatrix}\right\}$. Si poteva scegliere $u_{22}=(-1,0,1)'$; nell'esempio si continua con la scelta del professore. Verifica: $Au_{22}=(1,1,0)'=u_2$ ✔.

Quindi

$$\Lambda=\begin{pmatrix}\lambda_1&&\\&\boxed{\begin{matrix}\lambda_2&1\\0&\lambda_2\end{matrix}}\end{pmatrix}=\begin{pmatrix}-1&0&0\\0&\boxed{\begin{matrix}0&1\\0&0\end{matrix}}\end{pmatrix}$$

Manca $u_1$: $(A+I)u_1=0$, con $A+I=\begin{psmallmatrix}0&1&0\\0&1&1\\0&0&1\end{psmallmatrix}$, dà $u_1=(1,0,0)'$. Allora

$$U=\begin{pmatrix}u_1&u_2&u_{22}\end{pmatrix}=\begin{pmatrix}1&1&0\\0&1&1\\0&0&1\end{pmatrix},\qquad U^{-1}=\begin{pmatrix}1&-1&1\\0&1&-1\\0&0&1\end{pmatrix}$$

$$e^{At}=Ue^{\Lambda t}U^{-1}=U\begin{pmatrix}e^{\lambda_1t}&0&0\\0&\boxed{\begin{matrix}e^{\lambda_2t}&te^{\lambda_2t}\\0&e^{\lambda_2t}\end{matrix}}\end{pmatrix}U^{-1}=U\begin{pmatrix}e^{-t}&0&0\\0&\boxed{\begin{matrix}1&t\\0&1\end{matrix}}\end{pmatrix}U^{-1}$$

$$=\begin{pmatrix}e^{-t}&1&t\\0&1&1+t\\0&0&1\end{pmatrix}\begin{pmatrix}1&-1&1\\0&1&-1\\0&0&1\end{pmatrix}=\begin{pmatrix}e^{-t}&-e^{-t}+1&e^{-t}-1+t\\0&1&t\\0&0&1\end{pmatrix}$$

Compare la legge $e^{-t}$ del primo autovalore e le leggi del secondo: il "primo passo" (i termini costanti, gli 1, cioè $e^{0\cdot t}$) e il "secondo passo" (le $t$ di primo grado).

### Evoluzione libera e modi naturali

Moltiplicando per $x_0$, con $c=U^{-1}x_0=(c_1,c_{21},c_{22})'$:

$$e^{At}x_0=\begin{pmatrix}e^{-t}&1&t\\0&1&1+t\\0&0&1\end{pmatrix}\begin{pmatrix}c_1\\c_{21}\\c_{22}\end{pmatrix}=\begin{pmatrix}c_1e^{-t}+c_{21}+tc_{22}\\c_{21}+(t+1)c_{22}\\c_{22}\end{pmatrix}$$

Non è immediatamente comprensibile; per evidenziare i modi conviene tenere separato $U$:

$$e^{At}x_0=\begin{pmatrix}u_1&u_{21}&u_{22}\end{pmatrix}\begin{pmatrix}e^{-t}&0&0\\0&1&t\\0&0&1\end{pmatrix}\begin{pmatrix}c_1\\c_{21}\\c_{22}\end{pmatrix}=\begin{pmatrix}u_1&u_{21}&u_{22}\end{pmatrix}\begin{pmatrix}c_1e^{-t}\\c_{21}+tc_{22}\\c_{22}\end{pmatrix}$$

$$=c_1e^{-t}u_1+(c_{21}+tc_{22})\,u_{21}+c_{22}\,u_{22}$$

(con $u_{21}=u_2$). Il primo modo naturale è riconoscibile: quello aperiodico $c\,e^{-t}u_1$. Per il resto non è chiaro quali siano i modi naturali: il modo di $\lambda_2$ è l'insieme dei termini con $u_{21}$ e $u_{22}$, dove compare anche $t$.

> [!tip] Lettura geometrica
> La componente lungo $u_{22}$ resta costante ($c_{22}$), mentre quella lungo $u_{21}$ cresce linearmente con pendenza $c_{22}$: è la catena $u_{22}\to u_{21}$ della lezione precedente, che "versa" continuamente nella direzione dell'autovettore.

### Stabilità

Gli autovalori sono $-1$ e $0$, quindi a prima vista il sistema sarebbe **stabile semplicemente**. Ma allora l'evoluzione sarebbe limitata, e non lo è: mentre $e^{-t}\to0$, il termine $tc_{22}u_{21}$ va all'infinito. Se invece $\lambda_2$ fosse stato negativo, $t$ sarebbe stato moltiplicato per $e^{\lambda_2t}$ e sarebbe andato a zero. Quindi **nel caso non regolare un sistema che sembrerebbe semplicemente stabile può divergere**.

Nelle condizioni di limitatezza ($xy$ indica, a seconda del caso, gli autovalori osservabili, eccitabili o entrambi), $\mathrm{Re}(\Lambda_{xy})\le0$ va bene solo se non ci sono blocchi di Jordan (indice geometrico 1); se compaiono blocchi di Jordan (indice geometrico maggiore di 1) serve $\mathrm{Re}(\Lambda_{xy})<0$. Mettendo in evidenza l'indice geometrico:

$$\mathrm{Re}(\Lambda^1_{xy})\le0,\qquad\mathrm{Re}(\Lambda^{>1}_{xy})<0$$

È la stessa condizione già vista in [[11 - TDS - Punti di equilibrio e stabilità#Definizione operativa di stabilità|lezione 11]] ("gli autovalori con parte reale nulla devono avere molteplicità geometrica 1").

### Lo stesso calcolo con la trasformata

Vedi [[TDS - Antitrasformata e residui]].

Tutto si può fare, forse più semplicemente, con la trasformata:

$$e^{At}=\mathcal L^{-1}\big[(sI-A)^{-1}\big]=\mathcal L^{-1}\left[\begin{pmatrix}s+1&-1&0\\0&s&-1\\0&0&s\end{pmatrix}^{-1}\right]=\mathcal L^{-1}\left[\frac{\begin{pmatrix}s^2&s&1\\0&s(s+1)&s+1\\0&0&s(s+1)\end{pmatrix}}{s^2(s+1)}\right]$$

Come previsto è una funzione razionale strettamente propria: denominatore di terzo grado, numeratore al più di secondo grado. Si possono avere cancellazioni ma non possono "sparire" fattori: l'unico che si può semplificare è un $s$, non $s^2$. Al numeratore però $s$ non compare in **tutti** gli elementi, quindi non si semplifica, e si sa già che comparirà un termine in $t$ (polo doppio in 0, indice geometrico 2).

$$\mathcal L^{-1}\left[\frac{R_1}{s+1}+\frac{R_{21}}{s^2}+\frac{R_{22}}{s}\right]=R_1e^{-t}+R_{21}t+R_{22}$$

$$R_1=\lim_{s\to-1}(s+1)\frac{(\cdots)}{s^2(s+1)}=\lim_{s\to-1}\frac{\begin{pmatrix}s^2&s&1\\0&s(s+1)&s+1\\0&0&s(s+1)\end{pmatrix}}{s^2}=\begin{pmatrix}1&-1&1\\0&0&0\\0&0&0\end{pmatrix}$$

$$R_{21}=\lim_{s\to0}s^2\frac{(\cdots)}{s^2(s+1)}=\lim_{s\to0}\frac{\begin{pmatrix}s^2&s&1\\0&s(s+1)&s+1\\0&0&s(s+1)\end{pmatrix}}{s+1}=\begin{pmatrix}0&0&1\\0&0&1\\0&0&0\end{pmatrix}$$

$$R_{22}=\lim_{s\to0}\frac{d}{ds}\begin{pmatrix}\frac{s^2}{s+1}&\frac{s}{s+1}&\frac1{s+1}\\0&s&1\\0&0&s\end{pmatrix}=\lim_{s\to0}\begin{pmatrix}\frac{s^2+2s}{(s+1)^2}&\frac1{(s+1)^2}&-\frac1{(s+1)^2}\\0&1&0\\0&0&1\end{pmatrix}=\begin{pmatrix}0&1&-1\\0&1&0\\0&0&1\end{pmatrix}$$

Sommando $R_1e^{-t}+R_{21}t+R_{22}$ si ritrova esattamente la matrice calcolata prima. Questo approccio è forse più pulito, ma di nuovo il risultato è poco interpretabile: ci si concentra sulla **forma** (quali esponenziali, quali potenze di $t$).

> [!tip] Cosa dicono i residui
> $R_1$ ha rango 1 ed è $u_1v_1'$ (prima colonna di $U$ per prima riga di $U^{-1}$). $R_{21}$, il coefficiente di $t$, è nilpotente ($R_{21}^2=0$): è la traccia del blocco di Jordan. E $R_1+R_{22}=I$, perché $e^{A\cdot0}=I$.

## Trasformata nel tempo discreto

Vedi [[TDS - Trasformata Zeta]].

> [!note] Annotazione di Simone
> Prima del titolo, a mano in viola: **"TRASFORMATA tempo DISCRETO"**; le formule principali della sezione sono numerate a mano (1)–(4).

Nel tempo discreto lo stato è

$$x(t)=\Phi(t-t_0)x(t_0)+\sum_{\tau=t_0}^{t-1}H(t-\tau)u(\tau)\tag{1}$$

La somma forse è più semplice dell'integrale, ma bisogna comunque fare il prodotto tra $H$ e $u$ per tutti gli elementi della sommatoria. Esiste un corrispettivo discreto della trasformata di Laplace che semplifichi l'espressione di $x(t)$? Sarebbe comodo anche per mantenere il parallelismo con il tempo continuo. La vorremmo **lineare**, facile da calcolare e **biunivoca**: è la **trasformata Zeta**, che porta da $t\in\mathbb Z$ a $z\in\mathbb C$:

$$f(t)\longleftrightarrow F(z)=\mathcal Z[f(t)],\qquad F(z)=\sum_{t=0}^{\infty}f(t)\,z^{-t}\tag{2}$$

Anche questa funziona per $t\ge0$.

> [!note] Annotazione di Simone
> Accanto alla formula: **"Anziché $\mathcal L[\cdot]$ usiamo $\mathcal Z[\cdot]$ per indicare trasformata zeta"**.

> [!quote] Dal libro — raggio di convergenza
> Il termine generico $f(t)z^{-t}$ può essere reso piccolo per $t$ grande scegliendo $z$ di modulo abbastanza grande: la somma converge per $|z|>\rho_f$, dove $\rho_f$ è il **raggio di convergenza** (l'analogo dell'ascissa di convergenza di Laplace: un cerchio invece di un semipiano). _(libro, §4.6.1, p. 203)_

Trasformando la forma implicita, per linearità:

$$\mathcal Z[x(t+1)]=\mathcal Z[Ax(t)+Bu(t)]=A\mathcal Z[x(t)]+B\mathcal Z[u(t)]=AX(z)+BU(z)\tag{3}$$

### Traslazione in avanti

Come nel continuo serviva la trasformata della derivata, qui serve quella di $f(t+1)$. Con $\tau=t+1$:

$$\mathcal Z[f(t+1)]=\sum_{t=0}^{\infty}f(t+1)z^{-t}=\sum_{\tau=1}^{\infty}f(\tau)z^{-(\tau-1)}=z\sum_{\tau=1}^{\infty}f(\tau)z^{-\tau}=z\Bigg(\underbrace{\sum_{\tau=1}^{\infty}f(\tau)z^{-\tau}+f(0)}_{\mathcal Z[f(t)]}-f(0)\Bigg)=zF(z)-zf(0)\tag{4}$$

Quindi $\mathcal Z[x(t+1)]=zX(z)-zx(0)$. Da (3) e (4):

$$zX(z)-zx(0)=AX(z)+BU(z)\ \Longrightarrow\ (zI-A)X(z)=zx(0)+BU(z)$$

$$\boxed{X(z)=\underbrace{(zI-A)^{-1}z\,x(0)}_{\mathcal Z[\Phi(t)x_0]}+\underbrace{(zI-A)^{-1}BU(z)}_{\mathcal Z\left[\sum_{\tau=t_0}^{t-1}H(t-\tau)u(\tau)\right]}}$$

Confrontando con la (1):

$$\mathcal Z[\Phi(t)]=\Phi(z)=z(zI-A)^{-1}$$

> [!important] Differenza con Laplace
> Nel continuo $\Phi(s)=(sI-A)^{-1}$; nel discreto c'è un fattore $z$ in più: $\Phi(z)=z(zI-A)^{-1}$. Viene dalla traslazione $\mathcal Z[f(t+1)]=zF(z)-zf(0)$, dove anche la condizione iniziale è moltiplicata per $z$. Per questo $\Phi(z)$ è razionale **propria** ma non strettamente propria.

> [!note] Annotazioni di Simone
> A mano: "Per il calcolo di $x(t+1)$", "per $f(t+1)$:", "$\tau=t+1$", "da (3) e (4)", **"$\mathcal Z[H(t)]$ lo vedi sotto"** e, accanto a $\Phi(z)$, "caso tempo discreto".

### Traslazione all'indietro e $H(z)$

Ricordando che $\Phi(t)=A^t$ e $H(t)=A^{t-1}B$, bisogna calcolare $\mathcal Z[A^{t-1}]$ e non $\mathcal Z[A^t]$. Analogamente a $f(t+1)$, con $\tau=t-1$:

$$\mathcal Z[f(t-1)]=\sum_{t=0}^{\infty}f(t-1)z^{-t}=\sum_{\tau=-1}^{\infty}f(\tau)z^{-\tau-1}=z^{-1}\sum_{\tau=-1}^{\infty}f(\tau)z^{-\tau}=z^{-1}\mathcal Z[f(t)]$$

La sommatoria dopo il cambio di variabile parte da $\tau=-1$ ma, come sempre, le funzioni si considerano moltiplicate per $\delta_{-1}(t)$: prima di 0 è tutto nullo. Allora

$$\mathcal Z[H(t)]=\mathcal Z[A^{t-1}B]=z^{-1}\mathcal Z[A^t]B=z^{-1}\Phi(z)B=z^{-1}z(zI-A)^{-1}B=(zI-A)^{-1}B$$

Per **anticipare** una funzione di 1 passo la si moltiplica per $z$ (togliendo la condizione iniziale), per **ritardarla** di 1 basta moltiplicarla per $z^{-1}$. La prossima volta si vedrà come anticipare o ritardare di un numero generico $T$ di passi.

> [!note] Annotazioni di Simone
> A mano: **"Calcolo di $\mathcal Z[H(t)]$"**, **"Per $f(t-1)$: per $H(t)$"** e **"Come anticipare/ritardare una funzione"**; in $z^{-1}z(zI-A)^{-1}$ ha barrato $z^{-1}$ e $z$, che si semplificano.

> [!quote] Dal libro — teoremi di traslazione e funzione di trasferimento
> Il libro chiama **teorema della traslazione a sinistra** $\mathcal Z[f(t+1)]=zF(z)-zf(0)$ ("nel contesto discreto, svolge il ruolo del teorema della derivata in Laplace") e scrive la traslazione all'indietro come $\mathcal Z[f(t-1)]=\frac{F(z)}{z}$. Ne seguono
> $$\Phi(z)=(zI-A)^{-1}z,\quad\Psi(z)=C(zI-A)^{-1}z,\quad H(z)=(zI-A)^{-1}B,\quad W(z)=C(zI-A)^{-1}B+D$$
> e, come nel continuo, il **teorema della convoluzione**: $\mathcal Z\big[\sum_{\tau=0}^{t-1}H(t-\tau)u(\tau)\big]=H(z)U(z)$ e $\mathcal Z\big[\sum_{\tau=0}^{t}W(t-\tau)u(\tau)\big]=W(z)U(z)$. Anche $W(z)$ si chiama **funzione di trasferimento**. _(libro, §4.6.1, pp. 203–205)_

> [!warning] Correzione
> Nel libro (p. 205) la proprietà $\mathcal Z[f(t-1)]=\frac{F(z)}{z}$ è chiamata di nuovo "teorema della traslazione a **sinistra**", come quella per $f(t+1)$: un ritardo è una traslazione a **destra**.
