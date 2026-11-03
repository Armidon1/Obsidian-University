---
name: appuntiLatex
description: Genera appunti universitari completi in LaTeX e PDF (LuaLaTeX, capitoli, riquadri per correzioni e dubbi, figure spiegate, glossario, indice) da slide, dispense, libri e appunti presi in classe. Usare quando Simone chiede appunti in LaTeX o in PDF da compilare, o invoca /appuntiLatex, anche per integrare appunti LaTeX già esistenti. Per le note Obsidian in Markdown usare invece /appunti.
---

# /appuntiLatex — dal materiale del corso a un libro di appunti in LaTeX

Argomenti opzionali: percorso del materiale, e opzioni come `solo capitoli` (senza glossario), `con libro <file>`, `appunti classe <file>`. Senza argomenti si lavora sulla cartella corrente.

Il risultato è una cartella `appunti/` nel corso: `main.tex`, `capitoli/`, `images/`, `main.pdf`. Deve potersi studiare da sola, senza aprire le slide.

In questo file `<skill>` è la cartella della skill. Lancia gli script Python con `python3 -I` e tieni i file di lavoro nella scratchpad: in `appunti/images/` finisce solo ciò che viene incluso nel PDF.

## 0. Ricognizione

1. Elenca i sorgenti e leggi cosa c'è già. Se `appunti/` esiste, **non sovrascrivere**: chiedi se integrare o creare una nuova cartella, perché può contenere modifiche di Simone.
2. Stabilisci il ruolo di ogni fonte. Di solito le slide e le dispense sono il riferimento, e fissano ordine e citazioni. Gli appunti in classe aggiungono ciò che è stato detto a lezione, ma contengono spesso errori di trascrizione e nomi scritti a orecchio.
3. Lancia il sopralluogo sui PDF:
   ```bash
   python3 -I <skill>/scripts/survey_pdfs.py <scratchpad>/survey <file.pdf> [...]
   ```
   Scrive il testo in `txt/`, le miniature in `thumbs/` e i fogli di contatto `sheet-*.png`. Stampa anche le pagine con immagini e poco testo: possono contenere testo dentro un'immagine, che `pdftotext` non vede. Guarda tutti i fogli con Read.
4. Ricostruisci l'ordine delle lezioni e confronta le fonti: quali argomenti hanno slide, quali solo appunti, cosa manca.
5. Chiedi una sola volta, e solo se cambia il risultato (lingua, libro da integrare, ordine davvero ambiguo). Il resto lo decidi tu e lo dichiari nel riepilogo.

## 1. Estrazione

- **PDF di slide**
  - testo: già in `txt/`, oppure `pdftotext -layout -f N -l N file.pdf -`;
  - immagini raster: `pdfimages -png -f N -l N file.pdf <out>/LNN-PP`;
  - figure vettoriali o spezzate in tasselli (`pdfimages` restituisce molti frammenti o niente): renderizza con `pdftoppm -r 170 -png -f N -l N file.pdf <out>/LNN`, poi ritaglia:
    ```bash
    python3 -I <skill>/scripts/slide_crops.py <out>/crops <pagina.png> [...]
    ```
    Lo script ritaglia ogni blocco di inchiostro, anche i blocchi di testo: scarta quelli inutili. Se due figure si fondono, ritaglia a mano con `magick pagina.png -crop LxA+X+Y +repage -trim uscita.png`.
- **PDF di libro o dispensa**: trova i capitoli con `pdftotext -layout`, leggili con Read (`pages`, massimo 20 per volta). Per le figure con didascalia usa `python3 -I <skill>/scripts/pdf_figures.py file.pdf <out> SIGLA [prima] [ultima]`, con `--bands` per quelle senza. Cita la pagina.
- **docx**: `python3 -I <skill>/scripts/extract_docx.py file.docx <out> SIGLA-LNN` produce il testo con i marcatori `[IMG nome]`.
- **pptx**: usa la skill `pptx`.

Controlla i ritagli con un foglio di contatto prima di usarli:
```bash
montage -label '%f' *.png -tile 8x -geometry 220x220+3+3 -pointsize 10 <scratchpad>/foglio.png
```

**Guarda ogni immagine prima di scrivere il capitolo**: va spiegata, non solo inserita. Dai ai file nomi che dicono cosa mostrano (`mappa-ebstorf.png`), perché nel sorgente LaTeX sono l'unico modo di riconoscerli.

Scarta logo, sfondi e decorazioni ripetute. Un'immagine di contenuto che non puoi usare (per esempio un fermo video illeggibile) va omessa e dichiarata nel riepilogo, non tolta in silenzio.

## 2. Impianto e prova tecnica

Prepara lo scheletro prima di scrivere:

```bash
cp -r <skill>/assets/template <corso>/appunti
```

1. In `main.tex` sostituisci i segnaposto `@@...@@` e attiva le lingue e le scritture che servono al corso (istruzioni nei commenti).
2. In `capitoli/00-prova.tex` aggiungi un campione delle scritture e dei simboli presenti nel materiale, poi compila:
   ```bash
   <skill>/scripts/compile.sh <corso>/appunti
   ```
   L'immagine TeX Live pesa circa 6 GB: se manca, lo script si ferma. Chiedi a Simone prima di rilanciarlo con `--pull`.
3. Guarda la pagina di prova e correggi il preambolo ora: un carattere mancante scoperto dopo ottanta pagine costa molto di più.
4. Togli la prova: cancella il file e la sua riga `\input` da `main.tex`.

## 3. Capitoli

