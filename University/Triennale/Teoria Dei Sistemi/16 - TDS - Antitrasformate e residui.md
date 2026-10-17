---
title: Antitrasformate e residui
aliases:
  - TDS — Antitrasformate e residui
tags:
  - teoria-dei-sistemi
  - trasformata-di-laplace
  - antitrasformata
  - residui
  - esponenziale-di-matrice
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 77–84); libro Monaco et al., §4.2–4.2.2
---

# Antitrasformate e residui

> [!abstract] Scopo della lezione
> Nella [[15 - TDS - Trasformata di Laplace|lezione precedente]] il sistema è stato portato nel dominio $s$, dove tutto è un prodotto di funzioni razionali. Per tornare nel tempo servono le **antitrasformate**. Qui si vede come farle senza l'integrale complesso:
> 1. **scomposizione in fratti semplici** e calcolo dei coefficienti, i **residui**, con i limiti;
> 2. **poli multipli**: si usano le derivate, dividendo per $k!$;
> 3. **poli complessi coniugati**: i residui sono coniugati e si ricombinano in seni e coseni;
> 4. la **traslazione complessa** per antitrasformare termini come $\frac1{(s+1)^2}$;
> 5. il **calcolo di $e^{At}$** come $\mathcal L^{-1}[(sI-A)^{-1}]$: i residui sono matrici, e coincidono con le $u_iv_i'$ della [[05 - TDS - Calcolo dell'esponenziale di matrice|forma spettrale]].
>
> Segue [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori]]. Indice: [[MOC - Teoria dei Sistemi]].

> [!note] Annotazione di Simone
> In testa alla lezione, a mano in viola: **"RESIDUI"**.

## Riepilogo della scorsa lezione

La trasformata di Laplace

$$\mathcal L[f(t)]=F(s)=\int_0^{+\infty}f(t)e^{-st}\,dt$$

è biunivoca per $t\ge0$: per convenzione si assume $f(t)=0$ per $t<0$. Spesso la trasformata esiste per $\mathrm{Re}(s)>k$, con $k$ **ascissa di convergenza**. Con essa il sistema si rappresenta **univocamente** nel dominio di $s$:

$$X(s)=\Phi(s)x_0+H(s)U(s),\qquad Y(s)=\Psi(s)x_0+W(s)U(s)$$

con $\Phi(s)=(sI-A)^{-1}$, $\Psi(s)=C\Phi(s)$, $H(s)=\Phi(s)B$, $W(s)=C\Phi(s)B+D$. Trovate $X_F(s)$ e $Y_F(s)$ si deve tornare a $x_F(t)$ e $y_F(t)$. Si avranno sempre funzioni razionali **strettamente proprie**, tranne $W(s)$ quando $D\neq0$ (che è solo propria).

> [!warning] Correzione
> Negli appunti si legge "tornare a $x_F(s)$ e $y_F(s)$": si torna a $x_F(t)$ e $y_F(t)$. Inoltre il riepilogo scrive $W(s)=C\Phi(s)B$, che vale solo con $D=0$; in generale $W(s)=C\Phi(s)B+D$ (come dice la frase subito dopo).

## Antitrasformate e residui

Vedi [[TDS - Antitrasformata e residui]].

Come si antitrasforma una funzione razionale strettamente propria? Per esempio:

$$W(s)=\frac1{s+1},\qquad u(t)=\delta_{-1}(t)\ \Rightarrow\ U(s)=\frac1s,\qquad Y_F(s)=W(s)U(s)=\frac1{s+1}\cdot\frac1s=\frac1{s(s+1)}$$

