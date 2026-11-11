---
title: Esportare Dati da IDA
tags:
  - cyberbootcamp
  - concetto
  - reverse-engineering
  - ida
---

# Esportare Dati da IDA

> [!summary] In breve
> Per riusare un array del binario in uno script: tipizzarlo (`Y`, `D`, `*`) e poi esportarlo con `Shift+E` come *initialized C variable*.

1. `Y` → tipo (es. `int matrix[104]`)
2. `D` → dimensione (`db`/`dw`/`dd`/`dq`)
3. `*` → array
4. `Shift+E` → *Export data* → **initialized C variable** → Preview o file

Risultato: `int matrix[104] = { 10, 126, ... };`, pronto per C o Python.

## Collegamenti

- **Concetti correlati**: [[Scorciatoie IDA]] · [[Struct in IDA]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[02 - CB - Reverse Engineering 1#Estrarre i dati|Lezione 2 — Estrarre i dati]]
