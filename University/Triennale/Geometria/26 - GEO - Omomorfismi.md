---
title: "Omomorfismi"
aliases:
  - "GEO — Omomorfismi"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "26"
pdf_pages: "445–472"
---

# Omomorfismi

> [!abstract] Scopo e percorso
> Funzioni e applicazioni lineari. Questa nota segue il capitolo 26 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 26.1 - Omomorfismi tra spazi vettoriali

Vedi [[GEO - Applicazione lineare]].

Un omomorfismo di spazi vettoriali, o applicazione lineare, $f:V\to W$ preserva somma e prodotto per scalare:

$$f(u+v)=f(u)+f(v),\qquad f(ku)=kf(u).$$

Equivalentemente preserva ogni combinazione lineare. Ne segue $f(0)=0$. Questa condizione è necessaria ma non sufficiente: $f(x)=x^2$ manda zero in zero, ma non è lineare.

La funzione $f(x,y)=(x+2y,3x-y)$ è lineare; $g(x,y)=(x+1,y)$ è affine ma non lineare, perché $g(0,0)\ne0$. Per verificare la linearità bisogna considerare vettori e scalari generici.

_(Accascina–Monti, § 26.1, libro pp. 429–432; PDF pp. 445–448.)_

## 26.2 - Matrice associata a un omomorfismo

Vedi [[GEO - Matrice di un’applicazione lineare]].

Fissate una base $\mathcal B=(e_1,\ldots,e_n)$ di $V$ e una base $\mathcal C$ di $W$ con $m$ elementi, la matrice rappresentativa ha come colonna $j$ le coordinate di $f(e_j)$ nella base $\mathcal C$:

$$A=[f]_{\mathcal C\leftarrow\mathcal B},\qquad[f(v)]_{\mathcal C}=A[v]_{\mathcal B},\qquad A\in M(m,n,\mathbb R).$$

Per l’applicazione dell’esempio, nelle basi canoniche, $f(1,0)=(1,3)$ e $f(0,1)=(2,-1)$, quindi $A=\begin{pmatrix}1&2\\3&-1\end{pmatrix}$. Per $(1,2)$ il prodotto dà $(5,1)$, come la formula diretta.

Le basi sono parte dell’informazione: la stessa applicazione può avere matrici diverse in basi diverse.

_(Accascina–Monti, § 26.2, libro pp. 432–439; PDF pp. 448–455.)_

## 26.3 - Omomorfismo associato a una matrice

Vedi [[GEO - Applicazione lineare assegnata su una base]].

Assegnare immagini arbitrarie ai vettori di una base determina un’unica applicazione lineare:

$$f\left(\sum_jx_je_j\right)=\sum_jx_jf(e_j).$$

Non serve che le immagini siano indipendenti o generino tutto il codominio. Viceversa ogni matrice $m\times n$, fissate le basi, definisce un’applicazione lineare $V\to W$.

Se si assegnano immagini a una famiglia dipendente, invece, bisogna rispettarne le relazioni. Se $v_3=v_1+v_2$, la linearità impone $f(v_3)=f(v_1)+f(v_2)$: non si possono scegliere le tre immagini indipendentemente.

_(Accascina–Monti, § 26.3, libro pp. 439–441; PDF pp. 455–457.)_

## Ripasso attivo

- **Omomorfismi tra spazi vettoriali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Applicazione lineare]].
- **Matrice associata a un omomorfismo:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Matrice di un’applicazione lineare]].
- **Omomorfismo associato a una matrice:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Applicazione lineare assegnata su una base]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 446 (PDF p. 462). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[25 - GEO - Funzioni tra insiemi]] · Successiva: [[27 - GEO - Immagine]]

[[MOC - Geometria]]

Le matrici delle applicazioni lineari sono alla base dei modelli descritti in [[Linear Regression]].
