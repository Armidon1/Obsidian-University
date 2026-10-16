---
title: "Immagine"
aliases:
  - "GEO — Immagine"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "27"
pdf_pages: "473–482"
---

# Immagine

> [!abstract] Scopo e percorso
> Funzioni e applicazioni lineari. Questa nota segue il capitolo 27 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 27.1 - Immagine di un omomorfismo

Vedi [[GEO - Immagine di un’applicazione lineare]].

L’immagine $\operatorname{Im}f=f(V)$ di un’applicazione lineare è un sottospazio del **codominio**. Se $V=\langle v_1,\ldots,v_n\rangle$, allora

$$\operatorname{Im}f=\langle f(v_1),\ldots,f(v_n)\rangle.$$

Infatti la linearità permette di portare i coefficienti fuori da $f$. Le immagini di una base sono generatori dell’immagine, ma possono essere dipendenti o nulle.

_(Accascina–Monti, § 27.1, libro pp. 457–459; PDF pp. 473–475.)_

## 27.2 - Calcolo dell’immagine

Vedi [[GEO - Base dell’immagine e suriettività]].

Se $A$ rappresenta $f$, l’immagine è rappresentata dallo spazio delle colonne di $A$ e

$$\dim\operatorname{Im}f=\operatorname{rk}A.$$

Per estrarne una base, si esegue Gauss e si selezionano le colonne originali nelle posizioni dei pivot. Se le basi non sono canoniche, quelle colonne sono coordinate e vanno interpretate nella base del codominio.

Per $f(x,y,z)=(x+y,y+z)$, la matrice $A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$ ha rango $2$. La sua immagine è tutto $\mathbb R^2$ e una base è $((1,0),(1,1))$.

La suriettività equivale a $\operatorname{rk}A=\dim W$. Se $\dim V<\dim W$, non è possibile raggiungere tutto $W$ con un’applicazione lineare.

_(Accascina–Monti, § 27.2, libro pp. 459–462; PDF pp. 475–478.)_

## Ripasso attivo

- **Immagine di un omomorfismo:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Immagine di un’applicazione lineare]].
- **Calcolo dell’immagine:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Base dell’immagine e suriettività]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 464 (PDF p. 480). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[26 - GEO - Omomorfismi]] · Successiva: [[28 - GEO - Nucleo]]

[[MOC - Geometria]]
