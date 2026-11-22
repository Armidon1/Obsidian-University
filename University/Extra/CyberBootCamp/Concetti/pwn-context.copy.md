---
title: pwn-context.copy
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.copy
---

# context.copy

> [!abstract] In breve
> Copia le impostazioni correnti del contesto.

## Sintassi e ritorno

- `context.copy()`
- **Ritorno** · `dict`

Il risultato contiene le impostazioni assegnate nel contesto corrente. Le impostazioni predefinite non assegnate possono essere assenti.

## Esempio

```python
from pwn import context

with context.local(endian="big"):
    opzioni = context.copy()
assert opzioni["endian"] == "big"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-context.local|context.local]]
- [Documentazione ufficiale di context.copy](https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.copy)
