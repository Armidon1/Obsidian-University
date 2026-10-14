---
title: IPsec ed ESP
tags:
  - telecomunicazioni
  - concetto
  - ipsec
  - vpn
  - sicurezza
---

# IPsec ed ESP

> [!summary] In breve
> **IPsec** protegge i datagrammi IP tra host e router: riservatezza, autenticazione della sorgente, integrità e protezione dalla replica. Si usa per le **VPN**. Con **ESP** in modalità tunnel il datagramma originale viene cifrato e incapsulato in un nuovo datagramma IP (protocollo 50).

- **AH**: solo autenticazione e integrità · **ESP**: in più riservatezza (il più usato).
- **SA** (associazione di sicurezza) unidirezionale: SPI, interfacce, algoritmi e chiavi; VPN con $n$ agenti → $2 + 2n$ SA.
- **SAD** = come proteggere (stato delle SA) · **SPD** = cosa proteggere.
- Datagramma: nuova intestazione IP | intestazione ESP (SPI, seq) | [IP originale + coda ESP] cifrati | MAC ESP.
- Ricezione: SPI → SA → verifica MAC → numero di sequenza → decifra → togli il padding → inoltra.
- **IKE** (RFC 5996): fase 1 con Diffie-Hellman → SA IKE + autenticazione con firma; fase 2 → SA IPsec nei due sensi.

## Collegamenti

- **Concetti correlati**: [[Associazione di Sicurezza]] · [[IPsec]] · [[Codice di Autenticazione del Messaggio]] · [[Protocollo IPv6]] · [[Datagramma IPv4]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#8.7 Sicurezza a livello di rete: IPsec e reti private virtuali|Capitolo 8 — 8.7 Sicurezza a livello di rete: IPsec e reti private virtuali]]
> - [[08 - TLC - Sicurezza nelle reti#IPsec e le reti private virtuali (VPN)|Capitolo 8 — IPsec e le reti private virtuali (VPN)]]
> - [[08 - TLC - Sicurezza nelle reti#Il datagramma IPsec|Capitolo 8 — Il datagramma IPsec]]
> - [[08 - TLC - Sicurezza nelle reti#IKE: gestione delle chiavi in IPsec|Capitolo 8 — IKE: gestione delle chiavi in IPsec]]
