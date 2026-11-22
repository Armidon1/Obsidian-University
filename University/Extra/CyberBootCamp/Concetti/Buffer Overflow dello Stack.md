---
title: Buffer Overflow dello Stack
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - buffer-overflow
---

# Buffer Overflow dello Stack

> [!summary] In breve
> Scrivendo in un buffer locale più byte di quanti ne stia (es. con `gets`, che non controlla la lunghezza), la scrittura tracima sullo stack e sovrascrive `rbp` salvato e **indirizzo di ritorno**. Al `ret` si controlla `rip`.

- Causa tipica: lettura **senza limite** (`gets`, `read`/`scanf` usate male).
- Layout: `[ buffer ][ rbp salvato ][ ret addr ]` (verso indirizzi alti).
- Input `b"A"*32 + b"B"*8 + b"FUCKEDUP"` → `ret` fa `pop rip` su `0x4655434B45445550` → **segfault**: prova che controlliamo `rip`.
- Difesa reale: [[Canary dello Stack]], [[PIE]], [[NX]]. Cfr. [[Buffer Overflow]] (Ethical Hacking).

## Collegamenti

- **Concetti correlati**: [[Sovrascrivere il Return Address]] · [[Stack Frame x86-64]] · [[call e ret]] · [[Buffer Overflow]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[04 - CB - Binary Exploitation 1#Buffer overflow|Lezione 4 — Buffer overflow]]
