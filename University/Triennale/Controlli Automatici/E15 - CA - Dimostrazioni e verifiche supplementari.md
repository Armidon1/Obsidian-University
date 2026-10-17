---
title: "Dimostrazioni e verifiche supplementari"
aliases:
  - "CA — Dimostrazioni e verifiche supplementari"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "88-94"
---

# Dimostrazioni e verifiche supplementari

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[20 - CA - Raggiungibilità osservabilità e forme canoniche]] · [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]] · [[22 - CA - Osservatore asintotico e rilevabilità]] · [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]].

## Invarianza delle proprietà strutturali

Per $z=Tx$, $\mathcal R_z=T\mathcal R$, quindi il rango di raggiungibilità non cambia. Analogamente $\mathcal O_z=\mathcal O T^{-1}$. Sono moltiplicazioni per matrici invertibili: cambiano le coordinate dei sottospazi, non la loro dimensione.

Una retroazione dello stato non cambia il sottospazio raggiungibile: le potenze di $A+BK$ applicate a $B$ generano lo stesso spazio di quelle di $A$. Questo spiega perché i modi non raggiungibili rimangono fissi e perché il feedback non può crearne il controllo dal nulla.

## Principio di separazione attraverso le coordinate

Le pagine manoscritte ricostruiscono il passaggio dallo stato composto $(x,\hat x)$ a $(x,e)$, con $e=x-\hat x$. La trasformazione è invertibile e rende la matrice complessiva triangolare a blocchi. Il determinante si fattorizza quindi come
$$\det(sI-A_{\rm compl})=\det(sI-A-BK)\det(sI-A+LC).$$
Gli stessi passaggi dimostrano che il compensatore dinamico non ha, isolatamente, questa unione di poli: la fattorizzazione appartiene al complesso processo-controllore.

## Cosa controllare nei conti matriciali

Annotare la convenzione del cambio di base, verificare $TT^{-1}=I$, calcolare $A_z,B_z,C_z$, controllare il polinomio del feedback e quello dell'osservatore. Le ultime due pagine contengono un ulteriore esercizio numerico e il confronto dei coefficienti: sono un controllo della procedura, non nuovi argomenti rispetto alle lezioni.

_(Eserciziario, pagine PDF 88–94; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 88
> ![[CA-E-p088-1.jpg]]
> Scomposizione di Kalman e trasformazione delle matrici. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 89
> ![[CA-E-p089-1.jpg]]
> Verifica del feedback e dei modi fissi nelle nuove coordinate. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 90
> ![[CA-E-p090-1.jpg]]
> Dimostrazione della struttura a blocchi per il controllo con osservatore. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 91
> ![[CA-E-p091-1.jpg]]
> Proseguimento: dinamica dell’errore e fattorizzazione del polinomio. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 92
> ![[CA-E-p092-1.jpg]]
> Schema del controllore dinamico e matrici della realizzazione. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 93
> ![[CA-E-p093-1.jpg]]
> Esercizio matriciale supplementare e raggiungibilità. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 94
> ![[CA-E-p094-1.jpg]]
> Confronto dei coefficienti e soluzione del guadagno. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
