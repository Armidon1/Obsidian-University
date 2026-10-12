---
title: Stack Frame
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - stack
  - funzioni
---

# Stack Frame

> [!summary] In breve
> Il record di attivazione di una chiamata: parametri, indirizzo di ritorno, %ebp salvato e variabili locali. Con il frame pointer i frame formano una lista collegata percorribile dal debugger (backtrace).

```asm
f:  pushl %ebp          # prologo: salva il frame pointer del chiamante
    movl %esp, %ebp     #          %ebp = frame corrente
    subl $k, %esp       #          spazio per le variabili locali
    ...                 # parametri a 8(%ebp), 12(%ebp)…; locali a -4(%ebp)…
    movl %ebp, %esp
    popl %ebp           # epilogo
    ret
```

- `4(%ebp)` = indirizzo di ritorno, `(%ebp)` = ebp salvato.
- `gcc -fomit-frame-pointer`: niente collegamento, codice più veloce, debugging più difficile.
- Lo stack cresce verso indirizzi bassi.

## Collegamenti

- **Concetti correlati**: [[Convenzioni di Chiamata IA32]] · [[Immagine di Memoria di un Processo]] · [[GDB]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Stack frame e registro EBP|Lezione 3 — Stack frame e registro EBP]]
> - [[06 - SDC - Esecuzione dei programmi#Immagine di memoria di un processo|Lezione 6 — Immagine di memoria di un processo]]
