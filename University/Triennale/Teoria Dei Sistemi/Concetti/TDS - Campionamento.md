---
title: TDS - Campionamento
tags:
  - teoria-dei-sistemi
  - concetto
  - tempo-discreto
  - campionamento
---

# TDS - Campionamento

> [!summary] In breve
> Un sistema continuo con tenuta di ordine zero e campionatore (periodo $T_c$) è un sistema discreto con $A_d=e^{AT_c}$, $B_d=\int_0^{T_c}e^{A\vartheta}d\vartheta\,B$.

- **ZOH**: mantiene costante l'ingresso tra due campioni (tenute di ordine superiore introducono ritardo).
- Autovalori: $\lambda_d=e^{\lambda_cT_c}$ (stessi autovettori); reali → sempre positivi.
- Funzione di trasferimento: $W(z)=\frac{z-1}{z}\,\mathcal Z\big[\mathcal L^{-1}[W(s)/s]_{t=kT_c}\big]$.
- Guadagno statico conservato: $W(z=1)=W(s=0)$.

## Collegamenti

- **Concetti correlati**: [[TDS - Sistemi a tempo discreto]] · [[TDS - Trasformata Zeta]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[10 - TDS - Esempio a tempo discreto e campionamento#Tempo discreto campionato|Lezione 10 — Tempo discreto campionato]]
> - [[10 - TDS - Esempio a tempo discreto e campionamento#Il modello matematico del sistema campionato|Lezione 10 — Il modello matematico del sistema campionato]]
> - [[21 - TDS - Risposta a regime permanente#Trasformate nel tempo discreto campionato|Lezione 21 — Trasformate nel tempo discreto campionato]]