Nella [[15 - TDS - Trasformata di Laplace#Trasformate di alcune funzioni|tabella delle trasformate]] ci sono solo termini con denominatore di grado 1: questo, di secondo grado, non si antitrasforma "a occhio". Si prova a scriverlo come somma di **fratti semplici**:

$$\frac1{s(s+1)}=\frac as+\frac b{s+1}\quad\Longrightarrow\quad\mathcal L^{-1}\left[\frac1{s(s+1)}\right]=a\,\mathcal L^{-1}\left[\frac1s\right]+b\,\mathcal L^{-1}\left[\frac1{s+1}\right]=a\,\delta_{-1}(t)+b\,e^{-t}$$

> [!note] Annotazione di Simone
> Accanto alla scomposizione: **"Metodo 1 → Uso i fratti semplici"**.

**Metodo 1: identità dei polinomi.** Si fa la somma e si confrontano i coefficienti:

$$\frac as+\frac b{s+1}=\frac{a(s+1)+bs}{s(s+1)}=\frac{(a+b)s+a}{s(s+1)}\stackrel{\text{set}}{=}\frac1{s(s+1)}$$

I coefficienti di $s$ devono essere uguali (a destra $s$ non c'è, quindi il coefficiente è 0) e così i termini noti: $a+b=0$, $a=1$, quindi $b=-1$ e

$$y_F(t)=\mathcal L^{-1}[Y_F(s)]=\mathcal L^{-1}\left[\frac1s-\frac1{s+1}\right]=\delta_{-1}(t)-e^{-t}$$

**Metodo 2: limiti.** Con molti termini il metodo 1 diventa oneroso. Si moltiplica tutto per $s$:

$$\frac{s}{s(s+1)}=\frac{sa}{s}+\frac{sb}{s+1}$$

Per isolare $a$ bisogna far sparire gli altri termini a destra, cioè $\frac{sb}{s+1}$: si pone $s=0$, o più rigorosamente si fa il limite per $s\to0$:

$$\lim_{s\to0}\frac{s}{s(s+1)}=\lim_{s\to0}\frac1{s+1}=\lim_{s\to0}\left(\frac{sa}{s}+\frac{sb}{s+1}\right)=a+\lim_{s\to0}\frac{sb}{s+1}=a$$

e $\lim_{s\to0}\frac1{s+1}=1$, quindi $a=1$. Allo stesso modo per $b$: si moltiplica per $(s+1)$ e si manda $s+1$ a zero, cioè $s\to-1$ (il suo polo):

$$\lim_{s\to-1}\frac{s+1}{s(s+1)}=\lim_{s\to-1}\frac1s=\lim_{s\to-1}\left(\frac{(s+1)a}{s}+\frac{(s+1)b}{s+1}\right)=b\quad\Longrightarrow\quad b=-1$$

> [!warning] Correzione
> Negli appunti, nel calcolo di $b$, gli ultimi due limiti sono scritti $\lim_{s\to0}$: devono essere $\lim_{s\to-1}$, come all'inizio della riga (con $s\to0$ il termine $\frac{(s+1)a}{s}$ non si annullerebbe).

> [!note] Annotazioni di Simone
> A mano: **"Metodo 2 Calcolo i residui di un polo semplice"**, **"s → al suo polo"** e, accanto alla definizione di residuo, **"Visto in AM2"**.

I coefficienti $a$ e $b$ si chiamano **residui**, e le radici dei fattori al denominatore **poli** (qui $0$ e $-1$). D'ora in poi i residui si indicano con $R_1,R_2,\dots$ In generale, per un polo semplice $p_i$:

$$R_i=\lim_{s\to p_i}(s-p_i)F(s)$$

## Residui con denominatori di grado maggiore di 1

> [!note] Annotazione di Simone
> Accanto al titolo: **"Caso polo n ≥ 2"**.

Se il prodotto $W(s)U(s)$ (o $H(s)U(s)$) è del tipo $\frac1{s^2(s+1)}$, si potrebbe pensare di scomporre come

$$\frac1{s^2(s+1)}=\frac{R_1}{s^2}+\frac{R_2}{s+1}$$

$\frac1{s^2(s+1)}$ è strettamente propria, e scomponendola si ottengono sempre funzioni strettamente proprie. Quindi $R_2$ ha grado strettamente minore di quello di $s+1$ (che è 1), cioè è una costante; ma $s^2$ ha grado 2, quindi $R_1$ può avere grado 1:

$$\frac1{s^2(s+1)}=\frac{R_{11}s+R_{12}}{s^2}+\frac{R_2}{s+1}$$

con $R_{11},R_{12}$ costanti. Purtroppo così non si riesce a trovare i singoli $R_{11}$ e $R_{12}$, perché non si può mettere in evidenza un polinomio per poi fare il limite. L'alternativa è scomporre il fattore **una volta per ogni grado di molteplicità**:

$$\frac1{s^2(s+1)}=\frac{R_{11}}{s^2}+\frac{R_{12}}{s}+\frac{R_2}{s+1}$$

(i coefficienti $R_{11},R_{12}$ ora sono diversi da quelli di prima). In generale ogni fattore $(s-p)^m$ produce $m$ termini, uno per ogni potenza da $m$ a 1. Per esempio:

$$\frac1{s^2(s+1)^3(s-3)}=\frac{R_{11}}{s^2}+\frac{R_{12}}{s}+\frac{R_{21}}{(s+1)^3}+\frac{R_{22}}{(s+1)^2}+\frac{R_{23}}{s+1}+\frac{R_3}{s-3}$$

$R_{11}$ si calcola facilmente: moltiplicando per $s^2$ gli altri termini vanno a zero nel limite.

$$R_{11}=\lim_{s\to0}s^2\cdot\frac1{s^2(s+1)}=\lim_{s\to0}\frac1{s+1}=1,\qquad\text{infatti}\quad\lim_{s\to0}\left(R_{11}+sR_{12}+\frac{s^2R_2}{s+1}\right)=R_{11}$$

Lo stesso per $R_2$. Per $R_{12}$ la situazione è diversa: moltiplicando per $s^2$ resta $R_{11}+sR_{12}+\frac{s^2R_2}{s+1}$, e il limite dà solo $R_{11}$. Si può però **derivare**: $R_{11}$ sparisce (è una costante) e $sR_{12}$ diventa $R_{12}$:

$$\lim_{s\to0}\frac{d}{ds}\left[\frac{s^2}{s^2(s+1)}\right]=\lim_{s\to0}\frac{d}{ds}\left[R_{11}+sR_{12}+\frac{s^2R_2}{s+1}\right]=\lim_{s\to0}\left(R_{12}+\frac{2s(s+1)-s^2}{(s+1)^2}R_2\right)=R_{12}$$

Qui $R_{12}=\lim_{s\to0}\frac{d}{ds}\frac1{s+1}=\lim_{s\to0}\frac{-1}{(s+1)^2}=-1$, e $R_2=\lim_{s\to-1}\frac1{s^2}=1$.

> [!note] Annotazioni di Simone
> A mano: **"Soluzione"** (verso la scomposizione per gradi), **"Calcolo i residui"**, **"NOVITÀ!"** (verso la derivata) e **"problema risolto"**.

> [!tip] Verifica
> $\frac1{s^2}-\frac1s+\frac1{s+1}=\frac{(s+1)-s(s+1)+s^2}{s^2(s+1)}=\frac{1}{s^2(s+1)}$ ✔. Antitrasformando: $t-1+e^{-t}$ (per $t\ge0$).

### Un polo triplo

$$F(s)=\frac{s-10}{s^3(s+2)}=\frac{R_{11}}{s^3}+\frac{R_{12}}{s^2}+\frac{R_{13}}{s}+\frac{R_2}{s+2}$$

$R_{11}$: si moltiplica per $s^3$ e si fa il limite per $s\to0$:

$$R_{11}=\lim_{s\to0}\frac{s^3(s-10)}{s^3(s+2)}=\lim_{s\to0}\frac{s-10}{s+2}=-5$$

$R_{12}$: si moltiplica per $s^3$, si deriva e si fa il limite:

$$R_{12}=\lim_{s\to0}\frac{d}{ds}\left[\frac{s-10}{s+2}\right]=\lim_{s\to0}\frac{12}{(s+2)^2}=\frac{12}4=3$$

$R_{13}$: **non basta derivare ancora una volta**. Derivando $F(s)s^3$:

$$\frac{d}{ds}F(s)s^3=\frac{d}{ds}\left(R_{11}+sR_{12}+s^2R_{13}+\frac{s^3R_2}{s+2}\right)=R_{12}+2sR_{13}+\dots$$

(l'ultimo termine va a zero nel limite) e derivando di nuovo

$$\frac{d^2}{ds^2}F(s)s^3=\frac{d}{ds}(R_{12}+2sR_{13}+\dots)=2R_{13}+\dots$$

Non si ottiene $R_{13}$ ma $2R_{13}$, per via delle potenze che "scendono" derivando: bisogna dividere per 2.

$$R_{13}=\frac12\lim_{s\to0}\frac{d^2}{ds^2}\left[\frac{s-10}{s+2}\right]=\frac12\lim_{s\to0}\frac{d}{ds}\left[\frac{12}{(s+2)^2}\right]=\frac12\lim_{s\to0}\left(-\frac{24}{(s+2)^3}\right)=\frac12\cdot\frac{-24}8=-\frac32$$

In generale, **se si deriva $k$ volte si divide per $k!$**. $R_2$ si trova come $R_{11}$:

$$R_2=\lim_{s\to-2}\frac{(s+2)(s-10)}{s^3(s+2)}=\lim_{s\to-2}\frac{s-10}{s^3}=\frac{-12}{-8}=\frac32$$

> [!important] Formula generale dei residui
> Per un polo $p_i$ di molteplicità $m_i$, con scomposizione $\sum_{j=1}^{m_i}\frac{R_{ij}}{(s-p_i)^{m_i-j+1}}$:
> $$R_{ij}=\frac{1}{(j-1)!}\lim_{s\to p_i}\frac{d^{\,j-1}}{ds^{\,j-1}}\Big[(s-p_i)^{m_i}F(s)\Big]$$
> Il libro scrive la stessa formula con la numerazione inversa, $R_{ij}=\lim\frac{1}{(m_i-j)!}\frac{d^{m_i-j}}{ds^{m_i-j}}\big((s-\lambda_i)^{m_i}\Phi(s)\big)$, abbinando $R_{ij}$ a $\frac1{(s-\lambda_i)^j}$. _(libro, §4.2.2, p. 173)_

> [!note] Annotazioni di Simone
> A mano: "Sol banale" ($R_{11}$), "Caso precedente" ($R_{12}$), **"PROBLEMA"** (per $R_{13}$), **"Soluzione!!"** e, accanto alla regola $k!$, **"soluzione definitiva!!"** con la formula $R_{ij}=\frac1{k!}\lim_{s\to\text{polo}}\Big[\frac{d^k}{ds^k}\big(F(s)\cdot s^n\big)\Big]$.

> [!tip] Verifica
> $F(s)$ ha grado relativo 3 (denominatore di grado 4, numeratore di grado 1), quindi nella scomposizione i termini in $\frac1s$ e $\frac1{s+2}$ devono "annullarsi" all'infinito: $R_{13}+R_2=-\frac32+\frac32=0$ ✔. Antitrasformando: $f(t)=-5\frac{t^2}{2}+3t-\frac32+\frac32e^{-2t}$.

## Residui complessi

> [!note] Annotazione di Simone
> Accanto al titolo: **"Stesso Procedimento ma ancora più semplice!!"**.

Il denominatore può avere radici complesse coniugate, per esempio

$$F(s)=\frac{10}{(s+1)(s^2+1)}=\frac{10}{(s+1)(s+j)(s-j)}$$

Il teorema dei residui, così come è stato descritto, non richiede radici reali: funziona anche con radici complesse.

$$F(s)=\frac{R_1}{s+1}+\frac{R_2}{s+j}+\frac{R_3}{s-j}$$

$R_2$ sarà un residuo complesso, e anche $R_3$; in particolare $R_3=R_2^*$, perché i termini al denominatore sono coniugati. C'è quindi un calcolo in meno.

$$R_1=\lim_{s\to-1}(s+1)F(s)=\lim_{s\to-1}\frac{10}{(s+j)(s-j)}=\frac{10}{1+1}=5$$

$$R_2=\lim_{s\to-j}(s+j)F(s)=\lim_{s\to-j}\frac{10}{(s+1)(s-j)}=\frac{10}{(1-j)(-2j)}=\frac{10}{-2j-2}=-\frac5{1+j}$$

$$R_3=R_2^*=-\frac5{1-j}$$

Si antitrasforma termine a termine:

$$\mathcal L^{-1}[F(s)]=\mathcal L^{-1}\left[\frac{R_1}{s+1}\right]+\mathcal L^{-1}\left[\frac{R_2}{s+j}\right]+\mathcal L^{-1}\left[\frac{R_3}{s-j}\right]=R_1e^{-t}+R_2e^{-jt}+R_2^*e^{jt}$$

**Ricombinare in termini reali dopo l'antitrasformata.** Con $R_2=R_{2a}+jR_{2b}$:

$$\begin{aligned}R_2e^{-jt}+R_2^*e^{jt}&=(R_{2a}+jR_{2b})e^{-jt}+(R_{2a}-jR_{2b})e^{jt}=R_{2a}(e^{-jt}+e^{jt})+jR_{2b}(e^{-jt}-e^{jt})\\&=2R_{2a}\underbrace{\frac{e^{jt}+e^{-jt}}{2}}_{\cos t}-2j^2R_{2b}\underbrace{\frac{e^{jt}-e^{-jt}}{2j}}_{\sin t}=2R_{2a}\cos t+2R_{2b}\sin t\end{aligned}$$

**Oppure prima di antitrasformare**, sommando direttamente nel dominio di $s$:

$$F(s)=\frac{R_1}{s+1}+\frac{R_2}{s+j}+\frac{R_2^*}{s-j}=\frac{R_1}{s+1}+\frac{(R_2+R_2^*)s-j(R_2-R_2^*)}{s^2+1}=\frac{R_1}{s+1}+2R_{2a}\frac{s}{s^2+1}+2R_{2b}\frac1{s^2+1}$$

$$\Longrightarrow\ \mathcal L^{-1}[F(s)]=R_1e^{-t}+2R_{2a}\cos t+2R_{2b}\sin t$$

> [!warning] Correzione
> Negli appunti, nella seconda strada, il primo termine è antitrasformato come $R_1e^{t}$: $\mathcal L^{-1}\big[\frac1{s+1}\big]=e^{-t}$, come nella prima strada.

> [!example] Valori numerici
> $R_2=-\frac5{1+j}=-\frac{5(1-j)}{2}=-\frac52+\frac52j$, quindi $R_{2a}=-\frac52$, $R_{2b}=\frac52$ e
> $$f(t)=5e^{-t}-5\cos t+5\sin t$$
> Controllo: $f(0)=5-5=0$, coerente con il fatto che $F(s)$ ha grado relativo 3.

> [!note] Annotazioni di Simone
> A mano: "Si gode!" (per $R_1$), "COMPLESSISSIMO!!" (per $R_2$), "unica differenza da $R_2$" (sul segno di $j$ in $R_3$), "E poi antitrasformo", "di somma termini complessi → di posta somma termini reali", e accanto alle due strade **"procedimento fatto DOPO l'antitrasformata"** e **"procedimento fatto PRIMA dell'antitrasformata"**.

Il caso più complicato che può capitare è quello di radici complesse con molteplicità maggiore di 1:

$$F(s)=\frac{10}{(s+1)(s+j)^3(s-j)^3}$$

che si sviluppa come visto per il caso reale (con le derivate).

> [!quote] Dal libro — i termini complessi senza numeri complessi
> Il libro propone anche di non calcolare il residuo complesso: si scrive il termine della coppia come $\frac{L_as+L_b}{(s-\alpha)^2+\omega^2}$ e si trovano $L_a$, $L_b$ valutando l'uguaglianza in $2c$ valori di $s$ che non annullano il denominatore (sistema lineare). Poi $R_a=\frac{L_a}{2}$ e $R_b=-\frac{L_a\alpha+L_b}{2\omega}$. _(libro, §4.2.1, p. 169)_

## Esempio di antitrasformazione

$$F(s)=\frac{2}{(s+1)^2(s+2)}=\frac{R_{11}}{(s+1)^2}+\frac{R_{12}}{s+1}+\frac{R_2}{s+2}$$

$$R_{11}=\lim_{s\to-1}(s+1)^2F(s)=\lim_{s\to-1}\frac2{s+2}=2$$

$$R_{12}=\lim_{s\to-1}\frac{d}{ds}(s+1)^2F(s)=\lim_{s\to-1}\frac{d}{ds}\frac2{s+2}=\lim_{s\to-1}\left(-\frac2{(s+2)^2}\right)=-2$$

$$R_2=\lim_{s\to-2}(s+2)F(s)=\lim_{s\to-2}\frac2{(s+1)^2}=2$$

$$\mathcal L^{-1}[F(s)]=\mathcal L^{-1}\left[\frac2{(s+1)^2}-\frac2{s+1}+\frac2{s+2}\right]$$

$\mathcal L^{-1}\big[-\frac2{s+1}\big]=-2e^{-t}$ e $\mathcal L^{-1}\big[\frac2{s+2}\big]=2e^{-2t}$. Il primo termine non è immediato: è $\frac1{s^2}$ traslato di 1. Si usa la **traslazione complessa** $\mathcal L[e^{at}f(t)]=F(s-a)$, qui con $a=-1$:

$$2\,\mathcal L^{-1}\left[\frac1{(s+1)^2}\right]=2e^{-t}\,\mathcal L^{-1}\left[\frac1{s^2}\right]=2e^{-t}\,t\,\delta_{-1}(t)$$

In generale: se si riconosce una funzione di $s$ in cui al posto di $s$ c'è $s$ **traslato**, basta moltiplicare per l'esponenziale. Il risultato è

$$f(t)=\big(2te^{-t}-2e^{-t}+2e^{-2t}\big)\,\delta_{-1}(t)$$

> [!warning] Correzione
> Gli appunti scrivono "sappiamo che $\mathcal L[\delta_{-1}(t)]=\frac1{s^2}$" e quindi $2\mathcal L^{-1}\big[\frac1{(s+1)^2}\big]=2e^{-t}\delta_{-1}(t)$. Ma $\mathcal L[\delta_{-1}(t)]=\frac1s$: è la **rampa** $t$ ad avere trasformata $\frac1{s^2}$ (vedi la [[15 - TDS - Trasformata di Laplace#Trasformate di alcune funzioni|tabella]]). Il termine corretto è $2te^{-t}$, ed è proprio il tipo di modo ($te^{\lambda t}$) che comparirà con le matrici non diagonalizzabili. Verifica: $f(0)=-2+2=0$ e $\dot f(0)=2+2-4=0$, coerenti con il grado relativo 3 di $F(s)$.

## Calcolo di $e^{At}$ con l'antitrasformata

Vedi [[TDS - Esponenziale di matrice]].

Un sistema fisico semplice: una molla $k$ e uno smorzatore $b$ che sorreggono una massa $M$ (per esempio un'automobile). Il sistema è

$$\dot x=\begin{pmatrix}0&1\\-\frac kM&-\frac bM\end{pmatrix}x+\begin{pmatrix}\frac1M\\0\end{pmatrix}u,\qquad y=\begin{pmatrix}1&0\end{pmatrix}x$$

e con $M=1$, $k=2$, $b=3$:

$$\dot x=\begin{pmatrix}0&1\\-2&-3\end{pmatrix}x+\begin{pmatrix}1\\0\end{pmatrix}u$$

> [!warning] Correzione
> Con stato $x=(h,\dot h)$ la forza entra nell'equazione della **velocità**, quindi $B=\begin{psmallmatrix}0\\1/M\end{psmallmatrix}$, come nell'[[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Esempio fisico di applicazione|esempio della lezione 9]]. Per il calcolo di $e^{At}$ qui sotto $B$ non interviene, quindi il risultato non cambia; cambierebbe invece $W(s)$ nell'esercizio proposto.

Per esercizio (proposto negli appunti): calcolare $W(s)$; $y_F(t)$ con $u(t)=\delta_{-1}(t)$, cioè quando la macchina prende una "botta", uno scalino; $y_F(t)$ con $u(t)=\sin2t$, che rappresenta la macchina su un terreno con dei dossi.

Sappiamo che $\Phi(s)=\mathcal L[\Phi(t)]=\mathcal L[e^{At}]$, quindi

$$e^{At}=\mathcal L^{-1}\big[(sI-A)^{-1}\big]=\mathcal L^{-1}\left[\begin{pmatrix}s&-1\\2&s+3\end{pmatrix}^{-1}\right]=\mathcal L^{-1}\left[\frac{\begin{pmatrix}s+3&1\\-2&s\end{pmatrix}}{(s+1)(s+2)}\right]$$

Si procede esattamente come con i numeri al numeratore, calcolando i residui:

$$\frac{\begin{pmatrix}s+3&1\\-2&s\end{pmatrix}}{(s+1)(s+2)}=\frac{R_1}{s+1}+\frac{R_2}{s+2}$$

L'unica differenza è che, con una matrice $2\times2$ al numeratore, anche i residui sono **matrici** $2\times2$: prevedibile, perché si sta trovando $e^{At}$, che è una matrice $2\times2$.

$$R_1=\lim_{s\to-1}(s+1)\frac{\begin{pmatrix}s+3&1\\-2&s\end{pmatrix}}{(s+1)(s+2)}=\frac{\begin{pmatrix}2&1\\-2&-1\end{pmatrix}}{1}=\begin{pmatrix}2&1\\-2&-1\end{pmatrix},\qquad R_2=\lim_{s\to-2}(s+2)\frac{\begin{pmatrix}s+3&1\\-2&s\end{pmatrix}}{(s+1)(s+2)}=\frac{\begin{pmatrix}1&1\\-2&-2\end{pmatrix}}{-1}=\begin{pmatrix}-1&-1\\2&2\end{pmatrix}$$

$$e^{At}=\mathcal L^{-1}\left[\frac{R_1}{s+1}\right]+\mathcal L^{-1}\left[\frac{R_2}{s+2}\right]=\begin{pmatrix}2&1\\-2&-1\end{pmatrix}e^{-t}+\begin{pmatrix}-1&-1\\2&2\end{pmatrix}e^{-2t}$$

Il procedimento non cambia con scalari o matrici. Non solo: dalla forma di $e^{At}$ si leggono **autovalori e modi naturali**. Sappiamo che

$$e^{At}=e^{\lambda_1t}u_1v_1'+e^{\lambda_2t}u_2v_2'$$

quindi gli autovalori sono $\lambda_1=-1$ e $\lambda_2=-2$, e i residui sono proprio i prodotti $u_iv_i'$: matrici $n\times n$ di **rango 1** (prodotto di un $n\times1$ per un $1\times n$). In effetti $\begin{psmallmatrix}2&1\\-2&-1\end{psmallmatrix}$ e $\begin{psmallmatrix}-1&-1\\2&2\end{psmallmatrix}$ hanno rango 1:

$$u_1v_1'=\begin{pmatrix}2&1\\-2&-1\end{pmatrix},\qquad u_2v_2'=\begin{pmatrix}-1&-1\\2&2\end{pmatrix}$$

> [!tip] Verifica
> $R_1+R_2=I$ (perché $e^{A\cdot0}=I$), e $-R_1-2R_2=\begin{psmallmatrix}0&1\\-2&-3\end{psmallmatrix}=A$ (la derivata in 0). Si riconosce anche $u_1=\begin{psmallmatrix}1\\-1\end{psmallmatrix}$, $v_1'=(2\ \ 1)$: infatti $A u_1=\begin{psmallmatrix}-1\\1\end{psmallmatrix}=-u_1$.

> [!note] Annotazioni di Simone
> Accanto ai residui: "$=u_1v_1'$", "$=u_2v_2'$", "Visti a fine pagina", "$u_iv_i'$ è una matrice 2×2", "Si vedono subito gli autovalori"; in fondo alla lezione: **"Perciò, calcolando $e^{At}=\Phi$ in $s$, i residui sono $uv'$ e antitrasformando troviamo anche gli autovalori."**

> [!quote] Dal libro — residui e forma spettrale
> Nel caso di operatore regolare, $\Phi(s)=\sum_i\frac{R_i}{s-\lambda_i}+\sum_k\Big(\frac{\tilde R_k}{s-\alpha_k-j\omega_k}+\frac{\tilde R_k^*}{s-\alpha_k+j\omega_k}\Big)$, e dal confronto con la forma spettrale del Capitolo 2:
> $$R_i=\sum_{l=1}^{\mu_i}u_{il}v_{il}'$$
> "Il rango di $R_i$ permette di determinare la molteplicità geometrica dell'autovalore reale", cioè il numero di blocchi di Jordan di dimensione 1 associati. Nell'Esempio 4.2.1 ($A=\begin{psmallmatrix}-1&1\\0&-2\end{psmallmatrix}$) il libro trova allo stesso modo $R_1=\begin{psmallmatrix}1&1\\0&0\end{psmallmatrix}$, $R_2=\begin{psmallmatrix}0&-1\\0&1\end{psmallmatrix}$ e $\Phi(t)=R_1e^{-t}+R_2e^{-2t}$. Nell'Esempio 4.2.2 ($A=-I$) invece $\Phi(s)=\frac1{s+1}I$: il denominatore è di grado 1, **minore** di $n=2$, perché l'autovalore doppio ha ordine geometrico 1. _(libro, §4.2.1, pp. 167–171)_

> [!quote] Dal libro — un'anteprima del caso non diagonalizzabile
> Esempio 4.2.4: $A=\begin{psmallmatrix}-1&1\\0&-1\end{psmallmatrix}$ ha l'autovalore $-1$ doppio con un solo autovettore. Allora
> $$\Phi(s)=\frac1{s+1}I+\frac1{(s+1)^2}\begin{pmatrix}0&1\\0&0\end{pmatrix}\quad\Longrightarrow\quad\Phi(t)=e^{-t}I+te^{-t}\begin{pmatrix}0&1\\0&0\end{pmatrix}$$
> Compare la legge $te^{-t}$: è il caso in cui $A$ non è diagonalizzabile, trattato nella [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori|prossima lezione]]. Con l'antitrasformata lo si ottiene "gratis", senza conoscere la struttura degli autovettori. _(libro, §4.2.2, p. 174)_
