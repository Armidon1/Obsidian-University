---
title: SQL Injection (Basi di Dati)
tags:
  - basi-di-dati
  - concetto
  - accesso-da-software
  - sicurezza
---

# SQL Injection (Basi di Dati)

> [!summary] In breve
> Attacco in cui l'input dell'utente, concatenato in una stringa SQL, ne cambia la struttura; si previene con i prepared statement.

```java
st.executeQuery("SELECT nomepers FROM persona WHERE citta='" + s + "'");
// s = ' OR 1=1 --   →   ... WHERE citta='' OR 1=1 --'   → tutte le persone
```
- `--` commenta il resto; `1=1` è sempre vero.
- Con `PreparedStatement` + `setString(1, s)` la query è già compilata: `s` è solo un **valore** e la query non restituisce nulla.
- Approfondimento di sicurezza: [[SQL Injection]].

## Collegamenti

- **Concetti correlati**: [[PreparedStatement]] · [[JDBC]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[04 - BD - Accesso ai Dati da Software#Statement e PreparedStatement, la SQL injection|Lezione 4 — Statement e PreparedStatement, la SQL injection]]
