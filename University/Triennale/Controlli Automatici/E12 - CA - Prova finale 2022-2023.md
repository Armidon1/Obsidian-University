---
title: "Prova finale 2022-2023"
aliases:
  - "CA — Prova finale 2022-2023"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "67-72"
---

# Prova finale 2022-2023

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]] · [[22 - CA - Osservatore asintotico e rilevabilità]] · [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]] · [[26 - CA - Metodo diretto di Lyapunov]] · [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Problema 1 - Stato misurato e uscita

Determinare prima i modi fissi. Con stato disponibile basta la stabilizzabilità; con sola uscita serve anche la rilevabilità. Il numero di poli che si possono scegliere arbitrariamente dipende dal sottospazio raggiungibile e, per l'osservatore, da quello osservabile.

## Problema 2 - Pendolo in una configurazione assegnata

Il valore di equilibrio del comando compensa il termine gravitazionale. Dopo la traslazione, verificare raggiungibilità, scegliere il feedback e, se si misura solo l'angolo, costruire l'osservatore locale. Il principio di separazione del modello lineare non è una prova automatica di prestazioni globali del sistema non lineare.

## Problema 3 - Famiglia con certificato globale

Per $\dot x_1=-x_1^3+x_2$, $\dot x_2=-ax_1-bx_2$, $a,b>0$, gli equilibri soddisfano $x_2=x_1^3$ e $x_1(a+bx_1^2)=0$, quindi l'origine è unica. La Jacobiana ha $\lambda^2+b\lambda+a$, Hurwitz. Con
$$V=\frac12\left(x_1^2+\frac{x_2^2}{a}\right),\qquad
\dot V=-x_1^4-\frac ba x_2^2,$$
si conclude GAS. Tutte le ipotesi sono globali e la funzione è radialmente illimitata: non occorre fermarsi alla linearizzazione locale.

Nei quesiti finali ricordare che un sistema non lineare può avere molti equilibri isolati e che una linearizzazione marginale non classifica da sola il punto originale.

_(Eserciziario, pagine PDF 67–72; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 67
> ![[CA-E-p067-1.jpg]]
> Traccia completa della prova finale 2022-2023. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 68
> ![[CA-E-p068-1.jpg]]
> Problema 1: modi fissi e disponibilità dello stato. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 69
> ![[CA-E-p069-1.jpg]]
> Problema 1: progetto dell’osservatore e realizzazione. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 70
> ![[CA-E-p070-1.jpg]]
> Problema 2: pendolo e approssimazione locale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 71
> ![[CA-E-p071-1.jpg]]
> Problema 3: famiglia con funzione di Lyapunov globale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 72
> ![[CA-E-p072-1.jpg]]
> Problema 4: motivazioni dei vero/falso. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
