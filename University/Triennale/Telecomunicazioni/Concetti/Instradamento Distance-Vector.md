---
title: Instradamento Distance-Vector
tags:
  - telecomunicazioni
  - concetto
  - routing
  - bellman-ford
---

# Instradamento Distance-Vector

> [!summary] In breve
> Algoritmo **distribuito, iterativo e asincrono**: ogni nodo scambia con i vicini il proprio **vettore delle distanze** e lo aggiorna con la formula di **Bellman-Ford**.

$$d_x(y) = \min_v \{\, c(x,v) + d_v(y) \,\}$$

- Il nodo $x$ conosce $c(x,v)$, il proprio $\mathbf{D}_x$ e i vettori $\mathbf{D}_v$ dei vicini; se $\mathbf{D}_x$ cambia lo invia ai vicini.
- Prossimo hop verso $y$ = il vicino $v^*$ che realizza il minimo.
- Esempio: $x, y, z$ con costi 2, 1, 7 → $D_x(z) = \min\{2+1, 7+0\} = 3$.

| | LS | DV |
| --- | --- | --- |
| Parla con | tutti (broadcast) | solo i vicini |
| Messaggi | $O(\lvert N\rvert\lvert E\rvert)$ | solo tra vicini |
| Convergenza | $O(\lvert N\rvert^2)$ | lenta, cicli, conteggio all'infinito |
| Robustezza | errori localizzati | errori propagati in tutta la rete |

- Usato da RIP, BGP e dall'ARPAnet originale.

## Collegamenti

- **Concetti correlati**: [[Conteggio all'Infinito]] · [[Instradamento Link-State]] · [[Algoritmi di Instradamento]] · [[Protocollo BGP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[05 - TLC - Livello di rete - piano di controllo#Instradamento distance-vector (DV)|Capitolo 5 — Instradamento distance-vector (DV)]]
> - [[05 - TLC - Livello di rete - piano di controllo#Formula di Bellman-Ford|Capitolo 5 — Formula di Bellman-Ford]]
> - [[05 - TLC - Livello di rete - piano di controllo#L'algoritmo|Capitolo 5 — L'algoritmo]]
> - [[05 - TLC - Livello di rete - piano di controllo#Esempio su tre nodi|Capitolo 5 — Esempio su tre nodi]]
> - [[05 - TLC - Livello di rete - piano di controllo#Confronto tra LS e DV|Capitolo 5 — Confronto tra LS e DV]]
