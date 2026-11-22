---
title: Stack Frame x86-64
tags:
  - cyberbootcamp
  - concetto
  - assembly
  - stack
---

# Stack Frame x86-64

> [!summary] In breve
> Lo **stack** (gestito da `rsp`, cresce verso il basso) contiene variabili locali, `rbp` salvati e indirizzi di ritorno. Ogni funzione attiva ha un **frame** delimitato da `rbp` (base) e `rsp` (cima).

- `push`/`pop` spostano `rsp` (lo stack **cresce verso indirizzi bassi**).
- Prologo/epilogo tipici:

```asm
func:
    push rbp          ; salva rbp del chiamante
    mov  rbp, rsp     ; nuovo frame
    sub  rsp, 0x20    ; spazio per le locali
    ...
    leave             ; mov rsp,rbp ; pop rbp
    ret
```
- Cfr. la stessa idea in [[Stack Frame]] (Sistemi di Calcolo).

## Collegamenti

- **Concetti correlati**: [[Calling Convention]] · [[call e ret]] · [[Buffer Overflow dello Stack]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[03 - CB - Assembly 101#Lo stack|Lezione 3 — Lo stack]]
