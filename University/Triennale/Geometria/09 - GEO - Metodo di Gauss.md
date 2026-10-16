---
title: "Metodo di Gauss"
aliases:
  - "GEO — Metodo di Gauss"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "9"
pdf_pages: "157–174"
---

# Metodo di Gauss

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 9 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 9.1 - Alcuni esempi

Vedi [[GEO - Eliminazione delle incognite]].

L’eliminazione trasforma un sistema in uno equivalente più semplice. Consideriamo

$$\left[\begin{array}{ccc|c}1&1&1&3\\2&3&1&6\\1&2&3&6\end{array}\right].$$

Con $R_2\leftarrow R_2-2R_1$ e $R_3\leftarrow R_3-R_1$ le ultime due righe diventano $(0,1,-1\mid0)$ e $(0,1,2\mid3)$. Poi $R_3\leftarrow R_3-R_2$ dà $(0,0,3\mid3)$. Dal basso: $z=1$, $y-z=0$ dà $y=1$, $x+y+z=3$ dà $x=1$.

Ogni passaggio agisce sull’intera riga della **matrice completa**, incluso il termine noto. Il controllo nelle equazioni iniziali conferma $(1,1,1)$.

_(Accascina–Monti, § 9.1, libro pp. 141–145; PDF pp. 157–161.)_

## 9.2 - Metodo di Gauss

Vedi [[GEO - Metodo di Gauss e pivot]].

Una matrice è a scalini se le righe nulle sono in fondo e il primo elemento non nullo di ogni riga, il **pivot**, si trova più a destra rispetto a quello della riga precedente.

Il metodo di Gauss sceglie un pivot non nullo, scambia righe se necessario, elimina i coefficienti sottostanti e ripete sulla parte rimanente. Poi usa la sostituzione all’indietro, assegnando parametri alle colonne prive di pivot.

| Riga finale | Significato |
|---|---|
| $(0,\ldots,0\mid c)$ con $c\ne0$ | Incompatibilità |
| $(0,\ldots,0\mid0)$ | Identità eliminabile |
| Riga con pivot nei coefficienti | Vincolo indipendente |

> [!warning] Sistemi con parametri
> Prima di dividere per un’espressione contenente un parametro, separa il caso in cui essa è nulla. Per esempio dividere per $k-1$ esclude $k=1$, che va analizzato a parte.

_(Accascina–Monti, § 9.2, libro pp. 145–154; PDF pp. 161–170.)_

## Ripasso attivo

- **Alcuni esempi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Eliminazione delle incognite]].
- **Metodo di Gauss:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Metodo di Gauss e pivot]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 156 (PDF p. 172). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[08 - GEO - Sistemi di equazioni lineari]] · Successiva: [[10 - GEO - Applicazioni del metodo di Gauss]]

[[MOC - Geometria]]
