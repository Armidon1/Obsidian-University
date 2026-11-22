---
title: pwn-interactive
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.interactive
---

# interactive

> [!abstract] In breve
> Collega il tube al terminale per leggere e scrivere a mano.

## Sintassi

`io.interactive()`

## Esempio

```python
import sys
from pwn import process

programma = 'nome = input("Nome? "); print("Ciao, " + nome)'
with process([sys.executable, "-u", "-c", programma]) as io:
    io.interactive()
```

Esegui lo script da un terminale, digita un nome e premi Invio. Il terminale mostra la risposta del processo. Per verificare la risposta con un'asserzione, leggila con [[pwn-recvline|recvline]].

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-process|process]] · [[pwn-sendline|sendline]] · [[pwn-recvline|recvline]]
- [Documentazione ufficiale di interactive](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.interactive)
