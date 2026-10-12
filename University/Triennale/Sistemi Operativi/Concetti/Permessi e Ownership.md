---
title: Permessi e Ownership
tags:
  - sistemi-operativi
  - concetto
  - file-system
  - protezione
---

# Permessi e Ownership

> [!summary] In breve
> Ogni file ha un proprietario e un gruppo; per user, group e others ci sono i permessi r, w, x (`chown`, `chmod`).

- `-rw-rw-r--`: tipo, poi rwx per user, group e others.
- `chmod u+x f`, `chmod go-w f`, `chmod 644 f`; `chown user:group f`.
- Sulle directory: r = elencare, w = creare/eliminare, x = attraversare.
- Root può fare (quasi) tutto.

## Collegamenti

- **Concetti correlati**: [[File System]] · [[Dual Mode]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[12 - SO - File System#Ownership e permessi|Lezione 12 — Ownership e permessi]]
> - [[09 - SDC - Appendici#Permessi POSIX e chmod|Sistemi di Calcolo, cap. A–D — Permessi POSIX e chmod]]
