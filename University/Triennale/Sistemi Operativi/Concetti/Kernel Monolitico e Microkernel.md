---
title: Kernel Monolitico e Microkernel
tags:
  - sistemi-operativi
  - concetto
  - kernel
---

# Kernel Monolitico e Microkernel

> [!summary] In breve
> Due modi di strutturare un kernel: tutto in kernel mode in un unico programma (monolitico), oppure un nucleo minimo con i servizi in moduli meno privilegiati (microkernel).

| | Monolitico | Microkernel |
| --- | --- | --- |
| **Cosa gira in kernel mode** | tutto: FS, IPC, I/O, memoria virtuale, processi | solo il nucleo: memoria, processi, IPC |
| **Comunicazione interna** | chiamate di funzione | messaggi tra server |
| **Pro** | veloce | robusto e modulare (un server che crasha si riavvia) |
| **Contro** | un bug in un driver può bloccare tutto il sistema | overhead dovuto ai messaggi |
| **Esempi** | Linux | Minix, QNX |

## Collegamenti

- **Concetti correlati**: [[Sistema Operativo]] · [[Dual Mode]] · [[Driver e Block Device]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[01 - SO - Introduzione e Git#Strutture moderne di kernel|Lezione 1 — Strutture moderne di kernel]]
