# Obsidian-University

## Estensioni Obsidian consigliati
- Omnisearch
- Various Complements
- Minimal theme settings (per il tema `Minimal Theme`)
- Admonition
- Edge TTS
- Whisper
- LanguageTool integration
- Excalibur
- PDF++
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

**Obiettivo:** Creare una **Nota Master in Markdown per Obsidian** analizzando due input:
1.  **Visual Input:** Il contenuto delle Slide (PDF/PPTX).
2.  **Audio Input:** La sbobinatura della lezione (Transcript).

**IL TUO ALGORITMO DI LAVORO:**
Devi fondere le due fonti in un testo unico. Usa le slide come "scheletro" (struttura) e la sbobinatura come "muscoli" (spiegazione profonda).

---

### ⚠️ REGOLE INDEROGABILI (Strict Rules)

**LINGUA OUTPUT:** Scrivi il contenuto della nota rigorosamente in **ITALIANO**.

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