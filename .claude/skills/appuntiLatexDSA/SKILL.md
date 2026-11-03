---
name: appuntiLatexDSA
description: Genera appunti universitari completi in LaTeX e PDF pensati per chi ha DSA lievi (dislessia, discalculia, disortografia, disgrafia): stessi contenuti di /appuntiLatex, senza perdite né semplificazioni, con impaginazione ad alta leggibilità, mappe concettuali e diagrammi di flusso per capitolo e per concetto, schede di ripasso e controlli di completezza. Usare quando Simone chiede appunti per DSA o dislessia, appunti con più schemi e mappe concettuali, o invoca /appuntiLatexDSA. Per appunti LaTeX standard usare /appuntiLatex, per note Obsidian /appunti.
---

# /appuntiLatexDSA — appunti in LaTeX completi e accessibili per studenti con DSA

Argomenti opzionali: percorso del materiale, e opzioni come `solo capitoli` (senza glossario), `con libro <file>`, `appunti classe <file>`. Senza argomenti si lavora sulla cartella corrente.

Il risultato è una cartella `appunti/` nel corso: `main.tex`, `capitoli/`, `images/`, `inventario/`, `main.pdf`.

In questo file `<skill>` è la cartella della skill. Lancia gli script Python con `python3 -I` e tieni i file di lavoro nella scratchpad: in `appunti/images/` finisce solo ciò che viene incluso nel PDF.

## Il principio: stesso contenuto, più vie d'accesso

Chi ha un DSA lieve ha le stesse capacità di ragionamento degli altri studenti e sostiene lo stesso esame. La difficoltà sta nel decodificare il testo, nel tenere a mente sequenze, nomi, date e numeri, e nel ritrovare le informazioni. Questi appunti riducono il costo di lettura e offrono più vie per arrivare allo stesso concetto: testo, schema, tabella e ripasso.

Quindi **si aggiunge, non si toglie**:
- ogni concetto, nome, data, formula, esempio, eccezione e citazione del materiale resta nel testo;
- i termini tecnici restano, spiegati alla prima occorrenza: non si sostituiscono con parole più facili;
- le citazioni difficili restano integrali; la spiegazione semplice si aggiunge dopo;
- uno schema accompagna il testo e non lo sostituisce, anche perché la sintesi vocale non legge bene i diagrammi;
- rendere chiara la forma è permesso, ridurre il ragionamento no: scomponi una frase lunga in più frasi, ma mantieni ogni passaggio, condizione e sfumatura.

Il PDF sarà più lungo di una versione standard, ed è previsto: non comprimerlo togliendo contenuti.

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

**Guarda ogni immagine prima di scrivere il capitolo**: va spiegata, non solo inserita. Dai ai file nomi che dicono cosa mostrano (`mappa-ebstorf.png`).

Scarta logo, sfondi e decorazioni ripetute. Un'immagine di contenuto che non puoi usare va omessa e dichiarata nel riepilogo. Il testo dentro le immagini va trascritto, così la sintesi vocale può leggerlo.

## 2. Inventario dei contenuti

Questo passaggio protegge dalla perdita di concetti, il rischio principale di un adattamento. Prima di scrivere un capitolo, rileggi le sue fonti e crea `inventario/NN.txt`, con lo stesso numero del capitolo: una riga per ogni elemento da non perdere, scritta come dovrà comparire nel testo.

```
# 01: Il lato oscuro della traduzione
Venuti
invisibilità del traduttore
rough translation
1995
```

Includi concetti, termini tecnici, persone, opere, date, formule, esempi ed eccezioni. Dopo aver scritto il capitolo, controlla:

```bash
python3 -I <skill>/scripts/check_coverage.py <corso>/appunti
```

Lo script cerca ogni voce nella prosa, escludendo diagrammi e indici: un concetto presente solo in uno schema non basta. Trova le parole, non verifica la spiegazione, quindi rileggi anche le fonti accanto al capitolo.

## 3. Impianto e prova tecnica

```bash
cp -r <skill>/assets/template <corso>/appunti
```

