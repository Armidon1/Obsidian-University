---
title: "Prova completa del 12 luglio 2019"
aliases:
  - "CA — Prova completa del 12 luglio 2019"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "80-87"
---

# Prova completa del 12 luglio 2019

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[04 - CA - Robustezza margini di stabilità e criterio di Bode]] · [[09 - CA - Progetto in frequenza e reti compensatrici]] · [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]] · [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]] · [[27 - CA - LaSalle linearizzazione e studio degli equilibri]] · [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Problema 1 - Margine e guadagno

Per $P=1/(s+1)^3$ e controllore $K$, $\chi=(s+1)^3+K=s^3+3s^2+3s+1+K$. L'AS richiede $-1<K<8$. Con $K>1$, l'attraversamento soddisfa $(1+\omega_c^2)^{3/2}=K$ e il margine è $180^\circ-3\arctan\omega_c$. Per $0<K<1$ non c'è attraversamento unitario a pulsazione positiva: non inventare un margine di fase valutato a una frequenza arbitraria.

## Problema 2 - Sintesi in frequenza

I vincoli su errore, attraversamento e margine si applicano nell'ordine: struttura statica, guadagno, forma dell'anello. Il segno del guadagno e i contributi della rete vanno conservati nel calcolo della fase. La p. 87 contiene un ulteriore confronto di diagrammi.

## Problema 3 - Retroazione dinamica

Il controllore con osservatore deve essere esplicitato con matrici e segnali di ingresso e uscita. Assegnare separatamente i poli di controllo e stima, poi ricostruire $A_G=A+BK-LC$, $B_G=L$, $C_G=K$ nella convenzione adottata.

## Problema 4 - Bacino esatto nel caso scalare

Per $\dot x=x^3+u$, il feedback lineare $u=-kx$, $k>0$, dà $\dot x=x(x^2-k)$. L'origine è AS soltanto nel bacino **$(-\sqrt k,\sqrt k)$**: i due estremi sono altri equilibri e per stati esterni il campo punta via dall'origine. Con $V=x^2/2$ si ritrova $\dot V=x^2(x^2-k)<0$ all'interno.

La legge non lineare $u=-x^3-kx$ produce $\dot x=-kx$ e GAS sul modello ideale. Qui il termine cubico è destabilizzante, quindi cancellarlo ha una motivazione diversa dal caso $-bx^3$ dissipativo.

_(Eserciziario, pagine PDF 80–87; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 80
> ![[CA-E-p080-1.jpg]]
> Traccia completa della prova del 12 luglio 2019. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 81
> ![[CA-E-p081-1.jpg]]
> Problema 1: guadagno e margine di fase. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 82
> ![[CA-E-p082-1.jpg]]
> Problema 2: precisione e progetto della rete. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 83
> ![[CA-E-p083-1.jpg]]
> Problema 2: confronto dei diagrammi di Bode. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 84
> ![[CA-E-p084-1.jpg]]
> Problema 3: controllo dello stato e condizioni sui parametri. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 85
> ![[CA-E-p085-1.jpg]]
> Problema 3: osservatore e compensatore dinamico. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 86
> ![[CA-E-p086-1.jpg]]
> Problema 4: controllo cubico, bacino e legge globale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 87
> ![[CA-E-p087-1.jpg]]
> Diagrammi supplementari della compensazione. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
