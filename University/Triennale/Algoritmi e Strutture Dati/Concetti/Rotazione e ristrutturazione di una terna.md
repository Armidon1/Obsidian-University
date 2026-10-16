---
title: Rotazione e ristrutturazione di una terna
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
---

# Rotazione e ristrutturazione di una terna

> [!summary] In breve
> Una rotazione porta un figlio sopra il genitore in $O(1)$ preservando l'ordine simmetrico; la ristrutturazione di una terna $(x, y, z)$ mette in cima la chiave di mezzo con una rotazione singola o doppia.

```text
      y              x
     / \            / \
    x  T3   ⇄     T1   y
   / \                / \
  T1 T2              T2 T3
```

- Rotazione: $T_1$ sale di un livello, $T_3$ scende, $T_2$ cambia genitore.
- `restructure(x)`: si rinominano $x, y, z$ come $a < b < c$ (ordine simmetrico) e i quattro sottoalberi $T_1..T_4$; $b$ diventa la radice con figli $a$ e $c$.
  - direzioni uguali (destra-destra, sinistra-sinistra) → rotazione **singola** di $y$;
  - direzioni opposte → rotazione **doppia** di $x$.
- Operazione di base di AVL, splay e rosso-nero.

## Collegamenti

- **Concetti correlati**: [[Albero di ricerca binario]] · [[Albero AVL]] · [[Albero splay]] · [[Albero rosso-nero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[11 - ASD - Alberi di ricerca#Rotazioni|Lezione 11 — Rotazioni]]
