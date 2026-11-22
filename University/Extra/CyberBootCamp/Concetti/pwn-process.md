---
title: pwn-process
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.process.process
---

# process

> [!abstract] In breve
> Avvia un programma locale e restituisce un tube per scambiare byte con esso.

## Sintassi

`process([eseguibile, argomento, ...], timeout=2)`

## Esempio

```python
import sys
from pwn import process

programma = "print('pronto')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvline() == b"pronto\n"
```

Usa una lista per passare l'eseguibile e gli argomenti distintamente. Nell'esempio `-u` chiede a Python di scrivere l'output senza buffer. Il blocco `with` chiude il tube quando termina.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-remote|remote]] · [[pwn-close|close]] · [[pwn-recvline|recvline]]
- [Documentazione ufficiale di process](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.process.process)
