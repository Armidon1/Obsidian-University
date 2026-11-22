---
title: pwn-newline
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.newline
---

# newline

> [!abstract] In breve
> Attributo del tube che contiene i byte usati come fine riga. `sendline()` li aggiunge ai dati e `recvline()` li cerca durante la lettura.

## Sintassi

`io.newline = b"\r\n"` cambia il terminatore per il canale `io`, ottenuto da `process(...)` o `remote(...)`. Il valore predefinito è normalmente `b"\n"`.

## Esempio

```python
import sys
from pwn import process

programma = """
import sys
richiesta = sys.stdin.buffer.read(5)
if richiesta == b"Ada\\r\\n":
    sys.stdout.buffer.write(b"OK\\r\\n")
"""
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    io.newline = b"\r\n"
    io.sendline(b"Ada")
    assert io.recvline(drop=True) == b"OK"
```

Il processo risponde solo se ha ricevuto i cinque byte di `b"Ada\r\n"`. Con `drop=True`, `recvline()` rimuove dalla risposta il terminatore configurato.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-sendline|sendline]] · [[pwn-recvline|recvline]]
- [Documentazione ufficiale di newline](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.newline)
