---
title: Albero di decisione
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - lower-bound
---

# Albero di decisione

> [!summary] In breve
> Modella un algoritmo basato su confronti come albero binario pieno: nodi = confronti, foglie = risposte. Se le risposte possibili sono $f$, servono almeno $\log_2 f$ confronti nel caso peggiore.

- Ogni confronto dà 1 bit di informazione: **limite inferiore teorico dell'informazione**.
- **Ordinamento**: $n!$ permutazioni ⇒ altezza $\ge \log_2 n! = \Omega(n \log n)$, perché $n! \ge (n/2)^{n/2}$ (o per Stirling).
- **Ricerca** in tabella ordinata: $n + 1$ esiti ⇒ $\Omega(\log n)$.

Per 3 elementi: 6 foglie, altezza $3 = \lceil \log_2 6 \rceil$.

## Collegamenti

- **Concetti correlati**: [[Limite inferiore per l'ordinamento basato su confronti]] · [[Delimitazioni superiori e inferiori]] · [[Algoritmo ottimo]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[05 - MC - Delimitazioni superiori e inferiori#Alberi di decisione|Lezione 5 — Alberi di decisione]]
> - [[05 - MC - Delimitazioni superiori e inferiori#Complessità inferiore dell'ordinamento|Lezione 5 — Complessità inferiore dell'ordinamento]]
> - [[05 - MC - Delimitazioni superiori e inferiori#Esempio: ricerca in una tabella ordinata|Lezione 5 — Esempio: ricerca in una tabella ordinata]]
