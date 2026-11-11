---
title: Percent Encoding
tags:
  - cyberbootcamp
  - concetto
  - web-security
  - encoding
---

# Percent Encoding

> [!summary] In breve
> Ogni byte si può scrivere in un URL come `%` seguito dal suo valore esadecimale; serve per i caratteri speciali e, in attacco, per aggirare filtri sulle stringhe.

| Carattere | Codifica |
|---|---|
| spazio | `%20` o `+` |
| `&` | `%26` |
| `.` / `/` | `%2e` / `%2f` |
| `%` | `%25` |

- `../` → `%2e%2e%2f`; **double encoding** → `%252e%252e%252f`.
- Il double encoding funziona quando un componente decodifica e controlla, e un altro decodifica di nuovo prima di usare il valore.

## Collegamenti

- **Concetti correlati**: [[URL e URI]] · [[Path Traversal]] · [[Parser Differential]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[01 - CB - Web Insecurity 1#URL encoding|Lezione 1 — URL encoding]]
> - [[01 - CB - Web Insecurity 1#Path traversal: exploitation|Lezione 1 — Path traversal: exploitation]]
