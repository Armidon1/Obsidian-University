---
title: Microcontrollore e Bootloader
tags:
  - sistemi-operativi
  - concetto
  - hardware
  - avr
---

# Microcontrollore e Bootloader

> [!summary] In breve
> Un microcontrollore è un computer completo su un chip (CPU, RAM, flash, periferiche) senza OS; il bootloader è un piccolo programma nella flash che permette di caricare nuovi programmi via seriale senza programmer esterno.

- **Tight programming**: affidabilità, basso consumo, niente OS, poca RAM, cross compilation, debugging difficile.
- Per programmare servono: un **cross compiler**, un **programmer** e un'**utility** sul PC (es. PICkit).
- **Bootloader**: all'avvio ascolta sulla seriale; se riceve la sequenza di attivazione, offre un protocollo per scrivere la flash, altrimenti avvia il programma utente.
- Arduino Mega 2560: un secondo chip fa da convertitore USB-seriale e il bootloader rende inutile il programmer.

## Collegamenti

- **Concetti correlati**: [[Toolchain AVR]] · [[UART]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#Microcontrollori|Lezione 4 — Microcontrollori]]
> - [[04 - SO - Hardware e AVR#Il bootloader|Lezione 4 — Il bootloader]]
