---
title: Immagine di Memoria di un Processo
tags:
  - sistemi-operativi
  - concetto
  - processi
  - memoria
---

# Immagine di Memoria di un Processo

> [!summary] In breve
> Layout dello spazio di indirizzi: text, data, rodata, bss, heap (cresce verso l'alto), librerie/mmap, stack (cresce verso il basso); sopra c'è il kernel space.

| Sezione | Permessi | Contenuto |
| --- | --- | --- |
| `.text` | r-x | codice |
| `.rodata` | r-- | costanti, stringhe letterali |
| `.data` | rw- | globali inizializzate |
| `.bss` | rw- | globali azzerate |
| heap | rw- | `malloc` |
| libs / mmap | | librerie condivise, file mappati |
| stack | rw- | record di attivazione (limite `RLIMIT_STACK`) |

- A 32 bit: 3 GB user + 1 GB kernel (da `0xC0000000`).
- Tutti i processi hanno **lo stesso layout** grazie alla memoria virtuale.
- **Stack frame**: parametri, indirizzo di ritorno, FP salvato, variabili locali; FP (`EBP`) punta al frame corrente, SP alla cima.
- Esempio: `int *p = malloc(...)`: `p` sta sullo stack, `*p` nello heap.

## Collegamenti

- **Concetti correlati**: [[Program File e Processo]] · [[Contesto di un Processo]] · [[Memoria Virtuale]] · [[Loader ed ELF]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Immagine di memoria di un processo|Lezione 6 — Immagine di memoria di un processo]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Stack frame|Lezione 6 — Stack frame]]
> - [[05 - SO - Stack e Context Switch#Processo e contesto|Lezione 5 — Processo e contesto]]
