---
title: "Geometria analitica metrica del piano"
aliases:
  - "GEO — Geometria analitica metrica del piano"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "35"
pdf_pages: "593–620"
---

# Geometria analitica metrica del piano

> [!abstract] Scopo e percorso
> Geometria metrica e prodotto scalare. Questa nota segue il capitolo 35 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 35.1 - Ortogonalità fra rette

Vedi [[GEO - Ortogonalità di rette nel piano]].

In un riferimento cartesiano, per $r:ax+by+c=0$ un normale è $n=(a,b)$ e un direttore è $v=(-b,a)$. Due rette sono ortogonali se i direttori hanno prodotto scalare nullo; equivalentemente, se $a_1a_2+b_1b_2=0$.

Questa forma include le rette verticali. La regola sui coefficienti angolari $m_1m_2=-1$ si usa solo quando entrambi sono definiti.

_(Accascina–Monti, § 35.1, libro pp. 577–581; PDF pp. 593–597.)_

## 35.2 - Angoli tra rette

Vedi [[GEO - Angolo tra rette nel piano]].

L’angolo acuto o retto fra due rette è

$$\cos\alpha=\frac{|v\cdot w|}{\|v\|\|w\|},\qquad0\le\alpha\le\frac\pi2.$$

Il valore assoluto elimina la dipendenza dal verso dei direttori. L’altro angolo formato dalle rette è il supplementare. Per le rette di direttori $(1,0)$ e $(1,1)$ l’angolo minore è $\pi/4$.

_(Accascina–Monti, § 35.2, libro pp. 581–584; PDF pp. 597–600.)_

![[GEO-p598-1.png|650]]

**Lettura della figura (PDF p. 598, libro p. 582).** Le rette e gli angoli adiacenti distinguono l’angolo tra direttori dall’angolo minore tra rette. Il valore assoluto nel coseno rende il risultato indipendente dai versi.

## 35.3 - Distanza tra un punto e una retta

Vedi [[GEO - Distanza punto-retta nel piano]].

La distanza da $P=(x_0,y_0)$ a $r:ax+by+c=0$ è la lunghezza della proiezione dello spostamento sulla direzione normale:

$$d(P,r)=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}.$$

Il piede della perpendicolare è

$$H=P-\frac{ax_0+by_0+c}{a^2+b^2}(a,b).$$

Per $P=(0,0)$ e $r:3x+4y-10=0$, la distanza è $2$ e il piede è $(6/5,8/5)$. Sostituendo, $3(6/5)+4(8/5)=10$.

_(Accascina–Monti, § 35.3, libro pp. 584–586; PDF pp. 600–602.)_

## 35.4 - Distanza tra due rette

Vedi [[GEO - Distanza tra rette parallele nel piano]].

Due rette incidenti hanno distanza zero. Per due rette parallele, dopo aver uniformato i coefficienti di $x,y$:

$$r:ax+by+c_1=0,\quad s:ax+by+c_2=0\Rightarrow d(r,s)=\frac{|c_2-c_1|}{\sqrt{a^2+b^2}}.$$

Se le equazioni hanno coefficienti proporzionali, si riscalano prima. Per $x+y=1$ e $2x+2y=6$, la seconda diventa $x+y=3$ e la distanza è $2/\sqrt2=\sqrt2$.

_(Accascina–Monti, § 35.4, libro pp. 586–586; PDF pp. 602–602.)_

## 35.5 - Bisettrici

Vedi [[GEO - Bisettrici cartesiane]].

Le due bisettrici delle rette incidenti $r_i:a_ix+b_iy+c_i=0$ sono il luogo dei punti equidistanti dalle rette:

$$\frac{a_1x+b_1y+c_1}{\sqrt{a_1^2+b_1^2}}=\pm\frac{a_2x+b_2y+c_2}{\sqrt{a_2^2+b_2^2}}.$$

I due segni producono due rette ortogonali. Per gli assi $x=0$ e $y=0$ si ottiene $x=\pm y$. La normalizzazione evita che una moltiplicazione dell’equazione alteri artificialmente la distanza.

_(Accascina–Monti, § 35.5, libro pp. 586–587; PDF pp. 602–603.)_

## 35.6 - Circonferenze

Vedi [[GEO - Circonferenze cartesiane]].

La circonferenza di centro $C=(a,b)$ e raggio $R>0$ è

$$(x-a)^2+(y-b)^2=R^2.$$

Dalla forma $x^2+y^2+\alpha x+\beta y+\gamma=0$ si ricavano centro $(-\alpha/2,-\beta/2)$ e $R^2=(\alpha^2+\beta^2)/4-\gamma$. Se $R^2=0$ il luogo è un punto, se $R^2<0$ è vuoto.

Per intersecare una retta e una circonferenza si sostituisce una parametrizzazione della retta: l’equazione quadratica risultante ha due, una o nessuna soluzione reale. Equivalentemente si confrontano distanza del centro dalla retta e raggio: minore significa secante, uguale tangente, maggiore esterna.

Per $C=(1,-2)$ e $R=3$, l’equazione è $x^2+y^2-2x+4y-4=0$. La retta $y=1$ è tangente nel punto $(1,1)$.

_(Accascina–Monti, § 35.6, libro pp. 587–596; PDF pp. 603–612.)_

![[GEO-p607-1.png|650]]

**Lettura della figura (PDF p. 607, libro p. 591).** La configurazione di rette accompagna l’esercizio sulla circonferenza: le condizioni metriche si traducono in distanze del centro dalle rette e in vincoli sul raggio.

![[GEO-p608-1.png|650]]

**Lettura della figura (PDF p. 608, libro p. 592).** La figura prosegue la costruzione dell’esempio sulle circonferenze. Il disegno orienta la scelta delle condizioni, che vengono poi verificate nelle equazioni riportate.

## Ripasso attivo

- **Ortogonalità fra rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Ortogonalità di rette nel piano]].
- **Angoli tra rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Angolo tra rette nel piano]].
- **Distanza tra un punto e una retta:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Distanza punto-retta nel piano]].
- **Distanza tra due rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Distanza tra rette parallele nel piano]].
- **Bisettrici:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Bisettrici cartesiane]].
- **Circonferenze:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Circonferenze cartesiane]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 599 (PDF p. 615). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[34 - GEO - Riferimenti cartesiani]] · Successiva: [[36 - GEO - Geometria analitica metrica dello spazio]]

[[MOC - Geometria]]
