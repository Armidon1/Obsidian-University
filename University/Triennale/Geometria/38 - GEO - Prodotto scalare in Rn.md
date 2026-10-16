---
title: "Prodotto scalare in Rn"
aliases:
  - "GEO — Prodotto scalare in Rn"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "38"
pdf_pages: "655–678"
---

# Prodotto scalare in Rn

> [!abstract] Scopo e percorso
> Geometria metrica e prodotto scalare. Questa nota segue il capitolo 38 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 38.1 - Prodotto scalare

Vedi [[GEO - Prodotto scalare standard in Rn]].

In $\mathbb R^n$ il prodotto scalare standard è $\langle x,y\rangle=x^Ty=\sum_i x_iy_i$. È simmetrico, bilineare e positivo definito. La norma associata è $\|x\|=\sqrt{\langle x,x\rangle}$ e la distanza è $\|x-y\|$.

La disuguaglianza di Cauchy-Schwarz e quella triangolare sono

$$|\langle x,y\rangle|\le\|x\|\|y\|,\qquad\|x+y\|\le\|x\|+\|y\|.$$

La prima garantisce che $\cos\theta=\langle x,y\rangle/(\|x\|\|y\|)$ sia compreso tra $-1$ e $1$ per vettori non nulli. Si definisce $x\perp y$ quando $\langle x,y\rangle=0$: anche il vettore nullo è ortogonale a ogni vettore, pur non formando un angolo definito.

_(Accascina–Monti, § 38.1, libro pp. 639–643; PDF pp. 655–659.)_

## 38.2 - Basi ortonormali

Vedi [[GEO - Ortonormalizzazione di Gram-Schmidt]].

Se $(q_1,\ldots,q_r)$ è una base ortonormale di un sottospazio $E$, per $v\in E$:

$$v=\sum_{i=1}^r\langle v,q_i\rangle q_i.$$

Il procedimento di Gram-Schmidt trasforma una base $(v_1,\ldots,v_r)$ in una ortogonale:

$$u_1=v_1,\qquad u_k=v_k-\sum_{j<k}\frac{\langle v_k,u_j\rangle}{\langle u_j,u_j\rangle}u_j,$$

poi si normalizza $q_k=u_k/\|u_k\|$. Si sottraggono le componenti già presenti, preservando lo span. L’indipendenza iniziale assicura $u_k\ne0$.

Per $v_1=(1,1)$ e $v_2=(1,0)$, $u_2=(1,0)-\frac12(1,1)=(1/2,-1/2)$. La base ortonormale risultante è $((1,1)/\sqrt2,(1,-1)/\sqrt2)$.

_(Accascina–Monti, § 38.2, libro pp. 643–649; PDF pp. 659–665.)_

## 38.3 - Matrici ortogonali

Vedi [[GEO - Matrici ortogonali]].

Una matrice quadrata $Q$ è ortogonale se $Q^TQ=I$, equivalentemente $Q^{-1}=Q^T$. Le sue colonne, e anche le sue righe, costituiscono basi ortonormali.

Conserva prodotti scalari e norme:

$$\langle Qx,Qy\rangle=x^TQ^TQy=\langle x,y\rangle.$$

Quindi conserva distanze e angoli. Inoltre $\det Q=\pm1$. Essere ortogonale non significa essere simmetrica: le matrici di rotazione del piano sono ortogonali e generalmente non simmetriche.

_(Accascina–Monti, § 38.3, libro pp. 649–651; PDF pp. 665–667.)_

## Ripasso attivo

- **Prodotto scalare:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Prodotto scalare standard in Rn]].
- **Basi ortonormali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Ortonormalizzazione di Gram-Schmidt]].
- **Matrici ortogonali:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Matrici ortogonali]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 656 (PDF p. 672). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[37 - GEO - Endomorfismi di V3(O) - Due esempi]] · Successiva: [[39 - GEO - Diagonalizzazione di matrici simmetriche]]

[[MOC - Geometria]]

La nota esistente [[Squared Euclidean Norm]] riprende la norma al quadrato nelle applicazioni al machine learning; [[Linear Regression]] ne usa il significato di errore quadratico.
