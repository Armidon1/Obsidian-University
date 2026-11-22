---
title: pwn-close
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.close
---

# close

> [!abstract] In breve
> Chiude un tube e rilascia le risorse del processo o della connessione.

## Sintassi

`io.close()`

## Esempio

```python
import sys
from pwn import process

io = process([sys.executable, "-c", "print('pronto')"], timeout=2)
try:
    assert io.recvline() == b"pronto\n"
finally:
    io.close()
```

Un blocco `with process(...) as io` chiude il tube automaticamente all'uscita. Usa `close()` quando gestisci il ciclo di vita del canale in modo esplicito.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-process|process]] · [[pwn-recvall|recvall]]
- [Documentazione ufficiale di close](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.close)
