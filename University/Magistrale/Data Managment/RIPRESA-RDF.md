# Riprendere lo studio di RDF su un altro computer

## Aggiornamento prioritario del 23 ottobre 2026

Questa sezione sostituisce il vecchio punto di ripresa del 16 ottobre riportato sotto. È un riepilogo della chat, non un transcript integrale.

Simone ha continuato SPARQL in chat: query di classe, variabili in soggetto e oggetto, più condizioni, risposte DB rispetto a RDFS e catene delle quattro regole. Evidenze e punti da verificare: `learning-records/0006-sparql-e-catene-rdfs.md`. Restano reificazione e un Problem 5 completo prima di chiudere il blocco prioritario della 03.

01 e 02 sono già studiate; 04 è da fare. Esame 28 ottobre, 27 simulazioni; 25–26 disponibili tutto il giorno. Il 24 viaggio per Napoli e festa nel pomeriggio. Non basare il recupero sullo studio in viaggio. Piano aggiornato in NOTES.md.

### Prompt per la sessione vocale del 24 ottobre

> Sto preparando Data Management per il 28 ottobre. Oggi voglio una lezione solo orale sulla nota 05: transazioni e anomalie della concorrenza. Sto guidando: niente schermo, grafi, formule, notazione di schedule o calcoli. Spiega in italiano un concetto per volta, con interventi brevi ed esempi semplici di due persone che operano sullo stesso conto o prenotazione. Introduci transazione, commit, rollback e isolamento, poi lost update, dirty read e lettura non ripetibile. Fammi una domanda breve per volta e aspetta la risposta; correggimi subito. Parti da zero sulla 05, senza dare per acquisite le spiegazioni di oggi. Se chiedo una pausa, fermati. La priorità resta la guida. Alla fine riassumi cosa ho dimostrato di capire e cosa riprendere da fermo. Se hai accesso alla repository, leggi prima NOTES.md e la nota 05; non fingere di averli letti se non puoi accedervi.

### Ripresa successiva da fermo

Usare `.claude/skills/teach/SKILL.md` nella radice della repository, leggere NOTES.md e learning-records. Verificare ciò che è stato effettivamente affrontato in voce. Completare reificazione e Problem 5, poi studiare la 05 con esercizi scritti di conflitti, grafo delle precedenze e recuperabilità.

Aggiornato il 16 ottobre 2026. Questo è un riepilogo didattico, non un'esportazione completa della conversazione.

## Prompt da incollare nella nuova chat

> Usa la skill teach in `.claude/skills/teach/SKILL.md` nella radice della repository. La cartella di studio è `University/Magistrale/Data Managment`. Leggi `RIPRESA-RDF.md`, `MISSION.md`, `NOTES.md` e `learning-records/` in questa cartella. Sto studiando RDF per capire le slide e svolgere gli esercizi di Data Management. Riprendi dall'esercizio sull'amicizia con data, chiedendomi di scrivere le triple prima di mostrare la soluzione. Spiega in italiano, un passo alla volta, con feedback sugli errori.

## Obiettivo e materiale

- Obiettivo confermato: capire le slide e risolvere gli esercizi del corso.
- Nota principale: `03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs.md`.
- Slide: `Slides Lenzerini/3-GraphDatabases.pdf`.
- Lezione interattiva: `lessons/0001-rdf-dalle-frasi-alle-triple.html`, apribile direttamente nel browser. CSS e JavaScript sono incorporati: la correzione funziona anche con il solo HTML.
- Scheda: `reference/rdf-primi-passi.html`; copiare anche `assets/` per il suo stile e per mantenere i sorgenti della lezione.
- Stato didattico: `MISSION.md`, `RESOURCES.md`, `NOTES.md`, `learning-records/`.

## Comprensione dimostrata

Simone ha scritto correttamente:

```turtle
:John :isFriendOf :Mary .
:Mary :name "Mary" .
:Mary rdf:type :Person .
```

Ha trasferito la distinzione persona/nome a `:Ann :knows :John .` e `:Ann :name "Anna" .`, spiegando che una IRI identifica la persona e la stringa ne esprime il nome.

Ha riconosciuto quattro triple distinte in un elenco di cinque con una tripla duplicata: comprende l'unicità della tripla completa, senza unicità del predicato. È stato spiegato che due nomi diversi possono coesistere e che aggiungere una tripla non sostituisce automaticamente la precedente.

## Blank node: esercizi e punti da consolidare

Ha usato lo stesso blank node per tre informazioni collegate. Ha spiegato correttamente che `:Mary` collega alla persona e non alla stringa `"Mary"`.

Errori già corretti: `:x` invece di `_:x`; `feaf:` invece di `foaf:`; uso di `knows` per esprimere il nome; `rdf:Person` invece di `:Person` o `foaf:Person`. Quest'ultimo caso richiede un breve richiamo ai vocabolari.

È stato chiarito che scegliere una IRI o un blank node è una decisione di modellazione: si può assegnare una IRI anche a una persona di cui si sa poco; il blank node esprime qualcosa senza nominarlo globalmente. Non verificare la comprensione soltanto chiedendo di ripetere questa definizione.

## Punto preciso da cui continuare

È stata appena introdotta la rappresentazione di un'amicizia come risorsa, per collegarle una data. Esempio già mostrato:

```turtle
_:friendship1 rdf:type :Friendship .
_:friendship1 :participant :Mary .
_:friendship1 :participant :Ann .
_:friendship1 :since "2019-03-12"^^xsd:date .
```

Il blank node rappresenta l'amicizia, non una persona. Le proprietà del namespace `:` sono scelte per l'esercizio. Il pattern non implica automaticamente la tripla binaria `:Mary :isFriendOf :Ann .`.

**Esercizio assegnato e ancora senza risposta:** «John è amico di Mary dal 1º giugno 2020». Scrivere quattro triple con un unico blank node per l'amicizia e i termini `rdf:type`, `:Friendship`, `:participant`, `:since`, `xsd:date`. Assumere i prefissi già dichiarati. Non mostrare subito la soluzione.

## Trasferimento dei file

Copiare la cartella del corso con il contenuto aggiornato e la cartella `.claude/skills/teach/` dalla radice della repository, inclusi i file di formato. Una copia completa della repository include entrambi. Chat e filesystem sono separati: il riepilogo consente di riprendere senza trasferire l'intero transcript.

Su Windows verificare che `.agents/skills` sia realmente un collegamento funzionante prima di fare affidamento sul rilevamento automatico. In alternativa indicare esplicitamente il percorso della skill come nel prompt sopra. Non occorre cambiare gli esempi RDF per i diversi percorsi del computer.
