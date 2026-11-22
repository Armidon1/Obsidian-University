---
title: pwn-make_packer
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.make_packer
---

# make_packer

> [!abstract] In breve
> Crea una funzione per codificare interi con impostazioni fissate.

## Sintassi e ritorno

- `make_packer(word_size, endian=..., signed=...)`
- **Ritorno** · Funzione che converte un `int` in `bytes`

Il codificatore mantiene larghezza, ordine dei byte e segno scelti alla creazione, anche se cambia il contesto.

## Esempio

```python
from pwn import make_packer

codifica = make_packer(16, endian="big", signed=False)
assert codifica(258).hex() == "0102"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-pack|pack]]
- [Documentazione ufficiale di make_packer](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.make_packer)
