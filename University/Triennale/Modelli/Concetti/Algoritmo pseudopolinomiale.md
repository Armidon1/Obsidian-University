---
title: Algoritmo pseudopolinomiale
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - analisi-algoritmi
---

# Algoritmo pseudopolinomiale

> [!summary] In breve
> Un algoritmo è pseudopolinomiale se il suo costo è polinomiale nel **valore** numerico dell'input ma esponenziale nella sua **dimensione** (numero di bit).

| algoritmo | costo nel valore | costo nella dimensione $z$ |
|---|---|---|
| potenza banale $a^b$ | $\Theta(b)$ | $\Theta(2^z)$ |
| test di primalità per tentativi | $O(\sqrt n)$ | $O(2^{z/2})$ |
| Euclide, analisi banale | $O(b)$ | $O(2^z)$ (non tight) |
| potenza per quadrati successivi | $\Theta(\log b)$ | $\Theta(z)$, **polinomiale** |
| Euclide, analisi accurata | $O(\log b)$ | $O(z)$, **polinomiale** |

Regola: con input numerici si scrive sempre il costo in funzione di $z = \log_2(\text{valore})$.

## Collegamenti

- **Concetti correlati**: [[Dimensione dell'input]] · [[Algoritmo di Euclide]] · [[Classe P]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[03 - MC - Esempi di analisi di complessità#Calcolo della potenza di un numero|Lezione 3 — Calcolo della potenza di un numero]]
> - [[03 - MC - Esempi di analisi di complessità#Test di primalità|Lezione 3 — Test di primalità]]
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Un'analisi banale|Lezione 4 — Un'analisi banale]]
