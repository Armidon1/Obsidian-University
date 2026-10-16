---
title: Limite inferiore per l'ordinamento basato su confronti
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
  - analisi
---

# Limite inferiore per l'ordinamento basato su confronti

> [!summary] In breve
> Ogni algoritmo che ordina solo confrontando coppie di elementi richiede $\Omega(n\log n)$ confronti nel caso peggiore.

- L'algoritmo si modella con un **albero di decisione** binario: nodi interni = confronti, foglie = esiti.
- Ogni permutazione dell'input deve finire in una foglia diversa → almeno $n!$ foglie.
- Altezza $\ge \log(n!) \ge \log\big((n/2)^{n/2}\big) = \frac{n}{2}\log\frac{n}{2} = \Omega(n\log n)$.

Conseguenze: merge-sort e heap-sort sono asintoticamente ottimi; per fare meglio servono ipotesi sulle chiavi ([[Bucket-sort]], [[Radix-sort]]).

## Collegamenti

- **Concetti correlati**: [[Bucket-sort]] · [[Radix-sort]] · [[Proprietà degli alberi binari]] · [[Notazione asintotica]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Limite inferiore asintotico per l'ordinamento|Lezione 12 — Limite inferiore asintotico per l'ordinamento]]
