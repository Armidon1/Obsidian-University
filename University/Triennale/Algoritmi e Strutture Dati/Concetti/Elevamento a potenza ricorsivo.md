---
title: Elevamento a potenza ricorsivo
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ricorsione
---

# Elevamento a potenza ricorsivo

> [!summary] In breve
> $x^n$ si calcola in $O(\log n)$ con il quadrato ripetuto: $x^n = (x^{\lfloor n/2 \rfloor})^2$, moltiplicato per $x$ se $n$ è dispari.

```java
public static double power(double x, int n) {
  if (n == 0) return 1;
  double partial = power(x, n / 2);    // UNA sola chiamata
  double result = partial * partial;
  if (n % 2 == 1) result *= x;
  return result;
}
```

La versione banale $x^n = x \cdot x^{n-1}$ è $O(n)$. Chiamare due volte `power(x, n/2)` invece di salvare il risultato riporterebbe il costo a $O(n)$.

## Collegamenti

- **Concetti correlati**: [[Ricorsione lineare, binaria e multipla]] · [[Ricorsione]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[05 - ASD - Ricorsione#Algoritmi ricorsivi per l'elevamento a potenza|Lezione 5 — Algoritmi ricorsivi per l'elevamento a potenza]]
