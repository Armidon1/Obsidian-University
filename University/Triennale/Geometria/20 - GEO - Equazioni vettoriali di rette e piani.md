---
title: "Equazioni vettoriali di rette e piani"
aliases:
  - "GEO — Equazioni vettoriali di rette e piani"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "20"
pdf_pages: "321–330"
---

# Equazioni vettoriali di rette e piani

> [!abstract] Scopo e percorso
> Geometria affine nel piano e nello spazio. Questa nota segue il capitolo 20 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 20.1 - Equazioni vettoriali di rette

Vedi [[GEO - Equazione vettoriale di una retta]].

Una retta per $P_0$ di direzione $v\ne0$ ha equazione vettoriale

$$P=P_0+tv,\qquad t\in\mathbb R.$$

Se sono dati due punti distinti $P_0,P_1$, si sceglie $v=P_1-P_0$. Moltiplicare $v$ per uno scalare non nullo cambia il parametro ma non la retta. Il parametro descrive quanto ci si sposta da $P_0$ lungo la direzione scelta.

_(Accascina–Monti, § 20.1, libro pp. 305–307; PDF pp. 321–323.)_

![[GEO-p322-1.png|650]]

**Lettura della figura (PDF p. 322, libro p. 306).** La costruzione lega il punto base a un direttore trasportato nell’origine: variando il coefficiente si percorre tutta la retta.

## 20.2 - Semirette e segmenti

Vedi [[GEO - Segmenti e semirette vettoriali]].

Con $P=P_0+t(P_1-P_0)$, $t=0$ restituisce $P_0$ e $t=1$ restituisce $P_1$. Il segmento chiuso corrisponde a $0\le t\le1$, quello aperto a $0<t<1$.

La semiretta con origine $P_0$ verso $P_1$, includendo l’origine, usa $t\ge0$; escludendo l’origine usa $t>0$. È necessario dichiarare se gli estremi o il bordo sono inclusi.

Per $P_0=(1,0)$ e $P_1=(3,2)$ si ha $P=(1+2t,2t)$. Il punto medio si ottiene per $t=1/2$.

_(Accascina–Monti, § 20.2, libro pp. 307–308; PDF pp. 323–324.)_

![[GEO-p323-1.png|650]]

**Lettura della figura (PDF p. 323, libro p. 307).** Il disegno confronta gli spostamenti da punti diversi della retta e chiarisce la parametrizzazione delle sue semirette.

## 20.3 - Equazioni vettoriali di piani

Vedi [[GEO - Equazione vettoriale di un piano]].

Un piano ha equazione $P=P_0+su+tv$, con $u,v$ indipendenti e $s,t\in\mathbb R$. Tre punti non allineati $P_0,P_1,P_2$ danno $u=P_1-P_0$ e $v=P_2-P_0$.

Se i direttori fossero dipendenti, la parametrizzazione descriverebbe al massimo una retta. L’indipendenza è quindi un requisito geometrico, non una semplice formalità.

_(Accascina–Monti, § 20.3, libro pp. 308–310; PDF pp. 324–326.)_

![[GEO-p325-1.png|650]]

**Lettura della figura (PDF p. 325, libro p. 309).** I piani paralleli collegano la parametrizzazione affine a due direzioni indipendenti nel piano vettoriale per l’origine.

## 20.4 - Allineamento e complanarità

Vedi [[GEO - Criteri vettoriali di allineamento e complanarità]].

I punti $P_0,\ldots,P_k$ sono allineati se le differenze $P_i-P_0$ generano uno spazio di dimensione al massimo $1$; sono complanari se lo spazio generato ha dimensione al massimo $2$.

Per tre punti nello spazio l’allineamento si verifica con rango $\le1$ della matrice dei due spostamenti. Per quattro punti la complanarità si verifica annullando il determinante dei tre spostamenti. Si usano differenze tra punti perché la posizione dell’origine non deve modificare la proprietà.

_(Accascina–Monti, § 20.4, libro pp. 310–311; PDF pp. 326–327.)_

## Ripasso attivo

- **Equazioni vettoriali di rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Equazione vettoriale di una retta]].
- **Semirette e segmenti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Segmenti e semirette vettoriali]].
- **Equazioni vettoriali di piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Equazione vettoriale di un piano]].
- **Allineamento e complanarità:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Criteri vettoriali di allineamento e complanarità]].

## Collegamenti

Precedente: [[19 - GEO - Sottospazi affini]] · Successiva: [[21 - GEO - Riferimenti affini]]

[[MOC - Geometria]]
