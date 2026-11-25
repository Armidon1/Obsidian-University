---
title: Pohlig-Hellman
tags:
  - cyberbootcamp
  - concetto
  - cryptography
  - diffie-hellman
  - attack
---

# Pohlig-Hellman

> [!summary] In breve
> Se $p - 1$ ha solo fattori piccoli ($p$ *smooth*), il logaritmo discreto modulo $p$ si risolve un fattore alla volta e si ricompone con il CRT. Per questo DH usa un *safe prime* $p = 2q + 1$.

Per ogni fattore $p_i$ di $p-1$:
$$g_i = g^{(p-1)/p_i},\quad h_i = A^{(p-1)/p_i},\quad g_i^{x} \equiv h_i \;\Rightarrow\; x \bmod p_i \text{ (brute force su } p_i \text{ valori)}$$
Poi $x = \mathrm{CRT}(x \bmod p_i)$.

Esempio: $g = 3$, $A = 22$, $p = 31$, $p - 1 = 2\cdot3\cdot5$ → $x \equiv 1, 2, 2$ → $x = 17$.

- Con potenze $p_i^k$ si lavora modulo $p_i^k$.
- Sage lo usa in automatico: `Zmod(p)(A).log(g)` è istantaneo se $p$ è smooth.

## Collegamenti

- **Concetti correlati**: [[Discrete Logarithm (DL) Problem]] · [[Teorema Cinese del Resto]] · [[Diffie-Hellman Key Exchange]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[07 - CB - Crypto 2#Quando il logaritmo discreto è facile: Pohlig–Hellman|Lezione 7 — Quando il logaritmo discreto è facile: Pohlig–Hellman]]
> - [[07 - CB - Crypto 2#Il logaritmo discreto|Lezione 7 — Il logaritmo discreto]]
