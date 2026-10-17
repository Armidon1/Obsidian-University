---
title: TDS - Stabilità
tags:
  - teoria-dei-sistemi
  - concetto
  - stabilita
---

# TDS - Stabilità

> [!summary] In breve
> Un equilibrio è stabile semplicemente se partendo vicino si resta vicino, asintoticamente se in più ci si torna; nei sistemi lineari dipende dalla posizione degli autovalori.

| | Continuo | Discreto |
|---|---|---|
| asintotica | $\mathrm{Re}\,\lambda_i<0$ | $|\lambda_i|<1$ |
| semplice | $\mathrm{Re}\,\lambda_i\le0$, quelli con $\mathrm{Re}=0$ regolari | $|\lambda_i|\le1$, quelli con $|\lambda|=1$ regolari |

- Definizione: $\forall\varepsilon\ \exists\delta$: $\|x_0-x_e\|\le\delta\Rightarrow\|x(t)-x_e\|\le\varepsilon$.
- Lineare ⟺ $\Phi(t)$ limitata (semplice) / $\Phi(t)\to0$ (asintotica); stabilità **interna** comune a tutti gli equilibri.
- Asintotica solo se l'equilibrio è isolato (unico).

## Collegamenti

- **Concetti correlati**: [[TDS - Stabilità esterna]] · [[TDS - Criterio di Routh]] · [[TDS - Criterio di Jury]] · [[TDS - Criterio di Lyapunov]] · [[TDS - Punti di equilibrio]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[11 - TDS - Punti di equilibrio e stabilità#Definizione formale di stabilità|Lezione 11 — Definizione formale di stabilità]]
> - [[11 - TDS - Punti di equilibrio e stabilità#Definizione operativa di stabilità|Lezione 11 — Definizione operativa di stabilità]]
> - [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto#Stabilità interna|Lezione 13 — Stabilità interna]]
> - [[18 - TDS - Trasformata Zeta#Stabilità|Lezione 18 — Stabilità]]
