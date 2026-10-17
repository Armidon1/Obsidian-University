---
title: Punti di equilibrio e stabilità
aliases:
  - TDS — Punti di equilibrio e stabilità
tags:
  - teoria-dei-sistemi
  - stabilita
  - punti-di-equilibrio
  - stabilita-esterna
source: 1_Appunti Uniti TdS Patreon_241009_112348.pdf (pp. 41–45); libro Monaco et al., §3.1–3.2, §3.3 (inizio)
---

# Punti di equilibrio e stabilità

> [!abstract] Scopo della lezione
> Si passa da un'analisi "puntuale" delle evoluzioni (i [[06 - TDS - Modi naturali|modi naturali]]) a una domanda **qualitativa**: se perturbo un sistema fermo in equilibrio, resta vicino all'equilibrio, ci torna, o se ne allontana?
> - si definiscono i **punti di equilibrio** e la **stabilità semplice** e **asintotica** (definizione formale con $\varepsilon$ e $\delta$);
> - per i sistemi lineari si traduce tutto in condizioni sulla **matrice di transizione** e quindi sulla **parte reale degli autovalori**;
> - si introduce la **stabilità esterna** (ingresso limitato → uscita limitata), legata ai modi osservabili ed eccitabili;
> - si vede una **condizione necessaria** sui coefficienti del polinomio caratteristico, che prepara il [[12 - TDS - Criterio di Routh e linearizzazione|criterio di Routh]].
>
> Indice: [[MOC - Teoria dei Sistemi]].

> [!note] Annotazione di Simone
> In testa alla lezione, a mano in rosso: **"STABILITÀ"**.

## Punti di equilibrio e dinamica

Vedi [[TDS - Punti di equilibrio]].

È un argomento più qualitativo e generale: come si comporta un sistema se sollecitato da un ingresso o lasciato libero? In generale, senza limitarsi ai sistemi lineari e stazionari, un sistema è descritto da

$$\begin{cases}\Delta x(t)=f\big(x(t),u(t)\big)\\y(t)=h\big(x(t),u(t)\big)\end{cases}$$

dove $\Delta x$ è $\dot x$ nel tempo continuo e $x(t+1)$ nel discreto. Concentriamoci sull'equazione dello stato nel caso continuo (il discreto è analogo):

$$\dot x(t)=f\big(x(t),u(t)\big)$$

Esistono condizioni tali che, se il sistema parte da lì, **resta fermo**? Un punto del genere si chiama **punto di equilibrio** $x_e$ (possono essercene più d'uno), ed è tale da non far variare lo stato:

$$f(x_e,u_e)=0$$

per un qualche ingresso costante $u_e$. Molto spesso si studia il caso senza ingresso, $u_e=0$: gli equilibri sono le soluzioni di $f(x_e,0)=0$, che in generale è un sistema **non lineare**, quindi non si sa a priori quante soluzioni abbia (possono anche essere zero).

> [!note] Nel tempo discreto
> L'equilibrio è un punto fisso: $x(t+1)=x(t)$, cioè $f(x_e,u_e)=x_e$. Per un sistema lineare $x(t+1)=Ax(t)$ diventa $(A-I)x_e=0$.

Ci interessa cosa succede se, invece di partire esattamente da $x_e$, si parte da un punto $x_0$ **vicino** a $x_e$. Non essendo un equilibrio, il sistema evolve, e ci sono tre possibilità:
- il sistema resta in un intorno di $x_e$: **stabilità semplice**;
- il sistema tende a $x_e$: **stabilità asintotica**;
- il sistema si allontana: **instabilità**.

## Definizione formale di stabilità

Vedi [[TDS - Stabilità]].

**Stabilità semplice.** Un punto di equilibrio $x_e$ è **stabile semplicemente** se, comunque si prenda un intorno (di raggio $\varepsilon$) del punto, esiste un altro intorno (di raggio $\delta(\varepsilon)$) tale che, partendo da punti di quest'ultimo, l'evoluzione resta per sempre nel primo:

$$\forall\varepsilon>0\ \exists\delta(\varepsilon)>0\ \text{t.c.}\ \|x_0-x_e\|\le\delta(\varepsilon)\ \Rightarrow\ \|x(t)-x_e\|\le\varepsilon,\ \ \forall t\ge0\tag{$\spadesuit$}$$

Si usa la norma $\|\cdot\|$ perché si lavora con vettori.

![[TDS-L11-01.png]]

Il punto rosso è $x_e$, il cerchio verde l'intorno di raggio $\varepsilon$ (dove deve restare l'evoluzione), quello blu l'intorno di raggio $\delta(\varepsilon)$ (da cui si parte). Informalmente: c'è stabilità semplice se, scelto $x_0$ abbastanza vicino a $x_e$, l'evoluzione resta "vicina" a $x_e$ per tutto il tempo. Attenzione all'ordine dei quantificatori: è $\varepsilon$ a essere scelto per primo (arbitrariamente piccolo), e la definizione deve valere per **ogni** $\varepsilon$.

