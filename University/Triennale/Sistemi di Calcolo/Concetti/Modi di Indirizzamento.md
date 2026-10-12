---
title: Modi di Indirizzamento
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - ia32
---

# Modi di Indirizzamento

> [!summary] In breve
> Forma generale di un operando memoria in AT&T: `imm(base, indice, scala)` = M[imm + base + indice·scala], con scala ∈ {1, 2, 4, 8}.

| Sintassi | Valore |
| --- | --- |
| `$imm` | costante |
| `%reg` | R[reg] |
| `imm` | M[imm] (assoluto) |
| `(%b)` | M[R[b]] |
| `imm(%b)` | M[imm + R[b]] |
| `imm(%b,%i,s)` | M[imm + R[b] + R[i]·s] |

- `a[i]` con elementi di s byte → `(base,i,s)`: è l'aritmetica dei puntatori.
- La destinazione non può essere un immediato; non si possono avere **due operandi in memoria**.
- Sintassi **AT&T**: sorgente, destinazione (Intel: il contrario).

## Collegamenti

- **Concetti correlati**: [[Registri IA32]] · [[LEA]] · [[Traduzione dei Costrutti C in Assembly]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Operandi e modi di indirizzamento|Lezione 3 — Operandi e modi di indirizzamento]]
