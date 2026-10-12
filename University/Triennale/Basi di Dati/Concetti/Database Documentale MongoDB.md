---
title: Database Documentale MongoDB
tags:
  - basi-di-dati
  - concetto
  - nosql
  - mongodb
---

# Database Documentale MongoDB

> [!summary] In breve
> MongoDB è un DBMS NoSQL document-oriented: collezioni di documenti JSON senza schema rigido, con _id come chiave primaria e senza vincoli referenziali.

| MongoDB | Relazionale |
|---|---|
| collezione | tabella |
| documento | riga |
| campo | colonna |

```js
db.anagrafica.insert({nome: "Marco", eta: 22})
db.anagrafica.find({nome: "Mario"}, {eta: 1})    // SELECT _id, eta ... WHERE nome = 'Mario'
db.anagrafica.update({nome: "Mario"}, {$set: {eta: 45}}, {multi: true})
db.orders.aggregate({$lookup: {from: "products", localField: "item", foreignField: "_id", as: "p"}})
```
- Correlazioni con `_id` replicati o array; join con `$lookup` (pipeline `aggregate`).

## Collegamenti

- **Concetti correlati**: [[NoSQL]] · [[JSON]] · [[Graph Database]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[07 - BD - NoSQL#7.2 Document-oriented database, MongoDB|Lezione 7 — 7.2 Document-oriented database, MongoDB]]
> - [[07 - BD - NoSQL#Interrogazioni, find|Lezione 7 — Interrogazioni, find]]
> - [[07 - BD - NoSQL#Il join con $lookup|Lezione 7 — Il join con $lookup]]
