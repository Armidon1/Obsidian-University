---
title: init_array e fini_array
tags:
  - cyberbootcamp
  - concetto
  - reverse-engineering
  - elf
---

# init_array e fini_array

> [!summary] In breve
> Sezioni ELF con puntatori a funzione eseguiti prima (`.init_array`) e dopo (`.fini_array`) `main`; voci in più rispetto al default indicano codice nascosto.

```c
void init() __attribute__((constructor));
void fini() __attribute__((destructor));
```

| Sezione | Voce di default |
|---|---|
| `.init_array` | `frame_dummy` |
| `.fini_array` | `__do_global_dtors_aux` |

- In IDA: `Ctrl+S` → `.init_array`.
- Nelle challenge: controllo della flag o modifica dei dati nascosta fuori da `main`.

## Collegamenti

- **Concetti correlati**: [[Avvio di un Binario ELF]] · [[Sezioni e Segmenti ELF]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[02 - CB - Reverse Engineering 1#Costruttori e distruttori globali|Lezione 2 — Costruttori e distruttori globali]]
> - [[02 - CB - Reverse Engineering 1#In pratica|Lezione 2 — In pratica]]
