---
title: "Potenziale elettrostatico"
aliases:
  - "F2 — Potenziale elettrostatico"
tags:
  - fisica-2
  - capitolo
source: "pdf/Fisica Generale - Elettromagnetismo ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "57-96"
---

# Potenziale elettrostatico

> [!abstract]
> Il carattere conservativo del campo elettrostatico permette di descriverlo con una funzione scalare. Il potenziale semplifica i calcoli e collega campo, energia e condizioni al contorno.
> Percorso del corso: [[MOC - Fisica 2]]. Convenzioni e metodo: [[00 - F2 - Guida allo studio]].

## Conservatività e differenza di potenziale

Vedi [[F2 - Conservatività e differenza di potenziale]].

Per cariche sorgenti ferme,
$$V(B)-V(A)=-\int_A^B\mathbf E\cdot d\mathbf l,\qquad\oint\mathbf E\cdot d\mathbf l=0.$$
La differenza di potenziale si misura in volt, $1\,\mathrm V=1\,\mathrm{J/C}$. Il lavoro del campo su una carica $q$ è $W=q[V(A)-V(B)]$. Per un insieme di cariche localizzato si può porre $V(\infty)=0$; questa scelta non è disponibile per ogni distribuzione infinita. Lo zero del potenziale non cambia il campo.

_(Libro, cap. 2; pagine stampate 49–88; PDF pp. 57–96.)_

## Potenziale coulombiano e distribuzioni

Vedi [[F2 - Potenziale coulombiano e distribuzioni]].

