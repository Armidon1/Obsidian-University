---
title: Risposta forzata nel tempo discreto
aliases:
  - TDS — Risposta forzata nel tempo discreto
tags:
  - teoria-dei-sistemi
  - trasformata-zeta
  - risposta-forzata
  - tempo-discreto
  - esempio
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 106–111); libro Monaco et al., §4.5.2, §4.6.1
---

# Risposta forzata nel tempo discreto

> [!abstract] Scopo della lezione
> Si applica l'[[19 - TDS - Antitrasformata Zeta|antitrasformata Zeta]] al calcolo della **risposta forzata** di uno stesso sistema, $W(z)=\frac{z}{z+1}$, con tre ingressi diversi: costante, esponenziale, sinusoidale. In tutti i casi la risposta si divide in una parte che **dipende dal sistema** (i poli di $W$) e una che **dipende dall'ingresso** (i poli di $U$): è l'idea che porterà alla [[21 - TDS - Risposta a regime permanente|risposta a regime permanente]].
> Poi si ragiona in modo intuitivo su $W(z)=z^{-1}$ (un **ritardo**) e su come costruire ingressi complicati come **combinazione di gradini traslati**, sfruttando la linearità.
>
> Indice: [[MOC - Teoria dei Sistemi]].

## Esempio numerico

Vedi [[TDS - Trasformata Zeta]].

Un sistema a tempo discreto con

$$W(z)=\frac{z}{z+1}$$

Studiamo l'uscita forzata con diversi tipi di ingresso.

### Ingresso costante

Con $u(t)=\delta_{-1}(t)$ (ingresso costante), $U(z)=\frac{z}{z-1}$ e

$$y_F(t)=\mathcal Z^{-1}[Y_F(z)]=\mathcal Z^{-1}[W(z)U(z)]=\mathcal Z^{-1}\left[\frac{z}{z+1}\cdot\frac{z}{z-1}\right]=\mathcal Z^{-1}\left[\frac{z^2}{(z+1)(z-1)}\right]$$

La funzione è razionale propria (grado del numeratore = grado del denominatore): si può scomporre in fratti semplici **solo dopo aver diviso per $z$**:

$$\frac1zY_F(z)=\frac{z}{(z+1)(z-1)}=\frac{R_1}{z+1}+\frac{R_2}{z-1}$$

$$R_1=\lim_{z\to-1}\frac{z}{z-1}=\frac12,\qquad R_2=\lim_{z\to1}\frac{z}{z+1}=\frac12$$

Si rimoltiplica per $z$ e si antitrasforma:

$$y_F(t)=\mathcal Z^{-1}\left[\frac12\cdot\frac{z}{z+1}+\frac12\cdot\frac{z}{z-1}\right]=\frac12(-1)^t+\frac12$$

Per ricordare che vale per $t\ge0$ si può scrivere $y_F(t)=\left(\frac12(-1)^t+\frac12\right)\delta_{-1}(t)$, ma lo si può omettere se è chiaro.

> [!note] Annotazioni di Simone
> A mano: "$u(t)=\delta_{-1}(t)$ ingresso COSTANTE", "GRADO NUM = GRADO DEN → divido per z".

Nella risposta ci sono due termini:
- $\frac12(-1)^t$ nasce **dal sistema**: viene dal fattore $(z+1)$ che stava in $W(z)$;
- $\frac12$ viene **dall'ingresso**: dal fattore $(z-1)$ che stava in $U(z)$, quindi non è intrinseco al sistema.

In generale nella risposta forzata si distinguono una parte che dipende dal sistema e una che dipende dall'ingresso. Qui l'ingresso era una costante, e la parte relativa a $U(z)$ è anch'essa una costante: $\frac12$.

> [!note] Annotazione di Simone
> A margine: **"Modo di analizzare il sistema e l'ingresso"**.

> [!tip] Interpretazione
> Il sistema ha un polo in $-1$: un modo **alternante** di modulo 1, né convergente né divergente. Per questo la parte "del sistema" $\frac12(-1)^t$ non si spegne: l'uscita oscilla per sempre tra $1$ e $0$. Se il polo fosse dentro il cerchio unitario, quella parte andrebbe a zero e resterebbe solo la parte dovuta all'ingresso.

### Ingresso esponenziale

Con $u(t)=2^t$ (ingresso che varia nel tempo), $U(z)=\frac{z}{z-2}$:

