# SPARQL e catene di inferenza RDFS

Il 23 ottobre Simone ha scritto query SPARQL con variabili in soggetto e oggetto e più condizioni sulla stessa variabile, e distinto correttamente risposte su graph database e RDFS Knowledge Graph. Ha giustificato autonomamente catene subPropertyOf → domain → subClassOf e riconosciuto che la condizione di tipo Person è ridondante quando worksOn ha dominio Worker e Worker è sottoclasse di Person.

Ha inizialmente confuso range con domain, poi identificato correttamente entrambi gli oggetti come Course e trasferito la regola a Project; verificare nuovamente a distanza. Corretti i refusi rd:type e SELECT ?x AS courses; spiegato che la mancanza di una tripla non dimostra la falsità del fatto, ma quest'ultimo punto non è ancora stato verificato autonomamente. Restano reificazione e un Problem 5 completo; non considerare acquisita tutta la nota 03.
