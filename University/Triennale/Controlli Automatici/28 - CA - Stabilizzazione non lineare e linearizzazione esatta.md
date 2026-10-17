---
title: "Stabilizzazione non lineare e linearizzazione esatta"
aliases:
  - "CA — Stabilizzazione non lineare e linearizzazione esatta"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "270-297"
class_label: "19/05"
---

# Stabilizzazione non lineare e linearizzazione esatta

> [!abstract]
> Questa lezione sviluppa stabilizzazione non lineare e linearizzazione esatta seguendo il blocco delle pagine 270–297 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 19/05. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[27 - CA - LaSalle linearizzazione e studio degli equilibri]].

## Equilibrio forzato e progetto locale

Vedi [[CA - Equilibrio forzato]] · [[CA - Stabilizzazione mediante approssimazione]].

Per $\dot x=f(x,u)$ si vuole rendere AS uno stato operativo $x_e$. Prima si cerca $u_e$ tale che $f(x_e,u_e)=0$: senza questa condizione il punto desiderato non è un equilibrio del sistema controllato. Si traslano $z=x-x_e$, $v=u-u_e$ e si calcolano $A=f_x(x_e,u_e)$ e $B=f_u(x_e,u_e)$.

Se $(A,B)$ è stabilizzabile, si sceglie $v=Kz$ con $A+BK$ Hurwitz. Il criterio indiretto garantisce stabilità AS **locale** del sistema non lineare con $u=u_e+K(x-x_e)$. Non garantisce da solo GAS o un bacino grande.

Per stimare il dominio, si risolve $(A+BK)^TP+P(A+BK)=-Q$, con $Q\succ0$, e si prova $V=z^TPz$ sul modello non lineare completo. Il segno dei termini residui delimita i sottolivelli invarianti. Se la linearizzazione non è stabilizzabile, il metodo fallisce, ma potrebbe esistere una legge non lineare stabilizzante.

