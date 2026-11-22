---
title: pwn-sendafter
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendafter
---

# sendafter

> [!abstract] In breve
> Legge fino a un delimitatore e invia i byte indicati.

## Sintassi

`io.sendafter(delim, dati, timeout=...)`

## Esempio

```python
import sys
from pwn import process

programma = 'import sys; print("Byte? ", end=""); print(sys.stdin.buffer.read(1).hex())'
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    assert io.sendafter(b"? ", b"\x7f") == b"Byte? "
    assert io.recvline() == b"7f\n"
```

La sequenza è `recvuntil` seguita da `send`. L'invio avviene anche se la lettura va in timeout. Se il prompt è un prerequisito, esegui la lettura separatamente e controlla il risultato prima di inviare.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvuntil|recvuntil]] · [[pwn-send|send]] · [[pwn-sendlineafter|sendlineafter]]
- [Documentazione ufficiale di sendafter](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.sendafter)
