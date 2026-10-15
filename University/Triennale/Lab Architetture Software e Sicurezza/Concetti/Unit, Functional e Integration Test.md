---
title: Unit, Functional e Integration Test
tags:
  - lab-architetture-software-sicurezza
  - concetto
  - testing
---

# Unit, Functional e Integration Test

> [!summary] In breve
> Unit test su un metodo o classe (veloci, molti mock), functional su pochi metodi o classi (es. controller), integration/system su tutto il sistema (lenti, testano le interfacce).

| Tipo | Esempio | Velocità | Copertura | Mock | Interfacce |
|---|---|---|---|---|---|
| Unit | spec del model | alta | alta | molti | no |
| Functional | spec del controller | media | media | alcuni | parziale |
| Integration | scenari Cucumber | bassa | bassa | pochi | sì |

L'acceptance test (cliente soddisfatto) non coincide con l'integration test (moduli coerenti).

## Collegamenti

- **Concetti correlati**: [[Mock e Stub]] · [[Code Coverage]] · [[Outside-in Testing]]
- **Mappa**: [[MOC - Lab Architetture Software e Sicurezza]]

> [!info] Approfondimento
> - [[15 - LASS - Testing BDD e TDD#Unit vs. Functional test nelle app SaaS|Lezione 15 — Unit vs. Functional test nelle app SaaS]]
> - [[15 - LASS - Testing BDD e TDD#Che tipi di test?|Lezione 15 — Che tipi di test?]]
> - [[15 - LASS - Testing BDD e TDD#Testing stacks|Lezione 15 — Testing stacks]]
