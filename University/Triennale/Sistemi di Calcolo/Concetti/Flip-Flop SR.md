---
title: Flip-Flop SR
tags:
  - sistemi-di-calcolo
  - concetto
  - hardware
  - logica
---

# Flip-Flop SR

> [!summary] In breve
> Circuito sequenziale (latch) fatto di due porte NOR in retroazione: memorizza 1 bit. S lo porta a 1, R a 0, senza segnali mantiene lo stato.

| S | R | Q | Q' |
| --- | --- | --- | --- |
| 0 | 0 | invariato | |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | indefinito | |

- **Sequenziale** = ha uno stato (memoria); **combinatorio** = output funzione dei soli input.
- È il mattone dei **registri** della CPU.
- Il clock sincronizza i circuiti sequenziali; la sua frequenza è limitata dalla propagazione del segnale e dal calore.

## Collegamenti

- **Concetti correlati**: [[Porte Logiche]] · [[Circuiti Combinatori e Addizionatori]] · [[Registri IA32]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[01 - SDC - Cosa è un sistema di calcolo#Logica sequenziale e flip-flop|Lezione 1 — Logica sequenziale e flip-flop]]
