---
title: File Descriptor
tags:
  - sistemi-operativi
  - concetto
  - file-system
  - syscall
---

# File Descriptor

> [!summary] In breve
> Intero che identifica un file aperto in un processo (indice nella tabella dei file aperti del processo); 0 = stdin, 1 = stdout, 2 = stderr.

- `open`/`creat` → fd; `read`/`write` operano sulla posizione corrente e la spostano; `lseek(fd, off, SEEK_SET|SEEK_CUR|SEEK_END)`; `close`.
- `dup`/`dup2` clonano un fd (posizione condivisa): servono per la redirezione.
- `select` attende su insiemi di fd (`FD_SET`, `FD_ISSET`…).
- `stat`/`fstat` danno gli attributi; `getdents` legge le directory; `link`/`unlink`.
- Ogni `open` dello stesso file dà un fd con una posizione indipendente.

## Collegamenti

- **Concetti correlati**: [[File System]] · [[Strutture Dati del File System]] · [[Device File e ioctl]] · [[mmap]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[12 - SO - File System#File descriptor|Lezione 12 — File descriptor]]
> - [[12 - SO - File System#Strutture dati|Lezione 12 — Strutture dati]]
> - [[08 - SDC - Gestione dei file#Tabella dei descrittori di file di un processo|Sistemi di Calcolo, cap. 8 — Tabella dei descrittori di file di un processo]]
