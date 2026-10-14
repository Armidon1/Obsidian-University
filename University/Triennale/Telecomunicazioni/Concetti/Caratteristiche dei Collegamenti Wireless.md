---
title: Caratteristiche dei Collegamenti Wireless
tags:
  - telecomunicazioni
  - concetto
  - wireless
  - livello-fisico
---

# Caratteristiche dei Collegamenti Wireless

> [!summary] In breve
> I collegamenti wireless soffrono di **attenuazione**, **interferenze** e **propagazione su più cammini**, quindi hanno un BER alto. Il **BER** cala con l'**SNR** e cresce con la velocità della modulazione, per cui la modulazione si sceglie in modo adattivo.

- **SNR** in dB = $20\log_{10}(A_{segnale}/A_{rumore})$.
- Più SNR → meno BER; oltre una soglia, alzare la potenza costa batteria e interferenze.
- Con SNR 10 dB: BPSK (1 Mbps) ha BER < $10^{-7}$, 16-QAM (4 Mbps) ≈ $10^{-1}$. Con 20 dB: 16-QAM ≈ $10^{-7}$, quindi conviene.
- Conseguenze: CRC robusti e **ARQ a livello di collegamento**.
- **Terminale nascosto** e **fading** complicano l'accesso multiplo.

## Collegamenti

- **Concetti correlati**: [[Terminale Nascosto]] · [[Mezzi Trasmissivi]] · [[Wi-Fi 802.11]] · [[CRC]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#7.2 Collegamenti wireless e caratteristiche di rete|Capitolo 7 — 7.2 Collegamenti wireless e caratteristiche di rete]]
> - [[07 - TLC - Reti mobili e wireless#SNR, BER e modulazione|Capitolo 7 — SNR, BER e modulazione]]
