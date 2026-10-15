---
title: Architettura Multi-Tier
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - architettura-software
  - multi-tier
---

# Architettura Multi-Tier

> [!summary] In breve
> Distribuzione dei tre layer su 1, 2 o 3 (o più) tier: più tier significano più manutenibilità e scalabilità, ma costi di comunicazione.

| | Dove stanno i layer | Pro | Contro |
|---|---|---|---|
| 1-tier | tutto su una macchina | niente comunicazione, prestazioni | poco portabile e manutenibile |
| 2-tier | presentation sul client | client indipendenti, nasce l'API | logica e dati accoppiati |
| 3-tier | un tier per layer (+ [[Middleware]]) | scalabile, manutenibile, distribuibile | comunicazione tra tier |

Nel 3-tier scalabile ogni tier ha più server dietro un load balancer (DB master/slave).

## Collegamenti

- **Concetti correlati**: [[Layer e Tier]] · [[Middleware]] · [[Service-Oriented Architecture]] · [[Modello Client-Server]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[02 - LASS - Software Architectures#Architetture 1-tier, 2-tier e 3-tier|Lezione 2 — Architetture 1-tier, 2-tier e 3-tier]]
> - [[02 - LASS - Software Architectures#Scalabilità del 3-tier|Lezione 2 — Scalabilità del 3-tier]]
> - [[02 - LASS - Software Architectures#Architetture distribuite: multi-tier e service-oriented|Lezione 2 — Architetture distribuite: multi-tier e service-oriented]]
