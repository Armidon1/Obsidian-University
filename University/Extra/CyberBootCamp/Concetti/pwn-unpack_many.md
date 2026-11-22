---
title: pwn-unpack_many
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.unpack_many
---

# unpack_many

> [!abstract] In breve
> Decodifica più interi consecutivi della stessa larghezza.

## Sintassi e ritorno

- `unpack_many(dati, word_size, endian=...)`
- **Ritorno** · `list[int]`

Usa una larghezza multipla di otto bit e dati composti da campi interi di quella larghezza. Con `word_size='all'` ottieni una lista con un solo valore.

## Esempio

```python
from pwn import unpack_many

assert unpack_many(bytes.fromhex("00 0c 01 02"), 16, endian="big") == [12, 258]
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-unpack|unpack]]
- [Documentazione ufficiale di unpack_many](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.unpack_many)
