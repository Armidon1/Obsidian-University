---
title: "Rango di una matrice"
aliases:
  - "GEO — Rango di una matrice"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "7"
pdf_pages: "123–136"
---

# Rango di una matrice

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 7 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 7.1 - Definizione di rango

Vedi [[GEO - Rango e minori]].

Nel linguaggio del libro un **minore di ordine $r$** è una matrice quadrata estratta scegliendo $r$ righe e $r$ colonne. Altri testi chiamano “minore” direttamente il suo determinante: qui distinguiamo i due oggetti.

Il rango $\operatorname{rk}A$ è il massimo ordine di un minore con determinante non nullo. Per la matrice nulla si pone rango zero. Se $A$ ha tipo $(p,q)$:

$$0\le\operatorname{rk}A\le\min(p,q),\qquad\operatorname{rk}A^T=\operatorname{rk}A.$$

Per una matrice quadrata di ordine $n$, rango $n$, determinante non nullo e invertibilità sono condizioni equivalenti.

_(Accascina–Monti, § 7.1, libro pp. 107–109; PDF pp. 123–125.)_

## 7.2 - Calcolo del rango

Vedi [[GEO - Teorema dell’orlare]].

Per trovare il rango si cerca un minore invertibile e si controlla se può essere ampliato. Un **orlato** si ottiene aggiungendo una riga e una colonna.

> [!important] Teorema dell’orlare
> Se un minore $B$ di ordine $r$ ha determinante non nullo e tutti i suoi orlati di ordine $r+1$ hanno determinante nullo, allora $\operatorname{rk}A=r$.

Per $A=\begin{pmatrix}1&2&3\\2&4&6\end{pmatrix}$ esiste un coefficiente non nullo, ma ogni determinante $2\times2$ è zero perché la seconda riga è il doppio della prima: il rango è $1$.

Per matrici con parametri bisogna distinguere i valori che annullano i determinanti usati. Più avanti il metodo di Gauss permetterà di calcolare il rango contando i pivot.

_(Accascina–Monti, § 7.2, libro pp. 109–114; PDF pp. 125–130.)_

## Ripasso attivo

- **Definizione di rango:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Rango e minori]].
- **Calcolo del rango:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Teorema dell’orlare]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 116 (PDF p. 132). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[06 - GEO - Matrice inversa]] · Successiva: [[08 - GEO - Sistemi di equazioni lineari]]

[[MOC - Geometria]]
