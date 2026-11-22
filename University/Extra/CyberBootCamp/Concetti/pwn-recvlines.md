---
title: pwn-recvlines
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvlines
---

# recvlines

> [!abstract] In breve
> Legge fino al numero di righe indicato.

## Sintassi e ritorno

- `io.recvlines(numero_righe, drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `list[bytes]`

Con `drop=True` rimuove il fine riga. Al timeout restituisce le righe già raccolte, eventualmente una lista vuota.

## Esempio

```python
import sys
from pwn import process

programma = "print('uno')\nprint('due')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvlines(2, drop=True) == [b"uno", b"due"]
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvline|recvline]]
- [Documentazione ufficiale di recvlines](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvlines)
