---
title: pwn-connected
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.connected
---

# connected

> [!abstract] In breve
> Controlla lo stato del canale in una direzione.

## Sintassi e ritorno

- `io.connected("any")` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bool`

Usa `'send'` per controllare l'invio o `'recv'` per la ricezione. Per sapere se ci sono dati pronti usa `can_recv()`.

## Esempio

```python
import sys
from pwn import process

programma = 'input()'
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.connected("send")
    io.shutdown("send")
    assert not io.connected("send")
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-can_recv|can_recv]]
- [Documentazione ufficiale di connected](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.connected)
