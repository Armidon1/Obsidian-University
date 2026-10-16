---
title: "Lo spazio vettoriale delle matrici"
aliases:
  - "GEO — Lo spazio vettoriale delle matrici"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "3"
pdf_pages: "53–66"
---

# Lo spazio vettoriale delle matrici

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 3 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 3.1 - Matrice somma

Vedi [[GEO - Somma di matrici]].

L’addizione è definita tra matrici **dello stesso tipo** e agisce sulle singole posizioni:

$$(A+B)_{ij}=a_{ij}+b_{ij}.$$

Per $A=\begin{pmatrix}1&2\\0&-1\end{pmatrix}$ e $B=\begin{pmatrix}3&0\\2&1\end{pmatrix}$ si ottiene $A+B=\begin{pmatrix}4&2\\2&0\end{pmatrix}$. Non è possibile sommare direttamente una matrice $2\times2$ a una $2\times3$.

La somma è associativa e commutativa, ha come neutro la matrice nulla e ogni matrice ha un opposto $-A$. Vale la cancellazione additiva e la differenza si definisce $A-B=A+(-B)$. Inoltre $(A+B)^T=A^T+B^T$.

Le proprietà discendono da quelle dei numeri reali, applicate a ciascuna posizione.

_(Accascina–Monti, § 3.1, libro pp. 37–41; PDF pp. 53–57.)_

## 3.2 - Moltiplicazione per uno scalare

Vedi [[GEO - Prodotto di una matrice per uno scalare]].

Il prodotto per uno scalare $k\in\mathbb R$ è $(kA)_{ij}=ka_{ij}$. Per esempio $2A=\begin{pmatrix}2&4\\0&-2\end{pmatrix}$.

Le identità fondamentali sono

$$1A=A,\quad h(kA)=(hk)A,\quad(h+k)A=hA+kA,\quad k(A+B)=kA+kB.$$

Con la somma e questo prodotto, $M(p,q,\mathbb R)$ costituisce uno spazio vettoriale: le matrici possono essere trattate come vettori con $pq$ componenti. La moltiplicazione tra matrici, introdotta nel capitolo successivo, è un’operazione diversa e non serve per definire la struttura di spazio vettoriale.

> [!tip] Controllo rapido
> $kA=0$ implica $k=0$ oppure $A=0$: se $k\ne0$, basta moltiplicare per $1/k$.

_(Accascina–Monti, § 3.2, libro pp. 41–41; PDF pp. 57–57.)_

## Ripasso attivo

- **Matrice somma:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Somma di matrici]].
- **Moltiplicazione per uno scalare:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Prodotto di una matrice per uno scalare]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 45 (PDF p. 61). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[02 - GEO - Matrici e insiemi]] · Successiva: [[04 - GEO - Moltiplicazione tra matrici]]

[[MOC - Geometria]]
