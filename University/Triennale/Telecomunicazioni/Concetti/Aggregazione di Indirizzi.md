---
title: Aggregazione di Indirizzi
tags:
  - telecomunicazioni
  - concetto
  - ip
  - indirizzamento
  - routing
---

# Aggregazione di Indirizzi

> [!summary] In breve
> Un ISP annuncia un **solo prefisso** per tutte le reti dei suoi clienti (route aggregation/summarization). Se un cliente cambia ISP, il nuovo ISP annuncia un prefisso **più specifico**, che vince grazie al longest prefix match.

- Scappo-Con-La-Cassa-ISP: "mandami tutto ciò che inizia per **200.23.16.0/20**" (8 organizzazioni /23).
- L'Organizzazione 1 (200.23.18.0/23) passa a ISP-Siamo-Noi, che ora annuncia anche **200.23.18.0/23**.
- Per 200.23.18.x i router vedono /20 e /23 e scelgono **/23** (prefisso più lungo).
- Vantaggio: tabelle di inoltro piccole nel resto di Internet.

## Collegamenti

- **Concetti correlati**: [[CIDR]] · [[Longest Prefix Match]] · [[BGP]] · [[Gerarchia degli ISP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Aggregazione di indirizzi (Box 4.1)|Capitolo 4 — Aggregazione di indirizzi (Box 4.1)]]
