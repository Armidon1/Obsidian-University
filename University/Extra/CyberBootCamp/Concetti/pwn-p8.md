---
title: pwn-p8
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p8
---

# p8

> [!abstract] In breve
> Codifica un intero a 8 bit in un singolo byte.

## Sintassi

`p8(valore, signed=False)`

## Esempio

```python
from pwn import p8

campo = p8(42, signed=False)
assert campo.hex(" ") == "2a"
```

Con un solo byte l'ordine dei byte è ininfluente. Con `signed=False` il campo rappresenta valori tra 0 e 255 inclusi.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-u8|u8]] · [[pwn-pack|pack]]
- [Documentazione ufficiale di p8](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p8)
