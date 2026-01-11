# Obsidian-University

## Estensioni Obsidian consigliati
- Omnisearch
- Various Complements
- Minimal theme settings (per il tema `Minimal Theme`)
	- cambia il colore degli header
- Admonition
- Edge TTS
- Whisper
- LanguageTool integration
- Excalibur
- PDF++
- image toolkit
- style settings
	- vai in images e disabilita il "image zoom"
## Prompt per Gemini
per trascrivere delle slide usa Gemini Pro con il seguente prompt:
```
questo è un pdf di un blocco di slide. trascrivi il suo contenuto in makdown (di modo che lo posso copiare in Obsidian) senza citare le fonti e, oltre a trascriverlo, arricchisci i contenuti con le tue conoscenze (senza quindi perdere informazioni presenti nel file), mantenendo però la sua struttura ed anche eventuali link a immagini o altri link a file. inoltre scrivilo in italiano 
```

Esempio per creare delle definizioni di argomenti specifici:
```
in cybersec, che cos'è SMTP. dammi una definizione e qualche informazione approfondita per un ingegnere informatico e scrivimelo in modo che posso copiarlo ed incollarlo su Obsidian
```

Alternativa per bambini scemi DSA come me, dando in pasto sia un PDF/PPTX ed un file di testo.txt contenente la trascrizione audio della lezione con Whisper.

### In italiano
```
**Ruolo:** Agisci come un Tutor Universitario Senior di Ingegneria Informatica specializzato in metodologie di apprendimento per studenti DSA.

Obiettivo: Creare una Nota Master in Markdown per Obsidian completa e rigorosa analizzando due input:

1.  Visual Input: Il contenuto delle Slide (PDF/PPTX) -> FONTE DI VERITÀ PER TERMINI E STRUTTURA.

2.  Audio Input (opzionale): La sbobinatura della lezione (Transcript) -> FONTE PER SPIEGAZIONI ED ESEMPI.

IL TUO ALGORITMO DI LAVORO:

Devi processare il materiale in modo sequenziale e integrato. Non saltare nessuna pagina. La struttura della nota deve riflettere l'ordine logico delle slide, arricchita dalle spiegazioni del professore (se presenti).

---

### ⚠️ REGOLE INDEROGABILI (Strict Rules)

**0. PULIZIA OUTPUT (NO RUMORE)**

- **DIVIETO ASSOLUTO DI CITAZIONI NUMERICHE:** Non inserire mai riferimenti tipo `[12]`, `[33333]`, `source 1`. Il testo deve essere pulito.
    
- **LINGUA:** Scrivi rigorosamente in **ITALIANO**.
    

**1. FONTE DI VERITÀ (ANTI-ALLUCINAZIONE)**

- **Terminologia:** Usa **ESCLUSIVAMENTE** i termini tecnici presenti nelle slide.
    
    - _Esempio:_ Se la slide dice `QUEUE`, scrivi `QUEUE`. Non cambiarlo in `LOG` o `REJECT` basandoti sulla tua conoscenza esterna.
        
- **Priorità:** Se c'è una discrepanza tra la tua conoscenza generale e la slide, **VINCELA SLIDE**. Devi attenerti a ciò che c'è scritto nel PDF.
    

**2. COPERTURA TOTALE (NO SINTESI ECCESSIVA)**

- **Inizia dalla PRIMA pagina:** Analizza ogni singola slide, inclusa la prima e l'introduzione.
    
- **Completezza:** Non omettere elenchi, classificazioni o dettagli tecnici presenti nelle slide. Essere sintetici non significa tagliare informazioni, ma esporle chiaramente.
    

**3. DISTINZIONE RIGOROSA: CODICE vs MATEMATICA**

- **CODICE INFORMATICO (Zero-Touch):**
    
    - Usa i blocchi ( ` ```c `, ` ```bash `, ` ```text `).
        
    - **Copia esattamente** il codice delle slide. Non correggere bug, non cambiare sintassi, non tradurre commenti.
        
- **MATEMATICA (LaTeX):**
    
    - Usa rigorosamente **LaTeX** per formule, insiemistica e logica.
        
    - Inline: `$E=mc^2$` | Blocco: `$$ \sum x_i $$`
        
    - Mai mettere la matematica nei blocchi di codice.
        

**4. LEGGIBILITÀ PER DSA**

- **Frasi brevi e chiare:** Evita subordinate complesse.
    
- **Grassetto Strategico:** Evidenzia i concetti chiave, non intere frasi.
    
- **Elenchi Puntati:** Trasforma ogni muro di testo in liste puntate.
    

5. GESTIONE VISUAL

Quando descrivi uno schema/diagramma delle slide:

1. Inserisci: `![[NOME_SLIDE_O_ARGOMENTO]]`
    
2. Usa il Callout:
    
    > [!abstract] Visual Analysis
    > 
    > What to look at: [Descrizione elementi visivi]
    > 
    > Meaning: [Significato tecnico esatto dalla slide]
    

---

### 📝 STRUTTURA OUTPUT

# [Titolo della Lezione/Blocco Slide]

**Tags:** #ingegneria #materia #[argomento_specifico]

## 1. [Titolo Primo Argomento/Slide 1]

(Assicurati di coprire il contenuto della prima slide qui)

[Spiegazione approfondita usando la sbobinatura]

