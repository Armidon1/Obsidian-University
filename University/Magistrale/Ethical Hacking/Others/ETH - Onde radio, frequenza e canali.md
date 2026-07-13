---
tags: [ethl, wireless, radio, spettro-em, frequenza, canali, concetto, fisica]
tipo: concetto
data: 2026-07-13
collegamenti: ["[[ETHL - Cap 8 Wireless Hacking]]"]
---

# ETH — Onde radio, frequenza e canali

> [!abstract] Il filo
> Tre domande in fila. **Cosa oscilla** davvero in un'onda radio? Non la materia, ma il campo elettromagnetico. **Cosa significa «2.4 GHz»?** Quante volte al secondo il campo oscilla, legato per sempre alla lunghezza d'onda dalla relazione $\lambda = c/f$. **Da dove nascono i «canali»?** Sono fette di una banda, e sono *larghe* perché devono trasportare dati. L'ultimo punto chiude il cerchio con la regola 1/6/11 del [[ETHL - Cap 8 Wireless Hacking]]: la frequenza dice *dove* sei sullo spettro, la larghezza dice *quanto spazio occupi*, ed è la larghezza a causare la sovrapposizione.

## Cos'è un'onda elettromagnetica

Un'onda radio è la stessa cosa fisica della luce: un'onda elettromagnetica. La differenza rispetto a un'onda del mare o al suono è decisiva — qui non oscilla nessuna materia. Nel suono è l'aria che si comprime e si dilata; in un'onda radio non c'è nulla che sale e scende fisicamente. Quello che oscilla è il **campo elettromagnetico**: in ogni punto dello spazio esistono un campo elettrico e un campo magnetico (perpendicolari fra loro), e al passaggio dell'onda la loro intensità cresce, torna a zero, si inverte, ricresce dall'altra parte, e così via. Questa oscillazione si autosostiene e si propaga in avanti.

Due conseguenze da tenere fisse. Primo: non serve un mezzo, quindi un'onda radio (come la luce del Sole) attraversa anche il vuoto. Secondo: viaggia a una sola velocità, quella della luce, $c \approx 3 \times 10^{8}$ m/s. Quando disegni una sinusoide per rappresentarla, l'altezza della curva **non è una posizione nello spazio**: è l'intensità e il verso del campo elettrico in quel punto e in quell'istante. Il «+» in alto e il «−» in basso sono il campo che punta in un verso o nell'altro; lo zero è il campo nullo. È un valore di campo che cicla, non un oggetto che rimbalza su e giù.

## Le grandezze che descrivono l'onda

Poche grandezze bastano a definire completamente un'onda. La **frequenza** $f$ è quante oscillazioni complete avvengono in un secondo, misurata in hertz (Hz). Il **periodo** $T$ è la durata di un singolo ciclo, ed è l'inverso della frequenza. La **lunghezza d'onda** $\lambda$ è la distanza che l'onda percorre nello spazio durante un ciclo completo. L'**ampiezza** è il valore massimo dell'intensità del campo, ed è ciò che si lega alla potenza del segnale. La **fase** dice a che punto del ciclo ti trovi in un dato istante.

La relazione che tiene insieme tutto è

$$\lambda = \frac{c}{f} \qquad\qquad T = \frac{1}{f}$$

Siccome $c$ è fisso, frequenza e lunghezza d'onda sono legate in modo rigido e inverso: alza la frequenza e la lunghezza d'onda si accorcia, e viceversa.

| Grandezza | Simbolo | Cosa misura | Relazione |
|---|---|---|---|
| Frequenza | $f$ | oscillazioni al secondo (Hz) | $f = 1/T$ |
| Periodo | $T$ | durata di un ciclo (s) | $T = 1/f$ |
| Lunghezza d'onda | $\lambda$ | lunghezza spaziale di un ciclo (m) | $\lambda = c/f$ |
| Ampiezza | $A$ | intensità massima del campo | $\propto$ potenza |
| Fase | $\varphi$ | punto del ciclo in un istante | — |

## 2.4 GHz, concretamente

