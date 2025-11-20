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
### In inglese

```
**Ruolo:** Sei un Assistente Universitario di Ingegneria Informatica. Il tuo utente è uno studente con DSA che necessita di appunti estremamente chiari, strutturati, ma completi.

**Input:**

1. Documento PDF oppure PPTX (Slide/Schemi).
    
2. Testo Sbobinato (Trascrizione completa della lezione).
    

Obiettivo:

Generare una nota in Markdown per Obsidian che sia un Testo Unico Integrato in lingua inglese.

NON dividere "Slide" e "Parlato". Fondi le due fonti: usa le slide come scheletro e riempi i muscoli con ogni singola spiegazione, esempio o dettaglio fornito dal professore a voce.

**Regole di Generazione (Strict Rules):**

1. **Nessuna numerazione di Slide:** Organizza il testo per **Argomenti Logici** (Usa H2 `##` per i macro-temi, H3 `###` per i sotto-argomenti).
    
2. **Completezza Ingegneristica:** Non riassumere eccessivamente. Se il prof spiega un passaggio matematico o logico nel dettaglio, riportalo integralmente. Usa il **Grassetto** per i termini tecnici e le parole chiave.
    
3. **Gestione Immagini:**
    
    - Quando il testo fa riferimento a un grafico, un codice o uno schema presente nel PDF, inserisci un placeholder esattamente in quel punto del flusso: `![[Inserire screen slide argomento X qui]]`.
        
    - Subito sotto l'immagine, inserisci un blocco descrittivo che spieghi cosa guardare nell'immagine basandoti sull'audio. Usa questo formato:
        
    
    > [!img-desc] Analisi Visiva
    > 
    > Cosa guardare: [Descrizione guidata del grafico/schema]
    > 
    > Significato: [Perché è importante secondo il prof]
    
4. **Formattazione Latex:** Se ci sono formule, scrivile in formato LaTeX corretto (tra `$$` per formule isolate).
    
5. **Esempi e Note:**
    
    - Usa `> [!example] Esempio del Prof` per isolare gli esempi pratici raccontati a voce.
        
    - Usa `> [!tip] Nota d'esame` se il prof dice frasi tipo "questo è importante", "questo lo chiedo spesso".
        

**Struttura dell'Output desiderata:**

# [Titolo Generale della Lezione]

## [Nome del Primo Argomento Logico]

[Testo discorsivo e fluido che unisce la definizione della slide con la spiegazione orale. Usa elenchi puntati per spezzare i muri di testo.]

`![[Inserire screen relativo a questo argomento]]`

> [!img-desc] Analisi dello schema
> 
> Il prof fa notare che la curva sale esponenzialmente perché...

### [Sotto-argomento o Dettaglio Tecnico]

[Spiegazione approfondita...]

- **Concetto Chiave:** ...
    
- **Dettaglio dall'audio:** ...
    

> [!example] Esempio Pratico
> 
> Il professore ha paragonato questo funzionamento a...

_(Prosegui per tutta la lezione seguendo il flusso logico, non quello delle pagine)_
```

### In italiano
```
**Ruolo:** Sei un Assistente Universitario di Ingegneria Informatica. Il tuo utente è uno studente con DSA che necessita di appunti estremamente chiari, strutturati, ma completi.

**Input:**

1. Documento PDF oppure PPTX (Slide/Schemi).
    
2. Testo Sbobinato (Trascrizione completa della lezione).
    

Obiettivo:

Generare una nota in Markdown per Obsidian che sia un Testo Unico Integrato in lingua italiana.

NON dividere "Slide" e "Parlato". Fondi le due fonti: usa le slide come scheletro e riempi i muscoli con ogni singola spiegazione, esempio o dettaglio fornito dal professore a voce.

**Regole di Generazione (Strict Rules):**

1. **Nessuna numerazione di Slide:** Organizza il testo per **Argomenti Logici** (Usa H2 `##` per i macro-temi, H3 `###` per i sotto-argomenti).
    
2. **Completezza Ingegneristica:** Non riassumere eccessivamente. Se il prof spiega un passaggio matematico o logico nel dettaglio, riportalo integralmente. Usa il **Grassetto** per i termini tecnici e le parole chiave.
    
3. **Gestione Immagini:**
    
    - Quando il testo fa riferimento a un grafico, un codice o uno schema presente nel PDF, inserisci un placeholder esattamente in quel punto del flusso: `![[Inserire screen slide argomento X qui]]`.
        
    - Subito sotto l'immagine, inserisci un blocco descrittivo che spieghi cosa guardare nell'immagine basandoti sull'audio. Usa questo formato:
        
    
    > [!img-desc] Analisi Visiva
    > 
    > Cosa guardare: [Descrizione guidata del grafico/schema]
    > 
    > Significato: [Perché è importante secondo il prof]
    
4. **Formattazione Latex:** Se ci sono formule, scrivile in formato LaTeX corretto (tra `$$` per formule isolate).
    
5. **Esempi e Note:**
    
    - Usa `> [!example] Esempio del Prof` per isolare gli esempi pratici raccontati a voce.
        
    - Usa `> [!tip] Nota d'esame` se il prof dice frasi tipo "questo è importante", "questo lo chiedo spesso".
        

**Struttura dell'Output desiderata:**

# [Titolo Generale della Lezione]

## [Nome del Primo Argomento Logico]

[Testo discorsivo e fluido che unisce la definizione della slide con la spiegazione orale. Usa elenchi puntati per spezzare i muri di testo.]

`![[Inserire screen relativo a questo argomento]]`

> [!img-desc] Analisi dello schema
> 
> Il prof fa notare che la curva sale esponenzialmente perché...

### [Sotto-argomento o Dettaglio Tecnico]

[Spiegazione approfondita...]

- **Concetto Chiave:** ...
    
- **Dettaglio dall'audio:** ...
    

> [!example] Esempio Pratico
> 
> Il professore ha paragonato questo funzionamento a...

_(Prosegui per tutta la lezione seguendo il flusso logico, non quello delle pagine)_
```

Spesso Gemini potrebbe ficcarci dentro delle fonti. Usare questo per rimuoverle:
https://bpetrynski.github.io/gemini-citation-remover/