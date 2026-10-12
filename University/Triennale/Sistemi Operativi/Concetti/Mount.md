---
title: Mount
tags:
  - sistemi-operativi
  - concetto
  - file-system
---

# Mount

> [!summary] In breve
> `mount -t tipo device dir` aggancia il file system di un dispositivo a una directory (mount point); `umount` lo stacca.

- Il mount point mostra la radice del file system montato; i file che conteneva prima restano nascosti finché non lo si smonta.
- Spesso richiede privilegi; i daemon montano automaticamente i dispositivi USB.
- Esiste anche come syscall `mount()`.

## Collegamenti

- **Concetti correlati**: [[File System]] · [[Driver e Block Device]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[12 - SO - File System#Mount e umount|Lezione 12 — Mount e umount]]
