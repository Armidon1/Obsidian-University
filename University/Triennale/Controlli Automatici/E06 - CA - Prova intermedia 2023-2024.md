---
title: "Prova intermedia 2023-2024"
aliases:
  - "CA — Prova intermedia 2023-2024"
tags:
  - controlli-automatici
  - esercitazione
  - esame
source: "pdf/ES ERCIZI CONTROLLi_250609_213750.pdf"
pdf_pages: "32-37"
---

# Prova intermedia 2023-2024

> [!abstract]
> Guida alla prova nell'ordine dell'eserciziario: risultati verificati per i casi esplicitamente svolti in testo, procedure e scansioni integrali per gli altri passaggi. [[MOC - Controlli Automatici]].

**Richiami:** [[02 - CA - Interconnessioni e criterio di Nyquist]] · [[07 - CA - Disturbi rumore e astaticità]] · [[12 - CA - Dal modello di stato alla sintesi in frequenza]] · [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]].

## Problema 1 - Controllo della frontiera con Routh

Per $F=k/[(s+1)(s^2+100)]$:
$$\chi=s^3+s^2+100s+(100+k).$$
La prima colonna della tabella di Routh è $1,1,-k,100+k$. Perciò l'AS richiede **$-100<k<0$**. Per $k>0$ ci sono due poli con parte reale positiva, per $k<-100$ uno. A $k=-100$ c'è un polo nullo; a $k=0$ una coppia immaginaria.

> [!warning] Correzione dello svolgimento
> Nell'eserciziario, p. 33, il riquadro finale riporta soltanto «$k>k^*=-100$». Manca il vincolo superiore **$k<0$**, necessario dalla terza riga di Routh. Il grafico qualitativo nella stessa pagina identifica già l'intervallo negativo: la soluzione completa è $-100<k<0$.

## Problema 2 - Da stato a Bode

Le equazioni del processo vanno trasformate conservando correttamente il disturbo; il vincolo statico si applica al relativo canale. Poi il tempo di assestamento e il margine guidano la scelta della pulsazione e della rete, ma si verificano infine sul sistema chiuso.

## Problemi 3 e 4 - Dimensione minima e affermazioni

L'assegnazione polinomiale permette di imporre i poli con il minimo ordine compatibile con la struttura richiesta. Nel motivare i vero/falso distinguere fra proprietà della FdT ridotta e proprietà di una realizzazione interna, soprattutto quando la stabilità del processo non è garantita.

_(Eserciziario, pagine PDF 32–37; numerazione fisica del file.)_

## Testi grafici e svolgimenti originali

Le pagine seguenti conservano l'ordine della prova, con tracce e soluzioni manoscritte. I risultati riscritti sopra sono stati ricalcolati; i dettagli numerici non trascritti restano consultabili nell'originale e non sono dichiarati tutti verificati.

> [!example]- Eserciziario — pagina PDF 32
> ![[CA-E-p032-1.jpg]]
> Traccia completa della prova intermedia 2023-2024. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 33
> ![[CA-E-p033-1.jpg]]
> Problema 1: Nyquist e Routh; il riquadro finale va completato con k negativo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 34
> ![[CA-E-p034-1.jpg]]
> Problema 2: conversione dalle equazioni al trasferimento. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 35
> ![[CA-E-p035-1.jpg]]
> Problema 2: Bode e progetto della rete. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 36
> ![[CA-E-p036-1.jpg]]
> Problema 3: controllo minimo in presenza di disturbo. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.

> [!example]- Eserciziario — pagina PDF 37
> ![[CA-E-p037-1.jpg]]
> Problema 4: verifica delle affermazioni. La lettura va collegata alle equazioni e alle verifiche della sezione corrispondente; i segni dei sommatori e i modi fissi vanno conservati nel confronto con i grafici.
