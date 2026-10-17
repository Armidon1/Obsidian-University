---
title: TDS - Matrice di transizione dello stato
tags:
  - teoria-dei-sistemi
  - concetto
  - rappresentazione-con-lo-stato
---

# TDS - Matrice di transizione dello stato

> [!summary] In breve
> $\Phi(t)=e^{At}$ porta lo stato iniziale nello stato al tempo $t$ (evoluzione libera); nel discreto $\Phi(t)=A^t$.

- Forma esplicita: $x(t)=\Phi(t-t_0)x_0+\int_{t_0}^tH(t-\tau)u(\tau)\,d\tau$, con $H(t)=e^{At}B$.
- **Semigruppo**: $\Phi(0)=I$, $\Phi(t-t_0)=\Phi(t-t_1)\Phi(t_1-t_0)$ (lo stato riassume tutto il passato).
- **Fattorizzazione**: $H(t-\tau)=\Phi(t-t_1)H(t_1-\tau)$.
- Ritorno alla forma implicita: $A=\dot\Phi(0)$, $B=H(0)$, $C=\Psi(0)$.
- In Laplace $\Phi(s)=(sI-A)^{-1}$; in Zeta $\Phi(z)=z(zI-A)^{-1}$.

## Collegamenti

- **Concetti correlati**: [[TDS - Esponenziale di matrice]] · [[TDS - Evoluzione libera e forzata]] · [[TDS - Stazionarietà]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[04 - TDS - Uscita forzata e dalla forma esplicita alla implicita#Informazione nello stato iniziale|Lezione 4 — Informazione nello stato iniziale]]
> - [[04 - TDS - Uscita forzata e dalla forma esplicita alla implicita#Dalla forma esplicita alla forma implicita|Lezione 4 — Dalla forma esplicita alla forma implicita]]
> - [[15 - TDS - Trasformata di Laplace#Trasformate delle matrici della forma esplicita|Lezione 15 — Trasformate delle matrici della forma esplicita]]
