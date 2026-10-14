---
title: Protocolli a Rotazione
tags:
  - telecomunicazioni
  - concetto
  - accesso-multiplo
---

# Protocolli a Rotazione

> [!summary] In breve
> Danno a turno il diritto di trasmettere. Nel **polling** un nodo principale interpella gli altri; nel **token passing** circola un gettone. Niente collisioni né slot vuoti, ma c'è un punto debole: il nodo principale o il token.

| | Polling | Token passing |
| --- | --- | --- |
| Coordinamento | nodo principale | token che circola in ordine fisso |
| Contro | ritardo di polling; guasto del nodo principale | guasto di un nodo, token perso |
| Esempi | 802.15, Bluetooth | FDDI, token ring 802.5 |

## Collegamenti

- **Concetti correlati**: [[Protocolli di Accesso Multiplo]] · [[CSMA-CD]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Protocolli a rotazione|Capitolo 6 — Protocolli a rotazione]]
