---
title: pwn-recvline_contains
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_contains
---

# recvline_contains

> [!abstract] In breve
> Legge fino alla prima riga che contiene uno dei frammenti indicati.

## Sintassi e ritorno

- `io.recvline_contains(b"stato", drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`, oppure `b""` al timeout

Il filtro accetta un frammento o una raccolta di frammenti. Le righe precedenti vengono consumate.

## Esempio

```python
import sys
from pwn import process

programma = "print('inizio')\nprint('stato: pronto')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvline_contains(b"stato", drop=True) == b"stato: pronto"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvline|recvline]]
- [Documentazione ufficiale di recvline_contains](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_contains)
