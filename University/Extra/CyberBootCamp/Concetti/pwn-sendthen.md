---
title: pwn-sendthen
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendthen
---

# sendthen

> [!abstract] In breve
> Invia i dati e poi legge fino al delimitatore.

## Sintassi e ritorno

- `io.sendthen(delimitatore, dati, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`, oppure `b""` se la lettura va in timeout

Invia i byte esatti con `send()`. Poi legge con `recvuntil()`.

## Esempio

```python
import sys
from pwn import process

programma = "import sys\nsys.stdin.buffer.read(1)\nprint('OK')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.sendthen(b"OK", b"A") == b"OK"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-sendafter|sendafter]]
- [Documentazione ufficiale di sendthen](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendthen)
