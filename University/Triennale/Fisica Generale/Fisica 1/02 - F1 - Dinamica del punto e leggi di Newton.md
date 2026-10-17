---
title: "Dinamica del punto e leggi di Newton"
aliases:
  - "F1 — Dinamica del punto e leggi di Newton"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "48-87"
---

# Dinamica del punto e leggi di Newton

> [!abstract]
> Le forze spiegano la variazione del moto. Si sceglie un sistema, si individuano le interazioni con gli altri corpi e si traduce il bilancio vettoriale in equazioni differenziali.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Leggi di Newton e riferimento inerziale

Vedi [[F1 - Leggi di Newton e riferimento inerziale]].

In un riferimento inerziale un punto isolato mantiene la velocità costante. Per massa costante la seconda legge è
$$\sum_i\mathbf F_i=m\mathbf a.$$
La massa misura l'inerzia, la forza si misura in newton: $1\,\mathrm N=1\,\mathrm{kg\,m/s^2}$. La terza legge riguarda due corpi diversi: $\mathbf F_{A\to B}=-\mathbf F_{B\to A}$. Per questo azione e reazione non si cancellano nel diagramma delle forze di un solo corpo.

Disegnare prima il corpo isolato, poi scegliere gli assi e proiettare. La forza centripeta è il nome della **risultante radiale** necessaria al moto curvo, non una nuova interazione da aggiungere al peso o alla tensione.

_(Libro, cap. 2; pagine stampate 39–78; PDF pp. 48–87.)_

## Quantità di moto, impulso ed equilibrio

Vedi [[F1 - Quantità di moto, impulso ed equilibrio]].

Con $\mathbf p=m\mathbf v$, per un sistema materiale chiuso vale $\dot{\mathbf p}=\mathbf F_{\mathrm{ext}}$ e
$$\mathbf J=\int_{t_1}^{t_2}\mathbf F_{\mathrm{ext}}dt=\Delta\mathbf p.$$
L'impulso è utile quando la durata dell'interazione è breve e la forza istantanea non è nota. Risultante nulla implica velocità costante; la quiete richiede anche velocità iniziale nulla. Un oggetto che gira a rapidità costante ha invece risultante radiale non nulla.

> [!warning] Sistema a massa variabile
> Se entra o esce materia, occorre includere il flusso di quantità di moto. Non si applica automaticamente $\mathbf F=d(m\mathbf v)/dt$ alla sola massa rimasta nel sistema aperto.

_(Libro, cap. 2; pagine stampate 39–78; PDF pp. 48–87.)_

> [!warning] Correzione — moto circolare uniforme
> Il § 2.6 del libro (p. 47 stampata, PDF p. 56) descrive questo caso con le parole «moto uniforme e non accelerato». L'espressione è imprecisa se riferita al vettore accelerazione: nel moto circolare uniforme è nulla solo l'accelerazione tangenziale, mentre $a_n=v^2/R$ è non nulla. In questa nota "uniforme" indica rapidità costante; "accelerazione nulla" indica invece velocità vettoriale costante.

## Peso, vincoli, attrito e fili

Vedi [[F1 - Peso, vincoli, attrito e fili]].

Vicino alla superficie terrestre $\mathbf P=m\mathbf g$. La reazione normale $N$ va ricavata dalla proiezione della seconda legge; non è sempre uguale a $mg$. Un filo ideale, inestensibile e di massa trascurabile, impone un vincolo cinematico e trasmette tensione, diretta lungo il filo.

L'attrito statico si adatta alla necessità: $|F_s|\le\mu_sN$. Solo al limite di scorrimento vale l'uguaglianza. Nel modello di attrito dinamico $|F_d|=\mu_dN$, opposto allo scorrimento relativo. Sul piano inclinato le componenti del peso sono $mg\sin\theta$ lungo il piano e $mg\cos\theta$ normalmente; senza altre forze normali $N=mg\cos\theta$.

