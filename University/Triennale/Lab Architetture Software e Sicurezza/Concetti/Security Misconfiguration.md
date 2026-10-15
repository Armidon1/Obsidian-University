---
title: Security Misconfiguration
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
---

# Security Misconfiguration

> [!summary] In breve
> OWASP A5: configurazioni insicure in qualsiasi strato (patch mancanti, account di default, funzionalità inutili attive, segreti in repository o server di test).

- La sicurezza non deve dipendere dal codice sorgente segreto.
- Tutte le credenziali cambiano in produzione.
- Difese: hardening **automatizzato** di tutta la piattaforma, configurazione verificabile ("se non si può verificare non è sicuro"), scansioni.
- In Rails: niente ambiente development in produzione, niente `master.key` o API key su git.

## Collegamenti

- **Concetti correlati**: [[Using Known Vulnerable Components]] · [[Sensitive Data Exposure]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A5 – Security Misconfiguration|Lezione 17 — A5 – Security Misconfiguration]]
