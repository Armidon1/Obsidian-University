---
title: Istruzione dominante
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - analisi-algoritmi
---

# Istruzione dominante

> [!summary] In breve
> Un'istruzione elementare è dominante se il suo contributo $C_\gamma$ al costo totale $C_A$ soddisfa $\xi C_\gamma(z) + \zeta \ge C_A(z)$: basta contare le sue esecuzioni per avere l'andamento asintotico del costo.

- In pratica è l'istruzione **eseguita più volte** (di solito nel ciclo più interno).
- Può non essere unica: ne basta una.
- **Attenzione alle chiamate**: vanno espanse. In
  ```c
  for(k = 1; k <= n; k++) b = f(k);   /* f(k) costa k^2 */
  ```
  `b = f(k)` è eseguita $n$ volte, ma il ciclo costa $\sum k^2 = \Theta(n^3)$: la dominante è dentro $f$.
- Programma **linearizzato**: si ignorano i costi di sola gestione dei cicli.

## Collegamenti

- **Concetti correlati**: [[Modello di costo CEM]] · [[Notazione O grande]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[02 - MC - Notazione asintotica#Operazioni dominanti|Lezione 2 — Operazioni dominanti]]
> - [[03 - MC - Esempi di analisi di complessità#Tabelle riassuntive|Lezione 3 — Tabelle riassuntive]]
