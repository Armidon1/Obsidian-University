---
title: pwn-recvall
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvall
---

# recvall

> [!abstract] In breve
> Raccoglie l'output rimanente fino a fine flusso e chiude il tube.

## Sintassi

`io.recvall(timeout=...)`

## Esempio

```python
import sys
from pwn import process

programma = "print('prima'); print('seconda')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    dati = io.recvall(timeout=2)
    assert dati == b"prima\nseconda\n"
```

È adatto a un processo che stampa il risultato e termina. Senza timeout esplicito può aspettare indefinitamente. Un timeout può restituire solo i dati arrivati fino a quel momento e il tube viene comunque chiuso.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvline|recvline]] · [[pwn-close|close]]
- [Documentazione ufficiale di recvall](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvall)
