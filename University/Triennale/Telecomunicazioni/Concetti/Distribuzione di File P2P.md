---
title: Distribuzione di File P2P
tags:
  - telecomunicazioni
  - concetto
  - p2p
  - prestazioni
---

# Distribuzione di File P2P

> [!summary] In breve
> Distribuire un file di $F$ bit a $N$ peer: in client-server il tempo cresce **linearmente** con $N$; in P2P resta **limitato**, perché ogni peer aggiunge capacità di upload.

$$D_{cs} = \max\left\{\frac{NF}{u_s},\ \frac{F}{d_{\min}}\right\}$$

$$D_{P2P} = \max\left\{\frac{F}{u_s},\ \frac{F}{d_{\min}},\ \frac{NF}{u_s + \sum_i u_i}\right\}$$

- $u_s$ = upload del server, $u_i$ / $d_i$ = upload / download del peer $i$, $d_{\min}$ = download più lento.
- Ipotesi: i colli di bottiglia sono nelle reti di accesso.
- Con $F/u = 1$ h e $u_s = 10u$: $D_{cs} = N/10$ h, mentre $D_{P2P} = \max\{0{,}1,\ N/(10+N)\} < 1$ h.

## Collegamenti

- **Concetti correlati**: [[BitTorrent]] · [[Architetture Client-Server e P2P]] · [[Throughput e Collo di Bottiglia]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[02 - TLC - Livello di applicazione#Scalabilità dell'architettura P2P|Capitolo 2 — Scalabilità dell'architettura P2P]]
