---
title: Matrici non diagonalizzabili e catene di autovettori
aliases:
  - TDS — Matrici non diagonalizzabili e catene di autovettori
tags:
  - teoria-dei-sistemi
  - forma-di-jordan
  - autovettori-generalizzati
  - modi-naturali
  - esponenziale-di-matrice
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 85–92); libro Monaco et al., §2.2.2, §4.2.2, Appendice A.2
---

# Matrici non diagonalizzabili e catene di autovettori

> [!abstract] Scopo della lezione
> Finora si è sempre supposto che $A$ fosse **regolare** (diagonalizzabile). Qui si toglie questa ipotesi:
> 1. si guarda cosa dice $\Phi(s)=(sI-A)^{-1}$ nel caso regolare: poli **semplici**, con residui di rango pari alla molteplicità; se dopo le semplificazioni restano poli **multipli**, $A$ non è diagonalizzabile;
> 2. nel caso non regolare si costruiscono le **catene di autovettori generalizzati** e la **forma di Jordan**;
> 3. si calcola l'**esponenziale dei blocchi di Jordan**: compaiono termini $te^{\lambda t}$, $\frac{t^2}{2}e^{\lambda t}$, …;
> 4. molteplicità algebrica, geometrica e **indice** (ordine) geometrico: quanti vettori, quante catene, quanto è lunga la più lunga.
>
> Completa lo studio di [[05 - TDS - Calcolo dell'esponenziale di matrice]] e [[06 - TDS - Modi naturali]], usando gli strumenti di [[16 - TDS - Antitrasformate e residui]]. Segue [[18 - TDS - Trasformata Zeta]]. Indice: [[MOC - Teoria dei Sistemi]].

> [!note] Annotazione di Simone
> In testa alla lezione, a mano in viola: **"REGOLARITÀ"**.

## Studio di $\Phi(s)$ nel caso regolare

Dalle scorse lezioni

$$\Phi(s)=\mathcal L[\Phi(t)]=\mathcal L[e^{At}]=(sI-A)^{-1}\iff e^{At}=\mathcal L^{-1}[\Phi(s)]$$

Per studiare $e^{At}$ ci sono due strade: calcolarla in $t$, seguendo tutta la geometria che c'è dietro (diagonalizzazione, calcolo di $e^{\Lambda t}$, prodotti di matrici), oppure trovarla in $s$, invertendo $sI-A$ e antitrasformando. **Domanda**: si vedono tutte le informazioni di $e^{At}$ anche in $\Phi(s)$?

> [!note] Annotazioni di Simone
> A margine: **"2 Modi per calcolare $e^{At}$"**, **"DOMANDA"**, **"IMPORTANTE PREMESSA CHE ABBIAMO FATTO FINO A ORA"** e, accanto a $A=U\Lambda U^{-1}$, **"Definizione di matrice regolare"**.

Finora $A$ è stata sempre regolare, cioè diagonalizzabile:

$$A=\begin{pmatrix}u_1&u_2&\cdots\end{pmatrix}\begin{pmatrix}\lambda_1&&\\&\lambda_1&\\&&\ddots\end{pmatrix}\begin{pmatrix}v_1'\\v_2'\\\vdots\end{pmatrix}$$

Anche con autovalori di molteplicità algebrica maggiore di 1, finché si trovano abbastanza autovettori indipendenti per lo stesso autovalore (cioè finché la molteplicità geometrica è uguale a quella algebrica), $A$ si diagonalizza. Studiamo il legame con $\Phi(s)$, e poi il caso in cui $A$ **non** è diagonalizzabile.

Sia $\lambda$ un autovalore con molteplicità algebrica e geometrica 2, autovettori $u_1$, $u_2$:

$$\Phi(t)=\begin{pmatrix}u_1&u_2&\cdots\end{pmatrix}\begin{pmatrix}e^{\lambda t}&&\\&e^{\lambda t}&\\&&\ddots\end{pmatrix}\begin{pmatrix}v_1'\\v_2'\\\vdots\end{pmatrix}=e^{\lambda t}u_1v_1'+e^{\lambda t}u_2v_2'+\dots=e^{\lambda t}\begin{pmatrix}u_1&u_2\end{pmatrix}\begin{pmatrix}v_1'\\v_2'\end{pmatrix}+\dots$$

L'esponenziale $e^{\lambda t}$ si raccoglie, perché è comune ai due termini dello stesso autovalore. Con $R_1=\begin{pmatrix}u_1&u_2\end{pmatrix}\begin{pmatrix}v_1'\\v_2'\end{pmatrix}$, in $s$ ci si aspetta

$$\Phi(s)=\mathcal L[R_1e^{\lambda t}+\dots]=R_1\mathcal L[e^{\lambda t}]+\mathcal L[\dots]=\frac{R_1}{s-\lambda}+\dots$$

Il termine ha denominatore **di primo grado**, ma il residuo $R_1$ ha **rango 2** (prodotto di una matrice $n\times2$ e una $2\times n$, entrambe di rango 2). Quindi, calcolando $\Phi(s)$, **ogni polo è un autovalore, e la sua molteplicità** (algebrica e geometrica, che nel caso regolare coincidono) **è il rango del residuo**.

> [!note] Annotazione di Simone
> Sotto questo paragrafo: **"IMPORTANTISSIMA OSSERVAZIONE"**; sopra "caso regolare": **"!!"**.

In definitiva, se $A$ è diagonalizzabile, $\Phi(s)$ scomposta in fratti semplici ha solo termini con denominatore di **grado 1**:

$$\Phi(s)=\frac{R_1}{(s-\lambda_1)^1}+\frac{R_2}{(s-\lambda_2)^1}+\dots$$

Eppure sappiamo che

$$\Phi(s)=(sI-A)^{-1}=\frac{\mathrm{adj}(sI-A)}{\det(sI-A)}$$

e il denominatore $\det(sI-A)$ è il **polinomio caratteristico**, che contiene tutti gli autovalori con la loro molteplicità algebrica:

$$(sI-A)^{-1}=\frac{\mathrm{adj}(sI-A)}{\det(sI-A)}=\frac{(\dots)}{(s-\lambda_1)^2(s-\lambda_2)^3\cdots}$$

Se alla fine i fattori al denominatore hanno tutti grado 1, vuol dire che si **semplificano** con termini della matrice aggiunta:

$$\Phi(s)=\frac{\mathrm{adj}(sI-A)}{\det(sI-A)}\ \stackrel{\text{semplificazioni}}{=}\ \frac{\dots}{(s-\lambda_1)^1(s-\lambda_2)^1\cdots}$$

> [!note] Precisazione
> Gli appunti dicono che $\det(sI-A)$ "può essere riscritto come $-\det(A-sI)$". In generale $\det(sI-A)=(-1)^n\det(A-sI)$: il segno meno c'è solo per $n$ dispari. Non cambia nulla, perché interessano le radici.

Se dopo le semplificazioni restano al denominatore termini di grado **superiore** a 1, allora $A$ **non è diagonalizzabile**: è il caso non regolare. Nella semplificazione non può sparire un intero fattore $(s-\lambda_i)$: il grado finale è almeno 1, mai 0 (tutti gli autovalori compaiono in $\Phi(s)$).

> [!important] Riconoscere la diagonalizzabilità da $\Phi(s)$
> $A$ è diagonalizzabile se e solo se, nella scomposizione di $\Phi(s)=(sI-A)^{-1}$, **tutti i poli sono semplici**. Il denominatore comune ridotto si chiama **polinomio minimo**: ha le stesse radici del polinomio caratteristico, ma ciascuna con esponente pari al suo **indice geometrico** (vedi sotto).

> [!note] Annotazione di Simone
> A margine: **"Molto importante osservazione"**.

Per le altre matrici, in $\Psi(s)=C\Phi(s)=C\frac{(\dots)}{(s-\lambda_1)(s-\lambda_2)\cdots}$ si può cancellare **interamente** qualche fattore $(s-\lambda_i)$: in $\Psi(t)$ possono sparire i termini **non osservabili**. Lo stesso per $H(s)$ con i termini non eccitabili e, di conseguenza, per $W(s)$.

> [!quote] Dal libro — polinomio minimo
> "Il minimo comune multiplo dei polinomi a denominatore della trasformata della matrice di transizione è un fattore del polinomio caratteristico, il **polinomio minimo**, che ha la particolarità di avere tutti gli autovalori, ma ciascuno con molteplicità pari all'ordine geometrico corrispondente". Nell'Esempio 4.2.2 ($A=-I$) $\Phi(s)=\frac{1}{s+1}I$: il polinomio minimo $(s+1)$ ha grado 1 anche se $n=2$. _(libro, §4.1–4.2.1, pp. 164, 170–171)_

## Caso non regolare e blocchi di Jordan

Vedi [[TDS - Forma di Jordan]].

Se $A$ ha $r$ autovalori con molteplicità algebriche $\mu_1,\dots,\mu_r$ e per ciascuno si trovano $\mu_i$ autovettori indipendenti, $A$ è diagonalizzabile e

$$\Lambda=\begin{pmatrix}\boxed{\begin{matrix}\lambda_1&&\\&\ddots&\\&&\lambda_1\end{matrix}}_{\ \mu_1}&&\\&\ddots&\\&&\boxed{\begin{matrix}\lambda_r&&\\&\ddots&\\&&\lambda_r\end{matrix}}_{\ \mu_r}\end{pmatrix}$$

Nel caso regolare, se $u$ è autovettore, vale sempre $(A-\lambda I)u=0$: applicando l'operatore $(A-\lambda I)$ a $u$ si va **in zero**. Quando invece la molteplicità geometrica è **minore** di quella algebrica (concentriamoci sul caso in cui la geometrica è 1), questo succede in più "**passaggi**":

$$(A-\lambda I)u_2=u_1\ \longrightarrow\ (A-\lambda I)u_1=0$$

Applicando $(A-\lambda I)$ a $u_2$ **non si va in zero**, ma si ottiene l'autovettore $u_1$; applicandolo ancora a $u_1$ si va in zero. Equivale a

$$(A-\lambda I)^2u_2=0$$

> [!warning] Correzione
> Negli appunti l'equazione riassuntiva è scritta $(A-\lambda I)^2u_1=0$: è vera, ma banale (già $(A-\lambda I)u_1=0$). La relazione che caratterizza il nuovo vettore è $(A-\lambda I)^2u_2=0$ con $(A-\lambda I)u_2\neq0$; lo stesso vale per il caso a tre passaggi, dove la condizione giusta è $(A-\lambda I)^3u_3=0$.

Questo accade con molteplicità algebrica 2 (e geometrica 1); con algebrica 3 i passaggi sono tre:

$$(A-\lambda I)u_3=u_2\ \to\ (A-\lambda I)u_2=u_1\ \to\ (A-\lambda I)u_1=0\qquad\iff\qquad(A-\lambda I)^3u_3=0$$

Essendo la geometrica pari a 1 c'è **un solo autovettore**, $u_1$: l'unico che "va" direttamente in zero. Graficamente, applicando $(A-\lambda I)$ a qualsiasi punto della retta di $u_1$ si va in zero:

![[TDS-L17-01.png]]

Se la molteplicità algebrica è 2, si va comunque in zero, ma "passando" prima per la retta di $u_1$:

![[TDS-L17-02.png]]

Qualsiasi punto della retta di $u_2$ (blu) viene portato in un punto della retta di $u_1$ (verde), e da lì in zero. Il sottospazio di $u_1$ è **invariante**: applicandoci $(A-\lambda I)$ si resta su $u_1$ (anzi, si va in zero). Quello di $u_2$ **non** lo è, perché si finisce su $u_1$; però $u_1$ e $u_2$ **insieme** generano un sottospazio invariante (il piano).

> [!note] Annotazioni di Simone
> A margine: **"Come abbiamo sempre fatto"** (accanto a $(A-\lambda I)u=0$) e **"Osservazioni importanti"** (accanto al grafico).

I vettori $u_1,u_2,\dots,u_\mu$ si chiamano **autovettori generalizzati**, e queste applicazioni "a catena" di $(A-\lambda I)$ generano le **catene di autovettori** (generalizzati). Nella base di una catena la matrice $\Lambda$ assume una forma particolare; con molteplicità geometrica 1:

$$\Lambda=\begin{pmatrix}\lambda&1&&&\\&\lambda&1&&\\&&\ddots&\ddots&\\&&&\lambda&1\\&&&&\lambda\end{pmatrix}$$

Oltre alla diagonale con i $\lambda$, la diagonale subito a destra è fatta di **1**: indicano che ogni vettore "dipende" dal successivo nella catena, fino all'ultimo, che è un vero autovettore. Il resto della matrice è 0.

> [!tip] Da dove vengono gli 1
> In colonne, $AU=U\Lambda$. Con $U=(u_1\ u_2)$ e $(A-\lambda I)u_2=u_1$, cioè $Au_2=u_1+\lambda u_2$: la seconda colonna di $\Lambda$ ha un $1$ nella posizione di $u_1$ e $\lambda$ in quella di $u_2$. Ecco l'1 sopra la diagonale.

Con autovalori $\lambda_1,\dots,\lambda_r$ e $\lambda_1$ di molteplicità algebrica $\mu_1$ e geometrica 1, il blocco di $\lambda_1$ ha la diagonale a destra piena di 1:

$$\Lambda=\begin{pmatrix}\boxed{\begin{matrix}\lambda_1&1&&\\&\lambda_1&\ddots&\\&&\ddots&1\\&&&\lambda_1\end{matrix}}_{\ \mu_1}&&\\&\ddots&\\&&\boxed{\begin{matrix}\lambda_r&&\\&\ddots&\\&&\lambda_r\end{matrix}}_{\ \mu_r}\end{pmatrix}$$

**Esempi.** In $n=3$ con un solo autovalore $\lambda$: se la molteplicità geometrica è uguale all'algebrica, $A$ è diagonalizzabile; se è 1, c'è un blocco $3\times3$:

$$\Lambda_R=\begin{pmatrix}\lambda&0&0\\0&\lambda&0\\0&0&\lambda\end{pmatrix},\qquad\Lambda=\begin{pmatrix}\lambda&1&0\\0&\lambda&1\\0&0&\lambda\end{pmatrix}$$

Con $n=6$, $\lambda_1$ di molteplicità algebrica e geometrica 3, $\lambda_2$ semplice e $\lambda_3$ di molteplicità algebrica 2 e geometrica 1:

$$\Lambda=\begin{pmatrix}\boxed{\begin{matrix}\lambda_1&0&0\\0&\lambda_1&0\\0&0&\lambda_1\end{matrix}}&&\\&\boxed{\lambda_2}&\\&&\boxed{\begin{matrix}\lambda_3&1\\0&\lambda_3\end{matrix}}\end{pmatrix}$$

e se anche $\lambda_1$ ha molteplicità geometrica 1, il primo blocco diventa $\begin{psmallmatrix}\lambda_1&1&0\\0&\lambda_1&1\\0&0&\lambda_1\end{psmallmatrix}$. Questi "blocchetti" con gli autovalori sulla diagonale e gli 1 a destra si chiamano **blocchi di Jordan**. Poiché i vettori di ciascun autovalore determinano sottospazi invarianti, la matrice resta a blocchi e i blocchi non si influenzano.

## Esponenziale dei blocchi di Jordan

La forma a blocchi non crea problemi per $e^{\Lambda t}$, che resta semplice da calcolare. Si dimostra che

$$e^{\begin{pmatrix}\lambda&1&0\\0&\lambda&1\\0&0&\lambda\end{pmatrix}t}=\begin{pmatrix}e^{\lambda t}&te^{\lambda t}&\frac{t^2}{2}e^{\lambda t}\\0&e^{\lambda t}&te^{\lambda t}\\0&0&e^{\lambda t}\end{pmatrix}$$

Sulla diagonale principale c'è $e^{\lambda t}$, e spostandosi sulle diagonali a destra si moltiplica per $\frac{t^k}{k!}$: $t,\ \frac{t^2}{2},\ \frac{t^3}{6},\dots$

> [!tip] Perché
> Il blocco si scrive $J=\lambda I+N$, con $N$ la matrice con gli 1 sopra la diagonale. $\lambda I$ e $N$ commutano, quindi $e^{Jt}=e^{\lambda t}e^{Nt}$. $N$ è **nilpotente** ($N^3=0$ per un blocco $3\times3$: ogni potenza sposta gli 1 di una diagonale verso l'alto), quindi la serie di $e^{Nt}$ si ferma: $e^{Nt}=I+Nt+N^2\frac{t^2}{2}$. Ecco i termini $t$ e $\frac{t^2}{2}$.

Per l'esempio precedente (con $\lambda_1$ di geometrica 1):

$$e^{\Lambda t}=\begin{pmatrix}\boxed{\begin{matrix}e^{\lambda_1t}&te^{\lambda_1t}&\frac{t^2}{2}e^{\lambda_1t}\\0&e^{\lambda_1t}&te^{\lambda_1t}\\0&0&e^{\lambda_1t}\end{matrix}}&&\\&\boxed{e^{\lambda_2t}}&\\&&\boxed{\begin{matrix}e^{\lambda_3t}&te^{\lambda_3t}\\0&e^{\lambda_3t}\end{matrix}}\end{pmatrix}$$

> [!quote] Dal libro — Proposizione 2.2.2
> Per un blocco con $l$ blocchi uguali $\Lambda$ sulla diagonale e identità sopra, $e^{Mt}$ ha $e^{\Lambda t}$ sulla diagonale, $te^{\Lambda t}$ sopra, fino a $\frac{t^{l-1}}{(l-1)!}e^{\Lambda t}$ nell'angolo. Vale anche per coppie complesse: con $\Lambda=\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}$ e due coppie coincidenti di molteplicità geometrica 1 si ottengono termini $t\cos\omega t$, $t\sin\omega t$. "Nel caso generale tali funzioni potranno essere premoltiplicate per polinomi in $t$ di grado pari all'ordine geometrico $-1$." _(libro, §2.2.2, pp. 53–55)_

## Catene di autovettori

Vedi [[TDS - Catene di autovettori]].

Finora si è visto il caso limite, molteplicità geometrica 1. In generale la geometrica può essere minore dell'algebrica ma maggiore di 1 (per esempio algebrica 3 e geometrica 2): vanno trovate le **catene di autovettori**. Si parte dagli autovettori che vanno a zero **direttamente** con $(A-\lambda I)$:

$$(A-\lambda I)u=0$$

e se ne trovano tanti indipendenti quanta è la molteplicità geometrica. Con $\mu=3$ e geometrica $\hat\mu=2$ si trovano due autovettori $u_1,u_2$ dello stesso $\lambda$, e quindi **due catene** distinte, una per ciascuno. Per la catena di $u_1$ si cerca $a$ tale che $(A-\lambda I)a=u_1$: la catena è $a\to u_1$. Lo stesso per $u_2$: si cerca $b$ con $(A-\lambda I)b=u_2$ e, se è indipendente dagli altri, la catena è $b\to u_2$.

Con la notazione del professore si scrivono gli autovettori in alto e si va "a ritroso" verso il basso:

| $u_1$ | $u_2$ |
|---|---|
| $a$ | $b$ |

(le frecce, nella tabella degli appunti, vanno dal basso verso l'alto: applicando $(A-\lambda I)$ si sale).

> [!note] Annotazione di Simone
> A margine: **"Procedura"**.

Per trovare $a$ ci sono due modi:
- **1° metodo**: risolvere $(A-\lambda I)a=u_1$ come sistema lineare, con $a$ vettore generico. Per esempio, con $n=3$ e numeri inventati:
  $$\underbrace{\begin{pmatrix}1&2&0\\3&-2&3\\4&2&5\end{pmatrix}}_{A-\lambda I}\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}=\underbrace{\begin{pmatrix}3\\4\\2\end{pmatrix}}_{u_1}\ \Longrightarrow\ \begin{cases}a_1+2a_2=3\\3a_1-2a_2+3a_3=4\\4a_1+2a_2+5a_3=2\end{cases}$$
- **2° metodo**: imporre $(A-\lambda I)^2a=0$, cioè calcolare $(A-\lambda I)^2$ e trovarne il nucleo (scartando i vettori che stanno già in $\ker(A-\lambda I)$).

Lo stesso per $b$. Ci si ferma quando si sono trovati tanti vettori indipendenti quanta è la **molteplicità algebrica**: con $\mu=5$, cinque vettori. Le catene possono essere più lunghe:

| $u_1$ | $u_2$ |
|---|---|
| $a$ | $b$ |
| $a_2$ | $b_2$ |
| $a_3$ | $b_3$ |
| $\vdots$ | $\vdots$ |

$$(A-\lambda I)a_3=a_2,\quad(A-\lambda I)a_2=a,\quad(A-\lambda I)a=u_1\qquad\iff\qquad(A-\lambda I)^4a_3=0,\quad(A-\lambda I)^3a_2=0,\quad(A-\lambda I)^2a=0$$

**Esempio.** Un autovalore $\lambda$ con $\mu=3$ e $\hat\mu=2$, con due catene:

| $u_1$ | $u_2$ |
|---|---|
| | $b$ |

Il vettore $a$ è stato tolto, ipotizzando che $a,u_1,u_2$ risultassero **dipendenti** (in realtà può succedere che siano indipendenti sia $a,u_1,u_2$ sia $b,u_1,u_2$; il professore non ha specificato quale scegliere, quindi la scelta è arbitraria). $u_1$ genera un sottospazio invariante da solo, quindi si comporta come se $A$ fosse diagonalizzabile; anche $u_2$ è invariante da solo ma, visto che $b$ lo è solo insieme a $u_2$, compare un blocchetto di Jordan:

$$\Lambda=\begin{pmatrix}\boxed{\lambda}&0&0\\0&\boxed{\begin{matrix}\lambda&1\\0&\lambda\end{matrix}}&\\&&\ddots\end{pmatrix}$$

> [!important] Molteplicità algebrica, geometrica e indice geometrico
> | Grandezza | Significato | Nell'esempio |
> |---|---|---|
> | molteplicità algebrica $\mu$ | quanti vettori indipendenti trovare (dimensione totale dei blocchi) | 3 |
> | molteplicità geometrica $\hat\mu$ | quante catene ci sono = quanti blocchi di Jordan | 2 |
> | indice geometrico (I.G.) | quanti vettori ha la catena più lunga = dimensione del blocco più grande | 2 |
>
> Se la geometrica è uguale all'algebrica, ogni catena ha lunghezza 1 e non compaiono blocchi di Jordan (caso regolare).

L'esponenziale si calcola per ogni blocchetto:

$$e^{\Lambda t}=\begin{pmatrix}\boxed{e^{\lambda t}}&0&0\\0&\boxed{\begin{matrix}e^{\lambda t}&te^{\lambda t}\\0&e^{\lambda t}\end{matrix}}&\\&&\ddots\end{pmatrix}$$

Il grado massimo di $t$ che compare è pari all'**indice geometrico meno uno**.

> [!quote] Dal libro — procedura di calcolo della forma di Jordan
> Il libro (Appendice A.2.1) costruisce le catene a partire dall'alto: si trova l'**ordine geometrico** $m$, la prima potenza per cui $\ker(A-\lambda I)^m$ ha dimensione $\mu$; poi si scelgono i vettori $u^k$ con $\ker(A-\lambda I)^k=\ker(A-\lambda I)^{k-1}\oplus\mathrm{gen}\{u^k\}$ (autovettori generalizzati di ordine $k$), e li si fa "scendere" applicando $(A-\lambda I)$. Le dimensioni $d_i=\dim\ker(A-\lambda I)^i$ crescono fino a $\mu$ e dicono quante catene hanno lunghezza almeno $i$: $\hat\mu=d_1<d_2<\dots<d_m=\mu$.
>
> Esempio: $A=\begin{psmallmatrix}1&0&1\\1&1&0\\0&0&1\end{psmallmatrix}$ ha $\lambda=1$ con $\mu=3$, $\hat\mu=1$, $(A-I)^3=0$. La catena è $e_3\to e_1\to e_2$ e con $T^{-1}=(e_2\ e_1\ e_3)$ si ottiene $TAT^{-1}=\begin{psmallmatrix}1&1&0\\0&1&1\\0&0&1\end{psmallmatrix}$. _(libro, Appendice A.2.1, pp. 375–377)_

## Effetti dei blocchi di Jordan in $\Phi(s)$

Riprendendo l'esempio precedente,

$$\Phi(t)=Ue^{\Lambda t}U^{-1}=e^{\lambda t}R_1+(e^{\lambda t}+te^{\lambda t})R_2+\dots=(\dots)\,e^{\lambda t}+(\dots)\,te^{\lambda t}$$

dove $R_1,R_2,\dots$ e "$(\dots)$" sono matrici. Trasformando (con $\mathcal L[te^{\lambda t}]=\frac1{(s-\lambda)^2}$, dalla traslazione complessa):

$$\Phi(s)=(\dots)\frac1{s-\lambda}+(\dots)\frac1{(s-\lambda)^2}+\dots$$

> [!important] Effetto dei blocchi di Jordan
> - In $\Phi(t)$, oltre agli esponenziali, compaiono **polinomi** in $t$, di grado fino all'**indice geometrico meno 1**.
> - In $\Phi(s)$ compaiono **potenze maggiori di 1** al denominatore, fino all'**indice geometrico**.

È la conferma, dal lato del tempo, di quanto visto all'inizio dal lato di $s$.

## Discussione sui modi naturali non regolari

Vedi [[TDS - Modi naturali]].

Quando in $\Phi(t)$ ci sono anche potenze di $t$, cosa si chiama "modo naturale"? Informalmente, il modo naturale relativo a $\lambda$ è "tutto ciò in cui compare $e^{\lambda t}$" (anche moltiplicato per $t,t^2,\dots$). Nel calcolo di $\Psi(t)$, $H(t)$, $W(t)$ può succedere che spariscano **solo alcune parti** di questo modo (che ne siano osservabili o eccitabili solo alcune parti). In questo caso ha poco senso parlare di eccitabilità e osservabilità tout court: si parla di **completa eccitabilità** e **completa osservabilità** quando "non scompare nessun pezzo" del modo naturale. Se il modo compare integralmente in $\Psi(t)$ è completamente osservabile, altrimenti non lo è (come già visto, in un altro senso, per gli autovalori multipli regolari in [[07 - TDS - Autovalori complessi coniugati#Completa osservabilità e completa eccitabilità|lezione 7]]).

> [!quote] Dal libro — stabilità e modi non regolari
> Le leggi $t^ke^{\lambda t}$ spiegano la condizione di stabilità vista in [[11 - TDS - Punti di equilibrio e stabilità#Definizione operativa di stabilità|lezione 11]]: con $\mathrm{Re}(\lambda)<0$ convergono comunque (l'esponenziale "vince" sul polinomio), ma con $\mathrm{Re}(\lambda)=0$ e ordine geometrico maggiore di 1 compare $t^k$, che diverge. Per questo gli autovalori sull'asse immaginario sono ammessi, per la stabilità semplice, solo se di ordine 1. _(libro, §3.2.1, pp. 107–108)_

## Esercizio

Per esercizio (proposto negli appunti), con

$$A=\begin{pmatrix}0&1&1\\-1&-2&1\\0&0&-1\end{pmatrix}$$

calcolare $e^{At}$ nei due modi visti e confrontare i risultati:
1. calcolare $e^{\Lambda t}$ (forma di Jordan) e svolgere il prodotto $Ue^{\Lambda t}U^{-1}$;
2. calcolare $\Phi(s)=(sI-A)^{-1}$ ed $e^{At}=\mathcal L^{-1}[\Phi(s)]$.

> [!example]- Svolgimento con la trasformata (la soluzione degli appunti è in [[41 - TDS - Esercizi di riepilogo finale#Esercizio 2: blocchi di Jordan|lezione 41]])
> $A$ è triangolare a blocchi: il blocco $\begin{psmallmatrix}0&1\\-1&-2\end{psmallmatrix}$ ha polinomio $\lambda^2+2\lambda+1=(\lambda+1)^2$, e l'ultimo elemento è $-1$. Quindi $\lambda=-1$ con $\mu=3$. $A+I=\begin{psmallmatrix}1&1&1\\-1&-1&1\\0&0&0\end{psmallmatrix}$ ha rango 2, quindi $\hat\mu=1$: un solo blocco di Jordan $3\times3$, indice geometrico 3. Ci si aspettano termini fino a $t^2e^{-t}$.
>
> $\det(sI-A)=(s+1)^3$ e
> $$\Phi(s)=\begin{pmatrix}\frac{s+2}{(s+1)^2}&\frac1{(s+1)^2}&\frac{s+3}{(s+1)^3}\\[1mm]-\frac1{(s+1)^2}&\frac{s}{(s+1)^2}&\frac{s-1}{(s+1)^3}\\[1mm]0&0&\frac1{s+1}\end{pmatrix}$$
> Scomponendo, per esempio $\frac{s+3}{(s+1)^3}=\frac1{(s+1)^2}+\frac2{(s+1)^3}$ e $\frac{s-1}{(s+1)^3}=\frac1{(s+1)^2}-\frac2{(s+1)^3}$, e usando $\mathcal L^{-1}\big[\frac{1}{(s+1)^{k+1}}\big]=\frac{t^k}{k!}e^{-t}$:
> $$e^{At}=e^{-t}\begin{pmatrix}1+t&t&t+t^2\\-t&1-t&t-t^2\\0&0&1\end{pmatrix}$$
> Controllo: per $t=0$ si ha $I$, e la derivata in $0$ dà proprio $A$. Il polinomio minimo è $(s+1)^3$, come previsto dall'indice geometrico 3.
