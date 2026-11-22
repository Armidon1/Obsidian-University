---
title: pwn-group
tags:
  - cyberbootcamp
  - concetto
  - pwn
source: https://docs.pwntools.com/en/stable/util/lists.html#pwnlib.util.lists.group
---

# group

> [!abstract] In breve
> Divide una sequenza in blocchi di dimensione fissata.

## Sintassi e ritorno

- `group(dimensione, sequenza, underfull_action='ignore')`
- **Ritorno** · `list` di sottosequenze

L'ultimo blocco incompleto può essere mantenuto, scartato o riempito con i valori di `fill_value`.

## Esempio

```python
from pwn import group

assert group(2, [1, 2, 3]) == [[1, 2], [3]]
```

## Collegamenti

- [[pwntools#Indice dei metodi e delle funzioni|Indice di pwntools]]
- [[pwn-partition|partition]]
- [Documentazione ufficiale di group](https://docs.pwntools.com/en/stable/util/lists.html#pwnlib.util.lists.group)
