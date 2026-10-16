---
title: Funzione di hash
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - hashing
---

# Funzione di hash

> [!summary] In breve
> Si compone di un **codice hash** che trasforma la chiave in un intero e di una **funzione di compressione** che lo porta in $[0, N-1]$; deve distribuire le chiavi uniformemente.

**Codici hash**: reinterpretazione dei bit; somma o XOR delle parti (pessimi per stringhe: anagrammi collidono); **polinomiale** $x_0 a^{n-1} + \dots + x_{n-1}$ (Java usa $a = 31$); **scorrimento ciclico** dei bit.

**Compressione**:
- divisione: $i \bmod N$, con $N$ **primo**;
- MAD (*multiply-add-and-divide*): $[(ai + b) \bmod p] \bmod N$, con $p > N$ primo e $a \in [1, p-1]$, $b \in [0, p-1]$ casuali.

Oggetti uguali (`equals`) devono avere lo stesso `hashCode`. Diverse dalle [[Funzioni Hash Crittografiche|funzioni hash crittografiche]], che hanno requisiti di sicurezza.

## Collegamenti

- **Concetti correlati**: [[Tabella hash]] · [[Metodo equals]] · [[Funzioni Hash Crittografiche]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Funzioni di hash|Lezione 10 — Funzioni di hash]]
