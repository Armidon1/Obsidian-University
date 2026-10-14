---
title: Web Caching
tags:
  - telecomunicazioni
  - concetto
  - http
  - cache
  - prestazioni
---

# Web Caching

> [!summary] In breve
> Una **web cache** (proxy) risponde alle richieste HTTP al posto del server di origine usando copie locali degli oggetti. Riduce il tempo di risposta e il traffico sul collegamento d'accesso.

- Il proxy è **server** verso il browser e **client** verso il server di origine.
- **Hit rate**: frazione di richieste servite dalla cache (0,2–0,7).
- Esempio del libro: LAN a 100 Mbps, accesso a 15 Mbps, 15 richieste/s di oggetti da 1 Mbit, ritardo Internet 2 s:
  - $I_{\text{accesso}} = 15 \cdot 1 / 15 = 1$, quindi ritardi di minuti;
  - accesso a 100 Mbps → ≈ 2 s, ma costa caro;
  - proxy con hit rate 0,4 → $I = 0{,}6$, quindi $0{,}4 \cdot 0{,}01 + 0{,}6 \cdot 2{,}01 \approx 1{,}21$ s, e costa poco.
- Le copie possono scadere, e per questo esiste il **GET condizionale**.
- Le **CDN** sono cache distribuite geograficamente.

## Collegamenti

- **Concetti correlati**: [[GET Condizionale]] · [[Intensità di Traffico]] · [[Content Distribution Network]] · [[Proxy]] · [[Protocollo HTTP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Web caching|Capitolo 2 — Web caching]]
> - [[02 - TLC - Livello di applicazione#Esempio numerico: proxy o collegamento più veloce?|Capitolo 2 — Esempio numerico: proxy o collegamento più veloce?]]
