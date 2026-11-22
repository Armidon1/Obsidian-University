---
title: Canary dello Stack
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - mitigations
---

# Canary dello Stack

> [!summary] In breve
> In una funzione protetta, il compilatore dispone un valore sentinella tra il buffer e i dati di controllo del frame. Prima del ritorno il programma lo confronta con il riferimento e chiama `__stack_chk_fail` in caso di differenza.

- La verifica rileva una modifica del valore sentinella al momento del controllo. Una scrittura fuori dai limiti del buffer può danneggiare altri dati anche prima di raggiungere la sentinella.
- **Bypass**: il controllo verifica solo che sia *uguale*. L'ultimo byte è `\x00` (per non trapelare): lo si sovrascrive, `puts` stampa il canary, lo si **parsa**, si **rimette il `\x00`** e si rispedisce intatto nell'overflow completo.
- La dimensione del campo e il numero di bit casuali sono proprietà distinte.
- pwndbg: comando `canary`.

## Collegamenti

- **Concetti correlati**: [[Buffer Overflow dello Stack]] · [[PIE]] · [[NX]] · [[Stack Canary]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[05 - CB - Binary Exploitation 2#Stack canary|Lezione 5 — Stack canary]]
> - [[05 - CB - Binary Exploitation 2#Aggirare il canary: il leak|Lezione 5 — Aggirare il canary: il leak]]
