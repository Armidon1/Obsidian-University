---
title: Regole di derivazione
tags:
  - analisi-1
  - concetto
  - derivate
---

# Regole di derivazione

> [!summary] In breve
> Linearità, prodotto (f'g + fg'), quoziente ((gf' − g'f)/g²), catena ((g∘f)' = g'(f)·f') e inversa ((f⁻¹)' = 1/f').

| Regola | Formula |
|---|---|
| linearità | $(\alpha f + \beta g)' = \alpha f' + \beta g'$ |
| prodotto | $(fg)' = f'g + fg'$ |
| quoziente | $\left(\frac fg\right)' = \frac{gf' - g'f}{g^2}$ |
| catena | $(g \circ f)'(x) = g'(f(x))\, f'(x)$ |
| inversa | $(f^{-1})'(y_0) = \frac{1}{f'(x_0)}$ |
| potenza di funzioni | $(f^g)' = f^g\left(g'\ln f + g\frac{f'}{f}\right)$ |

- Ogni regola di derivazione dà una regola di integrazione: prodotto → [[Integrazione per parti|per parti]], catena → [[Integrazione per sostituzione|per sostituzione]].
- In più variabili la catena diventa $J_{g\circ f} = J_g(f(x))\,J_f(x)$.

## Collegamenti

- **Concetti correlati**: [[Derivata]] · [[Integrazione per parti]] · [[Integrazione per sostituzione]] · [[Matrice jacobiana]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[05 - AN1 - Calcolo Differenziale#Somme, prodotti e rapporti|Lezione 5 — Somme, prodotti e rapporti]]
> - [[05 - AN1 - Calcolo Differenziale#Derivazione delle funzioni composte|Lezione 5 — Derivazione delle funzioni composte]]
> - [[05 - AN1 - Calcolo Differenziale#Derivazione delle funzioni inverse|Lezione 5 — Derivazione delle funzioni inverse]]
