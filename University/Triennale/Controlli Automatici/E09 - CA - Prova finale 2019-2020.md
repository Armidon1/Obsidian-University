---
title: "Prova finale 2019-2020"
aliases:
  - "CA — Prova finale 2019-2020"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "52-56"
---

# Prova finale 2019-2020

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]] · [[22 - CA - Osservatore asintotico e rilevabilità]] · [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]] · [[26 - CA - Metodo diretto di Lyapunov]] · [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Problema 1 - Tutti i poli coincidenti

Controllare prima i modi non raggiungibili: se ne esiste uno stabile, il valore comune richiesto deve coincidere con esso, altrimenti la specifica non è realizzabile. Il progetto dell'osservatore segue lo stesso ragionamento per i modi non osservabili. La convergenza asintotica permette poli multipli strettamente a sinistra, anche se il transitorio può contenere fattori polinomiali.

## Problema 2 - Non linearità trigonometrica

Per $\dot x_1=-\sin x_1+x_2$, $\dot x_2=-2x_1-2x_2^3$, l'origine è l'unico equilibrio. Infatti $x_2=\sin x_1$ e $x_1=-x_2^3$ implicano $|x_1|\le1$, dove $\sin x_1$ ha lo stesso segno di $x_1$, costringendo entrambi a zero.

La Jacobiana ha polinomio $\lambda^2+\lambda+2$, quindi AS locale. Scegliendo $V=x_1^2+x_2^2/2$:
$$\dot V=-2x_1\sin x_1-2x_2^4.$$
È definita negativa nella striscia $|x_1|<\pi$. Ogni sottolivello $V\le c$ con $0<c<\pi^2$ è compatto e contenuto nella striscia, quindi dà una stima certificata del bacino. Questo argomento non dimostra da solo GAS, perché il segno del seno cambia fuori dalla striscia.

## Problema 3 - Equilibrio fuori dall’origine

Per $\dot x=\sin^2(x-1)+u$, stabilizzare $x_e=1$. Qui $u_e=0$, la Jacobiana rispetto a $x$ nel punto è nulla e $B=1$. Con $z=x-1$, $u=-kz$, $k>0$, l'origine è localmente AS. Una cancellazione $u=-\sin^2(x-1)-k(x-1)$ dà invece $\dot z=-kz$ globalmente sul modello ideale.

_(Eserciziario, pagine PDF 52–56; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 52
> ![[CA-E-p052-1.jpg]]
> Traccia completa della prova finale 2019-2020. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 53
> ![[CA-E-p053-1.jpg]]
> Problema 1: scomposizione e feedback. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 54
> ![[CA-E-p054-1.jpg]]
> Problema 1: osservatore e realizzazione del controllore. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 55
> ![[CA-E-p055-1.jpg]]
> Problema 2: non linearità trigonometrica e bacino locale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 56
> ![[CA-E-p056-1.jpg]]
> Problema 3: punto operativo non nullo e confronto delle leggi. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
