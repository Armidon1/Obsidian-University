---
title: Integrazione per sostituzione
tags:
  - analisi-1
  - concetto
  - integrali
  - metodi-di-integrazione
---

# Integrazione per sostituzione

> [!summary] In breve
> ∫ f(φ(t))φ'(t) dt = ∫ f(x) dx con x = φ(t), dx = φ'(t) dt: inverte la regola della catena; negli integrali definiti si cambiano anche gli estremi.

$$\int_\alpha^\beta f(\varphi(t))\varphi'(t)\,dt = \int_{\varphi(\alpha)}^{\varphi(\beta)} f(x)\,dx$$

- Procedura formale: $x = \varphi(t)$, $\frac{dx}{dt} = \varphi'(t)$, $dx = \varphi'(t)\,dt$.
- Esempi: $x = \sqrt{t - 1}$ in $\int_1^2 t\sqrt{t-1}\,dt = \frac{16}{15}$; $x = \sin t$ per l'area del cerchio ($\pi$); $x = \ln t$; $t = e^x$ per $\frac{1}{\cosh}$, $\frac{1}{\sinh}$.
- Negli indefiniti si torna sempre alla variabile iniziale.
- In più variabili: [[Cambiamento di variabili negli integrali multipli]] (con $|\det J|$).

## Collegamenti

- **Concetti correlati**: [[Integrazione per parti]] · [[Regole di derivazione]] · [[Cambiamento di variabili negli integrali multipli]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[06 - AN1 - Calcolo Integrale#Integrazione per sostituzione|Lezione 6 — Integrazione per sostituzione]]
