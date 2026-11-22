---
title: pwn-sendlinethen
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendlinethen
---

# sendlinethen

> [!abstract] In breve
> Invia i dati e poi legge fino al delimitatore.

## Sintassi e ritorno

- `io.sendlinethen(delimitatore, dati, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`, oppure `b""` se la lettura va in timeout

Invia una riga con `sendline()`. Poi legge con `recvuntil()`.

## Esempio

```python
import sys
from pwn import process

programma = "input()\nprint('OK')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.sendlinethen(b"OK", b"A") == b"OK"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-sendlineafter|sendlineafter]]
- [Documentazione ufficiale di sendlinethen](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendlinethen)
