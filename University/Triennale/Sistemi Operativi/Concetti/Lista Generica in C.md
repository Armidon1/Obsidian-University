---
title: Lista Generica in C
tags:
  - sistemi-operativi
  - concetto
  - linguaggio-c
  - strutture-dati
---

# Lista Generica in C

> [!summary] In breve
> Lista doppiamente concatenata i cui nodi (`ListItem`) contengono solo i link; il contenuto lo aggiunge la struct che "estende" `ListItem` come primo campo.

- `ListItem { prev, next }`, `ListHead { first, last, size }`.
- Operazioni: `List_init`, `List_find`, `List_insert(head, prev, item)`, `List_detach(head, item)`. `List_detach` **non** libera la memoria.
- Estensione: `typedef struct { ListItem list; int info; } IntListItem;` e cast `(IntListItem*)item`.
- Usata ovunque nel corso: code di TCB/PCB, liste dei figli, free list per livello del buddy allocator, lista dei timer.

## Collegamenti

- **Concetti correlati**: [[Ereditarietà in C]] · [[Virtual Method Table]] · [[Process Control Block]] · [[disastrOS]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[03 - SO - Programmazione OOP in C#Una lista generica in C|Lezione 3 — Una lista generica in C]]
> - [[03 - SO - Programmazione OOP in C#Estendere la lista: IntListItem|Lezione 3 — Estendere la lista: IntListItem]]