$$Y_F(z)=\frac{z^2}{(z+1)(z-2)}\ \Longrightarrow\ \frac1zY_F(z)=\frac{z}{(z+1)(z-2)}=\frac{R_1}{z+1}+\frac{R_2}{z-2}$$

con $R_1=\frac{-1}{-3}=\frac13$ e $R_2=\frac23$. Rimoltiplicando per $z$:

$$y_F(t)=\mathcal Z^{-1}\left[\frac13\cdot\frac{z}{z+1}+\frac23\cdot\frac{z}{z-2}\right]=\frac13(-1)^t+\frac23\,2^t$$

Anche stavolta c'è una parte che dipende dal sistema, $\frac13(-1)^t$, e una che dipende dall'ingresso, $\frac23 2^t$. In particolare l'ingresso era $2^t$ e la parte dovuta all'ingresso **rimane $2^t$** (a meno del coefficiente).

> [!note] Annotazioni di Simone
> A mano: "Ingresso che varia nel tempo", "Stesso procedimento", "$u(t)=2^t$".

### Ingresso sinusoidale

Con $u(t)=\sin2t$ (ingresso trigonometrico):

$$U(z)=\frac{z\sin2}{z^2-2z\cos2+1}$$

I termini trigonometrici che compaiono sono semplicemente costanti: $\sin2\approx0{,}909$ e $\cos2\approx-0{,}416$. Si ha

$$Y_F(z)=\frac{z^2\sin2}{(z+1)(z^2-2z\cos2+1)}$$

che è **strettamente propria**, quindi non serve dividere per $z$ e si scompone direttamente. Le radici di $z^2-2z\cos2+1$ sono

$$z_{1,2}=\frac{2\cos2\pm\sqrt{4\cos^2 2-4}}{2}=\cos2\pm\sqrt{\cos^22-1}=\cos2\pm\sqrt{-\sin^22}=\cos2\pm j\sin2=e^{\pm2j}$$

complesse coniugate. Si continua con la forma esponenziale $e^{\pm2j}$ invece di quella trigonometrica ($\cos2\pm j\sin2$) solo perché è più compatta: sono equivalenti (il professore, questa volta, ha usato quella trigonometrica).

$$Y_F(z)=\frac{R_1}{z+1}+\frac{R_2}{z-e^{2j}}+\frac{R_2^*}{z-e^{-2j}}$$

> [!note] Annotazioni di Simone
> A mano: "Ingresso TRIGONOMETRICO", "Stesso procedimento ma è strettamente propria", "Sono complessi coniugati".

**Residui.**

$$R_1=\lim_{z\to-1}\frac{z^2\sin2}{z^2-2z\cos2+1}=\frac{\sin2}{1+2\cos2+1}=\frac{\sin2}{2(1+\cos2)}$$

$$\begin{aligned}R_2&=\lim_{z\to e^{2j}}(z-e^{2j})\frac{z^2\sin2}{(z+1)(z-e^{2j})(z-e^{-2j})}=\frac{e^{4j}\sin2}{(e^{2j}+1)(e^{2j}-e^{-2j})}\\&=\frac{e^{4j}\sin2}{2j(e^{2j}+1)\frac{e^{2j}-e^{-2j}}{2j}}=\frac{e^{4j}\sin2}{2j(e^{2j}+1)\sin2}=-\frac{je^{4j}}{2(e^{2j}+1)}\end{aligned}$$

$R_1$ è un residuo reale, $R_2$ complesso. Razionalizzato, $R_2$ avrà parte reale $R_a$ e parte immaginaria $R_b$ (qui non le calcoliamo):

$$Y_F(z)=\frac{R_1}{z+1}+\frac{R_a+jR_b}{z-e^{2j}}+\frac{R_a-jR_b}{z-e^{-2j}}$$

> [!note] Annotazioni di Simone
> A mano: "Residuo Reale", "Residuo Complesso", "coniugato", "Ra e Rb li ricavo da R₂", "Non sappiamo anti-trasformare", "calcolo alternativo".

Queste quantità non si antitrasformano così, quindi si moltiplica per $z$, ricordando che si sta calcolando l'antitrasformata della funzione **anticipata**, $y_F(t+1)$:

$$zY_F(z)=\frac{z}{z+1}R_1+\frac{z}{z-e^{2j}}(R_a+jR_b)+\frac{z}{z-e^{-2j}}(R_a-jR_b)$$

