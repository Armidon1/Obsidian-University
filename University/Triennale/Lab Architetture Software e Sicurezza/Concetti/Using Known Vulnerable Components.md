---
title: Using Known Vulnerable Components
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
  - dipendenze
---

# Using Known Vulnerable Components

> [!summary] In breve
> OWASP A9: librerie e framework con vulnerabilità note, spesso nemmeno conosciuti dagli sviluppatori, sfruttabili con strumenti automatici.

- 29 milioni di download di librerie Java vulnerabili nel 2011.
- Difese: inventario delle dipendenze, controlli **automatici** a ogni build (obsolescenza + CVE), aggiornamenti.
- Strumenti: Maven Versions plugin (Java); `bundle outdated`, bundler-audit, Dependabot (Ruby/Rails).

## Collegamenti

- **Concetti correlati**: [[Security Misconfiguration]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A9 – Using Known Vulnerable Components|Lezione 17 — A9 – Using Known Vulnerable Components]]
> - [[17 - LASS - Sicurezza delle Web Application#Cosa si può fare?|Lezione 17 — Cosa si può fare?]]
