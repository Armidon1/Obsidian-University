---
title: Ritardi nelle Reti a Commutazione di Pacchetto
tags:
  - telecomunicazioni
  - concetto
  - prestazioni
  - ritardi
---

# Ritardi nelle Reti a Commutazione di Pacchetto

> [!summary] In breve
> In ogni nodo un pacchetto subisce quattro ritardi: elaborazione, accodamento, trasmissione e propagazione. La loro somma è il **ritardo di nodo**; sommando i nodi si ottiene il ritardo **end-to-end**.

$$d_{\text{nodo}} = d_{\text{elab}} + d_{\text{acc}} + d_{\text{trasm}} + d_{\text{prop}}$$

| Ritardo | Formula / causa | Tipico |
| --- | --- | --- |
| elaborazione | controllo intestazione ed errori, scelta dell'uscita | µs |
| accodamento | attesa in coda, dipende dal traffico | 0 – ms |
| **trasmissione** | $L/R$: lunghezza / velocità del collegamento | µs – ms |
| **propagazione** | $d/v$: distanza / velocità nel mezzo ($2$–$3 \cdot 10^8$ m/s) | ms su lunghe distanze |

- Trasmissione ≠ propagazione: la prima non dipende dalla distanza, la seconda non dipende da $L$ e $R$ (analogia dei caselli: 2 min + 60 min = 62 min).
- End-to-end, $N$ collegamenti, senza code: $d = N(d_{\text{elab}} + L/R + d_{\text{prop}})$.
- Si misurano con **Traceroute** (RTT verso ogni router, 3 prove).
- Ritardi negli host: accesso a un mezzo condiviso, **pacchettizzazione** VoIP.

## Collegamenti

- **Concetti correlati**: [[Intensità di Traffico]] · [[Throughput e Collo di Bottiglia]] · [[Commutazione di Pacchetto]] · [[Traceroute]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#I quattro tipi di ritardo|Capitolo 1 — I quattro tipi di ritardo]]
> - [[01 - TLC - Reti di calcolatori e Internet#Ritardo di trasmissione vs ritardo di propagazione|Capitolo 1 — Ritardo di trasmissione vs ritardo di propagazione]]
> - [[01 - TLC - Reti di calcolatori e Internet#Ritardo end-to-end|Capitolo 1 — Ritardo end-to-end]]
> - [[01 - TLC - Reti di calcolatori e Internet#Traceroute|Capitolo 1 — Traceroute]]
