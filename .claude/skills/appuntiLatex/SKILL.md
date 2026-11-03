---
name: appuntiLatex
description: "Progetta un libro universitario organico in LaTeX e PDF da slide, dispense, libri o appunti già rielaborati: contenuti completi, capitoli per argomento, copertura delle fonti, figure spiegate, glossario e indice. Usare per appunti LaTeX/PDF standard, anche da integrare; per Obsidian usare appunti e per esigenze DSA appuntiLatexDSA."
---

# /appuntiLatex — libro di studio organico in LaTeX e PDF

## Risultato e principio editoriale

Produci un **libro di studio organico e autonomo**, che si possa leggere dall'inizio alla fine senza dover aprire le slide. Conserva la conoscenza delle fonti e scegli la forma più utile per comprenderla.

**Completezza sostanziale, libertà di scrittura.** Mantieni concetti, passaggi del ragionamento, condizioni, distinzioni, esempi, formule, eccezioni, dati e riferimenti. Puoi riscrivere, spostare e accorpare spiegazioni ed eliminare duplicazioni. Quando fondi due fonti, conserva le rispettive precisazioni e provenienze. La fedeltà non richiede di ripetere ogni frase o ogni occorrenza dello stesso concetto. Lunghezza e numero di diagrammi non sono obiettivi; non comprimere il ragionamento per risparmiare pagine.

Le citazioni restano integrali e fedeli. Identificatori, nomi propri, valori, formule e listati mantengono la precisione necessaria. Conserva le annotazioni personali riconoscibili e con la formulazione originale, in un riquadro, in una sezione dedicata o in appendice; non mescolarle senza segnale alla trattazione verificata.

## Modalità e ambito

Senza argomenti lavora sulla cartella corrente. Opzioni utili: `da appunti già rielaborati`, `ordine delle lezioni`, `solo capitoli`, `con libro <file>`, `appunti classe <file>`. Rispetta eventuali richieste diverse dell'utente.

- **Libro organico (predefinita):** capitoli per argomenti e prerequisiti, anche accorpando più lezioni o separando una lezione molto eterogenea.
- **Da appunti già rielaborati:** usa gli appunti esistenti come fonte primaria e riusa testo, figure e correzioni valide. Concentra il lavoro su indice, integrazione, collegamenti, eliminazione delle ripetizioni e impaginazione. Non rifare automaticamente tutta l'estrazione dei PDF o una nuova integrazione del libro: consulta gli originali in modo mirato per lacune, figure o incongruenze, dichiarando ciò che hai verificato.
- **Ordine delle lezioni:** mantieni l'ordine originale quando richiesto o necessario per il contenuto; conserva comunque titoli per argomento e rimandi fra temi ripetuti.
- **Integrazione di un volume esistente:** leggi le modifiche presenti e conserva le personalizzazioni. Non rigenerare indiscriminatamente i capitoli.

Il risultato va in `appunti/`: `main.tex`, `capitoli/`, `images/`, `inventario/`, `main.pdf`. In `images/` conserva soltanto figure incluse nel volume. Tieni estratti, ritagli di prova e render nella scratchpad. Esegui gli script Python con `python3 -I`.

## 1. Ricognizione e progetto del libro

1. Leggi le istruzioni della cartella, elenca le fonti e stabiliscine il ruolo: materiale del docente, libro richiesto, appunti rielaborati, annotazioni personali, laboratori. Mantieni la lingua già usata nel corso, salvo richiesta diversa.
2. Se `appunti/` esiste, verifica l'autorizzazione già data: integra quando è quanto richiesto, proteggendo le modifiche personali. Se l'utente non ha indicato come trattare un volume esistente, chiarisci prima di sovrascriverlo.
3. Individua prerequisiti, idee centrali, sovrapposizioni, esempi e applicazioni. Scrivi in `inventario/struttura.md` l'indice ragionato: obiettivo e prerequisiti di ciascun capitolo, fonti associate, collocazione di laboratori e annotazioni, motivi dei principali accorpamenti. Procedi senza richiedere un'approvazione intermedia se l'ambito è chiaro.
4. Prepara `inventario/copertura.json`: per ogni contenuto sostanziale registra fonti e destinazioni previste. Leggi [references/copertura.md](references/copertura.md) per formato e verifica. La matrice consente di spostare o distribuire un concetto fra capitoli; non obbliga a usare le stesse parole.
5. Per fonti grezze o parti da estrarre, segui [references/estrazione.md](references/estrazione.md). Nella modalità da appunti rielaborati limita il sopralluogo ai materiali che servono effettivamente.

Chiedi chiarimenti soltanto quando lingua, ambito del libro o contraddizioni fra fonti cambiano materialmente il risultato e il contesto non li risolve. Non ricostruire a memoria una parte mancante.

## 2. Impianto e campione

Copia `assets/template/` nella nuova cartella di output, sostituisci i segnaposto `@@...@@` e configura lingua, docente e università. In un volume esistente adatta il preambolo senza sostituirlo in blocco.

