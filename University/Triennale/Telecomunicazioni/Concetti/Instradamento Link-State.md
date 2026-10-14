---
title: Instradamento Link-State
tags:
  - telecomunicazioni
  - concetto
  - routing
  - dijkstra
---

# Instradamento Link-State

> [!summary] In breve
> Ogni nodo diffonde in **broadcast** lo stato dei suoi collegamenti, così tutti hanno la mappa completa e calcolano localmente i percorsi minimi con **Dijkstra**. Complessità $O(n^2)$.

```text
N' = {u};  D(v) = c(u,v) se adiacente, altrimenti ∞
ciclo: scegli w ∉ N' con D(w) minimo; N' += w
       per v adiacente a w, v ∉ N':  D(v) = min(D(v), D(w) + c(w,v))
finché N' = N
```

- $D(v)$ = costo corrente, $p(v)$ = predecessore, $N'$ = nodi definitivi.
- Grafo d'esempio da $u$: x(1), y(2), v(2), w(3), z(4); tabella di inoltro: v → (u,v), tutto il resto → (u,x).
- $n(n+1)/2$ controlli, quindi $O(n^2)$; con uno heap si riduce.
- Con costi = carico si hanno **oscillazioni**; rimedio: istanti di esecuzione casuali (i router tendono ad auto-sincronizzarsi).
- Usato da **OSPF** e IS-IS.

## Collegamenti

- **Concetti correlati**: [[Algoritmi di Instradamento]] · [[Instradamento Distance-Vector]] · [[OSPF]] · [[Dijkstra Algorithm]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#Instradamento link-state (LS)|Capitolo 5 — Instradamento link-state (LS)]]
> - [[05 - TLC - Livello di rete - piano di controllo#Algoritmo di Dijkstra|Capitolo 5 — Algoritmo di Dijkstra]]
> - [[05 - TLC - Livello di rete - piano di controllo#Oscillazioni con costi sensibili al carico|Capitolo 5 — Oscillazioni con costi sensibili al carico]]
