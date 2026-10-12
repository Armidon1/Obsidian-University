---
title: Effective Access Time
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - prestazioni
---

# Effective Access Time

> [!summary] In breve
> Tempo medio atteso di un accesso a memoria, che tiene conto della TLB (hit ratio α) o dei page fault (page fault rate ρ).

Con TLB:

$$EAT = \alpha\,(T_{tlb} + T_{ram}) + (1-\alpha)\,(T_{tlb} + 2T_{ram})$$

Esempio: 100 ns RAM, 20 ns TLB, α = 0.8 → 140 ns.

Con demand paging:

$$EAT = (1-\rho)\,T_{mem} + \rho\,(\text{overhead del page fault} + \text{swap in})$$

Con un page fault di 8 ms, anche ρ = 1/1000 rende la memoria 40 volte più lenta.

## Collegamenti

- **Concetti correlati**: [[TLB]] · [[Demand Paging]] · [[Page Table Gerarchica]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Effective Access Time|Lezione 10 — Effective Access Time]]
> - [[11 - SO - Memoria Virtuale#Prestazioni|Lezione 11 — Prestazioni]]
