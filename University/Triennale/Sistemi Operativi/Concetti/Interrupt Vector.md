---
title: Interrupt Vector
tags:
  - sistemi-operativi
  - concetto
  - interrupt
---

# Interrupt Vector

> [!summary] In breve
> Array di puntatori a funzione (gli indirizzi delle ISR), indicizzato dal numero dell'interrupt o dell'eccezione.

| ID | ISR |
| --- | --- |
| 0 (reset) | ADR 0 |
| 1 (seriale) | ADR 1 |
| 2 (trap) | ADR 2 |
| … | … |

- Più interrupt possono condividere la stessa ISR.
- C'è una entry per ogni tipo di evento, eccezioni comprese.
- Deve essere modificabile **solo in modalità privilegiata**, altrimenti un programma utente potrebbe dirottare il kernel.
- Solo alcune entry (es. `0x80`) sono invocabili da user mode con `INT`.

## Collegamenti

- **Concetti correlati**: [[Interrupt]] · [[Puntatori a Funzione]] · [[Eccezioni]] · [[System Call]] · [[Dual Mode]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Interrupt vector|Lezione 6 — Interrupt vector]]
> - [[04 - SO - Hardware e AVR#Interrupt|Lezione 4 — Interrupt]]
