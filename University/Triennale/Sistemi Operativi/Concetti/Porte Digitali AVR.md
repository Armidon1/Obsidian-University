---
title: Porte Digitali AVR
tags:
  - sistemi-operativi
  - concetto
  - avr
  - io
---

# Porte Digitali AVR

> [!summary] In breve
> Ogni porta (A–L) è un registro a 8 bit, un bit per pin; si controlla con DDRx (direzione), PORTx (output o pull-up) e PINx (input).

| Registro | Bit = 1 | Bit = 0 |
| --- | --- | --- |
| `DDRx` | output | input |
| `PORTx` | output alto / pull-up attiva (se input) | output basso |
| `PINx` | si legge ~5V | si legge ~0V |

```c
const uint8_t mask = (1<<7);   // PB7 = LED su pin 13
DDRB |= mask;                  // output
PORTB |= mask;                 // acceso
DDRB &= ~(1<<6);               // PB6 input
PORTB |= (1<<6);               // pull-up
int key = (PINB & (1<<6)) == 0;
```

- Mai lasciare pin **flottanti**: si usano resistenze di pull-up/pull-down.
- La corrispondenza tra pin Arduino e coppia porta/bit si legge nel pin mapping.

## Collegamenti

- **Concetti correlati**: [[Memory Mapped IO]] · [[Timer AVR]] · [[Interrupt Esterni AVR]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#Porte digitali|Lezione 4 — Porte digitali]]
> - [[04 - SO - Hardware e AVR#Esempio: LED blink (scrittura su un pin)|Lezione 4 — Esempio: LED blink (scrittura su un pin)]]
> - [[04 - SO - Hardware e AVR#Esempio: lettura da un pin|Lezione 4 — Esempio: lettura da un pin]]
