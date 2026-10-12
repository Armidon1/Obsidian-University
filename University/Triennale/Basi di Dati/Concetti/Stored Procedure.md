---
title: Stored Procedure
tags:
  - basi-di-dati
  - concetto
  - accesso-da-software
  - plpgsql
---

# Stored Procedure

> [!summary] In breve
> Funzione scritta in un linguaggio procedurale del DBMS (in PostgreSQL PL/pgSQL), memorizzata nel database e invocabile da SQL o da un trigger.

```sql
CREATE OR REPLACE FUNCTION totale_fattura(sogg VARCHAR)
RETURNS TABLE (sgt VARCHAR, tot REAL) AS $$
DECLARE r record; totale REAL;
BEGIN
  totale := 0;
  FOR r IN SELECT * FROM fattura WHERE soggetto = sogg LOOP
    totale := totale + r.imponibile * (100 + r.aliquota) / 100;
  END LOOP;
  RETURN QUERY SELECT sogg, totale;
END; $$ LANGUAGE plpgsql;
```
- Vantaggio: gli utenti non scrivono query dirette → protezione e coerenza semantica.
- PL/pgSQL è Turing completo: calcola anche la chiusura transitiva.

## Collegamenti

- **Concetti correlati**: [[Trigger]] · [[Accesso da Software Interno ed Esterno]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[04 - BD - Accesso ai Dati da Software#PL/pgSQL|Lezione 4 — PL/pgSQL]]
> - [[04 - BD - Accesso ai Dati da Software#Sintassi di una stored procedure|Lezione 4 — Sintassi di una stored procedure]]
> - [[04 - BD - Accesso ai Dati da Software#Benefici delle stored procedure|Lezione 4 — Benefici delle stored procedure]]
