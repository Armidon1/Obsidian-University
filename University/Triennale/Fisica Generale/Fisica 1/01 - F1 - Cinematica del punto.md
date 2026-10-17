---
title: "Cinematica del punto"
aliases:
  - "F1 — Cinematica del punto"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "12-47"
---

# Cinematica del punto

> [!abstract]
> Descrivere il moto significa assegnare una posizione a ogni istante, rispetto a un riferimento. La cinematica costruisce questa descrizione senza cercarne ancora le cause: le forze entreranno nel capitolo successivo.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Posizione, velocità e accelerazione

Vedi [[F1 - Posizione, velocità e accelerazione]].

Una traiettoria è l'insieme dei punti occupati; la legge oraria specifica anche **quando** vengono occupati. Con $\mathbf r(t)=(x(t),y(t),z(t))$ si definiscono
$$\mathbf v=\frac{d\mathbf r}{dt},\qquad \mathbf a=\frac{d\mathbf v}{dt}.$$
La velocità è tangente alla traiettoria; l'accelerazione può avere anche una componente normale. Le unità sono rispettivamente $\mathrm m$, $\mathrm{m/s}$ e $\mathrm{m/s^2}$. La velocità media è $\Delta\mathbf r/\Delta t$, mentre la rapidità media usa la lunghezza del percorso: su un giro chiuso la prima è nulla, la seconda no.

Per ricostruire il moto si integra due volte:
$$\mathbf v(t)=\mathbf v_0+\int_{t_0}^t\mathbf a(\tau)d\tau,\qquad\mathbf r(t)=\mathbf r_0+\int_{t_0}^t\mathbf v(\tau)d\tau.$$
Le condizioni iniziali fissano le costanti di integrazione.

_(Libro, cap. 1; pagine stampate 3–38; PDF pp. 12–47.)_

## Moto rettilineo e caduta verticale

Vedi [[F1 - Moto rettilineo e caduta verticale]].

A accelerazione costante, lungo un asse,
$$x=x_0+v_0t+\tfrac12at^2,\qquad v=v_0+at,\qquad v^2=v_0^2+2a(x-x_0).$$
Si è scelto $t_0=0$. L'ultima relazione elimina il tempo ed è utile per gli spazi di arresto. In caduta libera, con asse verso l'alto, $a=-g$ anche durante la salita: al punto più alto si annulla la velocità, **non** l'accelerazione. Il segno di $v$ determina il verso del moto; il prodotto $va$ determina se la rapidità cresce o diminuisce. L'approssimazione trascura l'aria e assume $g$ uniforme.

_(Libro, cap. 1; pagine stampate 3–38; PDF pp. 12–47.)_

## Moto armonico e accelerazione dipendente dalla posizione

Vedi [[F1 - Moto armonico e accelerazione dipendente dalla posizione]].

Il moto $x=A\cos(\omega t+\varphi)$ soddisfa $\ddot x=-\omega^2x$. La pulsazione $\omega$ si misura in $\mathrm{rad/s}$, il periodo è $T=2\pi/\omega$ e la frequenza $f=1/T$. Ampiezza e fase vengono dalle condizioni iniziali.

Se è nota $a(x)$, la regola della catena dà $a=v\,dv/dx$, quindi
$$v^2(x)-v_0^2=2\int_{x_0}^{x}a(\xi)d\xi.$$
Questa equazione fornisce la rapidità; per scegliere il segno della velocità serve sapere quale tratto della traiettoria si sta percorrendo.

_(Libro, cap. 1; pagine stampate 3–38; PDF pp. 12–47.)_

## Accelerazione tangenziale e normale

Vedi [[F1 - Accelerazione tangenziale e normale]].

Scrivendo $\mathbf v=v\hat{\mathbf t}$, con $v=|\mathbf v|$, la derivata agisce sia sul modulo sia sulla direzione:
$$\mathbf a=\dot v\hat{\mathbf t}+\frac{v^2}{\rho}\hat{\mathbf n}.$$
$\rho$ è il raggio locale di curvatura e $\hat{\mathbf n}$ punta verso il centro di curvatura. Nel moto circolare $\rho=R$, $v=R\omega$, $a_t=R\alpha$, $a_n=R\omega^2$. Un moto circolare uniforme ha accelerazione centripeta anche se la rapidità è costante. In forma vettoriale $\mathbf v=\boldsymbol\omega\times\mathbf r$ rispetto a un punto dell'asse.

![[F1-p032-1.png]]

*Figura 1.17: la base tangente-normale cambia orientazione lungo il percorso. La componente tangenziale cambia la rapidità, quella normale cambia la direzione; i componenti cartesiani sono le proiezioni dello stesso vettore.* _(Libro, p. 23; PDF p. 32.)_

_(Libro, cap. 1; pagine stampate 3–38; PDF pp. 12–47.)_

## Moto parabolico

Vedi [[F1 - Moto parabolico]].

Senza resistenza dell'aria si separano un moto orizzontale uniforme e uno verticale uniformemente accelerato:
$$x=v_0\cos\theta\,t,\qquad y=y_0+v_0\sin\theta\,t-\tfrac12gt^2.$$
Eliminare $t$ produce una parabola. Solo per arrivo alla stessa quota di partenza si hanno $t_v=2v_0\sin\theta/g$ e gittata $G=v_0^2\sin(2\theta)/g$. Se le quote differiscono, si risolve prima $y(t)=y_{\mathrm{arrivo}}$ scegliendo la radice fisica positiva.

_(Libro, cap. 1; pagine stampate 3–38; PDF pp. 12–47.)_

## Derivazione guidata

Parti da $\mathbf v=v\hat{\mathbf t}$. Derivando il prodotto si ha $\mathbf a=\dot v\hat{\mathbf t}+v\dot{\hat{\mathbf t}}$. La tangente ruota di $d\theta=ds/\rho$, quindi $\dot{\hat{\mathbf t}}=(v/\rho)\hat{\mathbf n}$. Si ritrova $a_n=v^2/\rho$. Il termine normale nasce dalla variazione della direzione: porre $\dot v=0$ elimina solo il termine tangenziale.

_(Libro, cap. 1; pagine stampate 3–38; PDF pp. 12–47.)_

## Esempio svolto

> [!example] Applicazione originale
> Un corpo parte da fermo e cade da $h=20\,\mathrm m$, con $g=9{,}81\,\mathrm{m/s^2}$. Dalla legge verticale $t=\sqrt{2h/g}=2{,}02\,\mathrm s$; il modulo della velocità di impatto è $gt=19{,}8\,\mathrm{m/s}$. Il risultato ha verso verso il basso, quindi componente negativa se l'asse è rivolto verso l'alto.

## Richiami matematici

[[05 - AN1 - Calcolo Differenziale]] · [[06 - AN1 - Calcolo Integrale]] · [[09 - AN1 - Funzioni a Valori Vettoriali]] · [[GEO - Riferimento cartesiano ortonormale]].

## Verifica attiva

Un’auto percorre una curva a rapidità costante: che cosa si annulla?

> [!check]- Risposta ragionata
> Si annulla l’accelerazione tangenziale; quella normale resta $v^2/ho$. La velocità vettoriale cambia direzione.

## Navigazione

Precedente: [[00 - F1 - Guida allo studio]] · Successivo: [[02 - F1 - Dinamica del punto e leggi di Newton]].
