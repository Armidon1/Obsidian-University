---
title: Protocolli ALOHA
tags:
  - telecomunicazioni
  - concetto
  - accesso-multiplo
  - aloha
---

# Protocolli ALOHA

> [!summary] In breve
> Protocolli ad accesso casuale: si trasmette a velocità piena e, dopo una collisione, si ritrasmette con probabilità $p$. **Slotted ALOHA** (slot sincronizzati) ha efficienza massima $1/e \approx 37\%$; **ALOHA puro** $1/2e \approx 18\%$.

- Slotted: successo di un nodo qualsiasi $= Np(1-p)^{N-1}$ → per $N \to \infty$ vale $1/e$. Il 37% degli slot è utile, il 37% vuoto, il 26% in collisione.
- Puro: intervallo vulnerabile **doppio** → $p(1-p)^{2(N-1)}$ → $1/2e$.
- Pro: un nodo solo usa $R$; decentralizzato. Contro: slot sprecati per collisioni e slot vuoti.
- 100 Mbps in slotted ALOHA → meno di 37 Mbps utili.
- Origine: **ALOHAnet** di Norm Abramson (Hawaii, 1970), che ispirò Metcalfe ed Ethernet.

## Collegamenti

- **Concetti correlati**: [[CSMA-CD]] · [[Protocolli di Accesso Multiplo]] · [[Storia di Internet]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Protocolli ad accesso casuale|Capitolo 6 — Protocolli ad accesso casuale]]
> - [[06 - TLC - Livello di collegamento e reti locali#Slotted ALOHA|Capitolo 6 — Slotted ALOHA]]
> - [[06 - TLC - Livello di collegamento e reti locali#ALOHA puro|Capitolo 6 — ALOHA puro]]
