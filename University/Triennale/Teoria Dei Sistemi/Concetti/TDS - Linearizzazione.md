---
title: TDS - Linearizzazione
tags:
  - teoria-dei-sistemi
  - concetto
  - stabilita
  - sistemi-non-lineari
---

# TDS - Linearizzazione

> [!summary] In breve
> Attorno a un equilibrio $\dot z=Jz$ con $J=\partial f/\partial x|_{x_e}$: se il linearizzato è asintoticamente stabile (instabile con autovalori a $\mathrm{Re}>0$) lo è anche il non lineare; se è solo semplicemente stabile non si conclude.

- Procedura: equilibri → jacobiano in ciascuno → autovalori.
- Esempi: pendolo, modello SIR ($R_0<1$), preda-predatore.
- Vale anche nel discreto: $z(t+1)=Jz(t)$.
- Caso dubbio → [[TDS - Criterio di Lyapunov]].

## Collegamenti

- **Concetti correlati**: [[TDS - Punti di equilibrio]] · [[TDS - Criterio di Lyapunov]] · [[TDS - Stabilità]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[12 - TDS - Criterio di Routh e linearizzazione#Approssimazione di sistemi non lineari|Lezione 12 — Approssimazione di sistemi non lineari]]
> - [[12 - TDS - Criterio di Routh e linearizzazione#Modelli di epidemie: modello SIR|Lezione 12 — Modelli di epidemie: modello SIR]]
> - [[14 - TDS - Stabilità nel tempo discreto ed esempi#Approssimazione di sistemi non lineari a tempo discreto|Lezione 14 — Approssimazione di sistemi non lineari a tempo discreto]]
