---
title: Invariante di ciclo
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - analisi
  - dimostrazioni
---

# Invariante di ciclo

> [!summary] In breve
> Una proprietà vera prima del ciclo e preservata da ogni iterazione: alla fine del ciclo dimostra la correttezza dell'algoritmo.

Per dimostrare la correttezza di un ciclo con l'invariante $L$:
1. **Inizializzazione**: $L$ vale prima della prima iterazione;
2. **Conservazione**: se vale prima di un'iterazione, vale anche dopo;
3. **Terminazione**: quando il ciclo finisce, $L$ implica il risultato voluto.

Esempio (`arrayFind`): "nessuno dei primi $j$ elementi è uguale a `val`".

## Collegamenti

- **Concetti correlati**: [[Dimostrazione per induzione]] · [[Ordinamento per inserimento]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[04 - ASD - Analisi di algoritmi#Invarianti di ciclo|Lezione 4 — Invarianti di ciclo]]