> [!note] Annotazioni di Simone
> A mano: "$y(t+1)$ ora", **"Mai dimenticarlo!!"** accanto a "stiamo calcolando $y_F(t+1)$", "Termini Complessi".

> [!tip] Si può moltiplicare un termine alla volta
> Moltiplicare per $z$ si può fare anche per un **singolo termine**, non per forza per tutta la funzione: se servisse una $z$ al numeratore solo per il termine di $R_1$, si potrebbe moltiplicare per $z$ solo $R_1$, antitrasformare e poi ritardare solo quel termine.

> [!note] Annotazione di Simone
> A margine: **"Importante osservazione"**.

Per i termini complessi ci sono **due modi**: antitrasformarli direttamente lasciando l'esponenziale immaginario $e^{\pm2j}$, oppure fare prima la somma dei due termini e ricondurla a una forma simile alla trasformata del seno o del coseno (come visto in [[19 - TDS - Antitrasformata Zeta#Calcolo alternativo (sconsigliato)|lezione 19]]). Il primo è in genere più veloce:

$$\begin{aligned}y_F(t+1)&=R_1(-1)^t+(R_a+jR_b)e^{2jt}+(R_a-jR_b)e^{-2jt}\\&=R_1(-1)^t+R_a(e^{2jt}+e^{-2jt})+jR_b(e^{2jt}-e^{-2jt})\\&=R_1(-1)^t+2R_a\cos2t-2R_b\sin2t\end{aligned}$$

$$\Longrightarrow\ y_F(t)=R_1(-1)^{t-1}+2R_a\cos\big(2(t-1)\big)-2R_b\sin\big(2(t-1)\big)=\underbrace{R_1(-1)^{t-1}}_{\text{sistema}}+\underbrace{2R_a\cos(2t-2)-2R_b\sin(2t-2)}_{\text{ingresso}}$$

(per $t\ge1$; $y_F(0)=0$). Come negli esempi precedenti, la parte dipendente dal sistema è $R_1(-1)^{t-1}$, e quella dipendente dall'ingresso è fatta di seno e coseno con la **stessa frequenza dell'ingresso** (2): l'ingresso era un seno e si ottengono termini seno e coseno.

> [!note] Annotazioni di Simone
> A mano: "2 modi possibili per trasformare i termini complessi ⇓ 2° metodo sono quelli sottolineati in rosso", "1° metodo Rimango così ed ottengo una forma Complessa", "2° metodo, applicando Eulero", "SISTEMA", "INGRESSO".

> [!example] Valori numerici (non presenti negli appunti)
> $R_1=\frac{\sin2}{2(1+\cos2)}=\frac12\tan1\approx0{,}779$. Per $R_2$: $e^{2j}+1=e^{j}(e^{j}+e^{-j})=2\cos1\,e^{j}$, quindi
> $$R_2=-\frac{je^{4j}}{4\cos1\,e^{j}}=-\frac{je^{3j}}{4\cos1}=\frac{\sin3-j\cos3}{4\cos1}$$
> cioè $R_a=\frac{\sin3}{4\cos1}\approx0{,}065$, $R_b=-\frac{\cos3}{4\cos1}\approx0{,}458$. Controllo: $y_F(1)=R_1+2R_a=\frac{\sin2}{2(1+\cos2)}+\frac{\sin3}{2\cos1}$. D'altra parte, con $W(z)=\frac{z}{z+1}$ il sistema è $y(t)=-y(t-1)+u(t)$, e con $u(0)=\sin0=0$, $u(1)=\sin2$ si ha $y_F(1)=\sin2\approx0{,}909$; e infatti $0{,}779+0{,}130=0{,}909$ ✔.

> [!warning] Precisazione
> Con $W(z)=\frac{z}{z+1}$ si ha $D=W(\infty)=1\neq0$: l'uscita risponde **istantaneamente** all'ingresso ($y_F(t)=-y_F(t-1)+u(t)$). Per questo nei primi due esempi $y_F(0)=1$ (infatti $\frac12+\frac12=1$ e $\frac13+\frac23=1$), mentre nel terzo $y_F(0)=0$ solo perché $u(0)=\sin0=0$.

## Intuizione e funzioni

Un sistema a tempo discreto con

$$W(z)=\frac1z$$

e l'ingresso del grafico ($u=1$ in $t=0,1$ e $0$ dopo):

![[TDS-L20-01.png]]

