---
title: pwn-clean
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.clean
---

# clean

> [!abstract] In breve
> Consuma e restituisce i dati accumulati nel canale.

## Sintassi e ritorno

- `io.clean(timeout=0.05)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`

Con `timeout=0` preleva solo i dati nel buffer interno. Con un timeout positivo legge anche dal canale finché una lettura non produce altri dati.

## Esempio

```python
import sys
from pwn import process

programma = "print('pronto')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.can_recv(timeout=2)
    assert io.clean(timeout=0.5) == b"pronto\n"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvrepeat|recvrepeat]]
- [Documentazione ufficiale di clean](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.clean)
