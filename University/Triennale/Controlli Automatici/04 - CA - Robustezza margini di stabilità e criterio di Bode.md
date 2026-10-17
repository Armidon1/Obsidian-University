---
title: "Robustezza margini di stabilità e criterio di Bode"
aliases:
  - "CA — Robustezza margini di stabilità e criterio di Bode"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "39-43"
class_label: "Blocco in ordine di dispensa; data non assegnata"
---

# Robustezza margini di stabilità e criterio di Bode

> [!abstract]
> Questa lezione sviluppa robustezza margini di stabilità e criterio di bode seguendo il blocco delle pagine 39–43 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Prima:** [[03 - CA - Retroazione e stabilità al variare del guadagno]]. **Dopo:** [[05 - CA - Introduzione al controllo e modelli fisici]].

## Perché misurare la distanza dall’instabilità

Vedi [[CA - Robustezza]] · [[CA - Margine di guadagno]].

Un progetto non deve essere stabile solo per i parametri nominali: attrito, carico e ritardi cambiano. I margini misurano quanto può cambiare separatamente il guadagno o la fase prima che il diagramma di anello incontri il punto critico.

Alla pulsazione $\omega_\pi$ per cui $\arg F(j\omega_\pi)=-180^\circ$ (modulo $360^\circ$), il margine di guadagno moltiplicativo è $m_g=1/|F(j\omega_\pi)|$; in dB vale $-20\log_{10}|F(j\omega_\pi)|$. Un margine di 6.02 dB corrisponde a raddoppiare il guadagno, nelle condizioni del caso regolare.

Più intersezioni richiedono di esaminare tutte le frontiere. I margini classici non certificano perturbazioni simultanee arbitrarie di modulo e fase e non sostituiscono il conteggio di Nyquist per anelli instabili o complessi.

_(Dispensa commentata, pagine PDF 39–40; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 39
> ![[CA-p039-1.jpg]]
> La robustezza viene motivata come distanza dall'instabilità; le variazioni di guadagno e fase muovono il diagramma rispetto a meno uno.

> [!example]- Materiale originale — pagina PDF 40
> ![[CA-p040-1.jpg]]
> Il margine di guadagno si legge sull'asse reale negativo, mentre il margine di fase si riferisce all'attraversamento della circonferenza unitaria.

## Attraversamento e margine di fase

Vedi [[CA - Pulsazione di attraversamento]] · [[CA - Margine di fase]].

La pulsazione di attraversamento $\omega_c$ soddisfa $|F(j\omega_c)|=1$, ossia 0 dB. Il margine di fase è
$$m_\varphi=180^\circ+\arg F(j\omega_c),$$
usando una fase continua e coerente con l'attraversamento considerato. Per esempio, una fase di $-135^\circ$ dà $45^\circ$ di margine.

Un ritardo puro $e^{-s\tau}$ lascia invariato il modulo ma aggiunge fase $-\omega\tau$ in radianti. Nel caso con un unico attraversamento critico, una stima del ritardo aggiuntivo tollerabile è $\tau_{\max}\simeq m_\varphi[\mathrm{rad}]/\omega_c$. Per $m_\varphi=45^\circ$ e $\omega_c=10$ rad/s risulta $\tau_{\max}\simeq0.0785$ s.

Nelle figure con più attraversamenti, la lettura locale di un margine positivo può coesistere con instabilità globale. Il punto da controllare rimane sempre la curva completa.

_(Dispensa commentata, pagine PDF 41–42; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 41
> ![[CA-p041-1.jpg]]
> I disegni chiariscono la lettura del margine di fase e mostrano casi in cui attraversamenti multipli impediscono una conclusione locale immediata.

> [!example]- Materiale originale — pagina PDF 42
> ![[CA-p042-1.jpg]]
> I controesempi confrontano diagrammi con più incroci: un singolo numero di margine non sostituisce il conteggio globale degli avvolgimenti.

## Quando si può usare il criterio di Bode

Vedi [[CA - Criterio di Bode]].

Nel caso usuale di anello senza poli a parte reale positiva, guadagno di segno appropriato, andamento regolare e un solo attraversamento significativo del livello unitario, un margine di fase positivo consente di inferire la stabilità chiusa. Sono ipotesi sufficienti da controllare sul caso concreto: il solo valore $m_\varphi>0$ non è un teorema universale.

Il criterio di Bode è comodo per il progetto perché traduce la stabilità in vincoli sul guadagno e sulla fase vicino a $\omega_c$. Nyquist rimane il criterio di riferimento quando ci sono poli instabili, attraversamenti multipli o casi marginali. Richiamo: [[TDS - Margini di stabilità]].

_(Dispensa commentata, pagine PDF 43–43; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 43
> ![[CA-p043-1.jpg]]
> Il riepilogo del criterio di Bode richiama le ipotesi necessarie alla scorciatoia basata sul margine positivo.

## Esercizi collegati

[[E14 - CA - Prova completa del 12 luglio 2019]]
