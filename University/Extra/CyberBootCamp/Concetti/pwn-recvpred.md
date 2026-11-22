---
title: pwn-recvpred
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvpred
---

# recvpred

> [!abstract] In breve
> Legge byte fino a quando una condizione sui dati raccolti è soddisfatta.

## Sintassi e ritorno

- `io.recvpred(controllo, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes`, oppure `b""` al timeout

Il predicato viene provato sui byte accumulati. Durante la lettura può ricevere anche un blocco vuoto.

## Esempio

```python
import sys
from pwn import process

programma = "print('A B C')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvpred(lambda dati: dati.count(b" ") == 2) == b"A B "
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvregex|recvregex]]
- [Documentazione ufficiale di recvpred](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvpred)
