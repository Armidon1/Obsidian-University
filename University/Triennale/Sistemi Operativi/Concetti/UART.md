---
title: UART
tags:
  - sistemi-operativi
  - concetto
  - avr
  - io
  - seriale
---

# UART

> [!summary] In breve
> Universal Asynchronous Receiver-Transmitter: invia ogni byte incorniciato da start/stop bit a un baud rate concordato; si controlla con UDRn (dati), UBRRn (velocità), UCSRnA/B/C (stato e configurazione).

- Fili: **GND, TX, RX**. Comunicazione asincrona, quindi frame = start + 8 dati (+ parità) + stop: 10 bit per byte (8N1).
- `UBRR = F_CPU/16/BAUD - 1`.
- `UCSR0C = (1<<UCSZ01)|(1<<UCSZ00)`: 8 bit di dati. `UCSR0B = (1<<RXEN0)|(1<<TXEN0)|(1<<RXCIE0)`: abilita RX, TX e interrupt di ricezione.
- **putChar**: attende `UDRE0` = 1, poi scrive `UDR0`. **getChar**: attende `RXC0` = 1, poi legge `UDR0`.
- Versione a interrupt: le ISR di RX/TX riempiono e svuotano dei buffer circolari (come fa un driver).
- Lato PC compare come `/dev/ttyACM0`, un **character device**.

## Collegamenti

- **Concetti correlati**: [[Memory Mapped IO]] · [[Interrupt]] · [[Device File e ioctl]] · [[Toolchain AVR]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#UART: la porta seriale|Lezione 4 — UART: la porta seriale]]
> - [[04 - SO - Hardware e AVR#Esempio: funzioni base su UART0|Lezione 4 — Esempio: funzioni base su UART0]]
