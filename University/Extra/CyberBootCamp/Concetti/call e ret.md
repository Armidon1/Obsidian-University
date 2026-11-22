---
title: call e ret
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - stack
---

# call e ret

> [!summary] In breve
> `call f` trasferisce il controllo a `f`: salva sullo stack l'**indirizzo di ritorno**. `ret` ≡ `pop rip`: ci ritorna. Poiché `ret` salta a ciò che trova in cima allo stack, controllare lo stack = controllare `rip`.

```
call <func>  :=  push indirizzo_successivo ; jmp <func>
ret          :=  pop rip
```
- `rip` non è scrivibile con `mov`: avanza della lunghezza dell’istruzione durante l’esecuzione sequenziale. Chiamate, salti e ritorni trasferiscono il controllo.
- L'indirizzo di ritorno sta sullo stack → un [[Buffer Overflow dello Stack|overflow]] lo sovrascrive. È la base di tutto l'exploitation.

## Collegamenti

- **Concetti correlati**: [[Stack Frame x86-64]] · [[Buffer Overflow dello Stack]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[04 - CB - Binary Exploitation 1#Come funzionano call e ret|Lezione 4 — Come funzionano call e ret]]
> - [[03 - CB - Assembly 101#Lo stack|Lezione 3 — Lo stack]]
