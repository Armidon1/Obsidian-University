---
title: "Onde meccaniche"
aliases:
  - "F1 — Onde meccaniche"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "228-257"
---

# Onde meccaniche

> [!abstract]
> Un’onda trasporta una perturbazione attraverso un mezzo. I punti del mezzo oscillano localmente mentre la forma della perturbazione si propaga: velocità di oscillazione e velocità dell’onda sono grandezze diverse.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Onde progressive e armoniche

Vedi [[F1 - Onde progressive e armoniche]].

Una perturbazione $y(x,t)=f(x-vt)$ si propaga verso $+x$ senza cambiare forma; $f(x+vt)$ si propaga verso $-x$. Per un'onda armonica
$$y=A\cos(kx-\omega t+\varphi),\quad k=2\pi/\lambda,\quad\omega=2\pi f,\quad v=\omega/k=\lambda f.$$
La fase identifica i punti che oscillano nello stesso stato. Onde trasversali hanno spostamento perpendicolare alla propagazione; onde longitudinali parallelo. Un mezzo può essere dispersivo: allora la velocità di fase dipende dalla frequenza.

![[F1-p231-1.png]]

*Figura 9.7: istantanee successive mostrano lo spostamento della forma d’onda lungo la corda. I punti materiali oscillano trasversalmente: non percorrono con l’onda tutta la distanza di propagazione.* _(Libro, p. 222; PDF p. 231.)_

_(Libro, cap. 9; pagine stampate 219–248; PDF pp. 228–257.)_

## Equazione delle onde e corda tesa

Vedi [[F1 - Equazione delle onde e corda tesa]].

Per una corda ideale con tensione $\mathcal T$ uniforme, densità lineare $\mu$ e piccole pendenze,
$$\partial_t^2y=v^2\partial_x^2y,\qquad v=\sqrt{\mathcal T/\mu}.$$
La velocità trasversale del punto materiale è $\partial_ty$, mentre $v$ è la velocità della perturbazione. L'ipotesi di piccole deformazioni rende l'equazione lineare e consente la sovrapposizione delle soluzioni. Condizioni iniziali e condizioni ai bordi selezionano l'onda effettiva.

_(Libro, cap. 9; pagine stampate 219–248; PDF pp. 228–257.)_

## Energia, intensità e onde sonore

Vedi [[F1 - Energia, intensità e onde sonore]].

Una corda trasporta energia cinetica e potenziale elastica. Per un'onda armonica la potenza media è $\langle\mathcal P\rangle=\tfrac12\mu\omega^2A^2v$. L'intensità è potenza per area; per una sorgente puntiforme isotropa senza assorbimento $I=\mathcal P/(4\pi r^2)$. Nel suono la perturbazione è una variazione di pressione e densità. Il livello sonoro è $\beta=10\log_{10}(I/I_0)$ in decibel, con riferimento acustico usuale $I_0=10^{-12}\,\mathrm{W/m^2}$. Un raddoppio dell'intensità aumenta il livello di circa $3\,\mathrm{dB}$.

_(Libro, cap. 9; pagine stampate 219–248; PDF pp. 228–257.)_

## Effetto Doppler

Vedi [[F1 - Effetto Doppler]].

Per sorgente e osservatore che si muovono lungo la congiungente in un mezzo fermo,
$$f'=f\frac{v+v_O}{v-v_S},$$
se $v_O$ è positivo quando l'osservatore va verso la sorgente e $v_S$ quando la sorgente va verso l'osservatore. Le velocità vanno riferite al mezzo. Avvicinarsi aumenta la frequenza ricevuta. Questa formula classica per il suono non va trasferita alla luce, che richiede il Doppler relativistico.

_(Libro, cap. 9; pagine stampate 219–248; PDF pp. 228–257.)_

## Interferenza, onde stazionarie e battimenti

Vedi [[F1 - Interferenza, onde stazionarie e battimenti]].

Sovrapporre due onde coerenti richiede sommare gli spostamenti con le loro fasi. Due onde opposte di uguale ampiezza e frequenza producono $y=2A\sin(kx)\cos(\omega t)$, con nodi fissi. Per una corda fissata agli estremi $L=n\lambda/2$ e $f_n=nv/(2L)$. Nelle colonne d'aria i vincoli su pressione e spostamento sono diversi: un'estremità aperta è approssimativamente nodo di sovrapressione. Due frequenze vicine producono battimenti di frequenza $|f_1-f_2|$.

_(Libro, cap. 9; pagine stampate 219–248; PDF pp. 228–257.)_

## Onde sonore e onde d’urto

Vedi [[F1 - Onde sonore e onde d’urto]].

In un fluido la velocità del suono è $v=\sqrt{B/\rho}$, con modulo di comprimibilità adiabatico $B$; per un gas ideale $v=\sqrt{\gamma RT/M_{\mathrm{mol}}}$. Per un'onda piana armonica la sovrapressione di picco e lo spostamento di picco sono legati da $\Delta p_0=\rho v\omega A$, quindi $I=(\Delta p_0)^2/(2\rho v)$. Pressione e spostamento non hanno la stessa fase: la pressione è legata alla deformazione spaziale. Se una sorgente supera la velocità delle perturbazioni, i fronti si accumulano in un cono di Mach con $\sin\alpha=v/v_S$. La descrizione lineare del piccolo segnale non descrive completamente la struttura dissipativa di un'onda d'urto.

_(Libro, cap. 9; pagine stampate 219–248; PDF pp. 228–257.)_

## Derivazione guidata

Per una corda fissata a $x=0$ e $x=L$ cerca $y(x,t)=A\sin(kx)\cos(\omega t)$. Il primo vincolo è già soddisfatto; il secondo richiede $\sin(kL)=0$, cioè $k_n=n\pi/L$. Dalla dispersione $\omega=vk$ seguono $f_n=nv/(2L)$. Non sono ammesse tutte le frequenze: la selezione dei modi nasce dai bordi. Nel modo fondamentale ci sono due nodi agli estremi e un ventre al centro.

_(Libro, cap. 9; pagine stampate 219–248; PDF pp. 228–257.)_

## Esempio svolto

> [!example] Applicazione originale
> Una corda di $L=0{,}80\,\mathrm m$, tensione $80\,\mathrm N$ e densità lineare $0{,}005\,\mathrm{kg/m}$ ha $v=126{,}5\,\mathrm{m/s}$ e fondamentale $f_1=79{,}1\,\mathrm{Hz}$. Raddoppiare la tensione moltiplica le frequenze per $\sqrt2$, a lunghezza e densità invariate.

## Richiami matematici

[[09 - AN1 - Funzioni a Valori Vettoriali]] · [[11 - AN1 - Numeri Complessi]].

## Verifica attiva

Un ventre di un’onda stazionaria si sposta lungo la corda?

> [!check]- Risposta ragionata
> La posizione del ventre è fissa; il materiale lì oscilla con ampiezza massima. L’onda stazionaria ideale non coincide con un singolo profilo progressivo.

## Navigazione

Precedente: [[08 - F1 - Gravitazione]] · Successivo: [[10 - F1 - Proprietà meccaniche dei fluidi]].