1. In `main.tex` sostituisci i segnaposto `@@...@@` e attiva le lingue e le scritture che servono al corso (istruzioni nei commenti).
2. In `capitoli/00-prova.tex` aggiungi un campione delle scritture e dei simboli presenti nel materiale, poi compila:
   ```bash
   <skill>/scripts/compile.sh <corso>/appunti
   ```
   L'immagine TeX Live pesa circa 6 GB: se manca, lo script si ferma. Chiedi a Simone prima di rilanciarlo con `--pull`.
3. Guarda la pagina di prova e correggi il preambolo ora.
4. Togli la prova: cancella il file e la sua riga `\input` da `main.tex`. Il file mostra come si usano tutti gli ambienti: rileggilo prima di cancellarlo. `00-mappa-corso.tex`, `98-schede.tex` e `99-glossario.tex` rimandano ancora a `cap:prova`: i loro esempi vanno sostituiti al passo 6, e fino ad allora `check_latex.py` segnala quei `BROKEN REF`.

## 4. Impaginazione

Il template applica già font senza grazie, corpo 12, interlinea ampia, spaziatura tra lettere, testo allineato a sinistra, niente sillabazione, niente legature e sfondo crema. Tutto si regola nel blocco «Profilo di lettura» di `main.tex`, perché i DSA sono diversi tra loro: se Simone chiede un altro font, un'altra interlinea o uno sfondo bianco per la stampa, si cambia lì.

Non compromettere queste scelte nei capitoli:
- niente `\small`, `\footnotesize`, `\tiny`, note a piè di pagina, `\textit`, sottolineature o MAIUSCOLO esteso: rallentano la lettura. Il grassetto va sui termini chiave, solo la prima volta che compaiono in una sezione. `\emph` è già ridefinito senza corsivo, quindi si può usare per titoli e parole straniere;
- non usare font «per dislessici» come impostazione predefinita: le prove di un vantaggio sono deboli. Vanno bene se Simone li preferisce;
- il colore aiuta ma non basta: ogni riquadro e nodo porta anche un'etichetta scritta, così funziona in bianco e nero e per chi distingue male i colori.

## 5. Capitoli

Un capitolo per lezione o blocco di slide: `capitoli/NN-titolo.tex`, con `\chapter{...}\label{cap:...}`, aggiunto via `\input` in `main.tex`. Scrivi un capitolo alla volta e compila subito dopo.

### Struttura fissa di ogni capitolo

Una struttura sempre uguale permette di orientarsi senza rileggere e di sapere dove cercare.

1. `primadiiniziare`: di cosa parla, cosa bisogna ricordare (con rimandi), cosa si saprà fare alla fine.
2. `mappa`: mappa concettuale di tutto il capitolo.
3. Sezioni, nell'**ordine del materiale originale**, con titoli per argomento e mai «Slide N». Ogni sezione ha:
   - testo completo, con un'idea per paragrafo;
   - almeno uno schema o diagramma del concetto;
   - `parolesemplici` dopo citazioni o passaggi difficili;
   - `nonconfondere` dove due termini, nomi o procedure si somigliano;
   - `passoapasso` per ogni procedura o esempio numerico.
4. `daricordare`: i punti da non dimenticare, da 3 a 7.
5. `insintesi`: il filo del ragionamento in prosa.
6. `ripasso` con le domande, poi `risposte`, ciascuna con il rimando alla sezione. Sapere rispondere senza guardare fissa il contenuto meglio della rilettura.

### Scrittura

- **Spiega**: per ogni concetto dì cos'è, perché viene introdotto, a quale problema risponde e come si lega al resto.
- **Frasi**: una sola idea per frase, in forma attiva, con il soggetto esplicito. Evita incisi lunghi e doppie negazioni. Non comprimere una spiegazione lunga: dividila.
- **Paragrafi**: brevi, massimo 6-7 righe. Se un paragrafo contiene un elenco nascosto, usa un elenco vero.
- **Titoli**: descrittivi e frequenti, perché servono per ritrovare le informazioni. Ogni concetto importante ha una `\subsection`.
- **Riferimenti**: nomina sempre ciò di cui parli, senza contare su «quanto detto sopra» o «il primo dei due». Evita indicazioni come «a sinistra» e «a destra»: usa i nomi.
- **Sigle**: sciogli ogni sigla la prima volta che compare in ogni capitolo.
- **Nomi difficili e stranieri**: indica la pronuncia solo se ne sei sicuro, con un `\pron{...}` semplice alla prima occorrenza.
- **Rimandi**: `capitolo~\ref{cap:...}` verso i capitoli già visti, quando il legame è reale.
- **Indice**: `\aut{Cognome, Nome}` per autori e opere, `\idx{termine}` per i concetti.

