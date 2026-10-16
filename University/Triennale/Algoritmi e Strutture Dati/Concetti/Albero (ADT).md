---
title: Albero (ADT)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi
  - adt
---

# Albero (ADT)

> [!summary] In breve
> Un albero è un insieme di nodi con una relazione genitore-figlio: una radice senza genitore, ogni altro nodo con un solo genitore; l'ADT accede ai nodi tramite posizioni.

- **Radice**, **figli**, **fratelli**, **foglie** (esterni, senza figli), nodi **interni**, **antenati**, **discendenti**, **sottoalbero**.
- **Albero ordinato**: i figli di ogni nodo hanno un ordine (es. capitoli di un libro).
- Metodi: `root()`, `parent(p)`, `children(p)`, `numChildren(p)`, `isInternal(p)`, `isExternal(p)`, `isRoot(p)`, `size()`, `iterator()`, `positions()`.
- Struttura concatenata: ogni nodo ha elemento, genitore e contenitore dei figli.

Nei grafi un "albero" è un grafo connesso aciclico **senza** radice designata.

## Collegamenti

- **Concetti correlati**: [[Profondità e altezza di un albero]] · [[Albero binario]] · [[Attraversamenti di un albero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[08 - ASD - Alberi#Alberi: definizioni e proprietà|Lezione 8 — Alberi: definizioni e proprietà]]
