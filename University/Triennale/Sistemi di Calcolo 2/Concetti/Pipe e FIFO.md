---
title: Pipe e FIFO
tags:
  - sistemi-di-calcolo-2
  - concetto
  - ipc
---

# Pipe e FIFO

> [!summary] In breve
> Canali monodirezionali a byte: `pipe(fd)` crea fd[0] (lettura) e fd[1] (scrittura) tra processi parenti; `mkfifo` crea una pipe con nome nel file system, usabile da processi qualsiasi.

- Lettura da pipe vuota e scrittura su pipe piena **bloccano**. Capacità su Linux: 64 KiB.
- Scritture ≤ `PIPE_BUF` (4096) sono **atomiche**.
- `read` restituisce **0** quando tutti gli scrittori hanno chiuso fd[1]; scrivere senza lettori → **`SIGPIPE`**.
- **Chiudere i descrittori non usati** (il lettore chiude fd[1]), altrimenti deadlock.
- FIFO: `open` bloccante finché non c'è l'altro capo (`O_NONBLOCK` per evitarlo); si rimuove con `unlink`.

## Collegamenti

- **Concetti correlati**: [[Inter-Process Communication]] · [[File Descriptor]] · [[fork]] · [[Segnali]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[05 - SDC2 - Comunicazione tra Processi#Pipe|Lezione 5 — Pipe]]
> - [[05 - SDC2 - Comunicazione tra Processi#pipe() in Unix|Lezione 5 — pipe() in Unix]]
> - [[05 - SDC2 - Comunicazione tra Processi#FIFO (named pipe)|Lezione 5 — FIFO (named pipe)]]
> - [[05 - SDC2 - Comunicazione tra Processi#Pipe e FIFO a confronto|Lezione 5 — Pipe e FIFO a confronto]]
