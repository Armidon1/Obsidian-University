---
title: Network Adapter e Driver
tags:
  - sistemi-di-calcolo-2
  - concetto
  - reti
  - hardware
  - driver
---

# Network Adapter e Driver

> [!summary] In breve
> La scheda di rete (bus interface + link interface collegate da FIFO, comandate dalla SCO) comunica con la CPU tramite i registri CSR; i frame passano in DMA tramite una buffer descriptor list.

- CSR: `LE_TDMD` (richiesta di trasmissione), `LE_INEA` (abilita gli interrupt), `LE_TINT` (trasmissione completata), `LE_RINT` (frame ricevuto).
- Notifica: busy waiting o interrupt. Trasferimento: DMA o programmed I/O.
- BD list: es. 64 buffer da 1500 byte; scatter read / gather write.
- Il driver usa un semaforo contatore `xmit_queue` (64) e un `mutex`; l'interrupt handler a fine trasmissione fa `semsignal(xmit_queue)`.

## Collegamenti

- **Concetti correlati**: [[DMA]] · [[Interrupt]] · [[Semafori]] · [[Driver e Block Device]] · [[Socket]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[07 - SDC2 - Socket#Network adapter|Lezione 7 — Network adapter]]
> - [[07 - SDC2 - Socket#CSR|Lezione 7 — CSR]]
> - [[07 - SDC2 - Socket#Buffer descriptor list|Lezione 7 — Buffer descriptor list]]
> - [[07 - SDC2 - Socket#Il device driver|Lezione 7 — Il device driver]]