### Numeri e formule

Questi accorgimenti aiutano soprattutto con la discalculia e non tolgono rigore:
- dopo ogni formula, una tabella `simboli` spiega ogni simbolo a parole e con la sua unità di misura;
- scrivi ogni passaggio dei calcoli, anche quelli ovvi, spiegando cosa cambia e perché;
- mantieni la formula originale: la lettura a parole si aggiunge;
- date e dati in sequenza vanno in una `cronologia`, oltre che nel testo;
- dai ai numeri lunghi la separazione in gruppi (`1\,000\,000`). Controlla i conti.

### Schemi e diagrammi

Ambienti: `schema` e `flusso`, con il titolo tra parentesi quadre; dentro, `tikzpicture` con gli stili già pronti (`concetto`, `dettaglio`, `esempio`, `processo`, `decisione`, `estremo`, `freccia`, `collega`, `etichetta`).

Scegli la forma in base a ciò che va mostrato:

| Il contenuto è | Forma |
|---|---|
| Un'idea con le sue parti | Mappa concettuale, con le frecce etichettate |
| Una procedura, un'argomentazione a passi, una causa con i suoi effetti | Diagramma di flusso |
| Un algoritmo o un caso con condizioni | Flusso con rombi `decisione` e rami sì/no |
| Più elementi con le stesse caratteristiche | Tabella di confronto |
| Una sequenza di date | `cronologia` |
| Una gerarchia o una classificazione | Albero |

Regole, tutte al servizio di uno schema che si legge davvero:
- **Mostra solo relazioni presenti nelle fonti.** Una freccia è un'affermazione: una causa o un collegamento inventati da te sono un errore di contenuto. Se vuoi proporre un legame tuo, dichiaralo nel testo come osservazione.
- **Massimo 7-9 nodi per schema.** Se servono di più, fai una mappa generale e uno schema per ogni parte: il contenuto non si taglia, si divide.
- **Parole brevi nei nodi, ma quelle vere**: i termini del corso, non sinonimi.
- **Ogni freccia in una mappa ha un'etichetta** che dice la relazione («causa», «è un tipo di»). Una freccia muta costringe a indovinare.
- **Una direzione di lettura**: dall'alto al basso o da sinistra a destra.
- **Stessi stili per gli stessi significati** in tutto il documento.
- **Dopo ogni schema, una frase lo racconta**, così il contenuto arriva anche con la sintesi vocale.
- Se un diagramma non aggiunge niente, non inserirlo per riempire: metti in quella sezione il commento `% nodiagramma: motivo`, che il controllo riconosce e che resta verificabile. Vale lo stesso per `% noflusso: motivo` a livello di capitolo.

**Guarda ogni diagramma renderizzato** prima di proseguire: testi fuori dai nodi e frecce sovrapposte non generano errori di compilazione.

### Immagini, tabelle e citazioni

- **Immagini**: `\figw{larghezza}{file}{didascalia}` o `\figh{altezza}{a,b}{didascalia}` nel punto da cui provengono, con una spiegazione.
- **Tabelle**: `booktabs` con `tabularx` e colonne `Y`, che vanno a capo senza sillabare; poche colonne e testi brevi. Se una tabella è troppo stretta, dividila.
- **Codice**: `lstlisting`, spiegando riga per riga ciò che conta.
- **Citazioni**: `\begin{cit}[lingua] ... \fontecit{(fonte)} \end{cit}`. Testo a fronte: `\afronte[lingua]{originale}{traduzione}`.
- **Trucchi per ricordare**: `permemoria`, solo se davvero utili. Vengono da te e non dal corso, e il riquadro lo dichiara.

### Fedeltà alle fonti

| Situazione | Segnale |
|---|---|
| Errore o incongruenza nel materiale | `correzione`: testo originale, correzione e motivo |
| Punto che le fonti non permettono di risolvere | `dubbio` |
| Spiegazione dal libro (`con libro`) | `dallibro`, con pagina verificata |
| Sezione senza slide, solo dagli appunti in classe | `\soloappunti` all'inizio |
| Conoscenza generale aggiunta da te | `\integrazione{...}` |