Che grafico avrà $y_F(t)$? È immediato: $W(z)=z^{-1}$, e moltiplicare per $z^{-1}$ nel dominio di $z$ significa **ritardare** la funzione, cioè spostarla a destra:

$$y_F(t)=\mathcal Z^{-1}[Y_F(z)]=\mathcal Z^{-1}[U(z)W(z)]=\mathcal Z^{-1}[z^{-1}U(z)]=u(t-1)$$

$y_F(t)$ ha lo stesso grafico di $u(t)$ spostato a destra di 1:

![[TDS-L20-02.png]]

Se $W(z)$ fosse $z$, si avrebbe un **anticipo** dell'ingresso: ma non è possibile, perché non si può sapere "adesso" quello che accadrà al prossimo istante. Si perderebbe la **causalità**, e il sistema non avrebbe più senso fisico.

> [!note] Annotazione di Simone
> A margine: **"Importante osservazione"**.

> [!tip] Causalità e grado relativo
> $W(z)=z$ è impropria (numeratore di grado maggiore del denominatore). Le $W(z)$ dei sistemi in forma $(A,B,C,D)$ sono sempre **proprie**, $W(z)=C(zI-A)^{-1}B+D$: al più rispondono "nello stesso istante" (con $D\neq0$), mai in anticipo. Lo stesso vale nel continuo per $W(s)$.

Nel caso descritto, $W(z)$ è facile e corrisponde a un ritardo. Se non lo fosse (o per verificarlo numericamente), si passa ai numeri, e serve un'espressione analitica di $u(t)$. Nell'esempio

$$u(t)=\begin{cases}1&t\le1\\0&t\ge2\end{cases}$$

> [!note] Annotazioni di Simone
> A mano: "Se $W(t)$ non è facilmente trattabile" e, sotto $u(t)$, $\delta_{-1}(t)-\delta_{-1}(t-2)$.

Bisogna "costruire" analiticamente questa funzione. Un modo è pensarla come una costante a cui si **tolgono** i termini da $t=2$ in poi: un gradino a cui si sottrae un altro gradino spostato in $t=2$.

![[TDS-L20-03.png]]

A sinistra $\delta_{-1}(t)$, a destra $\delta_{-1}(t-2)$ (nullo in $t=0,1$, poi 1). Quindi

$$u(t)=\delta_{-1}(t)-\delta_{-1}(t-2)$$

$$U(z)=\mathcal Z[\delta_{-1}(t)]-\mathcal Z[\delta_{-1}(t-2)]=\mathcal Z[\delta_{-1}(t)]-z^{-2}\mathcal Z[\delta_{-1}(t)]=\frac{z}{z-1}-\frac1{z^2}\cdot\frac{z}{z-1}$$

perché $z^{-1}$ è un ritardo di 1, e per un ritardo di 2 si moltiplica due volte, cioè per $z^{-2}$.

> [!note] Annotazione di Simone
> Accanto a $U(z)$: "Ingresso $u(t)$ trasformato".

In alternativa si usa la definizione:

$$U(z)=\sum_{t=0}^{\infty}u(t)z^{-t}=u(0)+u(1)z^{-1}+u(2)z^{-2}+u(3)z^{-3}+\dots$$

con $u(2),u(3),\dots$ tutti nulli:

![[TDS-L20-04.png]]

$$U(z)=\underbrace{u(0)}_1+\underbrace{u(1)}_1z^{-1}+\underbrace{u(2)z^{-2}+\dots}_{0}=1+\frac1z$$

(ed è la stessa cosa: $\frac{z}{z-1}\big(1-\frac1{z^2}\big)=\frac{z^2-1}{z(z-1)}=\frac{z+1}{z}=1+\frac1z$ ✔). Allora

$$Y_F(z)=U(z)W(z)=\frac1z+\frac1{z^2}\ \Longrightarrow\ y_F(t)=\mathcal Z^{-1}\left[\frac1z+\frac1{z^2}\right]=\mathcal Z^{-1}\left[z^{-1}\cdot1\right]+\mathcal Z^{-1}\left[z^{-2}\cdot1\right]=\delta(t-1)+\delta(t-2)$$

(si ritardano gli impulsi che interessano, ricordando $\mathcal Z[\delta(t)]=1$). È esattamente la funzione trovata graficamente.

> [!note] Annotazioni di Simone
> A mano: "nell'esempio $\frac1z$" sopra $W(z)$, e "Ritardo i fattori che mi servono".

### Sfruttare la linearità

