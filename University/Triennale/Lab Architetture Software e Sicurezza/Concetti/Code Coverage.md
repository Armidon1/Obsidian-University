---
title: Code Coverage
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - testing
---

# Code Coverage

> [!summary] In breve
> Misura di quanto codice i test esercitano, a livelli crescenti: S0 metodi, S1 punti di chiamata, C0 istruzioni, C1 rami, C1+decisione sottoespressioni, C2 cammini.

| Livello | Richiede |
|---|---|
| S0 | ogni metodo chiamato |
| S1 | ogni metodo da ogni call site |
| C0 | ogni istruzione (SimpleCov) |
| C1 | ogni ramo in entrambe le direzioni |
| C1 + decision | ogni sottoespressione vera e falsa |
| C2 | ogni cammino |

Rapporto righe di test / codice di 1,2–1,5 ragionevole. La copertura indica cosa **non** è testato, non garantisce la correttezza.

## Collegamenti

- **Concetti correlati**: [[Unit, Functional e Integration Test]] · [[RSpec]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[15 - LASS - Testing BDD e TDD#Quanto testing basta?|Lezione 15 — Quanto testing basta?]]
> - [[15 - LASS - Testing BDD e TDD#Misurare la copertura|Lezione 15 — Misurare la copertura]]
