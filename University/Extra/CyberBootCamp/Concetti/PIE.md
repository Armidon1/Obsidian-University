---
title: PIE
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - mitigations
---

# PIE

> [!summary] In breve
> Un *position-independent executable* può essere caricato a basi diverse mantenendo le distanze relative interne. Quando ASLR è attivo, il sistema può scegliere una base diversa a ciascun avvio.

- Randomizzare ogni indirizzo singolarmente romperebbe `rip++`; invece **lo stesso offset** si somma a tutto, mantenendo gli offset relativi.
- Formula: `indirizzo reale = rand + offset` (l'offset è l'indirizzo base-0 visto in IDA).
- Con un leak si ricava `rand`, poi ogni indirizzo è `rand + offset_simbolo`. In pwntools: `e.address = base`.
- pwndbg: comando `pie`.

## Collegamenti

- **Concetti correlati**: [[Canary dello Stack]] · [[NX]] · [[Sovrascrivere il Return Address]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[05 - CB - Binary Exploitation 2#PIE|Lezione 5 — PIE]]
> - [[05 - CB - Binary Exploitation 2#Aggirare PIE: la formula|Lezione 5 — Aggirare PIE: la formula]]
