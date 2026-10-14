---
title: Reti Cellulari 3G e 4G
tags:
  - telecomunicazioni
  - concetto
  - cellulare
  - lte
---

# Reti Cellulari 3G e 4G

> [!summary] In breve
> Il **3G** (UMTS) aggiunge al nucleo voce un nucleo dati GPRS in parallelo (**SGSN**, **GGSN**) e usa WCDMA nell'accesso radio (**RNC**, Node B). Il **4G LTE** ha un nucleo **all-IP** (EPC) con eNodeB, P-GW, S-GW, MME e HSS, e usa OFDM con slot da 0,5 ms.

| 3G | Ruolo |
| --- | --- |
| RNC / Node B | accesso radio, verso MSC (voce) e SGSN (dati) |
| SGSN | consegna i datagrammi ai mobili, mobilità |
| GGSN | gateway verso Internet, nasconde la mobilità |

| 4G | Ruolo |
| --- | --- |
| eNodeB | stazione base; tunneling dei datagrammi verso il P-GW con QoS |
| P-GW | IP agli UE, QoS, gateway |
| S-GW | appoggio della mobilità nel piano dei dati, fatturazione |
| MME | connessione e mobilità |
| HSS | profilo, roaming, autenticazione |

- 4G: voce e dati in IP; piano dati e di controllo separati; 100/50 Mbps su 20 MHz; MIMO; scheduling opportunistico.
- GPRS = General **Packet** Radio Service (il libro scrive "Generalized Racket").

## Collegamenti

- **Concetti correlati**: [[Rete Cellulare GSM]] · [[CDMA]] · [[Protocollo IPv6]] · [[Inoltro e Instradamento]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[07 - TLC - Reti mobili e wireless#Rete dati cellulare 3G|Capitolo 7 — Rete dati cellulare 3G]]
> - [[07 - TLC - Reti mobili e wireless#Verso il 4G: LTE|Capitolo 7 — Verso il 4G: LTE]]
