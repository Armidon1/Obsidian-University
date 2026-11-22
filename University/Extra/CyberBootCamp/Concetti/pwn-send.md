---
title: pwn-send
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.send
---

# send

> [!abstract] In breve
> Scrive nel tube i byte indicati.

## Sintassi

`io.send(dati)`

## Esempio

```python
import sys
from pwn import process

programma = 'import sys; print(sys.stdin.buffer.read(4).hex())'
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    io.send(b"\x00\x01\x02\xff")
    assert io.recvline() == b"000102ff\n"
```

Usalo per un campo binario o quando il protocollo stabilisce già i byte esatti da inviare. La funzione trasmette anche i byte zero.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-sendline|sendline]] · [[pwn-sendafter|sendafter]]
- [Documentazione ufficiale di send](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.send)