«2.4 GHz» vuol dire $2{,}4 \times 10^{9}$ cicli al secondo: al tuo router il campo elettrico si inverte avanti e indietro 2,4 **miliardi** di volte ogni secondo — un tremolio velocissimo e impossibile da percepire direttamente. Il modo per renderlo tangibile è la lunghezza d'onda:

$$\lambda = \frac{c}{f} = \frac{3 \times 10^{8}\ \text{m/s}}{2{,}4 \times 10^{9}\ \text{Hz}} \approx 0{,}125\ \text{m} = 12{,}5\ \text{cm}$$

Un'onda intera di Wi-Fi 2.4 GHz è lunga circa 12,5 cm nello spazio: il pattern si ripete ogni 12,5 cm mentre l'onda vola. A 5 GHz scende a ~6 cm.

> [!tip] Ancora concreta
> La lunghezza d'onda spiega perché le antenne Wi-Fi sono lunghe pochi centimetri: si dimensionano a frazioni di $\lambda$ (tipicamente un quarto d'onda, ~3,1 cm a 2.4 GHz, o mezza, ~6,25 cm). L'antenna «risuona» meglio quando la sua lunghezza è in rapporto semplice con la lunghezza d'onda che deve ricevere o trasmettere.

## Dove sta nello spettro

Mettendo tutte le onde elettromagnetiche in fila per frequenza crescente, il Wi-Fi vive nella regione delle **microonde**, tra le onde radio classiche e la luce. Molto sotto ci sono la radio AM e FM; molto sopra, la luce visibile.

| Sorgente | Frequenza (circa) | Lunghezza d'onda (circa) |
|---|---|---|
| Radio AM | ~1 MHz | ~300 m |
| Radio FM | ~100 MHz | ~3 m |
| Wi-Fi 2.4 GHz | 2,4 GHz | ~12,5 cm |
| Forno a microonde | 2,45 GHz | ~12 cm |
| Wi-Fi 5 GHz | 5 GHz | ~6 cm |
| Luce visibile | ~500 THz | ~500–600 nm |

> [!example] Vicino al microonde
> Il forno a microonde lavora a ~2,45 GHz, praticamente sul Wi-Fi: è una frequenza a cui le molecole d'acqua assorbono bene energia e si scaldano. Stesso quartiere dello spettro, uso opposto — ed è anche il motivo per cui un microonde acceso può disturbare il Wi-Fi a 2.4 GHz.

Il confronto **2.4 vs 5 GHz** discende direttamente dalla fisica. A 5 GHz la lunghezza d'onda è più corta e l'attenuazione è maggiore, soprattutto attraversando muri e materiali ricchi d'acqua: la portata cala. In compenso a 5 GHz c'è molto più spettro disponibile e molti più canali non sovrapposti, quindi più banda e prestazioni migliori negli ambienti affollati. È il classico compromesso copertura-contro-capacità.

## Dalla banda al canale

Quel «2.4 GHz» non è una frequenza esatta: è una **banda**, cioè un intervallo. Nel caso del Wi-Fi è la banda ISM (Industrial, Scientific, Medical) non licenziata, che va da ~2400 a ~2483,5 MHz — poco più di 80 MHz di spettro. Un **canale** è una fetta di quella banda: una frequenza centrale precisa dove un apparecchio parcheggia il suo segnale. È la stessa logica delle stazioni FM (88.5, 92.3, 100.1…), frequenze diverse scelte per non pestarsi a vicenda. Nel Wi-Fi a 2.4 GHz il canale 1 è centrato a 2412 MHz, il 6 a 2437, l'11 a 2462, con i numeri di canale spaziati di 5 MHz l'uno dall'altro.

## Perché i canali hanno una larghezza

Qui sta il punto che spiega tutto il resto. Un canale non è una riga infinitamente sottile su una frequenza esatta: occupa una **larghezza** di frequenze attorno al suo centro (~20–22 MHz nel Wi-Fi classico).

> [!info] Larghezza e dati
> Un tono perfettamente stabile a frequenza singola non trasporta alcuna informazione — è sempre uguale a sé stesso. Per codificare dei bit devi **modulare** l'onda, cioè variarne ampiezza, frequenza o fase nel tempo. Ma ogni variazione «spalma» inevitabilmente il segnale su un intervallo di frequenze attorno alla portante: più bit al secondo vuoi trasmettere, più largo diventa quell'intervallo. È l'essenza dell'analisi di Fourier e del limite di Shannon, ed è il senso letterale del termine *banda larga* (bandwidth = larghezza di banda).

