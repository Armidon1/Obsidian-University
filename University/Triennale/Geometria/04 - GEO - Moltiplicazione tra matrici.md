---
title: "Moltiplicazione tra matrici"
aliases:
  - "GEO — Moltiplicazione tra matrici"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "4"
pdf_pages: "67–84"
---

# Moltiplicazione tra matrici

> [!abstract] Scopo e percorso
> Algebra delle matrici e sistemi. Questa nota segue il capitolo 4 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 4.1 - Matrice prodotto

Vedi [[GEO - Prodotto tra matrici]].

Il prodotto $AB$ è definito se il numero di colonne di $A$ coincide con quello di righe di $B$:

$$A\in M(p,q,\mathbb R),\ B\in M(q,r,\mathbb R)\Rightarrow AB\in M(p,r,\mathbb R),\qquad(AB)_{ij}=\sum_{k=1}^{q}a_{ik}b_{kj}.$$

Si combina la riga $i$ di $A$ con la colonna $j$ di $B$. Per esempio

$$\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}3&0\\1&4\end{pmatrix}=\begin{pmatrix}5&8\\1&4\end{pmatrix}.$$

Il prodotto non è elemento per elemento: questa distinzione è essenziale per rappresentare sistemi e composizioni di applicazioni.

_(Accascina–Monti, § 4.1, libro pp. 51–53; PDF pp. 67–69.)_

## 4.2 - Matrici e sistemi

Vedi [[GEO - Forma matriciale dei sistemi]].

Il sistema con matrice dei coefficienti $A$, colonna delle incognite $x$ e termini noti $b$ diventa $Ax=b$. Infatti la riga $i$ del prodotto è precisamente $\sum_j a_{ij}x_j$.

Scrivendo $A=[c_1\ \cdots\ c_q]$ per colonne si ottiene

$$Ax=x_1c_1+\cdots+x_qc_q.$$

Quindi risolvere $Ax=b$ equivale a chiedere se $b$ è combinazione lineare delle colonne di $A$, e con quali coefficienti. Questa lettura anticipa il concetto di immagine di un’applicazione lineare.

_(Accascina–Monti, § 4.2, libro pp. 53–55; PDF pp. 69–71.)_

## 4.3 - Proprietà della moltiplicazione

Vedi [[GEO - Proprietà del prodotto matriciale]].

Il prodotto è associativo e distributivo rispetto alla somma, quando le dimensioni lo consentono. In generale **non è commutativo**. Con le due matrici dell’esempio precedente il prodotto inverso è $BA=\begin{pmatrix}3&6\\1&6\end{pmatrix}$, diverso da $AB$.

Inoltre

$$(AB)^T=B^TA^T.$$

L’ordine si inverte perché righe e colonne si scambiano. Non vale la legge del prodotto nullo: con $A=\operatorname{diag}(1,0)$ e $B=\operatorname{diag}(0,1)$, entrambe non nulle, si ha $AB=0$.

Di conseguenza $AB=AC$ non permette di cancellare $A$ senza ulteriori ipotesi. L’invertibilità, studiata più avanti, fornirà una condizione sufficiente.

_(Accascina–Monti, § 4.3, libro pp. 55–61; PDF pp. 71–77.)_

## Ripasso attivo

- **Matrice prodotto:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Prodotto tra matrici]].
- **Matrici e sistemi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Forma matriciale dei sistemi]].
- **Proprietà della moltiplicazione:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Proprietà del prodotto matriciale]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 66 (PDF p. 82). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[03 - GEO - Lo spazio vettoriale delle matrici]] · Successiva: [[05 - GEO - Determinanti]]

[[MOC - Geometria]]
