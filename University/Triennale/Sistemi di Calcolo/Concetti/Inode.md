---
title: Inode
tags:
  - sistemi-di-calcolo
  - concetto
  - file-system
---

# Inode

> [!summary] In breve
> Struttura che descrive un file Unix (tipo, permessi, numero di hard link, UID/GID, dimensione, tempi, puntatori ai blocchi diretti e indiretti), ma non il nome, che sta nelle directory come coppia (nome, inode).

- Blocchi da 4096 byte e indici da 4 byte → 1024 indici per blocco.
- 12 diretti + indiretto singolo + indiretto doppio: $(12 + 1024 + 1024^2) \cdot 4096 \approx 4$ GiB; con il triplo > 16 TiB.
- Il file più piccolo occupa comunque **un blocco**.
- `ls -i` mostra il numero di inode, `stat` i suoi campi (`Links`, `Blocks` in unità da 512 B).
- Tabella dei descrittori del processo → tabella dei file aperti (posizione, modalità, inode) → inode.

## Collegamenti

- **Concetti correlati**: [[File System]] · [[Link Hard e Soft]] · [[File Descriptor]] · [[Strutture Dati del File System]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[08 - SDC - Gestione dei file#Inode e blocchi|Lezione 8 — Inode e blocchi]]
> - [[08 - SDC - Gestione dei file#Tabella dei descrittori di file di un processo|Lezione 8 — Tabella dei descrittori di file di un processo]]
