---
title: Linking Statico e Dinamico
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - compilazione
---

# Linking Statico e Dinamico

> [!summary] In breve
> Statico: le librerie vengono copiate nell'eseguibile. Dinamico: il collegamento avviene a runtime tramite uno stub, e una sola copia della shared library (`.so`) viene condivisa da tutti i processi.

- **Stub**: piccolo codice che trova la routine in memoria, sostituisce sé stesso con il suo indirizzo e la esegue.
- L'OS aggiunge la libreria allo spazio di indirizzi del processo se non c'è già.
- Pro del dinamico: meno memoria e disco, aggiornamenti senza ricompilare. Le pagine di codice sono condivise (vedi [[Paging]]).

## Collegamenti

- **Concetti correlati**: [[Address Binding]] · [[Loader ed ELF]] · [[Compilazione e Linking con gcc]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Linking statico e dinamico|Lezione 10 — Linking statico e dinamico]]
> - [[02 - SO - Programmi, Makefile e pkg-config#Costruzione di un eseguibile|Lezione 2 — Costruzione di un eseguibile]]
