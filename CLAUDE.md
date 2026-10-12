# Obsidian-University

Repo git con gli appunti universitari di Simone, in formato Obsidian. Non è codice: il "prodotto" sono note Markdown da studiare.

## Struttura

- La repo `Obsidian-University/` è una **sottocartella del vault** Obsidian, la cui radice è `../` (`Obsidian Vault/`). Il vault contiene anche altre cartelle (`Obsidian-English/`, `HackTheBox/`, `Projects/`, …) che non fanno parte di questa repo.
- `University/Triennale/<Corso>/` e `University/Magistrale/<Corso>/`: una cartella per corso.
- Dentro un corso, di solito:
  - le note delle lezioni nella radice del corso;
  - `images/` per le immagini;
  - `pdf/`, `PDF/` o `Slides/` per il materiale originale (i nomi non sono uniformi tra i corsi: guarda cosa c'è prima di creare cartelle);
  - `Concetti/` per le note atomiche e il MOC (finora solo in `Triennale/Sistemi Operativi`);
  - `lab/` per i laboratori.
- `Extra/` e `Obsidian Guide/` contengono note generali (es. `Obsidian Guide/Callouts.md`, `Obsidian Guide/LaTeX.md` per la sintassi).
- `README.md` contiene i prompt storici per la generazione delle note e i plugin Obsidian usati.

## Convenzioni delle note

- **Nome delle note di lezione**: `NN - SIGLA - Titolo.md` (es. `03 - MA - Basic Static Analysis.md`, `07 - SO - Allocatori di Memoria.md`). La SIGLA è l'abbreviazione del corso: prima di scegliere un numero o una sigla, guarda le note già presenti nel corso.
- **Frontmatter**:
  ```yaml
  ---
  title: <Titolo>
  aliases:
    - <Sigla corso> — <Titolo>
  tags:
    - <corso-in-kebab-case>
    - <argomenti>
  source: <file sorgente, es. slides.pdf>
  ---
  ```
- Si apre con `# Titolo` e un callout `> [!abstract]` che spiega lo scopo della lezione e come si collega alle altre.
- Struttura: segue **l'ordine del materiale originale**, mai intestazioni "Slide 1/2". Il contenuto va arricchito, così che la nota si capisca da sola: cos'è un concetto, perché viene introdotto, a quale problema risponde.
- Usare callout (`[!note]`, `[!important]`, `[!tip]`, `[!example]`, `[!warning]`, `[!summary]`), tabelle per i confronti, Mermaid per i flussi, LaTeX `$...$` per le formule.
- **Errori nel materiale originale**: non vanno corretti in silenzio. Si segnalano con `> [!warning] Correzione`.
- **Immagini**: in `images/` del corso, inserite con `![[nome.png]]` nel paragrafo da cui provengono. Le immagini incollate a mano da Simone si chiamano `Pasted image <timestamp>.png`: non rinominarle. Quelle estratte automaticamente si chiamano `SIGLA-LNN-XX.ext`.
- **Wikilink**: Obsidian risolve i `[[nomi]]` su **tutto il vault**, quindi i nomi delle nuove note devono essere unici anche fuori da questa repo. Controlla con `find .. -name "<nome>.md"` prima di creare una nota con un nome generico. Collegare i concetti tra corsi diversi è benvenuto (es. Sistemi Operativi ↔ Sistemi di Calcolo, Malware Analysis ↔ assembly x86).

## Lingua

- Se il corso ha già delle note, si usa la stessa lingua di quelle.
- Triennale e corsi nuovi: italiano, con i termini tecnici in inglese (spiegati alla prima occorrenza).
- Se non è chiaro, chiedere.

## Appunti personali di Simone

Le note contengono anche commenti scritti a mano da Simone (es. "notice that the professor said…"), a volte con refusi. **Non riscriverli e non correggerli** quando si modifica una nota esistente, a meno che non venga chiesto esplicitamente.

## Generare note da materiale di un corso

Usa la skill `/appunti` (`.claude/skills/appunti/`): estrae testo e immagini da docx/pdf, scrive le note complete per lezione, le note atomiche in `Concetti/` con il MOC, e verifica link e immagini.

## Git

- Commit e push solo su richiesta esplicita.
- Nei messaggi di commit Simone usa semplicemente `update`; va bene un messaggio breve e descrittivo.
- I file sorgente (pdf, docx) restano nella repo così come sono: non spostarli e non cancellarli senza chiedere.
