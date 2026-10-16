---
title: "Endomorfismi"
aliases:
  - "GEO — Endomorfismi"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "30"
pdf_pages: "511–524"
---

# Endomorfismi

> [!abstract] Scopo e percorso
> Funzioni e applicazioni lineari. Questa nota segue il capitolo 30 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 30.1 - Endomorfismi

Vedi [[GEO - Endomorfismi e composizione]].

Un endomorfismo è un’applicazione lineare $f:V\to V$. Rispetto a una stessa base usata in partenza e in arrivo è rappresentato da una matrice quadrata. La matrice della composizione $g\circ f$ è $BA$ se $A$ rappresenta $f$ e $B$ rappresenta $g$.

Rappresentazioni diverse possono rendere lo stesso endomorfismo più o meno semplice. L’obiettivo dei capitoli successivi sarà trovare basi in cui la matrice sia diagonale, così che le coordinate evolvano separatamente.

_(Accascina–Monti, § 30.1, libro pp. 495–497; PDF pp. 511–513.)_

## 30.2 - Cambiamento di base

Vedi [[GEO - Cambiamento di base e similitudine]].

Siano $\mathcal B$ la vecchia base e $\mathcal B'$ la nuova. Costruiamo $P$ mettendo nelle colonne le coordinate dei vettori della nuova base rispetto alla vecchia. Allora

$$[v]_{\mathcal B}=P[v]_{\mathcal B'},\qquad[v]_{\mathcal B'}=P^{-1}[v]_{\mathcal B}.$$

Se $A$ rappresenta $f$ nella vecchia base, nella nuova:

$$A'=P^{-1}AP.$$

Questa relazione si chiama similitudine. Determinante, rango e polinomio caratteristico non cambiano.

> [!example] Controllare il verso del passaggio
> Prendiamo $A=\operatorname{diag}(1,2)$ e nuova base $((1,0),(1,1))$. Allora $P=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ e $P^{-1}AP=\begin{pmatrix}1&-1\\0&2\end{pmatrix}$. La seconda colonna è corretta perché $f(1,1)=(1,2)=-1(1,0)+2(1,1)$.

La formula si ricava seguendo il percorso: nuove coordinate $\to$ vecchie coordinate $\to$ applicazione di $A$ $\to$ ritorno alle nuove coordinate.

_(Accascina–Monti, § 30.2, libro pp. 497–502; PDF pp. 513–518.)_

## Ripasso attivo

- **Endomorfismi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Endomorfismi e composizione]].
- **Cambiamento di base:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Cambiamento di base e similitudine]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 505 (PDF p. 521). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[29 - GEO - Isomorfismi]] · Successiva: [[31 - GEO - Autovalori e autovettori]]

[[MOC - Geometria]]
