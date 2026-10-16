---
title: Array dinamico
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - array
  - analisi-ammortizzata
---

# Array dinamico

> [!summary] In breve
> Quando l'array è pieno se ne alloca uno più grande (il doppio) e si copiano gli elementi: un singolo inserimento può costare $O(n)$, ma $n$ inserimenti in fondo costano $O(n)$ in totale.

```java
protected void resize(int capacity) {
  E[] temp = (E[]) new Object[capacity];
  for (int k = 0; k < size; k++) temp[k] = data[k];
  data = temp;
}
// in add: if (size == data.length) resize(2 * data.length);
```

| Strategia di crescita | Costo di $n$ `add` |
|---|---|
| geometrica (×2, ×3/2…) | $O(n)$: $O(1)$ ammortizzato |
| aritmetica (+$c$) | $O(n^2)$: $O(n)$ ammortizzato |

È così che funziona `java.util.ArrayList`. Si può anche dimezzare quando l'array è pieno per meno di un quarto.

## Collegamenti

- **Concetti correlati**: [[Analisi ammortizzata]] · [[Lista con indice]] · [[Array circolare]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[07 - ASD - Liste e iteratori#Array dinamici|Lezione 7 — Array dinamici]]
