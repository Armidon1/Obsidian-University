---
title: ROP
tags:
  - cyberbootcamp
  - concetto
  - pwn
  - rop
---

# ROP

> [!summary] In breve
> *Return Oriented Programming*: con [[NX]] attivo non si inietta codice, ma si **incollano** pezzi già presenti che finiscono in `ret` (**gadget**, es. `pop rax; ret`). Impilando indirizzi di gadget si costruisce un programma, es. `execve("/bin/sh")`.

- Un `ret` salta a ciò che c'è in cima allo stack: una catena di `gadget_addr` + dati fa eseguire un gadget dopo l'altro.
- Obiettivo shell: `rax=0x3b`, `rdi=&"/bin/sh"`, `rsi=0`, `rdx=0`, `syscall` → si cercano i `pop ...; ret` corrispondenti.
- Trovare i gadget: **`ropper -f ./bin`** (o `ROPgadget`); pwntools ha il modulo `ROP`.

## Collegamenti

- **Concetti correlati**: [[NX]] · [[Ret2Stack]] · [[Shellcode]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[05 - CB - Binary Exploitation 2#ROP — Return Oriented Programming|Lezione 5 — ROP — Return Oriented Programming]]
> - [[05 - CB - Binary Exploitation 2#ROP per una shell|Lezione 5 — ROP per una shell]]
