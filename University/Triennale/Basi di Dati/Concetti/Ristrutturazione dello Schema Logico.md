---
title: Ristrutturazione dello Schema Logico
tags:
  - basi-di-dati
  - concetto
  - progettazione-logica
---

# Ristrutturazione dello Schema Logico

> [!summary] In breve
> Ultima fase della progettazione logica: decomposizioni e accorpamenti di tabelle guidati dal carico applicativo, ricostruendo le tabelle originali con viste.

| Operazione | Quando | Ricostruzione |
|---|---|---|
| decomposizione verticale | attributi acceduti separatamente | join su K |
| decomposizione orizzontale | fasce di tuple accedute separatamente | unione |
| decomposizione mista | evitare NULL | join esterno |
| accorpamento (fortemente/debolmente accoppiate) | evitare join | proiezioni (+ flag) |
| accorpamento orizzontale | sottotipi acceduti insieme | attributo Tipo |
| per denormalizzazione | join frequente, dati stabili | proiezione |

Senza indicazioni sul carico non si ristruttura.

## Collegamenti

- **Concetti correlati**: [[Modello di Costo]] · [[Normalizzazione e Denormalizzazione]] · [[Vista]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[06 - BD - Progettazione Logica#6.4 Ristrutturazione dello schema logico|Lezione 6 — 6.4 Ristrutturazione dello schema logico]]
> - [[06 - BD - Progettazione Logica#Operazioni di ristrutturazione|Lezione 6 — Operazioni di ristrutturazione]]
> - [[06 - BD - Progettazione Logica#Decomposizione verticale|Lezione 6 — Decomposizione verticale]]
> - [[06 - BD - Progettazione Logica#Accorpamento caso 1, tabelle fortemente accoppiate|Lezione 6 — Accorpamento caso 1, tabelle fortemente accoppiate]]