Usa `capitoli/00-prova.tex` come campionario tecnico, non come struttura obbligatoria dei capitoli. Prova caratteri, formule, codice, una figura, una tabella e un diagramma rappresentativi dei materiali effettivi. Compila e guarda il campione prima di estendere il volume:

```bash
<skill>/scripts/compile.sh <corso>/appunti
```

Lo script usa LuaLaTeX/latexmk locali oppure un contenitore TeX Live. Se manca l'immagine, pesa circa 6 GB: chiedi prima di scaricarla con `--pull`. Dopo la prova rimuovi il file dimostrativo e il suo `\input`. Sostituisci o rimuovi anche i file comuni dimostrativi e i loro rimandi a `cap:prova`; non lasciare capitoli inutilizzati nella consegna.

Progetta poi un primo capitolo rappresentativo con la struttura editoriale scelta e controllane la resa. L'orientamento dato dal template non sostituisce il progetto del libro.

## 3. Scrittura e struttura

Usa `capitoli/NN-titolo.tex`, con `\chapter{...}\label{cap:...}`, e includi i file da `main.tex`. Scrivi per unità coerenti e compila dopo cambiamenti significativi, mantenendo localizzabili gli errori.

- Apri un capitolo con un orientamento breve: domanda centrale, prerequisiti e collegamento al percorso. Sviluppa prima ciò che serve per capire ciò che segue.
- Ogni concetto va spiegato: che cos'è, perché serve, quali condizioni e limiti ha, come si collega al resto. Rendi espliciti i passaggi impliciti senza inventare nuovi argomenti del corso.
- Usa sezioni descrittive e paragrafi focalizzati. Non creare una sottosezione, un riquadro o una figura per ogni termine tecnico.
- Chiudi con una sintesi o con punti da ricordare; usa entrambi soltanto quando svolgono funzioni diverse. Le domande di recupero e le risposte con rimandi sono utili dove verificano una comprensione concreta, e non sono domande d'esame.
- Riunisci una spiegazione ripetuta in una sede principale e richiamala altrove. Mantieni vicino all'uso le informazioni indispensabili per seguire il passaggio; evita continui salti fra capitoli.
- Le sigle si sciolgono alla prima occorrenza del capitolo. I rimandi reali usano etichette stabili; colloca `\idx{termine}` e `\aut{Cognome, Nome}` dove si spiega il contenuto, evitando di indicizzare automaticamente ogni titolo o domanda del laboratorio.

Adatta le unità al materiale:

| Unità | Elementi utili |
| --- | --- |
| Concetto | Definizione, problema, relazioni, esempio, condizioni e limiti |
| Procedura | Obiettivo, prerequisiti, passi, risultato atteso, errori o casi di fallimento |
| Codice o algoritmo | Listato, spiegazione delle parti decisive, stato iniziale/finale e condizioni |
| Strumento | Domanda a cui risponde, dati osservabili, interpretazione e limiti |
| Laboratorio | Consegna, metodo, osservazioni, interpretazioni, risultati verificati e questioni aperte |

Colloca laboratori ed esercizi in una parte autonoma o in appendice quando interrompono il percorso teorico; usa rimandi ai capitoli pertinenti. Un suggerimento dell'esercitazione non diventa un risultato osservato. Un file derivato dall'analista non diventa un artefatto prodotto dal campione.

## 4. Figure, schemi, tabelle e codice

Ogni elemento aggiunto deve aiutare a **capire, ricordare o ritrovare** un'informazione. Usa una mappa per relazioni fra concetti, un flusso per una procedura o una decisione, una tabella per confronti omogenei e una cronologia per date pertinenti. Evita mappe che elencano soltanto i titoli e flussi che fanno sembrare sequenziali attività indipendenti.

Non esiste un minimo di diagrammi per sezione o capitolo. Non inserire riempitivi o commenti di esenzione per soddisfare un controllo numerico. Dividi gli schemi troppo densi anziché ridurre il testo a dimensioni illeggibili. Etichetta le relazioni e i rami delle decisioni; usa solo relazioni sostenute dalle fonti. Accompagna ogni schema con una spiegazione in prosa. Guarda i diagrammi renderizzati: compilare senza errori non esclude sovrapposizioni.

