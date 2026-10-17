---
title: "Esercizi di compensazione anticipatrice e attenuatrice"
aliases:
  - "CA — Esercizi di compensazione anticipatrice e attenuatrice"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "93-97"
class_label: "24/03"
---

# Esercizi di compensazione anticipatrice e attenuatrice

> [!abstract]
> Questa lezione sviluppa esercizi di compensazione anticipatrice e attenuatrice seguendo il blocco delle pagine 93–97 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 24/03. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[09 - CA - Progetto in frequenza e reti compensatrici]]. **Dopo:** [[11 - CA - Progetto in frequenza con processi interconnessi]].

## Leggere l’anello non compensato

Vedi [[CA - Diagnosi del difetto di fase]] · [[CA - Bilancio del modulo]].

Le esercitazioni seguono lo stesso ordine della sintesi: prima precisione, poi attraversamento e margine. Dato $\omega_c^*$, si calcolano modulo e fase dell'anello iniziale $F_0(j\omega_c^*)$. La rete deve soddisfare due condizioni nello stesso punto:
$$|R(j\omega_c^*)|=\frac1{|F_0(j\omega_c^*)|},\qquad
\arg R(j\omega_c^*)=m_\varphi^*-180^\circ-\arg F_0(j\omega_c^*).$$
Queste sono richieste locali necessarie al progetto desiderato, non una certificazione globale della stabilità. Se la fase richiesta è positiva ma il modulo richiesto è inferiore a uno, una sola anticipatrice normalizzata potrebbe non bastare: occorrono più gradi di libertà o una rete mista.

Il manoscritto usa anche diagrammi universali: le ascisse sono normalizzate rispetto a una rottura o al centro della rete. Prima di trasformare la lettura in secondi, controllare quale normalizzazione è stata scelta.

_(Dispensa commentata, pagine PDF 93–94; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 93
> ![[CA-p093-1.jpg]]
> La nuova esercitazione impone errore e margine prima di scegliere la rete: leggere modulo e fase esatti alla frequenza obiettivo.

> [!example]- Materiale originale — pagina PDF 94
> ![[CA-p094-1.jpg]]
> Il dimensionamento individua il difetto di fase e il guadagno che la rete deve produrre nello stesso punto.

## Dimensionare e ricontrollare la rete

Vedi [[CA - Reti in cascata]] · [[CA - Compensazione mista]] · [[CA - Realizzabilità]].

Per una rete anticipatrice centrata in $\omega_c^*$, scegliere $\alpha$ dall'anticipo richiesto e $\tau=1/(\omega_c^*\sqrt\alpha)$. Il guadagno al centro vale $1/\sqrt\alpha$; se il bilancio non torna, si modifica il centro o si aggiunge una rete attenuatrice con rotture più basse.

> [!example] Rete con anticipo e attraversamento verificabili
> Con $\alpha=1/3$ e centro a 30 rad/s, $\tau=\sqrt3/30\simeq0.05774$ s, $\alpha\tau\simeq0.01925$ s. Zero e polo sono rispettivamente a $-17.32$ e $-51.96$ rad/s. L'anticipo al centro è $30^\circ$ e l'aumento di modulo è 4.77 dB: questi due effetti vanno usati insieme.

Non si cambiano i parametri arrotondandoli prima della verifica: anche pochi gradi possono contare se il margine iniziale è ridotto. Infine si controlla che $G$ sia proprio; una derivazione ideale richiede un filtro di alta frequenza per essere fisicamente implementabile.

_(Dispensa commentata, pagine PDF 95–97; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 95
> ![[CA-p095-1.jpg]]
> I diagrammi successivi confrontano la soluzione iniziale e quella con una compensazione ulteriore: le rotture cambiano entrambi i grafici.

> [!example]- Materiale originale — pagina PDF 96
> ![[CA-p096-1.jpg]]
> I conti mostrano la scelta di parametri normalizzati e la conversione in costanti di tempo, con una seconda rete quando la prima non basta.

> [!example]- Materiale originale — pagina PDF 97
> ![[CA-p097-1.jpg]]
> Il confronto finale dei diagrammi verifica se il margine ottenuto e l'attraversamento rispettano simultaneamente le richieste.
