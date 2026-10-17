---
title: "Prova finale 2018-2019"
aliases:
  - "CA — Prova finale 2018-2019"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "46-51"
---

# Prova finale 2018-2019

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]] · [[22 - CA - Osservatore asintotico e rilevabilità]] · [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]] · [[25 - CA - Equilibri e stabilità dei sistemi non lineari]] · [[26 - CA - Metodo diretto di Lyapunov]] · [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Problema 1 - Feedback e osservatore

Prima della scelta dei guadagni calcolare raggiungibilità e osservabilità. Se un rango è deficitario, identificare il modo fisso: l'assegnazione di tutti i poli è possibile soltanto se quel modo è compatibile con il polinomio richiesto. Per retroazione dell'uscita servono stabilizzabilità e rilevabilità; un osservatore non crea raggiungibilità.

## Problema 2 - Un certificato globale

Per $\dot x_1=-x_1^3+x_2$, $\dot x_2=-2x_1-x_2$, l'origine è l'unico equilibrio: sostituendo $x_2=-2x_1$ nella prima equazione si ottiene $x_1(x_1^2+2)=0$. La Jacobiana nell'origine ha polinomio $\lambda^2+\lambda+2$, quindi prova AS locale.

Si può concludere di più con
$$V=x_1^2+\frac12x_2^2,\qquad \dot V=-2x_1^4-x_2^2.$$
La funzione è DP e radialmente illimitata, la derivata è definita negativa: l'origine è **GAS**. La scelta dei pesi cancella i termini misti ed evita di fermarsi al risultato locale.

## Problema 3 - Pendolo attuato

Scrivere lo stato $(\theta,\dot\theta)$, trovare la coppia di equilibrio per l'angolo richiesto e linearizzare attorno a quel punto. La legge finale deve includere sia il termine di equilibrio sia il feedback delle variazioni. Il segno della gravità cambia tra la configurazione bassa e quella alta.

_(Eserciziario, pagine PDF 46–51; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 46
> ![[CA-E-p046-1.jpg]]
> Traccia completa della prova finale 2018-2019. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 47
> ![[CA-E-p047-1.jpg]]
> Problema 1: raggiungibilità, osservabilità e feedback. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 48
> ![[CA-E-p048-1.jpg]]
> Problema 1: osservatore e controllore dinamico. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 49
> ![[CA-E-p049-1.jpg]]
> Problema 2: equilibrio e certificato di Lyapunov globale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 50
> ![[CA-E-p050-1.jpg]]
> Problema 3: pendolo e comando di equilibrio. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 51
> ![[CA-E-p051-1.jpg]]
> Problema 3: guadagni e legge di controllo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