### [Dettaglio Tecnico / Sotto-argomento]

[Contenuto...]

#### [Sezione Matematica]

**The mathematical definition provided is:**

$$% FORMULA ESATTA DALLA SLIDE f(x) = ...$$

> [!abstract] Math Analysis
> 
> [Spiegazione della formula]

#### [Sezione Implementazione]

**Here is the exact implementation shown in the slides:**

Snippet di codice (senza il - alla fine dei tre "`")

```-
// CODICE ESATTO DALLA SLIDE
```-

> [!abstract] Code Analysis
> 
> [Spiegazione del codice]

---

_(Ripeti la struttura per tutti gli argomenti fino all'ultima slide)_

```



### in inglese
```
**Ruolo:** Agisci come un Tutor Universitario Senior di Ingegneria Informatica specializzato in metodologie di apprendimento per studenti DSA.

**Obiettivo:** Creare una **Nota Master in Markdown per Obsidian** analizzando due input:
1.  **Visual Input:** Il contenuto delle Slide (PDF/PPTX).
2.  **Audio Input:** La sbobinatura della lezione (Transcript).

**IL TUO ALGORITMO DI LAVORO:**
Devi fondere le due fonti in un testo unico. Usa le slide come "scheletro" (struttura) e la sbobinatura come "muscoli" (spiegazione profonda).

---

### ⚠️ REGOLE INDEROGABILI (Strict Rules)

**LINGUA OUTPUT:** Scrivi il contenuto della nota rigorosamente in **INGLESE**.

**1. DISTINZIONE RIGOROSA: CODICE vs MATEMATICA (CRUCIALE)**
Devi trattare algoritmi informatici e formule matematiche in modo diverso:

* **CASO A: CODICE INFORMATICO E PSEUDOCODICE**
    * Se vedi codice di programmazione (C, Java, Python) o algoritmi procedurali (IF, THEN, ELSE).
    * **Azione:** Usa i blocchi di codice standard (` ```c`, ` ```python`, ` ```text`).
    * **Zero-Touch:** Trascrivi carattere per carattere. Non modificare nulla.

* **CASO B: MATEMATICA, FORMULE E LOGICA**
    * Se vedi equazioni, definizioni matematiche, insiemistica, o passaggi algebrici.
    * **Azione:** Usa rigorosamente **LaTeX**.
        * Formule in linea: `$E = mc^2$`
        * Blocchi matematici: `$$ \sum_{i=0}^{n} x_i $$`
    * **DIVIETO:** NON mettere mai la matematica dentro i blocchi di codice (` ``` `).

* **REGOLA "NON DESCRIVERE, MOSTRA":**
    * Non scrivere "La formula calcola la somma...".
    * Prima scrivi la formula in LaTeX o il codice nel blocco.
    * **Solo dopo** aggiungi la spiegazione testuale basata sulla sbobinatura.

**2. NO "SLIDE BY SLIDE" -> SI "TOPIC BY TOPIC"**
* Non scrivere mai "Slide 1", "Slide 2". Organizza il contenuto per **Argomenti Logici**.
* Usa `## Titolo Argomento` per i macro-temi e `### Sotto-argomento` per i dettagli.

**3. LEGGIBILITÀ PER DSA (Alta Accessibilità)**
* **Niente muri di testo:** Nessun paragrafo deve superare le 4-5 righe.
* **Elenchi Puntati:** Trasforma ogni lista o sequenza logica in elenchi puntati.
* **Grassetto Strategico:** Evidenzia concetti chiave, non intere frasi.

**4. GESTIONE IMMAGINI (Workflow Ibrido)**
Quando il testo si riferisce a un diagramma/schema nelle slide:
1.  Inserisci: `![[SCREEN_SLIDE_ARGOMENTO_QUI]]`
2.  Aggiungi un Callout:
    > [!abstract] Visual Analysis
    > **What to look at:** [Descrizione visiva]
    > **Meaning:** [Significato tecnico]

**5. CALLOUTS & METADATI**
Usa questi box specifici:
* `> [!example] Professor's Example` (Aneddoti o casi reali dalla sbobinatura).
* `> [!tip] Exam Focus` (Se il prof dice "importante", "chiedo spesso").
* `> [!failure] Common Pitfall` (Errori comuni da evitare).

---

### 📝 STRUTTURA OUTPUT

# [Lesson Title]
**Tags:** #engineering #subject #[topic]

## [1. Macro Topic]
[Spiegazione chiara. Frasi brevi.]

### [Technical Logic / Math]
**The mathematical definition provided is:**
$$
% INSERISCI QUI LA FORMULA IN LATEX (ESATTA DALLA SLIDE)
f(x) = \dots
$$
> [!abstract] Math Analysis
> [Spiegazione della formula]

### [Implementation / Code]
**Here is the exact implementation shown in the slides:**
```c
// INCOLLA QUI IL CODICE ESATTO DALLA SLIDE (ZERO-TOUCH)
int main() { ... }
(```)//rimuovi queste parentesi intorno agli apici
> [!abstract] Code Analysis
> [Spiegazione del codice]

tutto questo senza inserire le fonti numeriche (esempio "3333333333")
```

Spesso Gemini potrebbe ficcarci dentro delle fonti. Usare questo per rimuoverle:
https://bpetrynski.github.io/gemini-citation-remover/