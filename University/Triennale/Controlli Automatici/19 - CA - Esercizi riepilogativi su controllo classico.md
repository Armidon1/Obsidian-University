---
title: "Esercizi riepilogativi su controllo classico"
aliases:
  - "CA — Esercizi riepilogativi su controllo classico"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "141-148"
class_label: "13/04"
---

# Esercizi riepilogativi su controllo classico

> [!abstract]
> Questa lezione sviluppa esercizi riepilogativi su controllo classico seguendo il blocco delle pagine 141–148 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 13/04. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]]. **Dopo:** [[20 - CA - Raggiungibilità osservabilità e forme canoniche]].

## Processi con disturbi e schemi equivalenti

Vedi [[CA - Metodo di progetto classico]] · [[CA - Disturbi interni allo schema]].

Gli esercizi riepilogativi combinano riduzione di schemi, tipo, guadagno, stabilità e luogo. Il primo passo è sempre individuare che cosa si vuole regolare e in quale punto entra ciascun disturbo. Con $y=P_u u+P_d d$, i trasferimenti chiusi sono $T_r=GP_u/(1+GP_u)$ e $T_d=P_d/(1+GP_u)$.

Da $T_r$ si ricavano precisione e inseguimento; da $T_d$ il rigetto. Lo stesso disturbo costante può essere annullato o lasciare un offset a seconda di $P_d$. Non trasferire un sommatore attraverso un blocco senza trasformare anche il segnale che vi entra.

Le specifiche dinamiche si affrontano poi con LdR o compensazione in frequenza. Per ogni struttura scelta il polinomio completo è il riferimento per la stabilità, inclusi eventuali modi cancellati.

_(Dispensa commentata, pagine PDF 141–145; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 141
> ![[CA-p141-1.jpg]]
> Gli esercizi riepilogativi ripartono dal modello e dai disturbi: la riduzione dello schema viene prima della scelta del controllore.

> [!example]- Materiale originale — pagina PDF 142
> ![[CA-p142-1.jpg]]
> Il primo luogo distingue intervalli stabili e punti critici; la struttura integrale deve rimanere compatibile con le altre specifiche.

> [!example]- Materiale originale — pagina PDF 143
> ![[CA-p143-1.jpg]]
> Il secondo esercizio modifica i poli e gli zeri della compensazione e ricalcola i trasferimenti dei diversi ingressi.

> [!example]- Materiale originale — pagina PDF 144
> ![[CA-p144-1.jpg]]
> Il confronto dei luoghi evidenzia come cambiano i modi chiusi dopo la modifica dello schema di controllo.

> [!example]- Materiale originale — pagina PDF 145
> ![[CA-p145-1.jpg]]
> Le equazioni dei rami ricavano separatamente comando e disturbo, evitando di spostare un sommatore senza il suo fattore di trasferimento.

## Verifica finale e schema risolutivo

Vedi [[CA - Checklist del progetto]] · [[CA - Valori critici del guadagno]] · [[CA - Controllore completo]].

Il riepilogo del manoscritto distingue i due rami principali: progetto in frequenza e progetto sul luogo. In entrambi, dopo avere scelto la struttura, serve un valore numerico del guadagno appartenente all'insieme ammissibile e la scrittura della FdT completa del controllore.

1. Ricavare processo e canali dei disturbi.
2. Imporre tipo e costanti di errore.
3. Determinare l'intervallo AS.
4. Soddisfare rapidità e smorzamento con i parametri rimasti.
5. Controllare realizzabilità, modi interni e prestazioni chiuse.

> [!example] Un limite di stabilità non è una soluzione
> Per $\chi=s^3+3s^2+2s+k$, $k=6$ dà $(s+3)(s^2+2)$: la coppia immaginaria persiste senza decadere. Usare $k=6$ per un progetto che richiede AS è errato, anche se il diagramma disegnato sembra toccare appena la frontiera.

Lo schema riassuntivo della p. 148 va usato come mappa dei passaggi, mentre le singole condizioni devono essere ricalcolate sul processo assegnato.

_(Dispensa commentata, pagine PDF 146–148; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 146
> ![[CA-p146-1.jpg]]
> L'ultimo esempio applica il confronto dei coefficienti e controlla che nessuna radice marginale venga inclusa come AS.

> [!example]- Materiale originale — pagina PDF 147
> ![[CA-p147-1.jpg]]
> La discussione delle frontiere collega il disegno delle radici alla stabilità stretta e richiama il controllo dei modi fissi.

> [!example]- Materiale originale — pagina PDF 148
> ![[CA-p148-1.jpg]]
> Lo schema risolutivo riassume i passaggi dei due metodi classici: precisione, stabilità, compensazione e verifica del risultato completo.
