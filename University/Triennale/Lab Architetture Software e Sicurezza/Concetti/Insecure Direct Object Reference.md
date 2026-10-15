---
title: Insecure Direct Object Reference
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
  - autorizzazione
---

# Insecure Direct Object Reference

> [!summary] In breve
> OWASP A4: l'app usa riferimenti diretti agli oggetti (id, nomi di file) nei parametri senza verificare lato server che l'utente possa accedervi.

`/user?acct=6065` → `/user?acct=6066` → conto di un altro.

- Il controllo "a livello di presentazione" (mostrare solo i link giusti) non funziona.
- Difese: **access reference map** per utente, oppure verifica di autorizzazione per ogni oggetto, meglio con un vincolo nella query:

```ruby
@review = current_user.reviews.find(params[:id])
```

## Collegamenti

- **Concetti correlati**: [[Missing Function Level Access Control]] · [[REST]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A4 – Insecure Direct Object References|Lezione 17 — A4 – Insecure Direct Object References]]
> - [[17 - LASS - Sicurezza delle Web Application#Insecure Direct Object References illustrata|Lezione 17 — Insecure Direct Object References illustrata]]