Un capitolo per lezione o blocco di slide: `capitoli/NN-titolo.tex`, con `\chapter{...}\label{cap:...}`, aggiunto via `\input` in `main.tex`. Scrivi un capitolo alla volta e compila subito dopo: gli errori restano facili da localizzare e un'interruzione non fa perdere il lavoro.

- **Segui l'ordine del materiale originale**, con titoli per argomento e mai «Slide N».
- **Apri ogni capitolo** spiegando di cosa parla e come si collega ai precedenti; **chiudilo** con un riquadro `insintesi`.
- **Spiega**: per ogni concetto dì cos'è, perché viene introdotto, a quale problema risponde e come si lega al resto. Scrivi in prosa piana e completa i passaggi lasciati impliciti, senza aggiungere argomenti nuovi.
- **Immagini**: `\figw{larghezza}{file}{didascalia}` o `\figh{altezza}{a,b}{didascalia}` nel punto da cui provengono, con una spiegazione. La didascalia dice cosa si vede; il testo dice perché conta.
- **Testo dentro le immagini**: trascrivilo, e dichiaralo nel riepilogo.
- **Confronti**: tabelle `booktabs` con `tabularx`, che restano leggibili anche con testo lungo.
- **Flussi e strutture**: TikZ dove un diagramma chiarisce davvero. **Formule**: `$...$` e `align`. **Codice**: `lstlisting`; dello screenshot di un codice spiega cosa fa.
- **Rimandi**: `capitolo~\ref{cap:...}` verso i capitoli già visti, quando il legame è reale.
- **Indice**: `\aut{Cognome, Nome}` per autori e opere, `\idx{termine}` per i concetti. Attaccali alla parola, senza spazi prima.

### Fedeltà alle fonti

Il valore di questi appunti è che si possa capire da dove viene ogni affermazione, quindi ogni tipo di provenienza ha il suo segnale:

| Situazione | Segnale |
|---|---|
| Errore o incongruenza nel materiale | `correzione`: testo originale, correzione e motivo |
| Punto che le fonti non permettono di risolvere | `dubbio` |
| Spiegazione dal libro (`con libro`) | `dallibro`, con pagina verificata |
| Sezione senza slide, solo dagli appunti in classe | `\soloappunti` all'inizio |
| Conoscenza generale aggiunta da te | `\integrazione{...}` |

Applica queste regole:
- Non correggere mai in silenzio, e non presentare una tua conoscenza come se venisse dal corso. Se una correzione viene da te e non dalle fonti, dillo nel riquadro.
- Cita le lingue straniere esattamente come sono nel materiale, confrontandole con il testo estratto. Se sani un refuso evidente, dichiaralo; se il dubbio è sostanziale, lascia il testo e usa `dubbio`.
- Non inventare ciò che manca: niente testi, traduzioni, date o riferimenti ricostruiti a memoria. Una traduzione tua va indicata come tale.
- Un nome che sembra scritto a orecchio negli appunti va riportato com'è, con la forma probabile in un `dubbio`.
- Controlla i conti degli esempi numerici.
- Non dedurre il genere di una persona dal nome: formula la frase in modo neutro, se le fonti non lo indicano.

Citazioni: `\begin{cit}[lingua] ... \fontecit{(fonte)} \end{cit}`. Testo a fronte: `\afronte[lingua]{originale}{traduzione}`.

## 4. Glossario e indice

Con tutti i capitoli pronti, compila `capitoli/99-glossario.tex` (salvo `solo capitoli`): una voce per concetto, in ordine alfabetico, con una definizione breve e il rimando al capitolo. Riassume senza aggiungere: se una voce richiede spiegazioni, mancano nel capitolo. Verifica che ogni voce concordi con il testo, comprese le correzioni fatte.

Adatta la pagina «Come leggere questi appunti» in `main.tex` ai segnali usati davvero: togli quelli assenti.

## 5. Verifica

```bash
<skill>/scripts/compile.sh <corso>/appunti
python3 -I <skill>/scripts/check_latex.py <corso>/appunti
```

`check_latex.py` controlla immagini mancanti e inutilizzate, rimandi rotti, etichette doppie, capitoli non inclusi, segnaposto rimasti e, dal log, errori, caratteri mancanti, riferimenti non risolti e righe che sforano il margine. Correggi finché non riporta `problems: 0`.

Lo script non vede tutto, quindi guarda anche il risultato:
1. renderizza tutte le pagine (`pdftoppm -r 40 -png main.pdf <scratchpad>/pg/p`), componile in fogli con `montage` e cerca figure tagliate, pagine vuote e tabelle rotte;
2. guarda da vicino (`-r 80`) le pagine con scritture non latine, testi a fronte, tabelle larghe e figure affiancate;
3. rileggi le citazioni in lingua straniera confrontandole con il testo estratto.

Se il PDF supera i 30 MB, segnalalo; riduci le immagini solo su richiesta: `magick mogrify -resize '1600x1600>' images/*.png`, poi ricompila.

## 6. Riepilogo per Simone

Breve, in italiano:
- cosa è stato creato: capitoli, pagine, peso del PDF e percorso;
- le correzioni principali;
- i dubbi da verificare, specie quelli che contano per l'esame;
- le scelte fatte senza chiedere: ordine, sezioni basate solo sugli appunti, immagini omesse, testi trascritti da immagini;
- cosa hai controllato davvero e cosa no: non dire di aver riletto tutto se hai visto solo i fogli di contatto.

Non fare commit: lo fa Simone, oppure lo fai tu se te lo chiede.