Applica queste regole:
- Non correggere mai in silenzio, e non presentare una tua conoscenza come se venisse dal corso. Se una correzione viene da te e non dalle fonti, dillo nel riquadro.
- `parolesemplici`, `permemoria` e le domande di ripasso sono tuoi: non attribuirli al docente e non presentare le domande come domande d'esame.
- Cita le lingue straniere esattamente come sono nel materiale. Se sani un refuso evidente, dichiaralo; se il dubbio è sostanziale, lascia il testo e usa `dubbio`.
- Non inventare ciò che manca: niente testi, traduzioni, date o riferimenti ricostruiti a memoria. Una traduzione tua va indicata come tale.
- Un nome che sembra scritto a orecchio negli appunti va riportato com'è, con la forma probabile in un `dubbio`.
- Non dedurre il genere di una persona dal nome: formula la frase in modo neutro, se le fonti non lo indicano.

## 6. Parti comuni

Con tutti i capitoli pronti:

1. `capitoli/00-mappa-corso.tex`: mappa generale del corso, un nodo per capitolo con i legami reali tra i capitoli, e una tabella capitolo-argomenti.
2. `capitoli/98-schede.tex`, schede da ripasso rapido, ciascuna con il rimando al capitolo. Tieni solo quelle utili al corso:
   - **Chi ha detto cosa**: persona, opera, idea, capitolo;
   - **Cronologia** generale;
   - **Formulario** con la spiegazione dei simboli;
   - **Parole da non confondere**, che raccoglie i riquadri `nonconfondere`;
   - **Procedure**: i diagrammi di flusso principali richiamati per nome.
3. `capitoli/99-glossario.tex` (salvo `solo capitoli`): una voce per concetto, in ordine alfabetico, con una definizione breve e il rimando al capitolo. Riassume senza aggiungere. Verifica che ogni voce concordi con il testo, comprese le correzioni fatte.
4. Adatta «Come leggere questi appunti» in `main.tex` ai segnali usati davvero.

## 7. Verifica

```bash
<skill>/scripts/compile.sh <corso>/appunti
python3 -I <skill>/scripts/check_latex.py <corso>/appunti
python3 -I <skill>/scripts/check_coverage.py <corso>/appunti
```

`check_latex.py` controlla le cose tecniche (immagini, rimandi, capitoli non inclusi, segnaposto, errori e caratteri mancanti nel log) e quelle di accessibilità (struttura di ogni capitolo, schema in ogni sezione, un flusso per capitolo, testo piccolo, corsivi, note a piè di pagina, paragrafi troppo lunghi). Correggi finché entrambi non riportano `problems: 0`, senza mai tagliare contenuti per farlo.

Lo script non vede tutto, quindi guarda anche il risultato:
1. renderizza tutte le pagine (`pdftoppm -r 40 -png main.pdf <scratchpad>/pg/p`), componile in fogli con `montage` e cerca figure tagliate, pagine vuote e tabelle rotte;
2. guarda da vicino (`-r 80`) **tutti** i diagrammi e le pagine con scritture non latine, testi a fronte e tabelle larghe;
3. rileggi le citazioni in lingua straniera confrontandole con il testo estratto;
4. prova la sintesi vocale in modo indiretto: `pdftotext main.pdf -` deve dare un testo scorrevole, senza parole spezzate né caratteri strani.

Se il PDF supera i 30 MB, segnalalo; riduci le immagini solo su richiesta: `magick mogrify -resize '1600x1600>' images/*.png`, poi ricompila.

## 8. Riepilogo per Simone

Breve e facile da scorrere, in italiano:
- cosa è stato creato: capitoli, pagine, numero di diagrammi, peso del PDF e percorso;
- l'esito di inventario e controlli;
- le correzioni principali e i dubbi da verificare, specie quelli che contano per l'esame;
- le scelte fatte senza chiedere: ordine, sezioni basate solo sugli appunti, sezioni senza diagramma e perché, immagini omesse, testi trascritti da immagini;
- cosa hai controllato davvero e cosa no.

Non fare commit: lo fa Simone, oppure lo fai tu se te lo chiede.
