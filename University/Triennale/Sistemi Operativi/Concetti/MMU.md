---
title: MMU
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - hardware
---

# MMU

> [!summary] In breve
> Memory Management Unit: hardware che traduce a runtime ogni indirizzo logico (generato dalla CPU) in un indirizzo fisico, sollevando un'eccezione se l'accesso non è valido.

- La CPU non vede gli indirizzi fisici: può solo **configurare** la MMU (operazione privilegiata). È questo che garantisce la **protezione**.
- Versione minima: registri **relocation** (base) e **limit**: se `addr < limit` allora `fisico = addr + relocation`, altrimenti trap.
- Versioni evolute: segment table, page table + TLB.
- Configurazioni diverse permettono a ogni processo lo stesso layout logico su memoria fisica diversa.

## Collegamenti

- **Concetti correlati**: [[Address Binding]] · [[Paging]] · [[Segmentazione]] · [[TLB]] · [[Dual Mode]] · [[Memoria Virtuale]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Indirizzi logici e fisici, MMU|Lezione 10 — Indirizzi logici e fisici, MMU]]
> - [[10 - SO - Gestione della Memoria#MMU con registri relocation e limit|Lezione 10 — MMU con registri relocation e limit]]
> - [[10 - SO - Gestione della Memoria#Registri base e limit|Lezione 10 — Registri base e limit]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#MMU: da indirizzi virtuali a fisici|Sistemi di Calcolo, cap. 7 — MMU: da indirizzi virtuali a fisici]]
