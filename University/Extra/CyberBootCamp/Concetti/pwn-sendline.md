---
title: pwn-sendline
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendline
---

# sendline

> [!abstract] In breve
> Invia i byte e aggiunge il fine riga del tube.

## Sintassi

`io.sendline(dati)`

## Esempio

```python
import sys
from pwn import process

programma = 'nome = input("Nome? "); print("Ciao, " + nome)'
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.recvuntil(b"? ") == b"Nome? "
    io.sendline(b"Ada")
    assert io.recvline() == b"Ciao, Ada\n"
```

Il fine riga predefinito è `b'\n'`. Il metodo è adatto a programmi che leggono una riga di input completa.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-send|send]] · [[pwn-sendlineafter|sendlineafter]] · [[pwn-recvline|recvline]]
- [Documentazione ufficiale di sendline](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendline)
