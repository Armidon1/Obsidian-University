---
title: CSMA-CD
tags:
  - telecomunicazioni
  - concetto
  - accesso-multiplo
  - ethernet
---

# CSMA-CD

> [!summary] In breve
> **CSMA/CD**: ascolta prima di trasmettere (*carrier sensing*) e smetti se rilevi una collisione (*collision detection*), poi aspetta un tempo casuale scelto con il **binary exponential backoff**. Le collisioni restano possibili a causa del ritardo di propagazione.

- Passi della NIC: buffer → canale libero? → trasmetti ascoltando → collisione: interrompi → backoff → riprova.
- **Backoff**: dopo l'$n$-esima collisione $K \in \{0, \dots, 2^n - 1\}$ (con $n \le 10$), si attende $K \cdot 512$ bit (5,12 µs a 100 Mbps).
- Efficienza:
  $$\frac{1}{1 + 5\,d_{prop}/d_{trasm}}$$
  tende a 1 se $d_{prop} \to 0$ o $d_{trasm} \to \infty$.
- Diagramma spazio-temporale: B trasmette a $t_0$, D a $t_1$ prima di "sentire" B → collisione.
- Con switch full-duplex non ci sono collisioni, e CSMA/CD diventa superfluo.

## Collegamenti

- **Concetti correlati**: [[Protocolli ALOHA]] · [[Ethernet]] · [[Protocolli di Accesso Multiplo]] · [[Ritardi nelle Reti a Commutazione di Pacchetto]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[06 - TLC - Livello di collegamento e reti locali#CSMA: accesso multiplo con rilevamento della portante|Capitolo 6 — CSMA: accesso multiplo con rilevamento della portante]]
> - [[06 - TLC - Livello di collegamento e reti locali#CSMA/CD|Capitolo 6 — CSMA/CD]]
