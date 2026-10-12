---
title: Paging
tags:
  - sistemi-operativi
  - concetto
  - memoria
---

# Paging

> [!summary] In breve
> Memoria logica divisa in pagine e memoria fisica in frame della stessa dimensione; la page table (una per processo) mappa pagina → frame. Niente frammentazione esterna.

- Indirizzo = (p, d): `fisico = page_table[p] · page_size + d`. Con pagine da 4 KB a 32 bit: 20 bit di p e 12 bit di d.
- **PTBR** / **PTLR**; cambiare spazio di indirizzi = cambiare il PTBR.
- Ogni accesso ai dati costa **2 accessi** in memoria → si usa la **TLB**.
- Entry: frame, **bit di validità**, bit di protezione (r/w/x), e per la memoria virtuale **reference** e **dirty** bit.
- **Pagine condivise**: codice rientrante read-only (es. editor, librerie) mappato sugli stessi frame da più processi.
- Contro: frammentazione interna (ultima pagina) e spazio per la page table.

## Collegamenti

- **Concetti correlati**: [[TLB]] · [[Page Table Gerarchica]] · [[Effective Access Time]] · [[MMU]] · [[Memoria Virtuale]] · [[Frammentazione]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Paging|Lezione 10 — Paging]]
> - [[10 - SO - Gestione della Memoria#Protezione con il paging|Lezione 10 — Protezione con il paging]]
> - [[10 - SO - Gestione della Memoria#Pagine condivise|Lezione 10 — Pagine condivise]]
