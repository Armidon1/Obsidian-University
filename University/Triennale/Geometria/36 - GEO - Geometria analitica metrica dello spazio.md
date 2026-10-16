---
title: "Geometria analitica metrica dello spazio"
aliases:
  - "GEO — Geometria analitica metrica dello spazio"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "36"
pdf_pages: "621–648"
---

# Geometria analitica metrica dello spazio

> [!abstract] Scopo e percorso
> Geometria metrica e prodotto scalare. Questa nota segue il capitolo 36 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 36.1 - Ortogonalità di rette

Vedi [[GEO - Ortogonalità di rette nello spazio]].

Due rette nello spazio sono ortogonali quando i loro direttori hanno prodotto scalare nullo. Seguendo il libro, questo vale anche se sono sghembe: si confrontano le direzioni dopo averle trasportate nello stesso punto.

Per $r=(t,0,0)$ e $s=(0,u,1)$ i direttori sono ortogonali, ma le rette non si incontrano. Se si richiede anche l’incidenza, bisogna controllarla separatamente.

_(Accascina–Monti, § 36.1, libro pp. 605–607; PDF pp. 621–623.)_

## 36.2 - Angoli tra rette

Vedi [[GEO - Angolo tra rette nello spazio]].

L’angolo minore tra rette di direttori $u,v$ soddisfa $\cos\alpha=|u\cdot v|/(\|u\|\|v\|)$. Le posizioni delle rette non intervengono: contano soltanto le direzioni.

_(Accascina–Monti, § 36.2, libro pp. 607–608; PDF pp. 623–624.)_

## 36.3 - Ortogonalità tra rette e piani

Vedi [[GEO - Ortogonalità retta-piano]].

Per un piano $\pi:n\cdot x+d=0$, il vettore $n\ne0$ è normale al piano. Una retta di direttore $v$ è ortogonale al piano se $v$ è proporzionale a $n$; è parallela al piano se $v\cdot n=0$, includendo la possibilità che sia contenuta.

Come conseguenza, l’angolo minore $\beta$ tra retta e piano è complementare a quello tra direttore e normale: $\sin\beta=|v\cdot n|/(\|v\|\|n\|)$.

_(Accascina–Monti, § 36.3, libro pp. 608–611; PDF pp. 624–627.)_

## 36.4 - Ortogonalità tra piani

Vedi [[GEO - Ortogonalità tra piani]].

Due piani sono ortogonali se i loro normali hanno prodotto scalare nullo; sono paralleli se i normali sono proporzionali. L’angolo minore tra piani si calcola come quello tra i normali.

Una retta contenuta in un piano ortogonale a un altro piano non è necessariamente ortogonale al secondo: bisogna controllare la sua specifica direzione.

_(Accascina–Monti, § 36.4, libro pp. 611–612; PDF pp. 627–628.)_

## 36.5 - Parallelismo e ortogonalità

Vedi [[GEO - Costruzioni ortogonali nello spazio]].

Le relazioni nello spazio richiedono attenzione alle dimensioni: due rette ortogonali a uno stesso piano sono parallele, ma due rette ortogonali a una stessa retta possono avere direzioni differenti.

Per trovare una retta per $P$ ortogonale a un piano si scrive $P+tn$. Per trovare il piano per $P$ ortogonale a una retta di direttore $v$ si scrive $v\cdot(x-P)=0$.

_(Accascina–Monti, § 36.5, libro pp. 612–614; PDF pp. 628–630.)_

## 36.6 - Distanze

Vedi [[GEO - Distanze nello spazio]].

La distanza punto-piano è

$$d(P,\pi)=\frac{|n\cdot P+d|}{\|n\|},\qquad H=P-\frac{n\cdot P+d}{\|n\|^2}n.$$

Per punto-retta $r=Q+\mathbb Rv$, si minimizza $\|P-Q-tv\|^2$: il piede corrisponde a $t=((P-Q)\cdot v)/\|v\|^2$. Il residuo è ortogonale a $v$.

Per due rette non parallele $r=P_0+tu$, $s=Q_0+sv$, si trova la perpendicolare comune imponendo

$$(Q_0+sv-P_0-tu)\cdot u=0,\qquad(Q_0+sv-P_0-tu)\cdot v=0.$$

È un sistema lineare in $t,s$; la norma del vettore congiungente i piedi è la distanza. Per rette parallele basta la distanza di un punto dell’una dall’altra. Due piani non paralleli e una retta incidente a un piano hanno distanza zero; per oggetti paralleli si riduce a una distanza punto-piano o punto-retta.

Per $P=(1,2,3)$ e piano $x+y+z=0$, $H=P-2(1,1,1)=(-1,0,1)$ e $d=2\sqrt3$.

_(Accascina–Monti, § 36.6, libro pp. 614–617; PDF pp. 630–633.)_

## 36.7 - Sfere e circonferenze

Vedi [[GEO - Sfere e sezioni circolari]].

La sfera di centro $C$ e raggio $R>0$ ha equazione $\|x-C\|^2=R^2$. Completando i quadrati si riconoscono centro e raggio nella forma sviluppata.

L’intersezione con un piano a distanza $\delta$ dal centro è vuota se $\delta>R$, un punto se $\delta=R$, una circonferenza di raggio $\sqrt{R^2-\delta^2}$ se $\delta<R$. Il centro della circonferenza è il piede della perpendicolare dal centro della sfera al piano.

Per $x^2+y^2+z^2=25$ e $z=3$, l’intersezione è $x^2+y^2=16$, $z=3$: centro $(0,0,3)$ e raggio $4$. Sottraendo due equazioni di sfere con lo stesso coefficiente dei termini quadratici si ottiene il piano radicale; nei casi non degeneri l’intersezione è una circonferenza.

_(Accascina–Monti, § 36.7, libro pp. 617–620; PDF pp. 633–636.)_

## Ripasso attivo

- **Ortogonalità di rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Ortogonalità di rette nello spazio]].
- **Angoli tra rette:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Angolo tra rette nello spazio]].
- **Ortogonalità tra rette e piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Ortogonalità retta-piano]].
- **Ortogonalità tra piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Ortogonalità tra piani]].
- **Parallelismo e ortogonalità:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Costruzioni ortogonali nello spazio]].
- **Distanze:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Distanze nello spazio]].
- **Sfere e circonferenze:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Sfere e sezioni circolari]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 625 (PDF p. 641). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[35 - GEO - Geometria analitica metrica del piano]] · Successiva: [[37 - GEO - Endomorfismi di V3(O) - Due esempi]]

[[MOC - Geometria]]
