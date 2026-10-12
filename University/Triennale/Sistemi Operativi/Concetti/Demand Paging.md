---
title: Demand Paging
tags:
  - sistemi-operativi
  - concetto
  - memoria-virtuale
---

# Demand Paging

> [!summary] In breve
> Le pagine vengono caricate in RAM solo al primo accesso: un accesso a una pagina invalida genera un page fault, il kernel la carica dal disco, aggiorna la page table e riesegue l'istruzione.

- Servono: il bit di validità, lo swap space, il **restart delle istruzioni** (il page fault è un *fault*).
- **Lazy swapper / pager**; **pure demand paging**: il processo parte con zero pagine in memoria.
- Page fault: trap → controllo di validità → lettura da disco in un frame libero (nel frattempo gira un altro processo) → interrupt del disco → aggiornamento della page table → riesecuzione.
- Swap space in raw mode, senza file system, per un I/O più veloce.

## Collegamenti

- **Concetti correlati**: [[Memoria Virtuale]] · [[Eccezioni]] · [[Page Replacement]] · [[Effective Access Time]] · [[Thrashing e Working Set]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[11 - SO - Memoria Virtuale#Demand paging|Lezione 11 — Demand paging]]
> - [[11 - SO - Memoria Virtuale#Gestione di un page fault|Lezione 11 — Gestione di un page fault]]
> - [[11 - SO - Memoria Virtuale#Prestazioni|Lezione 11 — Prestazioni]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Paginazione su richiesta|Sistemi di Calcolo, cap. 7 — Paginazione su richiesta]]
