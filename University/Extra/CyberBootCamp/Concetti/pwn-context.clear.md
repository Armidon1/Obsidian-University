---
title: pwn-context.clear
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.clear
---

# context.clear

> [!abstract] In breve
> Ripristina le impostazioni predefinite del contesto.

## Sintassi e ritorno

- `context.clear()`
- **Ritorno** · `None`

Puoi passare opzioni da impostare dopo il ripristino. `context.local()` permette di limitare le modifiche a un blocco.

## Esempio

```python
from pwn import context

with context.local():
    context.clear(endian="big")
    assert context.endian == "big"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-context.local|context.local]]
- [Documentazione ufficiale di context.clear](https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.clear)
