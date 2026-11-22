---
title: pwn-concat
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/lists.html#pwnlib.util.lists.concat
---

# concat

> [!abstract] In breve
> Appiattisce di un livello un iterabile di sequenze.

## Sintassi e ritorno

- `concat(sequenze)`
- **Ritorno** · `list`

Gli elementi delle sequenze interne finiscono nella stessa lista, mantenendo l'ordine.

## Esempio

```python
from pwn import concat

assert concat([[1, 2], [3]]) == [1, 2, 3]
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-group|group]]
- [Documentazione ufficiale di concat](https://docs.pwntools.com/en/stable/util/lists.html#pwnlib.util.lists.concat)
