---
title: "Retroazione dinamica dell’uscita e principio di separazione"
aliases:
  - "CA — Retroazione dinamica dell’uscita e principio di separazione"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "175-186"
class_label: "02/05"
---

# Retroazione dinamica dell’uscita e principio di separazione

> [!abstract]
> Questa lezione sviluppa retroazione dinamica dell’uscita e principio di separazione seguendo il blocco delle pagine 175–186 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 02/05. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[22 - CA - Osservatore asintotico e rilevabilità]]. **Dopo:** [[24 - CA - Inseguimento di riferimenti e modello interno]].

## Usare la stima al posto dello stato

Vedi [[CA - Controllore con osservatore]] · [[CA - Principio di separazione]].

Si realizza $u=K\hat x+v$ insieme all'osservatore. Il controllore ora ha una dinamica propria e usa soltanto ingresso di riferimento e uscita misurata. Con $e=x-\hat x$:
$$\begin{pmatrix}\dot x\\\dot e\end{pmatrix}=
\begin{pmatrix}A+BK&-BK\\0&A-LC\end{pmatrix}
\begin{pmatrix}x\\e\end{pmatrix}+\binom B0v.$$
La struttura triangolare dimostra il principio di separazione: i poli del complesso sono l'unione di quelli di $A+BK$ e di $A-LC$. I due progetti si possono svolgere separatamente nel caso LTI ideale.

La retroazione dinamica dell'uscita può stabilizzare il processo se e solo se esso è stabilizzabile e rilevabile. La completa raggiungibilità e osservabilità sono sufficienti per l'assegnazione arbitraria, ma più forti del necessario per la sola stabilizzazione.

_(Dispensa commentata, pagine PDF 175–177; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 175
> ![[CA-p175-1.jpg]]
> Il controllore dinamico usa lo stato stimato al posto di quello misurato e combina feedback e osservatore nello stesso schema.

> [!example]- Materiale originale — pagina PDF 176
> ![[CA-p176-1.jpg]]
> La classificazione dei sottospazi chiarisce quali modi impediscono il controllo dell'uscita: occorrono stabilizzabilità e rilevabilità.

> [!example]- Materiale originale — pagina PDF 177
> ![[CA-p177-1.jpg]]
> Il diagramma a insiemi riassume modi raggiungibili e osservabili, con i blocchi critici che devono essere già stabili se non modificabili.

## Realizzazione del controllore e FdT

Vedi [[CA - Realizzazione del compensatore dinamico]] · [[CA - Poli del controllore e poli chiusi]].

Per $v=0$ e $D=0$, sostituire $u=K\hat x$ nell'osservatore dà
$$\dot{\hat x}=(A+BK-LC)\hat x+Ly,\qquad u=K\hat x.$$
La FdT del controllore dalla misura al comando è $K[sI-(A+BK-LC)]^{-1}L$. Il segno globale dipende da come il sommatore esterno è disegnato; qui la misura entra positivamente nella correzione dell'osservatore.

I poli della realizzazione isolata del controllore sono gli autovalori di $A+BK-LC$, non l'unione dei poli scelti separatamente. Quest'ultima descrive il **complesso processo-controllore** nelle coordinate $(x,e)$. Un controllore può non essere AS da solo e stabilizzare comunque l'interconnessione nominale; la stabilità interna si verifica sul complesso.

Il controllore di ordine $n$ costruito con un osservatore completo è una soluzione sistematica, ma non è necessariamente di ordine minimo. Eventuali riduzioni devono preservare la stabilità interna e i canali effettivamente richiesti.

_(Dispensa commentata, pagine PDF 178–181; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 178
> ![[CA-p178-1.jpg]]
> La realizzazione del compensatore sostituisce il comando nella dinamica dell'osservatore; i poli del controllore isolato vanno distinti da quelli del complesso.

> [!example]- Materiale originale — pagina PDF 179
> ![[CA-p179-1.jpg]]
> Il progetto numerico verifica il guadagno di stato, quello di stima e la funzione del controllore dall'uscita al comando.

> [!example]- Materiale originale — pagina PDF 180
> ![[CA-p180-1.jpg]]
> Le condizioni strutturali limitano l'assegnazione: un modo fisso può impedire una specifica di poli coincidenti anche se il sistema è stabilizzabile.

> [!example]- Materiale originale — pagina PDF 181
> ![[CA-p181-1.jpg]]
> Il confronto dei polinomi verifica quali poli sono liberamente scelti e quali devono essere mantenuti nella posizione originaria.

## Esercizi con parametri e modi fissi

Vedi [[CA - Controllo con parametri]] · [[CA - Criterio PBH parametrico]] · [[CA - Verifica del principio di separazione]].

Se il modello contiene un parametro, i ranghi possono cambiare per valori isolati. Si calcolano determinanti o minori e si analizzano separatamente i valori che li annullano. Per ciascun valore eccezionale occorre identificare il modo che diventa non raggiungibile o non osservabile e controllarne la parte reale.

> [!example] Parametro che spegne il controllo
> Con $A=\operatorname{diag}(1,-2)$, $B=(a,1)^T$, la matrice di raggiungibilità ha determinante $-3a$. Per $a\ne0$ i poli sono assegnabili; per $a=0$ il modo $+1$ è non raggiungibile, quindi la stabilizzazione è impossibile. Non basta scrivere «rango non pieno»: occorre verificare quale modo rimane fisso.

Negli esercizi finali si scrivono esplicitamente $K,L$, le matrici del controllore e i due polinomi desiderati. Il controllo a blocchi triangolari costituisce una verifica indipendente dei calcoli in coordinate originali.

_(Dispensa commentata, pagine PDF 182–186; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 182
> ![[CA-p182-1.jpg]]
> Il foglio supplementare ricostruisce la matrice del controllore e la struttura triangolare dell'interconnessione nelle coordinate dell'errore.

> [!example]- Materiale originale — pagina PDF 183
> ![[CA-p183-1.jpg]]
> Gli esempi con parametri individuano i valori in cui il rango di raggiungibilità o osservabilità cambia.

> [!example]- Materiale originale — pagina PDF 184
> ![[CA-p184-1.jpg]]
> Il calcolo delle basi permette di identificare il modo che diventa fisso e di valutarne la stabilità.

> [!example]- Materiale originale — pagina PDF 185
> ![[CA-p185-1.jpg]]
> Il progetto del feedback viene verificato sul modello originale prima di aggiungere la stima dello stato.

> [!example]- Materiale originale — pagina PDF 186
> ![[CA-p186-1.jpg]]
> Il calcolo dell'osservatore conclude l'esempio e controlla separatamente il polinomio della dinamica di stima.

## Esercizi collegati

[[E08 - CA - Prova finale 2018-2019]] · [[E09 - CA - Prova finale 2019-2020]] · [[E10 - CA - Prova finale 2020-2021]] · [[E12 - CA - Prova finale 2022-2023]] · [[E13 - CA - Prova finale 2023-2024 e assegnazione canonica]] · [[E14 - CA - Prova completa del 12 luglio 2019]] · [[E15 - CA - Dimostrazioni e verifiche supplementari]]
