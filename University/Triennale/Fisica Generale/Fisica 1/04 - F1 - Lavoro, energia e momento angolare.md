---
title: "Lavoro, energia e momento angolare"
aliases:
  - "F1 — Lavoro, energia e momento angolare"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "106-127"
---

# Lavoro, energia e momento angolare

> [!abstract]
> La dinamica può essere integrata lungo uno spostamento o rispetto al tempo. Lavoro ed energia permettono di ricavare velocità senza conoscere tutta la legge oraria; i momenti descrivono gli effetti rotazionali.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Lavoro, potenza ed energia cinetica

Vedi [[F1 - Lavoro, potenza ed energia cinetica]].

Il lavoro lungo il percorso $\gamma$ è $W=\int_\gamma\mathbf F\cdot d\mathbf r$; dipende dalla componente tangenziale della forza. Da $\mathbf F=m\dot{\mathbf v}$ e $d\mathbf r=\mathbf vdt$ segue
$$W_{\mathrm{tot}}=\Delta K,\qquad K=\tfrac12mv^2.$$
La potenza istantanea è $\mathcal P=dW/dt=\mathbf F\cdot\mathbf v$. Lavoro ed energia si misurano in joule, la potenza in watt. Una forza perpendicolare alla velocità devia il moto ma non cambia l'energia cinetica.

_(Libro, cap. 4; pagine stampate 97–118; PDF pp. 106–127.)_

## Forze conservative ed energia potenziale

Vedi [[F1 - Forze conservative ed energia potenziale]].

Una forza è conservativa se il lavoro tra due punti non dipende dal percorso, equivalentemente se ogni circuitazione è nulla. Si introduce $U$ mediante
$$W_{A\to B}=U(A)-U(B),\qquad\mathbf F=-\nabla U.$$
In una dimensione $F_x=-dU/dx$. Per il peso uniforme $U=mgz$; per la molla $U=\tfrac12kx^2$. Lo zero di $U$ è arbitrario: solo le differenze entrano nel lavoro. Un minimo di $U$ è un equilibrio stabile se la curvatura è positiva; vicino a esso $U\simeq U_0+\tfrac12k_{\mathrm{eff}}(x-x_0)^2$.

![[F1-p113-1.png]]

*Figura 4.8: spostare l’origine dell’asse verticale cambia lo zero dell’energia potenziale del peso. La differenza fra le energie di due stati, e quindi il lavoro, resta invariata.* _(Libro, p. 104; PDF p. 113.)_

_(Libro, cap. 4; pagine stampate 97–118; PDF pp. 106–127.)_

## Conservazione e dissipazione

Vedi [[F1 - Conservazione e dissipazione]].

Separando forze conservative e non conservative,
$$\Delta(K+U)=W_{\mathrm{nc}}.$$
Se il lavoro non conservativo è nullo, l'energia meccanica $E=K+U$ si conserva. Il fatto che una forza sia esterna non implica che sia dissipativa, né ogni vincolo compie lavoro nullo: dipende dal suo moto. L'attrito può trasformare energia meccanica in energia interna; l'energia totale resta conservata includendo tutte le forme. I punti di inversione in un moto unidimensionale soddisfano $E=U(x)$, mentre le regioni accessibili hanno $E\ge U(x)$.

_(Libro, cap. 4; pagine stampate 97–118; PDF pp. 106–127.)_

## Momento della forza e momento angolare

Vedi [[F1 - Momento della forza e momento angolare]].

Rispetto a un polo fisso $O$ di un riferimento inerziale,
$$\boldsymbol\tau_O=\mathbf r\times\mathbf F,\qquad\mathbf L_O=\mathbf r\times m\mathbf v,\qquad\dot{\mathbf L}_O=\boldsymbol\tau_O.$$
Un momento nullo implica conservazione di $\mathbf L_O$. Per una forza centrale rispetto a $O$, $\mathbf F\parallel\mathbf r$, quindi il momento è nullo e il moto è piano. Il braccio è la distanza perpendicolare del polo dalla retta d'azione: una forza grande può produrre momento nullo se passa per il polo.

_(Libro, cap. 4; pagine stampate 97–118; PDF pp. 106–127.)_

## Derivazione guidata

Moltiplica scalarmente $m\dot{\mathbf v}=\mathbf F_{\mathrm{tot}}$ per $\mathbf v\,dt=d\mathbf r$. A sinistra $m\mathbf v\cdot d\mathbf v=d(mv^2/2)$; integrando ottieni $\Delta K=W_{\mathrm{tot}}$. Se una parte della forza è conservativa, il suo lavoro è $-\Delta U$ e si porta a sinistra: $\Delta(K+U)=W_{\mathrm{nc}}$. Non occorre conoscere il tempo di percorrenza, ma va conosciuto il lavoro delle forze lungo il percorso.

_(Libro, cap. 4; pagine stampate 97–118; PDF pp. 106–127.)_

## Esempio svolto

> [!example] Applicazione originale
> Una molla con $k=200\,\mathrm{N/m}$ è compressa di $0{,}10\,\mathrm m$ e lancia senza attrito una massa di $0{,}50\,\mathrm{kg}$. All'equilibrio $\tfrac12kx_0^2=\tfrac12mv^2$, quindi $v=x_0\sqrt{k/m}=2{,}0\,\mathrm{m/s}$. Il bilancio non fornisce direttamente il tempo necessario: per quello serve la dinamica dell'oscillatore.

## Richiami matematici

[[GEO - Prodotto scalare geometrico]] · [[06 - AN1 - Calcolo Integrale]] · [[08 - AN1 - Calcolo Differenziale in più Variabili]].

## Verifica attiva

Una forza può essere non nulla e compiere lavoro nullo?

> [!check]- Risposta ragionata
> Sì: una forza sempre perpendicolare allo spostamento, come la risultante centripeta in un moto circolare uniforme, compie lavoro nullo.

## Navigazione

Precedente: [[03 - F1 - Moti relativi e forze apparenti]] · Successivo: [[05 - F1 - Dinamica dei sistemi di punti materiali]].
