---
title: Ottimizzazioni del Compilatore
tags:
  - sistemi-di-calcolo
  - concetto
  - ottimizzazione
  - gcc
---

# Ottimizzazioni del Compilatore

> [!summary] In breve
> I livelli `-O0`…`-O3`, `-Os` attivano trasformazioni che preservano la semantica: constant folding/propagation, CSE, loop-invariant code motion, unrolling, inlining, register allocation, strength reduction, dead code elimination.

| Tecnica | Idea |
| --- | --- |
| Constant folding | `8+(14/2)*3` → `29` |
| Constant propagation | `x=8; return x-2;` → `return 6;` |
| CSE | `(x+y)*(x+y)` → `z=x+y; z*z` |
| Loop-invariant code motion | sposta fuori dal ciclo ciò che non cambia |
| Loop unrolling | k iterazioni per giro, meno test e salti |
| Function inlining | sostituisce la chiamata con il corpo (`-O3`) |
| Register allocation | variabili nei registri invece che in memoria |
| Strength reduction | `x*17` → `(x<<4)+x` |
| Dead code elimination | elimina `if (0) …` |

- Il passaggio `-O0` → `-O1` è quello con il guadagno maggiore.
- Il compilatore è **conservativo**: con chiamate a funzioni sconosciute non fa CSE né hoisting.

## Collegamenti

- **Concetti correlati**: [[Loop-Invariant Code Motion]] · [[Speedup e Legge di Amdahl]] · [[Allineamento e Padding]] · [[LEA]] · [[Pipelining]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[05 - SDC - Ottimizzazione dei programmi#Tecniche di ottimizzazione|Lezione 5 — Tecniche di ottimizzazione]]
> - [[05 - SDC - Ottimizzazione dei programmi#Livelli di ottimizzazione in gcc|Lezione 5 — Livelli di ottimizzazione in gcc]]
> - [[05 - SDC - Ottimizzazione dei programmi#Riepilogo: chi fa cosa|Lezione 5 — Riepilogo: chi fa cosa]]
