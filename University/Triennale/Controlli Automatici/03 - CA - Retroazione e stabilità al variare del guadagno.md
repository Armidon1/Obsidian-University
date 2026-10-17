---
title: "Retroazione e stabilità al variare del guadagno"
aliases:
  - "CA — Retroazione e stabilità al variare del guadagno"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "35-38"
class_label: "03/03"
---

# Retroazione e stabilità al variare del guadagno

> [!abstract]
> Questa lezione sviluppa retroazione e stabilità al variare del guadagno seguendo il blocco delle pagine 35–38 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 03/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[02 - CA - Interconnessioni e criterio di Nyquist]]. **Dopo:** [[04 - CA - Robustezza margini di stabilità e criterio di Bode]].

## Stabilità regolare e condizionata

Vedi [[CA - Stabilità regolare]] · [[CA - Stabilità condizionata]].

La retroazione non rende stabile ogni processo e aumentare il guadagno non migliora sempre il comportamento. Studiando $1+kF_0(s)$ si possono ottenere intervalli AS di forme differenti: da zero a un massimo, sopra una soglia minima, oppure tra due valori critici. Il manoscritto distingue questi comportamenti mediante i diagrammi di Nyquist e la posizione degli intervalli sull'asse di $k$.

La distinzione operativa è questa: prima si determina l'intero insieme di guadagni stabilizzanti, poi si progetta al suo interno. Una situazione in cui ridurre il guadagno destabilizza il sistema richiede cautela: l'intuizione «meno guadagno significa più stabilità» non è generale.

> [!example] Un processo instabile stabilizzato sopra soglia
> Per $P=1/(s-1)$ e controllore proporzionale $k$, il polo chiuso è $1-k$: il sistema è AS per $k>1$. Il guadagno piccolo non è sicuro. Il margine va interpretato rispetto all'intervallo corretto.

_(Dispensa commentata, pagine PDF 35–36; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 35
> ![[CA-p035-1.jpg]]
> La nuova lezione classifica gli intervalli di stabilità al variare del guadagno: un massimo ammissibile è solo uno dei comportamenti possibili.

> [!example]- Materiale originale — pagina PDF 36
> ![[CA-p036-1.jpg]]
> Gli intervalli disegnati mostrano che può esistere anche una soglia minima; il guadagno più piccolo non è sempre il più sicuro.

## Casi limite e modi non eliminabili

Vedi [[CA - Modi fissi]] · [[CA - Cancellazioni instabili]].

L'equazione ridotta della FdT deve essere accompagnata da un controllo dei modi interni. Un polo che non è raggiunto dall'ingresso o non è osservato dall'uscita può restare invariato qualunque sia il guadagno esterno: è un modo fisso per quella architettura.

Se $P$ ha un polo instabile e il controllore introduce uno zero coincidente, la FdT ridotta può sembrare innocua, ma il modo fisico non è stato stabilizzato. Le perturbazioni iniziali e le incertezze di modello rendono visibile il problema. Questo collega l'analisi classica a [[TDS - Scomposizione di Kalman]] e anticipa la parte sullo stato.

La pagina di esercizio lasciata parzialmente vuota nella dispensa serve da traccia: il procedimento completo è fattorizzare $F_0$, contare i poli instabili, costruire Nyquist, isolare i valori critici e verificare ogni intervallo con Routh o con le radici del polinomio completo.

_(Dispensa commentata, pagine PDF 37–38; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 37
> ![[CA-p037-1.jpg]]
> Gli esempi mettono in evidenza limiti strutturali e modi non eliminabili: prima di ottimizzare il guadagno occorre verificare la stabilizzabilità della struttura.

> [!example]- Materiale originale — pagina PDF 38
> ![[CA-p038-1.jpg]]
> La pagina è una traccia di esercizio non completata: applicare l'analisi del denominatore e il conteggio del punto critico descritti nella sezione.
