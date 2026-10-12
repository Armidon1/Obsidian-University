---
title: Algoritmo del Banchiere
tags:
  - sistemi-di-calcolo-2
  - concetto
  - deadlock
---

# Algoritmo del Banchiere

> [!summary] In breve
> Uno stato è safe se esiste un ordine in cui tutti i processi possono terminare. Si concede una richiesta solo se lo stato risultante è safe.

Strutture: R (risorse totali), V (disponibili), C (richieste massime), A (allocate), C − A (ciò che manca).

```c
boolean safe(state S) {
    currentavail = available; rest = {tutti};
    while (esiste Pk in rest con claim[k] - alloc[k] <= currentavail) {
        currentavail += alloc[k];   // Pk termina e restituisce le risorse
        rest -= {Pk};
    }
    return rest == {};
}
```

- Esempio safe: P2 → P1 → P3 → P4. Esempio unsafe: a tutti manca una unità di R1 e V(R1) = 0.
- Unsafe ≠ deadlock: significa solo che non si può più garantire di evitarlo.

## Collegamenti

- **Concetti correlati**: [[Gestione del Deadlock]] · [[Deadlock]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Stato safe|Lezione 3 — Stato safe]]
> - [[03 - SDC2 - Deadlock#L'algoritmo|Lezione 3 — L'algoritmo]]
