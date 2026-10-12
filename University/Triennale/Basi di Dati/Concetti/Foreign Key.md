---
title: Foreign Key
tags:
  - basi-di-dati
  - concetto
  - vincoli
  - sql
---

# Foreign Key

> [!summary] In breve
> Vincolo di integrità referenziale: ogni combinazione non nulla di valori degli attributi X di R1 deve comparire come valore di una chiave Y di R2.

```
foreign key: Infrazioni[Vigile] ⊆ Vigili[Matricola]
```
- $Y$ deve essere una **chiave** (altrimenti è un vincolo di **inclusione**).
- I NULL non violano il vincolo; con più attributi conta la **combinazione**.
- Direzionale: possono esistere vigili senza infrazioni.
- SQL: `references`, `foreign key (...) references ...`, con [[Politiche di Reazione]].

## Collegamenti

- **Concetti correlati**: [[Chiave Primaria]] · [[Politiche di Reazione]] · [[Vincolo di Integrità]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Integrità referenziale|Lezione 2 — Integrità referenziale]]
> - [[02 - BD - Modello Relazionale#Vincoli di inclusione|Lezione 2 — Vincoli di inclusione]]
> - [[03 - BD - SQL#Vincoli in SQL|Lezione 3 — Vincoli in SQL]]
