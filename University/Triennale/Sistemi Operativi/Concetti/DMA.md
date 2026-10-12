---
title: DMA
tags:
  - sistemi-operativi
  - concetto
  - hardware
  - io
---

# DMA

> [!summary] In breve
> Direct Memory Access: una periferica trasferisce dati da/verso la memoria senza la CPU, prendendo in prestito il bus; alla fine avvisa la CPU con un interrupt.

- La periferica chiede il bus (`BUSRQ`) e la CPU lo concede (`BUSACK`): servono segnali di **arbitraggio**.
- Durante il trasferimento la CPU non usa il bus, ma può continuare a lavorare grazie alla **cache**.
- Usato dai disk driver: il kernel deve avere **pagine fisiche contigue** disponibili per il buffer.
- Non presente sull'AVR.

## Collegamenti

- **Concetti correlati**: [[Bus di Sistema]] · [[Interrupt]] · [[Driver e Block Device]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#DMA|Lezione 4 — DMA]]
> - [[12 - SO - File System#Partizioni e disk controller|Lezione 12 — Partizioni e disk controller]]
