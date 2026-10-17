---
title: "Punti multipli e costruzione del luogo delle radici"
aliases:
  - "CA — Punti multipli e costruzione del luogo delle radici"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "113-117"
class_label: "31/03"
---

# Punti multipli e costruzione del luogo delle radici

> [!abstract]
> Questa lezione sviluppa punti multipli e costruzione del luogo delle radici seguendo il blocco delle pagine 113–117 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 31/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[13 - CA - Progetto mediante luogo delle radici]]. **Dopo:** [[15 - CA - Progetto sul luogo con aggiunta di poli e zeri]].

## Radici multiple e punti di diramazione

Vedi [[CA - Punti multipli del luogo]] · [[CA - Derivata del guadagno]].

Un punto di diramazione è una radice multipla del polinomio chiuso. Deve soddisfare simultaneamente $D+kN=0$ e $D'+kN'=0$. Eliminando $k$ si ottiene
$$D'(s)N(s)-D(s)N'(s)=0,$$
equivalente a $dk(s)/ds=0$ per $k(s)=-D(s)/N(s)$ nei punti dove questa espressione è definita. L'equazione logaritmica è $\sum_i1/(s-p_i)-\sum_j1/(s-z_j)=0$.

Le soluzioni sono soltanto **candidate**: bisogna verificare che appartengano al luogo del segno di $k$ considerato e che il guadagno calcolato sia reale e del segno richiesto. Un punto sul reale può appartenere al luogo negativo ma non a quello positivo.

> [!example] Verifica del candidato
> Per $F_0=1/[s(s+2)]$, $k(s)=-s(s+2)$ e $k'=-2s-2$: il candidato $s=-1$ dà $k=1>0$, quindi è un punto di diramazione del luogo positivo.

_(Dispensa commentata, pagine PDF 113–114; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 113
> ![[CA-p113-1.jpg]]
> La condizione di radice multipla collega incontro dei rami e derivata del guadagno, con distinzione del luogo positivo e negativo.

> [!example]- Materiale originale — pagina PDF 114
> ![[CA-p114-1.jpg]]
> I disegni locali mostrano le direzioni di diramazione vicino a una radice multipla; non tutti i candidati sono ammissibili.

## Tracciare un luogo completo

Vedi [[CA - Procedura del luogo]] · [[CA - Verifica con Routh]] · [[CA - Simmetria del luogo]].

La costruzione procede in quest'ordine: segnare poli e zeri, fissare il segno di $k$, selezionare tratti reali, calcolare centro e asintoti, trovare i punti multipli ammissibili, determinare eventuali attraversamenti dell'asse immaginario, collegare i rami rispettando la simmetria rispetto al reale.

Ogni polo iniziale genera un ramo e ogni zero finito ne riceve uno; il numero totale dei rami è l'ordine del polinomio caratteristico per guadagno generico. La simmetria deriva dai coefficienti reali. Non si possono inventare incroci tra rami: un incontro richiede una radice multipla.

Le figure della dispensa mostrano esempi con zeri, punti multipli e tratti appartenenti a luoghi di segno opposto. Il controllo finale è sostituire uno o due guadagni rappresentativi nel polinomio e verificare se le radici hanno la posizione prevista. Per le frontiere di stabilità usare Routh, non la sola precisione del disegno.

_(Dispensa commentata, pagine PDF 115–117; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 115
> ![[CA-p115-1.jpg]]
> L'esercizio applica le regole a un luogo con zeri: i rami devono partire e terminare nei punti corretti rispettando la simmetria.

> [!example]- Materiale originale — pagina PDF 116
> ![[CA-p116-1.jpg]]
> L'esempio successivo controlla i punti multipli e il loro guadagno, senza attribuire incroci arbitrari ai rami.

> [!example]- Materiale originale — pagina PDF 117
> ![[CA-p117-1.jpg]]
> Il luogo conclusivo della lezione riunisce tratti reali, diramazioni e asintoti, con una verifica dell'intervallo stabile.

## Esercizi collegati

[[E04 - CA - Prova intermedia 2021-2022]] · [[E05 - CA - Prova intermedia 2022-2023]]
