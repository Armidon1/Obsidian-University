---
title: "Prova intermedia 2018-2019"
aliases:
  - "CA — Prova intermedia 2018-2019"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "1-5"
---

# Prova intermedia 2018-2019

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[02 - CA - Interconnessioni e criterio di Nyquist]] · [[06 - CA - Specifiche statiche tipo del sistema ed errore a regime]] · [[09 - CA - Progetto in frequenza e reti compensatrici]] · [[15 - CA - Progetto sul luogo con aggiunta di poli e zeri]].

## Problema 1 - Nyquist e Routh

Il ramo diretto è $F=k(s+1)^2/[s^2(s-1)]$. Il polinomio chiuso è
$$\chi=s^3+(k-1)s^2+2ks+k.$$
Routh richiede $k-1>0$, $k>0$ e $(k-1)2k>k$, quindi **$k>3/2$**. Per $k<0$ c'è un polo a parte reale positiva; per $0<k<3/2$ ce ne sono due. A $k=3/2$, $\chi=(s+1/2)(s^2+3)$: due poli sono sull'asse immaginario e non si ha AS. A $k=0$ ricompaiono i modi aperti, inclusi quelli nulli.

Nyquist deve considerare un polo aperto nel semipiano destro e due poli nell'origine: ignorare le indentazioni darebbe un conteggio sbagliato. Il diagramma originale mostra entrambi i segni di $k$; il confronto con Routh ne quantifica esattamente gli intervalli.

## Problema 2 - Precisione e compensazione

Il disturbo entra nel processo: ricavare il suo trasferimento prima di scegliere gli integratori. Un polo in origine nel solo processo non garantisce astaticità rispetto a quel disturbo. Dopo la struttura statica, imporre il modulo unitario a $\omega_c=1$ rad/s e il margine richiesto, quindi verificare la rete esatta.

## Problema 3 - Dimensione minima

Per un riferimento costante e un disturbo costante all'ingresso, il controllore deve soddisfare sia il vincolo di precisione sia il rigetto nel canale $PS$. Il luogo della struttura iniziale mostra se il guadagno basta; in caso contrario aggiungere il minimo numero di poli e zeri necessario e motivarlo. Le pagine 3–5 conservano tracce, grafici e passaggi di sintesi.

_(Eserciziario, pagine PDF 1–5; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 1
> ![[CA-E-p001-1.jpg]]
> Traccia completa della prova intermedia 2018-2019. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 2
> ![[CA-E-p002-1.jpg]]
> Problema 1: Bode, Nyquist e verifica con Routh. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 3
> ![[CA-E-p003-1.jpg]]
> Problema 2: impostazione statica e anello iniziale. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 4
> ![[CA-E-p004-1.jpg]]
> Problema 2: diagrammi dopo la compensazione. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 5
> ![[CA-E-p005-1.jpg]]
> Problema 3: progetto sul luogo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
