---
title: Eventi e Storicizzazione
tags:
  - basi-di-dati
  - concetto
  - progettazione-concettuale
---

# Eventi e Storicizzazione

> [!summary] In breve
> Pattern per gli aspetti dinamici: un evento diventa un'entità (o relazione) con data; una proprietà che cambia nel tempo si storicizza con un'entità StatoDiE identificata da data di inizio.

| Pattern | Schema |
|---|---|
| evento su E, uno per finestra temporale | entità V (Data) – SoggettoA (1,1) – E |
| evento su N entità, al massimo uno | relazione V con Data |
| evento su N entità, più d'uno | entità V con (1,1) verso ognuna |
| storicizzazione | E (proprietà rigide) – HaStato – StatoDiE (Inizio, proprietà variabili) |

Eventi se interessa il fenomeno, stati se interessano gli effetti.

## Collegamenti

- **Concetti correlati**: [[Reificazione]] · [[Metodologia di Progettazione Concettuale]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[05 - BD - Progettazione Concettuale#Pattern, rappresentazione di aspetti dinamici|Lezione 5 — Pattern, rappresentazione di aspetti dinamici]]
> - [[05 - BD - Progettazione Concettuale#Esercitazione 8|Lezione 5 — Esercitazione 8]]
