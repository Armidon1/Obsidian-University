---
title: "Prova intermedia 2022-2023"
aliases:
  - "CA — Prova intermedia 2022-2023"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "24-31"
---

# Prova intermedia 2022-2023

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[02 - CA - Interconnessioni e criterio di Nyquist]] · [[09 - CA - Progetto in frequenza e reti compensatrici]] · [[14 - CA - Punti multipli e costruzione del luogo delle radici]] · [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]].

## Problema 1 - Intervallo stabile negativo

Per $F=k(s-1)^2/[(s^2+1)(s+1)]$:
$$\chi=s^3+(1+k)s^2+(1-2k)s+(1+k).$$
Routh impone $1+k>0$, $1-2k>0$ e $(1+k)(1-2k)>1+k$, quindi **$-1<k<0$**. Per $k>0$ ci sono due poli a parte reale positiva; per $k<-1$ tre. In $k=-1$ si ottiene $s(s^2+3)$, in $k=0$ si conserva la coppia $\pm j$: nessuno dei due estremi è AS.

Questo esercizio mostra perché il segno del guadagno deve essere libero durante l'analisi: cercando soltanto $k>0$ si perderebbe l'intero insieme stabilizzante.

## Problema 2 - Velocità dell automobile

Dal modello $m\dot v+bv=f$ si usa $P=1/(ms+b)$, non il modello di posizione. La specifica sull'errore a regime determina il guadagno o l'azione integrale; attraversamento e margine determinano la compensazione. Le unità di misura permettono di controllare il modello.

## Problema 3 - Equazioni di stato e controllore minimo

Ricavare la FdT dalle equazioni assegnate, distinguere i canali dell'ingresso e del disturbo e procedere con l'assegnazione del denominatore. Le pagine 29–30 conservano la soluzione grafica e matriciale. I quesiti finali vanno discussi distinguendo stabilità nominale, errore e tipo del sistema.

_(Eserciziario, pagine PDF 24–31; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 24
> ![[CA-E-p024-1.jpg]]
> Traccia completa della prova intermedia 2022-2023. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 25
> ![[CA-E-p025-1.jpg]]
> Problema 1: Nyquist con guadagno negativo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 26
> ![[CA-E-p026-1.jpg]]
> Problema 1: verifica con Routh e luogo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 27
> ![[CA-E-p027-1.jpg]]
> Problema 2: modello dell’automobile e requisiti statici. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 28
> ![[CA-E-p028-1.jpg]]
> Problema 2: diagrammi prima e dopo la compensazione. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 29
> ![[CA-E-p029-1.jpg]]
> Problema 3: FdT dalle equazioni e scelta della struttura. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 30
> ![[CA-E-p030-1.jpg]]
> Problema 3: luogo e controllore finale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 31
> ![[CA-E-p031-1.jpg]]
> Problema 4: affermazioni e motivazioni. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
