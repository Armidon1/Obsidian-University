---
title: "Moti relativi e forze apparenti"
aliases:
  - "F1 — Moti relativi e forze apparenti"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "88-105"
---

# Moti relativi e forze apparenti

> [!abstract]
> Una stessa traiettoria appare diversa a osservatori in moto relativo. Le trasformazioni cinematiche spiegano quali termini aggiungere quando il riferimento scelto accelera o ruota.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Trasformazioni galileiane

Vedi [[F1 - Trasformazioni galileiane]].

Se il riferimento mobile trasla con velocità costante $\mathbf V$, con assi paralleli, $\mathbf r=\mathbf R_0+\mathbf Vt+\mathbf r'$, $\mathbf v=\mathbf V+\mathbf v'$ e $\mathbf a=\mathbf a'$. Il tempo è comune nella meccanica galileiana. I riferimenti collegati da queste trasformazioni sono tutti inerziali se uno lo è. Le leggi di Newton mantengono la stessa forma, ma velocità, quantità di moto ed energia cinetica dipendono dall'osservatore.

_(Libro, cap. 3; pagine stampate 79–96; PDF pp. 88–105.)_

## Traslazione accelerata

Vedi [[F1 - Traslazione accelerata]].

Per assi che traslano senza ruotare, $\mathbf a=\mathbf a_O+\mathbf a'$. La dinamica mobile diventa
$$m\mathbf a'=\mathbf F_{\mathrm{reali}}-m\mathbf a_O.$$
Il termine $-m\mathbf a_O$ è una forza apparente dovuta alla scelta del riferimento. In un ascensore con accelerazione $a_O$ verso l'alto, una persona ferma rispetto alla cabina ha $N=m(g+a_O)$: la bilancia misura la reazione, non una variazione della massa.

_(Libro, cap. 3; pagine stampate 79–96; PDF pp. 88–105.)_

## Velocità e accelerazione in un riferimento rotante

Vedi [[F1 - Velocità e accelerazione in un riferimento rotante]].

Con origine mobile e velocità angolare $\boldsymbol\omega$,
$$\mathbf v=\mathbf v_O+\mathbf v'+\boldsymbol\omega\times\mathbf r',$$
$$\mathbf a=\mathbf a_O+\mathbf a'+\dot{\boldsymbol\omega}\times\mathbf r'+\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r')+2\boldsymbol\omega\times\mathbf v'.$$
Le derivate primate sono calcolate sugli assi mobili. Il termine con $\dot{\boldsymbol\omega}$ nasce dall'accelerazione angolare, il doppio prodotto dalla rotazione e l'ultimo dall'interazione tra moto relativo e rotazione.

_(Libro, cap. 3; pagine stampate 79–96; PDF pp. 88–105.)_

## Forza centrifuga e forza di Coriolis

Vedi [[F1 - Forza centrifuga e forza di Coriolis]].

Portando i termini di trascinamento a destra della seconda legge si introducono
$$\mathbf F_{\mathrm{cf}}=-m\boldsymbol\omega\times(\boldsymbol\omega\times\mathbf r'),\qquad\mathbf F_C=-2m\boldsymbol\omega\times\mathbf v'.$$
La centrifuga è diretta verso l'esterno rispetto all'asse; Coriolis esiste solo se c'è velocità relativa con componente perpendicolare all'asse. Per rotazione non uniforme si aggiunge la forza di Eulero $-m\dot{\boldsymbol\omega}\times\mathbf r'$. Una forza apparente non ha un partner di azione e reazione su un altro corpo: non è una nuova interazione fisica.

![[F1-p098-1.png]]

*Figura 3.11: il pendolo solidale alla piattaforma ruotante è descritto dall’osservatore inerziale con peso e tensione e da quello rotante aggiungendo la centrifuga. Nel riferimento mobile è fermo, quindi Coriolis è nulla.* _(Libro, p. 89; PDF p. 98.)_

_(Libro, cap. 3; pagine stampate 79–96; PDF pp. 88–105.)_

## Derivazione guidata

Per un vettore qualunque vale la regola di trasporto $(d\mathbf A/dt)_{\mathrm{inerziale}}=(d\mathbf A/dt)_{\mathrm{mobile}}+\boldsymbol\omega\times\mathbf A$. Applicala prima a $\mathbf r'$ per ottenere la velocità e poi alla velocità stessa. Due contributi uguali $\boldsymbol\omega\times\mathbf v'$ provengono da due derivazioni diverse: la loro somma spiega il fattore 2 dell'accelerazione di Coriolis. Cambiare riferimento non modifica le interazioni reali, ma modifica la relazione fra accelerazione misurata e risultante reale.

_(Libro, cap. 3; pagine stampate 79–96; PDF pp. 88–105.)_

## Esempio svolto

> [!example] Applicazione originale
> Su una piattaforma che ruota a $\omega=2\,\mathrm{rad/s}$, un oggetto fermo rispetto alla piattaforma a $r=0{,}50\,\mathrm m$ richiede un'accelerazione reale centripeta di $2{,}0\,\mathrm{m/s^2}$. Nel riferimento rotante la risultante reale verso l'asse è bilanciata dalla centrifuga; la forza di Coriolis è nulla perché $\mathbf v'=0$.

## Richiami matematici

[[09 - AN1 - Funzioni a Valori Vettoriali]] · [[GEO - Prodotto scalare geometrico]].

## Verifica attiva

Una particella si muove parallelamente all’asse di una piattaforma rotante: ha forza di Coriolis?

> [!check]- Risposta ragionata
> No, perché $\boldsymbol\omega\times\mathbf v’=0$. La presenza di rotazione da sola non basta a rendere non nullo questo termine.

## Navigazione

Precedente: [[02 - F1 - Dinamica del punto e leggi di Newton]] · Successivo: [[04 - F1 - Lavoro, energia e momento angolare]].
