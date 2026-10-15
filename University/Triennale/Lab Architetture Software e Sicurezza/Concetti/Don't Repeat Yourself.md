---
title: Don't Repeat Yourself
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - rails
  - principi
---

# Don't Repeat Yourself

> [!summary] In breve
> Principio DRY: ogni elemento di conoscenza deve avere una rappresentazione unica, non ambigua e autorevole nel sistema.

Esempi in Rails:
- le colonne della tabella definiscono gli attributi del model (non si ripetono nella classe);
- gli helper di route (`movie_path(m)`) invece degli URI scritti a mano;
- [[View Partial]], [[Model Validation]], [[Controller Filter]], `Background` in Cucumber.

È la linea guida *implement once* dell'architettura.

## Collegamenti

- **Concetti correlati**: [[Convention over Configuration]] · [[Ruby on Rails]] · [[Linee Guida di Progettazione Architetturale]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[05 - LASS - Rails Parte 1#Don't Repeat Yourself|Lezione 5 — Don't Repeat Yourself]]
> - [[06 - LASS - Rails Parte 2#DRY Ways to Write MVC Code|Lezione 6 — DRY Ways to Write MVC Code]]
