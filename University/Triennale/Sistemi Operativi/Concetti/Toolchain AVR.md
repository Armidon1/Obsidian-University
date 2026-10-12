---
title: Toolchain AVR
tags:
  - sistemi-operativi
  - concetto
  - avr
  - compilazione
---

# Toolchain AVR

> [!summary] In breve
> `avr-gcc` compila in `.elf`, `avr-objcopy` converte in `.hex`, `avrdude` carica il `.hex` tramite il bootloader su `/dev/ttyACM0`.

```bash
avr-gcc -mmcu=atmega2560 -DF_CPU=16000000UL -Wall --std=gnu99 -o p.elf p.c
avr-objcopy -O ihex -R .eeprom p.elf p.hex
avrdude -p m2560 -P /dev/ttyACM0 -c wiring -b 115200 -D -U flash:w:p.hex:i
```

- L'utente deve essere nel gruppo `dialout` per accedere a `/dev/ttyACM0`.
- Con il Makefile del corso basta `make p.hex`.
- Output: `printf_init()` con il wrapper della printf, letto con **cutecom** a 19200 baud, 8N1.

## Collegamenti

- **Concetti correlati**: [[Microcontrollore e Bootloader]] · [[Makefile]] · [[UART]] · [[Loader ed ELF]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#Arduino e toolchain|Lezione 4 — Arduino e toolchain]]
> - [[04 - SO - Hardware e AVR#Compilazione|Lezione 4 — Compilazione]]
> - [[04 - SO - Hardware e AVR#Caricamento tramite bootloader|Lezione 4 — Caricamento tramite bootloader]]
