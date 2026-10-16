---
title: Tabella hash
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - mappe
  - hashing
---

# Tabella hash

> [!summary] In breve
> Una tabella hash memorizza le voci in un array di $N$ bucket, mettendo la chiave $k$ in posizione $h(k)$: con un buon hash e fattore di carico basso le operazioni costano $O(1)$ atteso.

- **Funzione di hash** $h(k) = $ compressione(codice hash($k$)) ∈ $[0, N-1]$.
- **Collisione**: $h(k_1) = h(k_2)$ con $k_1 \ne k_2$; si gestisce con [[Concatenazione separata|concatenazione separata]] o [[Indirizzamento aperto|indirizzamento aperto]].
- **Fattore di carico** $\lambda = n/N$: va tenuto basso ($< 0.9$ con concatenazione, $< 0.5$ con indirizzamento aperto); se cresce si fa **rehashing** in una tabella circa doppia (costo ammortizzato $O(1)$).
- Caso peggiore $O(n)$ (tutte le chiavi nello stesso bucket).
- Non mantiene alcun ordine tra le chiavi.

## Collegamenti

- **Concetti correlati**: [[Funzione di hash]] · [[Concatenazione separata]] · [[Indirizzamento aperto]] · [[Mappa (ADT)]] · [[Hashing]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Tabelle hash|Lezione 10 — Tabelle hash]]
