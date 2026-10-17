---
title: Esempio a tempo discreto e campionamento
aliases:
  - TDS — Esempio a tempo discreto e campionamento
tags:
  - teoria-dei-sistemi
  - esempio
  - modi-naturali
  - tempo-discreto
  - campionamento
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 32–40); libro Monaco et al., §2.6
---

# Esempio a tempo discreto e campionamento

> [!abstract] Scopo della lezione
> 1. Un **esempio completo** di analisi modale su un sistema di dimensione 3 con un autovalore reale e una coppia complessa: autovalori, autovettori, base reale, $e^{At}$, modi naturali, eccitabilità e osservabilità. È la sintesi pratica delle lezioni [[05 - TDS - Calcolo dell'esponenziale di matrice|5]]–[[08 - TDS - Modi aperiodici e pseudoperiodici|8]].
> 2. Lo **stesso sistema a tempo discreto**, con gli autovalori complessi in forma polare ([[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Autovalori complessi nel tempo discreto|lezione 9]]).
> 3. Il **campionamento**: come vedere un sistema a tempo continuo dall'esterno come un sistema a tempo discreto, con un dispositivo di tenuta (ZOH) e un campionatore, e quali sono le matrici $A_d$ e $B_d$ del sistema campionato.
>
> Segue [[11 - TDS - Punti di equilibrio e stabilità]]. Indice: [[MOC - Teoria dei Sistemi]].

## Esempio pratico

Consideriamo il sistema a tempo continuo

$$\begin{cases}\dot x(t)=\begin{pmatrix}2&0&0\\1&1&1\\1&-1&1\end{pmatrix}x(t)+\begin{pmatrix}1\\1\\0\end{pmatrix}u(t)\\[2mm]y(t)=\begin{pmatrix}0&0&1\end{pmatrix}x(t)\end{cases}$$

con $n=3$ (dimensione di $A$), $p=1$ (colonne di $B$, cioè ingressi) e $q=1$ (righe di $C$, cioè uscite).

### Calcolo degli autovalori e autovettori

Vogliamo studiare la dinamica, quindi i modi naturali: servono autovalori e autovettori di $A$ (e si procede così se la matrice è regolare). Sviluppando il determinante lungo la prima riga:

$$\det(A-\lambda I)=\det\begin{pmatrix}2-\lambda&0&0\\1&1-\lambda&1\\1&-1&1-\lambda\end{pmatrix}=(2-\lambda)\big[(1-\lambda)^2+1\big]=(2-\lambda)(\lambda^2-2\lambda+2)\stackrel{\text{set}}{=}0$$

$$\iff\lambda_1=2,\quad\lambda_{2,3}=1\pm\sqrt{-1}\iff\lambda_1=2,\ \lambda_2=1+j,\ \lambda_3=1-j$$

**Autovettore di $\lambda_1=2$.** Si cerca $u_1$ tale che $(A-\lambda_1I)u_1=0$ (la matrice si ottiene sostituendo $\lambda=2$):

$$\begin{pmatrix}0&0&0\\1&-1&1\\1&-1&-1\end{pmatrix}\begin{pmatrix}u_{11}\\u_{12}\\u_{13}\end{pmatrix}=\begin{pmatrix}0\\u_{11}-u_{12}+u_{13}\\u_{11}-u_{12}-u_{13}\end{pmatrix}\stackrel{\text{set}}{=}\begin{pmatrix}0\\0\\0\end{pmatrix}\iff\begin{cases}u_{11}-u_{12}+u_{13}=0\\u_{11}-u_{12}-u_{13}=0\end{cases}$$

"A occhio" basta porre $u_{13}=0$ e $u_{11}=u_{12}$ (per esempio $1$): $u_1=(1,1,0)'$. In modo sistematico, come in Geometria, si trova tutto $\ker(A-\lambda_1I)$ riducendo a scala ([[GEO - Calcolo del nucleo e rango-nullità]]):

$$\begin{pmatrix}0&0&0\\1&-1&1\\1&-1&-1\end{pmatrix}\sim\begin{pmatrix}1&-1&-1\\1&-1&1\\0&0&0\end{pmatrix}\sim\begin{pmatrix}\boxed1&-1&0\\0&0&\boxed1\\0&0&0\end{pmatrix}$$

I pivot sono nelle colonne 1 e 3; la colonna senza pivot ($u_{12}$) diventa un parametro $h\in\mathbb R$: $u_{11}=h$, $u_{12}=h$, $u_{13}=0$. Con $h=1$ si ritrova la soluzione del professore.

**Autovettori complessi.** Ci sono due strade.
- **Consigliata**: procedere come per l'autovalore reale, risolvendo $(A-\lambda_2I)u_2=0$ in $\mathbb C^3$. Si trova $u_2=u_{2a}+ju_{2b}$, e $u_3$ non serve calcolarlo: è il coniugato, $u_3=u_2^*=u_{2a}-ju_{2b}$.
- **Sconsigliata**: separare parte reale e immaginaria. Con $\lambda_2=\alpha_2+j\omega$:
  $$(A-\lambda_2I)u_2=(A-\alpha_2I-j\omega I)(u_{2a}+ju_{2b})=(Au_{2a}-\alpha_2u_{2a}+\omega u_{2b})+j(Au_{2b}-\alpha_2u_{2b}-\omega u_{2a})\stackrel{\text{set}}{=}0$$
  $$\Longrightarrow\begin{cases}Au_{2a}-\alpha_2u_{2a}+\omega u_{2b}=0\\Au_{2b}-\alpha_2u_{2b}-\omega u_{2a}=0\end{cases}$$
  e il calcolo può diventare lungo.

Con il primo metodo:

$$(A-\lambda_2I)u_2=0\iff\begin{pmatrix}1-j&0&0\\1&-j&1\\1&-1&-j\end{pmatrix}\begin{pmatrix}u_{21}\\u_{22}\\u_{23}\end{pmatrix}=0\iff\begin{cases}(1-j)u_{21}=0\\u_{21}-ju_{22}+u_{23}=0\\u_{21}-u_{22}-ju_{23}=0\end{cases}$$

Subito $u_{21}=0$. Allora la seconda equazione ($-ju_{22}+u_{23}=0$) è la terza ($-u_{22}-ju_{23}=0$) moltiplicata per $j$: sono equivalenti e ne basta una. Si ha $u_{23}=ju_{22}$: scelto $u_{22}$, $u_{23}$ è lo stesso valore per $j$. Per coerenza con il professore si sceglie $u_{22}=-j$, quindi $u_{23}=-j\cdot j=1$:

$$u_2=\begin{pmatrix}0\\-j\\1\end{pmatrix}=\begin{pmatrix}0\\0\\1\end{pmatrix}+j\begin{pmatrix}0\\-1\\0\end{pmatrix}\quad\Longrightarrow\quad u_3=u_2^*=\begin{pmatrix}0\\0\\1\end{pmatrix}-j\begin{pmatrix}0\\-1\\0\end{pmatrix}=\begin{pmatrix}0\\j\\1\end{pmatrix}$$

(trovare $u_3$ è banale: basta cambiare segno a tutti i termini immaginari).

> [!tip] Verifica
> $Au_2=(0,\ 1-j,\ 1+j)'$ e $\lambda_2u_2=(1+j)(0,-j,1)'=(0,\ -j-j^2,\ 1+j)'=(0,\ 1-j,\ 1+j)'$. ✔

### Forma diagonale e base reale

Con autovalori e autovettori:

$$A=U\Lambda U^{-1}=\begin{pmatrix}1&0&0\\1&-j&j\\0&1&1\end{pmatrix}\begin{pmatrix}2&0&0\\0&1+j&0\\0&0&1-j\end{pmatrix}\begin{pmatrix}1&0&0\\1&-j&j\\0&1&1\end{pmatrix}^{-1}$$

(colonne $u_1,u_2,u_3$). Come visto, invece di tenere le parti immaginarie si sostituiscono a $u_2$ e $u_3=u_2^*$ i vettori reali $u_a$ e $u_b$, e la coppia diventa il blocchetto $2\times2$:

$$u_2=u_a+ju_b\ \Longrightarrow\ u_a=\begin{pmatrix}0\\0\\1\end{pmatrix},\ u_b=\begin{pmatrix}0\\-1\\0\end{pmatrix},\qquad A=\underbrace{\begin{pmatrix}1&0&0\\1&0&-1\\0&1&0\end{pmatrix}}_{(u_1\ u_a\ u_b)}\begin{pmatrix}2&0&0\\0&1&1\\0&-1&1\end{pmatrix}\begin{pmatrix}1&0&0\\1&0&-1\\0&1&0\end{pmatrix}^{-1}$$

Infatti $\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}=\begin{psmallmatrix}1&1\\-1&1\end{psmallmatrix}$ perché $\lambda_2=1+j$. L'esponenziale è

$$e^{At}=Ue^{\Lambda t}U^{-1}=\begin{pmatrix}1&0&0\\1&0&-1\\0&1&0\end{pmatrix}\begin{pmatrix}e^{2t}&0&0\\0&e^t\cos t&e^t\sin t\\0&-e^t\sin t&e^t\cos t\end{pmatrix}\begin{pmatrix}1&0&0\\1&0&-1\\0&1&0\end{pmatrix}^{-1}$$

**Inversa.** Si può usare il metodo del determinante (cofattori) oppure Gauss-Jordan. $\det U=1$ e

$$U^{-1}=\begin{pmatrix}1&0&0\\0&0&1\\1&-1&0\end{pmatrix}=\begin{pmatrix}v_1'\\v_a'\\v_b'\end{pmatrix}$$

Ogni **riga** di $U^{-1}$ è uno dei vettori riga: $(1\ 0\ 0)=v_1'$, ecc. Quindi

$$e^{At}=\begin{pmatrix}1&0&0\\1&0&-1\\0&1&0\end{pmatrix}\begin{pmatrix}e^{2t}&0&0\\0&e^t\cos t&e^t\sin t\\0&-e^t\sin t&e^t\cos t\end{pmatrix}\begin{pmatrix}1&0&0\\0&0&1\\1&-1&0\end{pmatrix}$$

### Modi naturali

Vedi [[TDS - Modi aperiodici e pseudoperiodici]].

L'evoluzione libera è

$$x_L(t)=c_1e^{2t}\underbrace{\begin{pmatrix}1\\1\\0\end{pmatrix}}_{u_1}+me^t\Bigg(\sin(t+\varphi)\underbrace{\begin{pmatrix}0\\0\\1\end{pmatrix}}_{u_a}+\cos(t+\varphi)\underbrace{\begin{pmatrix}0\\-1\\0\end{pmatrix}}_{u_b}\Bigg)$$

con $m=\sqrt{c_a^2+c_b^2}$ e $\varphi$ tale che $\sin\varphi=\frac{c_a}{m}$, $\cos\varphi=\frac{c_b}{m}$. Ci sono due modi: uno **aperiodico divergente** ($\lambda_1=2>0$) lungo $u_1$ e uno **pseudoperiodico divergente** ($\alpha=1>0$, $\omega=1$) nel piano di $u_a,u_b$. Il moto somiglia a questo:

![[TDS-L10-01.png]]

La traiettoria (rossa) è una spirale che si allarga nel piano di $u_a,u_b$ mentre si allontana lungo $u_1$, che cresce più in fretta ($e^{2t}$ contro $e^{t}$).

### Eccitabilità e osservabilità

Vedi [[TDS - Eccitabilità e osservabilità dei modi]].

**Modo aperiodico** ($\lambda_1=2$):

$$Cu_1=(0\ 0\ 1)\begin{pmatrix}1\\1\\0\end{pmatrix}=0,\qquad v_1'B=(1\ 0\ 0)\begin{pmatrix}1\\1\\0\end{pmatrix}=1$$

È **eccitabile** ma **non osservabile**.

> [!warning] Correzione
> Negli appunti si legge "verifichiamo i prodotti $Cu_1$ e $v_1'C$": il secondo prodotto è $v_1'B$, come nel calcolo subito dopo.

**Modo pseudoperiodico.** Le soluzioni sono due (complesse coniugate), ma il modo naturale è uno solo. È **non osservabile** se e solo se valgono **entrambe** $Cu_a=0$ e $Cu_b=0$:

$$Cu_a=(0\ 0\ 1)\begin{pmatrix}0\\0\\1\end{pmatrix}=1,\qquad Cu_b=(0\ 0\ 1)\begin{pmatrix}0\\-1\\0\end{pmatrix}=0$$

quindi è **osservabile**. È **non eccitabile** se valgono entrambe $v_a'B=0$ e $v_b'B=0$:

$$v_a'B=(0\ 0\ 1)\begin{pmatrix}1\\1\\0\end{pmatrix}=0,\qquad v_b'B=(1\ -1\ 0)\begin{pmatrix}1\\1\\0\end{pmatrix}=0$$

entrambi nulli: è **non eccitabile**. Quindi $H(t)$ contiene solo il modo aperiodico, $\Psi(t)$ solo quello pseudoperiodico, e $W(t)$ nessuno dei due. In notazione insiemistica:

$$\Lambda=\{2,\ 1+j,\ 1-j\},\qquad\Lambda_e=\{2\},\quad\Lambda_o=\{1+j,\ 1-j\},\quad\Lambda_{e,o}=\{\}$$

> [!example] Conseguenza
> Poiché $\Lambda_{e,o}=\emptyset$ e $D=0$, la risposta impulsiva in uscita è identicamente nulla: $W(t)=Ce^{At}B=0$. Dall'esterno (ingresso → uscita) il sistema sembra "non fare niente", eppure dentro ha due modi **divergenti**. È il primo esempio del perché serviranno [[TDS - Raggiungibilità|raggiungibilità]] e [[TDS - Osservabilità|osservabilità]] e la [[TDS - Scomposizione di Kalman|scomposizione di Kalman]].

## Esempio pratico: analogia con il caso discreto

Ora lo stesso sistema, ma a tempo discreto:

$$\begin{cases}x(t+1)=\begin{pmatrix}2&0&0\\1&1&1\\1&-1&1\end{pmatrix}x(t)+\begin{pmatrix}1\\1\\0\end{pmatrix}u(t)\\[2mm]y(t)=\begin{pmatrix}0&0&1\end{pmatrix}x(t)\end{cases}$$

Gli autovalori non cambiano: $2$, $1+j$, $1-j$. Ma conviene scrivere quelli complessi in forma **modulo-fase**:

$$\lambda_2=1+j=\rho e^{j\theta}=\sqrt2\,e^{j\frac\pi4},\qquad\rho=\sqrt{1+1}=\sqrt2,\quad\theta=\arctan(1)=\frac\pi4$$

![[TDS-L10-02.png]]

$1+j$ è il punto $(1,1)$ del piano complesso: il segmento che lo congiunge all'origine è lungo $\sqrt2$ e forma un angolo $\pi/4$ con l'asse reale. Si ritrova $\alpha=\rho\cos\theta=\sqrt2\cos\frac\pi4=1$ e $\omega=\rho\sin\theta=1$, quindi lo stesso blocco $\begin{psmallmatrix}1&1\\-1&1\end{psmallmatrix}$, ma ora si possono calcolare le potenze:

$$A^t=U\Lambda^tU^{-1}=\begin{pmatrix}1&0&0\\1&0&-1\\0&1&0\end{pmatrix}\begin{pmatrix}2^t&0&0\\0&(\sqrt2)^t\cos\big(\frac\pi4t\big)&(\sqrt2)^t\sin\big(\frac\pi4t\big)\\0&-(\sqrt2)^t\sin\big(\frac\pi4t\big)&(\sqrt2)^t\cos\big(\frac\pi4t\big)\end{pmatrix}\begin{pmatrix}1&0&0\\0&0&1\\1&-1&0\end{pmatrix}$$

Per eccitabilità e osservabilità non cambia nulla: $\Lambda_e$ e $\Lambda_o$ restano gli stessi (anche se i modi seguono leggi diverse). Entrambi i modi sono divergenti, perché $2>1$ e $\rho=\sqrt2>1$.

## Tempo discreto campionato

Vedi [[TDS - Campionamento]].

> [!note] Annotazione di Simone
> Accanto al titolo, a mano in rosso: **"CAMPIONATO"**.

Nei sistemi a tempo discreto la variabile $t$, nella maggior parte dei casi, non ha nulla a che fare con il "tempo dell'orologio": $t=1,2,\dots$ indicano **eventi** che possono accadere a intervalli di tempo diversi tra loro. Ma ci possono essere dei legami: se si legge un valore *una volta al secondo*, $t$ è chiaramente legato al tempo reale. Questo è il modo di rappresentare un sistema a tempo continuo in forma discreta, ed è come funziona la maggior parte degli strumenti digitali di misura.

**Obiettivo.** Abbiamo un sistema a tempo continuo $\mathcal S_{tc}$ con ingresso $u(t)$ e uscita $y(t)$, e vogliamo vederlo dall'esterno come un sistema a tempo discreto: un ingresso discreto $u_d(t)$ deve produrre un'uscita discreta $y_d(t)$.

![[TDS-L10-03.png]]

> [!note] Annotazione di Simone
> Sopra il paragrafo, a mano in verde: **"Obbiettivo"**.

### Il dispositivo di tenuta (holder)

Il primo problema è che $u_d(t)$ è una funzione discreta, mentre il sistema si aspetta un ingresso continuo: serve un dispositivo che "trasformi" l'ingresso discreto in un ingresso continuo. Si chiama **dispositivo di tenuta** (*holder*). Se si limita a **mantenere costante** il valore di un ingresso fino all'arrivo del successivo, si chiama **tenuta di ordine zero** o *zero-order holder* (**ZOH**):

![[TDS-L10-04.png]]

A sinistra i campioni dell'ingresso discreto; a destra, dopo lo ZOH, una funzione **costante a tratti** che su ogni intervallo vale l'ultimo campione.

> [!note] Annotazioni di Simone
> A mano: **"Holder"**, **"ingresso"** (sui campioni), **"EFFETTO DELL'HOLDER ZOH"** (sulla freccia), **"Mantiene Costante l'ingresso"** (sul grafico a destra).

Ora il tempo discreto non indica più eventi, ma il tempo reale: l'intervallo tra due "misurazioni" successive si chiama **tempo di campionamento** $T_c$.

> [!note] Annotazione di Simone
> Accanto alla definizione: **"Tempo di Campionamento"**.

Un'altra scelta per passare da discreto a continuo è l'**interpolazione** dei punti:

![[TDS-L10-05.png]]

> [!note] Annotazioni di Simone
> **"Interpolazione"** e **"in questo caso Interpolazione di ordine 1 (retta)"**.

Se i punti si uniscono con rette, come qui, si parla di **tenuta di ordine 1**; con archi di parabola di **ordine 2**, e così via. Si capisce anche il nome "ordine zero": si usano polinomi di grado zero, cioè costanti a tratti.

Il problema della tenuta di ordine 1 è che, fatta una misura al tempo $t$, per tracciare la retta serve anche la misura **successiva**: finché non c'è, non si sa "quanto vale in mezzo".

![[TDS-L10-06.png]]

A sinistra (ordine 1), all'istante indicato dalla barra rossa non si sa come tracciare il tratto tra $t=2$ e $t=3$, perché la misura in $t=3$ non c'è ancora: il valore del sistema in quell'istante non si conosce a priori. A destra (ordine zero) invece sì: si prolunga l'ultimo valore. Con tenute di ordine superiore a zero si introduce, di fatto, un **ritardo** nel sistema. Il ritardo cresce con l'ordine: per la tenuta di ordine 2 servono due misure successive oltre a quella iniziale per tracciare un arco di parabola, per l'ordine 3 tre, e così via.

> [!note] Annotazioni di Simone
> Accanto ai grafici, a mano in blu: **"problema dell' interpolazione di ordine 1"**, **"La retta da t₀=2 a t₀=3 non viene tracciata finche non registriamo t = t₀ = 3, a tempo di misurazione"** e **"Con tenute di ordine ≠0 abbiamo un ritardo di sistema"**.

### Il campionatore

Risolto il problema dell'ingresso, $u(t)$ continuo entra in $\mathcal S_{tc}$ e si ottiene $y(t)$. Se $D=0$ (il caso più frequente) l'uscita è continua ma con **derivata discontinua** negli istanti in cui l'ingresso salta:

![[TDS-L10-07.png]]

Se $D\neq0$ è discontinua l'uscita stessa, perché contiene il termine $Du(t)$ che salta. Resta da "trasformare" $y(t)$ in un'uscita discreta: basta prenderne il valore ogni $T_c$.

![[TDS-L10-08.png]]

> [!note] Annotazione di Simone
> Accanto al grafico, a mano in verde: **"Soluzione banale"**.

Il dispositivo che fa questo si chiama **campionatore**. Il sistema complessivo è:

![[TDS-L10-09.png]]

$u_d(t)$ → ZOH → $u(t)$ → $\mathcal S_{tc}$ → $y(t)$ → campionatore (interruttore che si chiude ogni $T_c$) → $y_d(t)$.

### Il modello matematico del sistema campionato

Vedi [[TDS - Sistemi a tempo discreto]].

$\mathcal S_{tc}$ è descritto in modo continuo:

$$\dot x(t)=Ax(t)+Bu(t)\iff x(t)=e^{A(t-t_0)}x(t_0)+\int_{t_0}^{t}e^{A(t-\tau)}Bu(\tau)\,d\tau$$

Per la forma discreta si prende come $t_0$ un generico istante di campionamento $kT_c$ e come $t$ "la volta dopo", $(k+1)T_c$:

$$x\big((k+1)T_c\big)=e^{AT_c}x(kT_c)+\int_{kT_c}^{(k+1)T_c}e^{A((k+1)T_c-\tau)}Bu(\tau)\,d\tau$$

> [!note] Annotazione di Simone
> Accanto alla formula, a mano: **"Tc è il tempo di campionamento"**.

$e^{AT_c}$ è $e^{At}$ calcolata in $t=T_c$: una matrice $n\times n$ **a valori costanti**. Ci aspettiamo infatti un sistema della forma $x(t+1)=A_dx(t)+B_du(t)$, e $e^{AT_c}$ è proprio la $A_d$ che cerchiamo.

Nell'integrale l'intervallo va da $kT_c$ a $(k+1)T_c$, e lì l'ingresso è **costante**, per via della tenuta di ordine zero:

![[TDS-L10-10.png]]

> [!note] Annotazione di Simone
> Accanto al grafico: **"Comportamento u(kTc)"**.

Quindi $u(\tau)=u(kT_c)$ esce dall'integrale:

$$x\big((k+1)T_c\big)=A_dx(kT_c)+\left(\int_{kT_c}^{(k+1)T_c}e^{A((k+1)T_c-\tau)}B\,d\tau\right)u(kT_c)$$

L'integrale tra parentesi è definito, quindi è una **matrice costante**, che chiamiamo $B_d$. Per leggerlo meglio si pone $\vartheta=(k+1)T_c-\tau$ ($d\tau=-d\vartheta$; per $\tau=kT_c$ si ha $\vartheta=T_c$, per $\tau=(k+1)T_c$ si ha $\vartheta=0$):

$$\int_{kT_c}^{(k+1)T_c}e^{A((k+1)T_c-\tau)}B\,d\tau=-\int_{T_c}^{0}e^{A\vartheta}B\,d\vartheta=\int_0^{T_c}e^{A\vartheta}B\,d\vartheta=:B_d$$

Il risultato è

$$x\big((k+1)T_c\big)=A_dx(kT_c)+B_du(kT_c),\qquad A_d=e^{AT_c},\quad B_d=\int_0^{T_c}e^{A\vartheta}B\,d\vartheta$$

e, poiché l'uscita è campionata negli stessi istanti, $C_d=C$, $D_d=D$.

**Autovalori del sistema campionato.** Con la forma spettrale, se $A=U\Lambda_RU^{-1}$:

$$A_d=e^{AT_c}=Ue^{\Lambda_RT_c}U^{-1}=U\begin{pmatrix}e^{\lambda_1T_c}&&\\&\ddots&\\&&e^{\lambda_nT_c}\end{pmatrix}U^{-1}$$

Ma anche $A_d=U\Lambda_dU^{-1}$, quindi $\Lambda_d=e^{\Lambda_RT_c}$: gli autovalori del sistema discreto campionato sono

$$\lambda_{i,d}=e^{\lambda_iT_c}$$

Nel caso reale, essendo esponenziali, sono **sempre positivi**: un sistema campionato non può avere modi alternanti che vengano da autovalori reali. Gli **autovettori** sono gli stessi di $A$, e per eccitabilità e osservabilità non cambia nulla: i modi eccitabili del sistema continuo restano eccitabili nel sistema discreto (con $v_i'B_d=v_i'B\int_0^{T_c}e^{\lambda_i\vartheta}d\vartheta$, e l'integrale è non nullo).

> [!quote] Dal libro — discretizzazione
> Il libro chiama il procedimento **discretizzazione**: "il problema in esame è noto nella letteratura dei sistemi dinamici con il nome di problema della discretizzazione (di un sistema a tempo continuo)", e il modello ottenuto **rappresentazione a tempo discreto** del sistema continuo; indica $A_T$, $B_T$ le matrici e $\mathcal C^T$ i campionatori. Sugli autovalori ($\lambda_i^d=e^{\lambda_i^cT}$) aggiunge che "non possono assumere valori arbitrari, non possono ad esempio essere uguali a zero. Inoltre possono essere negativi solo se corrispondenti ad una coppia di autovalori complessi coniugati di opportuna pulsazione", per cui gli eventuali modi alternanti si presentano **a coppie**. _(libro, §2.6, pp. 91–94)_

> [!warning] Precisazione
> L'affermazione degli appunti che eccitabilità e osservabilità "non cambiano" vale per gli autovalori reali. Con coppie complesse ci sono valori **particolari** di $T_c$ (quando $\omega T_c$ è multiplo di $\pi$) in cui due autovalori distinti del continuo diventano uguali nel discreto ($e^{(\alpha+j\omega)T_c}=e^{(\alpha-j\omega)T_c}$), e si possono perdere proprietà strutturali. È lo stesso fenomeno della frequenza "massima" visto in [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Alcune osservazioni sul moto pseudoperiodico|lezione 9]].

> [!example] Dal libro — l'integratore (Esempio 2.6.2)
> Per l'integratore di ordine $n$ ($\dot x_1=x_2,\dots,\dot x_n=u$) la matrice $A$ è nilpotente ($A^n=0$) e la serie di $e^{At}$ si ferma: $A_T=I+TA+\dots+\frac{T^{n-1}}{(n-1)!}A^{n-1}$ e $B_T=\int_0^Te^{A\vartheta}d\vartheta\,B=\big(TI+\frac{T^2}{2!}A+\dots+\frac{T^n}{n!}A^{n-1}\big)B=\big(\frac{T^n}{n!},\dots,\frac{T^2}{2},T\big)'$. Nel caso $n=1$ ($\dot x=u$) si ottiene $x(k+1)=x(k)+Tu(k)$: il **metodo di Eulero**. Un sistema il cui discretizzato ha un numero finito di termini in $T$ si dice **finito discretizzabile**. _(libro, §2.6, pp. 95–96)_
>
> Nota: nella formula generale il libro stampa $B_T=T\big(I+TA+\dots+\frac{T^{n-1}}{(n-1)!}A^{n-1}\big)B$, che non torna con il vettore $B_T=\big(\frac{T^n}{n!},\dots,T\big)'$ calcolato poche righe prima; integrando $e^{A\vartheta}$ termine a termine i coefficienti corretti sono $\frac{T^{k+1}}{(k+1)!}$, come scritto sopra.

Quando si trattano sistemi campionati spesso si omette $T_c$ e si scrive tutto in funzione del passo di campionamento $k$:

$$x(k+1)=A_dx(k)+B_du(k)$$

> [!note] Annotazione di Simone
> Accanto a questa formula, a mano: **"Notazione sistemi campionati"**.
