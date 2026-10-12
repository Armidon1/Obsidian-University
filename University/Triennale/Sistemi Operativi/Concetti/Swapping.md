---
title: Swapping
tags:
  - sistemi-operativi
  - concetto
  - memoria
---

# Swapping

> [!summary] In breve
> Spostare temporaneamente un processo intero dalla RAM a un backing store e poi riportarlo; permette di eseguire più processi di quanti ne entrino in RAM, ma con context switch molto costosi.

- Il costo è dominato dal **trasferimento**, proporzionale alla memoria spostata.
- **Roll out / roll in**: si portano fuori prima i processi a bassa priorità.
- Non si può portare fuori un processo con **I/O pendente** (o si usa il double buffering nel kernel).
- Negli OS moderni lo swapping di processi interi è disattivato (si attiva solo sopra una soglia); si swappano **pagine** → demand paging.

## Collegamenti

- **Concetti correlati**: [[Demand Paging]] · [[Memoria Virtuale]] · [[Address Binding]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Swapping|Lezione 10 — Swapping]]
