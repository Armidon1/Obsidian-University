---
title: pwn-context.update
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.update
---

# context.update

> [!abstract] In breve
> Imposta più opzioni del contesto con una chiamata.

## Sintassi e ritorno

- `context.update(arch=..., endian=...)`
- **Ritorno** · `None`

L'impostazione di un'architettura può definire valori predefiniti per altre opzioni. Specifica esplicitamente quelli che il tuo formato richiede.

## Esempio

```python
from pwn import context

with context.local():
    context.update(arch="amd64", endian="little")
    assert context.arch == "amd64"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-context.local|context.local]]
- [Documentazione ufficiale di context.update](https://docs.pwntools.com/en/stable/context.html#pwnlib.context.ContextType.update)
