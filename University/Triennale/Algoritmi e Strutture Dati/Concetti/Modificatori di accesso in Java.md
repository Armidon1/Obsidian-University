---
title: Modificatori di accesso in Java
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - java
  - incapsulamento
---

# Modificatori di accesso in Java

> [!summary] In breve
> `public`, `protected`, nessun modificatore (package) e `private` stabiliscono chi può vedere una classe, un campo o un metodo: sono lo strumento dell'incapsulamento.

| Modificatore | Visibile da |
|---|---|
| `public` | ovunque |
| `protected` | stesso package + sottoclassi |
| (nessuno) | stesso package |
| `private` | solo la classe stessa |

Altri modificatori: `static` (membro della classe, non dell'istanza), `final` (costante / metodo non ridefinibile / classe non estendibile), `abstract` (metodo senza corpo / classe non istanziabile).

Regola pratica: campi `private`, accesso tramite metodi (getter/setter) solo se serve.

## Collegamenti

- **Concetti correlati**: [[Interfacce e classi astratte]] · [[Ereditarietà in Java]] · [[Tipo di dato astratto]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[01 - ASD - Introduzione a Java#Modificatori per il controllo dell'accesso|Lezione 1 — Modificatori per il controllo dell'accesso]]
