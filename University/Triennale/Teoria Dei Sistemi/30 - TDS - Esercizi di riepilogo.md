---
title: Esercizi di riepilogo
aliases:
  - TDS — Esercizi di riepilogo
tags:
  - teoria-dei-sistemi
  - esercizi
  - regime-permanente
  - diagrammi-di-bode
  - diagramma-polare
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 181–189); libro Monaco et al., §5.1–5.2
---

# Esercizi di riepilogo

> [!abstract] Scopo della lezione
> Quattro esercizi sul comportamento ingresso-uscita a partire dalla sola $W(s)$:
> **risposta forzata** con i residui ([[16 - TDS - Antitrasformate e residui]]), **regime permanente** ([[21 - TDS - Risposta a regime permanente]], [[22 - TDS - Risposta armonica e forma di Bode]]), **diagrammi di Bode** con binomi e trinomi ([[23 - TDS - Diagrammi di Bode]], [[24 - TDS - Termine trinomio e risonanza]]) e **diagramma polare** ([[25 - TDS - Risposta indiciale e diagramma polare]]). Tre dei quattro sistemi hanno poli sull'asse immaginario: si vede cosa cambia quando il regime permanente non esiste.
>
> Segue [[31 - TDS - Algoritmi di realizzazione e forme canoniche]]. Indice: [[MOC - Teoria dei Sistemi]].

## Primo esempio

Vedi [[TDS - Funzione di trasferimento]].

$$W(s)=\frac{s-1}{(s+1)(s+2)}$$

Si fa l'ipotesi che il sistema sia tutto raggiungibile e tutto osservabile. Così si può dire subito qualcosa sulla stabilità: gli autovalori sono $\lambda_1=-1$ e $\lambda_2=-2$, quindi il sistema è **stabile asintoticamente**. Questo vale almeno con $x_0=0$; in generale bisognerebbe guardare $\Psi$, ma se il sistema è tutto raggiungibile e osservabile, $\Psi$ ha gli stessi poli e il sistema è asintoticamente stabile anche in generale.

