---
title: Unvalidated Redirects and Forwards
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
---

# Unvalidated Redirects and Forwards

> [!summary] In breve
> OWASP A10: la destinazione di un redirect o di un forward viene presa da un parametro dell'utente, permettendo phishing o l'aggiramento dei controlli di accesso.

| | Redirect | Forward |
|---|---|---|
| Dove | browser (3xx) | server, interno |
| Rischio | `?dest=www.evilsite.com` → phishing | `?dest=/admin` → scavalca il filtro |

Difese: evitarli, non usare parametri utente, **mappatura lato server** (`dest=2`), validare l'URL calcolato. In Rails: `redirect_to` solo verso route interne (da Rails 7 errore per host esterni).

## Collegamenti

- **Concetti correlati**: [[Missing Function Level Access Control]] · [[Insecure Direct Object Reference]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A10 – Unvalidated Redirects and Forwards|Lezione 17 — A10 – Unvalidated Redirects and Forwards]]
> - [[17 - LASS - Sicurezza delle Web Application#Redirect non validato illustrato|Lezione 17 — Redirect non validato illustrato]]
> - [[17 - LASS - Sicurezza delle Web Application#Forward non validato illustrato|Lezione 17 — Forward non validato illustrato]]
