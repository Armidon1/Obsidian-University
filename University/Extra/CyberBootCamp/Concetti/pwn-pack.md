---
title: pwn-pack
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.pack
---

# pack

> [!abstract] In breve
> Codifica un intero con una larghezza scelta esplicitamente in bit.

## Sintassi

`pack(valore, word_size, endianness, sign)`

## Esempio

```python
from pwn import pack

campo = pack(258, 24, "big", False)
assert campo.hex(" ") == "00 01 02"
```

Qui il campo occupa tre byte perché la larghezza è 24 bit. `False` seleziona un intero senza segno.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-unpack|unpack]] · [[pwn-p32|p32]]
- [Documentazione ufficiale di pack](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.pack)
