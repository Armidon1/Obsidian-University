---
title: Address Binding
tags:
  - sistemi-operativi
  - concetto
  - memoria
---

# Address Binding

> [!summary] In breve
> Associazione di istruzioni e dati a indirizzi di memoria: può avvenire a compile time (codice assoluto), a load time (codice rilocabile) o a execution time (serve la MMU).

- Indirizzi: simbolici (sorgente) → rilocabili/etichette (object file) → assoluti (dopo linker/loader).
- Con binding a compile/load time indirizzi logici e fisici **coincidono**; a execution time **differiscono**.
- Solo il binding a execution time permette di spostare i processi (compattazione, swapping).

## Collegamenti

- **Concetti correlati**: [[MMU]] · [[Linking Statico e Dinamico]] · [[Loader ed ELF]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Address binding|Lezione 10 — Address binding]]
