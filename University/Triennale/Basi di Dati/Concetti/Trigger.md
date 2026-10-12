---
title: Trigger
tags:
  - basi-di-dati
  - concetto
  - accesso-da-software
  - plpgsql
---

# Trigger

> [!summary] In breve
> Meccanismo che esegue automaticamente una stored procedure (RETURNS TRIGGER) quando su una tabella avviene un INSERT, DELETE o UPDATE.

```sql
CREATE TRIGGER t AFTER INSERT ON progetto
  FOR EACH ROW EXECUTE PROCEDURE assegna_progetto();
```
- `BEFORE` / `AFTER` / `INSTEAD OF` (solo viste); `FOR EACH ROW` / `FOR EACH STATEMENT` (default).
- `NEW` (insert/update), `OLD` (update/delete) nei trigger per riga.
- `BEFORE ... FOR EACH ROW` che restituisce `NULL` → l'operazione **non** avviene (es. vietare delete).
- Le operazioni del trigger fanno parte della transazione che l'ha attivato.
- Implementano i vincoli che `check` e `assertion` non permettono.

## Collegamenti

- **Concetti correlati**: [[Stored Procedure]] · [[Transazione]] · [[Vincolo Esterno]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[04 - BD - Accesso ai Dati da Software#Trigger|Lezione 4 — Trigger]]
> - [[04 - BD - Accesso ai Dati da Software#Semantica dei trigger|Lezione 4 — Semantica dei trigger]]
> - [[04 - BD - Accesso ai Dati da Software#Variabili NEW e OLD|Lezione 4 — Variabili NEW e OLD]]
> - [[04 - BD - Accesso ai Dati da Software#Trigger e transazioni, valore di ritorno|Lezione 4 — Trigger e transazioni, valore di ritorno]]
