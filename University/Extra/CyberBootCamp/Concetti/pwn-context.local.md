---
title: pwn-context.local
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.local
---

# context.local

> [!abstract] In breve
> Imposta temporaneamente opzioni di pwntools come il livello di log, il timeout o l'ordine dei byte. All'uscita dal blocco vengono ripristinati i valori precedenti.

## Sintassi

`with context.local(log_level="debug", timeout=2):` richiede `context` importato da `pwn`. Il livello `debug` mostra i byte scambiati dal canale durante il blocco.

## Esempio

```python
import sys
from pwn import context, process

timeout_precedente = context.timeout
with context.local(log_level="debug", timeout=2):
    with process([sys.executable, "-u", "-c", "print('pronto')"]) as io:
        assert io.recvline() == b"pronto\n"

assert context.timeout == timeout_precedente
```

Il processo viene creato dentro il blocco e usa il timeout impostato per quel contesto.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-settimeout|settimeout]] · [[pwn-process|process]] · [[pwn-hexdump|hexdump]]
- [Documentazione ufficiale di context.local](https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.local)
