---
title: Valore Nullo
tags:
  - basi-di-dati
  - concetto
  - modello-relazionale
  - sql
---

# Valore Nullo

> [!summary] In breve
> NULL è un valore speciale che indica l'assenza di un valore del dominio; ogni condizione su NULL è falsa, tranne IS NULL / IS NOT NULL.

| Interpretazione | Esempio |
|---|---|
| sconosciuto | Firenze ha una prefettura, indirizzo ignoto |
| inesistente | Tivoli non ha prefettura |
| senza informazione (quella dei DBMS) | Prato: non si sa |

- Non usare valori "speciali" (0, "999") al posto di NULL.
- `Età > 40 OR Età <= 40` **non** prende le tuple con età nulla.
- Aggregati: ignorano i NULL (`count(*)` no). Chiave primaria: niente NULL. Foreign key: i NULL non la violano.

## Collegamenti

- **Concetti correlati**: [[Chiave Primaria]] · [[Foreign Key]] · [[Operatori Aggregati]] · [[Join Esterno]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[NULL and Three-Valued Logic]] · [[NULL and Aggregate Functions]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Informazione incompleta e valori nulli|Lezione 2 — Informazione incompleta e valori nulli]]
> - [[02 - BD - Modello Relazionale#Il valore nullo nell'algebra|Lezione 2 — Il valore nullo nell'algebra]]
> - [[03 - BD - SQL#Valori nulli, is null e is not null|Lezione 3 — Valori nulli, is null e is not null]]
