---
title: Broken Authentication e Session Management
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - sicurezza
  - owasp
  - sessioni
---

# Broken Authentication e Session Management

> [!summary] In breve
> OWASP A2: credenziali o session ID esposti o gestiti male permettono di impersonare un utente; il session ID vale quanto le credenziali.

- Esempio: session ID nell'URL → finisce nell'header `Referer` verso il sito dell'attaccante → account dirottato.
- Attenzione alle *side doors*: reset password, domande segrete, logout.
- Difese: TLS ovunque, sessioni standard del framework (in cookie), logout che distrugge la sessione, `reset_session` al login.

## Collegamenti

- **Concetti correlati**: [[Autenticazione]] · [[Password Storage]] · [[OWASP Top 10]] · [[Cross-Site Scripting]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[17 - LASS - Sicurezza delle Web Application#A2 – Broken Authentication and Session Management|Lezione 17 — A2 – Broken Authentication and Session Management]]
> - [[17 - LASS - Sicurezza delle Web Application#Broken Authentication illustrata|Lezione 17 — Broken Authentication illustrata]]
