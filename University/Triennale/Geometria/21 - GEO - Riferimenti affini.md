---
title: "Riferimenti affini"
aliases:
  - "GEO — Riferimenti affini"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "21"
pdf_pages: "331–340"
---

# Riferimenti affini

> [!abstract] Scopo e percorso
> Geometria affine nel piano e nello spazio. Questa nota segue il capitolo 21 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 21.1 - Sistemi di riferimento affine nel piano

Vedi [[GEO - Riferimento affine nel piano]].

Un riferimento affine nel piano è formato da un’origine $O$ e una base $(e_1,e_2)$ di $V^2(O)$. Le coordinate di $P$ sono i coefficienti in $\overrightarrow{OP}=xe_1+ye_2$.

Gli assi possono essere obliqui e i vettori di base possono avere lunghezze diverse. Le coordinate permettono di trattare algebraicamente allineamento e parallelismo, senza introdurre ancora formule standard per angoli e distanze.

_(Accascina–Monti, § 21.1, libro pp. 315–317; PDF pp. 331–333.)_

![[GEO-p331-1.png|650]]

**Lettura della figura (PDF p. 331, libro p. 315).** La base obliqua e il parallelogramma mostrano come le coordinate affini siano coefficienti di una combinazione, anche senza assi ortogonali.

![[GEO-p332-1.png|650]]

**Lettura della figura (PDF p. 332, libro p. 316).** Le costruzioni per parallele leggono le due coordinate rispetto agli assi obliqui: proiettare parallelamente all’altro asse non equivale a proiettare ortogonalmente.

## 21.2 - Sistemi di riferimento affine nello spazio

Vedi [[GEO - Riferimento affine nello spazio]].

Nello spazio si sceglie una base $(e_1,e_2,e_3)$ e si scrive $\overrightarrow{OP}=xe_1+ye_2+ze_3$. La terna è unica per le proprietà della base.

Se $P=(x,y,z)$ e $Q=(x',y',z')$, le componenti di $\overrightarrow{PQ}$ sono $(x'-x,y'-y,z'-z)$. Cambiare origine modifica le coordinate dei punti; gli spostamenti si ottengono sempre sottraendo quelle dei loro estremi nello stesso riferimento.

_(Accascina–Monti, § 21.2, libro pp. 317–318; PDF pp. 333–334.)_

![[GEO-p333-1.png|650]]

**Lettura della figura (PDF p. 333, libro p. 317).** Gli assi e le direzioni nello spazio illustrano la decomposizione lungo una base tridimensionale e le coordinate dei vettori posizione.

## 21.3 - Punto medio

Vedi [[GEO - Coordinate del punto medio]].

La formula affine del punto medio è la media delle coordinate:

$$M=\frac{P+Q}{2}.$$

Per $P=(1,-2,4)$ e $Q=(3,6,0)$ si ottiene $M=(2,2,2)$. Questa formula vale anche con assi obliqui, perché deriva dalle operazioni vettoriali e non da misure di lunghezza.

_(Accascina–Monti, § 21.3, libro pp. 318–320; PDF pp. 334–336.)_

![[GEO-p334-1.png|650]]

**Lettura della figura (PDF p. 334, libro p. 318).** Le tre direzioni indipendenti permettono di ricostruire il punto nello spazio; la successiva media delle coordinate individua il punto medio.

## 21.4 - Allineamento e complanarità

Vedi [[GEO - Rango e configurazioni di punti]].

Disponendo per colonne le differenze $P_i-P_0$, il rango misura la dimensione dell’inviluppo affine. Rango $0$ significa tutti i punti coincidenti; rango $1$ allineamento; rango $2$ complanarità senza allineamento.

Per $P_0=(0,0,1)$, $P_1=(1,0,1)$, $P_2=(0,1,1)$, $P_3=(1,1,1)$, le differenze sono $(1,0,0)$, $(0,1,0)$, $(1,1,0)$: il rango è $2$, quindi i punti sono complanari nel piano $z=1$.

_(Accascina–Monti, § 21.4, libro pp. 320–321; PDF pp. 336–337.)_

## Figure del riepilogo e degli esercizi

Queste pagine conservano le figure riprese nel sunto o nelle soluzioni degli esercizi, nell’ordine del libro. Le ripetizioni del materiale originale sono mantenute per collegare definizioni e applicazioni.

![[GEO-p338-1.png|650]]

**Lettura della figura (PDF p. 338, libro p. 322).** Il riepilogo ripete la costruzione del riferimento affine: lo stesso punto è individuato dai coefficienti delle due direzioni di base.

## Ripasso attivo

- **Sistemi di riferimento affine nel piano:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Riferimento affine nel piano]].
- **Sistemi di riferimento affine nello spazio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Riferimento affine nello spazio]].
- **Punto medio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Coordinate del punto medio]].
- **Allineamento e complanarità:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Rango e configurazioni di punti]].

## Collegamenti

Precedente: [[20 - GEO - Equazioni vettoriali di rette e piani]] · Successiva: [[22 - GEO - Equazioni parametriche]]

[[MOC - Geometria]]