Lo stesso ragionamento da un'altra prospettiva: il sistema e tutte le operazioni sono **lineari**, quindi

$$u(t)=\delta_{-1}(t)-\delta_{-1}(t-2)=u_1(t)+u_2(t),\qquad u_1(t)=\delta_{-1}(t),\quad u_2(t)=-\delta_{-1}(t-2)$$

$$U(z)=\frac{z}{z-1}-\frac{z}{z^2(z-1)}=U_1(z)+U_2(z)\ \Longrightarrow\ Y_F(z)=W(z)U_1(z)+W(z)U_2(z)=Y_{F1}(z)+Y_{F2}(z)$$

Inoltre $U_2(z)=-\frac1{z^2}U_1(z)$, quindi $Y_{F2}(z)=-\frac1{z^2}Y_{F1}(z)$ e

$$y_F(t)=\mathcal Z^{-1}[Y_{F1}(z)-z^{-2}Y_{F1}(z)]=y_{F1}(t)-y_{F1}(t-2)$$

Se si riesce a scrivere l'ingresso come combinazione di funzioni "uguali" (traslate), si risparmiano molti calcoli: basta la risposta a una sola di esse. Lo stesso vale nel tempo continuo.

> [!quote] Dal libro — il teorema della traslazione a destra
> Nel continuo: $\mathcal L[f(t-T)\delta_{-1}(t-T)]=e^{-sT}F(s)$ per $T>0$. "La moltiplicazione per $e^{-sT}$ che moltiplica la trasformata dell'ingresso, resta a fattore di ogni termine nell'espansione della risposta forzata e si traduce in un ritardo nell'antitrasformata." È la conseguenza della **stazionarietà**: la risposta all'ingresso traslato di $T$ è la risposta all'ingresso non traslato, traslata di $T$.
>
> Esempio 4.5.8: $W(s)=\frac1{s+1}$, $u(t)=\delta_{-1}(t-1)$: $Y_f(s)=\big(\frac1s-\frac1{s+1}\big)e^{-s}$, quindi $y_f(t)=(1-e^{-(t-1)})\delta_{-1}(t-1)$, che è proprio la risposta al gradino ritardata. Esempio 4.5.9: un impulso rettangolare $u_1=\delta_{-1}(t)-\delta_{-1}(t-T)$ dà $y_1(t)=w_{-1}(t)-w_{-1}(t-T)$, dove $w_{-1}$ è la **risposta indiciale** (al gradino). _(libro, §4.5.2, pp. 196–197)_

## Esercizio

L'esercizio proposto dal professore, nel tempo continuo: con

$$W(s)=\frac1{s+1}$$

studiare la risposta forzata con i due ingressi del grafico (il secondo si ripete all'infinito):

![[TDS-L20-05.png]]

> [!example]- Traccia di soluzione (la soluzione completa è in [[41 - TDS - Esercizi di riepilogo finale#Esercizio 3: risposta forzata con ingressi non banali|lezione 41]])
> Le risposte di $W(s)=\frac1{s+1}$ al gradino e alla rampa sono
> $$w_{-1}(t)=\mathcal L^{-1}\Big[\tfrac{1}{s(s+1)}\Big]=1-e^{-t},\qquad w_{-2}(t)=\mathcal L^{-1}\Big[\tfrac{1}{s^2(s+1)}\Big]=t-1+e^{-t}$$
> (la seconda è il calcolo di [[16 - TDS - Antitrasformate e residui#Residui con denominatori di grado maggiore di 1|lezione 16]]).
> - **Triangolo** (sale fino a 1 in $t=2$ e torna a 0 in $t=4$): $u(t)=\frac12\big[t\,\delta_{-1}(t)-2(t-2)\delta_{-1}(t-2)+(t-4)\delta_{-1}(t-4)\big]$, quindi
>   $$y_F(t)=\tfrac12\big[w_{-2}(t)-2\,w_{-2}(t-2)\delta_{-1}(t-2)+w_{-2}(t-4)\delta_{-1}(t-4)\big]$$
> - **Onda quadra** (1 in $[0,1)$, 0 in $[1,2)$, …): $u(t)=\sum_{k\ge0}(-1)^k\delta_{-1}(t-k)$, quindi
>   $$y_F(t)=\sum_{k\ge0}(-1)^k\big(1-e^{-(t-k)}\big)\delta_{-1}(t-k)$$
>   dove a ogni istante $t$ contano solo i termini con $k\le t$.
