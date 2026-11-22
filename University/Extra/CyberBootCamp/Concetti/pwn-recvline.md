---
title: pwn-recvline
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline
---

# recvline

> [!abstract] In breve
> Legge una riga usando il fine riga configurato nel tube.

## Sintassi

`io.recvline(drop=False, timeout=...)`

## Esempio

```python
import sys
from pwn import process

programma = "print('uno'); print('due ')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvline() == b"uno\n"
    assert io.recvline(drop=True) == b"due "
```

Il fine riga predefinito è `b'\n'`. `drop=True` lo rimuove lasciando gli spazi. Con le impostazioni predefinite, una chiusura può restituire una riga incompleta se ci sono ancora byte nel buffer.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvuntil|recvuntil]] · [[pwn-sendline|sendline]]
- [Documentazione ufficiale di recvline](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline)
