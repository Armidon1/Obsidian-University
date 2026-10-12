---
title: Algebra Relazionale
tags:
  - basi-di-dati
  - concetto
  - algebra-relazionale
---

# Algebra Relazionale

> [!summary] In breve
> Linguaggio di interrogazione procedurale i cui operatori prendono relazioni e restituiscono relazioni (chiusura), quindi si possono comporre.

| Operatore | Notazione | Effetto |
|---|---|---|
| unione, intersezione, differenza | $\cup, \cap, -$ | stessi attributi |
| ridenominazione | $\text{REN}_{A \leftarrow B}$ | cambia nomi, istanza invariata |
| selezione | $\text{SEL}_{cond}$ | righe |
| proiezione | $\text{PROJ}_{lista}$ | colonne (elimina duplicati) |
| join | $\text{JOIN}$, $\text{JOIN}_{cond}$ | combina relazioni |

Base teorica di SQL; due espressioni sono **equivalenti** se danno lo stesso risultato su ogni istanza (es. anticipare le selezioni).

## Collegamenti

- **Concetti correlati**: [[Selezione e Proiezione]] · [[Join]] · [[Negazione in Algebra Relazionale]] · [[SQL]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Gli operatori|Lezione 2 — Gli operatori]]
> - [[02 - BD - Modello Relazionale#Operatori insiemistici|Lezione 2 — Operatori insiemistici]]
> - [[02 - BD - Modello Relazionale#Ridenominazione|Lezione 2 — Ridenominazione]]
> - [[02 - BD - Modello Relazionale#Equivalenza di espressioni|Lezione 2 — Equivalenza di espressioni]]
