---
title: Matrice hessiana
tags:
  - analisi-1
  - concetto
  - più-variabili
  - derivate
  - estremi
---

# Matrice hessiana

> [!summary] In breve
> Hf = (∂²f/∂xᵢ∂xⱼ): la matrice delle derivate seconde, simmetrica per Schwarz. Il suo segno classifica i punti critici come la derivata seconda in una variabile.

$$f(x) = f(x_0) + \nabla f(x_0)\cdot(x - x_0) + \tfrac12 (x - x_0)^T Hf(x_0)(x - x_0) + o(\|x - x_0\|^2)$$

| $Hf(x_0)$ in un punto critico | Natura |
|---|---|
| definita positiva (autovalori $> 0$) | minimo locale |
| definita negativa (autovalori $< 0$) | massimo locale |
| indefinita (autovalori di segno opposto) | sella |
| semi-definita | non si conclude |

**Criterio di Hurwitz** (minori principali): definita positiva $\iff \det A_k > 0\ \forall k$; definita negativa $\iff (-1)^k\det A_k > 0$.

## Collegamenti

- **Concetti correlati**: [[Teorema di Schwarz]] · [[Estremi in più variabili]] · [[Convessità e flessi]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[08 - AN1 - Calcolo Differenziale in più Variabili#Matrice hessiana|Lezione 8 — Matrice hessiana]]
> - [[08 - AN1 - Calcolo Differenziale in più Variabili#Matrici definite|Lezione 8 — Matrici definite]]
> - [[08 - AN1 - Calcolo Differenziale in più Variabili#Autovalori e criterio di Hurwitz|Lezione 8 — Autovalori e criterio di Hurwitz]]
