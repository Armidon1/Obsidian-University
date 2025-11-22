# Introduzione all'Intelligenza Artificiale

**Tags:** #uni #AI #ingegneria #appunti
**Fonte:** Slide Prof. Patrizi + Cap 1-2 "AI A Modern Approach"

---

## 1. Cos'è l'Intelligenza Artificiale?

Non esiste una definizione univoca, ma il campo si è evoluto attraverso diverse approcci storici. L'obiettivo principale è creare agenti (programmi o dispositivi) che agiscono in modo "intelligente".

### I 4 Approcci Storici
Il libro categorizza l'IA in base a due dimensioni: **Pensiero vs Azione** e **Umano vs Razionale**.

1.  **Agire umanamente (Test di Turing - 1950):** L'incapacità di distinguere la macchina dall'umano. Richiede NLP, rappresentazione della conoscenza e ragionamento automatico.
2.  **Pensare umanamente (Modellazione Cognitiva):** Cercare di simulare il funzionamento della mente umana (scienze cognitive).
3.  **Pensare razionalmente (Logica):** Usare la logica deduttiva (es. sillogismi di Aristotele) per arrivare a conclusioni corrette. *Problema:* difficile formalizzare tutto in logica.
4.  **Agire razionalmente (Approccio moderno):** Agire per massimizzare il raggiungimento di un obiettivo (o l'utilità attesa).
    * È l'approccio prevalente oggi.
    * Include il ragionamento logico come mezzo, ma ammette anche azioni basate su riflessi o intuizioni in caso di incertezza.

> **Definizione Formale:** L'IA consiste nel progettare **agenti** che si comportano in modo da massimizzare una **funzione obiettivo** (o misura di prestazione).

---

## 2. IA Deduttiva vs Induttiva (AI vs ML)

Le moderne applicazioni di IA combinano spesso due anime:

| **Approccio Deduttivo (Reasoning / "Good Old-Fashioned AI")** | **Approccio Induttivo (Machine Learning)** |
| :--- | :--- |
| Si parte da regole generali, fatti e obiettivi definiti a priori. | Si parte dai **dati** raccolti (esempi). |
| Si deduce nuova conoscenza o azioni tramite ragionamento logico/probabilistico. | Si apprende la relazione input-output (la "regola") analizzando i dati. |
| Metodi "esatti", spiegabili. | Focus sulle performance, spesso "black box". |

> **Nota:** Il Machine Learning è una sotto-area dell'IA. Riguarda l'apprendimento dai dati, ma non copre l'intera IA (che include pianificazione, ricerca, rappresentazione della conoscenza).

---

## 3. Cenni Storici

* **Nascita ufficiale:** Workshop di Dartmouth (1956). Ipotesi fondante: *"Ogni aspetto dell'apprendimento o dell'intelligenza può essere descritto così precisamente da poter essere simulato da una macchina"*.
* **Cicli di Hype e Inverni dell'IA:** La storia dell'IA alterna momenti di grandi aspettative a periodi di disillusione (AI Winter) dovuti a promesse non mantenute.
* **Stato dell'arte:** Oggi l'IA eccelle in compiti specifici (guida autonoma, traduzione, giochi come Scacchi/Go con AlphaZero, diagnosi medica), ma manca ancora di etica, empatia e comprensione profonda del contesto (Intelligenza Generale).

---

## 4. Agenti Intelligenti

Questa è la base architetturale dell'IA moderna.

### Definizione di Agente
Un agente è qualsiasi entità in grado di:
1.  **Percepire** l'ambiente attraverso **sensori**.
2.  **Agire** sull'ambiente attraverso **attuatori**.

L'agente possiede una "Funzione Agente" (o modulo di deliberazione) che mappa la storia delle percezioni in un'azione.

![[Inserire qui Immagine Figura 2.1 dal PDF]]
> *Figura 2.1: Schema generale di interazione Agente-Ambiente. L'agente riceve percorsi (Percepts) e restituisce Azioni.*

### Agente Razionale
Un agente razionale è colui che fa "la cosa giusta".
* **Criterio:** Massimizzare il valore atteso della **Misura di Prestazione** (Performance Measure).
* La razionalità dipende da:
    1.  La misura di prestazione (es. pulire casa, vincere a scacchi).
    2.  La conoscenza a priori dell'ambiente.
    3.  Le azioni disponibili.
    4.  La sequenza di percezioni passate.

> **Attenzione:** Razionalità $\neq$ Onniscienza. La razionalità massimizza il risultato *atteso* basandosi su ciò che l'agente sa, non il risultato *reale* (che potrebbe dipendere da fattori imprevisti).

---

## 5. Ambienti e Specifiche PEAS

Per progettare un agente, bisogna prima definire il problema tramite l'acronimo **PEAS**:
* **P**erformance (Misura di prestazione)
* **E**nvironment (Ambiente)
* **A**ctuators (Attuatori)
* **S**ensors (Sensori)

### Esempio: Taxi a guida autonoma (Figura 2.4)
![[Inserire qui Immagine Figura 2.4 dal PDF]]
> *Figura 2.4: Esempio di descrizione PEAS per un tassista automatico.*

### Proprietà degli Ambienti
La difficoltà del compito dipende dalle caratteristiche dell'ambiente. Le dimensioni principali (Fig 2.6 del libro) sono:

1.  **Osservabile (Fully vs Partially):** I sensori vedono tutto lo stato o solo una parte? (es. Scacchi = Totale; Poker/Guida = Parziale).
2.  **Agenti (Single vs Multi):** Sono solo o ci sono avversari/collaboratori?
3.  **Deterministico vs Stocastico:** L'azione ha un effetto certo o incerto? (Scacchi = Deterministico; Guida = Stocastico/Non-deterministico).
4.  **Episodico vs Sequenziale:** Le decisioni attuali influenzano quelle future? (Classificazione immagini = Episodico; Scacchi = Sequenziale).
5.  **Statico vs Dinamico:** L'ambiente cambia mentre l'agente "pensa"?
6.  **Discreto vs Continuo:** Gli stati sono finiti o continui? (Scacchi = Discreto; Guida = Continuo).

![[Inserire qui Immagine Figura 2.6 dal PDF]]
> *Figura 2.6: Esempi di ambienti classificati secondo le proprietà.*

---

## 6. Struttura degli Agenti (Reasoning Agents)

Le slide si concentrano sugli agenti che *ragionano*, ovvero che usano un **modello dell'ambiente**. Il libro (Cap 2.4) dettaglia diverse architetture, dalla più semplice alla più complessa.

### A. Agente Reattivo Semplice (Simple Reflex)
Agisce solo in base alla percezione *corrente*. Regole *Condition-Action* (es. `SE auto davanti frena ALLORA frena`).
* *Limite:* Funziona bene solo se l'ambiente è totalmente osservabile.

### B. Agente Basato su Modello (Model-Based)
Mantiene uno **Stato Interno** per gestire l'osservabilità parziale.
Deve sapere:
1.  Come evolve il mondo indipendentemente dall'agente.
2.  Come le azioni dell'agente influenzano il mondo.

![[Inserire qui Immagine Figura 2.11 dal PDF]]
> *Figura 2.11: Schema di un agente basato su modello. Nota il "What the world is like now" che persiste nel tempo.*

### C. Agente Basato su Obiettivi (Goal-Based)
Non basta sapere come è fatto il mondo, bisogna sapere **dove si vuole arrivare**.
L'agente usa ricerca e pianificazione per trovare sequenze di azioni che portano al *Goal*.

![[Inserire qui Immagine Figura 2.13 dal PDF]]
> *Figura 2.13: Agente basato su obiettivi. Introduce la proiezione futura: "What it will be like if I do action A".*

### D. Agente Basato su Utilità (Utility-Based) - **Focus Slide**
Spesso ci sono molti modi per raggiungere un obiettivo, ma alcuni sono migliori (più veloci, più sicuri, meno costosi).
* **Funzione di Utilità:** Assegna un numero reale (punteggio) a quanto è "buono" uno stato.
* L'agente sceglie l'azione che massimizza l'**Utilità Attesa**.

![[Inserire qui Immagine Figura 2.14 dal PDF]]
> *Figura 2.14: Agente basato su utilità. È il modello più generale e flessibile per agenti razionali.*

---
**Prossimi passi:** Approfondire come rappresentare gli stati (atomici, fattorizzati, strutturati) per permettere agli agenti di ragionare (Cap 3 e successivi).