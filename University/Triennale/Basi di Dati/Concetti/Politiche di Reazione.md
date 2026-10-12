---
title: Politiche di Reazione
tags:
  - basi-di-dati
  - concetto
  - sql
  - vincoli
---

# Politiche di Reazione

> [!summary] In breve
> Le azioni (no action, restrict, cascade, set null, set default) eseguite quando una cancellazione o modifica della tupla padre violerebbe una foreign key.

| Politica | Effetto sulla tupla figlia |
|---|---|
| `no action` (default) | errore alla verifica (a fine transazione se *deferred*) |
| `restrict` | errore immediato |
| `cascade` | cancellata/aggiornata |
| `set null` / `set default` | foreign key a NULL / al default |

- Vincoli `deferrable` + `set constraints nome deferred` → controllo a fine transazione (in PostgreSQL: unique, primary key, foreign key, exclude; **non** not null).

## Collegamenti

- **Concetti correlati**: [[Foreign Key]] · [[Transazione]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[03 - BD - SQL#Politiche di reazione sulle foreign key|Lezione 3 — Politiche di reazione sulle foreign key]]
> - [[03 - BD - SQL#Vincoli deferred|Lezione 3 — Vincoli deferred]]
