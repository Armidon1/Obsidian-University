---
title: Timer AVR
tags:
  - sistemi-operativi
  - concetto
  - avr
  - timer
---

# Timer AVR

> [!summary] In breve
> Contatore hardware (TCNTn) che avanza a una frequenza clock/prescaler; quando eguaglia un output compare register (OCRn) genera un evento (interrupt o cambio di un pin).

- ATmega2560: T/C 0 e 2 a **8 bit**, T/C 1, 3, 4, 5 a **16 bit**.
- Registri: `TCNTn` (contatore), `TCCRnA/B/C` (modalità e prescaler), `OCRnA/B/C` (compare), `TIMSKn` (abilitazione degli interrupt).
- Prescaler: 1, 8, 64, 256, 1024.

$$OCR = T \cdot \frac{f_{clock}}{prescaler}$$

Esempio: 16 MHz / 1024 = 15625 count/s, quindi 100 ms corrispondono a 1562.5 (con un errore di quantizzazione).

- Interrupt periodico: modalità CTC (`WGMn2`), `OCRnA = ocrval`, `TIMSKn |= 1<<OCIEnA`, `ISR(TIMERn_COMPA_vect)`.
- È il "battito" su cui si basa il **preemptive multitasking**.

## Collegamenti

- **Concetti correlati**: [[PWM]] · [[Interrupt]] · [[Preemptive Multitasking su AVR]] · [[Polling vs Interrupt]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[04 - SO - Hardware e AVR#Timer|Lezione 4 — Timer]]
> - [[04 - SO - Hardware e AVR#Prescaler|Lezione 4 — Prescaler]]
> - [[04 - SO - Hardware e AVR#Calcolare il valore di OCR|Lezione 4 — Calcolare il valore di OCR]]
> - [[04 - SO - Hardware e AVR#Interrupt da timer|Lezione 4 — Interrupt da timer]]
