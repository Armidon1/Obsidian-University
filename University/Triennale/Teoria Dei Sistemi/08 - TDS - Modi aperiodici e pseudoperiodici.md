---
title: Modi aperiodici e pseudoperiodici
aliases:
  - TDS — Modi aperiodici e pseudoperiodici
tags:
  - teoria-dei-sistemi
  - modi-naturali
  - autovalori-complessi
  - evoluzione-libera
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 21–24); libro Monaco et al., §2.3.1
---

# Modi aperiodici e pseudoperiodici

> [!abstract] Scopo della lezione
> Nella [[07 - TDS - Autovalori complessi coniugati|lezione precedente]] abbiamo calcolato $e^{At}$ con una coppia di autovalori complessi $\alpha\pm j\omega$. Qui si usa quel risultato per scrivere l'**evoluzione libera**, e si scopre un nuovo tipo di modo naturale, **pseudoperiodico** (oscillante con inviluppo esponenziale), accanto a quello **aperiodico** (esponenziale) già visto in [[06 - TDS - Modi naturali]]. Poi:
> - si disegna l'andamento del moto pseudoperiodico al variare di $\alpha$ (spirali ed ellissi);
> - si scrive la formula generale dell'evoluzione libera nel caso regolare;
> - si rivedono osservabilità ed eccitabilità nel caso complesso.
>
> Segue [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto]]. Indice: [[MOC - Teoria dei Sistemi]].

## Modi naturali aperiodici e pseudoperiodici

Vedi [[TDS - Modi aperiodici e pseudoperiodici]].

Con una coppia di autovalori complessi coniugati $\lambda=\alpha\pm j\omega$, l'evoluzione libera dello stato è (indicando con $v_a'$, $v_b'$ le righe di $(u_a\ u_b)^{-1}$):

$$\begin{aligned}
x_L(t)&=e^{\alpha t}(u_a\ \ u_b)\begin{pmatrix}\cos\omega t&\sin\omega t\\-\sin\omega t&\cos\omega t\end{pmatrix}\begin{pmatrix}v_a'\\v_b'\end{pmatrix}x_0
=e^{\alpha t}(u_a\ \ u_b)\begin{pmatrix}\cos\omega t&\sin\omega t\\-\sin\omega t&\cos\omega t\end{pmatrix}\begin{pmatrix}c_a\\c_b\end{pmatrix}\\
&=e^{\alpha t}(u_a\ \ u_b)\begin{pmatrix}c_a\cos\omega t+c_b\sin\omega t\\-c_a\sin\omega t+c_b\cos\omega t\end{pmatrix}
=e^{\alpha t}\Big[(c_a\cos\omega t+c_b\sin\omega t)\,u_a+(-c_a\sin\omega t+c_b\cos\omega t)\,u_b\Big]
\end{aligned}$$

dove $c_a=v_a'x_0$ e $c_b=v_b'x_0$ sono le coordinate di $x_0$ nella base reale $(u_a,u_b)$.

Le parentesi contengono somme di seni e coseni, che conviene compattare in un'unica sinusoide. Se fosse $c_a=\sin\varphi$ e $c_b=\cos\varphi$ avremmo subito $\sin\varphi\cos\omega t+\cos\varphi\sin\omega t=\sin(\omega t+\varphi)$; ma questa ipotesi non è giustificata, perché richiederebbe $c_a^2+c_b^2=1$, che in generale non vale. Si **normalizza** dividendo per

$$m=\sqrt{c_a^2+c_b^2}\qquad\text{così che}\qquad\frac{c_a^2}{m^2}+\frac{c_b^2}{m^2}=1,\qquad \frac{c_a}{m}:=\sin\varphi,\quad\frac{c_b}{m}:=\cos\varphi$$

Moltiplicando e dividendo per $m$:

$$\begin{aligned}
x_L(t)&=me^{\alpha t}\Big[\Big(\tfrac{c_a}{m}\cos\omega t+\tfrac{c_b}{m}\sin\omega t\Big)u_a+\Big(-\tfrac{c_a}{m}\sin\omega t+\tfrac{c_b}{m}\cos\omega t\Big)u_b\Big]\\
&=me^{\alpha t}\Big[(\sin\varphi\cos\omega t+\cos\varphi\sin\omega t)\,u_a+(-\sin\varphi\sin\omega t+\cos\varphi\cos\omega t)\,u_b\Big]\\
&=me^{\alpha t}\Big[\sin(\omega t+\varphi)\,u_a+\cos(\omega t+\varphi)\,u_b\Big]
\end{aligned}$$

