---
title: Sistemi di Rilevamento delle Intrusioni
tags:
  - telecomunicazioni
  - concetto
  - ids
  - sicurezza
---

# Sistemi di Rilevamento delle Intrusioni

> [!summary] In breve
> Un **IDS** fa **deep packet inspection** (intestazioni e payload) e genera allarmi sul traffico sospetto; un **IPS** lo blocca. I rilevatori sono basati sulle **firme** (attacchi noti) o sulle **anomalie** (deviazioni dal traffico normale). **Snort** è l'IDS open source più diffuso.

- Più **sensori** coordinati; rete interna ad alta sicurezza + **DMZ** (web, FTP, DNS) a bassa sicurezza.

| Firme | Anomalie |
| --- | --- |
| precise sugli attacchi noti | rilevano anche attacchi nuovi |
| cieche ai nuovi, falsi allarmi | difficile definire il "normale" |

Firma Snort contro i ping di nmap:
```text
alert icmp $EXTERNAL_NET any -> $HOME_NET any
(msg:"ICMP PING NMAP"; dsize: 0; itype: 8;)
```

## Collegamenti

- **Concetti correlati**: [[Filtri di Pacchetti e Gateway Applicativi]] · [[IDS]] · [[DMZ]] · [[Protocollo ICMP]] · [[Attacchi alle Reti]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#Sistemi di rilevamento delle intrusioni|Capitolo 8 — Sistemi di rilevamento delle intrusioni]]
> - [[08 - TLC - Sicurezza nelle reti#Snort|Capitolo 8 — Snort]]