**Stabilità asintotica.** Se, partendo vicino all'equilibrio, ci si avvicina sempre di più a esso, si ha stabilità asintotica: $x_e$ è **stabile asintoticamente** se vale la ($\spadesuit$) e, **in più**, la distanza dall'equilibrio tende a zero:

$$\lim_{t\to+\infty}\|x(t)-x_e\|=0$$

Queste definizioni valgono indifferentemente per il tempo continuo e discreto.

> [!note] Annotazioni di Simone
> A margine, a mano: **"definizione Formale STABILITÀ SEMPLICE"** accanto alla ($\spadesuit$), **"STABILITÀ ASINTOTICA"** accanto alla seconda definizione e **"in più →"** accanto al limite.

> [!quote] Dal libro — stabilità esponenziale, globale, dei moti
> Il libro aggiunge altre definizioni:
> - **esponenziale**: esistono $\lambda>0$ e $\delta_\varepsilon$ tali che $\|x(t)-x_e\|\le\varepsilon e^{-\lambda(t-t_0)}$; implica l'asintotica ma non viceversa;
> - **asintotica globale**: la convergenza vale per **ogni** stato iniziale, non solo vicino a $x_e$. Le altre proprietà sono **locali**;
> - la stabilità di un **moto** $x(t)$ (non solo di un equilibrio) si riconduce a quella dell'origine per lo **scostamento** $\xi=x_p-x$ tra moto perturbato e moto nominale.
>
> Osserva anche che la stabilità asintotica "può essere verificata solo se, nell'insieme dei punti di equilibrio, $x_e$ è un punto isolato". _(libro, §3.1, pp. 101–103)_

## Definizione operativa di stabilità

> [!note] Annotazioni di Simone
> Accanto al titolo: **"(Come Operare)"**; accanto a $\dot x=Ax+Bu$: **"Per il caso di un sistema discreto è uguale"**.

Con un sistema come $\dot x=x^2-1$ gli equilibri si trovano subito ($x_e^2-1=0\iff x_{e,1}=1,\ x_{e,2}=-1$), ma non si può verificare in pratica la definizione per "ogni" intorno di raggio $\varepsilon$: serve una definizione **operativa**. Consideriamo un sistema **lineare**

$$\dot x=Ax+Bu$$

Gli equilibri si trovano annullando il secondo membro con $u=0$:

$$\boxed{Ax_e=0}$$

È un sistema lineare omogeneo, quindi i punti di equilibrio sono **uno o infiniti**: se ce n'è uno solo è $x_e=0$ (che è sempre soluzione); se $\det A=0$ sono tutto il sottospazio $\ker A$.

> [!note] Annotazione di Simone
> Accanto a "uno o infiniti": **"Infiniti se il sistema risulta parametrico"**.

Ignorando l'ingresso, $x(t)=\Phi(t)x_0$, e l'equilibrio non evolve: $x_e(t)=\Phi(t)x_e=x_e$. Allora

$$\|x(t)-x_e\|=\|\Phi(t)x_0-\Phi(t)x_e\|=\|\Phi(t)(x_0-x_e)\|\le\|\Phi(t)\|\,\|x_0-x_e\|$$

