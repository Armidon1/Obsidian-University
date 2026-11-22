---
title: Ret2Stack
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - shellcode
---

# Ret2Stack

> [!summary] In breve
> Si fa tornare il programma a un indirizzo **sullo stack** dove abbiamo scritto dello [[Shellcode|shellcode]]: la CPU esegue il nostro codice. Richiede un **leak** di un indirizzo dello stack.

- Passi: leak di un indirizzo dello stack (dal `rbp` leakato) → `shellcode + padding + p64(indirizzo_stack)` → al `ret` parte lo shellcode.
- Utile quando **non esiste una `win()`**.
- Mitigato da [[NX]] (stack non eseguibile) → si passa a [[ROP]].

## Collegamenti

- **Concetti correlati**: [[Shellcode]] · [[NX]] · [[ROP]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[05 - CB - Binary Exploitation 2#Ret2Stack: eseguire codice proprio|Lezione 5 — Ret2Stack: eseguire codice proprio]]
