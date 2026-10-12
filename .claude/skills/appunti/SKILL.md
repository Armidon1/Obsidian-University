---
name: appunti
description: Genera note Obsidian da materiale di un corso universitario (slide PDF, docx, capitoli di libro) — una nota completa per lezione con tutte le immagini, più note atomiche di ripasso in Concetti/ collegate da un MOC. Usare quando Simone chiede di creare o aggiornare appunti di un corso a partire da file sorgente.
---

# /appunti — dal materiale del corso alle note Obsidian

Argomenti opzionali: percorso del corso o dei file sorgente, e opzioni come `solo lezioni`, `solo concetti`, `con libro <file>`. Senza argomenti si lavora sulla cartella corrente.

Prima di iniziare, rileggi le convenzioni in `CLAUDE.md` nella root della repo (nomi, frontmatter, lingua, immagini).

## 0. Ricognizione (prima di scrivere qualsiasi cosa)

1. Elenca i file sorgente (`*.pdf`, `*.docx`, `*.pptx`) e le note già presenti nel corso.
2. Fissa la **sigla** del corso e la **numerazione** in base alle note esistenti; se non ce ne sono, proponile tu.
3. Decidi la **lingua** come indicato in `CLAUDE.md`.
4. Se esiste già una nota per una lezione, **non sovrascriverla**: chiedi se vuoi integrarla o crearne una nuova. Le note di Simone contengono commenti personali da preservare.
5. Se mancano informazioni che cambiano il risultato (lingua, se servono le note atomiche, se c'è un libro da integrare), chiedi una volta sola e poi procedi.

## 1. Estrazione

Gli script sono in `.claude/skills/appunti/scripts/`. Lanciali con `python3 -I` e scrivi l'output nella scratchpad, non nel vault.

- **docx**:
  ```bash
  python3 -I <skill>/scripts/extract_docx.py <file.docx> <outdir> SIGLA-LNN
  ```
  Produce `<outdir>/SIGLA-LNN.md`: il testo in ordine, con marcatori `[IMG nome]` nel punto esatto in cui compaiono le immagini e tag `[LI]` (lista), `[B]` (grassetto) e `[szNN]` (dimensione del font) che aiutano a riconoscere i titoli. Le immagini finiscono in `<outdir>/img/`.
- **pdf** (slide):
  - testo pagina per pagina con `pdftotext -layout -f N -l N file.pdf -`;
  - immagini raster con `pdfimages -png -p file.pdf <outdir>/img/SIGLA-LNN` (`-p` mette il numero di pagina nel nome, così sai dove vanno);
  - se le figure sono vettoriali (schemi, grafici) `pdfimages` non le trova: renderizza la pagina con `pdftoppm -png -r 110 -f N -l N file.pdf <outdir>/img/SIGLA-LNN-pN` e inserisci la pagina come immagine;
  - per capire cosa mostra una slide puoi anche leggere il PDF direttamente con Read (`pages`).
- **pdf** (libro o dispensa, con figure in mezzo al testo):
  - indice e confini dei capitoli: `pdftotext -layout` di tutto il file, poi cerca i titoli dei capitoli pagina per pagina;
  - leggi i capitoli con Read (`pages`, al massimo 20 pagine per volta): così vedi testo, tabelle, codice e figure insieme;
  - figure con didascalia ("Figura x.y"): `python3 -I <skill>/scripts/pdf_figures.py file.pdf <outdir> SIGLA [prima] [ultima]` le ritaglia automaticamente sopra la didascalia (anche se vettoriali); con `--bands` prova a ritagliare anche le figure senza didascalia;
  - per le figure che il ritaglio automatico sbaglia o non trova, ritaglia a mano con coordinate: renderizza la pagina con `pdftoppm -r 150` e ritaglia la regione con PIL o `magick`. Controlla sempre i ritagli con un `magick montage` prima di inserirli;
  - le tabelle e il codice si trascrivono in Markdown, non si inseriscono come immagini; le figure come immagini;
  - i nomi delle immagini usano la pagina: `SIGLA-pNNN-K.png`;
  - nelle note cita la pagina del PDF alla fine di ogni blocco, es. _(dispensa, pp. 41–43)_.
- **pptx**: usa la skill `pptx` per estrarre il testo e le immagini.

Poi **guarda tutte le immagini** con Read, prima di scrivere la nota della lezione corrispondente: vanno spiegate, non solo inserite. Molte sono screenshot di codice: descrivi cosa fa il codice.

Copia le immagini in `images/` del corso (`cp`), mantenendo i nomi `SIGLA-LNN-XX.ext`.

## 2. Note complete per lezione

Una nota per lezione, `NN - SIGLA - Titolo.md`, nella cartella del corso.

- Frontmatter e callout `[!abstract]` come in `CLAUDE.md`. Nell'abstract metti anche il link `[[MOC - <Corso>]]`, se il MOC verrà creato.
- **Segui esattamente l'ordine del materiale originale**, con titoli per argomento e mai "Slide N".
- **Arricchisci il contenuto**: per ogni concetto spiega cos'è, perché viene introdotto, a quale problema risponde e come si collega agli argomenti prima e dopo. Aggiungi esempi concreti e i passaggi lasciati impliciti.
- **Tutte le immagini** vanno inserite con `![[...]]` nel paragrafo da cui provengono, ognuna seguita da una spiegazione. Nessuna immagine estratta deve restare inutilizzata (lo verifica lo script del punto 4). I duplicati si inseriscono comunque, ma vanno segnalati nel riepilogo finale.
- Aggiungi diagrammi **Mermaid** dove chiariscono un flusso (sequenze, stati, alberi), tabelle per i confronti e LaTeX per le formule.
- Controlla i conti degli esempi numerici. **Errori nel materiale** → `> [!warning] Correzione`, lasciando visibile il testo originale.
- Con un libro (`con libro <file>`): usalo per spiegare meglio quello che c'è nelle slide, non per aggiungere argomenti nuovi. Cita sezione o pagina, segna gli approfondimenti con un callout `> [!quote] Dal libro`, e non inventare riferimenti che non hai verificato.
- Inserisci **wikilink**:
  - verso le altre lezioni dello stesso corso, anche a sezioni specifiche (`[[NN - SIGLA - Titolo#Sezione|testo]]`);
  - verso le note atomiche (`[[Concetto]]`), all'inizio della sezione che tratta quel concetto ("Vedi [[Concetto]].");
  - verso note di altri corsi del vault, quando c'è un collegamento reale (cercale con `find`/`grep`).

## 3. Note atomiche e MOC

Solo dopo aver scritto tutte le lezioni.

1. **Scegli l'elenco dei concetti** (indicativamente 5–10 per lezione) **prima** di inserire i wikilink nelle lezioni, così i nomi sono stabili. Verifica che ogni nome sia unico nel vault: `find .. -name "<Nome>.md"`.
2. Crea `Concetti/` nel corso. Ogni nota atomica è un **riassunto per il ripasso**:
   - frontmatter con `title` e tag (`<corso>`, `concetto`, argomenti);
   - `> [!summary] In breve` con 1–2 frasi;
   - un corpo breve: bullet, formule, una tabella o un mini esempio di codice, senza ripetere tutta la lezione;
   - `## Collegamenti`: concetti correlati (`[[A]] · [[B]]`) e `[[MOC - <Corso>]]`;
   - `> [!info] Approfondimento` con i link alle **sezioni esatte** delle lezioni (`[[NN - SIGLA - Titolo#Sezione|Lezione N — Sezione]]`).
3. Per molte note conviene usare il generatore, che scrive tutte le note con un formato uniforme:
   ```bash
   python3 -I <skill>/scripts/gen_atomic.py <corso>/Concetti <dati.py> [<dati2.py> ...]
   ```
   Il formato del file dati è descritto in cima allo script. Scrivi i file dati nella scratchpad.
4. Crea `Concetti/MOC - <Corso>.md` con:
   - una tabella di tutte le lezioni (numero, link, argomenti);
   - i concetti raggruppati per tema;
   - una sezione "Percorsi trasversali" con un diagramma Mermaid e catene di link tra concetti.

## 4. Verifica (obbligatoria)

```bash
python3 -I <skill>/scripts/check_links.py <cartella-corso>
```

Lo script controlla che tutti i wikilink del corso puntino a note esistenti nel vault, che i link `#Sezione` puntino a titoli esistenti, che ogni `![[immagine]]` esista e che ogni immagine in `images/` sia usata almeno una volta. Correggi finché non riporta `problems: 0`. Le immagini incollate in precedenza da Simone e non usate vanno solo segnalate, non cancellate.

## 5. Riepilogo per Simone

Breve, in italiano:
- cosa è stato creato (numero di lezioni, di note atomiche, di immagini) e dove;
- le correzioni segnalate nelle note;
- le scelte fatte senza chiedere (lingua, sigla) e i dubbi rimasti (immagini duplicate, testo illeggibile, conti che non tornano).

Non fare commit: lo fa Simone, oppure lo fai tu se te lo chiede.
