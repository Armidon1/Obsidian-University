---
title: pwn-recvrepeat
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvrepeat
---

# recvrepeat

> [!abstract] In breve
> Raccoglie dati finché una lettura scade o il flusso termina.

## Sintassi e ritorno

- `io.recvrepeat(timeout=0.5)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`

Il timeout è il tempo di inattività atteso per ogni lettura. Un timeout lascia il canale disponibile per altre operazioni.

## Esempio

```python
import sys
from pwn import process

programma = "print('uno')\nprint('due')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvrepeat(timeout=2) == b"uno\ndue\n"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvall|recvall]]
- [Documentazione ufficiale di recvrepeat](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvrepeat)
