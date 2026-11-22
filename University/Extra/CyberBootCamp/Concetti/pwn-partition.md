---
title: pwn-partition
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/lists.html#pwnlib.util.lists.partition
---

# partition

> [!abstract] In breve
> Raggruppa gli elementi in base al valore restituito da una funzione.

## Sintassi e ritorno

- `partition(elementi, chiave, save_keys=False)`
- **Ritorno** · `list` di gruppi, oppure `OrderedDict` con `save_keys=True`

La funzione chiave viene applicata a ogni elemento. I gruppi seguono l'ordine in cui le chiavi compaiono per la prima volta.

## Esempio

```python
from pwn import partition

assert partition([3, 4, 5, 6], lambda n: n % 2) == [[3, 5], [4, 6]]
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-group|group]]
- [Documentazione ufficiale di partition](https://docs.pwntools.com/en/stable/util/lists.html#pwnlib.util.lists.partition)
