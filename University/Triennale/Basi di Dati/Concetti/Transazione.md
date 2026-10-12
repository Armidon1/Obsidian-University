---
title: Transazione
tags:
  - basi-di-dati
  - concetto
  - sql
  - transazioni
---

# Transazione

> [!summary] In breve
> Sequenza di operazioni indivisibile che rispetta le proprietà ACID; in SQL delimitata da begin e commit/rollback.

| | Proprietà |
|---|---|
| **A**tomicità | tutto o niente |
| **C**onsistenza | vincoli soddisfatti alla fine (anche se *deferred* durante) |
| **I**solamento | esecuzioni concorrenti equivalenti a quelle separate |
| **D**urabilità | dopo il commit l'effetto è permanente |

```sql
begin transaction;
  set transaction isolation level serializable;
  update ...; update ...;
end;   -- commit; rollback disfa
```

## Collegamenti

- **Concetti correlati**: [[Politiche di Reazione]] · [[Trigger]] · [[DBMS]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[03 - BD - SQL#Transazioni|Lezione 3 — Transazioni]]
> - [[03 - BD - SQL#Vincoli deferred|Lezione 3 — Vincoli deferred]]
