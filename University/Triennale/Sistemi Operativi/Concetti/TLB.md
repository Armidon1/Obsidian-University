---
title: TLB
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - hardware
  - cache
---

# TLB

> [!summary] In breve
> Translation Lookaside Buffer: cache associativa (ricerca in parallelo) delle traduzioni pagina → frame. Hit: niente accesso alla page table; miss: si legge la page table e si aggiorna la TLB.

- Piccola (decine o centinaia di entry) ma molto veloce; funziona grazie alla **località**.
- Al context switch va svuotata, oppure le entry vanno etichettate con un ASID.
- ARM: due micro-TLB (istruzioni e dati) più una TLB principale.
- **Hit ratio** α → [[Effective Access Time]].

## Collegamenti

- **Concetti correlati**: [[Paging]] · [[Effective Access Time]] · [[Page Table Gerarchica]] · [[Context Switch]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#TLB|Lezione 10 — TLB]]
> - [[10 - SO - Gestione della Memoria#ARM|Lezione 10 — ARM]]
