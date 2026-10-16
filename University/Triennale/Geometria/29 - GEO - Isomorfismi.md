---
title: "Isomorfismi"
aliases:
  - "GEO — Isomorfismi"
tags:
  - geometria
  - lezione
source: "pdf/Geometria.pdf"
chapter: "29"
pdf_pages: "503–510"
---

# Isomorfismi

> [!abstract] Scopo e percorso
> Funzioni e applicazioni lineari. Questa nota segue il capitolo 29 del libro e raccoglie definizioni, risultati e passaggi operativi. Indice generale: [[MOC - Geometria]].

> [!note] Come leggere i riferimenti
> Fonte: Giuseppe Accascina e Valerio Monti, *Geometria*, versione 1 del 21 settembre 2015. La pagina PDF è la pagina stampata più 16. Gli esempi di calcolo aggiuntivi sono elaborazioni didattiche; i riferimenti indicano dove il libro tratta il risultato. Le figure originali sono conservate come pagine renderizzate, con il loro contesto.

## 29.1 - Isomorfismi

Vedi [[GEO - Isomorfismi di spazi vettoriali]].

Un isomorfismo è un’applicazione lineare biiettiva. La sua inversa è lineare: se $f(u)=a$ e $f(v)=b$, allora $f(hu+kv)=ha+kb$, da cui $f^{-1}(ha+kb)=hf^{-1}(a)+kf^{-1}(b)$.

Due spazi vettoriali reali di dimensione finita sono isomorfi se e solo se hanno la stessa dimensione. La scelta di basi costruisce esplicitamente l’isomorfismo associando i vettori della prima base a quelli della seconda.

Per una **specifica** applicazione lineare $f:V\to W$ con $\dim V=\dim W=n$, sono equivalenti:

$$f\text{ iniettiva}\iff f\text{ suriettiva}\iff f\text{ isomorfismo}\iff\det A\ne0.$$

Avere ambienti di uguale dimensione non rende ogni applicazione un isomorfismo: la funzione nulla $\mathbb R^2\to\mathbb R^2$ non lo è. Per esempio $f(x,y)=(x+y,x-y)$ è invece invertibile, con inversa $((u+v)/2,(u-v)/2)$.

> [!warning] Correzione
> Nel sunto del libro compare la direzione «$f^{-1}:A\to B$» per l’inversa di $f:A\to B$ (p. 491, PDF p. 507). Il dominio e il codominio vanno scambiati: $f^{-1}:B\to A$.

_(Accascina–Monti, § 29.1, libro pp. 487–490; PDF pp. 503–506.)_

## Ripasso attivo

- **Isomorfismi:** ricostruisci definizione, ipotesi e procedimento; poi controlla la scheda [[GEO - Isomorfismi di spazi vettoriali]].

> [!tip] Allenamento sul libro
> Gli esercizi del capitolo iniziano a p. 491 (PDF p. 507). Prova a svolgerli prima di consultare le soluzioni del libro. Le note riassumono la teoria e propongono esempi svolti; non trascrivono tutte le risoluzioni.

## Collegamenti

Precedente: [[28 - GEO - Nucleo]] · Successiva: [[30 - GEO - Endomorfismi]]

[[MOC - Geometria]]
