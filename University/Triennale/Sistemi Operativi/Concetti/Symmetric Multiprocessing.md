---
title: Symmetric Multiprocessing
tags:
  - sistemi-operativi
  - concetto
  - multicore
  - scheduling
---

# Symmetric Multiprocessing

> [!summary] In breve
> Più CPU identiche che condividono la memoria; ognuna fa self-scheduling ed esegue sia codice utente che kernel.

- Il clock non può più crescere, quindi si mettono **più core in un chip**. Ogni core ha registri e cache propri, ma la **memoria è condivisa** (il bus può diventare un collo di bottiglia).
- **SMP**: CPU identiche, carico distribuito, ogni processore fa **self-scheduling** con una coda ready comune o una per core. È lo schema oggi più usato.
- **Multiprocessing asimmetrico**: un solo processore gestisce le strutture dati del sistema.
- **Affinità**: conviene tenere un processo sullo stesso core, perché la sua cache contiene i dati del processo. *Soft affinity*: l'OS ci prova. *Hard affinity*: il processo è vincolato a un insieme di core.
- Il kernel può essere preemptive o non preemptive.

## Collegamenti

- **Concetti correlati**: [[Scheduling Multiprocessore]] · [[CPU Scheduler e Dispatcher]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[01 - SO - Introduzione e Git#Multicore e Symmetric Multiprocessing|Lezione 1 — Multicore e Symmetric Multiprocessing]]
> - [[09 - SO - CPU Scheduling#Scheduling multiprocessore|Lezione 9 — Scheduling multiprocessore]]
> - [[05 - SDC - Ottimizzazione dei programmi#Quanto conta ottimizzare le prestazioni|Sistemi di Calcolo, cap. 5 — Quanto conta ottimizzare le prestazioni]]
