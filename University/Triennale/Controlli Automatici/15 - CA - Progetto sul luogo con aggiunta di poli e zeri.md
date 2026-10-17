---
title: "Progetto sul luogo con aggiunta di poli e zeri"
aliases:
  - "CA — Progetto sul luogo con aggiunta di poli e zeri"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "118-122"
class_label: "04/04"
---

# Progetto sul luogo con aggiunta di poli e zeri

> [!abstract]
> Questa lezione sviluppa progetto sul luogo con aggiunta di poli e zeri seguendo il blocco delle pagine 118–122 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 04/04. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[14 - CA - Punti multipli e costruzione del luogo delle radici]]. **Dopo:** [[16 - CA - Esercizi di sintesi sul luogo delle radici]].

## Struttura imposta dalle specifiche statiche

Vedi [[CA - Progetto sul luogo]] · [[CA - Integratori e luogo]].

Il luogo va costruito dopo avere soddisfatto la struttura statica. Se il processo non ha poli in origine e serve errore nullo al gradino, il controllore deve introdurre un integratore; se il processo ne ha già uno può bastare un guadagno, salvo le specifiche sui disturbi. Si studia dunque $F=kF_0$ con l'integratore già incluso in $F_0$.

Il grado relativo influenza gli asintoti e quindi i limiti geometrici del progetto. Aggiungere un integratore cambia sia il tipo sia il numero e la direzione dei rami all'infinito. Per questo una scelta motivata dalla precisione può rendere impossibile stabilizzare con il solo guadagno.

Il valore di $k$ deve appartenere all'intervallo AS e rispettare anche la costante di errore. Non basta trovare un punto stabile del luogo se il guadagno necessario viola il vincolo statico.

_(Dispensa commentata, pagine PDF 118–119; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 118
> ![[CA-p118-1.jpg]]
> Il progetto sul luogo parte dai requisiti statici: il numero di poli in origine scelto per l'errore cambia la geometria dei rami.

> [!example]- Materiale originale — pagina PDF 119
> ![[CA-p119-1.jpg]]
> Il grado relativo e il centro degli asintoti limitano le regioni raggiungibili variando il solo guadagno.

## Usare uno zero per modificare la geometria

Vedi [[CA - Zero del controllore]] · [[CA - Polo aggiuntivo del controllore]].

Uno zero aggiunto dal controllore cambia la condizione di fase e può attrarre i rami verso una zona utile. Un polo aggiuntivo consente di rendere proprio il controllore ma modifica nuovamente il luogo: va incluso nel progetto, anche se viene posto molto a sinistra.

> [!example] Un PI sul doppio integratore
> Con $P=1/s^2$ e $G=k(s+z)/s$, $\chi=s^3+ks+kz$: manca il termine in $s^2$, quindi non può essere Hurwitz per $k,z>0$. Aggiungere l'integratore senza verificare il polinomio non risolve il problema di controllo.

> [!example] Uno zero introduce smorzamento
> Con $P=1/[s(s+1)]$ e $G=k(s+z)$, $\chi=s^2+(1+k)s+kz$. Per $k,z>0$ è Hurwitz. Questo esempio serve a capire la geometria; il controllore derivativo non proprio va poi filtrato e il polo di filtro va verificato.

Quando si assegna una coppia desiderata $s_d,\bar s_d$, si calcola prima il difetto di fase del processo e si sceglie il polo/zero del controllore per compensarlo. Il modulo determina il guadagno solo dopo che la fase è soddisfatta.

_(Dispensa commentata, pagine PDF 120–122; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 120
> ![[CA-p120-1.jpg]]
> L'aggiunta di uno zero del controllore modifica la fase e può attrarre i rami verso il semipiano stabile.

> [!example]- Materiale originale — pagina PDF 121
> ![[CA-p121-1.jpg]]
> L'esercizio calcola il polinomio e verifica con Routh se il nuovo luogo contiene un intervallo utile.

> [!example]- Materiale originale — pagina PDF 122
> ![[CA-p122-1.jpg]]
> La soluzione completa richiede il controllo del guadagno e della struttura, inclusi i poli aggiunti per la realizzabilità.

## Esercizi collegati

[[E01 - CA - Prova intermedia 2018-2019]]
