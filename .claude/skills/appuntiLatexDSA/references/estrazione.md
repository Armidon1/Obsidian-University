# Estrazione mirata delle fonti

Leggi questa guida quando lavori da fonti grezze o devi recuperare una parte mancante dagli appunti rielaborati. `<skill>` indica la cartella della skill corrente.

Per PDF nuovi, lancia:

```bash
python3 -I <skill>/scripts/survey_pdfs.py <scratchpad>/survey <file.pdf> [...]
```

Leggi il testo in `txt/`, guarda le miniature e tutti i fogli `sheet-*.png` prodotti per le fonti da elaborare. Le pagine con poco testo e molte immagini possono contenere testo non riconosciuto da `pdftotext`. Il sopralluogo ricostruisce la copertura del materiale, non vincola l'indice del libro all'ordine delle pagine.

- Testo di slide: `pdftotext -layout -f N -l N file.pdf -`.
- Figure raster: `pdfimages -png -f N -l N file.pdf <out>/LNN-PP`.
- Figure vettoriali o frammentate: renderizza con `pdftoppm -r 170 -png -f N -l N file.pdf <out>/LNN`, poi usa `python3 -I <skill>/scripts/slide_crops.py <out>/crops <pagina.png> [...]`. Controlla i ritagli: lo script può includere blocchi di testo o fondere più figure. Per un ritaglio manuale: `magick pagina.png -crop LxA+X+Y +repage -trim uscita.png`.
- Libro o dispensa: individua i capitoli e verifica le pagine usate. Per le figure: `python3 -I <skill>/scripts/pdf_figures.py file.pdf <out> SIGLA [prima] [ultima]`; `--bands` aiuta con quelle senza didascalia.
- DOCX: `python3 -I <skill>/scripts/extract_docx.py file.docx <out> SIGLA-LNN`; il testo contiene marcatori `[IMG nome]`.
- PPTX: usa gli strumenti o una skill per presentazioni se disponibili; altrimenti estrai il contenuto con gli strumenti locali e verifica i render delle slide, dichiarando eventuali limiti.

Componi fogli di contatto dei ritagli, per esempio:

```bash
montage -label '%f' *.png -tile 8x -geometry 220x220+3+3 -pointsize 10 <scratchpad>/foglio.png
```

Guarda ogni figura prima di usarla e registrane provenienza e contenuto nella matrice. Usa nomi descrittivi; conserva i nomi originali dei file personali quando lavori direttamente sugli appunti esistenti. In una nuova cartella di output le copie possono avere nomi nuovi, purché la corrispondenza sia tracciabile. Scarta decorazioni e duplicati grafici; dichiara omissioni informative. Mantieni le copie non utilizzate e i file intermedi nella scratchpad.

In modalità da appunti rielaborati, riusa estrazioni e spiegazioni esistenti. Un rinvio a una pagina del libro già contenuto negli appunti conserva quella provenienza; non dichiarare di aver verificato personalmente la pagina senza averla consultata.
