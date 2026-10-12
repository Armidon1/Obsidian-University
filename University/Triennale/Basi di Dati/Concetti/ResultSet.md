---
title: ResultSet
tags:
  - basi-di-dati
  - concetto
  - accesso-da-software
  - java
---

# ResultSet

> [!summary] In breve
> Oggetto JDBC che scorre come un cursore le tuple del risultato di una query, leggendo le colonne con i metodi getXXX.

```java
ResultSet rs = stmt.executeQuery("SELECT COF_NAME, PRICE FROM COFFEES");
while (rs.next()) {                    // parte da prima della prima riga
    String s = rs.getString("COF_NAME");   // oppure getString(1)
    float n = rs.getFloat(2);
}
```
- Fa da ponte tra insiemi di tuple (SQL) e variabili singole (Java).
- `ResultSetMetaData`: `getColumnCount`, `getColumnLabel`, `getColumnType`…

## Collegamenti

- **Concetti correlati**: [[JDBC]] · [[PreparedStatement]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[04 - BD - Accesso ai Dati da Software#ResultSet e metodi getXXX|Lezione 4 — ResultSet e metodi getXXX]]
> - [[04 - BD - Accesso ai Dati da Software#Metadati di un ResultSet|Lezione 4 — Metadati di un ResultSet]]
