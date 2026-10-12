---
title: Ereditarietà in C
tags:
  - sistemi-operativi
  - concetto
  - linguaggio-c
  - oop
---

# Ereditarietà in C

> [!summary] In breve
> Si ottiene mettendo la struct genitore come **primo campo** della struct figlia: così un puntatore alla figlia è anche un puntatore al genitore.

```c
typedef struct { int my_int; float my_float; } A;
typedef struct { A parent; int my_other_int; } B;   // B "estende" A
B b; printMyInt((A*)&b);                             // cast lecito
```

- Un puntatore a struct punta al suo **primo byte**, cioè al primo campo.
- È la base delle liste "intrusive" (`ListItem` come primo campo di `IntListItem`, del PCB, del TCB, del `BuddyListItem`…).

## Collegamenti

- **Concetti correlati**: [[Lista Generica in C]] · [[Virtual Method Table]] · [[Process Control Block]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[03 - SO - Programmazione OOP in C#Ereditarietà|Lezione 3 — Ereditarietà]]
