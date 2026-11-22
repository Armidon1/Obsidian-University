---
title: pwn-stream
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.stream
---

# stream

> [!abstract] In breve
> Stampa l'output del canale man mano che arriva.

## Sintassi e ritorno

- `io.stream(line_mode=True)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes` con tutti i dati stampati

Con `line_mode=True` stampa per righe. Con `False` stampa blocchi di dati mentre li riceve.

## Esempio

```python
import sys
from pwn import process

programma = "print('pronto')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.stream() == b"pronto\n"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvall|recvall]]
- [Documentazione ufficiale di stream](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.stream)
