---
title: Normalizzazione e Denormalizzazione
tags:
  - basi-di-dati
  - concetto
  - progettazione-logica
---

# Normalizzazione e Denormalizzazione

> [!summary] In breve
> Una tabella è normalizzata se ogni attributo dipende funzionalmente dalla chiave; altrimenti ha ridondanze e anomalie. Le tabelle dalla traduzione diretta sono normalizzate; si denormalizza solo di proposito.

`Interesse(cliente, appartamento, valore)`: `valore` dipende solo da `appartamento` (parte della chiave).
- anomalia di **aggiornamento** (cambiare il valore in tutte le righe);
- di **cancellazione** (via il cliente, via il valore);
- di **inserimento** (non si registra un appartamento senza clienti).

Accorpamento per denormalizzazione: si accetta la ridondanza per evitare join frequenti, se i dati cambiano raramente.

## Collegamenti

- **Concetti correlati**: [[Ristrutturazione dello Schema Logico]] · [[Superchiave e Chiave]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[Third Normal Form 3NF]] · [[Star Schema]] · [[Snowflake Schema]]

> [!info] Approfondimento
> - [[06 - BD - Progettazione Logica#Normalizzazione e denormalizzazione|Lezione 6 — Normalizzazione e denormalizzazione]]
> - [[06 - BD - Progettazione Logica#Accorpamento caso 4, per denormalizzazione|Lezione 6 — Accorpamento caso 4, per denormalizzazione]]
