---
title: TDS - Algoritmo di Gilbert
tags:
  - teoria-dei-sistemi
  - concetto
  - realizzazione
  - realizzazione-minima
---

# TDS - Algoritmo di Gilbert

> [!summary] In breve
> Con poli semplici: $K(s)=\sum K_i/(s-p_i)$; ogni residuo di rango $\rho_i$ si fattorizza come $C_iB_i$ e si ottiene una realizzazione minima diagonale di dimensione $\sum\rho_i$.

- $A=\mathrm{diag}(p_1I_{\rho_1},\dots)$, $B=(B_1;\dots;B_r)$, $C=(C_1\ \cdots\ C_r)$.
- $C_i$ è $q\times\rho_i$, $B_i$ è $\rho_i\times p$; conviene usare l'identità quando possibile.
- Il rango del residuo = molteplicità dell'autovalore nella realizzazione minima.

## Collegamenti

- **Concetti correlati**: [[TDS - Realizzazione minima]] · [[TDS - Antitrasformata e residui]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[32 - TDS - Realizzazioni minime e realizzazione di Gilbert#Algoritmo di Gilbert|Lezione 32 — Algoritmo di Gilbert]]
> - [[32 - TDS - Realizzazioni minime e realizzazione di Gilbert#Esempio pratico|Lezione 32 — Esempio pratico]]
> - [[33 - TDS - Esercizio di realizzazione e matrice di Hankel#Realizzazione con l'algoritmo di Gilbert|Lezione 33 — Realizzazione con l'algoritmo di Gilbert]]
