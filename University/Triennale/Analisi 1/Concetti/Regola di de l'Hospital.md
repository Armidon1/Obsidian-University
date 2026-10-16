---
title: Regola di de l'Hospital
tags:
  - analisi-1
  - concetto
  - derivate
  - limiti
---

# Regola di de l'Hospital

> [!summary] In breve
> Per forme 0/0 o ∞/∞: se esiste lim f'/g' = l, allora anche lim f/g = l.

$$\lim \frac{f}{g} \overset{H}{=} \lim \frac{f'}{g'} \qquad \text{(forme } \tfrac00, \tfrac\infty\infty,\ g' \neq 0)$$

- Si può iterare: $\lim_{x\to0} \frac{x - \sin x}{x^3} = \frac16$.
- $0 \cdot \infty$ si riporta a un rapporto; $f^g$ si scrive $e^{g\ln f}$.
- Errori tipici:
  - applicarla a forme determinate ($\frac{1 + x}{2 + x}$);
  - concludere che $\lim\frac fg$ non esiste se non esiste $\lim\frac{f'}{g'}$ ($\frac{x + \sin x}{x} \to 1$).
- Con il teorema fondamentale permette limiti con integrali non calcolabili.

## Collegamenti

- **Concetti correlati**: [[Forme indeterminate]] · [[Formula di Taylor]] · [[Gerarchia degli infiniti]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[05 - AN1 - Calcolo Differenziale#Le Regole di de l'Hospital|Lezione 5 — Le Regole di de l'Hospital]]
> - [[06 - AN1 - Calcolo Integrale#Integrazione per sostituzione|Lezione 6 — Integrazione per sostituzione]]
