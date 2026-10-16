---
title: Logaritmo
tags:
  - analisi-1
  - concetto
  - funzioni-elementari
---

# Logaritmo

> [!summary] In breve
> log_a(y) è l'unico x con a^x = y (0 < a ≠ 1, y > 0); esiste per il teorema dei valori intermedi. Trasforma prodotti in somme; ln'(x) = 1/x.

$$\log_a(y) = \frac{\ln y}{\ln a}, \qquad \ln(x) = \int_1^x \frac{ds}{s}$$

- $\log_a(xy) = \log_a x + \log_a y$, $\log_a(x^r) = r\log_a x$, $\log_a 1 = 0$.
- Continuo (inversa di una funzione continua strettamente monotona).
- $\ln'(x) = \frac1x$, $\int \frac1x\,dx = \ln|x| + c$.
- Cresce più lentamente di ogni potenza: $\frac{\ln x}{x^\alpha} \to 0$; $x^\alpha \ln x \to 0$ per $x \to 0^+$.
- $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} + o(x^3)$.

## Collegamenti

- **Concetti correlati**: [[Funzione esponenziale]] · [[Teorema dei valori intermedi]] · [[Funzione inversa]] · [[Gerarchia degli infiniti]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[04 - AN1 - Funzioni Continue#Logaritmi|Lezione 4 — Logaritmi]]
> - [[05 - AN1 - Calcolo Differenziale#Derivazione delle funzioni inverse|Lezione 5 — Derivazione delle funzioni inverse]]
> - [[06 - AN1 - Calcolo Integrale#Primi integrali|Lezione 6 — Primi integrali]]
