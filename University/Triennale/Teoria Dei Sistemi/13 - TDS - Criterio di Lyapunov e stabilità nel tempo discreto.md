---
title: Criterio di Lyapunov e stabilità nel tempo discreto
aliases:
  - TDS — Criterio di Lyapunov e stabilità nel tempo discreto
tags:
  - teoria-dei-sistemi
  - stabilita
  - criterio-di-lyapunov
  - sistemi-non-lineari
  - tempo-discreto
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 54–59); libro Monaco et al., §3.4–3.4.2
---

# Criterio di Lyapunov e stabilità nel tempo discreto

> [!abstract] Scopo della lezione
> La [[12 - TDS - Criterio di Routh e linearizzazione#Approssimazione di sistemi non lineari|linearizzazione]] non dice nulla quando il sistema approssimante è solo semplicemente stabile. Qui si introduce uno strumento che **non** passa per il sistema lineare:
> 1. il **criterio di Lyapunov**, basato su una funzione "energia" $V(x)$ che decresce lungo il moto; con esempi in cui la linearizzazione basta e in cui invece serve Lyapunov, e con l'estensione alla stabilità **globale**;
> 2. il criterio di Lyapunov per i **sistemi lineari**, che diventa una condizione **necessaria e sufficiente** tramite l'equazione $A'Q+QA=-P$;
> 3. la stabilità **interna ed esterna nel tempo discreto**: le stesse idee, con il **modulo** degli autovalori al posto della parte reale e **1** al posto di **0**.
>
> Segue [[14 - TDS - Stabilità nel tempo discreto ed esempi]]. Indice: [[MOC - Teoria dei Sistemi]].

> [!note] Annotazione di Simone
> In testa alla lezione, a mano in rosso: **"LYAPUNOV (PER SISTEMI NON LINEARI)"**.

## Criterio di Lyapunov

Vedi [[TDS - Criterio di Lyapunov]].

Riassunto di dove siamo: la stabilità di un sistema lineare dipende dal segno della parte reale degli autovalori, che si può trovare senza calcolarli con il [[TDS - Criterio di Routh|criterio di Routh]]. I sistemi non lineari $\dot x=f(x,u)$ si approssimano localmente attorno agli equilibri con sistemi lineari, con $A=J(x)=\frac{\partial f(x,u)}{\partial x}$ calcolata nell'equilibrio (di solito con ingresso nullo). Se il linearizzato è asintoticamente stabile lo è anche il non lineare, e lo stesso per l'instabilità; per la stabilità **semplice** invece non vale.

> [!note] Perché la stabilità semplice "non passa"
> Linearizzando si trascurano i termini di grado maggiore o uguale a 2. Se il linearizzato converge o diverge, quei termini (piccoli vicino all'equilibrio) non cambiano l'andamento. Ma se il linearizzato **non converge né diverge** (stabilità semplice), i termini trascurati possono essere proprio quelli che decidono, spingendo il sistema a convergere o a divergere.

Per gli equilibri dei sistemi non lineari esistono criteri che **non** fanno riferimento a sistemi lineari: uno dei più usati è il **criterio di Lyapunov**. Sia $x_e$ un equilibrio. Si prende una funzione scalare $V(x):\mathbb R^n\to\mathbb R$ nulla nel punto e positiva attorno:

$$V(x_e)=0,\qquad V(x)>0\ \ \forall x\in I_{x_e}\setminus\{x_e\}$$

Una funzione così si dice **definita positiva** (nell'intorno $I_{x_e}$ di $x_e$). Se invece è negativa nell'intorno e nulla in $x_e$ è **definita negativa**; se nell'intorno può anche valere zero è **semidefinita positiva** ($\ge0$) o **semidefinita negativa** ($\le0$).

> [!important] Criterio di Lyapunov
> Sia $V(x)$ definita positiva in un intorno di $x_e$, e sia
> $$\dot V(x)=\frac{\partial V(x)}{\partial x}\,\dot x=\sum_{i=1}^n\frac{\partial V}{\partial x_i}f_i(x)$$
> la sua derivata **lungo il moto** del sistema.
> - Se $\dot V$ è **definita negativa**, $x_e$ è **localmente asintoticamente stabile**.
> - Se $\dot V$ è **semidefinita negativa**, $x_e$ è **localmente semplicemente stabile**.

La logica viene da un'idea fisica: un pendolo, in un certo punto, ha una certa energia $V(x)$ (positiva, essendo energia) che col passare del tempo, per via dell'attrito, diminuisce ($\dot V<0$), finché si arriva all'equilibrio in cui non c'è più energia e il pendolo è fermo in verticale ($V(x_e)=0$). Si noti che $\dot V$ si calcola **senza risolvere** il sistema: basta sostituire $\dot x=f(x)$.

> [!warning] Il criterio è solo sufficiente
> Non c'è un metodo universale per trovare $V(x)$. Se non si trova una funzione adatta, **non si può concludere che il punto non sia stabile**: non si può dire nulla.

> [!note] Annotazione di Simone
> In fondo alla pagina, a mano:
> **Lyapunov:**
> - Se V(x)>0, V̇(x)<0 → LOCALMENTE STABILE ASINTOTICAMENTE
> - Se V(x)>0, V̇(x)≤0 → LOCALMENTE STABILE SEMPLICEMENTE
> - Se non trovo un V(x) che soddisfa le condizioni, non posso concludere nulla

> [!quote] Dal libro — il metodo generale
> "Il criterio di Lyapunov estende, in un contesto puramente matematico, un concetto che è collegato a considerazioni energetiche": allo stato di equilibrio si associa un livello di energia nullo, agli stati vicini un livello superiore, e la stabilità corrisponde alla diminuzione dell'energia lungo il moto. Per esempio, dato $x_e$, la funzione $V(x)=\sum_i(x_i-x_{e,i})^2$ è definita positiva in tutto lo spazio. _(libro, §3.4.1, pp. 122–123)_

### Esempi di applicazione del criterio

**Esempio 1.** Consideriamo

$$\begin{cases}\dot x_1=-x_1-x_1x_2^2+u_1^2\\\dot x_2=-x_2-x_1u_1u_2\end{cases}$$

(non lineare per i termini $x_1x_2^2$ e $x_1u_1u_2$). Con ingresso nullo, $u_1=u_2=0$:

$$\begin{cases}\dot x_1=-x_1-x_1x_2^2=f_1(x_1,x_2)\\\dot x_2=-x_2=f_2(x_1,x_2)\end{cases}$$

Si vede subito che $x=\begin{psmallmatrix}0\\0\end{psmallmatrix}$ è un equilibrio. Proviamo con la linearizzazione:

$$J=\begin{pmatrix}\frac{\partial f_1}{\partial x_1}&\frac{\partial f_1}{\partial x_2}\\[1mm]\frac{\partial f_2}{\partial x_1}&\frac{\partial f_2}{\partial x_2}\end{pmatrix}=\begin{pmatrix}-1-x_2^2&-2x_1x_2\\0&-1\end{pmatrix}\Bigg|_{x_e}=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=A$$

Gli autovalori sono $-1,-1$: il sistema è **localmente asintoticamente stabile** nell'equilibrio, e Lyapunov non serve.

Volendolo usare comunque, serve una $V(x)$ nulla in $x_e$ e positiva altrove, per esempio $V(x)=\frac12(x_1^2+x_2^2)$. La derivata (sostituendo $\dot x$) è

$$\dot V(x)=\frac{\partial V(x)}{\partial x}\dot x=\begin{pmatrix}\frac{\partial V}{\partial x_1}&\frac{\partial V}{\partial x_2}\end{pmatrix}\begin{pmatrix}\dot x_1\\\dot x_2\end{pmatrix}=\begin{pmatrix}x_1&x_2\end{pmatrix}\begin{pmatrix}-x_1-x_1x_2^2\\-x_2\end{pmatrix}=-x_1^2-x_1^2x_2^2-x_2^2$$

Qui $\frac{\partial V}{\partial x}$ è il gradiente di $V$, una matrice $1\times n$ (una sola riga perché $V$ è scalare): è lo jacobiano di una funzione a valori reali. $\dot V$ è negativa ovunque tranne in $\begin{psmallmatrix}0\\0\end{psmallmatrix}$: **definita negativa**. Conclusione: l'origine è **localmente** asintoticamente stabile (localmente perché si studia il sistema nelle vicinanze dell'equilibrio).

> [!note] Annotazioni di Simone
> Sull'esempio, a mano: "Non lineare" sui termini $x_1x_2^2$ e $x_1u_1u_2$; "$=f_1(x_1,x_2)$", "$=f_2(x_1,x_2)$"; "Faccio l'approssimazione" accanto allo jacobiano; **"NON USO LYAPUNOV"** accanto alla conclusione con gli autovalori e **"USO LYAPUNOV"** accanto al secondo metodo; "Sostituisco" sopra $\dot x$.

**Esempio 2.** Ora cambia la seconda equazione:

$$\begin{cases}\dot x_1=-x_1-x_1x_2^2+u_1^2\\\dot x_2=-x_1^2x_2-x_1u_1u_2\end{cases}\qquad J=\begin{pmatrix}-1-x_2^2&-2x_1x_2\\-2x_1x_2&-x_1^2\end{pmatrix}\Bigg|_{x_e}=\begin{pmatrix}-1&0\\0&0\end{pmatrix}=A$$

Gli autovalori sono $-1$ e $0$: il linearizzato è semplicemente stabile e **non si può dire nulla** sul sistema non lineare. L'unica possibilità è Lyapunov. Con la stessa $V(x)=\frac12(x_1^2+x_2^2)$:

$$\dot V(x)=\begin{pmatrix}x_1&x_2\end{pmatrix}\begin{pmatrix}-x_1-x_1x_2^2\\-x_1^2x_2\end{pmatrix}=-x_1^2-2x_1^2x_2^2=-x_1^2(1+2x_2^2)\le0$$

È **semidefinita negativa**: è nulla nell'equilibrio, ma anche in tutti i punti con $x_1=0$, $x_2\neq0$, cioè per tutti i punti dell'intorno della forma $\begin{psmallmatrix}0\\x_2\end{psmallmatrix}$. Si conclude che $x_e=\begin{psmallmatrix}0\\0\end{psmallmatrix}$ è **almeno** stabile semplicemente. Non si può dire però che **non** sia asintoticamente stabile: si potrebbe trovare un'altra funzione di Lyapunov con derivata definita negativa.

> [!note] Annotazioni di Simone
> Accanto all'esempio 2, a mano: **"USANDO IL TEOREMA DI PRIMA Re(λ)≤0 ⇒ STABILITÀ SEMPL. ⇒ NON SI PUÒ CONCLUDERE NULLA ⇓ SFRUTTO LYAPUNOV CHE MI PERMETTE DI VERIFICARE LA STABILITÀ SEMPLICE"**; a margine della conclusione: "Infatti: punti di equilibrio … almeno stabile semplicemente".

> [!tip] In questo esempio non può essere asintotica
> Con $x_1=0$ il sistema dà $\dot x_1=0$ e $\dot x_2=0$: **tutti** i punti $\begin{psmallmatrix}0\\x_2\end{psmallmatrix}$ sono equilibri. L'origine non è un equilibrio isolato, quindi non può essere asintoticamente stabile (come visto in [[11 - TDS - Punti di equilibrio e stabilità#Stabilità asintotica nei sistemi lineari|lezione 11]]): la stabilità semplice trovata con Lyapunov è il meglio che si possa avere.

Se l'equilibrio è $x_e=\begin{psmallmatrix}x_{e1}\\x_{e2}\end{psmallmatrix}$, la funzione più semplice da provare è in genere

$$V(x)=\tfrac12(x_1-x_{e1})^2+\tfrac12(x_2-x_{e2})^2$$

che si annulla nel punto ed è definita positiva.

> [!warning] Correzione
> Negli appunti è scritta $V(x)=\frac12(x-x_{e1})^2+\frac12(x-x_{e2})^2$: le variabili vanno indicizzate, $x_1-x_{e1}$ e $x_2-x_{e2}$, altrimenti la funzione non si annulla in $x_e$.

### Stabilità globale

Il criterio si può estendere per stabilire se la stabilità di un equilibrio è solo **locale** (vicino al punto) o **globale** (in tutto lo spazio). Un equilibrio è **globalmente** stabile se si trova una $V(x)$ che, oltre a garantire la stabilità locale, è definita in tutto lo spazio ed è **radialmente illimitata**, cioè tende all'infinito quando $x$ tende all'infinito:

$$\lim_{\|x\|\to+\infty}V(x)=+\infty$$

La stabilità asintotica globale è possibile solo quando l'equilibrio $x_e$ è **unico**: se ce ne fossero altri, partendo da essi non si convergerebbe a $x_e$.

> [!note] Annotazione di Simone
> A margine: **"ESPANDE LYAPUNOV PER UNA STABILITÀ GLOBALE ANZICHÉ LOCALE"**.

> [!quote] Dal libro — Teorema 3.4.2 e La Salle
> "Lo stato $x_e$ di equilibrio è globalmente asintoticamente stabile se la funzione $V(x)$ è definita positiva rispetto ad $x_e$ in tutto lo spazio ed è radialmente illimitata e la funzione $\dot V$ è definita negativa rispetto ad $x_e$ in tutto lo spazio"; con $\dot V$ solo semidefinita negativa si ottiene la stabilità semplice globale. Quando $\dot V$ è solo semidefinita negativa si può ancora concludere la stabilità asintotica con il **teorema di La Salle**: se il più grande insieme invariante contenuto nell'insieme dove $\dot V=0$ è il solo $x_e$, allora $x_e$ è asintoticamente stabile. È il caso del pendolo con attrito con $V$ = energia: $\dot E=-\frac kmx_2^2$ si annulla per $x_2=0$, ma l'unico moto che resta in $\{x_2=0\}$ è l'equilibrio. _(libro, §3.4.1, pp. 124–127)_

> [!warning] Precisazione
> Gli appunti dicono che per la stabilità globale basta una $V$ radialmente illimitata con derivata "definita negativa o semidefinita negativa". Con $\dot V$ **semidefinita** negativa si ottiene la stabilità **semplice** globale; per quella **asintotica** globale serve $\dot V$ **definita** negativa in tutto lo spazio (oppure La Salle).

## Criterio di Lyapunov per i sistemi lineari

Proviamo a usare il criterio per $\dot x=Ax+Bu$ (con $u=0$). $x_e=0$ è sempre un equilibrio e, per studiarne la stabilità asintotica, deve essere l'**unico**. Il caso più semplice di funzione definita positiva è quella **quadratica**:

$$V(x)=x'Qx\qquad(x'=x^T)$$

Se $Q$ (che si può assumere **simmetrica** senza perdita di generalità) è **definita positiva**, $Q>0$, cioè i determinanti dei suoi **minori principali** sono tutti positivi, allora $V$ è definita positiva.

> [!note] Perché simmetrica e quali minori
> Se $M$ non è simmetrica si può sempre usare $V=x'Mx+x'M'x=x'(M+M')x$, con $M+M'$ simmetrica; la simmetria semplifica i calcoli (le incognite sono circa la metà). I minori principali (di nord-ovest) di una matrice $n\times n$ sono le sottomatrici $(a_{11})$, $\begin{psmallmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{psmallmatrix}$, $\begin{psmallmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{psmallmatrix}$, …, fino all'intera matrice: è il **criterio di Sylvester**.

La derivata, tenendo presente che $\dot x=Ax$, è

$$\dot V(x)=\dot x'Qx+x'Q\dot x=(Ax)'Qx+x'QAx=x'A'Qx+x'QAx=x'(A'Q+QA)x$$

Per Lyapunov, se $\dot V$ è definita negativa l'equilibrio è asintoticamente stabile, e $x'(A'Q+QA)x$ è definita negativa se $A'Q+QA$ lo è, cioè se

$$A'Q+QA=-P\qquad\text{con }P>0,\qquad\text{e allora }\dot V(x)=-x'Px<0$$

> [!note] Annotazione di Simone
> Accanto alla derivata: **"Applico Lyapunov"**.

La particolarità del caso lineare è che questa condizione è non solo **sufficiente** ma anche **necessaria**, e dà una soluzione **unica**:

> [!important] Criterio di Lyapunov per sistemi lineari
> $$\forall P>0\ \text{simmetrica}\ \ \exists!\,Q>0\ \text{simmetrica tale che}\ A'Q+QA=-P\quad\iff\quad x_e=0\ \text{è asintoticamente stabile}$$

Si può scegliere $Q$ così:

$$\boxed{Q=\int_0^{+\infty}e^{A't}Pe^{At}\,dt}$$

(l'integrale converge perché, con $A$ asintoticamente stabile, $e^{At}\to0$ esponenzialmente).

**È definita positiva**, perché con $z=e^{At}x$:

$$x'Qx=x'\left(\int_0^{+\infty}e^{A't}Pe^{At}\,dt\right)x=\int_0^{+\infty}\underbrace{x'e^{A't}}_{z'}P\underbrace{e^{At}x}_{z}\,dt>0$$

**È simmetrica**, perché $P$ lo è:

$$Q'=\int_0^{+\infty}(e^{At})'P'(e^{A't})'\,dt=\int_0^{+\infty}e^{A't}P'e^{At}\,dt=\int_0^{+\infty}e^{A't}Pe^{At}\,dt=Q$$

**È soluzione** di $A'Q+QA=-P$:

$$A'Q+QA=\int_0^{+\infty}\big(A'e^{A't}Pe^{At}+e^{A't}Pe^{At}A\big)\,dt$$

L'integrando è la derivata di $e^{A't}Pe^{At}$ (derivata di un prodotto, con $P$ costante e $\frac{d}{dt}e^{At}=Ae^{At}=e^{At}A$, per cui la $A$ si può mettere dove serve), quindi

$$A'Q+QA=\int_0^{+\infty}\frac{d}{dt}\big(e^{A't}Pe^{At}\big)\,dt=\Big[e^{A't}Pe^{At}\Big]_0^{+\infty}=0-P=-P$$

> [!quote] Dal libro — Teorema 3.4.6 e uso pratico
> "In un sistema lineare $\dot x=Ax$, il punto di equilibrio $x_e=0$ è stabile asintoticamente globalmente se, comunque si fissi una matrice $P$ simmetrica e definita positiva, l'equazione matriciale $A'Q+QA=-P$ nell'incognita $Q$ ha una soluzione unica, simmetrica e definita positiva." Nelle applicazioni si sceglie di solito $P=I$ e si risolve un sistema lineare di $\frac{n(n+1)}{2}$ equazioni (le incognite di una $Q$ simmetrica). A differenza del caso non lineare, se non c'è soluzione $Q>0$ si può **concludere** che il sistema non è asintoticamente stabile. _(libro, §3.4.2, pp. 129–130)_

> [!example] Dal libro — Esempio 3.4.4
> $A=\begin{psmallmatrix}0&1\\-5&-6\end{psmallmatrix}$, $P=I$. L'equazione $A'Q+QA=-I$ con $Q=\begin{psmallmatrix}q_{11}&q_{12}\\q_{12}&q_{22}\end{psmallmatrix}$ dà le tre equazioni
> $$-10q_{12}=-1,\qquad q_{11}-6q_{12}-5q_{22}=0,\qquad 2q_{12}-12q_{22}=-1$$
> da cui $q_{12}=\frac1{10}$, $q_{22}=\frac1{10}$, $q_{11}=\frac{11}{10}$. $Q=\frac1{10}\begin{psmallmatrix}11&1\\1&1\end{psmallmatrix}$ ha minori $\frac{11}{10}>0$ e $\det Q=\frac{10}{100}>0$: è definita positiva, quindi il sistema è asintoticamente stabile (infatti gli autovalori sono $-1$ e $-5$). _(libro, §3.4.2, p. 131)_

## Stabilità dei sistemi lineari a tempo discreto

Vedi [[TDS - Stabilità]].

> [!note] Annotazioni di Simone
> Il titolo negli appunti è "Sistemi **non** lineari a tempo discreto": Simone ha cancellato a mano il "non", ha aggiunto davanti "STABILITÀ dei" e ha scritto **"Correzione titolo"** e **"Poche Differenze"**. In effetti la sezione tratta i sistemi **lineari**.

In generale un sistema a tempo discreto è descritto da $x(t+1)=f(x(t),u(t))$. I punti di equilibrio sono quelli in cui il sistema resta fermo: se lo stato è $x_e$, anche "la volta dopo" $x(t+1)$ è $x_e$:

$$x_e=f(x_e,0)$$

Trovati gli equilibri $x_{e1},\dots,x_{ek}$ se ne studia la stabilità uno per uno, con le **stesse definizioni** del continuo:

$$\forall\varepsilon>0\ \exists\delta(\varepsilon)>0\ \text{t.c.}\ \|x_0-x_e\|<\delta(\varepsilon)\ \Rightarrow\ \|x(t)-x_e\|<\varepsilon$$

### Stabilità interna

Se il sistema è lineare, $x(t+1)=Ax(t)+Bu(t)$, gli equilibri (con $u=0$) si trovano da

$$x_e=Ax_e\iff(A-I)x_e=0$$

Le soluzioni sono come nel continuo: $x_e=0$ è sempre soluzione e, se ce n'è più d'una, sono infinite; la differenza è che invece di $A$ va studiata $A-I$ (ci sono altri equilibri se $1$ è autovalore di $A$).

> [!note] Annotazioni di Simone
> A mano: **"Trova Punti Equilibrio"** e, a margine, **"STABILITÀ INTERNA"**.

Come nel continuo $x(t)=\Phi(t)x_0$, l'equilibrio non si muove ($x_e=\Phi(t)x_e$) e

$$\|x(t)-x_e\|=\|\Phi(t)x_0-\Phi(t)x_e\|\le\|\Phi(t)\|\,\|x_0-x_e\|<\varepsilon$$

Si conclude che $\Phi(t)$ deve essere **limitata**, $\|\Phi(t)\|\le\Phi_0$. L'unica differenza è che ora $\Phi(t)=A^t$, e i modi naturali seguono leggi $\lambda^t$ (caso reale) o $\rho^t(\cdots)$ (caso complesso): perché siano limitati deve essere $|\lambda|\le1$ e $\rho\le1$, in generale $|\lambda|\le1$. Si ha stabilità asintotica se

$$\lim_{t\to+\infty}\|x(t)-x_e\|=0\iff\lim_{t\to+\infty}\|\Phi(t)\|=0\iff|\lambda_i|<1$$

> [!warning] Correzione
> Gli appunti scrivono "affinché il sistema sia stabile deve risultare rispettivamente $\lambda\le1$ e $\rho\le1$". Per gli autovalori reali la condizione è $|\lambda|\le1$, non $\lambda\le1$: per esempio $\lambda=-2$ è minore di 1 ma $(-2)^t$ diverge in modo alternato (vedi [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Calcolo di $A^t$ e modi naturali|lezione 9]]). La conclusione "in generale $|\lambda|\le1$" è quella giusta. Come nel continuo, gli autovalori con $|\lambda|=1$ devono essere regolari (molteplicità geometrica uguale a quella algebrica) perché ci sia stabilità semplice.

> [!note] Annotazione di Simone
> Accanto a $|\lambda|<1$, a mano in rosso: **"DIFFERENZA Consideriamo il modulo ed 1 al posto di 0"**.

### Stabilità esterna

Come nel continuo, il sistema discreto è stabile esternamente se a ingresso limitato corrisponde uscita limitata; al posto dell'integrale c'è la somma:

$$y(t)=\Psi(t)x_0+\sum_{\tau=0}^{t-1}W(t-\tau)u(\tau)\quad\Longrightarrow\quad\|y(t)\|\le\dots\le\|\Psi(t)\|\,\|x_0\|+\sum_{\tau=0}^{t-1}\|W(t-\tau)\|\,U$$

La dimostrazione è la stessa del continuo ([[11 - TDS - Punti di equilibrio e stabilità#Stabilità esterna|lezione 11]]), e si ha stabilità esterna se

$$\begin{cases}|\Lambda_o|\le1\\|\Lambda_{e,o}|<1\end{cases}$$

> [!note] Annotazioni di Simone
> A margine: **"STABILITÀ ESTERNA"**; sotto le condizioni: **"Anche qui la differenza sta solo nel modulo e l'1 al posto dello 0 ⇒ NON POSSO USARE ROUTH MA JURY (credo)"**.

| | Tempo continuo | Tempo discreto |
|---|---|---|
| equilibri ($u=0$) | $Ax_e=0$ | $(A-I)x_e=0$ |
| stabilità semplice | $\mathrm{Re}(\lambda_i)\le0$ | $|\lambda_i|\le1$ |
| stabilità asintotica | $\mathrm{Re}(\lambda_i)<0$ | $|\lambda_i|<1$ |
| stabilità esterna | $\mathrm{Re}(\Lambda_o)\le0$, $\mathrm{Re}(\Lambda_{e,o})<0$ | $|\Lambda_o|\le1$, $|\Lambda_{e,o}|<1$ |
| regione "buona" | semipiano sinistro | interno del cerchio unitario |

La differenza fondamentale è che non conta la parte reale ma il **modulo**, e c'è **1** al posto di **0**. Il criterio di Routh, che dice se la parte reale delle radici è negativa, **non è più utilizzabile direttamente**: serve un altro criterio. Come lo si ottiene (trasformando il problema in modo da poter riusare Routh) è l'argomento della [[14 - TDS - Stabilità nel tempo discreto ed esempi|prossima lezione]].
