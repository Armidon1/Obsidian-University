---
title: Coordinate polari
tags:
  - analisi-1
  - concetto
  - più-variabili
  - coordinate
---

# Coordinate polari

> [!summary] In breve
> x = ρ cos ϑ, y = ρ sin ϑ con ρ = distanza dall'origine e ϑ angolo con l'asse x; il determinante jacobiano è ρ, quindi dx dy = ρ dρ dϑ.

$$\begin{cases} x = \rho\cos\vartheta \\ y = \rho\sin\vartheta \end{cases} \qquad \rho = \sqrt{x^2 + y^2}, \qquad \det J = \rho$$

Usi:
- **limiti** in $(0, 0)$: $\rho \to 0 \iff (x, y) \to (0, 0)$ in ogni direzione;
- **integrali doppi** su cerchi e settori: $\iint_X f\,dx\,dy = \iint f(\rho\cos\vartheta, \rho\sin\vartheta)\,\rho\,d\rho\,d\vartheta$;
- integrale di Gauss: $\int e^{-x^2} = \sqrt\pi$;
- **forma trigonometrica** dei numeri complessi: $z = \rho(\cos\vartheta + i\sin\vartheta)$.

Punto singolare: l'origine.

## Collegamenti

- **Concetti correlati**: [[Limite in più variabili]] · [[Cambiamento di variabili negli integrali multipli]] · [[Coordinate cilindriche e sferiche]] · [[Numeri complessi]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[07 - AN1 - Funzioni di più Variabili - Limiti e Continuità#Coordinate polari e esistenza del limite|Lezione 7 — Coordinate polari e esistenza del limite]]
> - [[09 - AN1 - Funzioni a Valori Vettoriali#Coordinate polari|Lezione 9 — Coordinate polari]]
> - [[10 - AN1 - Integrali Multipli#Cambiamento di Variabili negli Integrali Doppi|Lezione 10 — Cambiamento di Variabili negli Integrali Doppi]]
