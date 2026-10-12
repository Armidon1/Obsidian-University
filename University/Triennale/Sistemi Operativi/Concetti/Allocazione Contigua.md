---
title: Allocazione Contigua
tags:
  - sistemi-operativi
  - concetto
  - memoria
---

# Allocazione Contigua

> [!summary] In breve
> Ogni processo occupa un intervallo contiguo di memoria fisica; i buchi liberi si assegnano con first-fit, best-fit o worst-fit. Soffre di frammentazione esterna.

- **First-fit**: il primo buco abbastanza grande (veloce).
- **Best-fit**: il buco più piccolo tra quelli sufficienti.
- **Worst-fit**: il buco più grande (il peggiore in pratica).
- **Compattazione**: si spostano i processi per riunire la memoria libera (serve rilocazione dinamica, ed è costosa).

## Collegamenti

- **Concetti correlati**: [[Frammentazione]] · [[MMU]] · [[Paging]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Allocazione contigua: partizioni multiple|Lezione 10 — Allocazione contigua: partizioni multiple]]
