---
title: Interrogazioni Annidate
tags:
  - basi-di-dati
  - concetto
  - sql
---

# Interrogazioni Annidate

> [!summary] In breve
> Una select dentro un'altra (where, from, target list, having); concettualmente valutata per ogni tupla esterna. Correlata se usa alias del blocco esterno.

| Operatore | Significato |
|---|---|
| `= (select ...)` | la sottoquery deve dare al più un valore |
| `any` / `in` (= `= any`) | vero per almeno un valore |
| `all` / `not in` (= `<> all`) | vero per tutti |
| `exists` | sottoquery non vuota |

```sql
select distinct padre from paternita z
where not exists (select * from paternita p join persone f on p.figlio = f.nome
                  where z.padre = p.padre and f.reddito <= 20)
```
- Visibilità: come nei linguaggi a blocchi (no variabili interne nei blocchi esterni o fratelli).
- Viste inline nella `from` e `with nome as (...)`.

## Collegamenti

- **Concetti correlati**: [[Select SQL]] · [[Negazione in Algebra Relazionale]] · [[Vista]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[03 - BD - SQL#Interrogazioni annidate|Lezione 3 — Interrogazioni annidate]]
> - [[03 - BD - SQL#Operatori per le sottoquery|Lezione 3 — Operatori per le sottoquery]]
> - [[03 - BD - SQL#Visibilità|Lezione 3 — Visibilità]]
> - [[03 - BD - SQL#Interrogazioni annidate e correlate|Lezione 3 — Interrogazioni annidate e correlate]]
