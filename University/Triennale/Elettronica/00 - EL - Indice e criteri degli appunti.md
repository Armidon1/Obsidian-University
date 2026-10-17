---
title: "Indice e criteri degli appunti"
tags:
  - elettronica
  - indice
source: "pdf/Appunti di Elettronica.pdf"
---

# Elettronica — indice degli appunti

> [!abstract]
> Inizia da [[MOC - Elettronica]]: contiene le 14 lezioni e i percorsi tra le 109 schede di ripasso. Materiale originale: [[Appunti di Elettronica.pdf]].

## Copertura e convenzioni

- Fonte: **Valerio Spagnoli, Appunti di Elettronica**, PDF di 193 pagine. La pagina 1 è l’indice; le note coprono le pp. 2–193.
- Lingua: italiano; sigla del corso: **EL**. Le numerazioni sono unità di studio ricavate dal libro, non date o lezioni effettivamente tenute.
- Il capitolo MOSFET è diviso in tre note consecutive per dispositivo, polarizzazione e amplificatori.
- Le note sono una rielaborazione didattica: spiegano i modelli e i passaggi senza riprodurre parola per parola la dispensa. Gli esempi mantengono i dati del sorgente; le approssimazioni sono dichiarate.
- Le formule nelle note usano LaTeX; gli schemi e i grafici provengono dal PDF. Le tabelle sono trascritte in Markdown.
- La convenzione MOS è $K=\mu C_{ox}(W/L)/2$: le correnti di triodo contengono quindi il fattore 2 davanti al termine lineare.

## Figure e qualità del sorgente

Sono incluse **413 immagini** didattiche, distribuite nelle sezioni e seguite da spiegazioni. Delle 432 risorse raster estratte, 19 sono state escluse prima dell’inserimento: tabelle già trascritte, frammenti di unità, barre dell’applicazione e maschere di annotazione. Le figure con schemi e tabelle nello stesso riquadro sono conservate e le tabelle rilevanti sono anche trascritte.

Le immagini mantengono le scritte del sorgente, anche quando contengono un errore: in quel caso vale la correzione esplicita nel testo. Una scritta sul ritaglio Thévenin di p. 13 è parzialmente tagliata già nel PDF. Gli svolgimenti manoscritti di pp. 14 e 16 restano consultabili nelle immagini.

Sono mantenuti i duplicati esatti già presenti nel materiale, per conservarne la collocazione:

- EL-p003-2.png (p. 3), EL-p035-2.png (p. 35).
- EL-p013-1.png (p. 13), EL-p013-4.png (p. 13).
- EL-p015-1.png (p. 15), EL-p015-2.png (p. 15), EL-p015-3.png (p. 15), EL-p015-4.png (p. 15).
- EL-p022-1.png (p. 22), EL-p023-3.png (p. 23).
- EL-p037-1.png (p. 37), EL-p038-1.png (p. 38), EL-p040-5.png (p. 40).
- EL-p037-2.png (p. 37), EL-p039-1.png (p. 39), EL-p040-8.png (p. 40).
- EL-p041-2.png (p. 41), EL-p042-1.png (p. 42).
- EL-p054-1.png (p. 54), EL-p054-2.png (p. 54).
- EL-p062-1.png (p. 62), EL-p062-2.png (p. 62).
- EL-p157-1.png (p. 157), EL-p173-1.png (p. 173).
- EL-p157-3.png (p. 157), EL-p163-1.png (p. 163).
- EL-p158-1.png (p. 158), EL-p163-2.png (p. 163).

## Correzioni da ricordare

