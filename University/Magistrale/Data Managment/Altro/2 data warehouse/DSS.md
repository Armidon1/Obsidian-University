**DSS = Decision Support System** (Sistema di Supporto alle Decisioni): un sistema informativo pensato non per registrare le operazioni quotidiane, ma per aiutare il management a prendere decisioni tattiche e strategiche analizzando grandi quantità di dati storici.

Nel contesto dei data warehouse (**DW**) il legame è diretto: il DW è l'infrastruttura dati che alimenta i DSS. La definizione classica di Inmon lo dice esplicitamente — una collezione di dati integrata, orientata al soggetto, variabile nel tempo e non volatile, costruita _a supporto dei processi decisionali_.

**Il contrasto con i sistemi operazionali (OLTP)**

| |OLTP|DSS / OLAP|
|---|---|---|
|Carico di lavoro|transazioni brevi e frequenti|poche query complesse|
|Record toccati|pochi, per accesso|milioni, con aggregazioni|
|Dati|correnti, aggiornati in tempo reale|storici, caricati in batch|
|Operazioni|lettura + scrittura|prevalentemente sola lettura|
|Schema|normalizzato (3NF)|denormalizzato (star / snowflake)|
|Metrica di ottimizzazione|throughput, concorrenza|tempo di risposta della singola query|

**Perché servono database separati**

Questa è la motivazione centrale per cui esiste il data warehouse. Far girare query decisionali (es. "fatturato per regione e categoria prodotto negli ultimi 5 anni") direttamente sul database transazionale sarebbe un disastro: quelle query scansionano tabelle intere e bloccherebbero le transazioni operative, degradando le performance del sistema di produzione. In più i dati operazionali sono sparsi su fonti eterogenee, vengono sovrascritti (perdendo la storia) e spesso hanno codifiche incoerenti.

Da qui l'architettura tipica: sorgenti operazionali → **ETL** (estrazione, pulizia, trasformazione, integrazione) → data warehouse → data mart → strumenti di front-end (OLAP, reporting, dashboard, data mining).

**Nota terminologica**

Vedrai spesso "DSS" usato anche come sinonimo del _tipo di carico di lavoro_ più che del sistema: si parla di "query DSS" per intendere query analitiche pesanti. È il senso in cui compare, per esempio, nei benchmark TPC-H e TPC-DS.