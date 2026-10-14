---
title: Throughput e Collo di Bottiglia
tags:
  - telecomunicazioni
  - concetto
  - prestazioni
  - throughput
---

# Throughput e Collo di Bottiglia

> [!summary] In breve
> Il **throughput** è la velocità (bps) con cui il destinatario riceve i dati. Su un percorso è circa la velocità del collegamento più lento, il **collo di bottiglia**, che dipende anche dal traffico che condivide i collegamenti.

- Throughput **istantaneo** contro **medio** $= F/T$.
- $\text{throughput} = \min(R_1, R_2, \dots, R_N)$ → tempo per un file $\approx F / \min(\dots)$.
- Esempio: $F = 32$ Mbit, $R_s = 2$ Mbps, $R_c = 1$ Mbps → **32 s**.
- Oggi il nucleo è sovradimensionato, quindi il collo di bottiglia è di solito la **rete di accesso**.
- Collegamento comune $R = 5$ Mbps diviso tra 10 download → 500 kbps ciascuno, e il collo di bottiglia passa al **nucleo**.

## Collegamenti

- **Concetti correlati**: [[Ritardi nelle Reti a Commutazione di Pacchetto]] · [[Reti di Accesso]] · [[Intensità di Traffico]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#Throughput|Capitolo 1 — Throughput]]
