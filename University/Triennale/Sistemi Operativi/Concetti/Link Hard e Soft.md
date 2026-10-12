---
title: Link Hard e Soft
tags:
  - sistemi-operativi
  - concetto
  - file-system
---

# Link Hard e Soft

> [!summary] In breve
> Hard link: un altro nome per lo stesso file (stesso inode); il file sparisce quando cade l'ultimo. Soft link: un file che contiene un percorso; cancellarlo non tocca il file.

- `ln old new` crea un hard link; `ln -s old new` un soft link.
- Gli hard link sono tutti equivalenti: non c'è un "originale".
- Un soft link a un file cancellato resta "appeso".
- `rm` = `unlink()`.

## Collegamenti

- **Concetti correlati**: [[File System]] · [[Strutture Dati del File System]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[12 - SO - File System#Directory e link|Lezione 12 — Directory e link]]
> - [[12 - SO - File System#Concetti base|Lezione 12 — Concetti base]]
