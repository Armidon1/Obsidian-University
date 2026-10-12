---
title: PWM
tags:
  - sistemi-operativi
  - concetto
  - avr
  - timer
---

# PWM

> [!summary] In breve
> Pulse Width Modulation: un'onda quadra di cui si varia il duty cycle; la media nel periodo simula un valore analogico tra 0 e 5V.

- **Duty cycle**: frazione del periodo in cui il segnale è alto. Media = duty × 5V (es. 25% → 1.25V).
- Si genera con un timer e un OCR collegato a un pin: il pin cambia stato quando `TCNT` raggiunge `OCR`.
- Esempio: timer 1 in Fast PWM a 8 bit, OC1C = PB7 (il LED); `OCR1CL` viene incrementato periodicamente e il LED "respira".
- In modalità invertente, un OCR più alto dà un duty cycle più basso, quindi meno luce.
- `analogWrite` di Arduino fa esattamente questo.

## Collegamenti

- **Concetti correlati**: [[Timer AVR]] · [[Porte Digitali AVR]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#PWM|Lezione 4 — PWM]]
> - [[04 - SO - Hardware e AVR#Esempio: LED che "respira"|Lezione 4 — Esempio: LED che "respira"]]
