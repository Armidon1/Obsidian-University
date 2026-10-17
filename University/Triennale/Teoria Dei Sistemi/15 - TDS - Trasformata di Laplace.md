---
title: Trasformata di Laplace
aliases:
  - TDS — Trasformata di Laplace
tags:
  - teoria-dei-sistemi
  - trasformata-di-laplace
  - funzione-di-trasferimento
  - dominio-complesso
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 70–76); libro Monaco et al., §4.1
---

# Trasformata di Laplace

> [!abstract] Scopo della lezione
> Finora l'evoluzione forzata richiedeva l'**integrale di convoluzione**, lungo e spesso difficile per ingressi qualsiasi. Si cambia **dominio**: dal tempo $t$ alla variabile complessa $s$, con la **trasformata di Laplace**. In questo dominio:
> - le equazioni differenziali diventano equazioni **algebriche**: $X(s)=(sI-A)^{-1}x_0+(sI-A)^{-1}BU(s)$;
> - le matrici della forma esplicita diventano $\Phi(s)=(sI-A)^{-1}$, $H(s)$, $\Psi(s)$ e $W(s)$ (la **funzione di trasferimento**);
> - la convoluzione diventa un **prodotto**.
>
> Si calcolano le trasformate delle funzioni che servono (esponenziali, seni, coseni, potenze) e si osserva che sono tutte **razionali strettamente proprie**. Per tornare nel tempo servono le antitrasformate: [[16 - TDS - Antitrasformate e residui]]. Indice: [[MOC - Teoria dei Sistemi]].

> [!note] Annotazione di Simone
> In testa alla lezione, a mano in rosso: **"TRASFORMATE CONTINUE"**.

## Ingressi non impulsivi e trasformata di Laplace

Vedi [[TDS - Trasformata di Laplace]].

Abbiamo visto come si comporta un sistema lineare con ingresso impulsivo $u(t)=\delta(t)$ (nel caso scalare). La forma esplicita è

$$\begin{cases}x(t)=\Phi(t-t_0)x(t_0)+\displaystyle\int_{t_0}^{t}H(t-\tau)u(\tau)\,d\tau\\[2mm]y(t)=\Psi(t-t_0)x(t_0)+\displaystyle\int_{t_0}^{t}W(t-\tau)u(\tau)\,d\tau\end{cases}$$

Vorremmo però vedere come si comporta il sistema con un ingresso qualsiasi, per esempio $u(t)=t^2$. L'integrale può essere semplice se $H$ e $W$ sono scalari, altrimenti va fatto per ogni elemento di $H$ e $W$ (funzioni del tempo): spesso è difficile, o comunque lungo e macchinoso. Cerchiamo allora una **trasformazione** che permetta di lavorare sull'ingresso senza passare per l'integrale di convoluzione (grazie a un teorema detto **teorema della convoluzione**).

L'idea è **cambiare dominio**: passare dal tempo $t$ a una variabile $s$ che non ha un significato fisico diretto, ma che semplifica i calcoli. Si trasforma il problema in "qualcosa di più semplice", lo si risolve lì e si torna indietro con la trasformazione inversa. La corrispondenza è biunivoca:

$$t\longleftrightarrow s,\qquad f(t)\longleftrightarrow F(s)$$

Questa trasformazione è la **trasformata di Laplace**:

$$\mathcal L[f(t)]=F(s)=\int_0^{+\infty}f(t)\,e^{-st}\,dt$$

L'integrale è in $t$: calcolato da 0 a $+\infty$, rimane solo la variabile $s$. Attenzione: $t\in\mathbb R$, ma $s\in\mathbb C$. Il passaggio inverso si farebbe con un integrale nel dominio complesso, che in questo corso non si vede: si procederà in altri modi.

La $f(t)$ dentro l'integrale è definita solo per $t\in[0,+\infty)$, non per tempi negativi. Altrimenti la si può pensare moltiplicata per il **gradino** $\delta_{-1}(t)$, l'integrale dell'impulso $\delta(t)$:

$$\delta_{-1}(t)=\int\delta(t)\,dt$$

