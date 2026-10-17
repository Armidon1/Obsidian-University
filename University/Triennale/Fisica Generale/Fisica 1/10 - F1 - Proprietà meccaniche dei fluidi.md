---
title: "Proprietà meccaniche dei fluidi"
aliases:
  - "F1 — Proprietà meccaniche dei fluidi"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "258-283"
---

# Proprietà meccaniche dei fluidi

> [!abstract]
> Il fluido non mantiene una forma propria e trasmette sforzi normali attraverso la pressione. Si passa dall’equilibrio idrostatico al moto ideale e poi agli effetti della viscosità.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Pressione e legge di Stevino

Vedi [[F1 - Pressione e legge di Stevino]].

La pressione $p=dF_\perp/dS$ si misura in pascal. In equilibrio, con asse verticale crescente verso l'alto, $dp/dz=-\rho g$. Per densità uniforme $p=p_0+\rho gh$ alla profondità $h$. La forza su una superficie è $\mathbf F=-\int p\hat{\mathbf n}\,dS$ per normale uscente dal corpo considerato. Il principio di Pascal descrive la trasmissione di una variazione di pressione in un fluido confinato. Pressione assoluta e relativa differiscono della pressione di riferimento, di solito atmosferica.

_(Libro, cap. 10; pagine stampate 249–274; PDF pp. 258–283.)_

## Spinta di Archimede

Vedi [[F1 - Spinta di Archimede]].

La risultante delle pressioni su un corpo immerso è verso l'alto e ha modulo $F_A=\rho_f gV_{\mathrm{spostato}}$. È il peso del fluido sostituito dal corpo, non necessariamente quello del corpo. Per galleggiamento statico $\rho_fV_{\mathrm{imm}}=m$; un corpo omogeneo ha frazione immersa $V_{\mathrm{imm}}/V=\rho_c/\rho_f$. La posizione del centro di spinta e del centro di massa conta per la stabilità dell'orientazione.

![[F1-p267-1.png]]

*Figura 10.18: in una vasca accelerata orizzontalmente l’equilibrio va studiato con la gravità efficace g−a. La superficie libera è perpendicolare a essa e la spinta è opposta alla forza di volume efficace.* _(Libro, p. 258; PDF p. 267.)_

_(Libro, cap. 10; pagine stampate 249–274; PDF pp. 258–283.)_

## Continuità e portata

Vedi [[F1 - Continuità e portata]].

La conservazione della massa in moto stazionario impone $\rho Av_n=\mathrm{costante}$ per un tubo di flusso con velocità uniforme sulla sezione. Per un liquido incomprimibile $Q=Av$ è la portata volumetrica e resta costante. Una strozzatura aumenta la velocità media. In forma locale $\partial_t\rho+\nabla\cdot(\rho\mathbf v)=0$; per densità costante si riduce a $\nabla\cdot\mathbf v=0$.

_(Libro, cap. 10; pagine stampate 249–274; PDF pp. 258–283.)_

## Bernoulli e applicazioni

Vedi [[F1 - Bernoulli e applicazioni]].

Per moto stazionario di fluido incomprimibile non viscoso, lungo una linea di corrente,
$$p+\tfrac12\rho v^2+\rho gz=\mathrm{costante}.$$
Ogni termine ha dimensioni di energia per volume. Fra superficie libera di un grande serbatoio e foro alla stessa pressione esterna, $v=\sqrt{2gh}$ è la legge di Torricelli. Non si applica Bernoulli senza correzioni attraverso pompe, turbine o tratti con dissipazione significativa. A uguale quota una velocità maggiore corrisponde a pressione minore soltanto sotto le ipotesi del teorema.

_(Libro, cap. 10; pagine stampate 249–274; PDF pp. 258–283.)_

## Viscosità, Poiseuille e numero di Reynolds

Vedi [[F1 - Viscosità, Poiseuille e numero di Reynolds]].

Per fluido newtoniano lo sforzo tangenziale è $\tau=\eta\,dv/dy$, con viscosità dinamica $\eta$ in $\mathrm{Pa\,s}$. Nel moto laminare sviluppato in un tubo cilindrico,
$$Q=\frac{\pi R^4}{8\eta\ell}\Delta p.$$
La dipendenza da $R^4$ rende il raggio decisivo. Il numero $\mathrm{Re}=\rho vD/\eta$ confronta inerzia e viscosità; le soglie di transizione dipendono dalla geometria e dalle perturbazioni. Per una sfera lenta in regime di Stokes $F_v=6\pi\eta Rv$; il modello non vale a qualsiasi Reynolds.

_(Libro, cap. 10; pagine stampate 249–274; PDF pp. 258–283.)_

## Derivazione guidata

Considera un elemento di fluido fermo di altezza $dz$ e area $A$. Le pressioni inferiore e superiore danno una risultante verticale $-[p(z+dz)-p(z)]A$; il peso è $-\rho gA\,dz$. Dall'equilibrio si ricava $dp/dz=-\rho g$. Integrando fra la superficie e profondità $h$ con densità costante segue Stevino. La pressione cresce scendendo: il segno va verificato rispetto all'asse scelto.

_(Libro, cap. 10; pagine stampate 249–274; PDF pp. 258–283.)_

## Esempio svolto

> [!example] Applicazione originale
> Un oggetto omogeneo di densità $600\,\mathrm{kg/m^3}$ galleggia in acqua di densità $1000\,\mathrm{kg/m^3}$. L'equilibrio impone una frazione immersa $0{,}60$. Se lo si immerge completamente, la spinta supera il suo peso: per trattenerlo occorre una forza verso il basso.

## Richiami matematici

[[06 - AN1 - Calcolo Integrale]] · [[10 - AN1 - Integrali Multipli]].

## Verifica attiva

Si può usare Bernoulli per calcolare una caduta di pressione viscosa in un tubo lungo?

> [!check]- Risposta ragionata
> Serve un termine di perdita di carico o una legge viscosa come Poiseuille nelle sue ipotesi. Bernoulli ideale non descrive la dissipazione.

## Navigazione

Precedente: [[09 - F1 - Onde meccaniche]] · Successivo: [[11 - F1 - Sistemi termodinamici e temperatura]].
