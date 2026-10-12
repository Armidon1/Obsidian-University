---
title: Remote Procedure Call
tags:
  - sistemi-di-calcolo-2
  - concetto
  - sistemi-distribuiti
---

# Remote Procedure Call

> [!summary] In breve
> Chiamare una procedura su un'altra macchina come se fosse locale: gli stub impacchettano i parametri (marshalling) e li inviano. Semantiche in caso di guasti: at least once, at most once, exactly once.

| Semantica | Garanzia | Requisiti |
| --- | --- | --- |
| at least once | ≥ 1 esecuzione | ritrasmissione su timeout; solo operazioni **idempotenti** |
| at most once | ≤ 1 esecuzione | rilevare i duplicati |
| exactly once | esattamente 1 | gestire le chiamate orfane; molto complessa |

- Parametri per valore: facili; per riferimento: difficili (i puntatori sono locali).
- Binding persistente / non persistente; RPC sincrona / asincrona.

## Collegamenti

- **Concetti correlati**: [[Middleware]] · [[Message Passing]] · [[Sistema Distribuito]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[08 - SDC2 - Sistemi Distribuiti#Remote Procedure Call|Lezione 8 — Remote Procedure Call]]
> - [[08 - SDC2 - Sistemi Distribuiti#Binding|Lezione 8 — Binding]]
> - [[08 - SDC2 - Sistemi Distribuiti#Semantiche delle chiamate in caso di guasti|Lezione 8 — Semantiche delle chiamate in caso di guasti]]
