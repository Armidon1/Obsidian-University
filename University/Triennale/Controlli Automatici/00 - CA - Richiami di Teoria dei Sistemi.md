---
title: "Richiami di Teoria dei Sistemi"
aliases:
  - "CA — Richiami di Teoria dei Sistemi"
tags:
  - controlli-automatici
  - prerequisiti
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "2-9"
class_label: "Blocco in ordine di dispensa; data non assegnata"
---

# Richiami di Teoria dei Sistemi

> [!abstract]
> Richiami iniziali già presenti nella dispensa: consolidano i prerequisiti di Teoria dei Sistemi prima delle lezioni di Controlli Automatici. Percorso completo: [[MOC - Controlli Automatici]].

**Dopo:** [[01 - CA - Risposta armonica e diagrammi di Bode]].

## Modello di stato ed evoluzione

Vedi [[CA - Modello di stato]] · [[CA - Evoluzione libera e forzata]].

Il controllo automatico sceglie l'ingresso di un processo per ottenere un comportamento desiderato. Il punto di partenza è il modello lineare tempo invariante (LTI):
$$\dot x=Ax+Bu,\qquad y=Cx+Du.$$
Lo stato $x\in\mathbb R^n$ contiene la memoria del sistema; $u$ è la variabile che possiamo modificare e $y$ quella osservata. Il termine $D$ descrive una trasmissione istantanea. Non confondere l'ordine $n$ del modello con il numero di ingressi o uscite.

La soluzione separa memoria iniziale ed effetto dell'ingresso:
$$x(t)=e^{At}x(0)+\int_0^t e^{A(t-\tau)}Bu(\tau)\,d\tau.$$
Il primo termine è l'evoluzione libera, il secondo quella forzata. La retroazione modifica la dinamica, quindi non basta calcolare la sola risposta forzata a condizioni iniziali nulle. Richiami completi: [[TDS - Evoluzione libera e forzata]] e [[TDS - Esponenziale di matrice]].

_(Dispensa commentata, pagine PDF 2–4; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 2
> ![[CA-p002-1.jpg]]
> Lo schema a integratori collega le matrici A, B, C, D ai segnali: lo stato conserva la memoria della dinamica.

> [!example]- Materiale originale — pagina PDF 3
> ![[CA-p003-1.jpg]]
> La soluzione libera e quella forzata separano l'effetto delle condizioni iniziali da quello del comando; gli autovalori governano i modi liberi.

> [!example]- Materiale originale — pagina PDF 4
> ![[CA-p004-1.jpg]]
> I grafici temporali e le spirali mostrano come parte reale e immaginaria degli autovalori producano decadimento, crescita e oscillazioni.

## Modi e stabilità interna

Vedi [[CA - Stabilità interna]].

Un sistema è asintoticamente stabile (AS) se ogni evoluzione libera tende all'origine. Nel caso LTI finito ciò equivale ad avere $\Re\lambda_i(A)<0$ per tutti gli autovalori. Per la sola stabilità servono parti reali non positive e autovalori sull'asse immaginario semisemplici: un blocco di Jordan non banale genera fattori polinomiali che possono far crescere la soluzione.

> [!example] L'autovalore non basta nei casi marginali
> $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ ha autovalori nulli ma $e^{At}=I+At$: da $x(0)=(0,1)^T$ si ottiene $x_1(t)=t$. L'origine è instabile.

Il criterio di Routh conta radici nel semipiano destro senza calcolarle. Per $s^3+a_2s^2+a_1s+a_0$, con coefficienti reali e polinomio monico, la stabilità stretta richiede $a_2,a_1,a_0>0$ e $a_2a_1>a_0$. Vedi [[TDS - Criterio di Routh]]; per la struttura algebrica dei modi vedi [[GEO - Autovalori autovettori e autospazi]].

_(Dispensa commentata, pagine PDF 5–6; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 5
> ![[CA-p005-1.jpg]]
> La classificazione dei sistemi tramite gli autovalori distingue stabilità e AS; i disegni dei poli vanno letti insieme alla struttura di Jordan.

> [!example]- Materiale originale — pagina PDF 6
> ![[CA-p006-1.jpg]]
> Il richiamo di Routh permette di classificare le radici senza risolvere il polinomio; la risposta impulsiva introduce la descrizione esterna.

## Funzione di trasferimento e modi nascosti

Vedi [[CA - Funzione di trasferimento]] · [[CA - Cancellazioni pole-zero]].

Con condizioni iniziali nulle la trasformata di Laplace dà
$$W(s)=C(sI-A)^{-1}B+D,\qquad Y(s)=W(s)U(s).$$
La funzione di trasferimento (FdT) descrive il legame ingresso-uscita, non necessariamente tutti i modi interni. È propria se il grado del numeratore non supera quello del denominatore, strettamente propria se è inferiore. Una realizzazione minima è raggiungibile e osservabile: solo in tal caso i poli della FdT coincidono con tutti gli autovalori della dinamica interna.

Una cancellazione può nascondere un modo instabile. La stabilità BIBO (ingresso limitato → uscita limitata) della FdT ridotta non certifica automaticamente la stabilità interna della realizzazione fisica. Richiami: [[TDS - Funzione di trasferimento]], [[TDS - Realizzazione minima]], [[TDS - Raggiungibilità]], [[TDS - Osservabilità]].

_(Dispensa commentata, pagine PDF 7–8; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 7
> ![[CA-p007-1.jpg]]
> La formula della FdT collega modello di stato e trasformata di Laplace; i blocchi elementari chiariscono proprietà e stretta proprietà.

> [!example]- Materiale originale — pagina PDF 8
> ![[CA-p008-1.jpg]]
> I residui spiegano la decomposizione della risposta; poli visibili e autovalori coincidono soltanto con raggiungibilità e osservabilità complete.

## Regime permanente e ingressi canonici

Vedi [[CA - Teorema del valore finale]].

Per trovare un valore a regime si può usare
$$\lim_{t\to\infty}y(t)=\lim_{s\to0}sY(s),$$
solo se tutti i poli di $sY(s)$ hanno parte reale strettamente negativa. Non basta che il limite algebrico esista. Gradino, rampa e parabola normalizzata hanno trasformate $1/s$, $1/s^2$, $1/s^3$: il numero di integratori dell'anello determinerà l'errore di inseguimento.

Per l'ingresso sinusoidale di pulsazione $\omega$, un sistema AS ammette una risposta di regime sinusoidale con ampiezza moltiplicata per $|W(j\omega)|$ e fase traslata di $\arg W(j\omega)$. Questa osservazione apre la prima parte del corso. Vedi [[TDS - Regime permanente]] e [[TDS - Risposta armonica]].

_(Dispensa commentata, pagine PDF 9–9; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 9
> ![[CA-p009-1.jpg]]
> Il regime permanente è introdotto separando transitorio e risposta forzata; i limiti richiedono stabilità prima della loro applicazione.