- **Introduzione e segnali**: [[01 - EL - Introduzione e segnali#Integrazione e capacità parassite|Integrazione e capacità parassite]].
- **Richiami di teoria dei circuiti**: [[02 - EL - Richiami di teoria dei circuiti#Thévenin, Norton e sovrapposizione|Thévenin, Norton e sovrapposizione]]; [[02 - EL - Richiami di teoria dei circuiti#Transitori RC e metodo asintotico|Transitori RC e metodo asintotico]]; [[02 - EL - Richiami di teoria dei circuiti#Carica con un generatore di corrente|Carica con un generatore di corrente]].
- **Amplificatori**: [[04 - EL - Amplificatori#Banda passante e accoppiamento|Banda passante e accoppiamento]].
- **Reti STC e risposta nel tempo**: [[05 - EL - Reti STC e risposta nel tempo#Passa-alto del primo ordine|Passa-alto del primo ordine]]; [[05 - EL - Reti STC e risposta nel tempo#Gradini e impulsi rettangolari|Gradini e impulsi rettangolari]]; [[05 - EL - Reti STC e risposta nel tempo#Esempio di amplificatore a transconduttanza|Esempio di amplificatore a transconduttanza]].
- **Retroazione**: [[06 - EL - Retroazione#Anello e guadagno retroazionato|Anello e guadagno retroazionato]]; [[06 - EL - Retroazione#Sensibilità e prodotto guadagno-banda|Sensibilità e prodotto guadagno-banda]].
- **Amplificatori operazionali**: [[07 - EL - Amplificatori operazionali#Modello ideale e cortocircuito virtuale|Modello ideale e cortocircuito virtuale]]; [[07 - EL - Amplificatori operazionali#Esercizi resistivi e verifica della saturazione|Esercizi resistivi e verifica della saturazione]]; [[07 - EL - Amplificatori operazionali#Integratore di Miller|Integratore di Miller]]; [[07 - EL - Amplificatori operazionali#Esercizio con integratore e corrente ripartita|Esercizio con integratore e corrente ripartita]]; [[07 - EL - Amplificatori operazionali#Amplificatore differenziale e strumentazione|Amplificatore differenziale e strumentazione]]; [[07 - EL - Amplificatori operazionali#Esercizio con riferimento e filtro di ingresso|Esercizio con riferimento e filtro di ingresso]].
- **Multivibratori e generatori di forme d’onda**: [[08 - EL - Multivibratori e generatori di forme d’onda#Schmitt non invertente e attraversamenti dello zero|Schmitt non invertente e attraversamenti dello zero]]; [[08 - EL - Multivibratori e generatori di forme d’onda#Monostabile e durata dell’impulso|Monostabile e durata dell’impulso]].
- **Semiconduttori e diodi**: [[09 - EL - Semiconduttori e diodi#Bande di energia e drogaggio|Bande di energia e drogaggio]]; [[09 - EL - Semiconduttori e diodi#Polarizzazione e legge di Shockley|Polarizzazione e legge di Shockley]]; [[09 - EL - Semiconduttori e diodi#Breakdown e stabilizzazione|Breakdown e stabilizzazione]]; [[09 - EL - Semiconduttori e diodi#Termometria, fotodiodi e celle solari|Termometria, fotodiodi e celle solari]]; [[09 - EL - Semiconduttori e diodi#Retta di carico e modelli del diodo|Retta di carico e modelli del diodo]].
- **MOSFET - Struttura e regioni di funzionamento**: [[10 - EL - MOSFET - Struttura e regioni di funzionamento#Triodo, pinch-off e saturazione|Triodo, pinch-off e saturazione]]; [[10 - EL - MOSFET - Struttura e regioni di funzionamento#Leggi di corrente e convenzione per K|Leggi di corrente e convenzione per K]].
- **MOSFET - Polarizzazione e specchi di corrente**: [[11 - EL - MOSFET - Polarizzazione e specchi di corrente#Specchio di corrente|Specchio di corrente]]; [[11 - EL - MOSFET - Polarizzazione e specchi di corrente#Esempio con due transistor accoppiati in continua|Esempio con due transistor accoppiati in continua]].
- **MOSFET - Piccolo segnale e carichi attivi**: [[12 - EL - MOSFET - Piccolo segnale e carichi attivi#Linearizzazione e transconduttanza|Linearizzazione e transconduttanza]]; [[12 - EL - MOSFET - Piccolo segnale e carichi attivi#Esempio con bypass della resistenza di source|Esempio con bypass della resistenza di source]]; [[12 - EL - MOSFET - Piccolo segnale e carichi attivi#Carichi PMOS e collegamento alla logica CMOS|Carichi PMOS e collegamento alla logica CMOS]].
- **Circuiti digitali e logica CMOS**: [[13 - EL - Circuiti digitali e logica CMOS#Inverter resistivo - energia, potenza e ritardo|Inverter resistivo - energia, potenza e ritardo]]; [[13 - EL - Circuiti digitali e logica CMOS#Simmetria e soglie del CMOS|Simmetria e soglie del CMOS]]; [[13 - EL - Circuiti digitali e logica CMOS#Scarica del carico e tempi di propagazione CMOS|Scarica del carico e tempi di propagazione CMOS]]; [[13 - EL - Circuiti digitali e logica CMOS#Consumo durante la commutazione|Consumo durante la commutazione]].
- **Esercizi di esame svolti**: [[14 - EL - Esercizi di esame svolti#Esame 13-02-2020 - Guadagno di una cascata|Esame 13-02-2020 - Guadagno di una cascata]]; [[14 - EL - Esercizi di esame svolti#Esame 05-04-2022 - Integratore e saturazione|Esame 05-04-2022 - Integratore e saturazione]].

Gli errori principali riguardano sorgenti negli equivalenti, percentuali di assestamento, condizioni del cortocircuito virtuale, unità di corrente, pinch-off, distinzione tra corrente e transconduttanza, segni della polarizzazione e differenza tra energia e potenza. Negli esercizi finali: guadagno caricato **18.18**, e saturazione dell’integratore a **10 ms**.
