---
title: Sicurezza 802.11 WEP e 802.11i
tags:
  - telecomunicazioni
  - concetto
  - wifi
  - sicurezza
---

# Sicurezza 802.11 WEP e 802.11i

> [!summary] In breve
> **WEP** cifra i frame con RC4 usando una chiave di 40 bit + un IV di 24 bit in chiaro, e autentica con un nonce. È **insicuro** (riuso dell'IV, testo in chiaro scelto, CRC al posto del MAC, chiavi deboli). **802.11i** (2004) introduce un server di autenticazione, EAP e una gerarchia di chiavi MK → PMK → TK.

- WEP: $c_i = d_i \oplus k_i^{IV}$; solo $2^{24}$ IV → ripetizione quasi certa dopo ~12.000 frame; con un testo noto si ricava $k_i^{IV} = d_i \oplus c_i$.
- 802.11i in 4 fasi: (1) riconoscimento delle capacità; (2) mutua autenticazione STA–AS e **MK** (l'AP fa da ripetitore); (3) **PMK** consegnata all'AP; (4) **TK** per cifratura e integrità.
- Pila: EAP-TLS / EAP / **EAPoL** (802.1X) su 802.11 tra STA e AP; **RADIUS** su UDP/IP tra AP e AS (in futuro DIAMETER).

## Collegamenti

- **Concetti correlati**: [[Wi-Fi 802.11]] · [[Associazione 802.11]] · [[Crittografia a Chiave Simmetrica]] · [[Stream Cipher]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#8.8 Sicurezza nelle LAN wireless|Capitolo 8 — 8.8 Sicurezza nelle LAN wireless]]
> - [[08 - TLC - Sicurezza nelle reti#Wired equivalent privacy (WEP)|Capitolo 8 — Wired equivalent privacy (WEP)]]
> - [[08 - TLC - Sicurezza nelle reti#IEEE 802.11i|Capitolo 8 — IEEE 802.11i]]
