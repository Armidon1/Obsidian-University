---
title: Antitrasformata Zeta
aliases:
  - TDS — Antitrasformata Zeta
tags:
  - teoria-dei-sistemi
  - trasformata-zeta
  - antitrasformata
  - residui
  - tempo-discreto
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 99–105); libro Monaco et al., §4.6.1–4.6.2
---

# Antitrasformata Zeta

> [!abstract] Scopo della lezione
> Si completa la [[18 - TDS - Trasformata Zeta|trasformata Zeta]] con gli strumenti pratici:
> 1. le **trasformate Z** delle funzioni che compaiono nei modi naturali discreti (impulso, gradino, $a^t$, seno, coseno, $\rho^t\sin\theta t$), raccolte in una tabella;
> 2. l'**antitrasformazione**: le trasformate Z sono razionali **proprie**, quindi prima di scomporre in fratti semplici si divide per $z$ (o si moltiplica per $z$ e si ottiene la funzione **anticipata**);
> 3. come antitrasformare evoluzioni libere e forzate: residui di $\Phi(z)$ e le $u_iv_i'$, come nel continuo ([[16 - TDS - Antitrasformate e residui]]);
> 4. un esempio con una coppia di poli complessi coniugati.
>
> Segue [[20 - TDS - Risposta forzata nel tempo discreto]]. Indice: [[MOC - Teoria dei Sistemi]].

## Trasformate Z di funzioni comuni

Vedi [[TDS - Trasformata Zeta]].

I sistemi a tempo discreto si rappresentano in modi diversi:

$$\underbrace{\begin{cases}x(t+1)=Ax(t)+Bu(t)\\y(t)=Cx(t)+Du(t)\end{cases}}_{\text{implicita}}\iff\underbrace{\begin{cases}x(t)=\Phi(t)x_0+\sum_{\tau=0}^{t-1}H(t-\tau)u(\tau)\\y(t)=\Psi(t)x_0+\sum_{\tau=0}^{t-1}W(t-\tau)u(\tau)\end{cases}}_{\text{esplicita}}\ \stackrel{\mathcal Z}{\Longrightarrow}\ \begin{cases}X(z)=(zI-A)^{-1}zx_0+(zI-A)^{-1}BU(z)\\Y(z)=C(zI-A)^{-1}zx_0+C(zI-A)^{-1}BU(z)\end{cases}$$

(vista la scorsa lezione; $Y(z)$ si ottiene subito da $X(z)$). In particolare

$$\mathcal Z[W(t)]=\begin{cases}\mathcal Z[CA^{t-1}B]&t\ge1\\\mathcal Z[D]&t=0\end{cases}=\begin{cases}C(zI-A)^{-1}B&t\ge1\\D&t=0\end{cases}$$