- **Figure:** `\figw{larghezza}{file}{didascalia}` o `\figh{altezza}{a,b}{didascalia}`. La didascalia identifica il contenuto e la provenienza; la prosa ne spiega la funzione. Puoi accorpare copie della stessa figura conservando i riferimenti alle fonti. Dichiara omissioni di contenuti non ridondanti e immagini illeggibili.
- **Testo nelle figure:** rendi disponibili come testo i contenuti necessari per lo studio, inclusi identificatori, valori e passaggi decisivi del codice. Non trascrivere decorazioni o ogni elemento irrilevante dell'interfaccia. Nella modalità da appunti rielaborati riusa le trascrizioni esistenti e integra ciò che manca; distingui spiegazione e trascrizione integrale.
- **Tabelle:** `booktabs` e colonne `Y` di `tabularx`, oppure `longtable` con colonne `>{\RaggedRight\arraybackslash}p{...}`. Le celle vanno a capo senza giustificazione forzata; le tabelle multipagina ripetono l'intestazione. Dividi confronti troppo larghi mantenendo intestazioni e informazioni.
- **Codice:** il template mantiene `lstlisting` come ambiente letterale con andata a capo anche per percorsi lunghi. Nel codice in linea preserva gli spazi fra istruzioni e operandi: usa per esempio `\texttt{mov eax, [ebx+4]}` con l'escaping LaTeX necessario. `\url` e `\nolinkurl` sono per indirizzi, non per istruzioni con spazi. Verifica anche il testo estratto dal PDF.
- **Formule:** conserva la notazione e controlla i conti; spiega simboli, unità, ipotesi e passaggi necessari nel punto di utilizzo. Definizioni condivise possono accompagnare un gruppo coerente di formule.

## 5. Fedeltà e provenienza

| Situazione | Segnale |
| --- | --- |
| Errore o incongruenza del materiale | `correzione`: originale, correzione e motivo |
| Punto irrisolto | `dubbio`: cosa manca e cosa verificare |
| Integrazione richiesta dal libro | `dallibro`, con pagina verificata |
| Contenuto ricostruito soltanto da appunti in classe | `\soloappunti` nella parte interessata |
| Conoscenza generale aggiunta oltre le fonti | `\integrazione{...}` |

Non correggere in silenzio. Mantieni le correzioni e i dubbi già segnalati, verificando che glossario, schemi e ripasso concordino con essi. Un accorpamento non risolve una contraddizione fra fonti. Non attribuire al docente inferenze, traduzioni o domande aggiunte dall'autore degli appunti. Conserva citazioni e lingue straniere con precisione; indica le traduzioni proprie. Per nomi trascritti a orecchio, conserva la forma originale e segnala quella probabile come dubbio. Non dedurre il genere di una persona dal nome.

Citazioni: `\begin{cit}[lingua] ... \fontecit{(fonte)} \end{cit}`. Testo a fronte: `\afronte[lingua]{originale}{traduzione}`.

## 6. Parti comuni e copertura

Salvo `solo capitoli`, prepara un glossario alfabetico dei concetti utili a orientarsi nel corso, con definizioni coerenti e rimandi alla spiegazione principale. L'indice analitico deve aiutare la ricerca, senza diventare un secondo sommario.

Una mappa generale è utile se mostra relazioni fra i temi; una tabella capitoli/argomenti può già bastare per l'orientamento. Schede di ripasso, formulario, cronologia e confronti finali vanno selezionati per utilità, evitando di ricopiare tutti i riepiloghi.

Aggiorna la matrice di copertura durante la scrittura. Verifica ogni voce leggendo fonte e destinazione: completezza del ragionamento, condizioni, esempi ed eventuali dubbi. Registra l'esito e una nota concreta. La ricerca letterale resta un ausilio per identificatori, dati e citazioni, non una prova automatica di comprensione o correttezza.

Adatta «Come leggere questi appunti» ai segnali e alle parti presenti davvero.

## 7. Verifica e consegna

```bash
<skill>/scripts/compile.sh <corso>/appunti
python3 -I <skill>/scripts/check_latex.py <corso>/appunti
python3 -I <skill>/scripts/check_coverage.py <corso>/appunti
```

Correggi gli errori tecnici e le lacune di copertura fino a `problems: 0`. Lo script di copertura valida la matrice e i riscontri dichiarati: non sostituisce il confronto editoriale. Gli eventuali inventari numerati `.txt` restano compatibili per i volumi precedenti.

Separa i controlli tecnici dalla revisione didattica: cerca prerequisiti mancanti, ripetizioni, attribuzioni confuse, mappe senza utilità e passaggi compressi. Gli avvisi editoriali richiedono giudizio, non materiale aggiunto per far sparire un numero.

Renderizza tutte le pagine (`pdftoppm -r 40 -png main.pdf <scratchpad>/pg/p`), componi fogli di contatto e cerca pagine vuote, tagli e tabelle spezzate male. Controlla a 80 dpi diagrammi, tabelle dense, codice, scritture non latine e testi a fronte. Confronta citazioni e valori sensibili con le fonti. Estrai il testo con `pdftotext`: verifica caratteri, ordine di lettura, spazi del codice e formule rappresentative. L'estrazione è un controllo indiretto, non una certificazione di accessibilità del PDF.

Se il PDF supera 30 MB, segnalalo; non ricomprimere automaticamente le immagini. Riducile se richiesto, poi ricompila e ricontrolla.

Consegna un riepilogo breve in italiano: percorsi di PDF e sorgenti, capitoli/pagine/peso, scelte di organizzazione e accorpamento, esiti tecnici e copertura, correzioni e dubbi importanti, immagini omesse o trascritte, verifiche svolte e limiti. Distingui materiale riutilizzato da nuove verifiche delle fonti. Non fare commit salvo richiesta esplicita.
