---
title: Filtri di Pacchetti e Gateway Applicativi
tags:
  - telecomunicazioni
  - concetto
  - firewall
  - sicurezza
---

# Filtri di Pacchetti e Gateway Applicativi

> [!summary] In breve
> Un **firewall** separa la rete interna da Internet: tutto il traffico ci passa, passa solo quello autorizzato, ed è immune alla penetrazione. I tipi sono **filtri di pacchetti** (regole su IP, porte, protocollo, flag), **filtri con memoria di stato** (tabella delle connessioni TCP) e **gateway a livello applicativo** (proxy per singola applicazione, con autenticazione degli utenti).

ACL per 222.22/16 (dall'alto verso il basso):
| Azione | Sorgente | Destinazione | Prot. | P. sorg. | P. dest. | Flag |
| --- | --- | --- | --- | --- | --- | --- |
| consenti | interno | esterno | TCP | >1023 | 80 | — |
| consenti | esterno | interno | TCP | 80 | >1023 | ACK |
| consenti | interno | esterno | UDP | >1023 | 53 | — |
| consenti | esterno | interno | UDP | 53 | >1023 | — |
| blocca | tutto | tutto | tutti | — | — | — |

- Bloccare i segmenti in entrata con **ACK = 0** impedisce le connessioni aperte dall'esterno.
- **Stateful**: un pacchetto ACK dalla porta 80 passa solo se appartiene a una connessione nella tabella.
- **Gateway applicativo** (es. Telnet): autenticazione, poi il gateway apre la connessione; costa in prestazioni e ne serve uno per applicazione.
- Anonimato: proxy fidato + SSL, oppure TOR (catena di 3 proxy).

## Collegamenti

- **Concetti correlati**: [[Sistemi di Rilevamento delle Intrusioni]] · [[Firewall]] · [[Packet Filtering]] · [[Application-Level Gateway]] · [[Proxy]] · [[NAT]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#8.9 Sicurezza operativa: firewall e sistemi di rilevamento delle intrusioni|Capitolo 8 — 8.9 Sicurezza operativa: firewall e sistemi di rilevamento delle intrusioni]]
> - [[08 - TLC - Sicurezza nelle reti#Filtri di pacchetti tradizionali|Capitolo 8 — Filtri di pacchetti tradizionali]]
> - [[08 - TLC - Sicurezza nelle reti#Filtri di pacchetti con memoria di stato|Capitolo 8 — Filtri di pacchetti con memoria di stato]]
> - [[08 - TLC - Sicurezza nelle reti#Gateway a livello applicativo|Capitolo 8 — Gateway a livello applicativo]]
