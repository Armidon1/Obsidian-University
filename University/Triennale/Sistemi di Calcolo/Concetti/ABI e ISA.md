---
title: ABI e ISA
tags:
  - sistemi-di-calcolo
  - concetto
  - architettura
  - assembly
---

# ABI e ISA

> [!summary] In breve
> ISA = stato della CPU, formato delle istruzioni e loro effetto (es. IA32, x86-64). ABI = convenzioni binarie tra programmi e librerie (passaggio dei parametri, valore di ritorno, registri da preservare).

| | ISA | ABI |
| --- | --- | --- |
| Cosa definisce | registri, istruzioni, effetti | convenzioni di chiamata, layout dei dati, formato dei binari |
| Esempi | IA32, x86-64, ARM | System V i386, System V AMD64 |
| Chi la stabilisce | il produttore della CPU | sistema operativo e compilatori |

- Le convenzioni sulle funzioni (stack frame, caller/callee-save) **non** fanno parte dell'ISA ma dell'ABI.
- x86-64 estende IA32 ed è retrocompatibile.

## Collegamenti

- **Concetti correlati**: [[Registri IA32]] · [[Convenzioni di Chiamata IA32]] · [[x86-64]] · [[Architettura a Strati]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[01 - SDC - Cosa è un sistema di calcolo#Panoramica del funzionamento|Lezione 1 — Panoramica del funzionamento]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Astrazioni: memoria e ISA|Lezione 3 — Astrazioni: memoria e ISA]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Funzioni|Lezione 3 — Funzioni]]
