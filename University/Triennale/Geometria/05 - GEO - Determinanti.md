---
title: "Determinanti"
aliases:
  - "GEO — Determinanti"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "5"
pdf_pages: "85–102"
---

# Determinanti

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 5 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 5.1 - Definizione

Vedi [[GEO - Determinante e sviluppo di Laplace]].

Il determinante associa uno scalare a una **matrice quadrata**. Per ordini piccoli:

$$\det(a)=a,\qquad\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc.$$

Se $A_{ij}$ è la matrice ottenuta eliminando riga $i$ e colonna $j$, il suo cofattore è $C_{ij}=(-1)^{i+j}\det A_{ij}$. Lo sviluppo di Laplace lungo una riga fissata è

$$\det A=\sum_{j=1}^n a_{ij}C_{ij};$$

analogamente si sviluppa lungo una colonna. Conviene scegliere quella con più zeri.

> [!example] Sviluppo economico
> Per $A=\begin{pmatrix}1&2&0\\0&3&4\\0&0&5\end{pmatrix}$, sviluppando lungo la prima colonna si ottiene $\det A=1\cdot(3\cdot5)=15$.

_(Accascina–Monti, § 5.1, libro pp. 70–73; PDF pp. 86–89.)_

## 5.2 - Proprietà

Vedi [[GEO - Proprietà del determinante]].

Le principali proprietà permettono di evitare sviluppi lunghi:

| Operazione o struttura | Effetto sul determinante |
|---|---|
| Trasposizione | $\det A^T=\det A$ |
| Scambio di due righe | Cambia segno |
| Moltiplicazione di una riga per $k$ | Moltiplica per $k$ |
| Somma a una riga di un multiplo di un’altra | Invariato |
| Matrice triangolare | Prodotto degli elementi diagonali |
| Riga nulla o due righe proporzionali | Determinante nullo |

Il teorema di Binet afferma $\det(AB)=\det A\det B$. Per una matrice di ordine $n$, $\det(kA)=k^n\det A$.

> [!warning] Errore frequente
> Il determinante non è additivo rispetto all’intera matrice: $\det(I_2+I_2)=4$, mentre $\det I_2+\det I_2=2$. La linearità riguarda una singola riga o colonna, mantenendo fisse le altre.

Un determinante nullo segnalerà dipendenza tra righe e colonne e impossibilità di invertire la matrice.

_(Accascina–Monti, § 5.2, libro pp. 73–80; PDF pp. 89–96.)_

## Ripasso attivo

- **Definizione:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Determinante e sviluppo di Laplace]].
- **Proprietà:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Proprietà del determinante]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 84 (PDF p. 100). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[04 - GEO - Moltiplicazione tra matrici]] · Successiva: [[06 - GEO - Matrice inversa]]

[[MOC - Geometria]]
