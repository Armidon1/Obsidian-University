---
title: Albero binario su array
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi
  - array
---

# Albero binario su array

> [!summary] In breve
> Numerando i nodi per livelli ($f(\text{radice}) = 0$, figlio sinistro $2f(p)+1$, destro $2f(p)+2$) un albero binario si memorizza in un array, senza puntatori.

- Genitore di $i$: $\lfloor (i-1)/2 \rfloor$.
- Navigazione con aritmetica sugli indici, $O(1)$.
- Spazio: dipende dal massimo indice usato, che può arrivare a $2^n - 1$ per alberi sbilanciati → adatto ad alberi **completi**, come lo [[Heap binario|heap]].
- Le modifiche strutturali (rimuovere un nodo e far salire il sottoalbero, rotazioni) costano $O(n)$.

## Collegamenti

- **Concetti correlati**: [[Albero binario]] · [[Heap binario]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[08 - ASD - Alberi#Albero binario rappresentato con un array|Lezione 8 — Albero binario rappresentato con un array]]
