---
title: "Endomorfismi di V 3 (O): due esempi"
aliases:
  - "GEO — Endomorfismi di V 3 (O): due esempi"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "37"
pdf_pages: "649–654"
---

# Endomorfismi di V 3 (O): due esempi

> [!abstract] Scopo e percorso
> Geometria metrica e prodotto scalare. Questa nota segue il capitolo 37 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## Proiezione ortogonale - Esempio 37.1

Vedi [[GEO - Proiezione ortogonale su un piano]].

Il primo esempio del capitolo proietta ortogonalmente sul piano $E:x+y+z=0$. Con normale $n=(1,1,1)$:

$$f(v)=v-\frac{v\cdot n}{n\cdot n}n,\qquad A=I-\frac13nn^T=\frac13\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}.$$

I vettori di $E$ restano fissi, quindi $E_1=E$. I multipli di $n$ sono annullati, quindi $E_0=\langle n\rangle$. Le dimensioni $2+1=3$ danno una base di autovettori.

Si può scegliere una base ortonormale:

$$q_1=\frac{(1,1,1)}{\sqrt3},\quad q_2=\frac{(1,-1,0)}{\sqrt2},\quad q_3=\frac{(-1,-1,2)}{\sqrt6}.$$

I prodotti scalari reciproci sono zero e le norme sono $1$. Con queste colonne in $Q$, $Q^TAQ=\operatorname{diag}(0,1,1)$ e $Q^{-1}=Q^T$: si semplificano insieme endomorfismo e prodotto scalare.

_(Accascina–Monti, esempio 37.1, libro pp. 633–637; PDF pp. 649–653.)_

## Proiezione obliqua - Esempio 37.5

Vedi [[GEO - Proiezione obliqua su un piano]].

L’esempio 37.5 del libro proietta sullo stesso piano lungo la direzione $d=(1,2,1)$, che non è ortogonale al piano. Poiché $n\cdot d=4$:

$$g(v)=v-\frac{n\cdot v}{4}d,\qquad B=I-\frac14dn^T=\begin{pmatrix}3/4&-1/4&-1/4\\-1/2&1/2&-1/2\\-1/4&-1/4&3/4\end{pmatrix}.$$

Restano $E_1=E$ ed $E_0=\langle d\rangle$. Quindi $g$ è diagonalizzabile; per esempio $d,(1,-1,0),(1,0,-1)$ formano una base di autovettori. Non esiste però una base **ortonormale** di autovettori, perché $d$ non è ortogonale a tutto $E$.

> [!warning] Correzione
> Nel libro, p. 638 (PDF p. 654), compare «Non esiste allora alcuna base … formata da autovettori di $g$». Va aggiunto **ortonormale**: le dimensioni degli autospazi sommano a $3$, dunque una base di autovettori esiste. Per esempio $d\cdot(1,-1,0)=-1$, quindi gli autospazi non sono ortogonali.
>
> Nella stessa pagina la matrice stampata ha elemento centrale $3/4$. La formula della proiezione dà invece $b_{22}=1-2/4=1/2$. Con il valore corretto $Bd=0$ e $Bv=v$ per ogni $v\in E$; con quello stampato tali verifiche falliscono.

Questo confronto motiva il teorema spettrale: la diagonalizzazione mediante una matrice ortogonale è una proprietà più forte della semplice diagonalizzabilità.

_(Accascina–Monti, esempio 37.5, libro pp. 637–638; PDF pp. 653–654.)_

## Ripasso attivo

- **Proiezione ortogonale:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Proiezione ortogonale su un piano]].
- **Proiezione obliqua:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Proiezione obliqua su un piano]].

## Collegamenti

Precedente: [[36 - GEO - Geometria analitica metrica dello spazio]] · Successiva: [[38 - GEO - Prodotto scalare in Rn]]

[[MOC - Geometria]]

Il caso ortogonale collega [[GEO - Teorema spettrale reale]] e [[GEO - Matrici ortogonali]].
