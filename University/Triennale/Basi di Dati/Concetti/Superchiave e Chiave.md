---
title: Superchiave e Chiave
tags:
  - basi-di-dati
  - concetto
  - vincoli
---

# Superchiave e Chiave

> [!summary] In breve
> Una superchiave è un insieme di attributi su cui non esistono due tuple uguali; una chiave è una superchiave minimale.

- Superchiave $K$: non esistono $t_1 \neq t_2$ con $t_1[K] = t_2[K]$.
- Chiave: superchiave da cui non si può togliere alcun attributo.
- L'insieme di tutti gli attributi è sempre superchiave → ogni relazione ha almeno una chiave.
- Il **vincolo** di chiave vale su **tutte** le istanze: si deduce dal dominio, non da un'istanza.
- Con NULL una chiave non garantisce l'identificazione → [[Chiave Primaria]].

## Collegamenti

- **Concetti correlati**: [[Chiave Primaria]] · [[Vincolo di Integrità]] · [[Identificatore ER]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Condizioni di superchiave e chiave|Lezione 2 — Condizioni di superchiave e chiave]]
> - [[02 - BD - Modello Relazionale#Vincolo di superchiave e vincolo di chiave|Lezione 2 — Vincolo di superchiave e vincolo di chiave]]
> - [[02 - BD - Modello Relazionale#Chiavi e valori nulli|Lezione 2 — Chiavi e valori nulli]]
