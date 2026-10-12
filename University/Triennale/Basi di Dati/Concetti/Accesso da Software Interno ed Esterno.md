---
title: Accesso da Software Interno ed Esterno
tags:
  - basi-di-dati
  - concetto
  - accesso-da-software
---

# Accesso da Software Interno ed Esterno

> [!summary] In breve
> Ai dati si accede da programmi in due modi: con moduli definiti dentro il DBMS (stored procedure, trigger) o da applicazioni esterne tramite un'API come JDBC.

| Interno | Esterno |
|---|---|
| codice nel livello dei dati | codice nel livello applicativo |
| PL/pgSQL (Turing completo) | Java + JDBC, Python, C… |
| riuso e ottimizzazione vicino ai dati | il programma si connette al DBMS |

`CallableStatement` collega i due: un programma esterno chiama una stored procedure.

## Collegamenti

- **Concetti correlati**: [[Stored Procedure]] · [[Trigger]] · [[JDBC]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[04 - BD - Accesso ai Dati da Software#Dove si colloca l'accesso da software|Lezione 4 — Dove si colloca l'accesso da software]]
> - [[04 - BD - Accesso ai Dati da Software#Due modi di accedere ai dati da software|Lezione 4 — Due modi di accedere ai dati da software]]
