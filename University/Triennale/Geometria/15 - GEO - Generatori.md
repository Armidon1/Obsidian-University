---
title: "Generatori"
aliases:
  - "GEO — Generatori"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "15"
pdf_pages: "231–240"
---

# Generatori

> [!abstract] Scopo e percorso
> Vettori, spazi e basi. Questa nota segue il capitolo 15 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 15.1 - Combinazioni lineari e generatori

Vedi [[GEO - Span e generatori]].

Il sottospazio generato da $v_1,\ldots,v_r$ è l’insieme di tutte le loro combinazioni lineari:

$$\langle v_1,\ldots,v_r\rangle=\left\{\sum_{i=1}^r a_iv_i:a_i\in\mathbb R\right\}.$$

Si usa anche la notazione inglese $\operatorname{span}(v_1,\ldots,v_r)$. È un sottospazio perché la somma di due combinazioni e il multiplo di una combinazione sono ancora combinazioni degli stessi vettori. È il più piccolo sottospazio che li contiene.

I vettori sono generatori di $V$ quando il loro span coincide con $V$. Per controllare se un vettore $w$ appartiene allo span, si risolve il sistema $a_1v_1+\cdots+a_rv_r=w$.

> [!example] Appartenenza allo span
> Per $u=(1,0,1)$ e $v=(0,1,1)$, lo span è $\{(a,b,a+b):a,b\in\mathbb R\}$. Il vettore $(2,-1,1)$ appartiene allo span, perché $2u-v=(2,-1,1)$; $(0,0,1)$ non vi appartiene.

Uno spazio è finitamente generato se bastano finitissimi generatori. $\mathbb R^n$ e gli spazi di matrici lo sono. $\mathbb R[x]$ non lo è: finitissimi polinomi hanno grado limitato e le loro combinazioni non possono produrre potenze arbitrariamente alte.

_(Accascina–Monti, § 15.1, libro pp. 215–219; PDF pp. 231–235.)_

## Ripasso attivo

- **Combinazioni lineari e generatori:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Span e generatori]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 222 (PDF p. 238). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[14 - GEO - Sottospazi vettoriali]] · Successiva: [[16 - GEO - Dipendenza e indipendenza lineare]]

[[MOC - Geometria]]
