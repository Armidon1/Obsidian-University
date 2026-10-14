---
title: Longest Prefix Match
tags:
  - telecomunicazioni
  - concetto
  - router
  - indirizzamento
---

# Longest Prefix Match

> [!summary] In breve
> La tabella di inoltro contiene **prefissi** di indirizzi, non indirizzi singoli. Se un indirizzo corrisponde a più righe, il router usa quella con il **prefisso più lungo**.

| Prefisso | Interfaccia |
| --- | --- |
| `11001000 00010111 00010` | 0 |
| `11001000 00010111 00011000` | 1 |
| `11001000 00010111 00011` | 2 |
| altrimenti | 3 |

- `…00011000 10101010` corrisponde alle righe 1 (24 bit) e 2 (21 bit) → vince la **riga 1**, cioè l'interfaccia 1.
- Ricerca in ns: hardware, SRAM/DRAM, **TCAM** (tempo costante).
- Rende possibile l'**aggregazione** degli indirizzi, con eccezioni più specifiche (es. /23 dentro un /20).
- È un caso particolare del paradigma **match-action**.

## Collegamenti

- **Concetti correlati**: [[CIDR]] · [[Aggregazione di Indirizzi]] · [[Architettura di un Router]] · [[Inoltro Generalizzato e OpenFlow]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[04 - TLC - Livello di rete - piano dei dati#Corrispondenza a prefisso più lungo|Capitolo 4 — Corrispondenza a prefisso più lungo]]
> - [[04 - TLC - Livello di rete - piano dei dati#Aggregazione di indirizzi (Box 4.1)|Capitolo 4 — Aggregazione di indirizzi (Box 4.1)]]
