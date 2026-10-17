---
title: "Assegnazione diretta dei poli con retroazione dinamica"
aliases:
  - "CA — Assegnazione diretta dei poli con retroazione dinamica"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "135-140"
class_label: "11/04"
---

# Assegnazione diretta dei poli con retroazione dinamica

> [!abstract]
> Questa lezione sviluppa assegnazione diretta dei poli con retroazione dinamica seguendo il blocco delle pagine 135–140 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 11/04. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[17 - CA - Poli dominanti e vincoli sul transitorio]]. **Dopo:** [[19 - CA - Esercizi riepilogativi su controllo classico]].

## Equazione diofantea per il controllore

Vedi [[CA - Assegnazione polinomiale]] · [[CA - Equazione diofantea]].

Sia $P=N_P/D_P$ e $G=N_G/D_G$. Il denominatore chiuso non ridotto è
$$\chi(s)=D_P(s)D_G(s)+N_P(s)N_G(s).$$
Assegnare i poli significa imporre $\chi=\chi_d$ e risolvere per i coefficienti incogniti di $N_G,D_G$. È un'equazione polinomiale lineare nei coefficienti del controllore quando i gradi sono fissati. I coefficienti di $\chi_d$ si scelgono dai poli desiderati e dai vincoli di ordine.

L'assenza di fattori comuni tra $N_P,D_P$ è essenziale per la libertà di assegnazione esterna; eventuali modi interni non rappresentati dal processo ridotto vanno comunque controllati. Un numero insufficiente di coefficienti incogniti può rendere il sistema senza soluzione.

Non si può confrontare una FdT chiusa semplificata con $\chi_d$ e concludere che tutti i modi siano stati assegnati: si confronta il polinomio dell'interconnessione.

_(Dispensa commentata, pagine PDF 135–137; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 135
> ![[CA-p135-1.jpg]]
> L'assegnazione diretta impone il polinomio chiuso tramite numeratore e denominatore del controllore, con gradi fissati in anticipo.

> [!example]- Materiale originale — pagina PDF 136
> ![[CA-p136-1.jpg]]
> Il confronto dei coefficienti trasforma il progetto in un sistema algebrico nelle incognite del controllore.

> [!example]- Materiale originale — pagina PDF 137
> ![[CA-p137-1.jpg]]
> L'esempio costruisce il denominatore desiderato e controlla la compatibilità dei coefficienti con ordine e struttura scelti.

## Ordine del controllore e verifica della soluzione

Vedi [[CA - Grado del controllore]] · [[CA - Causalità]] · [[CA - Verifica della realizzazione]].

Si sceglie un grado che renda risolvibile il confronto dei coefficienti e mantenga $\deg N_G\le\deg D_G$. Un controllore non proprio richiede derivate ideali del segnale: l'aggiunta successiva di un filtro cambia il polinomio e richiede una nuova verifica.

> [!example] PI e assegnazione di un secondo ordine
> Per $P=1/(s+1)$ e $G=(as+b)/s$, $\chi=s(s+1)+as+b=s^2+(1+a)s+b$. Volendo $(s+2)(s+3)=s^2+5s+6$, si ottiene $a=4,b=6$, cioè $G=4+6/s$. L'anello è AS, di tipo 1, ed elimina l'errore al gradino.

Il confronto dei coefficienti dà una soluzione algebrica; completare sempre il lavoro con schema dei segnali, stabilità interna e controllo delle specifiche di precisione. Le pagine finali confrontano assegnazione diretta e LdR: il secondo è molto intuitivo con un solo parametro, la prima sfrutta più parametri per imporre un polinomio desiderato.

_(Dispensa commentata, pagine PDF 138–140; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 138
> ![[CA-p138-1.jpg]]
> La realizzazione del controllore viene confrontata con il polinomio dell'interconnessione, per non perdere i modi eventualmente nascosti.

> [!example]- Materiale originale — pagina PDF 139
> ![[CA-p139-1.jpg]]
> L'esercizio seguente mostra come usare i parametri liberi per assegnare i poli e soddisfare le condizioni statiche.

> [!example]- Materiale originale — pagina PDF 140
> ![[CA-p140-1.jpg]]
> La tabella riassuntiva confronta luogo e assegnazione polinomiale: il primo segue un parametro, la seconda sfrutta più coefficienti.

## Esercizi collegati

[[E02 - CA - Prova intermedia 2019-2020]] · [[E03 - CA - Prova intermedia 2020-2021]] · [[E04 - CA - Prova intermedia 2021-2022]] · [[E05 - CA - Prova intermedia 2022-2023]] · [[E06 - CA - Prova intermedia 2023-2024]] · [[E07 - CA - Prova intermedia 2024-2025]] · [[E14 - CA - Prova completa del 12 luglio 2019]]
