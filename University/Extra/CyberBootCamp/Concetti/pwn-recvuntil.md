---
title: pwn-recvuntil
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvuntil
---

# recvuntil

> [!abstract] In breve
> Legge fino alla prima occorrenza di un delimitatore.

## Sintassi

`io.recvuntil(delim, drop=False, timeout=...)`

## Esempio

```python
import sys
from pwn import process

programma = "print('Nome? ', end='')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvuntil(b"? ", drop=True) == b"Nome"
```

Lo spazio in `b'? '` fa parte del delimitatore. `drop=True` lo toglie dal risultato. Al timeout la funzione restituisce `b''` e conserva nel buffer i byte parziali.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvline|recvline]] · [[pwn-sendlineafter|sendlineafter]]
- [Documentazione ufficiale di recvuntil](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvuntil)
