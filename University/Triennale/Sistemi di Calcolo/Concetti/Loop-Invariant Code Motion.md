---
title: Loop-Invariant Code Motion
tags:
  - sistemi-di-calcolo
  - concetto
  - ottimizzazione
---

# Loop-Invariant Code Motion

> [!summary] In breve
> Spostare prima del ciclo il codice che calcola sempre lo stesso valore a ogni iterazione. Il compilatore lo fa da solo, tranne quando c'è una chiamata a funzione di cui non conosce gli effetti.

```c
for (i = 0; i < strlen(s); i++) ...   // strlen ricalcolata: Θ(n²)
int n = strlen(s);                   // hoisting manuale: O(n)
for (i = 0; i < n; i++) ...
```

- È un **performance bug** classico.
- Il compilatore non può spostare `strlen`: non sa se ha effetti collaterali (scelta conservativa).

## Collegamenti

- **Concetti correlati**: [[Ottimizzazioni del Compilatore]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[05 - SDC - Ottimizzazione dei programmi#Loop-invariant code motion (hoisting)|Lezione 5 — Loop-invariant code motion (hoisting)]]
