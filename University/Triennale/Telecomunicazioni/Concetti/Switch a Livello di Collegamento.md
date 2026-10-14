---
title: Switch a Livello di Collegamento
tags:
  - telecomunicazioni
  - concetto
  - switch
  - lan
---

# Switch a Livello di Collegamento

> [!summary] In breve
> Lo switch inoltra **frame** in base al **MAC** di destinazione usando una **tabella di commutazione** (MAC, interfaccia, tempo). È trasparente ai nodi, elimina le collisioni e collega segmenti eterogenei.

Frame per D arrivato sull'interfaccia $x$:
1. D non è in tabella → **flooding** su tutte tranne $x$;
2. D è su $x$ → **filtraggio** (scarto);
3. D è su $y \neq x$ → **inoltro** su $y$.

- Proprietà: niente collisioni (throughput aggregato = somma delle interfacce), collegamenti a velocità e su mezzi diversi, gestione (isola le schede "blateranti", raccoglie statistiche).
- **Switch poisoning**: MAC falsi riempiono la tabella e costringono al broadcast → sniffing.

## Collegamenti

- **Concetti correlati**: [[Autoapprendimento degli Switch]] · [[Switch e Router a Confronto]] · [[Switch]] · [[LAN Virtuali]] · [[Attacchi alle Reti]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#Switch a livello di collegamento|Capitolo 6 — Switch a livello di collegamento]]
> - [[06 - TLC - Livello di collegamento e reti locali#Inoltro e filtraggio|Capitolo 6 — Inoltro e filtraggio]]
> - [[06 - TLC - Livello di collegamento e reti locali#Proprietà della commutazione a livello di collegamento|Capitolo 6 — Proprietà della commutazione a livello di collegamento]]
