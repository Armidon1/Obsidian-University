---
title: Forma normale congiuntiva
tags:
  - modelli-di-calcolo
  - concetto
  - logica
  - sat
  - cnf
---

# Forma normale congiuntiva

> [!summary] In breve
> Una formula è in CNF se è una congiunzione di **clausole**, cioè disgiunzioni di letterali: $C_1 \wedge \dots \wedge C_n$. Ogni formula ha una CNF equivalente, ma potenzialmente esponenziale.

- **Letterale**: atomo o atomo negato; **clausola**: $L_1 \vee \dots \vee L_n$, scritta anche $\{L_1, \dots, L_n\}$; la **clausola vuota** è falsa.
- **Clausola definita**: un solo letterale positivo ($A \vee \neg B_1 \vee \dots$).
- **Convert1**: eliminare $\to, \leftrightarrow$; NNF (De Morgan, doppia negazione); distribuire $\vee$ su $\wedge$. Risultato **equivalente**, ma $(X_1 \wedge Y_1) \vee \dots \vee (X_n \wedge Y_n)$ diventa $2^n$ clausole.
- **DNF**: disgiunzione di congiunzioni; la soddisfacibilità in DNF è lineare (un termine senza letterali complementari).

## Collegamenti

- **Concetti correlati**: [[Trasformazione Convert2]] · [[Algoritmo DPLL]] · [[Problema SAT]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[13 - MC - Forme normali e algoritmo DPLL#Clausole e forma normale congiuntiva|Lezione 13 — Clausole e forma normale congiuntiva]]
> - [[13 - MC - Forme normali e algoritmo DPLL#Trasformazione in clausole: Convert1|Lezione 13 — Trasformazione in clausole: Convert1]]
> - [[13 - MC - Forme normali e algoritmo DPLL#DNF e soddisfacibilità|Lezione 13 — DNF e soddisfacibilità]]
