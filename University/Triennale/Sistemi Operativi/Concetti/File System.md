---
title: File System
tags:
  - sistemi-operativi
  - concetto
  - file-system
---

# File System

> [!summary] In breve
> Astrazione che organizza i blocchi del disco in un albero di file (sequenze di byte con attributi) e directory, con radice `/`.

- **File**: dati persistenti con attributi (nome, dimensione, permessi, owner, date; per il sistema: un ID unico e la posizione). `file nome` riconosce il tipo dai primi byte.
- Operazioni: create, delete, truncate, open, close, seek, read, write, select.
- File system logici: `/proc` (processi), `/sys` (sistema), `/dev` (dispositivi).
- API: `FILE*` della libc (alto livello, con buffer) sopra i **file descriptor** delle syscall.

## Collegamenti

- **Concetti correlati**: [[File Descriptor]] · [[Link Hard e Soft]] · [[Mount]] · [[Permessi e Ownership]] · [[Strutture Dati del File System]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[12 - SO - File System#Concetti base|Lezione 12 — Concetti base]]
> - [[12 - SO - File System#File|Lezione 12 — File]]
> - [[12 - SO - File System#Il FILE come tipo di dato astratto|Lezione 12 — Il FILE come tipo di dato astratto]]
> - [[08 - SDC - Gestione dei file#File e directory|Sistemi di Calcolo, cap. 8 — File e directory]]
