---
title: "Prodotto scalare di vettori geometrici"
aliases:
  - "GEO — Prodotto scalare di vettori geometrici"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "33"
pdf_pages: "577–588"
---

# Prodotto scalare di vettori geometrici

> [!abstract] Scopo e percorso
> Geometria metrica e prodotto scalare. Questa nota segue il capitolo 33 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 33.1 - Norma di un vettore geometrico

Vedi [[GEO - Norma di un vettore geometrico]].

La norma di un vettore geometrico è la sua lunghezza. Vale $\|v\|\ge0$, con uguaglianza solo per $v=0$, e $\|kv\|=|k|\|v\|$.

La norma dipende dalla struttura metrica: prima di introdurla, la geometria affine permetteva già di parlare di combinazioni, rette e piani, ma non di misure di lunghezza.

_(Accascina–Monti, § 33.1, libro pp. 561–562; PDF pp. 577–578.)_

## 33.2 - Prodotto scalare di vettori geometrici

Vedi [[GEO - Prodotto scalare geometrico]].

Per vettori non nulli il prodotto scalare è

$$\langle u,v\rangle=\|u\|\|v\|\cos\theta.$$

Se uno dei due è nullo, il prodotto è zero. È simmetrico, bilineare e positivo definito: $\langle v,v\rangle=\|v\|^2$. Il prodotto è nullo per vettori non nulli esattamente quando sono ortogonali.

> [!note] Notazione del libro
> Il libro usa $u\times v$ per il **prodotto scalare**. Qui si usa $\langle u,v\rangle$, per distinguerlo dal prodotto vettoriale, che in altri testi usa il simbolo $\times$.

_(Accascina–Monti, § 33.2, libro pp. 562–563; PDF pp. 578–579.)_

## 33.3 - Basi ortogonali e ortonormali nel piano

Vedi [[GEO - Base ortonormale nel piano]].

Una base è ortogonale se i suoi vettori sono a due a due ortogonali; è ortonormale se hanno anche norma $1$. Nel piano, in una base ortonormale, se $u=(u_1,u_2)$ e $v=(v_1,v_2)$:

$$\langle u,v\rangle=u_1v_1+u_2v_2,\qquad\|u\|=\sqrt{u_1^2+u_2^2}.$$

La formula segue sviluppando il prodotto per bilinearità e usando $\langle e_i,e_j\rangle=\delta_{ij}$.

_(Accascina–Monti, § 33.3, libro pp. 563–564; PDF pp. 579–580.)_

![[GEO-p579-1.png|650]]

**Lettura della figura (PDF p. 579, libro p. 563).** La proiezione di una freccia lungo la direzione dell’altra collega il prodotto scalare alla lunghezza proiettata e al coseno dell’angolo.

## 33.4 - Basi ortogonali e ortonormali nello spazio

Vedi [[GEO - Base ortonormale nello spazio]].

In una base ortonormale dello spazio si aggiunge la terza componente:

$$\langle u,v\rangle=u_1v_1+u_2v_2+u_3v_3.$$

In una base ortogonale non normalizzata occorrono i fattori $\|e_i\|^2$. In una base obliqua compaiono anche termini incrociati: non si può usare automaticamente la somma dei prodotti delle coordinate.

_(Accascina–Monti, § 33.4, libro pp. 564–565; PDF pp. 580–581.)_

## 33.5 - Calcolo di angoli

Vedi [[GEO - Angolo tra vettori]].

Per due vettori non nulli:

$$\cos\theta=\frac{\langle u,v\rangle}{\|u\|\|v\|},\qquad0\le\theta\le\pi.$$

Per $u=(1,0)$ e $v=(1,1)$ in base ortonormale, $\cos\theta=1/\sqrt2$ e $\theta=\pi/4$. Un prodotto positivo indica un angolo acuto, negativo ottuso, nullo retto. L’angolo con il vettore nullo non è definito.

_(Accascina–Monti, § 33.5, libro pp. 565–566; PDF pp. 581–582.)_

## Ripasso attivo

- **Norma di un vettore geometrico:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Norma di un vettore geometrico]].
- **Prodotto scalare di vettori geometrici:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Prodotto scalare geometrico]].
- **Basi ortogonali e ortonormali nel piano:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Base ortonormale nel piano]].
- **Basi ortogonali e ortonormali nello spazio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Base ortonormale nello spazio]].
- **Calcolo di angoli:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Angolo tra vettori]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 569 (PDF p. 585). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[32 - GEO - Diagonalizzazione]] · Successiva: [[34 - GEO - Riferimenti cartesiani]]

[[MOC - Geometria]]
