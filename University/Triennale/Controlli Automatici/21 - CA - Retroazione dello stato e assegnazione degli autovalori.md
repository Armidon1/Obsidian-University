---
title: "Retroazione dello stato e assegnazione degli autovalori"
aliases:
  - "CA — Retroazione dello stato e assegnazione degli autovalori"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "156-166"
class_label: "27/04"
---

# Retroazione dello stato e assegnazione degli autovalori

> [!abstract]
> Questa lezione sviluppa retroazione dello stato e assegnazione degli autovalori seguendo il blocco delle pagine 156–166 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 27/04. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[20 - CA - Raggiungibilità osservabilità e forme canoniche]]. **Dopo:** [[22 - CA - Osservatore asintotico e rilevabilità]].

## Modificare la dinamica con lo stato misurato

Vedi [[CA - Retroazione dello stato]] · [[CA - Assegnazione degli autovalori]].

Se tutte le componenti di $x$ sono disponibili, si applica $u=Kx+v$. La dinamica chiusa è $\dot x=(A+BK)x+Bv$. Alcuni testi usano $u=-Kx+v$: qui il segno è positivo, coerente con le pagine della dispensa. Le formule dei coefficienti cambiano segno se cambia la convenzione.

Il teorema di assegnazione afferma che tutti gli autovalori di $A+BK$ possono essere scelti arbitrariamente se e solo se $(A,B)$ è completamente raggiungibile. Per matrici reali i poli non reali devono essere scelti in coppie coniugate. La raggiungibilità consente l'assegnazione, non garantisce automaticamente un basso sforzo di controllo.

In forma compagna con $B_c=e_n$, volendo $\chi_d=s^n+\beta_{n-1}s^{n-1}+\cdots+\beta_0$, basta
$$K_c=(a_0-\beta_0,\ldots,a_{n-1}-\beta_{n-1}).$$
Se $z=Tx$, il guadagno originale è $K=K_cT$. Vedi [[TDS - Retroazione dallo stato]] e [[TDS - Formula di Ackermann]].

_(Dispensa commentata, pagine PDF 156–160; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 156
> ![[CA-p156-1.jpg]]
> La retroazione dello stato modifica la matrice A attraverso BK: il comando dipende da tutte le componenti disponibili dello stato.

> [!example]- Materiale originale — pagina PDF 157
> ![[CA-p157-1.jpg]]
> La separazione fra variazione del riferimento e feedback distingue il progetto della dinamica da quello del guadagno ingresso-uscita.

> [!example]- Materiale originale — pagina PDF 158
> ![[CA-p158-1.jpg]]
> Il teorema di assegnazione collega raggiungibilità completa e scelta arbitraria dei poli; i blocchi non raggiungibili rimangono fissi.

> [!example]- Materiale originale — pagina PDF 159
> ![[CA-p159-1.jpg]]
> Il progetto in forma canonica impone i coefficienti desiderati e riporta poi il guadagno alle coordinate originali.

> [!example]- Materiale originale — pagina PDF 160
> ![[CA-p160-1.jpg]]
> L'esempio calcola i coefficienti del guadagno e controlla il polinomio caratteristico effettivamente ottenuto.

## Modi fissi stabilizzabilità e test PBH

Vedi [[CA - Stabilizzabilità]] · [[CA - Test PBH di controllo]].

Se il sistema non è completamente raggiungibile, il feedback sposta soltanto i modi raggiungibili. È comunque possibile stabilizzarlo se tutti i modi non raggiungibili sono già strettamente stabili. Questa proprietà si chiama stabilizzabilità.

Il test PBH la esprime come
$$\operatorname{rank}[\lambda I-A\ \ B]=n\qquad\forall\lambda:\Re\lambda\ge0.$$
Per la raggiungibilità il test deve valere su ogni autovalore; per la stabilizzabilità basta sui modi instabili o marginali. Un modo nullo non raggiungibile impedisce l'AS esattamente come un modo a parte reale positiva.

> [!example] Stabilizzabile ma non raggiungibile
> $A=\operatorname{diag}(1,-2)$, $B=(1,0)^T$. Con $K=(-4,0)$, $A+BK=\operatorname{diag}(-3,-2)$: il modo non raggiungibile resta $-2$ e il sistema è AS. Se il secondo modo fosse $+2$, nessun $K$ lo stabilizzerebbe.

_(Dispensa commentata, pagine PDF 161–163; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 161
> ![[CA-p161-1.jpg]]
> Le osservazioni confrontano controllabilità completa e stabilizzabilità: un modo non raggiungibile è accettabile solo se già strettamente stabile.

> [!example]- Materiale originale — pagina PDF 162
> ![[CA-p162-1.jpg]]
> La decomposizione separa il sottospazio raggiungibile e rende espliciti i modi che il feedback non può spostare.

> [!example]- Materiale originale — pagina PDF 163
> ![[CA-p163-1.jpg]]
> L'esercizio su un sistema non completamente raggiungibile assegna soltanto i poli mobili e conserva quelli fissi.

## Esempi di assegnazione e verifica

Vedi [[CA - Confronto dei coefficienti nello stato]] · [[CA - Guadagno nelle coordinate originali]].

Per ordini piccoli si può calcolare direttamente $\det(sI-A-BK)$ e confrontarlo con il polinomio desiderato. Questo evita errori di convenzione e fornisce un controllo indipendente della trasformazione canonica.

> [!example] Assegnare una coppia reale
> $A=\begin{pmatrix}0&1\\-2&-3\end{pmatrix}$, $B=(0,1)^T$. Per poli $-4,-5$, $\chi_d=s^2+9s+20$. Poiché $A+BK$ ha ultima riga $(-2+k_1,-3+k_2)$, si ottiene $k_1=-18,k_2=-6$. Verifica: $A+BK=\begin{pmatrix}0&1\\-20&-9\end{pmatrix}$.

Si deve infine specificare il comando $u=Kx+v$, le dimensioni delle matrici e il polinomio chiuso. Se lo stato non è misurato, questa legge non è ancora implementabile: occorrerà un osservatore, argomento della lezione successiva.

_(Dispensa commentata, pagine PDF 164–166; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 164
> ![[CA-p164-1.jpg]]
> Un nuovo esempio analizza come cambiano raggiungibilità e poli fissati al variare di un parametro.

> [!example]- Materiale originale — pagina PDF 165
> ![[CA-p165-1.jpg]]
> La verifica del polinomio chiuso conclude il caso parametrico e distingue valori ammissibili e degeneri.

> [!example]- Materiale originale — pagina PDF 166
> ![[CA-p166-1.jpg]]
> Il foglio supplementare ricostruisce il guadagno nelle coordinate iniziali e controlla matrici e radici dopo il progetto.

## Esercizi collegati

[[E08 - CA - Prova finale 2018-2019]] · [[E09 - CA - Prova finale 2019-2020]] · [[E10 - CA - Prova finale 2020-2021]] · [[E11 - CA - Prova finale 2021-2022]] · [[E12 - CA - Prova finale 2022-2023]] · [[E13 - CA - Prova finale 2023-2024 e assegnazione canonica]] · [[E15 - CA - Dimostrazioni e verifiche supplementari]]
