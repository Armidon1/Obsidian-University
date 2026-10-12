---
title: Page Table Gerarchica
tags:
  - sistemi-operativi
  - concetto
  - memoria
---

# Page Table Gerarchica

> [!summary] In breve
> Si pagina la page table stessa: una outer page table punta a pagine della page table, così si allocano solo le parti usate. Costo: più accessi in caso di TLB miss.

- Due livelli: indirizzo = (p₁, p₂, d).
- **IA-32**: page directory (puntata da CR3) da 10 bit + page table da 10 bit + offset da 12 bit; con pagine da 4 MB basta un livello.
- **ARM**: un livello per le sezioni da 1/16 MB, due livelli per le pagine da 4/16 KB.

## Collegamenti

- **Concetti correlati**: [[Paging]] · [[TLB]] · [[Effective Access Time]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Page table gerarchica|Lezione 10 — Page table gerarchica]]
> - [[10 - SO - Gestione della Memoria#IA-32|Lezione 10 — IA-32]]
> - [[10 - SO - Gestione della Memoria#ARM|Lezione 10 — ARM]]
