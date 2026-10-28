# Preferenze e contesto didattico

- Obiettivo confermato: capire le slide e svolgere gli esercizi di Data Management.
- Simone chiede spiegazioni concrete e progressive; ha richiesto esplicitamente introduzione ed esercizi RDF con la skill teach.
- Simone ha dichiarato di essere DSA e di preferire immagini esplicative: usare esempi coerenti, tabelle e schemi visivi per affiancare le spiegazioni; evitare di dedurre ulteriori esigenze non espresse.
- Nella conversazione ha distinto l'identificazione con IRI dal recupero di una pagina; verificare il trasferimento di questa intuizione agli esercizi, senza presumere padronanza completa.
- Nel tentativo sull'amicizia con data ha introdotto spontaneamente un blank node, ma ha confuso persona e relazione e usato proprietà FOAF non definite. Riprendere dopo il consolidamento delle triple.
- Prima lezione: lessons/0001-rdf-dalle-frasi-alle-triple.html. Simone ha completato correttamente l'esercizio scritto e quello di trasferimento su Ann: vedi learning-records/0001-iri-e-literal-nelle-triple.md. Da verificare la distinzione tra proprietà presenti e tipo dichiarato o dedotto.
- I risultati nella pagina restano in memoria finché aperta. La pagina non invia risposte all'agente: chiedere a Simone di riportare il risultato o le triple per adattare la lezione successiva.
- La lezione HTML incorpora CSS e JavaScript per funzionare anche come file singolo. Dopo modifiche agli asset condivisi eseguire `python3 -I assets/build-rdf-lesson.py`; non modificare manualmente le copie incorporate.

## 21 ottobre 2026: sprint verso l'esame
- Esame il 28/10; il 27 prove d'esame; entro il 26 tutte le note. Simone vuole accelerare ed è frustrato da SPARQL: lezioni brevi, mirate a quello che chiedono gli esami, niente giri larghi.
- Ha rifiutato il questionario a scelta multipla e ha risposto in chat: fare domande brevi in testo.
- Struttura degli appelli (giugno A/B, luglio, settembre): P1–P2 concurrency (nota 05), P3–P4 costi I/O (note 06–08), P5 option 1 = RDF/RDFS + SPARQL (giu A/B, set con property graph) oppure DW (lug). Document DB (nota 04) mai comparsa.
- Lezione 02: lessons/0002-sparql-per-il-problem-5.html (query di classe, DB answer vs certain answer, 4 regole IBC, trappola reificazione). Prossima: 5.1, costruire G dal testo.
- Lezione 02 usa assets/quiz.js (quiz generico + correttore query di classe). Build: `python3 -I assets/build-rdf-lesson.py lessons/0002-sparql-per-il-problem-5.html assets/quiz.js`.

## 23 ottobre 2026: stato e disponibilità confermati
- 01 e 02 già studiate (profondità non verificata); 03 in corso; 04 non ancora studiata. La pianificazione tratta 05–08 come da affrontare, senza una verifica preliminare della preparazione.
- SPARQL: vedere learning-records/0006-sparql-e-catene-rdfs.md. Prossimo lavoro scritto: reificazione e Problem 5 completo, poi priorità alla 05.
- Disponibilità dichiarata: il 23 fino alle 21; il 24 viaggio per Napoli e festa del cugino nel pomeriggio; il 25 e 26 tutto il giorno. Il 24 non deve sostenere attività indispensabili del piano.
- Piano concordato indicativo: 25 mattina 05, pomeriggio 04 (circa due ore) e 06; 26 note 07–08; 27 simulazione, correzione e ripasso mirato 01–02. Piano serrato da adattare alle prestazioni effettive.
- Per il viaggio del 24: argomento consigliato = nota 05, transazioni e anomalie della concorrenza, con esempi orali brevi. Non richiedere lettura dello schermo, notazione di schedule, grafi o calcoli mentre guida. Preparare la lezione scritta su serializzabilità in una sessione da fermo.
- Handoff aggiornato: RIPRESA-RDF.md, sezione iniziale del 23 ottobre; il vecchio esercizio sull'amicizia più sotto è storico e già superato.

## 25 ottobre 2026: nota 05 (Concurrency)
- Simone ha chiesto con /teach di studiare la nota 05 e di ritrovare il piano verso l'esame. Stava rivedendo le prime sezioni (5.1, schedule).
- Piano: oggi lezioni 03 precedence graph → 04 2PL X e S/X → 05 strict/rigorous → 06 timestamp scheduler; 26 note 06–08; 27 appelli a tempo.
- Lezione 03: lessons/0003-conflict-serializability-precedence-graph.html. Usa assets/quiz.js + assets/schedule.js (parser, conflitti, precedence graph SVG, generatore casuale bilanciato ciclico/aciclico; widget `.sched-drill`). Build: `python3 -I assets/build-rdf-lesson.py lessons/0003-....html assets/quiz.js assets/schedule.js` (ora accetta più script).
- Scheda: reference/concurrency-esame.html, da estendere a ogni lezione 04–06 (CSS incorporato a mano: reincorporarlo se cambia teaching.css).
- schedule.js è pensato per riuso: per 2PL/strict aggiungere funzioni nello stesso modulo invece di nuovi parser.

## 25 ottobre 2026: ansia e concentrazione
- Simone riferisce un'ansia bloccante: si distrae e controlla di continuo il proprio rendimento, e non riesce a entrare in concentrazione.
- Quindi: niente contatori, serie da completare o punteggi nelle lezioni; blocchi brevi con un solo compito chiaro; feedback sul metodo, non sul rendimento; non mettere in primo piano il conto alla rovescia verso l'esame. Esercizi anche in chat, uno alla volta, se lo preferisce.

## 26 ottobre 2026, pomeriggio

- Lezione 03 completata bene (anche lo schedule casuale). Alle 15:42 si passa alla lezione 04 (2PL, P2.2).
- `schedule.js` ora ha anche `twoPL(S, shared)` (backtracking sui lock point, restituisce lo schedule con i lock o il motivo) e il widget `.tpl-drill[data-schedule|data-random]`. Il generatore `random2PL` dà no/no, no/sì, sì/sì con la stessa probabilità.
- La scheda `reference/concurrency-esame.html` ha la sezione 2PL.
- Dopo la 04: costi di I/O (note 06–08, P3–P4). Strict/rigorous (05) e timestamp (06) stasera o domattina.

## 27 ottobre 2026

- 2PL fatto in chat (Simone non riusciva a leggere), poi pagine `0004b` (ripasso dalla chat) e `0004c` (8 esercizi + casuali): fatti.
- Bug corretto in `quiz.js`: il feedback finiva nella prima opzione (anche lei ha `data-feedback`); ora `div[data-feedback]`. Ricompilate 0002–0004.
- Lezione 05 strict/rigorous con `assets/recovery.js` (checker con commit mancanti inseriti dopo l'ultima azione, widget `.rec-drill`). Build: `python3 -I assets/build-rdf-lesson.py lessons/0005-strict-e-rigorous.html assets/quiz.js assets/recovery.js`.
- Simone dice che fare esercizi giusti lo fa sentire più sveglio: puntare su esercizi subito, poca lettura.
