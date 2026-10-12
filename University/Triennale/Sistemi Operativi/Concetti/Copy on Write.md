---
title: Copy on Write
tags:
  - sistemi-operativi
  - concetto
  - memoria-virtuale
  - processi
---

# Copy on Write

> [!summary] In breve
> Dopo una fork padre e figlio condividono gli stessi frame marcati read-only; la prima scrittura su una pagina genera una trap e solo quella pagina viene copiata.

- Alla `fork` si copia solo la **page table** e si imposta `trap_on_write`.
- Rende la `fork` economica e `vfork` quasi superflua.
- I frame liberi vengono presi da una free list e **azzerati** per sicurezza.

## Collegamenti

- **Concetti correlati**: [[fork]] · [[Memoria Virtuale]] · [[Paging]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[11 - SO - Memoria Virtuale#Ottimizzazioni|Lezione 11 — Ottimizzazioni]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#vfork|Lezione 6 — vfork]]
