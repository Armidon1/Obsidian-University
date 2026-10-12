---
title: Memory Mapped IO
tags:
  - sistemi-operativi
  - concetto
  - hardware
  - io
---

# Memory Mapped IO

> [!summary] In breve
> Le porte di I/O sono registri a indirizzi fissi: leggerli o scriverli è una normale lettura/scrittura in memoria, ma il valore dipende da (o pilota) segnali elettrici esterni.

- Leggere una porta di input = leggere una locazione il cui valore è imposto dall'esterno.
- Scrivere una porta di output = normale scrittura in memoria che pilota dei pin.
- Alternativa: **spazio di I/O separato** (pin `IORQ` dello Z80, istruzioni `in`/`out` di x86), perché l'I/O è più lento.
- Sull'AVR tutte le periferiche (porte, timer, UART) sono **control register** mappati in memoria, già dichiarati in `<avr/io.h>`.
- Per protezione, l'accesso a queste aree è riservato alla modalità privilegiata (vedi [[Dual Mode]]).

## Collegamenti

- **Concetti correlati**: [[Bus di Sistema]] · [[Porte Digitali AVR]] · [[Dual Mode]] · [[Device File e ioctl]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#I/O mappato in memoria|Lezione 4 — I/O mappato in memoria]]
> - [[04 - SO - Hardware e AVR#Periferiche dell'AVR|Lezione 4 — Periferiche dell'AVR]]
