---
title: "Spazi vettoriali sui reali"
aliases:
  - "GEO — Spazi vettoriali sui reali"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "13"
pdf_pages: "209–216"
---

# Spazi vettoriali sui reali

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 13 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 13.1 - Gli spazi vettoriali

Vedi [[GEO - Assiomi di spazio vettoriale]].

Uno spazio vettoriale reale è un insieme non vuoto $V$ dotato di somma interna e moltiplicazione per scalari reali. La somma è associativa e commutativa, ha uno zero e ogni elemento ha un opposto. Inoltre, per $h,k\in\mathbb R$ e $u,v\in V$:

$$1v=v,\quad h(kv)=(hk)v,\quad(h+k)v=hv+kv,\quad k(u+v)=ku+kv.$$

I vettori sono gli elementi di $V$: non devono necessariamente essere frecce. La definizione isola le proprietà comuni che rendono possibile usare gli stessi metodi in ambienti diversi.

_(Accascina–Monti, § 13.1, libro pp. 193–195; PDF pp. 209–211.)_

## 13.2 - Esempi di spazi vettoriali

Vedi [[GEO - Spazi di matrici e polinomi]].

Sono spazi vettoriali $\mathbb R^n$, $M(p,q,\mathbb R)$, i vettori geometrici e i polinomi $\mathbb R[x]$, con le operazioni usuali. Si possono sommare due polinomi o moltiplicarli per un numero senza uscire dall’insieme.

> [!note] Convenzione sui polinomi
> Il libro indica con $\mathbb R_n[x]$ i polinomi di grado **minore di $n$**, incluso il polinomio nullo: la base canonica è $1,x,\ldots,x^{n-1}$. Altri testi usano una notazione simile per grado minore o uguale a $n$.

I polinomi di grado esattamente $2$ non formano uno spazio: la somma di $x^2$ e $-x^2$ è il polinomio nullo, che non ha grado $2$.

_(Accascina–Monti, § 13.2, libro pp. 195–195; PDF pp. 211–211.)_

## 13.3 - Proprietà degli spazi vettoriali

Vedi [[GEO - Proprietà degli spazi vettoriali]].

Dagli assiomi seguono $0v=0$, $k0=0$, $(-1)v=-v$ e la cancellazione $u+v=u+w\Rightarrow v=w$.

Se $kv=0$, allora $k=0$ oppure $v=0$. Infatti, se $k\ne0$, moltiplicando per $1/k$ si ottiene $v=0$. Questa conclusione riguarda il prodotto **scalare per vettore**; non si estende al prodotto tra matrici, dove possono esistere fattori non nulli con prodotto nullo.

Per provare che un insieme con operazioni nuove è uno spazio, vanno controllati anche chiusura e assiomi: la sola somiglianza della notazione non basta.

_(Accascina–Monti, § 13.3, libro pp. 195–197; PDF pp. 211–213.)_

## Ripasso attivo

- **Gli spazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Assiomi di spazio vettoriale]].
- **Esempi di spazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Spazi di matrici e polinomi]].
- **Proprietà degli spazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Proprietà degli spazi vettoriali]].

## Collegamenti

Precedente: [[12 - GEO - Combinazioni lineari di vettori geometrici]] · Successiva: [[14 - GEO - Sottospazi vettoriali]]

[[MOC - Geometria]]
