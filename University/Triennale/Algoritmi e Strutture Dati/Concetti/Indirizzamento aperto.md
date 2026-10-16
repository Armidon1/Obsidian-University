---
title: Indirizzamento aperto
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - hashing
---

# Indirizzamento aperto

> [!summary] In breve
> Tutte le voci stanno nell'array stesso: in caso di collisione si prova una sequenza di celle alternative (scansione lineare, quadratica o doppio hashing); le rimozioni lasciano un marcatore `DEFUNCT`.

| Scansione | Celle provate ($i = 0, 1, 2, \dots$) | Problema |
|---|---|---|
| lineare | $(h(k) + i) \bmod N$ | **clustering primario** |
| quadratica | $(h(k) + i^2) \bmod N$ | clustering secondario; con $N$ primo e $\lambda < 1/2$ trova sempre un posto |
| doppio hashing | $(h(k) + i \cdot h'(k)) \bmod N$, $h'(k) \ne 0$ | — |

- Rimozione: non si può svuotare la cella (interromperebbe le sequenze di ricerca) → marcatore `DEFUNCT`, saltato dalle ricerche e riutilizzabile negli inserimenti.
- Serve $\lambda < 0.5$. Niente strutture ausiliarie: risparmio di spazio. (`ProbeHashMap` del libro.)

## Collegamenti

- **Concetti correlati**: [[Tabella hash]] · [[Concatenazione separata]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Indirizzamento aperto|Lezione 10 — Indirizzamento aperto]]
