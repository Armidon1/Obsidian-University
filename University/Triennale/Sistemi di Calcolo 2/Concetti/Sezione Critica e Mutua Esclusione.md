---
title: Sezione Critica e Mutua Esclusione
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
---

# Sezione Critica e Mutua Esclusione

> [!summary] In breve
> Sezione critica: codice che accede a risorse condivise. Mutua esclusione: un solo processo alla volta nella sezione critica di una certa risorsa, senza deadlock né starvation.

Requisiti:

1. mutua esclusione garantita;
2. chi si ferma fuori dalla sezione critica non deve bloccare gli altri;
3. niente deadlock né starvation;
4. se la sezione è libera, si entra subito;
5. nessuna ipotesi su velocità e numero dei processi;
6. tempo finito nella sezione critica.

- Problemi dei processi in competizione: mutua esclusione, deadlock, starvation.
- Soluzioni: hardware (interrupt, compare&swap, exchange), software (Dekker, Dijkstra, panettiere), OS e linguaggio (semafori, monitor, messaggi).

## Collegamenti

- **Concetti correlati**: [[Compare and Swap]] · [[Semafori]] · [[Monitor]] · [[Algoritmo di Dekker]] · [[Algoritmo del Panettiere]] · [[Deadlock]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[02 - SDC2 - Concorrenza#Terminologia|Lezione 2 — Terminologia]]
> - [[02 - SDC2 - Concorrenza#Processi in competizione|Lezione 2 — Processi in competizione]]
> - [[02 - SDC2 - Concorrenza#Requisiti per la mutua esclusione|Lezione 2 — Requisiti per la mutua esclusione]]
