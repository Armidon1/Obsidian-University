---
title: pwn-can_recv
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.can_recv
---

# can_recv

> [!abstract] In breve
> Controlla se il canale ha dati pronti da leggere entro il tempo indicato. Il controllo lascia i dati disponibili per la lettura successiva.

## Sintassi

`io.can_recv(timeout=0)` si usa su un tube ottenuto da `process(...)` o `remote(...)`. Con `timeout=0` il controllo è immediato. Il risultato è un booleano.

## Esempio

```python
import sys
from pwn import process

with process([sys.executable, "-u", "-c", "print('pronto')"], timeout=2) as io:
    assert io.can_recv(timeout=2)
    assert io.recvline() == b"pronto\n"
```

Il controllo riguarda la disponibilità di dati. Per aspettare una riga completa serve `recvline()` con il proprio timeout.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recv|recv]] · [[pwn-recvline|recvline]]
- [Documentazione ufficiale di can_recv](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.can_recv)
