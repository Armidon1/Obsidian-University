---
title: Select SQL
tags:
  - basi-di-dati
  - concetto
  - sql
---

# Select SQL

> [!summary] In breve
> L'istruzione di interrogazione di SQL: equivale a proiezione della selezione sul prodotto cartesiano delle tabelle nella from, valutata in un ordine logico preciso.

```sql
select   <target list>        -- espressioni, as, distinct, case
from     R1, R2 ... | join    -- prodotto cartesiano / join
where    <condizione>         -- sulle tuple
group by <attributi>
having   <condizione su gruppi>
order by <attributi> [desc]
limit    n
```
$$\text{PROJ}_{\text{target}}(\text{SEL}_{\text{cond}}(R_1 \times \dots \times R_n))$$
- Ordine logico: from → where → group by → having → select → order by → limit.
- Il DBMS non calcola davvero il prodotto cartesiano: ottimizza.

## Collegamenti

- **Concetti correlati**: [[SQL]] · [[Join]] · [[Group By e Having]] · [[Interrogazioni Annidate]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[Logical Order of SQL Query Evaluation]] · [[SQL Aliases and Attribute Qualification]]

> [!info] Approfondimento
> - [[03 - BD - SQL#L'istruzione select|Lezione 3 — L'istruzione select]]
> - [[03 - BD - SQL#Selezione, proiezione e join|Lezione 3 — Selezione, proiezione e join]]
> - [[03 - BD - SQL#Sintassi riassuntiva della select|Lezione 3 — Sintassi riassuntiva della select]]