Questa è l'evoluzione libera con una coppia di autovalori complessi coniugati, e tutta l'espressione è **un solo modo naturale**. Il moto è molto diverso da quello esponenziale, quindi si distinguono:

| Tipo | Autovalori | Espressione | Dove avviene |
|---|---|---|---|
| **aperiodico** | reale $\lambda_i$ | $c_ie^{\lambda_it}u_i$ | sulla retta di $u_i$ |
| **pseudoperiodico** | coppia $\alpha\pm j\omega$ | $me^{\alpha t}\big[\sin(\omega t+\varphi)u_a+\cos(\omega t+\varphi)u_b\big]$ | nel piano di $u_a,u_b$ |

$m$ (ampiezza) e $\varphi$ (fase) dipendono dallo stato iniziale; $\alpha$ e $\omega$ solo dal sistema.

> [!important] Il numero di modi non è la dimensione del sistema
> Un sistema di dimensione $n$ ha $n$ autovalori, ma ogni autovalore **reale** dà un modo naturale, mentre **due** autovalori complessi coniugati ne danno **uno solo**. Conoscendo solo la dimensione non si sa quanti modi naturali ha il sistema: con $r$ autovalori reali e $c$ coppie complesse ($n=r+2c$) i modi sono $r+c$.

## Andamento del moto pseudoperiodico

Per prima cosa il grafico di $m\sin(\omega t+\varphi)$:

![[TDS-L08-01.png]]

A sinistra, con $\varphi=0$, si vede l'effetto di $m$: cambia l'**ampiezza**, non la frequenza (le tre sinusoidi passano per zero negli stessi punti). A destra, al variare di $\varphi$, la sinusoide trasla lungo l'asse dei tempi: cambia la **fase**.

La sinusoide che moltiplica $u_a$ però non ha ampiezza fissa $m$, ma $me^{\alpha t}$, che varia nel tempo. L'andamento è quindi **divergente** se $\alpha>0$, **convergente** se $\alpha<0$, **costante** se $\alpha=0$:

![[TDS-L08-02.png]]

Le curve tratteggiate $\pm me^{\alpha t}$ sono l'**inviluppo** dell'oscillazione: a sinistra ($\alpha>0$) si allargano e l'oscillazione esplode, a destra ($\alpha<0$) si stringono e l'oscillazione si smorza verso zero. Solo con $\alpha=0$ si ha un moto sinusoidale puro. La componente lungo $u_b$ è la stessa curva con il coseno, cioè sfasata di $\pi/2$.

Disegnando il moto nel piano di $u_1$ e $u_2$ (cioè $u_a$ e $u_b$), con $\alpha<0$ si ottiene una **spirale** che si stringe esponenzialmente verso l'origine:

![[TDS-L08-03.png]]

Con $\alpha>0$ la spirale si **allarga** esponenzialmente; con $\alpha=0$ il moto è un'**ellisse** (chiusa: lo stato torna periodicamente nello stesso punto):

![[TDS-L08-04.png]]

Gli assi dell'ellisse sono legati ai vettori $u_a$, $u_b$, che in generale non sono ortogonali né di uguale lunghezza: per questo la traiettoria è un'ellisse e non una circonferenza.

> [!quote] Dal libro
> "Si tratta dei **modi naturali pseudoperiodici**. Sono evoluzioni che avvengono in un piano, quello degli autovettori $(u_{ka},u_{kb})$, con una legge di moto temporale che ammette un inviluppo esponenziale, $e^{\alpha t}$, ma con componenti periodiche seno e coseno, lungo due direzioni del piano del moto." Per $\alpha>0$ la traiettoria è una spirale divergente, per $\alpha=0$ un'ellisse, per $\alpha<0$ una spirale convergente; la **pulsazione** della legge temporale è $\omega$, la parte immaginaria dell'autovalore (Figura 2.4 del libro). _(libro, §2.3.1, pp. 58–59)_

## Evoluzione libera generale

