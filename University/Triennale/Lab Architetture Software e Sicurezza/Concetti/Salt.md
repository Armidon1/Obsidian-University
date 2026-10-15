---
title: Salt
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - password
  - crittografia
---

# Salt

> [!summary] In breve
> Stringa casuale diversa per ogni password, salvata in chiaro accanto all'hash e mescolata alla password prima di calcolarlo.

- Due utenti con la stessa password hanno hash diversi.
- Le [[Rainbow Table]] precalcolate diventano inutili.
- L'attaccante deve attaccare una password alla volta.
- Non basta da solo: con una funzione veloce (SHA-1) le password deboli cadono comunque → [[Bcrypt]].

## Collegamenti

- **Concetti correlati**: [[Password Storage]] · [[Bcrypt]] · [[Rainbow Table]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[14 - LASS - Autenticazione#Soluzione 4 - hash con salt per password|Lezione 14 — Soluzione 4 - hash con salt per password]]