![[F1-p060-1.png]]

*Figura 2.15: sul blocco agiscono peso, normale, forza applicata e attrito statico. In quiete l’attrito bilancia la forza tangenziale solo finché la sua intensità non supera il valore massimo consentito.* _(Libro, p. 51; PDF p. 60.)_

_(Libro, cap. 2; pagine stampate 39–78; PDF pp. 48–87.)_

## Forza viscosa e velocità limite

Vedi [[F1 - Forza viscosa e velocità limite]].

Per piccole velocità si può modellare la resistenza come $\mathbf F_v=-b\mathbf v$. In caduta, scegliendo il verso positivo verso il basso,
$$m\dot v=mg-bv,\qquad v(t)=\frac{mg}{b}+\left(v_0-\frac{mg}{b}\right)e^{-bt/m}.$$
La velocità limite $mg/b$ si raggiunge asintoticamente; il tempo caratteristico è $m/b$. Il modello lineare non descrive ogni regime: a velocità maggiori può servire una dipendenza quadratica dalla rapidità.

_(Libro, cap. 2; pagine stampate 39–78; PDF pp. 48–87.)_

## Oscillatori e pendolo

Vedi [[F1 - Oscillatori e pendolo]].

Una molla ideale esercita $F=-kx$, perciò $\ddot x+\omega_0^2x=0$, $\omega_0=\sqrt{k/m}$. Con smorzamento viscoso e forzante:
$$m\ddot x+b\dot x+kx=F_0\cos\Omega t.$$
Nel caso sottosmorzato l'ampiezza libera decade come $e^{-bt/(2m)}$; a regime la risposta ha ampiezza
$$A(\Omega)=\frac{F_0}{\sqrt{(k-m\Omega^2)^2+b^2\Omega^2}}.$$
Il massimo dell'ampiezza di spostamento non coincide sempre con $\omega_0$. Per il pendolo $\ddot\theta+(g/\ell)\sin\theta=0$; solo per piccoli angoli $\sin\theta\simeq\theta$ e $T\simeq2\pi\sqrt{\ell/g}$.

_(Libro, cap. 2; pagine stampate 39–78; PDF pp. 48–87.)_

## Derivazione guidata

Per risolvere $m\ddot x+kx=0$ poni $x=A\cos(\omega t+\varphi)$: sostituendo ottieni $(k-m\omega^2)x=0$, dunque $\omega=\sqrt{k/m}$. Una forma che incorpora direttamente i dati iniziali è $x(t)=x_0\cos\omega t+(v_0/\omega)\sin\omega t$. Le condizioni iniziali non cambiano la frequenza propria del modello lineare, ma ne fissano ampiezza e fase. Per il pendolo la linearità nasce invece dall'approssimazione $\sin\theta\simeq\theta$.

_(Libro, cap. 2; pagine stampate 39–78; PDF pp. 48–87.)_

## Esempio svolto

> [!example] Applicazione originale
> Un blocco scivola su un piano a $30^\circ$ con $\mu_d=0{,}20$. Lungo il piano $ma=mg\sin\theta-\mu_dmg\cos\theta$, quindi $a=3{,}21\,\mathrm{m/s^2}$ verso il basso. Per stabilire se parte da fermo serve invece $\mu_s$: la soglia è $\tan\theta>\mu_s$.

## Richiami matematici

[[GEO - Somma e differenza di vettori]] · [[05 - AN1 - Calcolo Differenziale]].

## Verifica attiva

Un blocco fermo su un piano orizzontale riceve 3 N orizzontali, con attrito statico massimo di 5 N. Quanto vale l’attrito?

> [!check]- Risposta ragionata
> Vale 3 N, opposto alla forza applicata, se non ci sono altre forze tangenziali. Il massimo di 5 N non è un valore da usare sempre.

## Navigazione

Precedente: [[01 - F1 - Cinematica del punto]] · Successivo: [[03 - F1 - Moti relativi e forze apparenti]].
