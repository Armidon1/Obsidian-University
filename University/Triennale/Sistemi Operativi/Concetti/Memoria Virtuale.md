---
title: Memoria Virtuale
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - memoria-virtuale
---

# Memoria Virtuale

> [!summary] In breve
> Separa la memoria logica da quella fisica: un processo può girare con solo una parte delle pagine in RAM, quindi lo spazio logico può superare la memoria fisica e si possono eseguire più processi.

- Vantaggi: programmi non limitati dalla RAM, più multiprogrammazione, meno I/O al caricamento, condivisione (librerie, COW).
- Layout: stack in alto che cresce verso il basso, heap che cresce verso l'alto; lo spazio in mezzo non costa nulla finché non viene usato.
- Si implementa con **demand paging** (o demand segmentation).

## Collegamenti

- **Concetti correlati**: [[Demand Paging]] · [[Paging]] · [[Copy on Write]] · [[Page Replacement]] · [[MMU]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[11 - SO - Memoria Virtuale#Perché la memoria virtuale|Lezione 11 — Perché la memoria virtuale]]
> - [[11 - SO - Memoria Virtuale#Lo spazio di indirizzi virtuale|Lezione 11 — Lo spazio di indirizzi virtuale]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Memoria fisica e memoria virtuale|Sistemi di Calcolo, cap. 7 — Memoria fisica e memoria virtuale]]
