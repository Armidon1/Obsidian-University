---
title: Sistemi Operativi per IoT
tags:
  - sistemi-di-calcolo-2
  - concetto
  - iot
  - embedded
---

# Sistemi Operativi per IoT

> [!summary] In breve
> I dispositivi vincolati (KB di RAM, batteria, niente MMU) richiedono OS minimi come TinyOS, RIOT, µClinux: memoria ridotta, hardware eterogeneo, rete a basso consumo, efficienza energetica, real time, sicurezza.

- Reti: IEEE 802.15.4 (ZigBee), BLE, 6LoWPAN, CoAP, RPL, LoRaWAN.
- Struttura: hardware → HAL (GPIO, UART, SPI, I2C) → kernel → stack di rete e driver → librerie → applicazioni.

| | µClinux | TinyOS | RIOT |
| --- | --- | --- | --- |
| RAM | < 32 MB | < 1 kB | ~1.5 kB |
| C/C++ | sì | no (nesC) | sì |
| Real time | parziale | no | sì |

## Collegamenti

- **Concetti correlati**: [[Internet of Things]] · [[MMU]] · [[Scheduling Real-Time]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[09 - SDC2 - Internet of Things#Dispositivi vincolati e sistemi operativi|Lezione 9 — Dispositivi vincolati e sistemi operativi]]