> [!tip] Perché serve l'ipotesi
> $W(s)$ contiene solo i modi eccitabili **e** osservabili (la parte $\chi_2$ della [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman#Scomposizione di Kalman|scomposizione di Kalman]]). Senza ipotesi potrebbero esistere modi nascosti, anche instabili, che dalla $W(s)$ non si vedono (come nel [[29 - TDS - Esercizi sulla scomposizione di Kalman#Primo esercizio|primo esercizio della lezione 29]], dove $W\equiv0$). Se il sistema è tutto raggiungibile e osservabile, gli autovalori di $A$ coincidono con i poli di $W$.

### Risposta forzata

Con l'ingresso $u(t)=t+1$:

$$Y_F(s)=W(s)U(s)=W(s)\left(\frac1{s^2}+\frac1s\right)=\frac{s-1}{(s+1)(s+2)}\cdot\frac{s+1}{s^2}=\frac{s-1}{s^2(s+2)}=\frac{R_1}{s+2}+\frac{R_{21}}{s^2}+\frac{R_{22}}{s}$$

(il fattore $s+1$ si semplifica). I residui:

$$R_1=\lim_{s\to-2}\frac{s-1}{s^2}=-\frac34,\qquad R_{21}=\lim_{s\to0}\frac{s-1}{s+2}=-\frac12,\qquad R_{22}=\lim_{s\to0}\frac{d}{ds}\frac{s-1}{s+2}=\lim_{s\to0}\frac{(s+2)-(s-1)}{(s+2)^2}=\frac34$$

$$y_F(t)=\mathcal L^{-1}\left[\frac{R_1}{s+2}+\frac{R_{21}}{s^2}+\frac{R_{22}}{s}\right]=-\frac34e^{-2t}-\frac12t+\frac34$$

Ci sono due tipi di contributi: uno che dipende dal **sistema**, $-\frac34e^{-2t}$, e uno che dipende dall'**ingresso**, $-\frac12t+\frac34$.

> [!note] La semplificazione
> L'ingresso $t+1$ ha uno zero in $s=-1$ ($U(s)=\frac{s+1}{s^2}$) che cancella il polo $-1$ di $W$: il modo $e^{-t}$ **non compare** nella risposta forzata. È il caso, descritto nel libro, in cui "la trasformata dell'ingresso ha un fattore a numeratore coincidente con uno a denominatore della $W(s)$": si realizza un'azione di filtro. _(libro, §4.5, p. 189)_

### Risposta a regime permanente

Il modo migliore è dividere la risposta in due: una per $u_1(t)=t$ e una per $u_2(t)=1$, con $u=u_1+u_2$:

$$y_{RP}(t)=y_{RP,1}(t)+y_{RP,2}(t)=\underbrace{W(s)\big|_{s=0}t+\left[\frac{d}{ds}W(s)\right]_{s=0}}_{y_{RP,1}(t)}+\underbrace{W(s)\big|_{s=0}}_{y_{RP,2}(t)}=-\frac12t+\frac54-\frac12=-\frac12t+\frac34$$

($W(0)=-\frac12$ e $W'(0)=\frac{(1)(2)-(-1)(3)}{4}=\frac54$.) Coincide con la parte della risposta forzata dovuta all'ingresso, come previsto.

### Risposta armonica

Il sistema ammette risposta a regime permanente, quindi $W(s)|_{s=j\omega}$ è una **risposta armonica**. In forma di Bode:

$$W(s)=\frac{s-1}{(s+1)(s+2)}=\frac{(-1)(1-s)}{(1+s)\cdot2\left(1+\frac s2\right)}=-\frac12\cdot\frac{1-s}{(1+s)\left(1+\frac s2\right)}\quad\Longrightarrow\quad W_s(j\omega)=-\frac12\cdot\frac{1-j\omega}{(1+j\omega)\left(1+\frac{j\omega}2\right)}$$

$K=-\frac12$ e tre termini binomi, uno al numeratore e due al denominatore. Punti di interesse: $\frac1{\tau_1}=1$, $\frac1{\tau_2}=1$, $\frac1{\tau_3}=2$.

- $K=-\frac12$: modulo $20\log_{10}\frac12\approx-6$ dB, fase $-\pi$ (è negativo).
- $1-j\omega$ al numeratore: modulo circa zero prima di $\omega=1$, poi retta a $+20$ dB/dec. Fase circa 0 una decade prima di 1 ($\approx0{,}1$), $-\frac\pi2$ una decade dopo ($\approx10$), interpolata in mezzo.
- $1+j\omega$ al denominatore: modulo come quello di $1-j\omega$ ma ribaltato, 0 fino a 1 e poi $-20$ dB/dec. La fase è **identica** a quella di $1-j\omega$ al numeratore (uno è al numeratore con il segno meno, l'altro ha il segno più ma sta al denominatore).
- $1+\frac12j\omega$ al denominatore: modulo 0 fino a $\frac1\tau=2$, poi $-20$ dB/dec. Fase 0 fino a $0{,}2$ e $-\frac\pi2$ da $\omega=20$.

> [!warning] Correzione
> Per l'ultimo termine gli appunti scrivono "salirà con pendenza 20 dB/dec dopo 2": essendo al **denominatore** scende, $-20$ dB/dec, come mostra il grafico (curva viola).

![[TDS-L30-01.png]]

Sommando:

![[TDS-L30-02.png]]

Il modulo è costante a $-6$ dB fino a 2: tra 1 e 2 le pendenze $+20$ (numeratore) e $-20$ ($1+j\omega$) si compensano, e da 2 in poi resta il $-20$ dB/dec del terzo binomio. La fase parte da $-\pi$ e scende fino a $-\frac{5\pi}2$.

> [!tip] Un "passa-tutto" nascosto
> $\frac{1-j\omega}{1+j\omega}$ ha modulo **esattamente** 1 per ogni $\omega$ (zero e polo simmetrici rispetto all'asse immaginario): contribuisce solo alla fase, con $-\pi$ in tutto. Per questo nel modulo restano solo $K$ e il binomio in 2.

### Diagramma polare

Per $\omega\to0^+$ il modulo vale $\frac12$ e la fase $-\pi$; al crescere di $\omega$ il modulo decresce e tende a zero, mentre la fase decresce da $-\pi$ a $-\frac{5\pi}2$. All'infinito la fase tende a $-\frac{5\pi}2$ (equivalente a $-\frac\pi2$), quindi la curva arriva nell'origine **tangente** al semiasse corrispondente:

![[TDS-L30-03.png]]

## Secondo esercizio

$$W(s)=\frac{s+1}{s^2(s+10)}$$

### Risposta forzata

Con un ingresso semplice, $u(t)=e^{2t}$:

$$Y_F(s)=W(s)U(s)=\frac{s+1}{s^2(s+10)(s-2)}=\frac{R_{11}}{s^2}+\frac{R_{12}}{s}+\frac{R_2}{s+10}+\frac{R_3}{s-2}$$

$$y_F(t)=R_{11}t+R_{12}+R_2e^{-10t}+R_3e^{2t},\qquad R_{11}=-\frac1{20},\ R_{12}=-\frac7{100},\ R_2=\frac3{400},\ R_3=\frac1{16}$$

La prima parte della risposta forzata viene dal sistema, mentre $R_3e^{2t}$ dipende dall'ingresso.

> [!tip] Verifica
> $R_{11}=\frac{1}{10\cdot(-2)}$, $R_3=\frac{3}{4\cdot12}$, $R_2=\frac{-9}{100\cdot(-12)}$; e $R_{12}+R_2+R_3=-0{,}07+0{,}0075+0{,}0625=0$, come deve essere per una funzione con grado relativo 3 ✔.

### Risposta a regime permanente

Il sistema **non ammette** risposta a regime permanente: non c'è limite convergente per $t\to+\infty$, perché ci sono poli non negativi (il polo doppio in 0) e, in particolare, termini in $t$ che crescono.

### Diagrammi di Bode

Si disegna $W_s(j\omega)$, che **non** è la risposta armonica (quella esiste solo se esiste il regime permanente). In forma di Bode:

$$W(s)=\frac{s+1}{s^2(s+10)}=\frac1{10}\cdot\frac{1+s}{s^2\left(1+\frac s{10}\right)}\quad\Longrightarrow\quad W_s(j\omega)=\frac1{10}\cdot\frac{1+j\omega}{(j\omega)^2\left(1+\frac{j\omega}{10}\right)}$$

- $K=\frac1{10}$: modulo $20\log_{10}\frac1{10}=-20$ dB, fase 0 (positivo).
- $1+j\omega$ al numeratore: modulo 0 fino a $\omega=1$, poi $+20$ dB/dec; fase 0 fino a $0{,}1$ e $\frac\pi2$ dopo 10, in mezzo si uniscono i punti.
- $(j\omega)^2$ al denominatore: è come contare $j\omega$ due volte. Il modulo è una retta decrescente (al denominatore) passante per $\omega=1$ con pendenza $-40$ dB/dec invece di $-20$; la fase è $-\frac\pi2$ contata due volte, $-\pi$ (i conti tornano: $(j\omega)^2=-\omega^2$, sempre negativo).
- $1+\frac{j\omega}{10}$ al denominatore: modulo 0 prima di $\omega=10$, poi $-20$ dB/dec; fase 0 prima di 1 e $-\frac\pi2$ dopo 100, e in mezzo si uniscono i punti.

> [!warning] Correzione
> Per l'ultimo termine gli appunti scrivono "la fase vale 0 prima di 1, e $\frac\pi2$ dopo 100": essendo al denominatore vale $-\frac\pi2$, come nel grafico (curva viola).

![[TDS-L30-04.png]]

Sommando tutto:

![[TDS-L30-05.png]]

La fase parte da $-\pi$, sale fino a $-\frac{3\pi}4$ (tra 1 e 10 le due rampe si compensano) e torna a $-\pi$ dopo 100.

### Diagramma polare

Per $\omega\to0^+$ il modulo tende a $+\infty$ (continua a crescere per via di $(j\omega)^2$ al denominatore) e la fase è $-\pi$; al crescere di $\omega$ il modulo diminuisce sempre, mentre la fase aumenta leggermente e poi torna a $-\pi$. Approssimativamente, per $\omega>0$:

![[TDS-L30-06.png]]

Dettaglio per $\omega\to+\infty$:

![[TDS-L30-07.png]]

> [!note] Il grafico effettivo
> Per $\omega\to0^+$ il modulo tende a $+\infty$ e la fase va a $-\pi$, quindi la curva dovrebbe adagiarsi sull'asse reale negativo. Nel grafico effettivo non avviene perché, anche se il modulo aumenta e la fase diminuisce, il modulo aumenta molto di più: la curva "da lontano" sembra un arco di parabola. Nel compito d'esame va benissimo farla adagiare sull'asse reale.
>
> In effetti $W_s(j\omega)=\frac{1+j\omega}{-\omega^2(10+j\omega)}$, e la parte immaginaria vale $-\frac{9}{\omega(100+\omega^2)}$: va a $-\infty$ come $\frac1\omega$, mentre la parte reale va a $-\infty$ come $\frac1{\omega^2}$. Il rapporto tende a zero (la fase tende a $-\pi$), ma la distanza dall'asse reale cresce: un asintoto "parabolico", non orizzontale.

## Terzo esercizio

Si modifica "leggermente" la funzione dell'esercizio precedente:

$$W(s)=\frac{s^2+1}{s^2(s+10)}=\frac1{10}\cdot\frac{1+s^2}{s^2\left(1+\frac s{10}\right)}$$

Il termine al numeratore non è più binomio ma **trinomio**: è già in forma di Bode, con $\zeta=0$ (non c'è il termine in $s$ al primo grado) e $\omega_n=1$. Per il modulo in decibel di $W_s(j\omega)$ (modulo e fase si riferiscono sempre a $W_s(j\omega)$, non a $W(s)$): vale 0 fino a una decade prima di $\omega_n=1$ e una decade dopo cresce di 40 dB/dec (cresce perché è al numeratore). La fase vale 0 una decade prima di $\omega_n$ e $\pi$ una decade dopo; la pendenza del passaggio dipende da $\zeta$ e, con $\zeta=0$, il passaggio è immediato: la fase ha un **salto**.

Tutto il resto è identico all'esempio precedente.

![[TDS-L30-08.png]]

> [!warning] Correzione
> Nella legenda dei grafici di questo esercizio la costante è indicata come $-\frac1{10}$, e la fase complessiva parte da $-2\pi$: sono i grafici di $K=-\frac1{10}$. Ma qui $K=+\frac{1}{10}$ (fase 0), come nell'esercizio precedente e come confermano gli appunti nel diagramma polare (fase $-\pi$ per $\omega\to0^+$). Con il segno corretto la fase va da $-\pi$ (per $\omega<1$) a $0$ subito dopo il salto in $\omega=1$, e poi scende a $-\frac\pi2$ per effetto del binomio $1+\frac{s}{10}$: i grafici della fase vanno quindi traslati di $+\pi$. Il modulo non cambia.

Per il modulo conviene sommare gli asintoti del termine trinomio e **poi** aggiungere le "pance" (qui la "pancia" è proprio un asintoto verticale verso $-\infty$):

![[TDS-L30-09.png]]

### Diagramma polare

Per $\omega\to0^+$ il modulo va all'infinito con fase $-\pi$: la curva parte dall'estrema sinistra dell'asse reale. Il modulo decresce al crescere di $\omega$, e a $\omega=1$ il modulo in decibel vale $-\infty$, cioè il modulo effettivo vale **zero**: a $\omega=1$ la curva passa per l'origine, e c'è il salto della fase (si sta banalmente attraversando l'origine). Superato $\omega=1$ il modulo cresce fino a un certo valore e poi decresce, mentre la fase decresce fino a $-\frac\pi2$. Il diagramma polare si può immaginare così:

![[TDS-L30-12.png]]

(le frecce vanno da $\omega=0^+$ a $\omega=+\infty$; tratteggiato il ribaltamento per $\omega<0$ vicino all'origine).

> [!tip] Interpretazione
> Lo zero di trasmissione in $s=\pm j$ significa che una sinusoide di pulsazione esattamente 1 **non passa** attraverso il sistema (a regime, se esistesse): $W_s(j1)=0$. È un filtro "elimina banda" ideale a $\omega=1$.

## Quarto esercizio

$$W(s)=\frac{s+10}{s(s^2+1)}=10\cdot\frac{1+\frac s{10}}{s(1+s^2)}$$

- $K=10$: modulo 20 dB, fase 0 (positivo).
- $1+\frac{j\omega}{10}$ al numeratore: zero fino a $\omega=\frac1\tau=10$, poi $+20$ dB/dec. Fase 0 prima di 1, $\frac\pi2$ dopo 100, e in mezzo si uniscono gli estremi.
- $s$ al denominatore: modulo passante per $\omega=1$ e decrescente con $-20$ dB/dec. Fase fissa a $-\frac\pi2$.
- $1+s^2$: termine trinomio come nell'esercizio precedente, ma stavolta al **denominatore**: modulo e fase ribaltati. Gli asintoti del modulo valgono 0 prima di $\omega_n=1$ e scendono con $-40$ dB/dec dopo 1; la fase ha un salto a $\omega=1$ da 0 a $-\pi$.

> [!warning] Correzione
> Per il termine $s$ al denominatore gli appunti scrivono "la fase è fissa a $\frac\pi2$": al denominatore è $-\frac\pi2$ (curva gialla nel grafico).

![[TDS-L30-10.png]]

Sommando:

![[TDS-L30-11.png]]

Il picco in $\omega=1$ è la risonanza con $\zeta=0$ (modulo infinito).

### Diagramma polare

Per $\omega\to0^+$ il modulo è infinito e la fase vale $-\frac\pi2$: la curva parte dal semiasse immaginario negativo, all'infinito "verso il basso". Mentre la fase resta (asintoticamente) costante, il modulo decresce fino a un minimo e poi risale all'infinito (per $\omega\to1^-$). A destra di 1 il modulo "torna" dall'infinito e la fase passa da $-\frac{3\pi}2$ a $-\pi$ (la fase $-\frac{3\pi}2$ corrisponde a $\frac\pi2$: la curva rientra dall'alto), mentre il modulo va a $-\infty$ in decibel, cioè a zero:

![[TDS-L30-13.png]]

È mostrata solo la parte per $\omega>0$; per $\omega<0$ si ribalta il grafico rispetto all'asse reale.

> [!tip] Verifica
> $W_s(j\omega)=\frac{10+j\omega}{j\omega(1-\omega^2)}=\frac{1}{1-\omega^2}\Big(1-j\frac{10}{\omega}\Big)$. Per $\omega<1$ la parte immaginaria è negativa, per $\omega>1$ positiva (e la parte reale cambia segno): la curva passa dal semipiano inferiore a quello superiore "attraverso l'infinito", come nel disegno. Per $\omega\to0^+$ la parte reale tende a 1: c'è un asintoto verticale in $\mathrm{Re}=1$, simile a quello visto per $\frac{1}{s(s+1)}$ in [[25 - TDS - Risposta indiciale e diagramma polare#Rappresentazione della risposta armonica nel diagramma polare|lezione 25]].

## Considerazioni finali

Un sistema con funzione di trasferimento

$$W(s)=\frac{s+10}{s^2+1}$$

ammette risposta a regime permanente? **No**: $s^2+1=(s+j)(s-j)$ ha due radici complesse coniugate con **parte reale nulla**, e per il regime permanente servono poli a parte reale **strettamente negativa**. Lo stesso varrebbe con un termine $s$ o $s^2$ al denominatore.

> [!important] Quando esiste il regime permanente
> Serve che tutti i poli di $W(s)$ (e, per l'indipendenza dallo stato iniziale, tutti gli autovalori osservabili) abbiano parte reale **strettamente** negativa. Poli sull'asse immaginario ($s=0$, $s=\pm j\omega_0$) danno modi che non si spengono, e la risposta a un ingresso limitato può anche divergere (risonanza con $\zeta=0$, oppure integratore con ingresso costante).
