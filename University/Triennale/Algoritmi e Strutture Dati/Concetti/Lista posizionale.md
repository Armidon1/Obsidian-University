---
title: Lista posizionale
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - liste
  - adt
---

# Lista posizionale

> [!summary] In breve
> L'ADT lista posizionale identifica i punti della lista con oggetti `Position` stabili (non indici) e permette inserimenti e rimozioni in qualunque posizione nota in $O(1)$.

| Metodo | Effetto |
|---|---|
| `first()`, `last()`, `before(p)`, `after(p)` | navigazione |
| `addFirst`, `addLast`, `addBefore(p,e)`, `addAfter(p,e)` | inserimento, restituiscono la nuova posizione |
| `set(p,e)`, `remove(p)` | modifica / rimozione |

- `Position<E>` ha solo `getElement()`; resta valida finché il suo elemento non viene rimosso.
- Implementazione: [[Lista doppiamente concatenata|lista doppiamente concatenata]] con sentinelle; il metodo privato `validate` converte `Position` in `Node`. Tutto $O(1)$.
- Usata per le liste di vertici e lati dei grafi, per le liste dei livelli BFS, ecc.

## Collegamenti

- **Concetti correlati**: [[Lista con indice]] · [[Lista doppiamente concatenata]] · [[Iteratore]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[07 - ASD - Liste e iteratori#Liste posizionali|Lezione 7 — Liste posizionali]]
