---
title: CPU Burst e IO Burst
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# CPU Burst e IO Burst

> [!summary] In breve
> I processi alternano intervalli di calcolo (CPU burst) e di attesa di I/O (I/O burst); la distribuzione delle durate dei CPU burst ha moltissimi burst brevi e pochi lunghi.

- **I/O bound** (es. editor): burst di CPU brevi. **CPU bound** (es. compilatore): burst di CPU lunghi.
- Previsione del prossimo burst (media esponenziale):

$$\hat b_{t+1} = \alpha\, b_t + (1-\alpha)\, \hat b_t$$

- Il quanto del RR si sceglie in modo che circa l'80% dei CPU burst sia più corto di q.

## Collegamenti

- **Concetti correlati**: [[Shortest Job First]] · [[Round Robin]] · [[Criteri di Scheduling]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#CPU burst e I/O burst|Lezione 9 — CPU burst e I/O burst]]
> - [[09 - SO - CPU Scheduling#Predire il prossimo burst|Lezione 9 — Predire il prossimo burst]]