![[TDS-L15-01.png]]

Il gradino vale 0 per $t<0$ e 1 per $t\ge0$ (pallino pieno in $t=0$), quindi

$$f(t)\,\delta_{-1}(t)=\begin{cases}f(t)&t\ge0\\0&t<0\end{cases}$$

> [!note] Notazione
> L'impulso si indica spesso con $\delta_0(t)$; ogni integrazione abbassa l'indice di uno: $\delta_{-1}$ è il gradino (integrale di $\delta_0$), $\delta_{-2}$ la rampa, e così via. Sono gli **ingressi canonici** già incontrati in [[04 - TDS - Uscita forzata e dalla forma esplicita alla implicita#Uscita forzata|lezione 4]].

### Linearità

La trasformata di Laplace è **lineare**:

$$\mathcal L[\alpha f(t)+\beta g(t)]=\int_0^{+\infty}\big(\alpha f(t)+\beta g(t)\big)e^{-st}\,dt=\alpha\int_0^{+\infty}f(t)e^{-st}\,dt+\beta\int_0^{+\infty}g(t)e^{-st}\,dt=\alpha\mathcal L[f(t)]+\beta\mathcal L[g(t)]$$

Quindi la struttura lineare del sistema si conserva, supponendo di poter calcolare la trasformata:

$$\begin{cases}\dot x(t)=Ax(t)+Bu(t)\\y(t)=Cx(t)+Du(t)\end{cases}\Longrightarrow\begin{cases}\mathcal L[\dot x(t)]=\mathcal L[Ax(t)+Bu(t)]=A\mathcal L[x(t)]+B\mathcal L[u(t)]\\\mathcal L[y(t)]=\mathcal L[Cx(t)+Du(t)]\end{cases}$$

### Trasformata della derivata

Applicando la definizione a $\dot x$ e integrando per parti (IPP):

$$\mathcal L[\dot x(t)]=\int_0^{+\infty}\dot x(t)e^{-st}\,dt\stackrel{\text{IPP}}{=}\Big[x(t)e^{-st}\Big]_0^{+\infty}-\int_0^{+\infty}(-s)\,x(t)e^{-st}\,dt$$

Il termine $\big[x(t)e^{-st}\big]_0^{+\infty}$ potrebbe non essere finito. Con $s=\alpha+j\omega$, $e^{-st}=e^{-\alpha t}e^{-j\omega t}$: il fattore $e^{-j\omega t}$ ha modulo 1 (gira sulla circonferenza unitaria, non converge ma è limitato), quindi $e^{-st}\to0$ solo se $\alpha>0$, cioè $\mathrm{Re}(s)>0$. Assumendo che $x(t)$ non diverga e $\mathrm{Re}(s)>0$:

$$\mathcal L[\dot x(t)]=-x(0)+s\int_0^{+\infty}x(t)e^{-st}\,dt=s\mathcal L[x(t)]-x(0)$$

> [!note] Precisazione: l'ascissa di convergenza
> Se $x(t)$ cresce (per esempio come $e^{2t}$), il termine di bordo si annulla lo stesso, purché $\mathrm{Re}(s)$ sia **maggiore** del tasso di crescita di $x$. Il libro lo formalizza: a ogni $f(t)$ è associato un numero reale $\alpha_f$, l'**ascissa di convergenza**, e la trasformata è definita nel semipiano $\mathrm{Re}(s)>\alpha_f$. Il risultato, il **teorema della derivata** $\mathcal L\big[\frac{d}{dt}f(t)\big]=sF(s)-f(0)$, vale con la stessa ascissa di convergenza. _(libro, §4.1, p. 160)_

### Il sistema nel dominio di Laplace

Ora abbiamo due espressioni di $\mathcal L[\dot x(t)]$, che possiamo uguagliare:

$$\mathcal L[\dot x(t)]=A\mathcal L[x(t)]+B\mathcal L[u(t)]=s\mathcal L[x(t)]-x(0)$$

Con $X(s):=\mathcal L[x(t)]$ e $U(s):=\mathcal L[u(t)]$:

$$sX(s)-x(0)=AX(s)+BU(s)$$

(attenzione alla variabile: se è $s$, siamo nel dominio della trasformata). Riordinando:

$$sX(s)-AX(s)=x(0)+BU(s)\ \Longrightarrow\ (sI-A)X(s)=x(0)+BU(s)\ \Longrightarrow\ X(s)=(sI-A)^{-1}x(0)+(sI-A)^{-1}BU(s)$$

e, con $Y(s):=\mathcal L[y(t)]$,

$$\begin{cases}X(s)=(sI-A)^{-1}x(0)+(sI-A)^{-1}BU(s)\\Y(s)=CX(s)+DU(s)\end{cases}$$

Le espressioni sono ancora lineari: nella prima, $(sI-A)^{-1}$ moltiplica la condizione iniziale e $(sI-A)^{-1}B$ moltiplica l'ingresso. L'equazione **differenziale** è diventata **algebrica**.

> [!tip] L'identità $I$
> Si scrive $sI-A$ e non $s-A$: $s$ è uno scalare e $A$ una matrice, quindi bisogna moltiplicare $s$ per l'identità per poterli sottrarre.

## Trasformate delle matrici della forma esplicita

Vedi [[TDS - Funzione di trasferimento]].

La forma ottenuta ricorda la forma esplicita. Trasformiamo direttamente quest'ultima:

$$\mathcal L[x(t)]=\mathcal L\left[\Phi(t)x(0)+\int_0^tH(t-\tau)u(\tau)\,d\tau\right]\ \Longrightarrow\ X(s)=\Phi(s)x(0)+\mathcal L\left[\int_0^tH(t-\tau)u(\tau)\,d\tau\right]$$

con $\Phi(s):=\mathcal L[\Phi(t)]$. L'integrale $\int_{t_0}^tH(t-\tau)u(\tau)\,d\tau$ si chiama **integrale di convoluzione** e si indica spesso con $(H*u)(t)$; per ora non sappiamo trasformarlo. Ma confrontando le due espressioni di $X(s)$, il coefficiente di $x(0)$ è $(sI-A)^{-1}$ nella prima e $\Phi(s)$ nella seconda, quindi

$$\boxed{\Phi(s)=(sI-A)^{-1}}$$

Inoltre $H(t)=\Phi(t)B$, quindi $\mathcal L[H(t)]=\mathcal L[\Phi(t)B]=\Phi(s)B$:

$$H(s)=\Phi(s)B=(sI-A)^{-1}B$$

che è proprio il coefficiente di $U(s)$. Si arriva quindi a

$$X(s)=\Phi(s)x_0+H(s)U(s)$$

**Dall'integrale si è passati al prodotto**, molto più facile da trattare. Lo stesso per l'uscita:

$$Y(s)=CX(s)+DU(s)=C\Phi(s)x_0+CH(s)U(s)+DU(s)=\underbrace{C\Phi(s)}_{\Psi(s)}x_0+\underbrace{\big(CH(s)+D\big)}_{W(s)}U(s)$$

> [!note] Annotazioni di Simone
> A margine, a mano: **"INGRESSO"** accanto alle formule di $\Phi(s)$, $H(s)$, $X(s)$, e **"USCITA"** accanto a quella di $Y(s)$.

$\Psi(s)=\mathcal L[\Psi(t)]=\mathcal L[C\Phi(t)]=C\Phi(s)$. Per $W(s)$ non è ovvio che coincida con $\mathcal L[W(t)]$, perché $W(t)=CH(t)+D\delta(t)$: serve la trasformata dell'impulso, che deve valere 1. Infatti, per la proprietà di campionamento dell'impulso

$$\int_a^b\delta(t-k)f(t)\,dt=\begin{cases}f(k)&k\in[a,b]\\0&k\notin[a,b]\end{cases}$$

con $k=0\in[0,+\infty)$:

$$\mathcal L[\delta(t)]=\int_0^{+\infty}\delta(t)e^{-st}\,dt=e^{-s\cdot0}=1$$

Quindi

$$\mathcal L[W(t)]=\mathcal L[C\Phi(t)B+D\delta(t)]=C\mathcal L[\Phi(t)]B+D\mathcal L[\delta(t)]=C\Phi(s)B+D=:W(s)$$

| Tempo | Laplace |
|---|---|
| $\Phi(t)=e^{At}$ | $\Phi(s)=(sI-A)^{-1}$ |
| $H(t)=e^{At}B$ | $H(s)=(sI-A)^{-1}B$ |
| $\Psi(t)=Ce^{At}$ | $\Psi(s)=C(sI-A)^{-1}$ |
| $W(t)=Ce^{At}B+D\delta(t)$ | $W(s)=C(sI-A)^{-1}B+D$ |

> [!quote] Dal libro — funzione di trasferimento e teorema della convoluzione
> Per un sistema con $q$ uscite e $p$ ingressi, $W(s)$ ha dimensioni $q\times p$ ed è detta **matrice delle funzioni di trasferimento** o semplicemente **funzione di trasferimento**. Dal confronto delle due espressioni segue che $\mathcal L\big[\int_0^tW(t-\tau)u(\tau)d\tau\big]=W(s)U(s)$: è il **teorema della convoluzione**, $\mathcal L[f_1*f_2]=F_1(s)F_2(s)$. Nel caso di un ingresso e un'uscita, $W(s)=Y_f(s)/U(s)$: "l'operazione di deconvoluzione si riduce alla divisione". _(libro, §4.1, pp. 162–164)_

Ottenute le espressioni trasformate, bisogna saper **tornare indietro**: studiando per esempio l'uscita forzata con la trasformata si ottiene $Y_F(s)$, ma serve $y_F(t)$. Bisogna calcolare le **antitrasformate**, senza passare per l'integrale complesso.

> [!note] Annotazione di Simone
> Accanto a questa frase, a mano: **"OBBIETTIVO"**.

## Trasformate di alcune funzioni

Vediamo le trasformate delle funzioni più comuni, come quelle che compaiono nei modi naturali (esponenziali, seni, coseni); serviranno a capire come antitrasformare.

**Esponenziale.**

$$\mathcal L[e^{at}]=\int_0^{+\infty}e^{at}e^{-st}\,dt=\int_0^{+\infty}e^{-(s-a)t}\,dt=\left[\frac{e^{-(s-a)t}}{-(s-a)}\right]_0^{+\infty}=\frac{1}{s-a}$$

Essendo $s\in\mathbb C$, per la convergenza deve essere $\mathrm{Re}(s-a)>0$, cioè $\mathrm{Re}(s)>\mathrm{Re}(a)$; vale per qualsiasi $a\in\mathbb C$.

**Seno e coseno**, dalle formule di Eulero e dalla linearità:

$$\mathcal L[\sin\omega t]=\mathcal L\left[\frac{e^{j\omega t}-e^{-j\omega t}}{2j}\right]=\frac{1}{2j}\left(\frac{1}{s-j\omega}-\frac{1}{s+j\omega}\right)=\frac{1}{2j}\cdot\frac{2j\omega}{s^2+\omega^2}=\frac{\omega}{s^2+\omega^2}$$

$$\mathcal L[\cos\omega t]=\mathcal L\left[\frac{e^{j\omega t}+e^{-j\omega t}}{2}\right]=\frac12\left(\frac{1}{s-j\omega}+\frac{1}{s+j\omega}\right)=\frac12\cdot\frac{2s}{s^2+\omega^2}=\frac{s}{s^2+\omega^2}$$

valide per $\mathrm{Re}(s)>0$ (qui $a=\pm j\omega$ ha parte reale nulla).

**Gradino.**

$$\mathcal L[\delta_{-1}(t)]=\int_0^{+\infty}1\cdot e^{-st}\,dt=\left[\frac{e^{-st}}{-s}\right]_0^{+\infty}=\frac1s\qquad(\mathrm{Re}(s)>0)$$

**Potenze di $t$.** Sono utili, per esempio, per trasformare le approssimazioni di Taylor di una funzione, addendo per addendo. Per parti:

$$\mathcal L[t]=\int_0^{+\infty}te^{-st}\,dt\stackrel{\text{IPP}}{=}\left[\frac{te^{-st}}{-s}\right]_0^{+\infty}-\int_0^{+\infty}1\cdot\frac{e^{-st}}{-s}\,dt=\frac1s\int_0^{+\infty}e^{-st}\,dt=\frac1s\cdot\frac1s=\frac1{s^2}$$

(l'ultimo integrale è quello calcolato per il gradino). In generale conviene trasformare $\frac{t^k}{k!}$: integrando per parti si scende di un grado,

$$\mathcal L\left[\frac{t^k}{k!}\right]=\left[\frac{t^ke^{-st}}{-s\,k!}\right]_0^{+\infty}-\int_0^{+\infty}\frac{t^{k-1}}{(k-1)!}\cdot\frac{e^{-st}}{-s}\,dt=\frac1s\,\mathcal L\left[\frac{t^{k-1}}{(k-1)!}\right]$$

e quindi, iterando, $\mathcal L\big[\frac12t^2\big]=\frac1s\mathcal L[t]=\frac1{s^3}$ e in generale

$$\mathcal L\left[\frac{t^k}{k!}\right]=\frac{1}{s^{k+1}}$$

| $f(t)$ | $F(s)$ | Condizioni |
|---|---|---|
| $\delta(t)$ | $1$ | |
| $e^{at}$ | $\dfrac1{s-a}$ | $\mathrm{Re}(s)>\mathrm{Re}(a)$ |
| $\sin\omega t$ | $\dfrac{\omega}{s^2+\omega^2}$ | $\mathrm{Re}(s)>0$ |
| $\cos\omega t$ | $\dfrac{s}{s^2+\omega^2}$ | $\mathrm{Re}(s)>0$ |
| $\delta_{-1}(t)$ | $\dfrac1s$ | $\mathrm{Re}(s)>0$ |
| $t$ | $\dfrac1{s^2}$ | $\mathrm{Re}(s)>0$ |
| $\dfrac{t^k}{k!}$ | $\dfrac1{s^{k+1}}$ | $\mathrm{Re}(s)>0$ |

### Traslazione nel dominio complesso

Per l'esponenziale vale la proprietà $\mathcal L[e^{at}f(t)]=F(s-a)$, perché (ponendo $\vartheta=s-a$)

$$\mathcal L[e^{at}f(t)]=\int_0^{+\infty}e^{at}f(t)e^{-st}\,dt=\int_0^{+\infty}f(t)e^{-\overbrace{(s-a)}^{\vartheta}t}\,dt=\int_0^{+\infty}f(t)e^{-\vartheta t}\,dt=F(\vartheta)=F(s-a)$$

> [!note] Annotazione di Simone
> Accanto alla formula, a mano: **"Traslazione Complessa"**.

Con questa proprietà si trasformano subito i modi pseudoperiodici:

$$\mathcal L[e^{at}\sin\omega t]=\frac{\omega}{(s-a)^2+\omega^2},\qquad\mathcal L[e^{at}\cos\omega t]=\frac{s-a}{(s-a)^2+\omega^2}$$

## Cenni sulle antitrasformate

Vedi [[TDS - Antitrasformata e residui]].

Nella tabella le trasformate sono tutte **funzioni razionali strettamente proprie**: il denominatore ha grado strettamente maggiore del numeratore (a parte $\delta(t)$, che non è una vera funzione). In genere bisognerà antitrasformare

$$\Phi(s)=(sI-A)^{-1}=\mathcal L[\Phi(t)]=\mathcal L[e^{At}]\qquad\Longrightarrow\qquad\mathcal L^{-1}\big[(sI-A)^{-1}\big]=e^{At}$$

Questo permetterà di calcolare $e^{At}$ **senza passare per autovalori, autovettori e molteplicità**: basta calcolare $sI-A$, invertirla e antitrasformare. La matrice è

$$sI-A=\begin{pmatrix}s-a_{11}&-a_{12}&\cdots&-a_{1n}\\-a_{21}&s-a_{22}&\cdots&-a_{2n}\\\vdots&\vdots&\ddots&\vdots\\-a_{n1}&-a_{n2}&\cdots&s-a_{nn}\end{pmatrix}$$

e la sua inversa è la **matrice aggiunta trasposta** divisa per il determinante:

$$(sI-A)^{-1}=\frac{\mathrm{adj}(sI-A)}{\det(sI-A)}$$

Ogni elemento dell'aggiunta è (a meno del segno) il determinante di una sottomatrice $(n-1)\times(n-1)$, quindi un polinomio di grado al più $n-1$; il determinante $\det(sI-A)$ è il polinomio caratteristico, di grado $n$. Quindi $(sI-A)^{-1}$ è una matrice di funzioni razionali **strettamente proprie**, e lo sono anche $\Psi(s)=C\Phi(s)$ e $H(s)=\Phi(s)B$. Invece $W(s)=C\Phi(s)B+D$ è una somma: la prima parte è strettamente propria, ma aggiungendo $D$ diventa una funzione razionale **propria** (non strettamente).

> [!quote] Dal libro — poli, zeri e polinomio minimo
> - Le radici del numeratore di una funzione razionale sono gli **zeri**, quelle del denominatore i **poli**. I poli di $W(s)$ coincidono con gli autovalori dei modi **eccitabili e osservabili**: "i poli sono un sottoinsieme degli autovalori e corrispondono ai modi che sono simultaneamente eccitabili ed osservabili".
> - Il minimo comune multiplo dei denominatori di $\Phi(s)$ è il **polinomio minimo** $m(s)$: contiene tutti gli autovalori, ciascuno con molteplicità pari al suo **ordine** (la dimensione del blocco di Jordan più grande), mentre il polinomio caratteristico ha la molteplicità algebrica. Moltiplicando per $C$ e $B$ possono avvenire **cancellazioni**: i denominatori di $H(s)$, $\Psi(s)$, $W(s)$ contengono solo gli autovalori eccitabili, osservabili, ed eccitabili e osservabili.
> - $W(s)$ è strettamente propria se e solo se $D=0$: è la traccia, nel dominio complesso, della stretta causalità del legame ingresso-uscita. _(libro, §4.1–4.2, pp. 163–166)_

> [!example] Dal libro — Esempio 4.1.1
> $A=\begin{psmallmatrix}-1&0&1\\-1&1&2\\0&0&-2\end{psmallmatrix}$, $B=\begin{psmallmatrix}1\\1\\0\end{psmallmatrix}$, $C=(1\ 0\ 1)$. Si trova
> $$H(s)=\begin{pmatrix}\frac1{s+1}\\\frac{s}{s^2-1}\\0\end{pmatrix},\qquad\Psi(s)=\begin{pmatrix}\frac1{s+1}&0&\frac{s}{(s+1)(s+2)}\end{pmatrix},\qquad W(s)=\frac1{s+1}$$
> I modi di $-1$ e $1$ sono eccitabili, quelli di $-1$ e $-2$ osservabili, e $W(s)$ contiene solo $-1$, l'unico eccitabile e osservabile: "il modello forzato del sistema in oggetto non raccoglie tutte le informazioni relative al comportamento dinamico". Con $x_0=(0\ 0\ 1)'$ e $u=\delta_{-1}$: $Y_l(s)=-\frac1{s+1}+\frac2{s+2}$, $Y_f(s)=\frac1s-\frac1{s+1}$, quindi $y_l(t)=(2e^{-2t}-e^{-t})\delta_{-1}(t)$ e $y_f(t)=(1-e^{-t})\delta_{-1}(t)$. _(libro, §4.1, pp. 164–165)_

> [!warning] Correzione
> Nel libro, alla fine dell'Esempio 4.1.1, l'evoluzione libera è stampata come $y_l(t)=(e^{-2t}-e^{-t})\delta_{-1}(t)$; antitrasformando $Y_l(s)=-\frac1{s+1}+\frac2{s+2}$ il coefficiente di $e^{-2t}$ è **2**, come scritto sopra (e infatti $y_l(0)=Cx_0=1$).
