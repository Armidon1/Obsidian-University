---
title: "Equazioni parametriche"
aliases:
  - "GEO — Equazioni parametriche"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "22"
pdf_pages: "341–360"
---

# Equazioni parametriche

> [!abstract] Scopo e percorso
> Geometria affine nel piano e nello spazio. Questa nota segue il capitolo 22 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 22.1 - Equazioni parametriche di rette nel piano

Vedi [[GEO - Retta parametrica nel piano]].

La forma vettoriale di una retta nel piano si traduce componente per componente:

$$r:\begin{cases}x=x_0+lt\\y=y_0+mt\end{cases},\qquad(l,m)\ne(0,0).$$

La coppia $(l,m)$ contiene i parametri direttori. Per $P_0=(1,2)$ e $v=(2,-1)$ si ottiene $(x,y)=(1+2t,2-t)$. L’appartenenza di un punto richiede un **unico valore dello stesso parametro** che soddisfi entrambe le coordinate.

_(Accascina–Monti, § 22.1, libro pp. 325–328; PDF pp. 341–344.)_

![[GEO-p342-1.png|650]]

**Lettura della figura (PDF p. 342, libro p. 326).** Il disegno interpreta i parametri direttori della retta come componenti dello spostamento dal punto iniziale a un altro punto della retta.

## 22.2 - Posizione reciproca di rette nel piano

Vedi [[GEO - Posizione di rette parametriche nel piano]].

Due rette si confrontano prima attraverso i direttori. Se sono proporzionali, le rette sono parallele, eventualmente coincidenti: per distinguere i casi si verifica un punto. Se non sono proporzionali, nel piano si intersecano in un unico punto.

Per trovare l’intersezione si uguagliano $P_0+tv=Q_0+sw$ usando parametri diversi $t,s$. Imporre lo stesso parametro alle due rette aggiungerebbe un vincolo ingiustificato.

_(Accascina–Monti, § 22.2, libro pp. 328–331; PDF pp. 344–347.)_

## 22.3 - Equazioni parametriche di rette nello spazio

Vedi [[GEO - Retta parametrica nello spazio]].

Nello spazio si aggiunge la terza componente:

$$r:P=P_0+tv,\qquad v=(l,m,n)\ne0.$$

Due rette non parallele possono essere incidenti oppure sghembe. Risolvendo $P_0+tv=Q_0+sw$, una soluzione dà l’intersezione; nessuna soluzione con direttori indipendenti dà rette sghembe.

Per esempio l’asse $x$, $r=(t,0,0)$, e $s=(0,u,1)$ sono sghembe: le quote sono rispettivamente $0$ e $1$, quindi non possono incontrarsi, e i direttori non sono proporzionali.

_(Accascina–Monti, § 22.3, libro pp. 331–333; PDF pp. 347–349.)_

![[GEO-p347-1.png|650]]

**Lettura della figura (PDF p. 347, libro p. 331).** La costruzione nello spazio lega la terna delle differenze di coordinate alla direzione della retta; i parametri non devono essere tutti nulli.

## 22.4 - Equazioni parametriche di piani

Vedi [[GEO - Piano parametrico]].

Un piano si scrive

$$\begin{cases}x=x_0+l_1s+l_2t\\y=y_0+m_1s+m_2t\\z=z_0+n_1s+n_2t\end{cases},\qquad\operatorname{rk}[u\ v]=2.$$

Per $P_0=(1,0,2)$, $u=(1,1,0)$ e $v=(0,1,1)$ si ottiene $(1+s,s+t,2+t)$. L’appartenenza di $Q=(2,3,4)$ corrisponde a $s=1$, $t=2$ e tutte e tre le componenti risultano verificate.

_(Accascina–Monti, § 22.4, libro pp. 333–334; PDF pp. 349–350.)_

## 22.5 - Semirette, semipiani e segmenti

Vedi [[GEO - Vincoli sui parametri geometrici]].

Le restrizioni sui parametri descrivono parti dell’oggetto affine: $0\le t\le1$ un segmento chiuso, $t>0$ una semiretta senza origine. In un piano $P=P_0+su+tv$, la condizione $s>0$ seleziona un semipiano delimitato dalla retta $P_0+\mathbb Rv$; $s\ge0$ include anche il bordo.

Il significato dipende dalla parametrizzazione: prima si identifica quale parametro misura il movimento trasversale alla retta di bordo, poi se ne impone il segno.

_(Accascina–Monti, § 22.5, libro pp. 334–336; PDF pp. 350–352.)_

## Ripasso attivo

- **Equazioni parametriche di rette nel piano:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Retta parametrica nel piano]].
- **Posizione reciproca di rette nel piano:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Posizione di rette parametriche nel piano]].
- **Equazioni parametriche di rette nello spazio:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Retta parametrica nello spazio]].
- **Equazioni parametriche di piani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Piano parametrico]].
- **Semirette, semipiani e segmenti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Vincoli sui parametri geometrici]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 341 (PDF p. 357). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[21 - GEO - Riferimenti affini]] · Successiva: [[23 - GEO - Equazioni cartesiane nel piano]]

[[MOC - Geometria]]
