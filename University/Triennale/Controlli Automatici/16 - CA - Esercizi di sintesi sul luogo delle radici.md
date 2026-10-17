---
title: "Esercizi di sintesi sul luogo delle radici"
aliases:
  - "CA — Esercizi di sintesi sul luogo delle radici"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "123-128"
class_label: "06/04"
---

# Esercizi di sintesi sul luogo delle radici

> [!abstract]
> Questa lezione sviluppa esercizi di sintesi sul luogo delle radici seguendo il blocco delle pagine 123–128 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 06/04. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[15 - CA - Progetto sul luogo con aggiunta di poli e zeri]]. **Dopo:** [[17 - CA - Poli dominanti e vincoli sul transitorio]].

## Compensazione e cancellazioni ammissibili

Vedi [[CA - Compensazione sul luogo]] · [[CA - Cancellazione di poli stabili]].

La compensazione modifica il luogo dell'intero anello $GP$, non quello del solo processo. Una cancellazione di un polo stabile può essere usata come approssimazione progettuale, tenendo presenti incertezza e modo residuo; una cancellazione instabile non realizza una stabilizzazione interna.

L'obiettivo è trovare un controllore con ordine e struttura sufficienti a soddisfare i vincoli, senza introdurre inutilmente stati. «Dimensione minima» significa motivare perché un controllore di ordine inferiore non potrebbe soddisfare insieme precisione e stabilità.

Nelle esercitazioni si confrontano luoghi prima e dopo la compensazione, si cercano punti multipli e si determinano gli intervalli di guadagno AS. La verifica con Routh permette di evitare conclusioni basate su tratti disegnati troppo vicino all'asse immaginario.

_(Dispensa commentata, pagine PDF 123–126; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 123
> ![[CA-p123-1.jpg]]
> La compensazione sul luogo viene applicata a processi per cui il guadagno da solo non basta: si confrontano le strutture prima e dopo.

> [!example]- Materiale originale — pagina PDF 124
> ![[CA-p124-1.jpg]]
> Gli esempi mostrano perché una compensazione va verificata sul sistema interno, evitando di usare cancellazioni instabili come stabilizzazione.

> [!example]- Materiale originale — pagina PDF 125
> ![[CA-p125-1.jpg]]
> I diagrammi successivi confrontano i rami al cambiare dei poli e zeri del controllore e localizzano i punti multipli.

> [!example]- Materiale originale — pagina PDF 126
> ![[CA-p126-1.jpg]]
> Il riepilogo delle strutture collega numero di parametri, grado relativo e possibilità di soddisfare le specifiche.

## Intersecare vincoli statici e dinamici

Vedi [[CA - Intersezione delle specifiche]] · [[CA - Guadagni ammissibili]] · [[CA - Minimo ordine del controllore]].

Un vincolo come $e_{\infty,\text{rampa}}\le\varepsilon$ diventa una disuguaglianza su $k$; Routh ne dà un'altra per la stabilità. Il risultato del progetto è la loro intersezione, non uno dei due insiemi preso separatamente.

> [!example] Incompatibilità con il solo guadagno
> Per $F=k/[s(s+1)(s+2)]$, $K_v=k/2$ e l'errore alla rampa è $2/k$. Routh sul polinomio $s^3+3s^2+2s+k$ dà $0<k<6$. Se si richiede $e_\infty\le0.1$, serve $k\ge20$: l'intersezione è vuota. Occorre una compensazione, non un nuovo tentativo di guadagno.

Se un valore critico compare con uguaglianza in Routh, si analizza il caso separatamente. La presenza di poli sull'asse immaginario esclude l'AS e rende inapplicabili in modo automatico le formule d'errore usate per il progetto.

_(Dispensa commentata, pagine PDF 127–128; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 127
> ![[CA-p127-1.jpg]]
> L'esercizio impone un limite d'errore e trova il relativo insieme di guadagni: occorre intersecarlo con quello AS.

> [!example]- Materiale originale — pagina PDF 128
> ![[CA-p128-1.jpg]]
> Il confronto con Routh conclude l'esercizio: se gli intervalli non si incontrano bisogna modificare il controllore, non ignorare una delle richieste.