> [!note] Precisazione
> La scrittura "a casi" va intesa così: il contributo per $t\ge1$ ha trasformata $C(zI-A)^{-1}B$, quello in $t=0$ (il valore $D$ nell'istante iniziale) ha trasformata $D$; quindi, sommando, $W(z)=C(zI-A)^{-1}B+D$. Nella formula di $y(t)$ sopra il termine $Du(t)$ va incluso estendendo la somma fino a $\tau=t$, come in [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Sistemi a tempo discreto|lezione 9]].

Come per Laplace, si calcolano le trasformate delle funzioni che compaiono nei modi naturali, per poi antitrasformare.

**Impulso.** $\delta(t)$ vale 1 in $t=0$ e 0 altrove:

$$\mathcal Z[\delta(t)]=\sum_{t=0}^{\infty}\delta(t)z^{-t}=z^0=1$$

**Gradino** (funzione costante):

$$\mathcal Z[\delta_{-1}(t)]=\sum_{t=0}^{\infty}z^{-t}=\sum_{t=0}^{\infty}\left(\frac1z\right)^t=\frac1{1-\frac1z}=\frac{z}{z-1}$$

È una **serie geometrica** ([[Serie geometrica]]), che converge a quel valore solo se $\left|\frac1z\right|<1$, cioè $|z|>1$.

**Potenze $a^t$** (la forma $\lambda^t$ dei modi):

$$\mathcal Z[a^t]=\sum_{t=0}^{\infty}a^tz^{-t}=\sum_{t=0}^{\infty}\left(\frac az\right)^t=\frac1{1-\frac az}=\frac{z}{z-a}\qquad(|z|>|a|)$$

**Seno e coseno.** $e^{j\theta t}=(e^{j\theta})^t$, quindi si usa la trasformata di $a^t$ con $a=e^{j\theta}$:

$$\mathcal Z[\sin\theta t]=\frac{\mathcal Z[e^{j\theta t}]-\mathcal Z[e^{-j\theta t}]}{2j}=\frac{1}{2j}\left(\frac{z}{z-e^{j\theta}}-\frac{z}{z-e^{-j\theta}}\right)=\frac{e^{j\theta}-e^{-j\theta}}{2j}\cdot\frac{z}{z^2-(e^{j\theta}+e^{-j\theta})z+1}=\frac{z\sin\theta}{z^2-2z\cos\theta+1}$$

$$\mathcal Z[\cos\theta t]=\frac{1}{2}\left(\frac{z}{z-e^{j\theta}}+\frac{z}{z-e^{-j\theta}}\right)=\frac z2\cdot\frac{2z-e^{-j\theta}-e^{j\theta}}{(z-e^{j\theta})(z-e^{-j\theta})}=\frac{z^2-z\cos\theta}{z^2-2z\cos\theta+1}$$

**Modi pseudoperiodici.** Nei modi naturali compaiono esponenziali moltiplicati per termini trigonometrici. Per una generica $a^tf(t)$:

$$\mathcal Z[a^tf(t)]=\sum_{t=0}^{\infty}a^tf(t)z^{-t}=\sum_{t=0}^{\infty}f(t)\left(\frac za\right)^{-t}=F\!\left(\frac za\right)$$

perché se $\sum f(t)z^{-t}=F(z)$ allora $\sum f(t)\left(\frac za\right)^{-t}=F\!\left(\frac za\right)$. È l'analogo discreto della traslazione complessa di Laplace. Per il modo pseudoperiodico (la parte con il seno; il coseno è analogo):

$$\mathcal Z[\rho^t\sin\theta t]=\frac{\frac z\rho\sin\theta}{\left(\frac z\rho\right)^2-2\frac z\rho\cos\theta+1}=\frac{\rho z\sin\theta}{z^2-2\rho z\cos\theta+\rho^2}$$

> [!note] Annotazioni di Simone
> A mano: "δ(t) IMPULSO", "δ₋₁(t) GRADINO", "Serie geometrica converge a quel valore se", "Proprietà" (accanto a $\mathcal Z[a^tf(t)]$), "solo una parte del modo pseudoperiodico" e "modulo" (sotto $\rho^t$).

| $f(t)$ | $F(z)$ | Condizioni |
|---|---|---|
| $\delta(t)$ | $1$ | |
| $\delta_{-1}(t)$ | $\dfrac{z}{z-1}$ | $|z|>1$ |
| $a^t$ | $\dfrac{z}{z-a}$ | $|z|>|a|$ |
| $\sin\theta t$ | $\dfrac{z\sin\theta}{z^2-2z\cos\theta+1}$ | $|z|>1$ |
| $\cos\theta t$ | $\dfrac{z^2-z\cos\theta}{z^2-2z\cos\theta+1}$ | $|z|>1$ |
| $\rho^t\sin\theta t$ | $\dfrac{\frac z\rho\sin\theta}{\left(\frac z\rho\right)^2-2\frac z\rho\cos\theta+1}$ | $|z|>|\rho|$ |

> [!note] Annotazione di Simone
> Accanto alla tabella, a mano in rosso: **"Tabella Trasformate Z"**.

> [!warning] Precisazione
> Nella tabella degli appunti la riga di $\rho^t\sin\theta t$ riporta le condizioni "$|z|>1$, $|z|>|\rho|$": la condizione è solo $|z|>|\rho|$ (si ottiene da quella del seno, $|z/\rho|>1$).

> [!quote] Dal libro
> Le trasformate dei modi discreti "sono funzioni razionali proprie": $\mathcal Z[\lambda^t]=\frac{z}{z-\lambda}$, $\mathcal Z[\delta_{-1}(t)]=\frac{z}{z-1}$, e per i modi pseudoperiodici
> $$\mathcal Z[|\lambda|^t\sin\theta t]=\frac{z|\lambda|\sin\theta}{z^2-2z|\lambda|\cos\theta+|\lambda|^2},\qquad\mathcal Z[|\lambda|^t\cos\theta t]=\frac{z^2-z|\lambda|\cos\theta}{z^2-2z|\lambda|\cos\theta+|\lambda|^2}$$
> Per gli ingressi polinomiali nel discreto il libro usa i **polinomi fattoriali** $\frac{t^{[k]}}{k!}=\frac{t(t-1)\cdots(t-k+1)}{k!}$, con $\mathcal Z\big[\frac{t^{[k]}}{k!}\big]=\frac{z}{(z-1)^{k+1}}$ (per esempio $\mathcal Z[t]=\frac{z}{(z-1)^2}$), grazie alla proprietà $\mathcal Z[tf(t)]=-z\frac{d}{dz}F(z)$. _(libro, §4.6.1, pp. 206–208)_

## Antitrasformazione

Vedi [[TDS - Antitrasformata e residui]].

> [!note] Annotazione di Simone
> Accanto al titolo: **"Per Trasformate Z"**.

A differenza del continuo, le trasformate Z ottenute sono funzioni razionali **proprie, non strettamente**: possono essere strettamente proprie (come il seno), ma in generale non lo sono. Per esempio

$$\Phi(z)=z(zI-A)^{-1}=z\,\frac{\mathrm{adj}(zI-A)}{p(z)}$$

con $p(z)$ polinomio caratteristico. L'aggiunta trasposta divisa per $p(z)$ dà funzioni strettamente proprie, ma moltiplicando per $z$ possono comparire funzioni proprie non strettamente. Quindi antitrasformare è più complicato che in $s$: per esempio non si può scomporre **direttamente** in fratti semplici (con il numeratore dello stesso grado del denominatore, il fratto $\frac{1}{z-z_1}$ dovrebbe avere al numeratore un polinomio $az+b$, cosa che con le funzioni strettamente proprie non accadeva).

Però tutte le trasformate hanno sempre $z$ al numeratore: la $F(z)$ da antitrasformare è del tipo $z\tilde F(z)$. Si prende allora $\tilde F(z)=\frac{F(z)}{z}$, che è **strettamente propria**, e la si scompone:

$$\tilde F(z)=\frac{R_1}{z-z_1}+\frac{R_2}{z-z_2}+\dots+\frac{R_n}{z-z_n}$$

con $z_1,\dots,z_n$ radici del denominatore. I residui si calcolano con il teorema dei residui come nel continuo (si moltiplica $\tilde F$ per $(z-z_i)$ e si fa il limite per $z\to z_i$). Poi

$$F(z)=z\tilde F(z)=\frac{z}{z-z_1}R_1+\frac{z}{z-z_2}R_2+\dots+\frac{z}{z-z_n}R_n$$

e, dalla tabella,

$$f(t)=\mathcal Z^{-1}[F(z)]=\mathcal Z^{-1}\left[\frac{z}{z-z_1}\right]R_1+\dots+\mathcal Z^{-1}\left[\frac{z}{z-z_n}\right]R_n=R_1z_1^t+R_2z_2^t+\dots+R_nz_n^t$$

**Seconda strada.** Ricordando che

$$\mathcal Z[f(t-1)]=z^{-1}F(z),\qquad\mathcal Z[f(t+1)]=zF(z)-zf(0)$$

se $\mathcal Z^{-1}[\tilde F(z)]=\tilde f(t)$, allora $\mathcal Z^{-1}[z\tilde F(z)]=\tilde f(t+1)$ (moltiplicare per $z$ **anticipa** la funzione). Sono due modi equivalenti di antitrasformare.

> [!note] Annotazione di Simone
> Sotto: **"procedimento importante per casi particolari"**.

> [!warning] Precisazione
> $\mathcal Z^{-1}[z\tilde F(z)]=\tilde f(t+1)$ vale esattamente quando $\tilde f(0)=0$, cioè quando $\tilde F$ è **strettamente** propria (per il teorema del valore iniziale, $\tilde f(0)=\lim_{z\to\infty}\tilde F(z)$): altrimenti mancherebbe il termine $-z\tilde f(0)$. È proprio il caso in cui si usa.

### Due esempi

**Funzione non strettamente propria.**

$$F(z)=\frac{z^2}{(z-1)(z+1)}\qquad\Longrightarrow\qquad\tilde F(z)=\frac1zF(z)=\frac{z}{(z-1)(z+1)}=\frac{R_1}{z-1}+\frac{R_2}{z+1}$$

con $R_1=\frac{1}{2}$, $R_2=\frac{-1}{-2}=\frac12$. Allora

$$F(z)=z\tilde F(z)=\frac12\cdot\frac{z}{z-1}+\frac12\cdot\frac{z}{z+1}\ \Longrightarrow\ \mathcal Z^{-1}[F(z)]=\frac12\cdot1^t+\frac12(-1)^t$$

(vale 1 per $t$ pari e 0 per $t$ dispari).

**Funzione strettamente propria.**

$$F(z)=\frac{z}{(z-1)(z+1)}=\frac12\cdot\frac1{z-1}+\frac12\cdot\frac1{z+1}$$

Ma $\frac1{z-1}$ e $\frac1{z+1}$ non si sanno antitrasformare (in tabella c'è sempre $z$ al numeratore). Si moltiplica $F(z)$ per $z$ e si antitrasforma:

$$zF(z)=\frac12\cdot\frac{z}{z-1}+\frac12\cdot\frac{z}{z+1}\ \Longrightarrow\ \mathcal Z^{-1}[zF(z)]=f(t+1)=\frac12\cdot1^t+\frac12(-1)^t$$

Avendo moltiplicato per $z$, si è trovata la funzione **anticipata** $f(t+1)$, non $f(t)$; ma da $f(t+1)$ si passa subito a $f(t)$:

$$f(t)=\frac12\cdot1^{t-1}+\frac12(-1)^{t-1}$$

(per $t\ge1$; e $f(0)=0$, coerente con $F$ strettamente propria). Vale 0 per $t$ pari e 1 per $t$ dispari: è il segnale del primo esempio ritardato di un passo, infatti $F_2(z)=z^{-1}F_1(z)$.

> [!note] Annotazioni di Simone
> A mano: "Esempio NON strettamente proprio", "procedimento visto sopra", "Esempio strettamente proprio", "Caso particolare", **"ANTICIPATA se moltiplichi per z, RITARDATA se moltiplichi per 1/z"** e "Importante osservazione".

## Antitrasformare evoluzioni forzate e libere

Per l'**evoluzione forzata** (o la risposta forzata) si scrivono le trasformate di $H$ (o $W$), si calcola la trasformata di $u(t)$ e

$$X_F(z)=H(z)U(z)\ \Longrightarrow\ x_F(t)=\mathcal Z^{-1}[X_F(z)],\qquad Y_F(z)=W(z)U(z)\ \Longrightarrow\ y_F(t)=\mathcal Z^{-1}[Y_F(z)]$$

Per le **evoluzioni libere** la relazione continuo-discreto è più "diretta":

$$\Phi(z)=(zI-A)^{-1}z=\mathcal Z[\Phi(t)]=\mathcal Z[A^t]$$

Se $A$ è regolare, $\Phi(z)=z\frac{\mathrm{adj}(zI-A)}{p(z)}$, e il modo comune è dividere per $z$, scomporre in fratti semplici e rimoltiplicare per $z$. Il resto è del tutto analogo al continuo: se $A^t=\lambda_1^tu_1v_1'+\lambda_2^tu_2v_2'+\dots$, allora

$$\Phi(z)=\frac{z}{z-\lambda_1}R_1+\frac{z}{z-\lambda_2}R_2+\dots\quad\Longrightarrow\quad\mathcal Z^{-1}[\Phi(z)]=A^t=\lambda_1^tR_1+\lambda_2^tR_2+\dots$$

e quindi $R_1=u_1v_1'$, $R_2=u_2v_2'$, …, $R_n=u_nv_n'$, proprio come nel continuo: il residuo $R_i$ ha rango pari alla molteplicità dell'autovalore $\lambda_i$.

> [!note] Annotazioni di Simone
> A mano: "Se A regolare" e, a margine, **"ANALOGIA caso tempo CONTINUO"**.

> [!quote] Dal libro — la matrice di transizione in $z$
> "$\Phi(z)$ è una matrice $n\times n$ i cui coefficienti sono funzioni razionali proprie. Per tale ragione non è possibile applicare direttamente lo sviluppo in frazioni parziali […] Per poter quindi calcolare la $\Phi(t)$ a partire dalla $\Phi(z)$, si può considerare l'espansione in frazioni parziali della $\frac{\Phi(z)}{z}=(zI-A)^{-1}=\frac{E(z)}{m(z)}$." Il libro sottolinea anche che "l'operazione di antitrasformazione è particolarmente semplice in presenza di ingressi che ammettono trasformate razionali". _(libro, §4.6.1–4.6.2, p. 208)_

## Antitrasformazione di funzioni trigonometriche

Calcolo di una risposta forzata, con

$$W(t)=2^t\sin3t,\qquad u(t)=\delta_{-1}(t)$$

Dalla tabella, con $\rho=2$ e $\theta=3$:

$$W(z)=\mathcal Z[2^t\sin3t]=\frac{\frac z2\sin3}{\left(\frac z2\right)^2-2\frac z2\cos3+1}=\frac{2z\sin3}{z^2-4z\cos3+4},\qquad U(z)=\mathcal Z[\delta_{-1}(t)]=\frac{z}{z-1}$$

$$Y_F(z)=W(z)U(z)=\frac{2z\sin3}{z^2-4z\cos3+4}\cdot\frac{z}{z-1}$$

La funzione è strettamente propria e si scompone in fratti semplici: c'è una radice reale ($z-1$) e una coppia complessa coniugata da $z^2-4z\cos3+4$, della forma $z_{1,2}=\alpha\pm j\omega=\rho e^{\pm j\theta}$ (qui $\rho=2$, $\theta=3$):

$$Y_F(z)=\frac{R_1}{z-1}+\frac{R_2}{z-\rho e^{j\theta}}+\frac{R_2^*}{z-\rho e^{-j\theta}}$$

I residui si calcolano come nel continuo. Queste funzioni però non si antitrasformano così: si moltiplica per $z$ (si **anticipa** la funzione) e si antitrasforma, ottenendo $y_F(t+1)$:

$$zY_F(z)=\frac{zR_1}{z-1}+\frac{zR_2}{z-\rho e^{j\theta}}+\frac{zR_2^*}{z-\rho e^{-j\theta}}\ \Longrightarrow\ y_F(t+1)=\mathcal Z^{-1}[zY_F(z)]=R_1\,1^t+R_2(\rho e^{j\theta})^t+R_2^*(\rho e^{-j\theta})^t$$

> [!note] Annotazioni di Simone
> A mano: "Calcolo risposta Forzata"; "il calcolo residui come nel caso del tempo continuo e poi…"; **"Soluzione!"**; in rosso: **"Non confonderti con le trasformate a tempo continuo. Non conosciamo trasformate zeta in questa forma!!"** e **"l'antitrasformata di $zy_F(z)$ ha proprio la forma $y_F(t+1)$, da qui è facile procedere da $y_F(t+1)\to y_F(t)$"**.

Per evitare errori conviene esplicitare ciò che finora era sottinteso: tutto è moltiplicato per $\delta_{-1}(t)$:

$$y_F(t+1)=\big(R_1+R_2\rho^te^{j\theta t}+R_2^*\rho^te^{-j\theta t}\big)\,\delta_{-1}(t)$$

e quindi

$$y_F(t)=\big(R_1+R_2\rho^{t-1}e^{j\theta(t-1)}+R_2^*\rho^{t-1}e^{-j\theta(t-1)}\big)\,\delta_{-1}(t-1)$$

Finora $\delta_{-1}$ era sottinteso perché per $t\ge0$ vale 1; ma $\delta_{-1}(t-1)$ vale **0** in $t=0$, quindi qui va scritto. Ottenuta l'espressione, la si porta nel campo reale per interpretarla: gli esponenziali con $j$ diventano termini trigonometrici con Eulero, $e^{j\theta}=\cos\theta+j\sin\theta$ (come in [[16 - TDS - Antitrasformate e residui#Residui complessi|lezione 16]]: $R_2e^{j\theta t}+R_2^*e^{-j\theta t}=2R_a\cos\theta t-2R_b\sin\theta t$, con $R_2=R_a+jR_b$).

> [!note] Annotazioni di Simone
> **"IMPORTANTE!"** accanto a $\delta_{-1}(t)$, e "ora passiamo da t+1 a t".

> [!warning] Correzione
> Negli appunti, nelle due formule con $\delta_{-1}$, gli esponenziali sono scritti $e^{\pm j\omega t}$ e $e^{\pm j\omega(t-1)}$: per coerenza con i poli $\rho e^{\pm j\theta}$ devono essere $e^{\pm j\theta t}$ e $e^{\pm j\theta(t-1)}$ ($\theta$ è la fase del polo, qui $\theta=3$).

### Calcolo alternativo (sconsigliato)

Un altro modo per gestire la coppia coniugata è sommare direttamente nel dominio di $z$ e cercare una trasformata nota in tabella. Con $R_2=R_a+jR_b$:

$$\begin{aligned}zY_F(z)&=\frac{zR_1}{z-1}+\frac{zR_2(z-\rho e^{-j\theta})+zR_2^*(z-\rho e^{j\theta})}{(z-\rho e^{j\theta})(z-\rho e^{-j\theta})}\\&=\frac{zR_1}{z-1}+z\cdot\frac{2R_az-\rho R_a(e^{j\theta}+e^{-j\theta})+j\rho R_b(e^{j\theta}-e^{-j\theta})}{z^2-\rho z(e^{j\theta}+e^{-j\theta})+\rho^2}\\&=\frac{zR_1}{z-1}+\frac{z(2R_az)}{z^2-2\rho z\cos\theta+\rho^2}-\frac{z(2\rho R_a\cos\theta+2\rho R_b\sin\theta)}{z^2-2\rho z\cos\theta+\rho^2}\end{aligned}$$

Il termine centrale ha (quasi) esattamente la forma della trasformata di $\rho^t\sin\theta t$: moltiplicando e dividendo per $\sin\theta$,

$$\frac{z(2R_az)}{z^2-2\rho z\cos\theta+\rho^2}=z\cdot\underbrace{\frac{2R_a}{\rho\sin\theta}}_{r}\cdot\frac{\rho z\sin\theta}{z^2-2\rho z\cos\theta+\rho^2}=z\cdot r\,\mathcal Z[\rho^t\sin\theta t]$$

Con $r=\frac{2R_a}{\rho\sin\theta}$ è proprio la trasformata di $r\rho^t\sin\theta t$, ma con una $z$ di troppo: pensandola come un anticipo, l'antitrasformata è

$$r\rho^{t+1}\sin\big(\theta(t+1)\big)$$

Ricordando che all'inizio si è moltiplicato per $z$ (perché la funzione era strettamente propria):

$$y_F(t+1)=R_1\delta_{-1}(t)+r\rho^{t+1}\sin\big(\theta(t+1)\big)+\dots\quad\Longrightarrow\quad y_F(t)=R_1\delta_{-1}(t-1)+r\rho^t\sin(\theta t)+\dots$$

tralasciando l'ultimo termine (che si tratta in modo analogo). Il pezzo $r\rho^{t+1}\sin(\theta(t+1))$ torna "normale" ($r\rho^t\sin\theta t$) perché la moltiplicazione per $z$ aveva anticipato la funzione.

> [!warning] Precisazione
> Nella conversione finale anche il termine con il seno andrebbe moltiplicato per $\delta_{-1}(t-1)$, come $R_1$: per $t=0$ vale comunque $0$ ($\sin0=0$), quindi il risultato non cambia.

Questo procedimento (i complessi nel dominio di $z$) è spesso più lungo e oneroso: è più semplice l'altro metodo, lasciare i complessi all'esponente e applicare Eulero per ottenere i termini trigonometrici.

> [!note] Annotazione di Simone
> A margine, in viola: **"Calcolo Alternativo SCONSIGLIATO"**.
