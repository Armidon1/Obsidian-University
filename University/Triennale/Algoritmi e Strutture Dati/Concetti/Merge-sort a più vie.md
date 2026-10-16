---
title: Merge-sort a più vie
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
  - memoria-esterna
---

# Merge-sort a più vie

> [!summary] In breve
> Ordinamento esterno: si divide in $d = M/B - 1$ parti, le si ordina ricorsivamente e le si fonde tutte insieme tenendo un blocco per sequenza in memoria: $O\big(\frac{n}{B}\log_{M/B}\frac{n}{B}\big)$ trasferimenti.

- Ricorrenza: $t(n) = d\,t(n/d) + cn/B$, $t(n) = 1$ se $n \le B$.
- Fusione a $d$ vie: un blocco in memoria per ciascuna sequenza + uno per l'output; ogni blocco letto/scritto una volta → $O(n/B)$ trasferimenti.
- Il minimo dei $d$ elementi di testa si trova con una [[Coda prioritaria (ADT)|coda prioritaria]] in $O(\log d)$.
- Calcolo interno $O(n\log n)$. È l'[[External Merge Sort]] dei DBMS.

## Collegamenti

- **Concetti correlati**: [[Merge-sort]] · [[B-albero]] · [[External Merge Sort]] · [[Coda prioritaria (ADT)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[15 - ASD - Gestione della memoria e B-alberi#Merge-sort a più vie|Lezione 15 — Merge-sort a più vie]]
