---
title: Group By e Having
tags:
  - basi-di-dati
  - concetto
  - sql
---

# Group By e Having

> [!summary] In breve
> group by divide le tuple in gruppi con gli stessi valori e produce una riga per gruppo; having filtra i gruppi, where filtra le tuple prima del raggruppamento.

```sql
select t.padre, avg(f.reddito)
from persone f join paternita t on f.nome = t.figlio
where f.eta < 30               -- tuple che formano i gruppi
group by t.padre
having avg(f.reddito) > 20     -- gruppi
```
- Target list **omogenea**: solo attributi della `group by` e aggregati (PostgreSQL dà errore, MySQL sceglie un valore a caso).
- Non usare alias della target list nella `having`.

## Collegamenti

- **Concetti correlati**: [[Operatori Aggregati]] · [[Select SQL]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[03 - BD - SQL#Raggruppamenti, group by|Lezione 3 — Raggruppamenti, group by]]
> - [[03 - BD - SQL#Raggruppamenti e target list|Lezione 3 — Raggruppamenti e target list]]
> - [[03 - BD - SQL#Condizioni sui gruppi, having|Lezione 3 — Condizioni sui gruppi, having]]
