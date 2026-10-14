---
title: CRC
tags:
  - telecomunicazioni
  - concetto
  - errori
  - crc
---

# CRC

> [!summary] In breve
> Il **controllo a ridondanza ciclica** accoda ai dati $D$ un resto $R$ di $r$ bit, calcolato in modo che $D \cdot 2^r \text{ XOR } R$ sia divisibile per il **generatore** $G$ ($r+1$ bit) in aritmetica modulo 2. Il ricevente divide per $G$: un resto non nullo indica un errore.

$$R = \text{resto di } \frac{D \cdot 2^r}{G} \qquad (\text{somma} = \text{sottrazione} = \text{XOR})$$

Esempio: $D = 101110$, $G = 1001$, $r = 3$ → $R = 011$, si trasmette `101110011`.

- Rileva tutti i burst di **meno di $r + 1$** bit, un burst più lungo con probabilità $1 - 0{,}5^r$, e qualsiasi numero **dispari** di errori.
- CRC-32 (IEEE): `100000100110000010001110110110111`.
- Si usa nel livello di collegamento perché è in **hardware**; al trasporto, che è in software, si usa il checksum.

## Collegamenti

- **Concetti correlati**: [[Controllo di Parità]] · [[Checksum Internet]] · [[Frame Ethernet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Controllo a ridondanza ciclica (CRC)|Capitolo 6 — Controllo a ridondanza ciclica (CRC)]]
> - [[06 - TLC - Livello di collegamento e reti locali#Checksum|Capitolo 6 — Checksum]]
