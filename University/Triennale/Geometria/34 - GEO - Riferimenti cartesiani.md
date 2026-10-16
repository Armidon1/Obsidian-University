---
title: "Riferimenti cartesiani"
aliases:
  - "GEO — Riferimenti cartesiani"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "34"
pdf_pages: "589–592"
---

# Riferimenti cartesiani

> [!abstract] Scopo e percorso
> Geometria metrica e prodotto scalare. Questa nota segue il capitolo 34 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 34.1 - Sistemi di riferimento cartesiani

Vedi [[GEO - Riferimento cartesiano ortonormale]].

Un riferimento cartesiano è un riferimento affine la cui base è ortonormale. Permette di leggere direttamente prodotti scalari, angoli e lunghezze dalle coordinate. Un riferimento affine generico, invece, garantisce solo la descrizione di posizione e direzioni.

Traslare l’origine non cambia distanze e angoli. Anche passare tra due basi ortonormali conserva la struttura metrica, come sarà espresso dalle matrici ortogonali.

_(Accascina–Monti, § 34.1, libro pp. 573–574; PDF pp. 589–590.)_

![[GEO-p589-1.png|650]]

**Lettura della figura (PDF p. 589, libro p. 573).** Il riferimento ortonormale distingue le componenti lungo assi perpendicolari; Pitagora applicato allo spostamento giustifica la formula della distanza.

## 34.2 - Distanza tra punti

Vedi [[GEO - Distanza tra punti]].

La distanza tra due punti è la norma dello spostamento:

$$d(P,Q)=\|Q-P\|=\sqrt{\sum_{i=1}^{n}(q_i-p_i)^2}.$$

Nel piano bastano due termini, nello spazio tre. Per $P=(1,2,3)$ e $Q=(3,-1,3)$ la differenza è $(2,-3,0)$, quindi $d(P,Q)=\sqrt{13}$.

> [!important] Ipotesi sulle coordinate
> La formula con la somma dei quadrati vale in un riferimento cartesiano ortonormale. In assi obliqui le coordinate non misurano spostamenti ortogonali e la formula va adattata al prodotto scalare della base.

_(Accascina–Monti, § 34.2, libro pp. 574–575; PDF pp. 590–591.)_

## Ripasso attivo

- **Sistemi di riferimento cartesiani:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Riferimento cartesiano ortonormale]].
- **Distanza tra punti:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Distanza tra punti]].

## Collegamenti

Precedente: [[33 - GEO - Prodotto scalare di vettori geometrici]] · Successiva: [[35 - GEO - Geometria analitica metrica del piano]]

[[MOC - Geometria]]
