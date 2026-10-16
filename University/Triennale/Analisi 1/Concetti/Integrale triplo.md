---
title: Integrale triplo
tags:
  - analisi-1
  - concetto
  - integrali
  - più-variabili
---

# Integrale triplo

> [!summary] In breve
> ∭_X f dx dy dz (massa di un corpo di densità f); si calcola per fili (prima in z, poi doppio) o per strati (prima doppio sulla sezione D_z, poi in z).

$$\text{per fili: } \iint_D\left(\int_{g_1}^{g_2} f\,dz\right)dx\,dy, \qquad \text{per strati: } \int_a^b\left(\iint_{D_z} f\,dx\,dy\right)dz$$

- Volume: $|X| = \iiint_X 1$.
- Esempi: $\iiint z$ sul cono $\{z \le 1 - \rho\} = \frac{\pi}{12}$; $\iiint (x^2 + y^2)$ su $\{\rho \le z \le 1\} = \frac\pi{10}$; massa del tetraedro con densità $1 - z$: $\frac18$.
- Per strati conviene quando l'integranda dipende solo da $z$.

## Collegamenti

- **Concetti correlati**: [[Integrale doppio]] · [[Teorema di Fubini-Tonelli]] · [[Coordinate cilindriche e sferiche]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[10 - AN1 - Integrali Multipli#Integrali Tripli|Lezione 10 — Integrali Tripli]]
> - [[10 - AN1 - Integrali Multipli#Integrazione per fili|Lezione 10 — Integrazione per fili]]
> - [[10 - AN1 - Integrali Multipli#Integrazione per strati|Lezione 10 — Integrazione per strati]]
