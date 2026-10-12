---
title: Shell e Comandi Unix
tags:
  - sistemi-di-calcolo
  - concetto
  - shell
  - strumenti
---

# Shell e Comandi Unix

> [!summary] In breve
> La shell (bash) esegue comandi interni (built-in, es. `cd`) o esterni (eseguibili cercati nel PATH, lanciati con fork + exec); offre redirezione (`>`, `>>`, `2>`, `&>`), pipe (`|`) e gestione dei job (`&`, CTRL+Z, `fg`, `bg`, `jobs`).

- Ordine di risoluzione: alias → built-in → binario nel `PATH` (la prima directory che lo contiene). `type cmd` dice cosa verrà eseguito.
- File: `pwd`, `cd`, `ls -l`, `touch`, `mv`, `mkdir`, `rmdir`, `rm -rf`, `cp -R`.
- Utili: `cat`, `less`, `man`, `env`, `head`, `tail`, `which`, `whereis`, `grep`, `ln`.
- Terminazione: CTRL+C (`SIGINT`), `kill PID` (`SIGTERM`), `kill -9 PID` (`SIGKILL`, non ignorabile).

## Collegamenti

- **Concetti correlati**: [[Permessi e Ownership]] · [[File Descriptor]] · [[Segnali]] · [[fork]] · [[exec e Variabili d'Ambiente]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[09 - SDC - Appendici#Appendice B: la shell dei comandi|Lezione 9 — Appendice B: la shell dei comandi]]
> - [[09 - SDC - Appendici#Redirezione di stdin, stdout e stderr|Lezione 9 — Redirezione di stdin, stdout e stderr]]
> - [[09 - SDC - Appendici#Esecuzione in background e terminazione|Lezione 9 — Esecuzione in background e terminazione]]
