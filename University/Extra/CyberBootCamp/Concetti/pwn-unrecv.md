---
title: pwn-unrecv
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.unrecv
---

# unrecv

> [!abstract] In breve
> Rimette byte all'inizio del buffer di ricezione.

## Sintassi e ritorno

- `io.unrecv(dati)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `None`

La prossima lettura vede prima i byte rimessi nel buffer. Puoi usarlo se hai letto un prefisso per determinare come interpretare il messaggio.

## Esempio

```python
import sys
from pwn import process

programma = "print('ABC')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    prefisso = io.recvn(1)
    io.unrecv(prefisso)
    assert io.recvline(drop=True) == b"ABC"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recv|recv]]
- [Documentazione ufficiale di unrecv](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.unrecv)
