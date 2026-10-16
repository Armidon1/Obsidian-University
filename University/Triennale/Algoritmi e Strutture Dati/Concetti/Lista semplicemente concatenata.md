---
title: Lista semplicemente concatenata
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - liste
  - strutture-dati
---

# Lista semplicemente concatenata

> [!summary] In breve
> Sequenza di nodi, ognuno con un elemento e un riferimento al successivo, più `head` e `tail`: inserimento in testa e in coda e rimozione in testa in $O(1)$, ma rimuovere in coda costa $O(n)$.

```text
head → [A|•] → [B|•] → [C|∅] ← tail
```

| Operazione | Tempo |
|---|---|
| `addFirst`, `addLast`, `removeFirst` | $O(1)$ |
| `removeLast` | $O(n)$ (serve il penultimo) |
| accesso all'$i$-esimo | $O(i)$ |

Base per [[Pila (ADT)|pile]] e [[Coda (ADT)|code]] concatenate.

## Collegamenti

- **Concetti correlati**: [[Lista doppiamente concatenata]] · [[Lista concatenata circolare]] · [[Lista Generica in C]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[03 - ASD - Strutture dati fondamentali#Liste semplicemente concatenate|Lezione 3 — Liste semplicemente concatenate]]
