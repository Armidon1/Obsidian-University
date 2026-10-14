---
title: CDMA
tags:
  - telecomunicazioni
  - concetto
  - accesso-multiplo
  - wireless
  - cellulare
---

# CDMA

> [!summary] In breve
> **Code Division Multiple Access**: ogni trasmittente moltiplica i suoi bit per un **codice** di $M$ chip ($\pm1$). I segnali nel canale si sommano, e il ricevente recupera i dati di un trasmittente usando il suo codice: con codici **ortogonali** gli altri si annullano.

$$Z_{i,m} = d_i \cdot c_m \qquad d_i = \frac{1}{M}\sum_{m=1}^{M} Z^*_{i,m}\, c_m$$

- Il bit 0 si rappresenta come $-1$; il **chipping rate** è molto più alto del tasso dei dati.
- Esempio: $c^1 = (1,1,1,-1,1,-1,-1,-1)$, $c^2 = (1,-1,1,1,1,-1,1,1)$, $c^1 \cdot c^2 = 0$ → con $d^1 = -1$ e $d^2 = 1$ il canale vale $(0,-2,0,2,0,0,2,2)$ e il ricevente 1 ottiene $-8/8 = -1$.
- Divide lo **spazio dei codici** (invece di tempo o frequenze). Analogia: un invitato che parla più lingue.
- Ipotesi semplificative: codici scelti bene, segnali con la stessa potenza.
- Usato nelle reti cellulari (WCDMA in 3G).

## Collegamenti

- **Concetti correlati**: [[Protocolli di Accesso Multiplo]] · [[Multiplexing FDM e TDM]] · [[Reti Cellulari 3G e 4G]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#CDMA|Capitolo 7 — CDMA]]
