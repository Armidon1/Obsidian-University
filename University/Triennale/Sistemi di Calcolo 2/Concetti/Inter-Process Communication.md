---
title: Inter-Process Communication
tags:
  - sistemi-di-calcolo-2
  - concetto
  - ipc
---

# Inter-Process Communication

> [!summary] In breve
> Meccanismi con cui processi cooperanti, che hanno spazi di indirizzi separati, comunicano e si sincronizzano: memoria condivisa (veloce, sincronizzazione a carico del programmatore) o message passing (tramite il kernel).

- Motivi per cooperare: condivisione di informazioni, velocità, modularità, comodità.
- Comunicazione: byte stream (pipe, FIFO, stream socket), messaggi (code, datagram socket), memoria condivisa (shm, mmap).
- Sincronizzazione: semafori (named/unnamed), lock, mutex, condition variable. Più i segnali.

| | Shared memory | Message passing |
| --- | --- | --- |
| Kernel coinvolto | solo per creare la zona | a ogni messaggio |
| Velocità | alta | più bassa |
| Sincronizzazione | esplicita | implicita (receive bloccante) |

## Collegamenti

- **Concetti correlati**: [[Shared Memory POSIX]] · [[Pipe e FIFO]] · [[Message Passing]] · [[Socket]] · [[Segnali]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[05 - SDC2 - Comunicazione tra Processi#Processi indipendenti e cooperanti|Lezione 5 — Processi indipendenti e cooperanti]]
> - [[05 - SDC2 - Comunicazione tra Processi#Mappa dei meccanismi IPC in Linux|Lezione 5 — Mappa dei meccanismi IPC in Linux]]
> - [[05 - SDC2 - Comunicazione tra Processi#Modelli di IPC|Lezione 5 — Modelli di IPC]]
