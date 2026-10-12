---
title: Bus di Sistema
tags:
  - sistemi-operativi
  - concetto
  - hardware
---

# Bus di Sistema

> [!summary] In breve
> Gruppi di fili condivisi tra CPU, memoria e periferiche: data bus (dati), address bus (indirizzo), control bus (lettura/scrittura, interrupt, arbitraggio).

| Bus | Contenuto |
| --- | --- |
| **Data** | dati letti/scritti (bidirezionale) |
| **Address** | indirizzo della cella (di solito scritto dalla CPU) |
| **Control** | `RD`, `WR`, `MREQ`, `IORQ`, `WAIT`, `INT`, `BUSRQ`/`BUSACK` |

- Le periferiche si presentano alla CPU come **celle di memoria con un indirizzo**.
- Un segnale con la barra sopra ($\overline{RD}$) è **attivo basso**.
- Il **clock** (onda quadra) sincronizza tutti i dispositivi.
- Architettura PC classica: CPU → Northbridge (memoria, grafica) → Southbridge (dischi, USB, PCI, Super I/O).

## Collegamenti

- **Concetti correlati**: [[Ciclo di Lettura e Scrittura in Memoria]] · [[Memory Mapped IO]] · [[DMA]] · [[Interrupt]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#CPU e bus|Lezione 4 — CPU e bus]]
> - [[04 - SO - Hardware e AVR#Esempio: una CPU a 8 bit (Z80)|Lezione 4 — Esempio: una CPU a 8 bit (Z80)]]
> - [[01 - SO - Introduzione e Git#Organizzazione di un computer|Lezione 1 — Organizzazione di un computer]]
