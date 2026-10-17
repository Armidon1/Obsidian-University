---
title: TDS - Cambio di coordinate nello spazio di stato
tags:
  - teoria-dei-sistemi
  - concetto
  - rappresentazione-con-lo-stato
---

# TDS - Cambio di coordinate nello spazio di stato

> [!summary] In breve
> Con $z=Tx$ il sistema diventa $(TAT^{-1},TB,CT^{-1},D)$: stessi autovalori, stessa $W$; si sceglie $T$ per mettere in evidenza una struttura.

- Rappresentazioni **equivalenti**: differiscono solo per la scelta delle coordinate.
- $T=U^{-1}$ → forma diagonale (o di Jordan).
- $T^{-1}=$ (base di $\mathcal I$ | completamento) → scomposizione rispetto all'osservabilità.
- $T^{-1}=$ (base di $\mathcal R$ | completamento) → scomposizione rispetto alla raggiungibilità.
- $T$ da $\gamma'$ (ultima riga di $R^{-1}$) → forma canonica raggiungibile.
- Retroazione: $\tilde F=FT^{-1}$; osservatore: $\tilde K=TK$.

## Collegamenti

- **Concetti correlati**: [[TDS - Forma spettrale]] · [[TDS - Scomposizione di Kalman]] · [[TDS - Forme canoniche]] · [[GEO - Cambiamento di base e similitudine]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[05 - TDS - Calcolo dell'esponenziale di matrice#Considerazioni sul cambio di coordinate in un sistema|Lezione 5 — Considerazioni sul cambio di coordinate in un sistema]]
> - [[26 - TDS - Stati inosservabili#Cambio di coordinate dello spazio di stato|Lezione 26 — Cambio di coordinate dello spazio di stato]]
> - [[37 - TDS - Assegnazione degli autovalori con retroazione dallo stato#Portare un sistema in forma canonica raggiungibile|Lezione 37 — Portare un sistema in forma canonica raggiungibile]]