_(Dispensa commentata, pagine PDF 270–277; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 270
> ![[CA-p270-1.jpg]]
> Le slide aprono il problema di stabilizzazione non lineare mediante retroazione dello stato.

> [!example]- Materiale originale — pagina PDF 271
> ![[CA-p271-1.jpg]]
> Lo stato operativo desiderato deve diventare un equilibrio del sistema controllato: prima si cerca l'ingresso di equilibrio.

> [!example]- Materiale originale — pagina PDF 272
> ![[CA-p272-1.jpg]]
> Il foglio di richiamo separa comando nominale e feedback delle variazioni e mostra la traslazione nello stato e nell'ingresso.

> [!example]- Materiale originale — pagina PDF 273
> ![[CA-p273-1.jpg]]
> Il controllo lineare è richiamato come caso particolare, mentre la retroazione statica non lineare dipende direttamente dallo stato.

> [!example]- Materiale originale — pagina PDF 274
> ![[CA-p274-1.jpg]]
> Il primo metodo stabilizza la linearizzazione e usa il criterio indiretto per ottenere una garanzia locale sul sistema completo.

> [!example]- Materiale originale — pagina PDF 275
> ![[CA-p275-1.jpg]]
> L'esercizio esplicita Jacobiana rispetto a stato e ingresso e controlla la stabilizzabilità della coppia risultante.

> [!example]- Materiale originale — pagina PDF 276
> ![[CA-p276-1.jpg]]
> La procedura generale sottolinea che il successo della linearizzazione garantisce stabilità locale, mentre il suo fallimento non esclude ogni controllo non lineare.

> [!example]- Materiale originale — pagina PDF 277
> ![[CA-p277-1.jpg]]
> L'equazione di Lyapunov costruisce una candidata quadratica dal lineare stabilizzato, da verificare poi sulla dinamica completa.

## Pendolo attuato e coppia di equilibrio

Vedi [[CA - Controllo del pendolo]] · [[CA - Equazione di Lyapunov]].

Per $m\ell^2\ddot\theta+d\dot\theta+mg\ell\sin\theta=u$, volendo $\theta=\theta_e$, $\dot\theta=0$, la coppia nominale è $u_e=mg\ell\sin\theta_e$. Con $z=(\theta-\theta_e,\dot\theta)$:
$$A=\begin{pmatrix}0&1\\-(g/\ell)\cos\theta_e&-d/(m\ell^2)\end{pmatrix},\quad B=\binom0{1/(m\ell^2)}.$$
Questa coppia è raggiungibile per parametri fisici non degeneri. Si sceglie $K$ per i poli desiderati e si applica $u=u_e+Kz$.

> [!example] Equazione di Lyapunov controllata
> Per $A_c=\begin{pmatrix}0&1\\-1&-1\end{pmatrix}$ e $Q=I$, $P=\begin{pmatrix}3/2&1/2\\1/2&1\end{pmatrix}$ soddisfa $A_c^TP+PA_c=-I$. È DP perché $p_{11}=3/2>0$ e $\det P=5/4>0$. Questa $V$ certifica il lineare globalmente; per il pendolo va ricalcolata $\dot V$ includendo il seno completo.

_(Dispensa commentata, pagine PDF 278–283; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 278
> ![[CA-p278-1.jpg]]
> Il pendolo con attuatore al giunto richiede una coppia di equilibrio che compensi la gravità all'angolo desiderato.

> [!example]- Materiale originale — pagina PDF 279
> ![[CA-p279-1.jpg]]
> Il richiamo fisico e le equazioni del pendolo fissano i parametri e la distinzione tra posizione assoluta e variazione dal punto operativo.

> [!example]- Materiale originale — pagina PDF 280
> ![[CA-p280-1.jpg]]
> Il foglio di progetto confronta i punti di lavoro e la struttura della coppia composta da termine nominale e feedback.

> [!example]- Materiale originale — pagina PDF 281
> ![[CA-p281-1.jpg]]
> La traslazione attorno all'angolo desiderato produce il modello per le variazioni e il relativo termine gravitazionale linearizzato.

> [!example]- Materiale originale — pagina PDF 282
> ![[CA-p282-1.jpg]]
> La coppia linearizzata del pendolo è raggiungibile: il feedback permette di assegnare i poli e introdurre rigidezza e smorzamento desiderati.

> [!example]- Materiale originale — pagina PDF 283
> ![[CA-p283-1.jpg]]
> La soluzione dell'equazione di Lyapunov fornisce una matrice positiva esplicita e una candidata per stimare il bacino locale.

## Cancellazione esatta e trasformazioni di coordinate

Vedi [[CA - Linearizzazione esatta]] · [[CA - Diffeomorfismo]] · [[CA - Dominio della linearizzazione]].

Se il modello ha forma $\dot x=Ax+B\Gamma(x)[u-\alpha(x)]$, con $\Gamma(x)$ invertibile nel dominio considerato, si può scegliere $u=\alpha(x)+\Gamma(x)^{-1}v$ e ottenere esattamente $\dot x=Ax+Bv$. A differenza dell'approssimazione di Taylor, la cancellazione è esatta nel dominio in cui è definita.

Talvolta occorre prima un cambio di coordinate non lineare $z=T(x)$. Per preservare localmente la descrizione dello stato, $T$ deve essere un diffeomorfismo: invertibile, regolare e con inversa regolare nel dominio specificato. Una Jacobiana singolare o un coefficiente di controllo nullo limita il dominio.

> [!example] Controllare segno e dominio
> Per $\dot x_1=a\sin x_2$, $\dot x_2=x_1^2+u$, $a>0$, porre $z_1=x_1$, $z_2=a\sin x_2$. Segue $\dot z_1=z_2$, $\dot z_2=a\cos x_2(x_1^2+u)$. La legge corretta è $u=-x_1^2+v/(a\cos x_2)$. È definita localmente per $|x_2|<\pi/2$, con inversa $x_2=\arcsin(z_2/a)$ e $|z_2|<a$.

> [!warning] Lettura del segno nella formula originale
> Nell'estrazione testuale della p. 287 il segno davanti a $x_1^2$ scompare e la legge può sembrare $u=+x_1^2+v/(a\cos x_2)$. Il controllo tramite sostituzione determina senza ambiguità il **meno**: con il più il termine non lineare raddoppierebbe. La formula sopra è quella verificata algebricamente.

_(Dispensa commentata, pagine PDF 284–288; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 284
> ![[CA-p284-1.jpg]]
> La linearizzazione esatta cancella le non linearità accessibili al comando e produce una dinamica lineare nel dominio valido.

> [!example]- Materiale originale — pagina PDF 285
> ![[CA-p285-1.jpg]]
> L'esempio del pendolo mostra la cancellazione del seno e distingue i termini di compensazione da quelli che stabilizzano la dinamica risultante.

> [!example]- Materiale originale — pagina PDF 286
> ![[CA-p286-1.jpg]]
> La formulazione generale richiede invertibilità del coefficiente del comando; non ogni sistema è immediatamente nella struttura cancellabile.

> [!example]- Materiale originale — pagina PDF 287
> ![[CA-p287-1.jpg]]
> Il cambio di coordinate con il seno permette di portare un esempio nella forma utile: il segno della cancellazione si verifica sostituendo il comando.

> [!example]- Materiale originale — pagina PDF 288
> ![[CA-p288-1.jpg]]
> L'inversa con arcseno chiarisce il dominio in cui la trasformazione è un diffeomorfismo e la legge non presenta singolarità.

## Robustezza e controllo diretto non lineare

Vedi [[CA - Non linearità stabilizzanti]] · [[CA - Robustezza della cancellazione]] · [[CA - Progetto con Lyapunov]].

La cancellazione esatta richiede parametri sufficientemente noti e può eliminare effetti fisici benefici. Per $\dot x=ax-bx^3+u$, $a,b>0$, la legge $u=-kx+bx^3$, $k>a$, cancella il termine cubico e dà $\dot x=-(k-a)x$. Ma basta $u=-kx$: con $V=x^2/2$,
$$\dot V=-(k-a)x^2-bx^4<0\quad(x\ne0),$$
quindi l'origine è GAS senza cancellare il richiamo cubico. Il comando è anche meno oneroso per stati grandi.

Il progetto diretto sceglie una funzione $V$ e cerca un comando che renda negativa $\dot V=\nabla V^Tf(x,u)$. Non ogni termine non lineare è un ostacolo: alcuni aiutano la dissipazione. Se il guadagno del comando si annulla in una regione, la divisione necessaria alla cancellazione potrebbe non essere lecita.

Le ultime pagine confrontano i due approcci su esercizi: si trovano gli equilibri, si verifica il modello linearizzato, si sceglie il comando locale, poi si valuta se una legge non lineare consenta una conclusione più ampia. I casi critici della linearizzazione richiedono ancora il metodo diretto o LaSalle.

_(Dispensa commentata, pagine PDF 289–297; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 289
> ![[CA-p289-1.jpg]]
> La discussione dei limiti evidenzia dipendenza dai parametri, robustezza e possibilità di cancellare effetti fisici benefici.

> [!example]- Materiale originale — pagina PDF 290
> ![[CA-p290-1.jpg]]
> Il termine cubico dissipativo mostra che un feedback lineare può già dare GAS e richiedere meno comando della cancellazione esatta.

> [!example]- Materiale originale — pagina PDF 291
> ![[CA-p291-1.jpg]]
> Il foglio di esercizi confronta stabilizzazione locale, dominio di attrazione e scelta di una legge non lineare più ampia.

> [!example]- Materiale originale — pagina PDF 292
> ![[CA-p292-1.jpg]]
> L'esempio riparte dalla ricerca degli equilibri e dal caso critico della Jacobiana, che richiede un metodo diretto.

> [!example]- Materiale originale — pagina PDF 293
> ![[CA-p293-1.jpg]]
> La candidata scalare identifica il segno della derivata e distingue i punti stabili dalle soglie repulsive.

> [!example]- Materiale originale — pagina PDF 294
> ![[CA-p294-1.jpg]]
> Un secondo esercizio costruisce la funzione energetica e il dominio di segno certo, separando proprietà locali e globali.

> [!example]- Materiale originale — pagina PDF 295
> ![[CA-p295-1.jpg]]
> L'ultimo problema controlla raggiungibilità della linearizzazione e scelta dei guadagni prima del confronto con una legge non lineare.

> [!example]- Materiale originale — pagina PDF 296
> ![[CA-p296-1.jpg]]
> Il confronto dei coefficienti verifica la matrice chiusa ottenuta e le condizioni sui parametri del feedback.

> [!example]- Materiale originale — pagina PDF 297
> ![[CA-p297-1.jpg]]
> La pagina finale riporta i guadagni del progetto: la legge completa deve essere sostituita nel sistema per controllare equilibrio e stabilità.

## Esercizi collegati

[[E08 - CA - Prova finale 2018-2019]] · [[E09 - CA - Prova finale 2019-2020]] · [[E10 - CA - Prova finale 2020-2021]] · [[E11 - CA - Prova finale 2021-2022]] · [[E12 - CA - Prova finale 2022-2023]] · [[E13 - CA - Prova finale 2023-2024 e assegnazione canonica]] · [[E14 - CA - Prova completa del 12 luglio 2019]]
