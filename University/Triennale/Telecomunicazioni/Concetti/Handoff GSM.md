---
title: Handoff GSM
tags:
  - telecomunicazioni
  - concetto
  - gsm
  - mobilita
---

# Handoff GSM

> [!summary] In breve
> L'**handoff** sposta una chiamata in corso da una stazione base a un'altra, per segnale debole o cella sovraccarica. Con un MSC comune avviene in **8 fasi** preparate dalla rete; tra MSC diversi si usa l'**MSC di appoggio**, fisso per tutta la chiamata.

1. vecchia BS → MSC: handoff verso la nuova BS
2. MSC prepara il percorso
3. la nuova BS alloca il canale
4. la nuova BS conferma
5. la stazione mobile viene avvisata (fino a qui non sapeva nulla)
6. attivazione del canale
7. completamento → re-instradamento
8. rilascio delle risorse vecchie

- Decisione basata sui beacon misurati 1–2 volte al secondo; l'algoritmo non è standardizzato.
- **MSC di appoggio**: al massimo 3 MSC in catena (di appartenenza, di appoggio, visitato); in alternativa concatenamento (IS-41).

## Collegamenti

- **Concetti correlati**: [[Mobilità nelle Reti Cellulari]] · [[Rete Cellulare GSM]] · [[Instradamento Indiretto e Diretto]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#Handoff in GSM|Capitolo 7 — Handoff in GSM]]
