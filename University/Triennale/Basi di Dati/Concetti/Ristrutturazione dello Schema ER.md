---
title: Ristrutturazione dello Schema ER
tags:
  - basi-di-dati
  - concetto
  - progettazione-logica
---

# Ristrutturazione dello Schema ER

> [!summary] In breve
> Prima fase della progettazione logica: elimina dallo schema ER i costrutti non traducibili in relazionale, mantenendo la semantica, e sceglie gli identificatori principali.

0. preparazione (vincoli impliciti rilevanti);
1. analisi delle **ridondanze** (in base al carico);
2. eliminazione degli **attributi multivalore** (reificazione);
3. eliminazione degli **attributi composti** (componenti o entità);
4. eliminazione di **ISA e generalizzazioni**;
5. scelta degli **identificatori principali**;
6. riformulazione dei **vincoli esterni**.

Risultato: tutte le entità disgiunte, un identificatore principale per ogni entità e relazione.

## Collegamenti

- **Concetti correlati**: [[Eliminazione delle ISA]] · [[Identificatore Principale]] · [[Traduzione Diretta]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[06 - BD - Progettazione Logica#6.2 Ristrutturazione dello schema ER|Lezione 6 — 6.2 Ristrutturazione dello schema ER]]
> - [[06 - BD - Progettazione Logica#Attività 0 e 1, preparazione e ridondanze|Lezione 6 — Attività 0 e 1, preparazione e ridondanze]]
> - [[06 - BD - Progettazione Logica#Attività 3, attributi composti|Lezione 6 — Attività 3, attributi composti]]
