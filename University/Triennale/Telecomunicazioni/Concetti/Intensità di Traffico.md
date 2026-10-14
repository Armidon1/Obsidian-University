---
title: Intensità di Traffico
tags:
  - telecomunicazioni
  - concetto
  - prestazioni
  - code
---

# Intensità di Traffico

> [!summary] In breve
> $La/R$ è il rapporto tra la velocità con cui i bit arrivano in coda e quella con cui escono. Se supera 1 la coda cresce senza limiti; vicino a 1 il ritardo medio esplode e aumentano le perdite.

- $a$ = pacchetti/s in arrivo, $L$ = bit per pacchetto, $R$ = bps del collegamento.
- **Regola d'oro**: progettare in modo che $La/R \le 1$.
- Con $La/R \le 1$ conta la natura del traffico:
  - arrivi periodici → nessuna attesa;
  - raffiche di $N$ pacchetti → l'$n$-esimo attende $(n-1)L/R$.
- Ritardo medio di accodamento in funzione di $La/R$: curva che tende all'infinito per $La/R \to 1$.
- Buffer finito → **perdita di pacchetti** (*buffer overflow*), che aumenta con l'intensità di traffico; TCP ritrasmette.

## Collegamenti

- **Concetti correlati**: [[Ritardi nelle Reti a Commutazione di Pacchetto]] · [[Commutazione di Pacchetto]] · [[Attacchi alle Reti]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#Ritardo di accodamento e intensità di traffico|Capitolo 1 — Ritardo di accodamento e intensità di traffico]]
> - [[01 - TLC - Reti di calcolatori e Internet#Perdita di pacchetti|Capitolo 1 — Perdita di pacchetti]]
