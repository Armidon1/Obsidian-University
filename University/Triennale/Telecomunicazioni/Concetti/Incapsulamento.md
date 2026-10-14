---
title: Incapsulamento
tags:
  - telecomunicazioni
  - concetto
  - protocolli
  - livelli
---

# Incapsulamento

> [!summary] In breve
> Scendendo lungo la pila, ogni livello aggiunge la propria **intestazione** al pacchetto del livello superiore, che diventa il suo **payload**. A destinazione ogni livello toglie la propria intestazione (de-incapsulamento).

```text
M                    messaggio   (applicazione)
Ht | M               segmento    (trasporto)
Hn | Ht | M          datagramma  (rete)
Hl | Hn | Ht | M     frame       (collegamento)
```

- Lo **switch** elabora fino a $H_l$, il **router** fino a $H_n$; solo gli host arrivano a $H_t$ e $M$.
- Un messaggio grande può diventare più segmenti, e un segmento più datagrammi: a destinazione vanno ricomposti.
- Analogia: la circolare (messaggio) nella busta interna (segmento) nella busta postale (datagramma).

## Collegamenti

- **Concetti correlati**: [[Pila di Protocolli Internet]] · [[Commutazione di Pacchetto]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#Incapsulamento|Capitolo 1 — Incapsulamento]]
