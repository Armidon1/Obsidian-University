---
title: pwn-settimeout
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.settimeout
---

# settimeout

> [!abstract] In breve
> Imposta il tempo d'attesa predefinito per le letture del tube.

## Sintassi

`io.settimeout(secondi)`

## Esempio

```python
import sys
from pwn import process

programma = 'import time; time.sleep(1)'
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    io.settimeout(0.05)
    assert io.recv(1) == b""
```

Le singole letture possono specificare un proprio `timeout`. Passa `'default'` per tornare a `context.timeout` oppure `None` per attendere senza limite.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recv|recv]] · [[pwn-recvuntil|recvuntil]]
- [Documentazione ufficiale di settimeout](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.settimeout)
