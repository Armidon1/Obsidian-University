---
title: pwn-sendlineafter
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendlineafter
---

# sendlineafter

> [!abstract] In breve
> Legge fino al prompt, poi invia una riga.

## Sintassi

`io.sendlineafter(delim, dati, timeout=...)`

## Esempio

```python
import sys
from pwn import process

programma = 'nome = input("Nome? "); print("Ciao, " + nome)'
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.sendlineafter(b"? ", b"Ada") == b"Nome? "
    assert io.recvline() == b"Ciao, Ada\n"
```

La sequenza è `recvuntil` seguita da `sendline`. Il delimitatore viene cercato byte per byte, spazi inclusi. Anche in caso di timeout della lettura il metodo procede con l'invio.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvuntil|recvuntil]] · [[pwn-sendline|sendline]] · [[pwn-sendafter|sendafter]]
- [Documentazione ufficiale di sendlineafter](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendlineafter)
