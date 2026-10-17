---
title: TDS - Antitrasformata e residui
tags:
  - teoria-dei-sistemi
  - concetto
  - trasformata-di-laplace
  - antitrasformata
---

# TDS - Antitrasformata e residui

> [!summary] In breve
> Si scompone la funzione razionale strettamente propria in fratti semplici; i coefficienti (residui) si calcolano con limiti e, per poli multipli, derivate divise per $k!$.

- Polo semplice: $R_i=\lim_{s\to p_i}(s-p_i)F(s)$.
- Polo di molteplicità $m$: $R_{ij}=\frac{1}{(j-1)!}\lim_{s\to p}\frac{d^{j-1}}{ds^{j-1}}\big[(s-p)^mF(s)\big]$ (per il termine $\frac{1}{(s-p)^{m-j+1}}$).
- Poli complessi: residui coniugati, $Re^{j\omega t}+R^*e^{-j\omega t}=2R_a\cos\omega t-2R_b\sin\omega t$.
- Con matrici (es. $(sI-A)^{-1}$) i residui sono matrici ($u_iv_i'$).
- Zeta: si scompone $F(z)/z$ e si rimoltiplica per $z$ (o si antitrasforma $zF$ = funzione anticipata).

## Collegamenti

- **Concetti correlati**: [[TDS - Trasformata di Laplace]] · [[TDS - Trasformata Zeta]] · [[TDS - Esponenziale di matrice]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[16 - TDS - Antitrasformate e residui#Antitrasformate e residui|Lezione 16 — Antitrasformate e residui]]
> - [[16 - TDS - Antitrasformate e residui#Residui con denominatori di grado maggiore di 1|Lezione 16 — Residui con denominatori di grado maggiore di 1]]
> - [[16 - TDS - Antitrasformate e residui#Residui complessi|Lezione 16 — Residui complessi]]
> - [[19 - TDS - Antitrasformata Zeta#Antitrasformazione|Lezione 19 — Antitrasformazione]]