e la condizione $\|x(t)-x_e\|\le\varepsilon$ è garantita se $\|\Phi(t)\|\le\frac{\varepsilon}{\|x_0-x_e\|}$.

> [!warning] Correzione
> Negli appunti i passaggi sono scritti con "$\iff$": $\|\Phi(t)x_0-\Phi(t)x_e\|\le\varepsilon\iff\|\Phi(t)\|\,\|x_0-x_e\|\le\varepsilon$. In realtà tra $\|\Phi(t)(x_0-x_e)\|$ e $\|\Phi(t)\|\,\|x_0-x_e\|$ c'è solo una disuguaglianza ($\le$). La conclusione è comunque giusta, come mostra il libro: **condizione necessaria e sufficiente** di stabilità è che $\Phi(t)$ sia **limitata**, $\|\Phi(t)\|\le k$; basta poi scegliere $\delta(\varepsilon)=\varepsilon/k$. _(libro, §3.2.1, pp. 104–105)_

Quindi un punto è stabile se $\Phi(t)$ è **limitata**, e questo succede quando i modi naturali sono limitati: quelli aperiodici ($e^{\lambda t}$) se $\lambda\le0$, quelli pseudoperiodici ($e^{\alpha t}(\cdots)$) se $\alpha\le0$. Combinando: gli autovalori devono avere $\mathrm{Re}(\lambda_i)\le0$.

Questa condizione **non dipende dal singolo punto di equilibrio**: se il sistema ha infiniti equilibri, basta che uno sia stabile semplicemente perché lo siano tutti.

Per la stabilità asintotica serve anche

$$\lim_{t\to+\infty}\|x(t)-x_e\|=0\iff\lim_{t\to+\infty}\|\Phi(t)\|\cdot\|x_0-x_e\|=0\iff\lim_{t\to+\infty}\|\Phi(t)\|=0$$

cioè tutti i modi naturali devono **convergere**: $\mathrm{Re}(\lambda_i)<0$. In sintesi:

$$\begin{cases}\|\Phi(t)\|\le\dfrac{\varepsilon}{\|x_0-x_e\|}&\iff\ \mathrm{Re}(\lambda_i)\le0\quad\text{(stabilità semplice)}\\[2mm]\lim\limits_{t\to+\infty}\|\Phi(t)\|=0&\iff\ \mathrm{Re}(\lambda_i)<0\quad\text{(stabilità asintotica)}\end{cases}$$

Il sistema **non è stabile** se ha almeno un autovalore con parte reale positiva.

> [!note] Annotazione di Simone
> In un riquadro accanto alla formula: **"★ STABILITÀ SEMPLICE se Re(λ) ≤ 0 dove i λᵢ con Re(λᵢ)=0 hanno mg(λᵢ)=1"**; sopra e sotto le condizioni: "Stabilità semplice", "Stabilità Asintotica".

> [!important] Il caso $\mathrm{Re}(\lambda)=0$
> La condizione $\mathrm{Re}(\lambda_i)\le0$ basta se la matrice è **regolare**. Se un autovalore con parte reale nulla ha molteplicità geometrica **minore** di quella algebrica, compaiono modi del tipo $t\,e^{0\cdot t}=t$, che divergono (lo si vedrà con le [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori|catene di autovettori]]). Il libro lo dice così: gli autovalori sull'asse immaginario sono ammessi "solo se di ordine uno", cioè se per essi molteplicità algebrica e geometrica coincidono.

> [!quote] Dal libro — stabilità interna e piano complesso
> Poiché nei sistemi lineari la stabilità locale è comune a tutti gli equilibri, e quella asintotica locale implica quella globale, il libro parla di **stabilità interna** del sistema. La Figura 3.3 del libro riassume: autovalori nel semipiano sinistro aperto → stabilità asintotica; sull'asse immaginario con ordine geometrico 1 → stabilità semplice; sull'asse immaginario con ordine maggiore di 1, o nel semipiano destro → instabilità. _(libro, §3.2.1, pp. 106–108)_

