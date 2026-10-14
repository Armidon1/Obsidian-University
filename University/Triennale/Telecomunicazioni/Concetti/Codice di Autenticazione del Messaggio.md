---
title: Codice di Autenticazione del Messaggio
tags:
  - telecomunicazioni
  - concetto
  - crittografia
  - integrita
  - mac
---

# Codice di Autenticazione del Messaggio

> [!summary] In breve
> Il **MAC** (*message authentication code*) è $H(m + s)$: l'hash del messaggio concatenato con una **chiave di autenticazione** $s$ condivisa. Il destinatario lo ricalcola e lo confronta. Garantisce integrità e origine **senza cifratura**.

- L'hash da solo non basta: Trudy invierebbe $(m', H(m'))$.
- Passi: $(m, H(m+s))$ → il ricevente calcola $H(m+s)$ con il suo $s$ → confronto.
- Standard: **HMAC** (RFC 2104), con MD5 o SHA-1, che applica l'hash due volte.
- Usato in OSPF, SSL, IPsec.
- Da non confondere con il MAC (*Medium Access Control*) del livello di collegamento.
- Non è una firma: la chiave è condivisa, quindi non è unica per il mittente.

## Collegamenti

- **Concetti correlati**: [[Funzioni Hash Crittografiche]] · [[Firma Digitale]] · [[HMAC]] · [[MAC]] · [[Protocollo SSL]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#Codice di autenticazione dei messaggi (MAC)|Capitolo 8 — Codice di autenticazione dei messaggi (MAC)]]
