---
title: Interrupt Esterni AVR
tags:
  - sistemi-operativi
  - concetto
  - avr
  - interrupt
---

# Interrupt Esterni AVR

> [!summary] In breve
> INTn: un interrupt per uno specifico pin, configurabile su fronte di salita/discesa; PCINTn: un interrupt condiviso da tutti i pin di una porta, che scatta a ogni cambio di stato.

| | INTn | PCINTn |
| --- | --- | --- |
| Legato a | un pin | una porta (un gruppo di pin) |
| Trigger | rising, falling, entrambi, livello basso (`EICRA`/`EICRB`) | qualunque cambio di stato |
| Abilitazione | bit `INTn` in `EIMSK` | bit `PCIEk` in `PCICR` e i bit dei pin in `PCMSKk` |
| Handler | `ISR(INTn_vect)` | `ISR(PCINTk_vect)`: bisogna capire quale pin è cambiato confrontando `PINx` con lo stato precedente |

- **Rising edge** = 0 → 1, **falling edge** = 1 → 0.
- I contatti meccanici "rimbalzano" (**bouncing**) e generano interrupt multipli.

## Collegamenti

- **Concetti correlati**: [[Interrupt]] · [[Porte Digitali AVR]] · [[Interrupt Vector]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#Interrupt esterni|Lezione 4 — Interrupt esterni]]
> - [[04 - SO - Hardware e AVR#Esempio INTn|Lezione 4 — Esempio INTn]]
> - [[04 - SO - Hardware e AVR#Esempio PCINTn|Lezione 4 — Esempio PCINTn]]
