---
title: Lettori-Scrittori
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
  - problemi-classici
---

# Lettori-Scrittori

> [!summary] In breve
> Più lettori possono leggere insieme, uno scrittore scrive da solo e mentre scrive nessuno legge. La soluzione con `readcount` dà priorità ai lettori e può affamare gli scrittori.

```c
writer: wait(wsem); WRITE(); signal(wsem);
reader: wait(x); readcount++; if (readcount == 1) wait(wsem); signal(x);
        READ();
        wait(x); readcount--; if (readcount == 0) signal(wsem); signal(x);
```

- `x` protegge `readcount`; il primo lettore blocca gli scrittori, l'ultimo li sblocca.
- **Starvation degli scrittori** se i lettori continuano ad arrivare: serve una variante con priorità agli scrittori.

## Collegamenti

- **Concetti correlati**: [[Semafori]] · [[Produttore-Consumatore]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[02 - SDC2 - Concorrenza#Lettori/scrittori|Lezione 2 — Lettori/scrittori]]
