---
title: Parser Differential
tags:
  - cyberbootcamp
  - concetto
  - web-security
---

# Parser Differential

> [!summary] In breve
> Due componenti interpretano lo stesso input in modo diverso: un filtro lo giudica innocuo, il componente successivo ci trova il payload.

- Catena tipica: Browser → Proxy → CDN → WAF → App Server; ognuno ha il suo parser.
- Esempi:
  - WAF che decodifica l'URL una volta, server che lo decodifica due volte (double encoding);
  - funzioni PHP che si fermano al null byte mentre il resto del codice no ([[Null Byte Injection]]).
- Si aggiungono i **comportamenti legacy** mantenuti per compatibilità.

## Collegamenti

- **Concetti correlati**: [[Percent Encoding]] · [[Null Byte Injection]] · [[Path Traversal]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[01 - CB - Web Insecurity 1#Il percorso di una richiesta e i parser differentials|Lezione 1 — Il percorso di una richiesta e i parser differentials]]
> - [[01 - CB - Web Insecurity 1#Path traversal: tips & tricks|Lezione 1 — Path traversal: tips & tricks]]
