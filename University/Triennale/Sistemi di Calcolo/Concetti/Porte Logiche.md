---
title: Porte Logiche
tags:
  - sistemi-di-calcolo
  - concetto
  - hardware
  - elettronica
---

# Porte Logiche

> [!summary] In breve
> Circuiti elementari che calcolano funzioni booleane (AND, OR, NOT, XOR, NOR), realizzati con transistor usati come interruttori comandati.

| X | Y | AND | OR | XOR | NOR |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

- NOT inverte. Precedenza: **NOT > AND > OR**.
- Transistor NPN: corrente sulla base → collettore ed emettitore collegati. **AND** = transistor in serie, **OR** = in parallelo, **NOT** = il transistor cortocircuita il LED a massa.
- XOR = `NOT X AND Y OR X AND NOT Y`.
- VLSI: circa 17 milioni di transistor per mm², circa 3 miliardi in una CPU.

## Collegamenti

- **Concetti correlati**: [[Circuiti Combinatori e Addizionatori]] · [[Flip-Flop SR]] · [[Macchina di Von Neumann]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[01 - SDC - Cosa è un sistema di calcolo#Porte logiche|Lezione 1 — Porte logiche]]
> - [[09 - SDC - Appendici#Transistor|Lezione 9 — Transistor]]
