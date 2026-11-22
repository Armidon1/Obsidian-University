---
title: pwn-recvline_endswith
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_endswith
---

# recvline_endswith

> [!abstract] In breve
> Legge fino a una riga che termina con uno dei suffissi indicati.

## Sintassi e ritorno

- `io.recvline_endswith(b"OK", drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`, oppure `b""` al timeout

Il confronto con il suffisso avviene sul contenuto della riga. Imposta `drop=True` per escludere il terminatore dal risultato.

## Esempio

```python
import sys
from pwn import process

programma = "print('inizio')\nprint('stato: OK')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvline_endswith(b"OK", drop=True) == b"stato: OK"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvline_contains|recvline_contains]]
- [Documentazione ufficiale di recvline_endswith](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_endswith)
