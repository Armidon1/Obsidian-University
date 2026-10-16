---
title: Gerarchia degli infiniti
tags:
  - analisi-1
  - concetto
  - limiti
---

# Gerarchia degli infiniti

> [!summary] In breve
> Per n → +∞: ln n ≪ n^α ≪ qⁿ ≪ n! ≪ nⁿ (α > 0, q > 1), dove a ≪ b significa a/b → 0.

$$\ln(n) \ll n^\alpha \ll q^n \ll n! \ll n^n \qquad (\alpha > 0,\ q > 1)$$

| Limite | Valore |
|---|---|
| $\frac{\ln n}{n^\alpha}$ | $0$ |
| $\frac{n^\alpha}{q^n}$ | $0$ |
| $\frac{q^n}{n!}$ | $0$ |
| $\frac{n!}{n^n}$ | $0$ |

- Per le funzioni: $\frac{\ln x}{x^\alpha} \to 0$ per $x \to +\infty$ e $x^\alpha \ln x \to 0$ per $x \to 0^+$ (de l'Hospital).
- È la stessa scala delle [[Funzioni di crescita]] in informatica.

## Collegamenti

- **Concetti correlati**: [[Forme indeterminate]] · [[Limiti notevoli]] · [[Regola di de l'Hospital]] · [[Funzioni di crescita]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[12 - AN1 - Appendice#Successioni|Lezione 12 — Successioni]]
> - [[05 - AN1 - Calcolo Differenziale#Le Regole di de l'Hospital|Lezione 5 — Le Regole di de l'Hospital]]