Il Wi-Fi porta questa idea all'estremo con **OFDM**: il canale da 20 MHz viene suddiviso in decine di sottoportanti ravvicinate (nel caso base ~52 sottoportanti spaziate 312,5 kHz), ciascuna modulata piano e in parallelo. Insieme trasportano molti dati restando robuste al rumore e agli echi. Il risultato è che ogni canale «pesa» circa 20–22 MHz di spettro, non un valore singolo.

## Sovrapposizione e la terna 1/6/11

Adesso il conto torna. I numeri di canale sono spaziati di 5 MHz, ma ogni canale è largo ~22 MHz: la larghezza supera di molto la spaziatura, quindi canali con numeri vicini si accavallano quasi del tutto (il canale 1 e il 2 sono praticamente sovrapposti). Perché due canali *non* si sovrappongano servono centri distanti almeno ~22 MHz, cioè circa 5 numeri di canale. Da qui la terna **1, 6, 11**, spaziata di 25 MHz: sono le uniche tre fette che stanno affiancate senza toccarsi negli ~83 MHz della banda 2.4 GHz.

Attenzione a una distinzione fine sull'interferenza. Due AP sullo **stesso** canale si «sentono» a vicenda e si alternano educatamente via CSMA/CA: condivisione ordinata, degradata ma pulita. Due AP su canali **diversi ma sovrapposti** (es. 1 e 3) non riescono a decodificarsi, quindi non si coordinano affatto: si limitano ad alzarsi il rumore di fondo, con frame corrotti e ritrasmissioni — spesso *peggio* dello stesso canale. A **5 GHz** il problema quasi sparisce: la canalizzazione è progettata già non sovrapposta (ogni canale da 20 MHz nel suo slot separato) e i canali sono molti di più.

> [!question] Domanda d'esame
> «Perché a 2.4 GHz solo i canali 1, 6 e 11 non si sovrappongono?» → Perché la larghezza reale di un canale (~22 MHz) è molto maggiore della spaziatura fra i numeri di canale (5 MHz); servono circa 5 numeri di distanza perché due fette non si accavallino, e nella banda di soli ~83 MHz ci stanno appena tre fette pulite: 1, 6, 11.

## Perché conta per l'ethical hacking

Questa base fisica non è ornamentale, regge diversi punti del capitolo wireless. La radio ascolta **un canale alla volta**, e i canali vanno campionati singolarmente anche se si sovrappongono: per questo i tool di discovery e cattura (airodump-ng, Kismet) fanno **channel hopping**, saltando di canale in canale per coprire tutta la banda. La **monitor mode** è ciò che permette alla scheda di ricevere i frame 802.11 grezzi su un dato canale. Le **antenne direzionali** (Yagi, cantenna) concentrano l'energia in una direzione e allungano la portata — è la fisica che rende possibile lo sniffing dal parcheggio (wardriving). E la lunghezza d'onda, con l'attenuazione che cresce alla frequenza, spiega quanta portata e quanta penetrazione nei muri ci si può aspettare.

> [!summary] In una riga
> Un'onda radio è il campo elettromagnetico che oscilla $f$ volte al secondo e si ripete ogni $\lambda = c/f$ metri nello spazio; la banda 2.4 GHz è un intervallo di frequenze, i canali sono fette centrate a frequenze precise, larghe ~22 MHz perché trasportano dati — e da quella larghezza nascono la sovrapposizione e la terna 1/6/11.

> [!tip] Candidati Excalidraw
> Due schizzi «con un movimento» da ridisegnare a mano: la **sinusoide** con $f$ e $\lambda$ marcate (alzando la frequenza l'onda si stringe e $\lambda$ si accorcia); e la **scala dello spettro EM** (AM → FM → Wi-Fi → microonde → luce) con 2.4 e 5 GHz evidenziati. Grezzi, timer 3–4 minuti.
