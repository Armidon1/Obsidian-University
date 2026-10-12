---
title: Codifica ASCII
tags:
  - sistemi-di-calcolo
  - concetto
  - codifica
---

# Codifica ASCII

> [!summary] In breve
> Codifica a 7 bit (codici 0–127): 0–31 caratteri di controllo (`\0`, `\t`=9, `\n`=10, `\r`=13), 32–126 caratteri stampabili (spazio=32, '0'=48, 'A'=65, 'a'=97), 127 DEL.

| Carattere | DEC | HEX |
| --- | --- | --- |
| `\0` | 0 | 00 |
| `\n` | 10 | 0A |
| spazio | 32 | 20 |
| `'0'` | 48 | 30 |
| `'A'` | 65 | 41 |
| `'a'` | 97 | 61 |

- `c - '0'` = valore di una cifra; maiuscole e minuscole distano 32 (`0x20`).

## Collegamenti

- **Concetti correlati**: [[Endianness]] · [[Funzioni della libc]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[09 - SDC - Appendici#Appendice A: tabella ASCII a 7 bit|Lezione 9 — Appendice A: tabella ASCII a 7 bit]]
