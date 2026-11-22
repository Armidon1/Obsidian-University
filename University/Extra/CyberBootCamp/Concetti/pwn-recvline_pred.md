---
title: pwn-recvline_pred
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_pred
---

# recvline_pred

> [!abstract] In breve
> Legge fino a una riga che soddisfa una funzione di controllo.

## Sintassi e ritorno

- `io.recvline_pred(controllo, drop=True, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`, oppure `b""` al timeout

La funzione di controllo riceve una riga per volta, comprensiva del terminatore, e decide se accettarla.

## Esempio

```python
import sys
from pwn import process

programma = "print('inizio')\nprint(42)"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    risposta = io.recvline_pred(lambda riga: riga.rstrip().isdigit(), drop=True)
    assert risposta == b"42"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvline_contains|recvline_contains]]
- [Documentazione ufficiale di recvline_pred](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvline_pred)
