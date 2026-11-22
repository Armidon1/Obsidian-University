---
title: pwn-shutdown
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.shutdown
---

# shutdown

> [!abstract] In breve
> Chiude una direzione del canale. È utile quando il programma aspetta la fine dell'input prima di produrre una risposta.

## Sintassi

- `io.shutdown("send")` chiude il lato di invio e lascia aperta la ricezione.
- `io.shutdown("recv")` chiude il lato di ricezione.

`io` è un tube ottenuto da `process(...)` o `remote(...)`.

## Esempio

```python
import sys
from pwn import process

programma = "import sys; print(len(sys.stdin.buffer.read()))"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    io.send(b"Ada")
    io.shutdown("send")
    assert io.recvline() == b"3\n"
```

`read()` attende la fine del flusso di input. Dopo `shutdown("send")` il programma può contare i byte ricevuti e mandare la risposta.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-close|close]] · [[pwn-send|send]] · [[pwn-recvline|recvline]]
- [Documentazione ufficiale di shutdown](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.shutdown)
