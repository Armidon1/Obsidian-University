---
title: Sensitive Data Exposure
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
  - crittografia
---

# Sensitive Data Exposure

> [!summary] In breve
> OWASP A6: dati sensibili memorizzati o trasmessi senza protezione adeguata, spesso in posti dimenticati come log e backup.

- **A riposo**: identificare tutti i dati sensibili e dove finiscono (log!), cifrarli con algoritmi standard e gestione corretta delle chiavi; password con [[Bcrypt]].
- **In transito**: TLS su tutte le connessioni (anche interne), HSTS, verifica dei certificati.
- In Rails: `filter_parameters` (niente password nei log), `force_ssl`.

## Collegamenti

- **Concetti correlati**: [[Password Storage]] · [[Security Misconfiguration]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A6 – Sensitive Data Exposure|Lezione 17 — A6 – Sensitive Data Exposure]]
> - [[17 - LASS - Sicurezza delle Web Application#Insecure Cryptographic Storage|Lezione 17 — Insecure Cryptographic Storage]]
> - [[17 - LASS - Sicurezza delle Web Application#Insufficient Transport Layer Protection|Lezione 17 — Insufficient Transport Layer Protection]]
