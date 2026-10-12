---
title: ucontext
tags:
  - sistemi-operativi
  - concetto
  - linguaggio-c
  - context-switch
  - coroutine
---

# ucontext

> [!summary] In breve
> Libreria della libc per gestire esplicitamente i contesti in user space (coroutine): `getcontext`, `setcontext`, `makecontext`, `swapcontext` su `ucontext_t`.

| Funzione | Effetto |
| --- | --- |
| `getcontext(&c)` | salva il contesto corrente in `c` |
| `setcontext(&c)` | salta a `c` (non ritorna) |
| `makecontext(&c, f, argc, ...)` | prepara `c` per partire da `f` (serve uno stack proprio: `uc_stack`) |
| `swapcontext(&old, &new)` | salva in `old` e salta a `new` |

- Campi di `ucontext_t`: `uc_link` (contesto a cui tornare quando la funzione finisce), `uc_sigmask` (segnali bloccati), `uc_stack` (`ss_sp`, `ss_size`, `ss_flags`), `uc_mcontext` (registri, tipo opaco e dipendente dall'architettura).
- Da solo realizza **multitasking cooperativo**; combinato con `SIGALRM` diventa preemptive ([[disastrOS]]).
- Le variabili globali **non** vengono ripristinate: il contesto contiene solo registri e stack.

## Collegamenti

- **Concetti correlati**: [[Contesto di un Processo]] · [[Context Switch]] · [[disastrOS]] · [[Segnali]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[05 - SO - Stack e Context Switch#La libreria ucontext|Lezione 5 — La libreria ucontext]]
> - [[08 - SO - disastrOS#Parte B: un preemptive scheduler in user space|Lezione 8 — Parte B: un preemptive scheduler in user space]]
