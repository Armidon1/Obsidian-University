---
title: Sezioni e Segmenti ELF
tags:
  - cyberbootcamp
  - concetto
  - reverse-engineering
  - elf
---

# Sezioni e Segmenti ELF

> [!summary] In breve
> Un ELF ha due viste dello stesso contenuto: le **sezioni** (per linker e analisi) e i **segmenti** (per il loader, con i permessi di memoria).

| Parte | Contenuto |
|---|---|
| ELF header | magic `\x7f ELF`, architettura, entry point |
| Program header table | segmenti → cosa caricare, dove, con quali permessi |
| Section header table | sezioni → `.text`, `.rodata`, `.data`, `.bss`, `.plt`, `.got`, `.init_array` |

- Un segmento può contenere più sezioni.
- `readelf -h` (header), `readelf -l` (segmenti), `readelf -S` (sezioni).

## Collegamenti

- **Concetti correlati**: [[ELF]] · [[GOT e PLT]] · [[init_array e fini_array]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[02 - CB - Reverse Engineering 1#Magic number|Lezione 2 — Magic number]]
> - [[02 - CB - Reverse Engineering 1#Cosa c'è in un binario|Lezione 2 — Cosa c'è in un binario]]
