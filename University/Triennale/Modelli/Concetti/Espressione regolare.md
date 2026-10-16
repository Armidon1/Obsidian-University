---
title: Espressione regolare
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - linguaggi-regolari
---

# Espressione regolare

> [!summary] In breve
> Descrizione algebrica di un linguaggio, definita per induzione: i simboli, $\varepsilon$ e $\emptyset$ sono espressioni; se $e_1, e_2$ lo sono, lo sono $e_1 + e_2$ (unione), $e_1 e_2$ (concatenazione) ed $e^*$ (stella).

| espressione | linguaggio |
|---|---|
| $(0 + 1)^*$ | tutte le stringhe binarie |
| $a(b + c)a^*$ | $a$, poi $b$ o $c$, poi $a$ arbitrarie |
| $(0 + 11)^*1$ | blocchi di 0 e coppie 11, poi un 1 |
| $(b + abb)^*$ | ogni $a$ seguita da almeno due $b$ |

- Descrivono esattamente i linguaggi **regolari** (= tipo 3 = ASF).
- ER → ASF: costruzioni di chiusura (unione, concatenazione, stella); ASF/GR3 → ER: equazioni e **lemma di Arden** $X = AX + B \Rightarrow X = A^*B$.

## Collegamenti

- **Concetti correlati**: [[Automa a stati finiti]] · [[Gerarchia di Chomsky]] · [[Pumping lemma per linguaggi regolari]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Descrizione algebrica: le espressioni regolari|Lezione 9 — Descrizione algebrica: le espressioni regolari]]
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Dalle grammatiche alle espressioni regolari|Lezione 10 — Dalle grammatiche alle espressioni regolari]]
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Dalle espressioni regolari agli automi|Lezione 10 — Dalle espressioni regolari agli automi]]
