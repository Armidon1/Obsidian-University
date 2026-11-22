---
title: pwn-unhex
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.unhex
---

# unhex

> [!abstract] In breve
> Converte testo esadecimale in dati binari.

## Sintassi e ritorno

- `unhex(testo)`
- **Ritorno** · `bytes`

Ogni coppia di cifre rappresenta un byte. Passa le cifre senza separatori interni. Gli spazi ai bordi vengono rimossi e, se il numero di cifre è dispari, viene aggiunto uno zero iniziale.

## Esempio

```python
from pwn import unhex

assert unhex("4100") == b"A\x00"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-enhex|enhex]]
- [Documentazione ufficiale di unhex](https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.unhex)
