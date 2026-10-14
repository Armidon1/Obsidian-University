---
title: Gerarchia degli ISP
tags:
  - telecomunicazioni
  - concetto
  - internet
  - isp
---

# Gerarchia degli ISP

> [!summary] In breve
> Internet è una **rete di reti**: ISP di accesso → ISP regionali → ISP di primo livello (tier-1), con relazioni **cliente–fornitore**, più PoP, multi-homing, peering, IXP e le reti private dei content provider.

| Elemento | Significato |
| --- | --- |
| **Cliente / fornitore** | l'ISP di livello più basso paga quello superiore; i tier-1 non pagano nessuno |
| **Tier-1** | circa una dozzina (Level 3, AT&T, Sprint, NTT) |
| **PoP** | gruppo di router del provider a cui si collegano i clienti |
| **Multi-homing** | collegarsi a 2+ provider (tutti tranne i tier-1) |
| **Peering** | collegamento diretto e **gratuito** tra ISP pari |
| **IXP** | punto d'incontro dove più ISP fanno peering (~400 nel 2016) |
| **Content provider network** | rete privata (es. Google) che fa peering con gli ISP bassi per aggirare quelli alti |

Evoluzione: struttura 1 (un ISP globale) → 2 (più ISP globali) → 3 (gerarchia) → 4 (+ PoP, multi-homing, peering, IXP) → 5 (+ content provider) = Internet odierna.

## Collegamenti

- **Concetti correlati**: [[Reti di Accesso]] · [[BGP]] · [[Commutazione di Pacchetto]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[01 - TLC - Reti di calcolatori e Internet#Una rete di reti|Capitolo 1 — Una rete di reti]]
