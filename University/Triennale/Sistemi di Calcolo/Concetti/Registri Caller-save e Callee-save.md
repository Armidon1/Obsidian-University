---
title: Registri Caller-save e Callee-save
tags:
  - sistemi-di-calcolo
  - concetto
  - assembly
  - abi
---

# Registri Caller-save e Callee-save

> [!summary] In breve
> Caller-save: chi chiama deve salvarli se gli servono dopo la chiamata. Callee-save: la funzione chiamata deve preservarli. IA32: caller-save A, C, D; callee-save B, SI, DI, SP, BP.

| ABI | Caller-save | Callee-save |
| --- | --- | --- |
| System V i386 | EAX, ECX, EDX | EBX, ESI, EDI, ESP, EBP |
| System V AMD64 | tutti gli altri (incl. RDI, RSI, R8–R11) | RBX, RSP, RBP, R12–R15 |

- Un registro callee-save usato da una funzione si salva una volta nel prologo e si ripristina nell'epilogo.
- Per una variabile che deve sopravvivere a molte chiamate (es. il contatore di un ciclo con `call`) conviene un callee-save: il compilatore sceglie `%ebx`.

## Collegamenti

- **Concetti correlati**: [[Convenzioni di Chiamata IA32]] · [[Registri IA32]] · [[x86-64]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Registri caller-save e callee-save|Lezione 3 — Registri caller-save e callee-save]]
> - [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Estensione a x86-64|Lezione 3 — Estensione a x86-64]]
> - [[05 - SDC - Ottimizzazione dei programmi#Register allocation|Lezione 5 — Register allocation]]
