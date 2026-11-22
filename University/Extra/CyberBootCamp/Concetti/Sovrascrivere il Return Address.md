---
title: Sovrascrivere il Return Address
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - buffer-overflow
---

# Sovrascrivere il Return Address

> [!summary] In breve
> Se al posto della spazzatura si mette un indirizzo **valido**, l'overflow non crasha: dirotta l'esecuzione. Il bersaglio classico è una funzione `win()` che stampa la flag (*ret2win*).

```python
payload = b"A"*0x20 + b"B"*8 + p64(e.symbols['win'])
r.sendline(payload)
```
- L'**offset** esatto fino al return address si ricava dal disassemblato (`sub rsp, 0x20` → buffer) o con un *pattern ciclico* (`cyclic`) osservando `rip` al crash in [[pwndbg]].
- Senza una `win()` servono tecniche più potenti: [[Ret2Stack]], [[ROP]].

## Collegamenti

- **Concetti correlati**: [[Buffer Overflow dello Stack]] · [[Ret2Stack]] · [[ROP]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[04 - CB - Binary Exploitation 1#Exploitation: sovrascrivere il return address|Lezione 4 — Exploitation: sovrascrivere il return address]]
