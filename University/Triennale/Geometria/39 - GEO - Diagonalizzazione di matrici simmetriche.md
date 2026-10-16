---
title: "Diagonalizzazione di matrici simmetriche"
aliases:
  - "GEO — Diagonalizzazione di matrici simmetriche"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "39"
pdf_pages: "679–694"
---

# Diagonalizzazione di matrici simmetriche

> [!abstract] Scopo e percorso
> Geometria metrica e prodotto scalare. Questa nota segue il capitolo 39 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 39.1 - Matrici ed endomorfismi simmetrici

Vedi [[GEO - Teorema spettrale reale]].

Il teorema spettrale reale afferma che una matrice reale $A$ è simmetrica se e solo se è diagonalizzabile mediante una matrice ortogonale:

$$A=A^T\iff\exists Q\text{ ortogonale},\quad Q^TAQ=D\text{ diagonale reale}.$$

Gli autovalori sono reali e autospazi relativi ad autovalori distinti sono ortogonali. Infatti, se $Av=\lambda v$, $Aw=\mu w$ e $A=A^T$:

$$\lambda\langle v,w\rangle=\langle Av,w\rangle=\langle v,Aw\rangle=\mu\langle v,w\rangle.$$

Se $\lambda\ne\mu$, il prodotto è zero. Per un endomorfismo la simmetria della matrice si riferisce a basi ortonormali: una base obliqua può nasconderla.

_(Accascina–Monti, § 39.1, libro pp. 663–667; PDF pp. 679–683.)_

## 39.2 - Procedimento di diagonalizzazione

Vedi [[GEO - Diagonalizzazione ortogonale]].

Si calcolano autovalori e basi degli autospazi. All’interno di ciascun autospazio si applica Gram-Schmidt e si normalizza; infine si uniscono le basi ottenute, già ortogonali fra autospazi distinti. Questi vettori diventano le colonne di $Q$, con gli autovalori corrispondenti in $D$.

Per $A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, gli autovalori sono $3$ e $1$, con autovettori $(1,1)$ e $(1,-1)$. Quindi

$$Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad D=\operatorname{diag}(3,1).$$

Il controllo $AQ=QD$ e $Q^TQ=I$ verifica sia la diagonalizzazione sia l’ortonormalità. Con un autovalore ripetuto, autovettori dello **stesso** autospazio non sono automaticamente ortogonali: serve ortonormalizzarli.

_(Accascina–Monti, § 39.2, libro pp. 667–670; PDF pp. 683–686.)_

## Ripasso attivo

- **Matrici ed endomorfismi simmetrici:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Teorema spettrale reale]].
- **Procedimento di diagonalizzazione:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Diagonalizzazione ortogonale]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 674 (PDF p. 690). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[38 - GEO - Prodotto scalare in Rn]] · Successiva: [[40 - GEO - Geometria in Rn]]

[[MOC - Geometria]]
