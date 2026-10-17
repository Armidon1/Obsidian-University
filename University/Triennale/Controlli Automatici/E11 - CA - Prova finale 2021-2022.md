---
title: "Prova finale 2021-2022"
aliases:
  - "CA — Prova finale 2021-2022"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "63-66"
---

# Prova finale 2021-2022

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]] · [[22 - CA - Osservatore asintotico e rilevabilità]] · [[26 - CA - Metodo diretto di Lyapunov]] · [[27 - CA - LaSalle linearizzazione e studio degli equilibri]] · [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Problema 1 - Stabilizzazione parametrica

Ricavare gli autovalori non raggiungibili al variare del parametro: la condizione di stabilizzabilità si applica al loro segno, non al solo annullamento del determinante della matrice di raggiungibilità. Per l'uscita aggiungere il controllo della rilevabilità e motivare quali poli non si possono scegliere liberamente.

## Problema 2 - Caso critico risolto con LaSalle

Per $\dot x_1=-3x_2-x_1^3$, $\dot x_2=2x_1$, l'unico equilibrio è l'origine. La Jacobiana ha autovalori $\pm j\sqrt6$: il criterio indiretto non conclude. Scegliendo
$$V=\frac13x_1^2+\frac12x_2^2,\qquad\dot V=-\frac23x_1^4\le0,$$
si trova $E=\{x_1=0\}$. Per restare in $E$ deve anche essere $\dot x_1=-3x_2=0$, quindi il massimo insieme invariante è solo l'origine. Poiché $V$ è radialmente illimitata, LaSalle prova **GAS**.

> [!warning] Correzione del passaggio invariante
> A p. 65 lo svolgimento passa verbalmente al caso «$x_2=0$» dopo avere trovato l'annullamento della derivata. Il vincolo da cui partire è invece **$x_1=0$**; l'equazione del moto impone poi $x_2=0$. È essenziale distinguere i due passaggi.

## Problema 3 - Molla non lineare

Per un carrello con richiamo cubico, trovare la forza che mantiene la posizione richiesta, traslare il punto di lavoro e linearizzare. Il controllo locale stabilizza la Jacobiana; una candidata energetica può ampliare la conclusione senza cancellare il richiamo stabilizzante.

_(Eserciziario, pagine PDF 63–66; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 63
> ![[CA-E-p063-1.jpg]]
> Traccia completa della prova finale 2021-2022. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 64
> ![[CA-E-p064-1.jpg]]
> Problema 1: stabilizzabilità e rilevabilità parametriche. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 65
> ![[CA-E-p065-1.jpg]]
> Problema 2: caso critico, funzione pesata e LaSalle. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 66
> ![[CA-E-p066-1.jpg]]
> Problema 3: carrello con richiamo cubico e punto di lavoro. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
