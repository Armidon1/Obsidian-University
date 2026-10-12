---
title: Cluster
tags:
  - sistemi-di-calcolo-2
  - concetto
  - sistemi-distribuiti
  - parallelismo
---

# Cluster

> [!summary] In breve
> Gruppo di computer completi interconnessi che lavora come un'unica risorsa: scalabilità assoluta e incrementale, alta disponibilità, buon rapporto prezzo/prestazioni. Alternativa all'SMP.

- Metodi: passive standby, active secondary, server separati (con copia), server collegati ai dischi, server che condividono i dischi (serve un lock manager).
- Cluster **highly available** (le query in corso si perdono) vs **fault-tolerant** (sempre disponibile).
- **Failover**: spostare su un nodo alternativo. **Failback**: riportare sul nodo riparato (se automatico può "rimbalzare").
- Parallelizzazione: compilatore parallelizzante, applicazione parallelizzata (message passing), calcolo parametrico.

## Collegamenti

- **Concetti correlati**: [[Symmetric Multiprocessing]] · [[Tassonomia di Flynn]] · [[Sistema Distribuito]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[08 - SDC2 - Sistemi Distribuiti#Cluster|Lezione 8 — Cluster]]
> - [[08 - SDC2 - Sistemi Distribuiti#Metodi di clustering|Lezione 8 — Metodi di clustering]]
> - [[08 - SDC2 - Sistemi Distribuiti#Gestione dei guasti|Lezione 8 — Gestione dei guasti]]
