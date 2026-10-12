---
title: Botnet e DDoS
tags:
  - sistemi-di-calcolo-2
  - concetto
  - sicurezza
  - reti
---

# Botnet e DDoS

> [!summary] In breve
> Una botnet è un insieme di macchine compromesse controllate da remoto; serve soprattutto per DDoS. Il DoS esaurisce le risorse della vittima (flood ICMP/UDP/SYN, SYN spoofing).

- Botnet: funzionalità del bot + controllo remoto + meccanismo di diffusione (scanning casuale, hit list, topologico, sottorete locale).
- **SYN spoofing**: molti SYN con IP falsi riempiono la tabella delle connessioni mezze aperte.
- DDoS: attaccante → handler zombie → agent zombie → bersaglio.
- Difese: bloccare gli IP falsificati vicino alla sorgente, rate limiting, **SYN cookie**, puzzle/CAPTCHA, server replicati, piano di risposta con l'ISP.

## Collegamenti

- **Concetti correlati**: [[Malware]] · [[TCP e UDP]] · [[Attacchi Passivi e Attivi]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[10 - SDC2 - Sicurezza#Botnet|Lezione 10 — Botnet]]
> - [[10 - SDC2 - Sicurezza#Denial of Service|Lezione 10 — Denial of Service]]
> - [[10 - SDC2 - Sicurezza#DDoS|Lezione 10 — DDoS]]
> - [[10 - SDC2 - Sicurezza#Difese contro il DoS|Lezione 10 — Difese contro il DoS]]
