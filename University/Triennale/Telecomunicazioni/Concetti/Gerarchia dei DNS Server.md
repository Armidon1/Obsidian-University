---
title: Gerarchia dei DNS Server
tags:
  - telecomunicazioni
  - concetto
  - dns
---

# Gerarchia dei DNS Server

> [!summary] In breve
> Il DNS è un database **distribuito e gerarchico**: root server → TLD server → server autoritativi, più il **DNS server locale** di ogni ISP che fa da proxy per gli host. Usa UDP sulla porta 53.

| Livello | Ruolo |
| --- | --- |
| **Root** | 400 server, 13 organizzazioni; restituiscono gli IP dei TLD |
| **TLD** | `com`, `org`, `edu`, `uk`, `fr`…; restituiscono gli IP degli autoritativi |
| **Autoritativi** | record dei server pubblici di un'organizzazione (primario + secondario) |
| **Locale** (default name server) | non è nella gerarchia; riceve le query degli host e le inoltra; indirizzo fornito via DHCP |

- Perché non centralizzato: unico punto di fallimento, troppo traffico, distanza, manutenzione. **Non scala**.
- Servizi: traduzione nome → IP, **host aliasing**, **mail server aliasing**, **distribuzione del carico** (rotazione degli IP).
- **Caching**: i server conservano le risposte (TTL, ~2 giorni), anche gli IP dei TLD, così spesso saltano i root.

## Collegamenti

- **Concetti correlati**: [[Query DNS Ricorsive e Iterative]] · [[Record DNS]] · [[DNS]] · [[Extra/DNS/Stub Resolver|Stub Resolver]] · [[Load Balancing]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#2.4 DNS: il servizio di directory di Internet|Capitolo 2 — 2.4 DNS: il servizio di directory di Internet]]
> - [[02 - TLC - Livello di applicazione#Servizi forniti da DNS|Capitolo 2 — Servizi forniti da DNS]]
> - [[02 - TLC - Livello di applicazione#Un database distribuito e gerarchico|Capitolo 2 — Un database distribuito e gerarchico]]
> - [[02 - TLC - Livello di applicazione#DNS caching|Capitolo 2 — DNS caching]]
