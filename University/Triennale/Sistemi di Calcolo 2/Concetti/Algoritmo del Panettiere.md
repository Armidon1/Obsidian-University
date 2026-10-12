---
title: Algoritmo del Panettiere
tags:
  - sistemi-di-calcolo-2
  - concetto
  - mutua-esclusione
  - algoritmi
  - esame
---

# Algoritmo del Panettiere

> [!summary] In breve
> Ogni processo prende un biglietto 1 + max dei biglietti altrui ed entra in ordine (biglietto, ID). L'array `choosing` impedisce di scavalcare chi sta ancora scegliendo. ME, ND e NS senza letture/scritture atomiche.

```c
choosing[i] = true;
number[i] = 1 + max(number[j]);
choosing[i] = false;
for j != i {
    while (choosing[j]);
    while (number[j] != 0 && (number[j], j) < (number[i], i));
}
/* CS */
number[i] = 0;
```

- Errori tipici: (1) confronto solo sul numero → due processi con lo stesso biglietto entrano insieme; (2) senza `choosing` → un processo legge `number[j] = 0` mentre j sta per scegliere.
- Ogni variabile ha un solo scrittore: si porta in un **sistema distribuito** con messaggi (thread client + thread server).
- Variante con biglietti limitati: `% MAXIMUM`.

## Collegamenti

- **Concetti correlati**: [[Algoritmo di Dijkstra per la Mutua Esclusione]] · [[Algoritmo di Dekker]] · [[Sezione Critica e Mutua Esclusione]] · [[Sistema Distribuito]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[04 - SDC2 - Algoritmo del Panettiere#L'idea del panettiere|Lezione 4 — L'idea del panettiere]]
> - [[04 - SDC2 - Algoritmo del Panettiere#Bakery algorithm corretto|Lezione 4 — Bakery algorithm corretto]]
> - [[04 - SDC2 - Algoritmo del Panettiere#Bakery in un'applicazione client/server|Lezione 4 — Bakery in un'applicazione client/server]]
