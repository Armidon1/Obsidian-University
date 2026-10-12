---
title: PreparedStatement
tags:
  - basi-di-dati
  - concetto
  - accesso-da-software
  - java
---

# PreparedStatement

> [!summary] In breve
> Statement parametrico con '?' che il DBMS compila prima (piano di esecuzione) e istanzia a run-time con setXXX; riutilizzabile e immune alla SQL injection.

```java
PreparedStatement pst = conn.prepareStatement(
    "UPDATE COFFEES SET SALES = ? WHERE COF_NAME = ?");
pst.setInt(1, 75);
pst.setString(2, "Colombian");
pst.executeUpdate();
```
- I valori restano fino a una nuova `set` o a `clearParameters()`.
- `CallableStatement` (sottoclasse) chiama le stored procedure.

## Collegamenti

- **Concetti correlati**: [[JDBC]] · [[SQL Injection (Basi di Dati)]] · [[ResultSet]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[04 - BD - Accesso ai Dati da Software#PreparedStatement|Lezione 4 — PreparedStatement]]
> - [[04 - BD - Accesso ai Dati da Software#CallableStatement|Lezione 4 — CallableStatement]]
