---
title: Ordinamento stabile
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
---

# Ordinamento stabile

> [!summary] In breve
> Un ordinamento è stabile se due voci con chiave uguale restano nello stesso ordine relativo che avevano nell'input.

| Algoritmo | Stabile? |
|---|---|
| insertion-sort | sì |
| merge-sort | sì (se a parità prende dalla prima metà) |
| bucket-sort (bucket FIFO), radix-sort | sì |
| quick-sort, heap-sort, selection-sort | no (scambi a distanza) |

Serve per ordinare per più criteri in passate successive (prima il criterio secondario, poi il principale): è il principio del [[Radix-sort|radix-sort]]. Java usa Tim-sort (stabile) per gli array di oggetti.

## Collegamenti

- **Concetti correlati**: [[Radix-sort]] · [[Bucket-sort]] · [[Merge-sort]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Ordinamento stabile|Lezione 12 — Ordinamento stabile]]
