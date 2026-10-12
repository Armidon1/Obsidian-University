---
title: Gestione del Deadlock
tags:
  - sistemi-di-calcolo-2
  - concetto
  - deadlock
---

# Gestione del Deadlock

> [!summary] In breve
> Prevention (si elimina una condizione: conservativa), avoidance (si evitano gli stati unsafe: serve conoscere le richieste massime), detection + recovery (si concede tutto e si interviene quando succede).

- **Avoidance**: process initiation denial, resource allocation denial (algoritmo del banchiere).
- **Detection**: si marcano i processi senza risorse; con W = available si marcano ripetutamente i processi con richieste ≤ W, sommando a W le loro allocazioni. I **non marcati** sono in deadlock.
- **Recovery**: terminare tutti, rollback a un checkpoint, terminare uno alla volta, preemption delle risorse.

| | Prevention | Avoidance | Detection |
| --- | --- | --- | --- |
| Politica | conservativa | intermedia | liberale |
| Pro | nessuna preemption (alcuni schemi) | nessuna preemption | non ritarda l'avvio |
| Contro | inefficiente | richieste future note; blocchi lunghi | perdite per la preemption |

## Collegamenti

- **Concetti correlati**: [[Deadlock]] · [[Algoritmo del Banchiere]] · [[Condizioni di Coffman]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Gestione del deadlock|Lezione 3 — Gestione del deadlock]]
> - [[03 - SDC2 - Deadlock#Detection|Lezione 3 — Detection]]
> - [[03 - SDC2 - Deadlock#Recovery|Lezione 3 — Recovery]]
> - [[03 - SDC2 - Deadlock#Tabella riassuntiva|Lezione 3 — Tabella riassuntiva]]
