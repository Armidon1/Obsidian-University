---
title: Teorema di Fubini-Tonelli
tags:
  - analisi-1
  - concetto
  - integrali
  - più-variabili
---

# Teorema di Fubini-Tonelli

> [!summary] In breve
> Per f continua su un dominio semplice, l'integrale doppio si calcola come due integrali in una variabile in successione: ∬ f = ∫ₐᵇ (∫_{g₁(x)}^{g₂(x)} f dy) dx.

$$X\ y\text{-semplice}: \iint_X f = \int_a^b\left(\int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\right)dx, \qquad X\ x\text{-semplice}: \iint_X f = \int_c^d\left(\int_{h_1(y)}^{h_2(y)} f(x, y)\,dx\right)dy$$

- Interpretazione: si integra l'area $A(x)$ delle sezioni (principio di Cavalieri).
- Nell'integrale interno l'altra variabile è costante.
- **Scegliere l'ordine**: $\iint \sin(y^3)$ su $\{\sqrt x \le y \le 1\}$ si fa solo integrando prima in $x$: $\frac13(1 - \cos 1)$.
- In $\mathbb{R}^3$: integrazione **per fili** e **per strati**.

## Collegamenti

- **Concetti correlati**: [[Domini normali]] · [[Integrale doppio]] · [[Integrale triplo]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[10 - AN1 - Integrali Multipli#Il teorema|Lezione 10 — Il teorema]]
> - [[10 - AN1 - Integrali Multipli#Integrazione per fili|Lezione 10 — Integrazione per fili]]
