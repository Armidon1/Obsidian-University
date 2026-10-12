---
title: Circuiti Combinatori e Addizionatori
tags:
  - sistemi-di-calcolo
  - concetto
  - hardware
  - logica
---

# Circuiti Combinatori e Addizionatori

> [!summary] In breve
> Circuiti il cui output dipende solo dagli input attuali; esempio: half adder (XOR + AND), full adder (con riporto in ingresso) e addizionatore a n bit in cascata.

- **Half adder**: $S = X \oplus Y$, $R = X \cdot Y$.
- **Full adder**: $S = X \oplus Y \oplus R$, $R' = XY + R(X \oplus Y)$.
- **Addizionatore a n bit** (*ripple carry*): n full adder in cascata, il riporto passa da uno al successivo, e il primo riporto vale 0.
- Si ricava la formula dalle righe in cui l'output vale 1 (somma di prodotti).

## Collegamenti

- **Concetti correlati**: [[Porte Logiche]] · [[Flip-Flop SR]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[01 - SDC - Cosa è un sistema di calcolo#Circuiti combinatori|Lezione 1 — Circuiti combinatori]]
