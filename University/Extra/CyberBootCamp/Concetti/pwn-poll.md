---
title: pwn-poll
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes/processes.html#pwnlib.tubes.process.process.poll
---

# poll

> [!abstract] In breve
> Controlla lo stato di un processo locale. Restituisce il codice di uscita se il processo è terminato, altrimenti restituisce `None`.

## Sintassi

`io.poll(block=False)` si usa su un oggetto creato con `process(...)`. Con `block=True` attende che il processo termini e poi restituisce il codice.

## Esempio

```python
import sys
from pwn import process

with process([sys.executable, "-c", "raise SystemExit(3)"]) as io:
    assert io.poll(block=True) == 3
```

`poll()` controlla la terminazione del processo. Per leggere ciò che ha scritto usa un metodo di ricezione come `recvline()` o `recvall()`.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-process|process]] · [[pwn-recvall|recvall]]
- [Documentazione ufficiale di poll](https://docs.pwntools.com/en/stable/tubes/processes.html#pwnlib.tubes.process.process.poll)