| Posizione degli autovalori | Stabilità |
|---|---|
| tutti con $\mathrm{Re}(\lambda_i)<0$ | asintotica (e globale) |
| $\mathrm{Re}(\lambda_i)\le0$, quelli con $\mathrm{Re}=0$ regolari | semplice |
| almeno uno con $\mathrm{Re}>0$, oppure $\mathrm{Re}=0$ non regolare | instabilità |

## Stabilità asintotica nei sistemi lineari

Consideriamo due punti di equilibrio $x_{e,1}$ e $x_{e,2}$ "vicini" tra loro.

![[TDS-L11-02.png]]

Per la stabilità semplice non c'è problema: partendo dall'intorno blu di raggio $\delta(\varepsilon)$ si resta in quello verde di raggio $\varepsilon$. Ma la stabilità asintotica non può valere: partendo da $x_{e,2}$ il sistema **resta fermo lì** (è un equilibrio) e non si avvicina mai a $x_{e,1}$. Si potrebbe rimediare prendendo un intorno più piccolo, che non contenga $x_{e,2}$:

![[TDS-L11-03.png]]

Nei sistemi lineari però questo non si può fare: se gli equilibri non sono solo $x_e=0$, sono infiniti e formano un intero **sottospazio** (per esempio una retta):

![[TDS-L11-04.png]]

Qualunque intorno, per quanto piccolo, contiene infiniti altri equilibri (i punti della retta nera). Quindi, **in un sistema lineare, può esserci stabilità asintotica solo se l'equilibrio è unico ($x_e=0$)**; altrimenti al più stabilità semplice.

> [!tip] Il collegamento con gli autovalori
> Se esistono equilibri diversi da 0, l'equazione $Ax_e=0$ si può leggere come $(A-\lambda I)x_e=0$ con $\lambda=0$: **$0$ è un autovalore** di $A$. Allora la condizione $\mathrm{Re}(\lambda_i)<0\ \forall i$ è violata, e la stabilità asintotica è automaticamente esclusa. Le due strade (geometrica e algebrica) portano alla stessa conclusione.

## Stabilità esterna

Vedi [[TDS - Stabilità esterna]].

Guardando il sistema **dall'esterno**, senza vedere cosa succede dentro, si può definire la **stabilità esterna** (contrapposta alla stabilità **interna** studiata finora): un sistema ha stabilità esterna se a ogni ingresso **limitato** corrisponde un'uscita **limitata**:

$$\forall\ \|u(t)\|\le U\ \ \Rightarrow\ \ \|y(t)\|\le Y\quad\forall t\ge0$$

(in inglese *BIBO*, *bounded input – bounded output*). In un sistema lineare, posto $t_0=0$, usando la disuguaglianza triangolare e quella per gli integrali:

$$\begin{aligned}
\|y(t)\|&=\left\|\Psi(t)x_0+\int_0^tW(t-\tau)u(\tau)\,d\tau\right\|\le\|\Psi(t)x_0\|+\left\|\int_0^tW(t-\tau)u(\tau)\,d\tau\right\|\\
&\le\|\Psi(t)\|\,\|x_0\|+\int_0^t\|W(t-\tau)\|\,\underbrace{\|u(\tau)\|}_{\le U}\,d\tau\le\|\Psi(t)\|\,\|x_0\|+U\int_0^t\|W(t-\tau)\|\,d\tau
\end{aligned}$$

Questa quantità è limitata se lo sono entrambi gli addendi: $\Psi(t)$ deve essere limitata e l'integrale di $\|W\|$ deve restare finito, il che (per le funzioni esponenziali che compongono $W$) avviene se $W$ tende a zero:

$$\begin{cases}\|\Psi(t)\|\le\Psi_0\\\lim_{t\to+\infty}\|W(t)\|=0\end{cases}$$

- La prima condizione vale se i modi in $\Psi(t)$, cioè quelli **osservabili**, sono limitati: parte reale degli autovalori osservabili $\le0$.
- La seconda vale se i modi in $W(t)$, cioè quelli **osservabili ed eccitabili**, sono **convergenti**: parte reale $<0$.

In definitiva l'uscita è limitata se

