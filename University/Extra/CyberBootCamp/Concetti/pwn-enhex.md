---
title: pwn-enhex
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.enhex
---

# enhex

> [!abstract] In breve
> Converte dati binari in testo esadecimale.

## Sintassi e ritorno

- `enhex(dati)`
- **Ritorno** · `str`

Ogni byte diventa una coppia di cifre. Il risultato è utile per visualizzare o confrontare un campo binario.

## Esempio

```python
from pwn import enhex

assert enhex(b"A\x00") == "4100"
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-unhex|unhex]]
- [Documentazione ufficiale di enhex](https://docs.pwntools.com/en/stable/util/fiddling.html#pwnlib.util.fiddling.enhex)
