---
title: URL e URI
tags:
  - cyberbootcamp
  - concetto
  - web-security
  - http
---

# URL e URI

> [!summary] In breve
> Un URI **identifica** una risorsa; un URL è un URI che la **localizza**, cioè dice anche come e dove recuperarla in rete.

```
URI       = scheme ":" ["//" authority] path ["?" query] ["#" fragment]
authority = [userinfo "@"] host [":" port]
```

| Parte | Esempio in `https://example.com:80/blog?search=test#header` |
|---|---|
| scheme | `https` |
| host | `example.com` |
| port | `80` |
| path | `/blog` |
| query | `search=test` |
| fragment | `header` (resta nel browser, non arriva al server) |

- Path e query sono input dell'utente: primo posto dove cercare vulnerabilità.
- `https://google.com@evil.com/` → l'host è `evil.com`, `google.com` è *userinfo*.
- FQDN `somehost.example.com.` = subdomain . second-level domain . TLD . root.

## Collegamenti

- **Concetti correlati**: [[Percent Encoding]] · [[HTTP]] · [[DNS]]
- **Mappa**: [[MOC - CyberBootCamp]]

> [!info] Approfondimento
> - [[01 - CB - Web Insecurity 1#URL e URI|Lezione 1 — URL e URI]]
> - [[01 - CB - Web Insecurity 1#Fully Qualified Domain Name|Lezione 1 — Fully Qualified Domain Name]]
