---
title: Driver e Block Device
tags:
  - sistemi-operativi
  - concetto
  - file-system
  - io
  - driver
---

# Driver e Block Device

> [!summary] In breve
> Un driver è una "classe virtuale" che implementa un'interfaccia standard per un dispositivo; i dispositivi di storage implementano la block interface (read/write block), su cui si appoggiano i file system.

- Interfaccia uniforme → portabilità; i driver sono organizzati **a strati** (es. un disco USB usa il driver USB).
- **Partition table** all'inizio del disco.
- Disk driver: la parte bassa offre `read/write block`, la parte alta fa **scheduling** e **caching**; il trasferimento avviene in **DMA**.
- `read block`: si sospende il processo, il disco lavora, l'interrupt lo risveglia e i dati vengono copiati.

## Collegamenti

- **Concetti correlati**: [[Virtual Method Table]] · [[DMA]] · [[Device File e ioctl]] · [[Strutture Dati del File System]] · [[Interrupt]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[12 - SO - File System#Driver e block device|Lezione 12 — Driver e block device]]
> - [[12 - SO - File System#Partizioni e disk controller|Lezione 12 — Partizioni e disk controller]]
