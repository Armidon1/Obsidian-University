---
title: Coordinate cilindriche e sferiche
tags:
  - analisi-1
  - concetto
  - più-variabili
  - coordinate
---

# Coordinate cilindriche e sferiche

> [!summary] In breve
> Cilindriche: polari nel piano xy più l'altezza z (det J = ρ). Sferiche: distanza ρ, longitudine ϑ e angolo φ dall'asse z (det J = ρ² sin φ).

$$\text{cilindriche: } \begin{cases} x = \rho\cos\vartheta \\ y = \rho\sin\vartheta \\ z = t \end{cases} \qquad \text{sferiche: } \begin{cases} x = \rho\sin\varphi\cos\vartheta \\ y = \rho\sin\varphi\sin\vartheta \\ z = \rho\cos\varphi \end{cases}$$

- $dV = \rho\,d\rho\,d\vartheta\,dt$ (cilindriche), $dV = \rho^2\sin\varphi\,d\rho\,d\varphi\,d\vartheta$ (sferiche).
- Volume della sfera: $\int_0^{2\pi}\int_0^R\int_0^\pi \rho^2\sin\varphi = \frac43\pi R^3$.
- Cilindriche per solidi con simmetria attorno a un asse (coni, cilindri), sferiche per sfere.

## Collegamenti

- **Concetti correlati**: [[Coordinate polari]] · [[Trasformazione regolare di coordinate]] · [[Integrale triplo]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[09 - AN1 - Funzioni a Valori Vettoriali#Coordinate cilindriche|Lezione 9 — Coordinate cilindriche]]
> - [[09 - AN1 - Funzioni a Valori Vettoriali#Coordinate sferiche|Lezione 9 — Coordinate sferiche]]
> - [[10 - AN1 - Integrali Multipli#Cambiamento di variabili negli integrali tripli|Lezione 10 — Cambiamento di variabili negli integrali tripli]]
