---
title: Puntatori a Funzione
tags:
  - sistemi-operativi
  - concetto
  - linguaggio-c
---

# Puntatori a Funzione

> [!summary] In breve
> Variabili che contengono l'indirizzo di una funzione; il tipo dipende da ritorno e parametri. Un array di puntatori a funzione indicizzato da un numero è la struttura di interrupt vector e syscall vector.

```c
typedef int (*IntCharFnPtr)(char);
IntCharFnPtr p = myFn;      // assegnazione (nome = indirizzo)
int r = (*p)('c');          // oppure p('c')
void (*actions[10])(int);   // vettore di puntatori a funzione
```

- Puntatori di tipo diverso non sono assegnabili tra loro.
- Usi: macchine a stati, callback, **[[Interrupt Vector]]**, **[[System Call|syscall vector]]**, **[[Virtual Method Table|VMT]]**, `ThreadFn` dei TCB, `makecontext`.

## Collegamenti

- **Concetti correlati**: [[Interrupt Vector]] · [[System Call]] · [[Virtual Method Table]] · [[ucontext]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[03 - SO - Programmazione OOP in C#Puntatori a funzione|Lezione 3 — Puntatori a funzione]]
> - [[03 - SO - Programmazione OOP in C#Esempio: vettore di puntatori a funzione|Lezione 3 — Esempio: vettore di puntatori a funzione]]
