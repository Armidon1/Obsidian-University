---
title: pwn-recvn
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvn
---

# recvn

> [!abstract] In breve
> Legge esattamente la quantità richiesta di byte.

## Sintassi

`io.recvn(numb, timeout=...)`

## Esempio

```python
import sys
from pwn import process

programma = "import sys; sys.stdout.buffer.write(b'ABCDEF')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvn(4) == b"ABCD"
    assert io.recvn(2) == b"EF"
```

È adatto a campi di lunghezza fissa. Se scade il timeout, restituisce `b''` e conserva i byte parziali nel buffer. Se il flusso finisce prima di completare il campo, solleva `EOFError`.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recv|recv]] · [[pwn-u32|u32]]
- [Documentazione ufficiale di recvn](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvn)
