---
title: Allineamento e Padding
tags:
  - sistemi-di-calcolo
  - concetto
  - memoria
  - ottimizzazione
  - linguaggio-c
---

# Allineamento e Padding

> [!summary] In breve
> Un oggetto di s byte va a un indirizzo multiplo di s; il compilatore inserisce padding tra i campi di una struct e in fondo (dimensione multipla del campo più grande). Ordinare i campi dal più grande riduce lo spazio.

```c
struct S { char a; int b; short c; char d; int e; char f; };  // 20 byte
struct S { int b; int e; short c; char a; char d; char f; };  // 16 byte
```

- Compromesso **tempo-spazio**: gli accessi disallineati sono lenti o generano un'eccezione.
- Allineamento ovunque: globali, stack, heap (16 byte), codice (linea di cache).
- Il compilatore **non può** riordinare i campi (lo vieta lo standard C): lo deve fare il programmatore.

## Collegamenti

- **Concetti correlati**: [[Frammentazione]] · [[Ottimizzazioni del Compilatore]] · [[Traduzione dei Costrutti C in Assembly]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[05 - SDC - Ottimizzazione dei programmi#Allineamento dei dati in memoria|Lezione 5 — Allineamento dei dati in memoria]]
> - [[05 - SDC - Ottimizzazione dei programmi#Ottimizzare lo spazio delle struct|Lezione 5 — Ottimizzare lo spazio delle struct]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Strutture|Lezione 3 — Strutture]]
