---
title: Algoritmo di Dijkstra per la Mutua Esclusione
tags:
  - sistemi-di-calcolo-2
  - concetto
  - mutua-esclusione
  - algoritmi
  - esame
---

# Algoritmo di Dijkstra per la Mutua Esclusione

> [!summary] In breve
> Generalizza Dekker a N processi: si prende il turno `k` se il proprietario non è interessato, poi si controlla che nessun altro sia `passed`. Garantisce ME e ND, non NS.

```
1. interested[i] = true
2. while (k != i) {
3.     passed[i] = false
4.     if (!interested[k]) then k = i }
5. passed[i] = true
6. for j != i: if (passed[j]) goto 2
8. <critical section>
9. passed[i] = false; interested[i] = false
```

- In caso di conflitto vince chi ha scritto `k` **per ultimo**.
- Richiede letture e scritture **atomiche** su `k`; starvation possibile.
- **All'esame**: domanda su Dijkstra o sul panettiere, mostrati con un errore.

## Collegamenti

- **Concetti correlati**: [[Algoritmo di Dekker]] · [[Algoritmo del Panettiere]] · [[Sezione Critica e Mutua Esclusione]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Algoritmo di Dijkstra|Lezione 3 — Algoritmo di Dijkstra]]
> - [[04 - SDC2 - Algoritmo del Panettiere#Dijkstra: riepilogo|Lezione 4 — Dijkstra: riepilogo]]
