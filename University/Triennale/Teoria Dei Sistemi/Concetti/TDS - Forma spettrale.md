---
title: TDS - Forma spettrale
tags:
  - teoria-dei-sistemi
  - concetto
  - forma-spettrale
  - autovalori
---

# TDS - Forma spettrale

> [!summary] In breve
> Se $A$ è diagonalizzabile, $A=U\Lambda U^{-1}=\sum_i\lambda_iu_iv_i\'$, con $u_i$ autovettori (colonne di $U$) e $v_i\'$ righe di $U^{-1}$.

- $v_i'u_j=\delta_{ij}$; $R_i=u_iv_i'$ ha rango 1; raggruppando un autovalore multiplo la **matrice residua** ha rango pari alla molteplicità.
- $A^k=\sum\lambda_i^kR_i$, $e^{At}=\sum e^{\lambda_it}R_i$.
- Coordinate di $x_0$ nella base degli autovettori: $c_i=v_i'x_0$.
- Diagonalizzabile ⟺ molteplicità geometrica = algebrica per ogni autovalore (vedi [[GEO - Criterio di diagonalizzabilità]]).

## Collegamenti

- **Concetti correlati**: [[TDS - Esponenziale di matrice]] · [[TDS - Modi naturali]] · [[TDS - Cambio di coordinate nello spazio di stato]] · [[GEO - Molteplicità algebrica e geometrica]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[05 - TDS - Calcolo dell'esponenziale di matrice#Caso in cui $A$ abbia $n$ autovalori distinti|Lezione 5 — Caso in cui $A$ abbia $n$ autovalori distinti]]
> - [[06 - TDS - Modi naturali#Considerazioni sulla matrice $A$|Lezione 6 — Considerazioni sulla matrice $A$]]
