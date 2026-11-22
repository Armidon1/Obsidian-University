---
title: pwn-unbits
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.unbits
---

# unbits

> [!abstract] In breve
> Raggruppa i bit in byte.

## Sintassi e ritorno

- `unbits(bit, endian="big")`
- **Ritorno** · `bytes`

L'ordine indica come disporre i bit all'interno di ogni byte. Usa multipli di otto bit se il formato ha campi di byte interi.

## Esempio

```python
from pwn import unbits

assert unbits([1, 0, 1, 0, 0, 0, 0, 0]) == b"\xA0"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-bits|bits]]
- [Documentazione ufficiale di unbits](https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.unbits)
