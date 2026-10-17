---
title: "Prova intermedia 2019-2020"
aliases:
  - "CA — Prova intermedia 2019-2020"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "6-11"
---

# Prova intermedia 2019-2020

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[02 - CA - Interconnessioni e criterio di Nyquist]] · [[07 - CA - Disturbi rumore e astaticità]] · [[11 - CA - Progetto in frequenza con processi interconnessi]] · [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]].

## Problema 1 - Oscillatore in anello

Per $F(s)=ks/(s^2+100)$ il polinomio chiuso è $s^2+ks+100$. È AS esattamente per **$k>0$**; per $k<0$ entrambi i poli hanno parte reale positiva, mentre $k=0$ è marginale. Il trasferimento chiuso è $T=ks/(s^2+ks+100)$.

Per un riferimento costante, $T(0)=0$: l'uscita a regime è nulla, non uguale al riferimento. Per $r=\sin10t$, $T(j10)=1$ se $k>0$: il sistema riproduce la sinusoide a regime senza errore. È un esempio di comportamento selettivo che non si riassume con la sola tabella degli ingressi polinomiali.

## Problema 2 - Processo a rami paralleli

Ricavare la somma algebrica dei rami per il canale del comando. Una cancellazione fra contributi può cambiare guadagno statico e tipo: non assegnarli osservando un ramo soltanto. L'errore relativo della rampa e i vincoli a $\omega_c=30$ rad/s si applicano al processo equivalente completo.

## Problema 3 - Disturbo in un ramo

Il canale del disturbo non coincide con il processo equivalente. Scrivere $y=P_u u+P_d d$, quindi progettare usando $GP_u$ e verificare separatamente $P_d/(1+GP_u)$. L'assegnazione del denominatore tramite coefficienti può essere più diretta del tentativo grafico quando sono prescritti poli reali. La p. 11 contiene la verifica supplementare del luogo.

_(Eserciziario, pagine PDF 6–11; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 6
> ![[CA-E-p006-1.jpg]]
> Traccia completa della prova intermedia 2019-2020. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 7
> ![[CA-E-p007-1.jpg]]
> Problema 1: oscillatore, Nyquist e risposta a regime. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 8
> ![[CA-E-p008-1.jpg]]
> Problema 2: riduzione dei rami e progetto iniziale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 9
> ![[CA-E-p009-1.jpg]]
> Problema 2: diagrammi e controllore finale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 10
> ![[CA-E-p010-1.jpg]]
> Problema 3: canale del disturbo e assegnazione dei poli. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 11
> ![[CA-E-p011-1.jpg]]
> Verifica supplementare del luogo e del guadagno. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
