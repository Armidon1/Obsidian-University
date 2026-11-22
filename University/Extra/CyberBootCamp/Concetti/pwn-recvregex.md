---
title: pwn-recvregex
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvregex
---

# recvregex

> [!abstract] In breve
> Legge fino a una corrispondenza con un'espressione regolare.

## Sintassi e ritorno

- `io.recvregex(pattern, capture=False, timeout=...)` su un tube da `process(...)` o `remote(...)`
- **Ritorno** · `bytes` con `capture=False`. Con `capture=True` restituisce `re.Match` per una corrispondenza o `None` se manca

Usa un'espressione regolare per byte, ad esempio un letterale `br'...'`. Con `exact=True` la corrispondenza deve iniziare al primo byte.

## Esempio

```python
import sys
from pwn import process

programma = "print('temperatura=21 C')"
with process([sys.executable, "-u", "-c", programma], timeout=2) as io:
    risposta = io.recvregex(br"temperatura=([0-9]+) ", capture=True)
    assert risposta.group(1) == b"21"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-recvpred|recvpred]]
- [Documentazione ufficiale di recvregex](https://docs.pwntools.com/en/stable/tubes.html#pwnlib.tubes.tube.tube.recvregex)
