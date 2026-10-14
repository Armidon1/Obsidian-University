---
title: Protocolli di Autenticazione ap
tags:
  - telecomunicazioni
  - concetto
  - autenticazione
---

# Protocolli di Autenticazione ap

> [!summary] In breve
> L'autenticazione del punto terminale si costruisce per passi: ap1.0 ("Sono Alice") → ap2.0 (+ IP, ma c'è lo spoofing) → ap3.0 (+ password, che si può intercettare) → ap3.1 (password cifrata, ma c'è la replica) → **ap4.0 con nonce** cifrato con la chiave condivisa.

| Versione | Falla |
| --- | --- |
| ap1.0 | chiunque può dire "Sono Alice" |
| ap2.0 | **IP spoofing** |
| ap3.0 | password intercettata (Telnet in chiaro) |
| ap3.1 | **attacco di replica** del messaggio cifrato |
| ap4.0 | ✓ Bob invia un **nonce** $R$, Alice risponde con $K_{A-B}(R)$ |

- **Nonce** = *number used once*: prova che l'altra parte è **viva** ora (come l'ISN casuale di TCP).
- Anche SSL e IPsec usano i nonce contro le repliche.

## Collegamenti

- **Concetti correlati**: [[Attacchi alle Reti]] · [[Nonce]] · [[Gestione della Connessione TCP]] · [[Protocollo SSL]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#8.4 Autenticazione di un punto terminale|Capitolo 8 — 8.4 Autenticazione di un punto terminale]]
> - [[08 - TLC - Sicurezza nelle reti#ap4.0: il nonce|Capitolo 8 — ap4.0: il nonce]]
