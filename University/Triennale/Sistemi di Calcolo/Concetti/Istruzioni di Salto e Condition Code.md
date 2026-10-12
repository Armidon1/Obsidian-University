---
title: Istruzioni di Salto e Condition Code
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - ia32
---

# Istruzioni di Salto e Condition Code

> [!summary] In breve
> I flag ZF, SF, CF, OF (in EFLAGS) sono impostati dalle operazioni aritmetiche e da CMP/TEST; Jcc salta, CMOVcc copia e SETcc scrive 0/1 in base a una condizione.

- `CMP S,D` calcola D−S e aggiorna i flag; `TEST S,D` calcola S&D. Il risultato viene scartato.
- Dopo `cmpl S,D` la condizione è "**D op S**".

| Con segno | Senza segno | Significato |
| --- | --- | --- |
| `jg` / `jge` | `ja` / `jae` | > / ≥ |
| `jl` / `jle` | `jb` / `jbe` | < / ≤ |
| `je` / `jne` | | == / != |

- `jmp L` (diretto), `jmp *op` (indiretto: switch, puntatori a funzione).
- `call f`: push dell'indirizzo di ritorno e salto; `ret`: pop in EIP.
- `CMOVcc` ed `SETcc` sono **branchless**: evitano gli hazard di controllo nella pipeline.

## Collegamenti

- **Concetti correlati**: [[Traduzione dei Costrutti C in Assembly]] · [[Registri IA32]] · [[Pipelining]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Istruzioni di salto|Lezione 3 — Istruzioni di salto]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Jcc e CMP: salti condizionati|Lezione 3 — Jcc e CMP: salti condizionati]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Altre istruzioni e vincoli|Lezione 3 — Altre istruzioni e vincoli]]
