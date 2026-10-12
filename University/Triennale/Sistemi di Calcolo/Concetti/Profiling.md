---
title: Profiling
tags:
  - sistemi-di-calcolo
  - concetto
  - prestazioni
  - strumenti
---

# Profiling

> [!summary] In breve
> Misurare dove un programma spende il tempo: instrumentazione manuale con `clock_gettime` (tempo reale) o `getrusage` (tempo di CPU), oppure un profiler come `gprof` (`gcc -pg`, poi `gmon.out`).

- **Tempo reale** (`clock_gettime(CLOCK_MONOTONIC, …)`): preciso, ma include il tempo dato agli altri processi.
- **Tempo di CPU** (`getrusage`: `ru_utime` utente, `ru_stime` sistema): conta solo il processo.
- La durata misurata deve essere **≥ 10 volte** la risoluzione e la latenza della misura; altrimenti si ripete il codice (attenzione: la cache distorce).
- `gprof`: flat profile con `% time`, `self seconds`, `calls`; campionamento ogni 0.01 s.

## Collegamenti

- **Concetti correlati**: [[Speedup e Legge di Amdahl]] · [[Ottimizzazioni del Compilatore]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[05 - SDC - Ottimizzazione dei programmi#Profilazione delle prestazioni|Lezione 5 — Profilazione delle prestazioni]]
> - [[05 - SDC - Ottimizzazione dei programmi#gprof|Lezione 5 — gprof]]
