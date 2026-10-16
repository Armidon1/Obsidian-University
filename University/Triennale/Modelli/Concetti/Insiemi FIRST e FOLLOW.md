---
title: Insiemi FIRST e FOLLOW
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - ll-parsing
---

# Insiemi FIRST e FOLLOW

> [!summary] In breve
> $\mathrm{FIRST}(\alpha)$ = terminali con cui può iniziare una stringa derivata da $\alpha$ (più $\varepsilon$ se $\alpha \Rightarrow^* \varepsilon$); $\mathrm{FOLLOW}(A)$ = terminali (o `$`) che possono seguire $A$ in una forma di frase.

**FIRST** di $A \to B_1 \dots B_k$: si aggiunge $\mathrm{FIRST}(B_1) \setminus \{\varepsilon\}$; se $B_1$ si annulla anche $\mathrm{FIRST}(B_2)$, e così via; $\varepsilon$ solo se si annullano tutti.

**FOLLOW**: $\$ \in \mathrm{FOLLOW}(S)$; per $X \to \alpha B \beta$: $\mathrm{FIRST}(\beta) \setminus \{\varepsilon\} \subseteq \mathrm{FOLLOW}(B)$; se $\beta \Rightarrow^* \varepsilon$ (o $\beta$ è vuota), $\mathrm{FOLLOW}(X) \subseteq \mathrm{FOLLOW}(B)$.

**SELECT**($A \to \alpha$) = $\mathrm{FIRST}(\alpha)$, più $\mathrm{FOLLOW}(A)$ se $\alpha$ si annulla (senza $\varepsilon$).

> [!example] $E \to TE'$, $E' \to +TE' \mid \varepsilon$, $T \to FT'$, $T' \to *FT' \mid \varepsilon$, $F \to \mathrm{id} \mid (E)$
> $\mathrm{FIRST}(E) = \{\mathrm{id}, (\}$, $\mathrm{FIRST}(E') = \{+, \varepsilon\}$; $\mathrm{FOLLOW}(E) = \mathrm{FOLLOW}(E') = \{\$, )\}$, $\mathrm{FOLLOW}(T) = \{+, ), \$\}$, $\mathrm{FOLLOW}(F) = \{*, +, ), \$\}$.

## Collegamenti

- **Concetti correlati**: [[Grammatica LL(1)]] · [[Parser a discesa ricorsiva]] · [[Item LR(0)]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[11 - MC - Analisi sintattica top-down e automi a pila#FIRST-set|Lezione 11 — FIRST-set]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#FOLLOW-set|Lezione 11 — FOLLOW-set]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#SELECT-set per la grammatica modificata|Lezione 11 — SELECT-set per la grammatica modificata]]
