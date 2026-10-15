---
title: Prepared Statement
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - database
  - injection
---

# Prepared Statement

> [!summary] In breve
> Query con segnaposto in cui i dati vengono passati separatamente dal codice SQL (bind variable), così l'interprete non può scambiarli per comandi.

```ruby
Movie.where("title = '#{params[:t]}'")   # vulnerabile
Movie.where("title = ?", params[:t])     # parametrizzata
Movie.where(title: params[:t])           # parametrizzata
```

Difesa principale contro la [[SQL Injection]], insieme a validazione white list e minimo privilegio sul database.

## Collegamenti

- **Concetti correlati**: [[SQL Injection]] · [[ActiveRecord Query Interface]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A1 – Injection|Lezione 17 — A1 – Injection]]
> - [[17 - LASS - Sicurezza delle Web Application#Evitare le injection|Lezione 17 — Evitare le injection]]
