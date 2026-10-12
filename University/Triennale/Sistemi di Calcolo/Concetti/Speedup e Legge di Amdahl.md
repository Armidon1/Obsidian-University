---
title: Speedup e Legge di Amdahl
tags:
  - sistemi-di-calcolo
  - concetto
  - prestazioni
  - ottimizzazione
---

# Speedup e Legge di Amdahl

> [!summary] In breve
> Speedup S = T/T'. Se una parte che pesa α del tempo diventa k volte più veloce: S = 1 / (α/k + 1 − α), che con k → ∞ non supera 1/(1 − α).

$$S = \frac{1}{\frac{\alpha}{k} + 1 - \alpha}$$

- Esempio: α = 0.4, k = 2 → S = 1/0.8 = **1.25**. Anche con k infinito: S ≤ 1/0.6 ≈ 1.67.
- Conseguenza: conviene ottimizzare gli **hot spot** (α grande), che si trovano con il **profiling**.
- Nata per stimare i limiti della parallelizzazione.

## Collegamenti

- **Concetti correlati**: [[Profiling]] · [[Ottimizzazioni del Compilatore]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[05 - SDC - Ottimizzazione dei programmi#Speedup e legge di Amdahl|Lezione 5 — Speedup e legge di Amdahl]]
