---
title: "Diagonalizzazione"
aliases:
  - "GEO — Diagonalizzazione"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "32"
pdf_pages: "549–576"
---

# Diagonalizzazione

> [!abstract] Scopo e percorso
> Autovalori e diagonalizzazione. Questa nota segue il capitolo 32 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 32.1 - Diagonalizzazione

Vedi [[GEO - Criterio di diagonalizzabilità]].

Un endomorfismo è diagonalizzabile se esiste una base di autovettori. Per una matrice $A$ ciò significa trovare $P$ invertibile e $D$ diagonale con

$$D=P^{-1}AP,\qquad AP=PD.$$

Le colonne di $P$ sono gli autovettori e l’elemento $D_{jj}$ è l’autovalore della colonna $j$. L’ordine va mantenuto coerente.

Su $\mathbb R$, il criterio completo è: il polinomio caratteristico si deve scomporre in fattori lineari reali e, per ogni autovalore, deve valere $m_g=m_a$. Equivalentemente, la somma delle dimensioni degli autospazi deve essere $n$.

> [!example] Diagonalizzare e verificare
> Per $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ scegliamo $P=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ e $D=\operatorname{diag}(2,3)$. Si ha $AP=\begin{pmatrix}2&3\\0&3\end{pmatrix}=PD$. Le colonne indipendenti rendono $P$ invertibile.

Una matrice con $n$ autovalori distinti è diagonalizzabile. La condizione è sufficiente, ma non necessaria: $I_n$ è già diagonale pur avendo un solo autovalore. La matrice $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ non è diagonalizzabile, perché offre un solo autovettore indipendente.

Il vantaggio operativo è $A^k=PD^kP^{-1}$: elevare la matrice a potenza diventa elevare a potenza gli autovalori. Una base di autovettori può però essere obliqua: diagonalizzare non garantisce di conservare le formule euclidee più semplici.

_(Accascina–Monti, § 32.1, libro pp. 533–543; PDF pp. 549–559.)_

## Ripasso attivo

- **Diagonalizzazione:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Criterio di diagonalizzabilità]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 548 (PDF p. 564). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[31 - GEO - Autovalori e autovettori]] · Successiva: [[33 - GEO - Prodotto scalare di vettori geometrici]]

[[MOC - Geometria]]
