---
title: pwn-recv
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recv
---

# recv

> [!abstract] In breve
> Legge fino al numero di byte richiesto e risponde appena ci sono dati.

## Sintassi

`io.recv(numb, timeout=...)`

## Esempio

```python
import sys
from pwn import process

programma = "print('abc')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    dati = io.recv(2)
    assert 1 <= len(dati) <= 2
    assert b"abc".startswith(dati)
```

La lunghezza richiesta è il massimo. Al timeout restituisce `b''`. Se il canale è chiuso e il buffer è vuoto, solleva `EOFError`.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvn|recvn]] · [[pwn-recvline|recvline]]
- [Documentazione ufficiale di recv](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recv)