$$\begin{cases}\mathrm{Re}(\Lambda_o)\le0\\\mathrm{Re}(\Lambda_{e,o})<0\end{cases}$$

(con la notazione insiemistica di [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Osservabilità ed eccitabilità nel tempo discreto|lezione 9]]). Le due condizioni sono indipendenti e una non esclude l'altra. Spesso si assume che il sistema parta da condizioni iniziali nulle ($x_0=0$): allora i termini con $x_0$ spariscono e per la stabilità esterna resta solo $\mathrm{Re}(\Lambda_{e,o})<0$.

> [!note] Annotazioni di Simone
> Accanto alle due condizioni, a mano: **"Devono valere entrambi"**, **"considerazione solo gli autovalori Osservabili"** (prima riga), **"considerazione gli autovalori Osservabili ed Eccitabili"** (seconda riga) e **"STABILITÀ ESTERNA"**.

> [!example] Stabilità esterna senza stabilità interna
> Nell'[[10 - TDS - Esempio a tempo discreto e campionamento#Eccitabilità e osservabilità|esempio della lezione 10]] $\Lambda_{e,o}=\emptyset$: con $x_0=0$ il sistema è esternamente stabile ($W\equiv0$), ma internamente instabile (autovalori $2$ e $1\pm j$). La stabilità esterna guarda solo la parte "visibile" del sistema.

> [!warning] Precisazione
> Per la limitatezza dell'integrale, in generale non basta che $W(t)\to0$: serve che $\int_0^\infty\|W(\tau)\|d\tau<\infty$ (una funzione come $1/t$ tende a zero ma ha integrale infinito). Nei sistemi lineari stazionari a dimensione finita $W$ è combinazione di modi naturali, e per questi le due condizioni coincidono: tendono a zero se e solo se decadono esponenzialmente.

## Segno degli autovalori senza calcolarli

Non interessa il **valore** degli autovalori, ma solo se sono positivi, negativi o nulli; e c'è un modo (lo si vedrà nella [[12 - TDS - Criterio di Routh e linearizzazione|prossima lezione]]) per verificarne il segno **senza trovarli**. Si parte dal polinomio caratteristico fattorizzato:

$$p(\lambda)=a_n\lambda^n+a_{n-1}\lambda^{n-1}+\dots+a_1\lambda+a_0=a_n(\lambda-\lambda_1)(\lambda-\lambda_2)\cdots(\lambda-\lambda_n)$$

Se tutti gli autovalori sono reali con $\mathrm{Re}(\lambda_i)<0$, tutti i fattori sono del tipo $(\lambda+|\lambda_i|)$:

$$p(\lambda)=a_n(\lambda+|\lambda_1|)\cdots(\lambda+|\lambda_n|)$$

I coefficienti $a_0,\dots,a_n$ nascono da somme di prodotti di numeri positivi, quindi (a meno del segno di $a_n$) sono tutti positivi. Avere tutti i coefficienti dello **stesso segno** è quindi **condizione necessaria** perché le radici abbiano parte reale negativa: se il polinomio ha coefficienti non tutti dello stesso segno (o qualche coefficiente nullo), ci sono sicuramente radici a parte reale non negativa.

> [!quote] Dal libro — anche con radici complesse
> Il ragionamento vale anche con coppie complesse a parte reale negativa: i due fattori corrispondenti si scrivono $(\lambda+|\alpha_i|-j\omega)(\lambda+|\alpha_i|+j\omega)=(\lambda+|\alpha_i|)^2+\omega^2$, che ha coefficienti positivi. Per $n=2$ la condizione è anche sufficiente (regola di Cartesio: a ogni **permanenza** di segno tra coefficienti consecutivi corrisponde una radice a parte reale negativa, a ogni **variazione** una a parte reale positiva). _(libro, §3.3, p. 109)_

> [!example] Non è sufficiente per $n\ge3$
> $p(\lambda)=\lambda^3+\lambda^2+\lambda+1=(\lambda+1)(\lambda^2+1)$ ha tutti i coefficienti positivi, ma radici $\pm j$ sull'asse immaginario. Per $n\ge3$ serve il criterio di Routh.
