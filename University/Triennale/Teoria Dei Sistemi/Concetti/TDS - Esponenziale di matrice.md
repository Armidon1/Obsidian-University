---
title: TDS - Esponenziale di matrice
tags:
  - teoria-dei-sistemi
  - concetto
  - esponenziale-di-matrice
---

# TDS - Esponenziale di matrice

> [!summary] In breve
> $e^{At}=\sum_k A^kt^k/k!$; si calcola diagonalizzando ($Ue^{\Lambda t}U^{-1}$), con i blocchi reali per gli autovalori complessi e con la forma di Jordan, oppure come $\mathcal L^{-1}[(sI-A)^{-1}]$.

| Caso | Blocco | Esponenziale |
|---|---|---|
| diagonale | $\lambda$ | $e^{\lambda t}$ |
| coppia $\alpha\pm j\omega$ | $\begin{psmallmatrix}\alpha&\omega\\-\omega&\alpha\end{psmallmatrix}$ | $e^{\alpha t}\begin{psmallmatrix}\cos\omega t&\sin\omega t\\-\sin\omega t&\cos\omega t\end{psmallmatrix}$ |
| Jordan $k\times k$ | $\lambda I+N$ | $e^{\lambda t}\big(I+Nt+\dots+N^{k-1}\frac{t^{k-1}}{(k-1)!}\big)$ |

- Con autovalori distinti: $e^{At}=\sum_ie^{\lambda_it}u_iv_i'$.
- Con Laplace: i residui di $(sI-A)^{-1}$ sono le matrici $u_iv_i'$.
- Discreto: $A^t=U\Lambda^tU^{-1}$, con $\rho^t$ e $\theta t$ per le coppie complesse.

## Collegamenti

- **Concetti correlati**: [[TDS - Forma spettrale]] · [[TDS - Forma di Jordan]] · [[TDS - Antitrasformata e residui]] · [[TDS - Matrice di transizione dello stato]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[05 - TDS - Calcolo dell'esponenziale di matrice#Caso in cui $A$ abbia $n$ autovalori distinti|Lezione 5 — Caso in cui $A$ abbia $n$ autovalori distinti]]
> - [[07 - TDS - Autovalori complessi coniugati|Lezione 7]]
> - [[16 - TDS - Antitrasformate e residui|Lezione 16]]
> - [[17 - TDS - Matrici non diagonalizzabili e catene di autovettori#Esponenziale dei blocchi di Jordan|Lezione 17 — Esponenziale dei blocchi di Jordan]]
