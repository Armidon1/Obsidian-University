---
title: "Progetto in frequenza con processi interconnessi"
aliases:
  - "CA — Progetto in frequenza con processi interconnessi"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "98-100"
class_label: "28/03"
---

# Progetto in frequenza con processi interconnessi

> [!abstract]
> Questa lezione sviluppa progetto in frequenza con processi interconnessi seguendo il blocco delle pagine 98–100 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 28/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[10 - CA - Esercizi di compensazione anticipatrice e attenuatrice]]. **Dopo:** [[12 - CA - Dal modello di stato alla sintesi in frequenza]].

## Ridurre lo schema senza perdere il disturbo

Vedi [[CA - Riduzione dello schema]] · [[CA - Canale del disturbo]].

Con due rami $P_1,P_2$ e un disturbo interno, non si può sempre sostituire l'intero disegno con una sola FdT e sommare poi il disturbo all'uscita. La riduzione del canale del comando e quella del canale del disturbo sono calcoli distinti.

Si scrivono le equazioni dei segnali intermedi e si ricava una forma $y=P_u u+P_d d$. Solo dopo si chiude $u=G(r-y)$:
$$y=\frac{GP_u}{1+GP_u}r+\frac{P_d}{1+GP_u}d.$$
Il denominatore condiviso governa la dinamica chiusa, ma il numeratore del disturbo dipende dalla sua posizione. Per un disturbo costante il limite da imporre è $\lim_{s\to0}P_d/(1+GP_u)=0$.

_(Dispensa commentata, pagine PDF 98–99; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 98
> ![[CA-p098-1.jpg]]
> Il processo a rami richiede una riduzione dello schema prima di poter applicare le regole statiche e la compensazione.

> [!example]- Materiale originale — pagina PDF 99
> ![[CA-p099-1.jpg]]
> Le equazioni dei segnali intermedi separano il processo equivalente dal canale del disturbo: non possono essere ridotti come se fossero lo stesso ingresso.

## Dal processo equivalente alla compensazione

Vedi [[CA - Astaticità del processo equivalente]] · [[CA - Progetto con rami paralleli]] · [[CA - Controllo dei segni]].

Una volta trovato $P_u$, si sceglie $G=KR/s^h$ seguendo i vincoli statici. L'eventuale integratore già presente in un ramo conta soltanto se rimane nel trasferimento equivalente e se non viene cancellato. La specifica sulla rampa usa $K_v=\lim sGP_u$, mentre quella sul disturbo usa il trasferimento $P_d$ effettivo.

Poi si disegnano modulo e fase di $GP_u$, si valuta il margine e si aggiunge la rete necessaria. Un segno negativo in un ramo può cambiare il guadagno statico e la fase di $180^\circ$: non va assorbito nel modulo ignorandolo.

> [!tip] Controllo rapido del risultato
> Confrontare il limite statico calcolato dalla FdT con le equazioni a regime dello schema originale. Se i due risultati differiscono, cercare prima un errore nel segno del sommatore o nel punto di ingresso del disturbo.

_(Dispensa commentata, pagine PDF 100–100; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 100
> ![[CA-p100-1.jpg]]
> Una volta ridotto il processo, l'anello iniziale permette di fissare il guadagno e stimare il difetto dinamico ancora da compensare.

## Esercizi collegati

[[E02 - CA - Prova intermedia 2019-2020]]