Per una carica puntiforme $V=Q/(4\pi\varepsilon_0r)$ con zero all'infinito. Per sovrapposizione,
$$V(\mathbf r)=\frac1{4\pi\varepsilon_0}\int\frac{dq}{|\mathbf r-\mathbf r'|}.$$
È una somma scalare: spesso più semplice dell'integrale vettoriale del campo. Il dipolo è formato da $+q$ e $-q$ separate dal vettore $\mathbf d$ diretto dalla carica negativa alla positiva. Lontano dalle sorgenti, con $\mathbf p=q\mathbf d$, $V\simeq\mathbf p\cdot\hat{\mathbf r}/(4\pi\varepsilon_0r^2)$; il suo campo decade come $r^{-3}$.

_(Libro, cap. 2; pagine stampate 49–88; PDF pp. 57–96.)_

## Gradiente e superfici equipotenziali

Vedi [[F2 - Gradiente e superfici equipotenziali]].

Dalla definizione differenziale $dV=-\mathbf E\cdot d\mathbf l$ segue
$$\mathbf E=-\nabla V.$$
Il campo punta verso potenziali decrescenti ed è normale alle superfici equipotenziali dove il gradiente è non nullo. Una carica positiva inizialmente libera accelera nella direzione del campo; una negativa in quella opposta. Dire $V=0$ in un punto non implica $\mathbf E=0$ lì: contano le variazioni spaziali. Superfici equipotenziali più ravvicinate a parità di incremento di $V$ indicano un campo più intenso.

![[F2-p068-1.png]]

*Figura 2-13: uno spostamento tangente alla superficie equipotenziale non cambia V. Il campo non ha componente tangenziale e risulta normale alla superficie nei punti regolari con campo non nullo.* _(Libro, p. 60; PDF p. 68.)_

_(Libro, cap. 2; pagine stampate 49–88; PDF pp. 57–96.)_

## Energia potenziale e dipolo in un campo

Vedi [[F2 - Energia potenziale e dipolo in un campo]].

Per una carica di prova in un campo esterno fissato $U=qV$. Per cariche puntiformi interagenti,
$$U=\sum_{i<j}\frac{q_iq_j}{4\pi\varepsilon_0r_{ij}}=\tfrac12\sum_iq_iV_{\mathrm{altre}}(\mathbf r_i).$$
Il fattore $1/2$ evita il doppio conteggio; il potenziale proprio della singola carica non va incluso. Un dipolo rigido in campo uniforme ha $U=-\mathbf p\cdot\mathbf E$ e momento $\boldsymbol\tau=\mathbf p\times\mathbf E$. La forza risultante è nulla nel campo uniforme ma può essere non nulla in un campo non uniforme.

_(Libro, cap. 2; pagine stampate 49–88; PDF pp. 57–96.)_

## Rotore, Poisson e Laplace

Vedi [[F2 - Rotore, Poisson e Laplace]].

L'elettrostatica soddisfa $\nabla\times\mathbf E=0$ nei punti regolari. Combinando Gauss con $\mathbf E=-\nabla V$,
$$\nabla^2V=-\rho/\varepsilon_0.$$
In una regione senza cariche si ottiene l'equazione di Laplace $\nabla^2V=0$. Per determinare una soluzione occorrono condizioni al contorno. L'annullamento del rotore garantisce localmente un potenziale; per una conclusione globale serve anche controllare il dominio e l'assenza di circuitazioni non nulle. Il metodo non sostituisce le condizioni fisiche ai confini dei conduttori.

_(Libro, cap. 2; pagine stampate 49–88; PDF pp. 57–96.)_

## Sviluppo multipolare e dipolo non uniforme

Vedi [[F2 - Sviluppo multipolare e dipolo non uniforme]].

Molto lontano da una distribuzione localizzata si sviluppa il potenziale in potenze del rapporto fra dimensione della sorgente e distanza. Il termine di monopolo dipende dalla carica totale e scala come $1/r$; se questa è nulla, il dipolo è in genere il primo contributo e scala come $1/r^2$; il termine quadrupolare scala come $1/r^3$. Uno zero del dipolo non rende nullo tutto il campo. In campo esterno non uniforme un dipolo piccolo e fissato sente $\mathbf F=\nabla(\mathbf p\cdot\mathbf E)$, con le opportune ipotesi sul dipolo; l'approssimazione perde validità se il campo varia molto sulla sua dimensione.

_(Libro, cap. 2; pagine stampate 49–88; PDF pp. 57–96.)_

## Derivazione guidata

Per una carica $Q$, la differenza di potenziale fra due raggi è $V(r)-V(\infty)=-\int_\infty^r Q\,ds/(4\pi\varepsilon_0s^2)=Q/(4\pi\varepsilon_0r)$. Il segno del potenziale coincide con quello della sorgente con questa scelta dello zero. Derivare di nuovo dà $E_r=-dV/dr=Q/(4\pi\varepsilon_0r^2)$. Integrare il campo e derivare il potenziale sono operazioni inverse, a meno della costante additiva.

_(Libro, cap. 2; pagine stampate 49–88; PDF pp. 57–96.)_

## Esempio svolto

> [!example] Applicazione originale
> Una carica positiva $q=2\,\mathrm{nC}$ va da $V_A=100\,\mathrm V$ a $V_B=40\,\mathrm V$. Il lavoro elettrico è $q(V_A-V_B)=1{,}2\cdot10^{-7}\,\mathrm J$ e la variazione di energia potenziale è l'opposto. In assenza di altre forze cresce della stessa quantità l'energia cinetica.

## Richiami matematici

[[08 - AN1 - Calcolo Differenziale in più Variabili]] · [[GEO - Prodotto scalare geometrico]] · [[04 - F1 - Lavoro, energia e momento angolare]].

## Verifica attiva

Un punto ha potenziale zero: una carica lì sente necessariamente forza nulla?

> [!check]- Risposta ragionata
> No. Il valore del potenziale dipende dallo zero scelto; il campo dipende dal gradiente. Per esempio il piano mediano di un dipolo può avere V nullo e campo non nullo.

## Navigazione

Precedente: [[01 - F2 - Fenomeni elettrici e legge di Gauss]] · Successivo: [[03 - F2 - Conduttori, condensatori e dielettrici]].
