---
title: pwn-recvline_startswith
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_startswith
---

# recvline_startswith

> [!abstract] In breve
> Legge fino a una riga che inizia con uno dei prefissi indicati.

## Sintassi e ritorno

- `io.recvline_startswith(b"stato", drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`, oppure `b""` al timeout

Passa una tupla di prefissi per accettarne più di uno. Le righe scartate vengono consumate.

## Esempio

```python
import sys
from pwn import process

programma = "print('inizio')\nprint('stato: pronto')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvline_startswith(b"stato", drop=True) == b"stato: pronto"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvline_contains|recvline_contains]]
- [Documentazione ufficiale di recvline_startswith](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_startswith)
