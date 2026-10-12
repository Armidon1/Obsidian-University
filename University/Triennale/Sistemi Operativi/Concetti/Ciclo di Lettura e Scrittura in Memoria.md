---
title: Ciclo di Lettura e Scrittura in Memoria
tags:
  - sistemi-operativi
  - concetto
  - hardware
---

# Ciclo di Lettura e Scrittura in Memoria

> [!summary] In breve
> La CPU mette l'indirizzo sul bus, attende che si stabilizzi, abbassa RD (o WR dopo aver messo il dato), aspetta il WAIT della memoria e legge/scrive il dato.

**Lettura**: indirizzo sull'address bus → `MREQ` e `RD` bassi → la memoria mette il dato sul data bus (eventualmente segnalando con `WAIT`) → la CPU lo preleva → i segnali tornano alti.

**Scrittura**: indirizzo **e dato** sui bus → `WR` basso → la memoria memorizza il dato → fine del ciclo.

- I segnali vengono abbassati **dopo** che l'indirizzo si è stabilizzato elettricamente.
- La memoria è più lenta della CPU: questo è il motivo degli stati di attesa e degli stalli.

## Collegamenti

- **Concetti correlati**: [[Bus di Sistema]] · [[Memory Mapped IO]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#Ciclo di lettura dalla memoria|Lezione 4 — Ciclo di lettura dalla memoria]]
> - [[04 - SO - Hardware e AVR#Ciclo di scrittura in memoria|Lezione 4 — Ciclo di scrittura in memoria]]
