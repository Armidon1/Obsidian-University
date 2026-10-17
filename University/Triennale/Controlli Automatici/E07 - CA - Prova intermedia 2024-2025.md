---
title: "Prova intermedia 2024-2025"
aliases:
  - "CA — Prova intermedia 2024-2025"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "38-45"
---

# Prova intermedia 2024-2025

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[02 - CA - Interconnessioni e criterio di Nyquist]] · [[06 - CA - Specifiche statiche tipo del sistema ed errore a regime]] · [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]] · [[24 - CA - Inseguimento di riferimenti e modello interno]].

## Problema 1 - Tipo due e ingressi non normalizzati

Per $F=k(10s+1)/[s^2(s+100)]$:
$$\chi=s^3+100s^2+10ks+k.$$
Routh richiede $k>0$ e $100\cdot10k>k$, quindi l'intero intervallo **$k>0$** è AS. Per $k<0$ c'è un polo a parte reale positiva. Il sistema è di tipo 2 e $K_a=k/100$.

Con $r_1=2t$, l'errore tende a zero. Con $r_2=2t^2$, $R_2=4/s^3$ ed $e_\infty=4/K_a=400/k$. Con $r_3=2t^3$, l'errore è non limitato e il termine dominante cresce come $(1200/k)t$. Usare la tabella della parabola $t^2/2$ senza riscalarla produrrebbe un errore di fattore 4.

## Problema 2 - Inseguimento e disturbo

Si richiedono errore nullo al gradino, un limite sull'errore alla rampa e astaticità al disturbo. Imporre ognuna delle tre condizioni sul trasferimento appropriato prima di scegliere l'ordine del controllore.

## Problema 3 - Pendolo sul carrello

Il modello linearizzato ha forma $\ddot\theta=a\theta-bf$. La FdT è $-b/(s^2-a)$. Il caso $a>0$ contiene un polo instabile; il caso $a=0$ è un doppio integratore. Un guadagno statico può modificare la rigidezza ma non introduce da solo un termine di smorzamento: la struttura del controllore deve tenerne conto.

## Problema 4 - PI e disturbo

Il blocco $1/s+10$ forma una legge PI. Per ciascuna affermazione calcolare il trasferimento dal riferimento o dal disturbo al punto richiesto; un offset può essere indipendente da $k$ o annullarsi secondo la posizione del disturbo, non secondo il solo nome del controllore.

_(Eserciziario, pagine PDF 38–45; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 38
> ![[CA-E-p038-1.jpg]]
> Traccia della prova intermedia 2024-2025, prima pagina. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 39
> ![[CA-E-p039-1.jpg]]
> Traccia della prova intermedia 2024-2025, seconda pagina. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 40
> ![[CA-E-p040-1.jpg]]
> Problema 1: stabilità con Nyquist e Routh. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 41
> ![[CA-E-p041-1.jpg]]
> Problema 1: luogo delle radici e proseguimento. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 42
> ![[CA-E-p042-1.jpg]]
> Problema 2: modello, errore e disturbo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 43
> ![[CA-E-p043-1.jpg]]
> Problema 3: pendolo sul carrello, primo caso. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 44
> ![[CA-E-p044-1.jpg]]
> Problema 3: confronto delle condizioni sul parametro. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 45
> ![[CA-E-p045-1.jpg]]
> Problema 4: PI e risposte ai quesiti. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
