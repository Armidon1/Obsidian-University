---
title: pwn-xor
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.xor
---

# xor

> [!abstract] In breve
> Combina sequenze binarie con l'operazione XOR.

## Sintassi e ritorno

- `xor(*sequenze, cut=...)`
- **Ritorno** · `bytes`

Gli operandi più corti vengono ripetuti. Usa `cut` per scegliere la lunghezza del risultato.

## Esempio

```python
from pwn import xor

assert xor(b"\x55\x00", b"\x0F") == b"\x5A\x0F"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-bits|bits]]
- [Documentazione ufficiale di xor](https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.xor)
