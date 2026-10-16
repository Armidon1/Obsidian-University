---
title: Problema della fermata
tags:
  - modelli-di-calcolo
  - concetto
  - calcolabilita
  - indecidibilita
---

# Problema della fermata

> [!summary] In breve
> Dato un programma $S$ e un input $x$, stabilire se $S$ termina su $x$. È **indecidibile** ma **semi-decidibile**.

Prova per assurdo (diagonalizzazione): se esistesse `itHalts(S, x)`,

```c
void diag(char *s) {
   if(itHalts(s, s)) while(1);   /* se s termina, cicla */
   else return;                  /* se s non termina, termina */
}
```

`diag(s_diag)` terminerebbe se e solo se non termina.

- **Semi-decidibile**: si simula $S$ su $x$ (macchina universale) e si risponde sì se termina.
- Il complemento (*$S$ va in loop su $x$?*) non è nemmeno semi-decidibile.
- Per riduzione: se HP $\le B$, anche $B$ è indecidibile.

## Collegamenti

- **Concetti correlati**: [[Diagonalizzazione di Cantor]] · [[Linguaggio semidecidibile]] · [[Macchina di Turing universale]] · [[Riduzione tra linguaggi]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[07 - MC - Halting Problem#Definizione dell'Halting Problem|Lezione 7 — Definizione dell'Halting Problem]]
> - [[07 - MC - Halting Problem#Costruzione della contraddizione|Lezione 7 — Costruzione della contraddizione]]
> - [[07 - MC - Halting Problem#Semi-decidibilità|Lezione 7 — Semi-decidibilità]]
> - [[08 - MC - Macchine di Turing e calcolabilità#L'indecidibilità della terminazione|Lezione 8 — L'indecidibilità della terminazione]]
