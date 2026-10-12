---
title: Autenticazione e Controllo degli Accessi
tags:
  - sistemi-di-calcolo-2
  - concetto
  - sicurezza
---

# Autenticazione e Controllo degli Accessi

> [!summary] In breve
> Autenticazione: qualcosa che sai (password con salt e hash lento), che hai (memory card, smart card), che sei (biometria). Controllo degli accessi: DAC, MAC, RBAC, matrice di controllo degli accessi.

- Il **salt** nasconde le password uguali, rende difficili gli attacchi a dizionario offline e il riuso tra sistemi. Hash lenti: crypt(3) (DES), MD5, **bcrypt**.
- Smart card: protocolli statici, password dinamiche, challenge-response.
- Biometria: l'iride è la più accurata e costosa.
- **DAC** (decide il proprietario, es. i permessi Unix), **MAC** (etichette e clearance), **RBAC** (diritti ai ruoli, utenti ai ruoli).

## Collegamenti

- **Concetti correlati**: [[Triade CIA]] · [[Permessi e Ownership]] · [[Crittografia Simmetrica e Asimmetrica]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[10 - SDC2 - Sicurezza#Autenticazione|Lezione 10 — Autenticazione]]
> - [[10 - SDC2 - Sicurezza#Password con hash e salt|Lezione 10 — Password con hash e salt]]
> - [[10 - SDC2 - Sicurezza#Token|Lezione 10 — Token]]
> - [[10 - SDC2 - Sicurezza#Biometria|Lezione 10 — Biometria]]
> - [[10 - SDC2 - Sicurezza#Controllo degli accessi|Lezione 10 — Controllo degli accessi]]
> - [[10 - SDC2 - Sicurezza#RBAC|Lezione 10 — RBAC]]
