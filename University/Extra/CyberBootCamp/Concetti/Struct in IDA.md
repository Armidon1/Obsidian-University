---
title: Struct in IDA
tags:
  - cyberbootcamp
  - concetto
  - reverse-engineering
  - ida
---

# Struct in IDA

> [!summary] In breve
> Il compilatore cancella i nomi dei campi: IDA vede solo `base + offset`, quindi le struct vanno definite a mano e assegnate come tipo.

```c
struct Brooom { char brand[50]; char model[50]; int year; };  // offset 0, 50, 100; sizeof 104
```

| Tasto | Azione |
|---|---|
| `INS` | nuova struct (finestra Structures) |
| `D` su struct / campo | nuovo campo / cambia dimensione |
| `Shift+*` | campo → array |
| `Y` sulla variabile | assegna la struct |

`*(v1 + 100)` → `v1->year`. Da IDA 9: *Local Types*, si può incollare la definizione C.

## Collegamenti

- **Concetti correlati**: [[Scorciatoie IDA]] · [[Esportare Dati da IDA]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[02 - CB - Reverse Engineering 1#Struct|Lezione 2 — Struct]]
> - [[02 - CB - Reverse Engineering 1#Struct in IDA|Lezione 2 — Struct in IDA]]