Vedi [[TDS - Evoluzione libera e forzata]].

Mettendo insieme tutti i casi regolari (autovalori reali e complessi, $A$ diagonalizzabile), l'evoluzione libera è la somma di tutti i modi naturali, aperiodici e pseudoperiodici:

$$x_L(t)=\sum_{i=1}^{r}c_ie^{\lambda_it}u_i+\sum_{i=1}^{c}m_ie^{\alpha_it}\big(\sin(\omega_it+\varphi_i)\,u_{ia}+\cos(\omega_it+\varphi_i)\,u_{ib}\big)$$

La prima somma scorre gli $r$ autovalori reali, la seconda le $c$ **coppie** di autovalori complessi (quindi $2c$ autovalori): in tutto $n=r+2c$.

> [!example] Un moto in $\mathbb R^3$
> Un autovalore reale $\lambda_1<0$ con autovettore $u_1$ e una coppia complessa $\lambda,\lambda^*$ con $u=u_a+ju_b$, con $\alpha<0$. Da una condizione iniziale $x_0$:
>
> ![[TDS-L08-05.png]]
>
> La traiettoria (rossa) è la composizione dei due modi: la componente lungo $u_1$ decresce esponenzialmente (il moto scende lungo $u_1$ verso l'origine), mentre la componente nel piano verde di $u_a,u_b$ ruota con raggio che si stringe. Ne risulta un'elica che si avvolge attorno a $u_1$ e si chiude verso l'origine. Quale dei due moti si esaurisce prima dipende da quanto sono negativi $\lambda_1$ e $\alpha$.

## Studio di $e^{At}$ e delle varie matrici nel caso complesso

Vedi [[TDS - Eccitabilità e osservabilità dei modi]].

Sviluppando il prodotto, la parte di $\Phi(t)=e^{At}$ relativa a una coppia complessa è

$$e^{At}=e^{\alpha t}(u_a\ \ u_b)\begin{pmatrix}\cos\omega t\,v_a'+\sin\omega t\,v_b'\\-\sin\omega t\,v_a'+\cos\omega t\,v_b'\end{pmatrix}=e^{\alpha t}\Big[\cos\omega t\,u_av_a'+\sin\omega t\,u_av_b'-\sin\omega t\,u_bv_a'+\cos\omega t\,u_bv_b'\Big]$$

Da qui le altre matrici della forma esplicita.

**Evoluzione libera in uscita**, $\Psi(t)=Ce^{At}$:

$$\Psi(t)=e^{\alpha t}\Big[\cos\omega t\,Cu_av_a'+\sin\omega t\,Cu_av_b'-\sin\omega t\,Cu_bv_a'+\cos\omega t\,Cu_bv_b'\Big]$$

Se $Cu_a=0$ **e** $Cu_b=0$ contemporaneamente, il modo non compare in $\Psi(t)$: anche nel caso complesso, se entrambi i prodotti sono nulli il modo è **non osservabile**.

**Risposta impulsiva nello stato**, $H(t)=e^{At}B$:

$$H(t)=e^{\alpha t}\Big[\cos\omega t\,u_av_a'B+\sin\omega t\,u_av_b'B-\sin\omega t\,u_bv_a'B+\cos\omega t\,u_bv_b'B\Big]$$

Il modo è **non eccitabile** se $v_a'B$ e $v_b'B$ sono nulli **contemporaneamente**; basta che uno dei due sia diverso da zero perché sia eccitabile.

**Risposta impulsiva in uscita**, $W(t)=Ce^{At}B$:

$$W(t)=e^{\alpha t}\Big[\cos\omega t\,Cu_av_a'B+\sin\omega t\,Cu_av_b'B-\sin\omega t\,Cu_bv_a'B+\cos\omega t\,Cu_bv_b'B\Big]$$

Ha le caratteristiche di entrambe: non vi compaiono né i modi non osservabili né quelli non eccitabili.

> [!tip] Perché "contemporaneamente"
> Il modo pseudoperiodico vive in un **piano**, non su una retta: è invisibile in uscita solo se $C$ annulla tutto il piano, cioè entrambi i vettori $u_a$ e $u_b$. Se $C$ ne vede anche solo uno, la rotazione porta prima o poi lo stato in una direzione visibile.
