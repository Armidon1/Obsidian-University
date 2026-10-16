---
title: Dimensione dell'input
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - analisi-algoritmi
---

# Dimensione dell'input

> [!summary] In breve
> La dimensione dell'input è il numero di bit necessari e sufficienti a descriverlo. Il costo di un algoritmo si esprime in funzione della dimensione, non del valore: per un intero $N$ la dimensione è $\log_2 N$, non $N$.

| input | dimensione $z$ |
|---|---|
| array di $n$ elementi | $z = \Theta(n)$ |
| un intero $N$ | $z = \lfloor \log_2 N \rfloor + 1$ |
| grafo | numero di nodi + archi |

Conseguenza: un ciclo di $N$ iterazioni su un intero $N$ costa $\Theta(N) = \Theta(2^z)$, **esponenziale** (vedi [[Algoritmo pseudopolinomiale]]).

> [!danger] Errore tipico
> Per un array di $n$ celle la dimensione è $\Theta(n)$, **non** $\log n$: $\log n$ è la dimensione dell'intero $n$.

## Collegamenti

- **Concetti correlati**: [[Modello di costo CEM]] · [[Algoritmo pseudopolinomiale]] · [[Analisi del caso peggiore]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[01 - MC - Costo degli algoritmi e modello CEM#Analisi nel caso peggiore in funzione della dimensione dell'input|Lezione 1 — Analisi nel caso peggiore in funzione della dimensione dell'input]]
> - [[03 - MC - Esempi di analisi di complessità#Ricerca binaria|Lezione 3 — Ricerca binaria]]
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Dimensione dell'output|Lezione 4 — Dimensione dell'output]]
