---
title: "Geometria in Rn"
aliases:
  - "GEO — Geometria in Rn"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "40"
pdf_pages: "695–728"
---

# Geometria in Rn

> [!abstract] Scopo e percorso
> Geometria in dimensione n. Questa nota segue il capitolo 40 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 40.1 - Sottospazi affini

Vedi [[GEO - Affini in Rn]].

Le definizioni affini si estendono a $\mathbb R^n$. Un affine di dimensione $r$ si scrive $\Pi=P_0+E$, dove $E$ ha base $v_1,\ldots,v_r$:

$$x=P_0+t_1v_1+\cdots+t_rv_r.$$

Dimensione zero significa punto, uno retta, due piano anche se l’ambiente ha dimensione maggiore. La parametrizzazione non è unica, mentre la direzione e la dimensione lo sono.

_(Accascina–Monti, § 40.1, libro pp. 679–681; PDF pp. 695–697.)_

## 40.2 - Parallelismo di sottospazi affini

Vedi [[GEO - Parallelismo affine in Rn]].

Per affini della stessa dimensione, $P_0+E$ e $Q_0+F$ sono paralleli se $E=F$. Coincidono se inoltre $Q_0-P_0\in E$, altrimenti sono disgiunti.

Il libro estende il parallelismo a dimensioni diverse richiedendo $E\subseteq F$ oppure $F\subseteq E$. Se $E\subseteq F$, l’affine minore è contenuto in quello maggiore oppure è disgiunto da esso.

Con dimensioni diverse la transitività generale non vale: due rette parallele a uno stesso piano possono avere direzioni differenti.

_(Accascina–Monti, § 40.2, libro pp. 681–685; PDF pp. 697–701.)_

## 40.3 - Inviluppi affini

Vedi [[GEO - Inviluppo affine]].

L’inviluppo affine di $P_0,\ldots,P_s$ è il più piccolo affine che li contiene:

$$\operatorname{Aff}(P_0,\ldots,P_s)=P_0+\langle P_1-P_0,\ldots,P_s-P_0\rangle.$$

La dimensione è il rango della matrice delle differenze ed è al massimo $s$. Equivalentemente i punti dell’inviluppo sono combinazioni $\sum_i\alpha_iP_i$ con $\sum_i\alpha_i=1$; i coefficienti possono essere negativi.

Per i quattro punti canonici di $\mathbb R^4$, l’inviluppo è $x_1+x_2+x_3+x_4=1$, di dimensione $3$. Le tre differenze rispetto al primo punto sono indipendenti.

_(Accascina–Monti, § 40.3, libro pp. 685–688; PDF pp. 701–704.)_

## 40.4 - Iperpiani

Vedi [[GEO - Iperpiani]].

Un iperpiano di $\mathbb R^n$ è un affine di dimensione $n-1$ e ha equazione

$$a_1x_1+\cdots+a_nx_n+b=0,\qquad a\ne0.$$

Due iperpiani sono paralleli se i vettori dei coefficienti sono proporzionali; coincidono se lo sono anche i termini noti con lo stesso fattore. Due iperpiani non paralleli si intersecano in un affine di dimensione $n-2$.

Un piano in $\mathbb R^4$ ha dimensione $2$ e quindi non è un iperpiano: servono due vincoli lineari indipendenti per descriverlo.

_(Accascina–Monti, § 40.4, libro pp. 688–689; PDF pp. 704–705.)_

## 40.5 - Ortogonalità

Vedi [[GEO - Normale a un iperpiano]].

Nel prodotto scalare standard $a=(a_1,\ldots,a_n)$ è ortogonale alla direzione dell’iperpiano $a\cdot x+b=0$. Tutti i vettori normali sono multipli di $a$.

La retta per $P$ ortogonale all’iperpiano è $P+ta$. Il piede della perpendicolare si trova imponendo l’equazione dell’iperpiano:

$$H=P-\frac{a\cdot P+b}{\|a\|^2}a.$$

È lo stesso procedimento già usato nel piano e nello spazio; il numero di coordinate cambia, la struttura del calcolo resta identica.

_(Accascina–Monti, § 40.5, libro pp. 689–690; PDF pp. 705–706.)_

## 40.6 - Insiemi convessi e semispazi

Vedi [[GEO - Insiemi convessi e semispazi]].

Un insieme $C$ è convesso se contiene il segmento tra ogni coppia di suoi punti:

$$P,Q\in C,\quad0\le t\le1\Rightarrow(1-t)P+tQ\in C.$$

Gli affini, i segmenti e i semispazi sono convessi. Un iperpiano delimita i semispazi aperti $a\cdot x+b>0$ e $a\cdot x+b<0$; con disuguaglianze non strette si include il bordo. L’intersezione di insiemi convessi è convessa, quindi anche una regione descritta da più disequazioni lineari lo è.

Per $x_1+x_2+x_3+x_4-1=0$, il semispazio contenente l’origine è quello con somma minore di $1$. La convessità di un insieme riguarda segmenti tra punti, mentre la convessità di una funzione, trattata nella nota esistente, riguarda un confronto tra valori della funzione e loro interpolazioni.

_(Accascina–Monti, § 40.6, libro pp. 690–692; PDF pp. 706–708.)_

## Ripasso attivo

- **Sottospazi affini:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Affini in Rn]].
- **Parallelismo di sottospazi affini:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Parallelismo affine in Rn]].
- **Inviluppi affini:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Inviluppo affine]].
- **Iperpiani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Iperpiani]].
- **Ortogonalità:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Normale a un iperpiano]].
- **Insiemi convessi e semispazi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Insiemi convessi e semispazi]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 702 (PDF p. 718). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[39 - GEO - Diagonalizzazione di matrici simmetriche]] · Successiva: [[A - GEO - Approfondimenti]]

[[MOC - Geometria]]

Per distinguere la convessità di un insieme dalla proprietà di una funzione, vedi le note esistenti [[Convex Function]] e [[Concave Function]].
