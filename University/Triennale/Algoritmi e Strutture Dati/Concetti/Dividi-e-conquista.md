---
title: Dividi-e-conquista
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - progettazione-algoritmi
  - ricorsione
---

# Dividi-e-conquista

> [!summary] In breve
> Schema di progettazione: si **divide** il problema in sotto-problemi disgiunti, li si risolve **ricorsivamente** e si **combinano** le soluzioni.

1. **Dividi**: sotto una soglia si risolve direttamente; altrimenti si spezza l'input.
2. **Conquista**: si risolvono ricorsivamente i sotto-problemi.
3. **Combina**: si fondono le soluzioni.

| Algoritmo | Lavoro nella divisione | Lavoro nella combinazione |
|---|---|---|
| [[Merge-sort]] | banale (a metà) | fusione $O(n)$ |
| [[Quick-sort]] | partizione col pivot | banale (concatenazione) |

Si analizza con [[Equazione di ricorrenza|equazioni di ricorrenza]]. Varianti: **prune-and-search** (un solo sotto-problema, es. ricerca binaria, quick-select); se i sotto-problemi si sovrappongono conviene la [[Programmazione dinamica|programmazione dinamica]].

## Collegamenti

- **Concetti correlati**: [[Merge-sort]] · [[Quick-sort]] · [[Equazione di ricorrenza]] · [[Programmazione dinamica]] · [[Ricorsione]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Dividi-e-conquista (divide-and-conquer)|Lezione 12 — Dividi-e-conquista (divide-and-conquer)]]
