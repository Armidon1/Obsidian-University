---
title: Content Distribution Network
tags:
  - telecomunicazioni
  - concetto
  - video
  - cdn
  - cache
---

# Content Distribution Network

> [!summary] In breve
> Una **CDN** è una rete di server (cluster) distribuiti che conservano copie dei contenuti e servono ogni utente dal cluster più adatto. La scelta avviene di solito tramite il **DNS**.

- Problemi di un unico data center: distanza e colli di bottiglia, banda sprecata per i video popolari, unico punto di rottura.
- **CDN privata** (Google per YouTube) o **di terze parti** (Akamai, Limelight).

| Enter deep | Bring home |
| --- | --- |
| cluster dentro gli ISP di accesso (Akamai, ~1700 siti) | pochi grandi cluster nei PoP/IXP |
| vicino agli utenti | più facile da gestire |

- **Redirezione DNS** (NetCinema → KingCDN): l'autoritativo di NetCinema risponde con un nome di KingCDN (`a1105.kingcdn.com`), e il DNS di KingCDN restituisce l'IP del server scelto.
- **Selezione del cluster**: il più vicino geograficamente all'LDNS, oppure misure in tempo reale di ritardo e perdite.
- I contenuti si recuperano su richiesta, come in una cache.

## Collegamenti

- **Concetti correlati**: [[DASH]] · [[Web Caching]] · [[Gerarchia dei DNS Server]] · [[Gerarchia degli ISP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Reti per la distribuzione di contenuti (CDN)|Capitolo 2 — Reti per la distribuzione di contenuti (CDN)]]
> - [[02 - TLC - Livello di applicazione#Come funziona una CDN|Capitolo 2 — Come funziona una CDN]]
> - [[02 - TLC - Livello di applicazione#Strategie di selezione dei cluster|Capitolo 2 — Strategie di selezione dei cluster]]
