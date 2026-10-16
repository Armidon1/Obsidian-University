---
title: Pumping lemma per linguaggi regolari
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - linguaggi-regolari
---

# Pumping lemma per linguaggi regolari

> [!summary] In breve
> Se $L$ è regolare esiste $n$ tale che ogni $x \in L$ con $|x| \ge n$ si scrive $x = uvw$ con $|uv| \le n$, $|v| \ge 1$ e $uv^kw \in L$ per ogni $k \ge 0$. Si usa per dimostrare che un linguaggio **non** è regolare.

- Idea: $n$ = stati dell'ASF minimo; una stringa lunga almeno $n$ ripassa per uno stato, e il ciclo $v$ si può ripetere.
- **Condizione necessaria, non sufficiente**: regolare ⇒ pompaggio; non pompaggio ⇒ non regolare.

> [!example] $a^n b^n$ non è regolare
> $x = a^n b^n$; con $|uv| \le n$, $v = a^j$, $j \ge 1$; $uv^2w = a^{n+j}b^n \notin L$.

- Analogamente $0^h 1^k$ con $h > k > 0$ (si pompa verso il basso, $k = 0$).
- Ogni linguaggio **finito** è regolare.

## Collegamenti

- **Concetti correlati**: [[Automa a stati finiti]] · [[Espressione regolare]] · [[Gerarchia di Chomsky]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Pumping lemma|Lezione 10 — Pumping lemma]]
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Problemi di decidibilità sui linguaggi regolari|Lezione 10 — Problemi di decidibilità sui linguaggi regolari]]
