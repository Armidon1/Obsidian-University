---
title: "Correnti elettriche stazionarie"
aliases:
  - "F2 — Correnti elettriche stazionarie"
tags:
  - fisica-2
  - capitolo
source: "pdf/Fisica Generale - Elettromagnetismo ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "153-194"
---

# Correnti elettriche stazionarie

> [!abstract]
> In regime stazionario le cariche si muovono ma le grandezze macroscopiche restano costanti nel tempo. La conservazione della carica e il bilancio energetico collegano la descrizione locale ai circuiti.
> Percorso del corso: [[MOC - Fisica 2]]. Convenzioni e metodo: [[00 - F2 - Guida allo studio]].

## Corrente e conservazione della carica

Vedi [[F2 - Corrente e conservazione della carica]].

L'intensità $I=dq/dt$ si misura in ampere e ha verso convenzionale del moto delle cariche positive. La densità è $\mathbf J=nq\mathbf v_d$ per un solo tipo di portatori e la corrente attraverso una sezione è $I=\int\mathbf J\cdot d\mathbf S$. Gli elettroni hanno velocità di deriva opposta a $\mathbf J$. Il loro moto termico disordinato non coincide con la deriva. La continuità impone $\partial_t\rho+\nabla\cdot\mathbf J=0$; in regime stazionario $\nabla\cdot\mathbf J=0$.

_(Libro, cap. 4; pagine stampate 145–186; PDF pp. 153–194.)_

## Legge di Ohm e modello di conduzione

Vedi [[F2 - Legge di Ohm e modello di conduzione]].

Un materiale ohmico isotropo soddisfa $\mathbf J=\sigma\mathbf E$. Per un filo omogeneo di lunghezza $\ell$ e sezione $A$, $R=\rho_e\ell/A$, con resistività $\rho_e=1/\sigma$, e $\Delta V=RI$. Nel modello classico di Drude $\sigma=nq^2\tau/m$: il campo accelera i portatori e gli urti ne limitano la velocità media di deriva. La legge di Ohm richiede condizioni fisiche appropriate, in particolare una temperatura controllata; non è una legge di tutti i bipoli.

_(Libro, cap. 4; pagine stampate 145–186; PDF pp. 153–194.)_

## Resistenze, generatori e leggi di Kirchhoff

Vedi [[F2 - Resistenze, generatori e leggi di Kirchhoff]].

In serie $R_{\mathrm{eq}}=\sum_iR_i$; in parallelo $1/R_{\mathrm{eq}}=\sum_i1/R_i$. Un generatore ha forza elettromotrice $\mathcal E$, lavoro delle forze non elettrostatiche per unità di carica. Con resistenza interna $r$ e corrente erogata $I$, la tensione ai morsetti è $V=\mathcal E-rI$.

La legge dei nodi $\sum I=0$ deriva dalla conservazione della carica senza accumulo al nodo. La legge delle maglie somma algebricamente salti di tensione e f.e.m.; in presenza di flussi magnetici variabili va incluso il contributo indotto. I versi di corrente si scelgono: un risultato negativo li corregge.

![[F2-p164-1.png]]

*Figura 4-13: due resistenze in parallelo condividono gli stessi nodi e la stessa tensione. La corrente in ingresso si divide fra i rami e si ricompone in uscita; si sommano le conduttanze, non le resistenze.* _(Libro, p. 156; PDF p. 164.)_

_(Libro, cap. 4; pagine stampate 145–186; PDF pp. 153–194.)_

## Potenza, effetto Joule e misure

Vedi [[F2 - Potenza, effetto Joule e misure]].

Con convenzione passiva un resistore assorbe $\mathcal P=VI=RI^2=V^2/R$, trasformando energia elettrica in energia interna. Localmente la densità di potenza è $\mathbf J\cdot\mathbf E$. Un amperometro si collega in serie e idealmente ha resistenza nulla; un voltmetro in parallelo e idealmente ha resistenza infinita. Gli strumenti reali modificano il circuito: valutare il loro carico è parte della misura. Una f.e.m. non è una forza meccanica: ha dimensioni di tensione.

