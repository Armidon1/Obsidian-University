---
title: "Funzioni tra insiemi"
aliases:
  - "GEO — Funzioni tra insiemi"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "25"
pdf_pages: "431–444"
---

# Funzioni tra insiemi

> [!abstract] Scopo e percorso
> Funzioni e applicazioni lineari. Questa nota segue il capitolo 25 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 25.1 - Funzioni. Immagini e controimmagini

Vedi [[GEO - Immagine e controimmagine di una funzione]].

Una funzione $f:A\to B$ assegna a ogni elemento del dominio $A$ esattamente un elemento del codominio $B$. L’immagine effettiva è $f(A)=\{f(a):a\in A\}$, che può essere più piccola di $B$.

La controimmagine di $b$ è l’insieme $f^{-1}(b)=\{a\in A:f(a)=b\}$. Può essere vuoto, contenere un punto oppure più punti. Per $f(x)=x^2$ su $\mathbb R$, l’immagine è $[0,+\infty)$ e $f^{-1}(4)=\{-2,2\}$.

_(Accascina–Monti, § 25.1, libro pp. 415–417; PDF pp. 431–433.)_

## 25.2 - Funzioni iniettive, suriettive, biiettive

Vedi [[GEO - Iniettività suriettività e biiettività]].

Una funzione è iniettiva se $f(a)=f(a')\Rightarrow a=a'$, suriettiva se $f(A)=B$, biiettiva se entrambe le proprietà valgono.

| Proprietà | Controimmagine di ogni elemento del codominio |
|---|---|
| Iniettiva | Al massimo un elemento |
| Suriettiva | Almeno un elemento |
| Biiettiva | Esattamente un elemento |

La suriettività dipende dal codominio dichiarato. La funzione $x\mapsto x^2$ è suriettiva come applicazione $\mathbb R\to[0,+\infty)$, ma non come applicazione $\mathbb R\to\mathbb R$.

_(Accascina–Monti, § 25.2, libro pp. 417–419; PDF pp. 433–435.)_

## 25.3 - Funzione inversa

Vedi [[GEO - Funzione inversa]].

Una funzione biiettiva ammette inversa $f^{-1}:B\to A$: riporta ogni immagine al suo unico elemento di partenza. Per $f(x)=2x+1$ su $\mathbb R$, $f^{-1}(y)=(y-1)/2$.

> [!important] Due significati dello stesso simbolo
> La controimmagine $f^{-1}(b)$ come **insieme** è definita anche se $f$ non è invertibile. La funzione inversa esiste invece solo se $f$ è biiettiva.

_(Accascina–Monti, § 25.3, libro pp. 419–420; PDF pp. 435–436.)_

## 25.4 - Composizione di funzioni

Vedi [[GEO - Composizione di funzioni]].

Se $f:A\to B$ e $g:B\to C$, la composizione è $(g\circ f)(a)=g(f(a))$. Si applica prima la funzione più a destra. La composizione è associativa, ma in generale non commutativa.

Con $f(x)=x+1$ e $g(x)=2x$ si ottiene $g(f(x))=2x+2$, mentre $f(g(x))=2x+1$. Per una funzione invertibile $f^{-1}\circ f=\operatorname{id}_A$ e $f\circ f^{-1}=\operatorname{id}_B$.

_(Accascina–Monti, § 25.4, libro pp. 420–422; PDF pp. 436–438.)_

## Ripasso attivo

- **Funzioni. Immagini e controimmagini:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Immagine e controimmagine di una funzione]].
- **Funzioni iniettive, suriettive, biiettive:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Iniettività suriettività e biiettività]].
- **Funzione inversa:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Funzione inversa]].
- **Composizione di funzioni:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Composizione di funzioni]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 426 (PDF p. 442). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[24 - GEO - Equazioni cartesiane nello spazio]] · Successiva: [[26 - GEO - Omomorfismi]]

[[MOC - Geometria]]
