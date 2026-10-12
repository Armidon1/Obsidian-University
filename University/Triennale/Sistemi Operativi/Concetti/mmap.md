---
title: mmap
tags:
  - sistemi-operativi
  - concetto
  - file-system
  - memoria-virtuale
---

# mmap

> [!summary] In breve
> Mappa un file (o un dispositivo) nello spazio di indirizzi del processo: lo si legge e scrive come un array, e il caricamento/scrittura delle pagine lo gestisce il memory manager (demand paging).

```c
void *p = mmap(NULL, len, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);
munmap(p, len);
```

- Le pagine vengono caricate al primo accesso e riscritte se dirty: la cache è trasparente.
- Permette di mappare memoria dei dispositivi (es. video) e di condividere memoria tra processi.

## Collegamenti

- **Concetti correlati**: [[Demand Paging]] · [[File Descriptor]] · [[Memoria Virtuale]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[12 - SO - File System#mmap|Lezione 12 — mmap]]
