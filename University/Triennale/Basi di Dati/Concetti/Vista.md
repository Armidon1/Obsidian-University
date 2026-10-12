---
title: Vista
tags:
  - basi-di-dati
  - concetto
  - sql
---

# Vista

> [!summary] In breve
> Tabella virtuale la cui istanza è derivata da altre tabelle tramite una query, calcolata solo quando viene usata.

```sql
create view etaReddito(eta, totaleReddito) as
  select eta, sum(reddito) from persone group by eta
```
- **Inline**: query tra parentesi nella `from`, o `with`.
- `create temporary view/table`: spariscono a fine sessione.
- Nella progettazione logica le viste **ricostruiscono** le tabelle originali dopo decomposizioni e accorpamenti.

## Collegamenti

- **Concetti correlati**: [[Interrogazioni Annidate]] · [[Ristrutturazione dello Schema Logico]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[03 - BD - SQL#Query annidate nella from, viste inline|Lezione 3 — Query annidate nella from, viste inline]]
> - [[03 - BD - SQL#Viste|Lezione 3 — Viste]]
