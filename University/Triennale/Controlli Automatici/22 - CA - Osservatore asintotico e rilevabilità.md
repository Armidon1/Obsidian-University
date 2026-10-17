---
title: "Osservatore asintotico e rilevabilità"
aliases:
  - "CA — Osservatore asintotico e rilevabilità"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "167-174"
class_label: "28/04"
---

# Osservatore asintotico e rilevabilità

> [!abstract]
> Questa lezione sviluppa osservatore asintotico e rilevabilità seguendo il blocco delle pagine 167–174 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 28/04. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[21 - CA - Retroazione dello stato e assegnazione degli autovalori]]. **Dopo:** [[23 - CA - Retroazione dinamica dell’uscita e principio di separazione]].

## Stimare lo stato da ingresso e uscita

Vedi [[CA - Osservatore di Luenberger]] · [[CA - Errore di stima]].

Quando lo stato non è misurabile, lo si ricostruisce attraverso un modello alimentato con lo stesso ingresso del processo e corretto dall'errore di uscita. Con $D=0$:
$$\dot{\hat x}=A\hat x+Bu+L(y-C\hat x).$$
Per $e=x-\hat x$, sottraendo le due equazioni si ottiene
$$\dot e=(A-LC)e.$$
Il termine $Bu$ si cancella perché l'osservatore conosce l'ingresso effettivamente applicato. Se un disturbo ignoto entra nel processo, il suo effetto sull'errore non si cancella automaticamente.

L'osservatore è asintotico se $A-LC$ è Hurwitz: la stima converge al vero stato per qualsiasi errore iniziale. Non ricostruisce istantaneamente lo stato e non richiede di conoscere $x(0)$.

_(Dispensa commentata, pagine PDF 167–168; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 167
> ![[CA-p167-1.jpg]]
> L'osservatore nasce dalla necessità di ricostruire lo stato usando ingresso noto e uscita misurata, senza conoscere la condizione iniziale.

> [!example]- Materiale originale — pagina PDF 168
> ![[CA-p168-1.jpg]]
> La sottrazione delle equazioni produce la dinamica autonoma dell'errore: il guadagno di correzione agisce tramite LC.

## Dualità e progetto del guadagno

Vedi [[CA - Dualità controllo osservazione]] · [[CA - Rilevabilità]] · [[CA - Test PBH di osservazione]].

Se $(A,C)$ è completamente osservabile, gli autovalori di $A-LC$ si assegnano arbitrariamente. Il problema è duale a quello della retroazione dello stato: si progetta per $(A^T,C^T)$ e si traspone il risultato, controllando il segno della correzione.

Se l'osservabilità non è completa, i modi non osservabili restano fissi. Un osservatore asintotico esiste se e solo se tutti questi modi sono strettamente stabili: il sistema è rilevabile (detectable). Il test è
$$\operatorname{rank}\begin{bmatrix}\lambda I-A\\C\end{bmatrix}=n\qquad\forall\Re\lambda\ge0.$$
Una modalità non osservabile stabile non deve essere identificata esattamente all'istante iniziale: il suo contributo all'errore si esaurisce da solo. Una modalità non osservabile instabile rende invece impossibile la convergenza per ogni stato iniziale.

_(Dispensa commentata, pagine PDF 169–171; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 169
> ![[CA-p169-1.jpg]]
> La forma A meno LC mostra il progetto dei poli di stima e la dualità con la retroazione del sistema trasposto.

> [!example]- Materiale originale — pagina PDF 170
> ![[CA-p170-1.jpg]]
> Lo schema esplicita l'innovazione di uscita e un primo esercizio determina il guadagno tramite la forma canonica.

> [!example]- Materiale originale — pagina PDF 171
> ![[CA-p171-1.jpg]]
> La discussione dei modi nascosti introduce rilevabilità: quelli non osservabili devono essere già stabili per consentire convergenza.

## Esercizio e scelta della velocità di stima

Vedi [[CA - Velocità dell’osservatore]] · [[CA - Rumore e osservatore]].

> [!example] Guadagno verificato
> Per $A=\begin{pmatrix}0&1\\-2&-3\end{pmatrix}$, $C=(1,0)$ e $L=(l_1,l_2)^T$, il polinomio di $A-LC$ è $s^2+(3+l_1)s+(3l_1+2+l_2)$. Volendo poli $-8,-9$, si impongono $3+l_1=17$ e $3l_1+2+l_2=72$: risulta $L=(14,28)^T$.

Poli dell'osservatore più veloci di quelli del controllo riducono il tempo in cui l'errore di stima influenza il comando. Non vanno però spinti arbitrariamente a sinistra: un guadagno $L$ elevato amplifica il rumore, può introdurre picchi transitori e peggiora la sensibilità alle dinamiche non modellate.

Gli esercizi della dispensa includono la scomposizione osservabile: in quel caso si assegnano soltanto i poli del blocco osservabile e si controllano quelli fissi. Vedi [[TDS - Osservatore asintotico]] e [[TDS - Principio di separazione]].

_(Dispensa commentata, pagine PDF 172–174; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 172
> ![[CA-p172-1.jpg]]
> La decomposizione osservabile limita i poli di stima assegnabili e conserva il blocco invisibile alle misure.

> [!example]- Materiale originale — pagina PDF 173
> ![[CA-p173-1.jpg]]
> L'esercizio calcola una trasformazione e il guadagno dell'osservatore verificando l'ordine delle matrici e delle trasposte.

> [!example]- Materiale originale — pagina PDF 174
> ![[CA-p174-1.jpg]]
> La conclusione controlla i poli dell'errore nelle coordinate originali e richiama il compromesso fra velocità di stima e rumore.

## Esercizi collegati

[[E08 - CA - Prova finale 2018-2019]] · [[E09 - CA - Prova finale 2019-2020]] · [[E10 - CA - Prova finale 2020-2021]] · [[E11 - CA - Prova finale 2021-2022]] · [[E12 - CA - Prova finale 2022-2023]] · [[E13 - CA - Prova finale 2023-2024 e assegnazione canonica]] · [[E15 - CA - Dimostrazioni e verifiche supplementari]]
