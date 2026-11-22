---
title: pwn-p16
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p16
---

# p16

> [!abstract] In breve
> Codifica un intero a 16 bit in un campo di 2 byte.

## Sintassi

`p16(valore, endian="little", signed=False)`

## Esempio

```python
from pwn import p16

campo = p16(258, endian="little", signed=False)
assert campo.hex(" ") == "02 01"
```

Con `endian='little'` il byte meno significativo viene per primo. Con `signed=False` il campo rappresenta valori tra 0 e 65 535 inclusi.

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-u16|u16]] · [[pwn-pack|pack]]
- [Documentazione ufficiale di p16](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p16)
