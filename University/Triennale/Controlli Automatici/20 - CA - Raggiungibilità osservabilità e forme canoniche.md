---
title: "Raggiungibilità osservabilità e forme canoniche"
aliases:
  - "CA — Raggiungibilità osservabilità e forme canoniche"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "149-155"
class_label: "21/04"
---

# Raggiungibilità osservabilità e forme canoniche

> [!abstract]
> Questa lezione sviluppa raggiungibilità osservabilità e forme canoniche seguendo il blocco delle pagine 149–155 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 21/04. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[19 - CA - Esercizi riepilogativi su controllo classico]]. **Dopo:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]].

## Riprendere il modello nello spazio di stato

Vedi [[CA - Matrice di raggiungibilità]] · [[CA - Matrice di osservabilità]].

La seconda parte torna al modello $\dot x=Ax+Bu$, $y=Cx$, perché il progetto deve modificare o stimare i modi interni e non solo la risposta ingresso-uscita. Per un sistema SISO di ordine $n$:
$$\mathcal R=[B\ AB\ \cdots\ A^{n-1}B],\qquad
\mathcal O=\begin{bmatrix}C\\CA\\\vdots\\CA^{n-1}\end{bmatrix}.$$
Il sistema è completamente raggiungibile se $\operatorname{rank}\mathcal R=n$, completamente osservabile se $\operatorname{rank}\mathcal O=n$. La raggiungibilità misura gli stati influenzabili dall'ingresso; l'osservabilità gli stati distinguibili dalle uscite.

> [!example] Due modi con ruoli diversi
> Con $A=\operatorname{diag}(-1,2)$, $B=(1,0)^T$ e $C=(1,0)$, la FdT è $1/(s+1)$ ma il modo $e^{2t}$ è sia non raggiungibile sia non osservabile. Il processo esterno è BIBO stabile, il modello interno è instabile e quel modo non è stabilizzabile dall'ingresso assegnato.

Per i prerequisiti algebrici vedi [[GEO - Rango e minori]] e [[GEO - Matrice inversa]]; per le definizioni dinamiche [[TDS - Raggiungibilità]] e [[TDS - Osservabilità]].

_(Dispensa commentata, pagine PDF 149–150; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 149
> ![[CA-p149-1.jpg]]
> La seconda parte riprende il modello di stato e le matrici di raggiungibilità e osservabilità, necessarie per intervenire sui modi interni.

> [!example]- Materiale originale — pagina PDF 150
> ![[CA-p150-1.jpg]]
> Il richiamo alle forme canoniche distingue le trasformazioni di coordinate e i blocchi strutturali del sistema.

## Cambiamento di coordinate e forma compagna

Vedi [[CA - Cambio di coordinate]] · [[CA - Forma canonica raggiungibile]] · [[CA - Forma canonica osservabile]].

Fissiamo la convenzione $z=Tx$ con $T$ invertibile. Allora
$$A_z=TAT^{-1},\qquad B_z=TB,\qquad C_z=CT^{-1}.$$
Non si cambia il sistema fisico, ma la sua rappresentazione. Autovalori, FdT e ranghi di raggiungibilità/osservabilità rimangono invariati. Nella dispensa possono comparire entrambe le convenzioni $z=Tx$ e $x=Tz$: prima di confrontare formule occorre controllare quale sia usata.

Per un sistema SISO raggiungibile si può ottenere la forma compagna
$$A_c=\begin{pmatrix}0&1&\cdots&0\\\vdots&&\ddots&\vdots\\0&0&\cdots&1\\-a_0&-a_1&\cdots&-a_{n-1}\end{pmatrix},\quad B_c=e_n.$$
I coefficienti dell'ultima riga sono quelli di $\det(sI-A)$. La forma osservabile è duale: si costruisce applicando le stesse idee alla coppia $(A^T,C^T)$. Queste forme rendono immediato il confronto dei coefficienti nel progetto di poli e osservatori.

_(Dispensa commentata, pagine PDF 151–152; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 151
> ![[CA-p151-1.jpg]]
> La forma compagna raccoglie i coefficienti del polinomio caratteristico nell'ultima riga e rende semplice il confronto per il feedback.

> [!example]- Materiale originale — pagina PDF 152
> ![[CA-p152-1.jpg]]
> La dualità porta alla forma osservabile; le equazioni trasformate ricordano di controllare la convenzione del cambio di base.

## Esercizi e sottospazi non completi

Vedi [[CA - Scomposizione raggiungibile]] · [[CA - Scomposizione osservabile]].

Se il rango non è pieno, si sceglie una base della parte raggiungibile e la si completa a una base di tutto lo spazio. Con la convenzione $x=Tz$ si ottiene
$$A_z=\begin{pmatrix}A_r&A_{12}\\0&A_{nr}\end{pmatrix},\qquad B_z=\binom{B_r}{0}.$$
La parte non raggiungibile evolve autonomamente: qualunque comando non può spostarne gli autovalori. La scomposizione osservabile separa analogamente i modi che non influenzano le misure.

Negli esercizi conviene evitare una trasformazione simbolica completa se il solo scopo è decidere la stabilizzabilità: si può usare il test PBH sui modi critici. Quando invece si richiede il controllore esplicito, la base e la trasformazione vanno scritte e verificate moltiplicando le matrici.

_(Dispensa commentata, pagine PDF 153–155; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 153
> ![[CA-p153-1.jpg]]
> Gli esempi calcolano rango e basi dei sottospazi, distinguendo i modi raggiungibili da quelli autonomi.

> [!example]- Materiale originale — pagina PDF 154
> ![[CA-p154-1.jpg]]
> Il foglio risolve una trasformazione canonica e verifica le matrici nelle nuove coordinate attraverso moltiplicazioni esplicite.

> [!example]- Materiale originale — pagina PDF 155
> ![[CA-p155-1.jpg]]
> Gli esercizi completano il confronto fra forme canoniche, struttura di Kalman e trasferimenti visibili.

## Esercizi collegati

[[E15 - CA - Dimostrazioni e verifiche supplementari]]
