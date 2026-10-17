---
title: TDS - Criterio di Nyquist
tags:
  - teoria-dei-sistemi
  - concetto
  - criterio-di-nyquist
  - stabilita
---

# TDS - Criterio di Nyquist

> [!summary] In breve
> Il sistema in anello chiuso (retroazione unitaria) è stabile se e solo se il diagramma polare di $F(j\omega)$ compie attorno a $-1$ tanti giri antiorari quanti sono i poli instabili di $F$: $N^+=P_p$.

- Da $\frac{d_{ch}}{d_{ap}}=1+F$ e dalla variazione di fase $n\pi-2\pi P$ di un polinomio.
- Con guadagno $K$: il punto critico diventa $-\frac1K$ (o si ruotano gli assi se $K<0$).
- Giri contati con una semiretta da $-1$, con segno.
- Poli sull'asse immaginario: si aggirano con $\varepsilon\to0$ e il diagramma si chiude all'infinito in senso orario ($h$ semigiri per un polo di ordine $h$ in zero).

## Collegamenti

- **Concetti correlati**: [[TDS - Diagramma polare]] · [[TDS - Retroazione]] · [[TDS - Margini di stabilità]] · [[TDS - Criterio di Routh]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[35 - TDS - Criterio di Nyquist#Stabilità del sistema chiuso per $p=q=1$|Lezione 35 — Stabilità del sistema chiuso per $p=q=1$]]
> - [[35 - TDS - Criterio di Nyquist#Studio della stabilità dal diagramma polare di $W_{ap}(s)+1$|Lezione 35 — Studio della stabilità dal diagramma polare di $W_{ap}(s)+1$]]
> - [[36 - TDS - Nyquist con poli sull'asse immaginario#Caso in cui una radice di $F(s)$ è nulla|Lezione 36 — Caso in cui una radice di $F(s)$ è nulla]]
