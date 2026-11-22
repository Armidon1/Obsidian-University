---
title: pwn-wait_for_close
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.wait_for_close
---

# wait_for_close

> [!abstract] In breve
> Attende che il canale si chiuda entro il tempo indicato.

## Sintassi e ritorno

- `io.wait_for_close(timeout=2)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `None`

Il ritorno è lo stesso quando il canale si chiude e quando scade il timeout. Usa `connected()` per controllarne lo stato.

## Esempio

```python
import sys
from pwn import process

programma = 'pass'
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    io.wait_for_close(timeout=2)
    assert not io.connected()
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-connected|connected]]
- [Documentazione ufficiale di wait_for_close](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.wait_for_close)
