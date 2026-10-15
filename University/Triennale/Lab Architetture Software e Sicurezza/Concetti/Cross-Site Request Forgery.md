---
title: Cross-Site Request Forgery
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
  - csrf
---

# Cross-Site Request Forgery

> [!summary] In breve
> OWASP A8: un sito esterno fa inviare al browser della vittima una richiesta verso un'app in cui è loggata; il browser allega da solo i cookie e l'azione viene eseguita.

```html
<img src="https://bank.com/transfer?to=attacker&amount=1000" width="0">
```

Condizioni: azione rilevante, sessione solo via cookie, nessun parametro imprevedibile.

Difesa: **token segreto** non inviato automaticamente (campo nascosto) in tutte le richieste sensibili; niente effetti collaterali con GET. In Rails: `protect_from_forgery` e `authenticity_token` nei form. Un XSS può aggirare il token.

## Collegamenti

- **Concetti correlati**: [[Cross-Site Scripting]] · [[Route HTTP e URI]] · [[Form Tag Helper]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A8 – Cross Site Request Forgery (CSRF)|Lezione 17 — A8 – Cross Site Request Forgery (CSRF)]]
> - [[17 - LASS - Sicurezza delle Web Application#Evitare le falle CSRF|Lezione 17 — Evitare le falle CSRF]]
