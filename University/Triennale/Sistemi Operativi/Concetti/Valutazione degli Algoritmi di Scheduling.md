---
title: Valutazione degli Algoritmi di Scheduling
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# Valutazione degli Algoritmi di Scheduling

> [!summary] In breve
> Modelli deterministici (un carico fisso calcolato a mano), modelli a code (legge di Little n = λW), simulazioni (anche guidate da tracce reali).

- **Deterministico**: 10, 29, 3, 7, 12 all'istante 0 → waiting medio FCFS 28, SJF 13, RR (q = 10) 23.
- **Legge di Little**: $n = \lambda W$ (lunghezza della coda = frequenza di arrivo × attesa). Esempio: 14 processi in coda, 7 arrivi/s → W = 2 s.
- **Simulazione**: un modello programmato con il clock come variabile; i dati possono venire da un *trace tape* di esecuzioni reali, così si confrontano FCFS, SJF e RR sullo stesso carico.

## Collegamenti

- **Concetti correlati**: [[Criteri di Scheduling]] · [[First Come First Served]] · [[Shortest Job First]] · [[Round Robin]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#Valutazione degli algoritmi|Lezione 9 — Valutazione degli algoritmi]]
