---
title: Endianness
tags:
  - sistemi-di-calcolo
  - concetto
  - memoria
  - architettura
---

# Endianness

> [!summary] In breve
> Ordine dei byte di un valore in memoria: big-endian mette per primo (all'indirizzo più basso) il byte più significativo, little-endian il meno significativo. x86 è little-endian.

`0x12345678` all'indirizzo `0x100`:

| Indirizzo | 0x100 | 0x101 | 0x102 | 0x103 |
| --- | --- | --- | --- | --- |
| big-endian | 12 | 34 | 56 | 78 |
| little-endian | 78 | 56 | 34 | 12 |

- Big-endian: PowerPC, SPARC (e l'ordine dei protocolli di rete). Little-endian: x86, ARM (di solito).
- Nei dump di gdb/objdump gli interi x86 appaiono "al contrario".

## Collegamenti

- **Concetti correlati**: [[Registri IA32]] · [[Codifica ASCII]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Endianness|Lezione 3 — Endianness]]
> - [[04 - SDC - Librerie standard del C#File binari: fwrite e fread|Lezione 4 — File binari: fwrite e fread]]
