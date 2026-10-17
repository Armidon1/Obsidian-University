---
title: "Poli dominanti e vincoli sul transitorio"
aliases:
  - "CA — Poli dominanti e vincoli sul transitorio"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "129-134"
class_label: "Blocco in ordine di dispensa; data non assegnata"
---

# Poli dominanti e vincoli sul transitorio

> [!abstract]
> Questa lezione sviluppa poli dominanti e vincoli sul transitorio seguendo il blocco delle pagine 129–134 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Prima:** [[16 - CA - Esercizi di sintesi sul luogo delle radici]]. **Dopo:** [[18 - CA - Assegnazione diretta dei poli con retroazione dinamica]].

## Tradurre tempo e smorzamento in geometria

Vedi [[CA - Poli dominanti]] · [[CA - Settori di smorzamento]].

Un polo $s=-\sigma+j\omega_d$ ha velocità di decadimento $\sigma>0$, pulsazione naturale $\omega_n=\sqrt{\sigma^2+\omega_d^2}$ e smorzamento $\zeta=\sigma/\omega_n$. I vincoli sul tempo di assestamento delimitano semipiani a sinistra di una verticale, quelli su $\zeta$ delimitano settori.

Le formule del secondo ordine descrivono bene l'uscita soltanto se gli altri poli sono abbastanza più veloci e gli zeri non alterano la dinamica dominante. Un polo molto a sinistra può avere un residuo grande; la sola distanza geometrica è una guida, non una garanzia sufficiente.

Nel progetto si disegna prima la regione ammissibile, poi si verifica se il luogo la attraversa. Scegliere il guadagno «più grande possibile» può allontanare la coppia dal settore di smorzamento anche se il sistema resta stabile.

_(Dispensa commentata, pagine PDF 129–131; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 129
> ![[CA-p129-1.jpg]]
> Il vincolo di transitorio viene tradotto in una verticale e in un settore del piano dei poli, da sovrapporre al luogo.

> [!example]- Materiale originale — pagina PDF 130
> ![[CA-p130-1.jpg]]
> I punti scelti sul luogo determinano il guadagno soltanto dopo aver soddisfatto la condizione di fase e la regione richiesta.

> [!example]- Materiale originale — pagina PDF 131
> ![[CA-p131-1.jpg]]
> L'esercizio confronta la posizione dei poli e il polinomio risultante, distinguendo rapidità e smorzamento.

## Confronto fra approcci e casi speciali

Vedi [[CA - Progetto in frequenza e sul luogo]] · [[CA - Zeri non a fase minima]] · [[CA - Vincoli strutturali]].

Il progetto in frequenza agisce sulla forma dell'anello vicino all'attraversamento; il luogo mostra direttamente la posizione dei poli chiusi. Si tratta di due rappresentazioni dello stesso problema e la soluzione deve soddisfare entrambe.

Gli zeri del processo non si possono spostare con una semplice retroazione esterna: influenzano la risposta e vincolano la possibilità di assegnare un trasferimento chiuso desiderato. Uno zero nel semipiano destro non va cancellato con un polo instabile del controllore per simulare una dinamica ideale.

> [!tip] Controllo di consistenza
> Dopo la scelta di $k$, calcolare $T=GP/(1+GP)$ e il suo polinomio completo, controllare i poli interni, verificare l'errore, poi confrontare il gradino previsto con i vincoli. Un luogo qualitativo non mostra da solo ampiezza del comando o sensibilità al rumore.

_(Dispensa commentata, pagine PDF 132–134; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 132
> ![[CA-p132-1.jpg]]
> I vincoli del processo, in particolare gli zeri, limitano i trasferimenti chiusi ottenibili senza cancellazioni problematiche.

> [!example]- Materiale originale — pagina PDF 133
> ![[CA-p133-1.jpg]]
> L'esempio confronta il guadagno statico e il luogo: una soluzione stabile può restare incompatibile con l'inseguimento desiderato.

> [!example]- Materiale originale — pagina PDF 134
> ![[CA-p134-1.jpg]]
> La verifica finale controlla l'intervallo AS dopo la compensazione e richiama i limiti dei metodi approssimati.
