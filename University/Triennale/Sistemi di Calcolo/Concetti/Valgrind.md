---
title: Valgrind
tags:
  - sistemi-di-calcolo
  - concetto
  - strumenti
  - debugging
  - memoria
---

# Valgrind

> [!summary] In breve
> `valgrind ./prog` (tool memcheck) rileva accessi non validi alla memoria, uso di valori non inizializzati, memory leak e free non valide; `--track-origins=yes` mostra da dove viene un valore non inizializzato.

- Le righe di Valgrind iniziano con `==PID==`.
- `HEAP SUMMARY` e `LEAK SUMMARY` (definitely/indirectly/possibly lost, still reachable); `--leak-check=full` per i dettagli.
- Un solo bug può generare molti errori: correggere **il primo** e rieseguire.
- Compilare con `-g` per avere i numeri di riga.

## Collegamenti

- **Concetti correlati**: [[GDB]] · [[malloc e free]] · [[Gestione degli Errori in C]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[09 - SDC - Appendici#Valgrind|Lezione 9 — Valgrind]]
