---
title: RTS e CTS
tags:
  - telecomunicazioni
  - concetto
  - wifi
  - accesso-multiplo
---

# RTS e CTS

> [!summary] In breve
> Prenotazione opzionale del canale in 802.11: la sorgente invia un **RTS** con la durata richiesta, l'AP risponde con un **CTS** in broadcast, e tutti gli altri rimandano l'accesso. Risolve il terminale nascosto al prezzo di un po' di overhead.

Sequenza: DIFS → RTS → SIFS → CTS (tutti gli altri: accesso rimandato) → SIFS → DATI → SIFS → ACK.

- Le collisioni possono riguardare solo RTS e CTS, che sono brevi.
- Si usa solo per i frame più grandi della **soglia RTS** (spesso, di default, non si usa affatto).

## Collegamenti

- **Concetti correlati**: [[CSMA-CA]] · [[Terminale Nascosto]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#Terminali nascosti: RTS e CTS|Capitolo 7 — Terminali nascosti: RTS e CTS]]
