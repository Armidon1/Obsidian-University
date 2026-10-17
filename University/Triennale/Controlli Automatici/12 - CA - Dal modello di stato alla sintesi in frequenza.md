---
title: "Dal modello di stato alla sintesi in frequenza"
aliases:
  - "CA — Dal modello di stato alla sintesi in frequenza"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "101-105"
class_label: "Blocco in ordine di dispensa; data non assegnata"
---

# Dal modello di stato alla sintesi in frequenza

> [!abstract]
> Questa lezione sviluppa dal modello di stato alla sintesi in frequenza seguendo il blocco delle pagine 101–105 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Prima:** [[11 - CA - Progetto in frequenza con processi interconnessi]]. **Dopo:** [[13 - CA - Progetto mediante luogo delle radici]].

## Ricavare la FdT dal modello assegnato

Vedi [[CA - Conversione stato trasferimento]] · [[CA - Guadagno a bassa frequenza]].

Quando il processo è dato da matrici, il primo passaggio per il progetto classico è $P(s)=C(sI-A)^{-1}B+D$. Per non invertire inutilmente una matrice simbolica si può risolvere $(sI-A)X=BU$ e poi $Y=CX+DU$. I sistemi triangolari o in forma canonica permettono spesso una soluzione diretta.

Il denominatore $\det(sI-A)$ è un candidato: prima di dichiarare ordine e poli della FdT occorre controllare le cancellazioni. Il polinomio caratteristico completo rimane necessario per la stabilità interna. Richiami: [[TDS - Funzione di trasferimento]], [[GEO - Matrice inversa]] e [[GEO - Polinomio caratteristico]].

Se $P(s)\sim K_P/s^\nu$, si combina questo limite con quello del controllore per trovare il tipo e la costante d'errore. Non usare automaticamente $P(0)$ quando il processo ha un polo in origine.

_(Dispensa commentata, pagine PDF 101–102; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 101
> ![[CA-p101-1.jpg]]
> L'esercizio parte da matrici di stato: la FdT si ricava risolvendo le equazioni nel dominio di Laplace e controllando le cancellazioni.

> [!example]- Materiale originale — pagina PDF 102
> ![[CA-p102-1.jpg]]
> Il Bode del processo equivalente e il limite statico fissano il primo tentativo di controllore prima delle reti dinamiche.

## Completare il progetto e confrontare le alternative

Vedi [[CA - Verifica esatta di Bode]] · [[CA - Scelta della rete]] · [[CA - Poli e zeri dominanti]].

Le pagine di esercizi confrontano la soluzione con rete anticipatrice e le situazioni in cui la compensazione può essere meno aggressiva. Il criterio di scelta resta il doppio vincolo locale su modulo e fase; la verifica finale comprende il polinomio chiuso.

Uno zero vicino a un polo dominante può modificare sensibilmente il transitorio. La previsione ricavata dal solo margine di fase è meno affidabile con zeri vicini all'origine, zeri a parte reale positiva, ritardi e poli poco separati. Non trattare ogni anello come un secondo ordine standard.

Per rendere il progetto ripetibile annotare: modello originale, processo equivalente, controllore completo, valori esatti di $\omega_c$ e $m_\varphi$, tipo e costante di errore, poli chiusi, banda e picco di $T$. Le figure prima e dopo compensazione sono il controllo visivo di questi calcoli.

_(Dispensa commentata, pagine PDF 103–105; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 103
> ![[CA-p103-1.jpg]]
> Il difetto di fase viene tradotto in una compensazione concreta; la rete deve rispettare anche il livello unitario di modulo.

> [!example]- Materiale originale — pagina PDF 104
> ![[CA-p104-1.jpg]]
> Il secondo esercizio verifica come cambia il progetto quando lo schema e la posizione delle rotture sono differenti.

> [!example]- Materiale originale — pagina PDF 105
> ![[CA-p105-1.jpg]]
> Il riepilogo confronta le scelte delle reti nei due esercizi e chiude la parte di sintesi guidata dal Bode.

## Esercizi collegati

[[E06 - CA - Prova intermedia 2023-2024]]
