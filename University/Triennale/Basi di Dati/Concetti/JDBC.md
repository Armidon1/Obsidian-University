---
title: JDBC
tags:
  - basi-di-dati
  - concetto
  - accesso-da-software
  - java
---

# JDBC

> [!summary] In breve
> API Java standard per eseguire comandi SQL su un DBMS tramite un driver specifico; l'interazione ha quattro fasi.

```mermaid
flowchart LR
    A["1. Class.forName(driver)"] --> B["2. DriverManager.getConnection(url, user, pwd)"]
    B --> C["3. Statement / PreparedStatement → ResultSet"]
    C --> D["4. close()"]
```
- URL: `jdbc:postgresql:test`.
- `executeUpdate` (DDL e modifiche, restituisce il numero di tuple) / `executeQuery` (restituisce un ResultSet).
- Stringhe SQL tra apici singoli dentro stringhe Java tra apici doppi, senza `;` finale.

## Collegamenti

- **Concetti correlati**: [[ResultSet]] · [[PreparedStatement]] · [[Accesso da Software Interno ed Esterno]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[04 - BD - Accesso ai Dati da Software#Il framework JDBC|Lezione 4 — Il framework JDBC]]
> - [[04 - BD - Accesso ai Dati da Software#Le fasi dell'interazione|Lezione 4 — Le fasi dell'interazione]]
> - [[04 - BD - Accesso ai Dati da Software#Terza fase, Statement|Lezione 4 — Terza fase, Statement]]
