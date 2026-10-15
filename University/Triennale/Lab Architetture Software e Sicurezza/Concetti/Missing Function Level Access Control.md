---
title: Missing Function Level Access Control
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
  - autorizzazione
---

# Missing Function Level Access Control

> [!summary] In breve
> OWASP A7: funzioni o pagine riservate raggiungibili digitando direttamente l'URL, perché il controllo è solo nel nascondere i link.

`/user/getAccounts` → `/admin/getAccounts`.

Per ogni funzione: richiedere l'autenticazione, verificare ruolo e permessi, vietare i tipi di file non autorizzati. Modello **deny by default** a ogni livello. In Rails: [[Controller Filter]] (`before_action :require_admin`), test dei sad path con Cucumber.

## Collegamenti

- **Concetti correlati**: [[Insecure Direct Object Reference]] · [[Controller Filter]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A7 – Missing Function Level Access Control|Lezione 17 — A7 – Missing Function Level Access Control]]