_(Libro, cap. 4; pagine stampate 145–186; PDF pp. 153–194.)_

## Transitorio RC e altri meccanismi di conduzione

Vedi [[F2 - Transitorio RC e altri meccanismi di conduzione]].

Un condensatore rompe la stazionarietà durante carica e scarica. In un circuito RC alimentato da un gradino $\mathcal E$, inizialmente scarico,
$$q(t)=C\mathcal E(1-e^{-t/RC}),\qquad I(t)=\frac{\mathcal E}{R}e^{-t/RC}.$$
In scarica $q=q_0e^{-t/RC}$. La tensione del condensatore non salta con correnti finite. A carica completa il generatore ha fornito $C\mathcal E^2$: metà è immagazzinata e metà dissipata nel modello ideale resistivo. Nei liquidi conducono ioni, nei gas ionizzati elettroni e ioni; effetti termoelettrici e dispositivi fotovoltaici convertono forme diverse di energia. La superconduttività include resistenza continua nulla e comportamento magnetico caratteristico, non equivale semplicemente a un conduttore ordinario molto buono.

_(Libro, cap. 4; pagine stampate 145–186; PDF pp. 153–194.)_

## Conduzione nei mezzi e conversione energetica

Vedi [[F2 - Conduzione nei mezzi e conversione energetica]].

Negli elettroliti la corrente è trasporto ionico e può accompagnare reazioni agli elettrodi. Nei gas la ionizzazione genera portatori e può portare a scariche: non basta una resistività costante per descriverle. L'effetto Seebeck collega una differenza di temperatura a una f.e.m.; Peltier descrive uno scambio termico a una giunzione attraversata da corrente, distinto dal riscaldamento Joule. Una cella fotovoltaica usa l'assorbimento della radiazione e la separazione dei portatori; una cella a combustibile converte energia chimica con reazioni elettrochimiche. Nel superconduttore l'espulsione del campo nel regime di Meissner distingue la fase superconduttiva dall'idealizzazione di un metallo con sola resistenza nulla.

_(Libro, cap. 4; pagine stampate 145–186; PDF pp. 153–194.)_

## Derivazione guidata

Nella carica RC la maglia dà $\mathcal E-R\dot q-q/C=0$. Introduci la distanza dall'equilibrio $u=q-C\mathcal E$: allora $\dot u=-u/(RC)$. La soluzione è $u(t)=u(0)e^{-t/RC}$, cioè $q(t)=C\mathcal E+[q(0)-C\mathcal E]e^{-t/RC}$. La soluzione usuale con condensatore scarico è un caso particolare. La costante $RC$ ha dimensioni di tempo e descrive il rilassamento verso il nuovo equilibrio.

_(Libro, cap. 4; pagine stampate 145–186; PDF pp. 153–194.)_

## Esempio svolto

> [!example] Applicazione originale
> Due resistenze da $6\,\Omega$ e $3\,\Omega$ in parallelo hanno equivalente $2\,\Omega$. Ai capi di $12\,\mathrm V$ assorbono $2$ e $4\,\mathrm A$, totale $6\,\mathrm A$; la potenza totale è $72\,\mathrm W$. Per $R=10\,\mathrm{k\Omega}$ e $C=100\,\mathrm{\mu F}$, $\tau=RC=1\,\mathrm s$ e dopo una costante di tempo la tensione raggiunge il $63{,}2\%$ del valore finale.

## Richiami matematici

[[06 - AN1 - Calcolo Integrale]] · [[GEO - Sistemi lineari generali]].

## Verifica attiva

Come modifica una misura un voltmetro con resistenza finita?

> [!check]- Risposta ragionata
> Aggiunge un ramo in parallelo e assorbe corrente. La tensione letta può differire da quella del circuito privo di strumento, soprattutto se la sua resistenza non è grande rispetto a quella equivalente vista ai morsetti.

## Navigazione

Precedente: [[03 - F2 - Conduttori, condensatori e dielettrici]] · Successivo: [[05 - F2 - Campi magnetici stazionari]].
