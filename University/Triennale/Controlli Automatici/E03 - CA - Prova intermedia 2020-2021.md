---
title: "Prova intermedia 2020-2021"
aliases:
  - "CA — Prova intermedia 2020-2021"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "12-16"
---

# Prova intermedia 2020-2021

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[02 - CA - Interconnessioni e criterio di Nyquist]] · [[06 - CA - Specifiche statiche tipo del sistema ed errore a regime]] · [[09 - CA - Progetto in frequenza e reti compensatrici]] · [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]].

## Problema 1 - Processo instabile e zero destro

È assegnato $F=k(s-1)/(s-10)^2$. Il denominatore chiuso è
$$\chi=s^2+(k-20)s+(100-k).$$
La stabilità stretta richiede **$20<k<100$**. Per $k<20$ ci sono due poli a parte reale positiva; per $k>100$ uno. Agli estremi si hanno rispettivamente una coppia immaginaria e un polo nullo: entrambi sono esclusi.

Per $r(t)=2$ e $k$ nell'intervallo AS, $F(0)=-k/100$ e
$$e_\infty=\frac{2}{1-k/100}=\frac{200}{100-k}.$$
Per esempio a $k=50$, $e_\infty=4$ e $y_\infty=-2$: la stabilità non implica che il segno della risposta statica sia quello desiderato. Per $r=2t$ l'errore è non limitato, poiché il tipo è zero.

## Problema 2 - Riduzione dello schema

Nel processo con disturbo su un ramo ricavare entrambi i trasferimenti equivalenti. I vincoli statici e quello sul margine devono riferirsi all'anello corretto; il limite di banda va verificato dopo la compensazione.

## Problema 3 - Ascensore

L'uscita richiesta è la posizione. Dalla dinamica $m\ddot q=u+d$ si ottiene un doppio integratore, con un disturbo costante legato al peso. Senza saturazioni si può compensare il valore nominale con un termine costante, ma per errore robustamente nullo rispetto a una forza ignota occorre analizzare il canale del disturbo e la necessità dell'integratore nel controllore.

_(Eserciziario, pagine PDF 12–16; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 12
> ![[CA-E-p012-1.jpg]]
> Traccia completa della prova intermedia 2020-2021. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 13
> ![[CA-E-p013-1.jpg]]
> Problema 1: stabilità del processo instabile e calcolo dell’errore. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 14
> ![[CA-E-p014-1.jpg]]
> Problema 2: schema equivalente e sintesi in frequenza. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 15
> ![[CA-E-p015-1.jpg]]
> Problema 2: confronto dei diagrammi compensati. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 16
> ![[CA-E-p016-1.jpg]]
> Problema 3: modello dell’ascensore e struttura del controllore. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
