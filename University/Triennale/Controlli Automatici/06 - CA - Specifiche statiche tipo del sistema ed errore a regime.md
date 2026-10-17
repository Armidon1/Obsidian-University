---
title: "Specifiche statiche tipo del sistema ed errore a regime"
aliases:
  - "CA — Specifiche statiche tipo del sistema ed errore a regime"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "49-54"
class_label: "14/03"
---

# Specifiche statiche tipo del sistema ed errore a regime

> [!abstract]
> Questa lezione sviluppa specifiche statiche tipo del sistema ed errore a regime seguendo il blocco delle pagine 49–54 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 14/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[05 - CA - Introduzione al controllo e modelli fisici]]. **Dopo:** [[07 - CA - Disturbi rumore e astaticità]].

## Architettura e funzioni di sensibilità

Vedi [[CA - Funzione di anello]] · [[CA - Sensibilità]] · [[CA - Sensibilità complementare]].

Indichiamo con $P$ il processo, $G$ il controllore e $F=GP$ la FdT di anello. Nella retroazione unitaria definiamo
$$S=\frac1{1+F},\qquad T=\frac F{1+F},\qquad S+T=1.$$
Nelle dispense $W$ indica spesso il trasferimento chiuso di riferimento, qui $T$. Con disturbo $d_u$ sommato all'ingresso di $P$, disturbo $d_y$ sommato all'uscita e rumore $n$ sommato alla misura:
$$y=Tr+PSd_u+Sd_y-Tn.$$
Per sovrapposizione si studia un ingresso per volta. L'errore fisico $r-y$ e il segnale al comparatore $r-y-n$ coincidono soltanto se $n=0$.

Questa notazione rende esplicito il compromesso: a bassa frequenza vogliamo $S$ piccolo per precisione e rigetto dei disturbi; ad alta frequenza vogliamo $T$ piccolo per non trasferire il rumore di misura.

_(Dispensa commentata, pagine PDF 49–50; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 49
> ![[CA-p049-1.jpg]]
> Il sistema di controllo viene classificato attraverso stabilità, precisione, risposta ai disturbi e prestazioni transitorie.

> [!example]- Materiale originale — pagina PDF 50
> ![[CA-p050-1.jpg]]
> Le specifiche statiche vengono ricondotte ai trasferimenti del riferimento e dei disturbi: il tipo si riferisce alla funzione di anello.

## Tipo e costanti di errore

Vedi [[CA - Tipo del sistema]] · [[CA - Costanti di errore]].

Il tipo $\nu$ è il numero di poli nell'origine della funzione d'anello, dopo avere verificato che non si stanno nascondendo modi interni problematici. Se $F(s)\sim K_\nu/s^\nu$ per $s\to0$, l'errore di riferimento è $E=SR$.

| Tipo | Gradino unitario | Rampa unitaria | Parabola $t^2/2$ |
|---|---|---|---|
| 0 | $1/(1+K_p)$ | non limitato | non limitato |
| 1 | 0 | $1/K_v$ | non limitato |
| 2 | 0 | 0 | $1/K_a$ |

Qui $K_p=\lim F$, $K_v=\lim sF$, $K_a=\lim s^2F$. La tabella presuppone stabilità interna e applicabilità del valore finale; un integratore inserito in un anello instabile non garantisce alcuna precisione a regime.

> [!example] Dimensionare il guadagno statico
> Con $F=k/[s(s+2)]$, $K_v=k/2$ ed $e_{\infty,\text{rampa}}=2/k$. Per $e_\infty\le0.01$ serve $k\ge200$. Il polinomio $s^2+2s+k$ è AS per $k>0$, ma per $k=200$ lo smorzamento è soltanto $1/\sqrt{200}$: il vincolo statico da solo non dà un buon transitorio.

_(Dispensa commentata, pagine PDF 51–52; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 51
> ![[CA-p051-1.jpg]]
> La derivazione per ingressi polinomiali mostra come integratori e guadagno a bassa frequenza fissino il valore dell'errore.

> [!example]- Materiale originale — pagina PDF 52
> ![[CA-p052-1.jpg]]
> La tabella distingue gradino, rampa e parabola: conservare la normalizzazione dell'ingresso quando si usa la costante d'errore.

## Tradurre correttamente una specifica

Vedi [[CA - Specifiche di precisione]].

La frase «errore nullo per ogni riferimento costante» impone la struttura, cioè almeno un integratore nell'anello. La frase «errore sulla rampa non superiore a $\varepsilon$» impone poi un limite sul guadagno: $K_v\ge1/\varepsilon$ per rampa unitaria. Una rampa $at$ produce invece errore $a/K_v$.

Le schermate aggiunte nel manoscritto sono spiegazioni di supporto: i risultati da usare sono le equazioni del circuito e le ipotesi di stabilità. Per ogni esercizio scrivere sempre trasformata dell'ingresso, trasferimento verso l'errore e condizioni del valore finale, prima della sostituzione $s\to0$.

_(Dispensa commentata, pagine PDF 53–54; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 53
> ![[CA-p053-1.jpg]]
> Le osservazioni aggiunte discutono il numero di integratori e l'uso del valore finale: la stabilità chiusa è sempre una premessa.

> [!example]- Materiale originale — pagina PDF 54
> ![[CA-p054-1.jpg]]
> Le schermate di commento approfondiscono il significato delle specifiche; le condizioni operative restano quelle ricavate dalle equazioni del circuito.

## Esercizi collegati

[[E01 - CA - Prova intermedia 2018-2019]] · [[E03 - CA - Prova intermedia 2020-2021]] · [[E07 - CA - Prova intermedia 2024-2025]]
