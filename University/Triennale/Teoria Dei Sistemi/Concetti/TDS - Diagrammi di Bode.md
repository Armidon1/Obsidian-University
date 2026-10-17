---
title: TDS - Diagrammi di Bode
tags:
  - teoria-dei-sistemi
  - concetto
  - diagrammi-di-bode
  - risposta-armonica
---

# TDS - Diagrammi di Bode

> [!summary] In breve
> Modulo in dB ($20\log_{10}|W|$) e fase in funzione di $\log_{10}\omega$: con la forma di Bode si sommano i contributi dei singoli fattori, approssimati con asintoti.

| Fattore | Modulo | Fase |
|---|---|---|
| $K$ | $20\log|K|$ | $0$ o $-\pi$ |
| $s$ | $\pm20$ dB/dec da $\omega=1$ | $\pm\frac\pi2$ |
| $1+\tau s$ | 0, poi $\pm20$ dB/dec da $1/\tau$ | da 0 a $\pm\frac\pi2$ in $[\frac{0{,}1}\tau,\frac{10}\tau]$ |
| trinomio $\omega_n,\zeta$ | 0, poi $\pm40$ dB/dec da $\omega_n$ (+ picco) | da 0 a $\pm\pi$ |

- Forma di Bode: $W=K\frac{\prod(1+\tau_is)}{s^h\prod(1+\tau_js)\cdots}$.
- Al denominatore i grafici si ribaltano; le potenze moltiplicano pendenze e fasi.
- Ogni sistema strettamente proprio "taglia" le alte frequenze.

## Collegamenti

- **Concetti correlati**: [[TDS - Risposta armonica]] · [[TDS - Diagramma polare]] · [[TDS - Margini di stabilità]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[22 - TDS - Risposta armonica e forma di Bode#Risposta armonica in forma di Bode|Lezione 22 — Risposta armonica in forma di Bode]]
> - [[23 - TDS - Diagrammi di Bode#Grafico delle radici reali nella risposta armonica|Lezione 23 — Grafico delle radici reali nella risposta armonica]]
> - [[24 - TDS - Termine trinomio e risonanza#Grafico del modulo del termine trinomio|Lezione 24 — Grafico del modulo del termine trinomio]]
> - [[24 - TDS - Termine trinomio e risonanza#Grafico della fase del termine trinomio|Lezione 24 — Grafico della fase del termine trinomio]]
