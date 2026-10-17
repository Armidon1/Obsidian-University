---
title: TDS - Regime permanente
tags:
  - teoria-dei-sistemi
  - concetto
  - regime-permanente
---

# TDS - Regime permanente

> [!summary] In breve
> La parte di risposta che resta quando i transitori si spengono: $y_{RP}(t)=\int_{-\infty}^tW(t-\tau)u(\tau)d\tau$; esiste se i modi (osservabili) sono tutti convergenti.

- $y=y_T+y_{RP}$; il transitorio contiene la parte libera e quella forzata dovuta ai poli di $W$.
- Gradino: $y_{RP}=W(0)$. Rampa: $tW(0)+W'(0)$.
- Polinomio $\frac{t^k}{k!}$: $y_{RP}=\sum_i\frac{t^{k-i}}{(k-i)!}c_i$, con $c_i$ coefficienti di Maclaurin di $W$.
- Esponenziale $e^{at}$: $e^{at}W(a)$. Seno: $|W(j\omega)|\sin(\omega t+\angle W(j\omega))$.
- Con un polo a parte reale $\ge0$ il regime non esiste.

## Collegamenti

- **Concetti correlati**: [[TDS - Risposta armonica]] · [[TDS - Risposta indiciale]] · [[TDS - Evoluzione libera e forzata]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[21 - TDS - Risposta a regime permanente#Risposta a regime permanente|Lezione 21 — Risposta a regime permanente]]
> - [[21 - TDS - Risposta a regime permanente#Studio dell'uscita a regime permanente con vari ingressi|Lezione 21 — Studio dell'uscita a regime permanente con vari ingressi]]
> - [[22 - TDS - Risposta armonica e forma di Bode#Uscita a regime permanente con ingresso polinomiale|Lezione 22 — Uscita a regime permanente con ingresso polinomiale]]
> - [[22 - TDS - Risposta armonica e forma di Bode#Ingresso sinusoidale|Lezione 22 — Ingresso sinusoidale]]
