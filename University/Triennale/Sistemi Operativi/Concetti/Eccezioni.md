---
title: Eccezioni
tags:
  - sistemi-operativi
  - concetto
  - interrupt
---

# Eccezioni

> [!summary] In breve
> Interrupt generati dal software (dall'istruzione in esecuzione). Su x86: trap (intenzionali, dopo l'istruzione), fault (errori recuperabili, prima: l'istruzione si può rieseguire), abort (irrecuperabili).

| Tipo | Esempi | Dopo l'handler |
| --- | --- | --- |
| **Trap** | `INT` (syscall), breakpoint | istruzione successiva |
| **Fault** | divisione per 0, **page fault**, istruzione illegale | si **riesegue** l'istruzione |
| **Abort** | double fault | il processo termina |

- Sono gestite come gli interrupt: si salvano flag e IP e si salta all'entry del vettore.
- **INT vs CALL**: `INT n` salva flag e IP, salta a un entry point controllato del vettore e **passa in supervisor mode**; `CALL addr` salva solo l'IP, salta a qualunque indirizzo e non cambia modalità.
- Il fault rende possibile il **demand paging**.

## Collegamenti

- **Concetti correlati**: [[Interrupt]] · [[Interrupt Vector]] · [[System Call]] · [[Demand Paging]] · [[Dual Mode]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Eccezioni|Lezione 6 — Eccezioni]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#INT vs CALL|Lezione 6 — INT vs CALL]]
> - [[06 - SDC - Esecuzione dei programmi#Interruzioni|Sistemi di Calcolo, cap. 6 — Interruzioni]]
