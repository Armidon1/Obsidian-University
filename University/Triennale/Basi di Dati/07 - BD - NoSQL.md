---
title: Modelli e Sistemi NoSQL
aliases:
  - BD — Modelli e Sistemi NoSQL
tags:
  - basi-di-dati
  - nosql
  - mongodb
  - json
  - graph-database
source: 7-NoSQL.pdf
---

# Modelli e Sistemi NoSQL

> [!abstract]
> Ultima parte del corso: i DBMS **non basati sul modello relazionale**. Tre sezioni:
> 1. **introduzione ai sistemi NoSQL**: cosa significa il termine, le proprietà tipiche, i modelli logici (chiave/valore, documenti, colonne, grafi);
> 2. **document-oriented database**: **MongoDB**, i documenti JSON, le operazioni CRUD, `find` e il confronto con [[03 - BD - SQL|SQL]], le correlazioni tra collezioni e `$lookup`;
> 3. **graph database**: nodi e archi etichettati, confronto con le basi relazionali (amici e amici degli amici), **regular path query**.
>
> Il confronto costante è con il [[02 - BD - Modello Relazionale|modello relazionale]]: rigidità dello schema, join, proprietà [[03 - BD - SQL#Transazioni|ACID]]. Una parte delle slide si basa sul materiale del prof. Marco Di Felice (Università di Bologna). Il corso magistrale riprende i grafi in [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs]].
>
> Indice dei concetti: [[MOC - Basi di Dati]].

---

## 7.1 Introduzione ai sistemi NoSQL

Vedi [[NoSQL]].

**NoSQL** è un movimento che promuove l'adozione di DBMS **non basati sul modello relazionale**.
- Il termine compare per la prima volta in una pubblicazione del 1998.
- Oggi si intende per lo più come **"Not Only SQL"** (annotazione: "fanno cose NoSQL").
- Definizione di nosql-database.org: *"Next generation databases mostly addressing some of the points: being non-relational, distributed, open source and horizontally scalable"*.

**Proprietà tipiche** (annotazione: "in realtà si può avere anche con SQL tutto"):

| Proprietà | Significato |
|---|---|
| **distribuiti** | i dati stanno su più macchine |
| **scalabili orizzontalmente** | si aumenta la capacità aggiungendo macchine, non potenziandone una |
| **enormi moli di dati** | progettati per i *big data* |
| **repliche** | i dati sono copiati su più nodi |
| **open source** | in generale |
| schema **non necessariamente** presente | annotazione: "questo è senza: il relazionale invece è rigido" |
| tipicamente **niente join** | |
| tipicamente **niente ACID** | annotazione: "non tutte le applicazioni richiedono l'ACID → sacrifico il join per guadagnare in flessibilità" |

Annotazione in fondo: la rigidità di SQL permette di fare operazioni (compreso il join) **perfette**. Le proprietà mancanti sono il prezzo pagato per scalabilità e flessibilità.

Il termine NoSQL comprende molti DBMS con **modelli logici diversi** (annotazione: "esistono contesti in cui si usano entrambi i sistemi SQL e NoSQL"):

| Modello | Idea | Esempi tipici |
|---|---|---|
| **chiave/valore** | un dizionario gigante: a ogni chiave un valore opaco | Redis |
| **document-oriented** | documenti strutturati (JSON) raggruppati in collezioni | **MongoDB** |
| **column-oriented** | dati organizzati per colonne/famiglie di colonne | Cassandra |
| **graph-oriented** | nodi e archi etichettati | **Neo4j** |

I due evidenziati come "più interessanti" sono document-oriented e graph-oriented, quelli studiati nel corso.

---

## 7.2 Document-oriented database, MongoDB

Vedi [[Database Documentale MongoDB]].

MongoDB (annotazione: "il modello dei dati è JSON"; "abbiamo un livello di dati dal JSON"):
- gestisce dati **eterogenei e complessi** (**semi-strutturati**);
- è **scalabile orizzontalmente**, con **partizionamento** dei dati (*sharding*) su sistemi distribuiti;
- un **documento** è un insieme di coppie chiave/valore (**JSON**);
- offre funzioni di aggregazione e analisi (**MapReduce**).

Un database MongoDB è organizzato in **collezioni**; una collezione contiene una lista di **documenti**; ogni documento è un insieme **non rigido** di **campi** con i loro valori.

| MongoDB | Modello relazionale |
|---|---|
| Collezione | Tabella (annotazione: "+ flessibile" vs "+ rigida") |
| Documento | Riga |
| Campo | Colonna di una riga |

![[BD-L07-p011.png]]

Una **collezione** di tre documenti: una DeLorean DMC-12 (con un campo `notes` che è un **array** di stringhe), una Fiat Panda 4x4 (con un campo `colour` che le altre non hanno) e un carro armato (senza `company`, con `gun`). Annotazioni: la collezione è come una "tabella", il documento una "tupla in formato JSON", il campo/valore una "colonna più riga"; `notes` "non è un valore atomico!! non sarebbe possibile nel modello relazionale"; "non contengono tutti gli attributi: estremamente flessibile". Ogni documento ha la **sua** struttura.

### JSON

Vedi [[JSON]].

JSON è un formato per lo **scambio di dati** tra applicazioni, facile da interpretare per le macchine (molti parser). I dati di un documento sono racchiusi tra `{ }`; ogni dato ha la forma `nomeCampo: valore`. Esempi: `{ nome: "mario" }`, `{ nome: "mario", cognome: "rossi" }`.

| Tipo di valore | Esempio |
|---|---|
| numero (intero o reale) | `{ nome: "mario", eta: 15, punti: 13.45 }` |
| stringa (tra apici) | `{ nome: "mario", cognome: "rossi" }` |
| booleano | `{ nome: "mario", impiegato: true }` |
| array (tra quadre) | `{ nome: "mario", cap: ["134", "042"] }` |
| documento annidato (tra graffe) | `{ nome: "mario", indirizzo: { citta: "bologna", via: "po", numero: 3 } }` |

```json
{  nome: "Mario",
   cognome: "Rossi",
   eta: 45,
   impiegato: false,
   salario: 1205.50,
   telefono: ["0243434", "064334343"],
   ufficio: [ {nome: "A", via: Zamboni, numero: 7},
              {nome: "B", via: Irnerio, numero: 49} ]
}
```

Il campo `ufficio` ha come valore un **array di documenti**. In relazionale servirebbero altre due tabelle (telefoni e uffici) con foreign key.

![[BD-L07-p015.png]]

Appunto di Simone: possono anche mettere dentro la stessa collezione documenti che tra loro non centrano nulla! Forte critica a questa tipologia di DBMS.

### Server, database e collezioni

```
mongod        // demone in ascolto sulla porta
mongo         // shell client
```

| Comando | Azione |
|---|---|
| `show dbs` | mostra i DB disponibili |
| `show collections` | mostra le collezioni del db |
| `show users` | mostra gli utenti |
| `show rules` | mostra il sistema di accessi |
| `show logs` | mostra i log |

```js
use provaDB                       // usa (o crea) un database
db.createCollection("circoli")    // crea una collezione vuota
```

### Documenti e _id

Un documento è un oggetto JSON con un campo **`_id`**:
```js
{ _id: 100, nome: "Marco", cognome: "Rossi", eta: 22, data: new Date(1997,6,2,12,30) }
{ _id: 200, nome: "Gianni", cognome: "Bosi", eta: 30, data: new Date(1999,7,12,10,00) }
```

Nella stessa collezione si possono inserire documenti con **strutture diverse**: nella collezione anagrafica DOC1 ha nome ed età, DOC2 nome e cognome, DOC3 nome, cognome, età e data. In relazionale bisognerebbe prevedere **a priori** tutte le possibilità e usare **massicciamente i valori nulli**.

`_id` corrisponde alla **chiave primaria** nella collezione; può essere dato **esplicitamente** o aggiunto **implicitamente** dal sistema:
```js
db.anagrafica.insert({_id: 1, name: "Marco", cognome: "Rossi", eta: 22})     // ID esplicito
db.anagrafica.insert({name: "Marco", cognome: "Rossi", ruolo: 'Manager'})    // ID implicito
```

### Inserimento e cancellazione

```js
db.NOMECOLLEZIONE.insert(DOCUMENTO)

db.anagrafica.insert({nome: "Marco", cognome: "Rossi", eta: 22})
db.anagrafica.insert({cognome: "Rossi", eta: 22, domicilio: ["Roma", "Bologna"]})
db.anagrafica.insert({nome: "Maria", eta: 25})

db.NOMECOLLEZIONE.delete({})          // svuota la collezione
db.NOMECOLLEZIONE.delete(SELETTORE)   // elimina i documenti che soddisfano il selettore
```

> [!note] Nota
> Nelle versioni attuali di MongoDB i metodi si chiamano `insertOne`/`insertMany`, `deleteOne`/`deleteMany`, `updateOne`/`updateMany`; `insert` e `update` sono deprecati e `delete` come metodo di collezione non esiste (c'era `remove`). Le slide usano la sintassi semplificata storica.

### Selettori

Un **selettore** è un documento JSON che descrive i documenti da selezionare (è l'analogo della `where`):

| Selettore | Significato |
|---|---|
| `{campo1: valore1, campo2: valore2}` | **AND** delle uguaglianze. Es. `{name: "Marco", cognome: "Rossi"}` |
| `{$or: [{campo1: valore1}, {campo2: valore2}]}` | **OR**. Es. `{$or: [{name: "Marco"}, {cognome: "Rossi"}]}` |
| `{campo: {$OP: valore}}` | confronti con `$gt`, `$lt`, `$gte`, `$lte`, `$ne`, `$in`. Es. `{name: "Marco", eta: {$gt: 30}}` |

### Aggiornamento

```js
db.NOMECOLLEZIONE.update(SELETTORE, DOCUMENTO)          // sostituisce l'intero documento
db.NOMECOLLEZIONE.update(SELETTORE, {$set: CAMPI})      // imposta/aggiunge campi
db.NOMECOLLEZIONE.update(SELETTORE, {$push: CAMPI})     // appende a un array
db.NOMECOLLEZIONE.update(SELETTORE, CAMPI, OPZIONI)     // OPZIONI = {upsert: <bool>, multi: <bool>}
```

| Esempio | Effetto |
|---|---|
| `update({nome: "Mario"}, {eta: 45})` | nel **primo** documento con nome Mario, **sostituisce** l'intero documento con `{eta: 45}` (il nome sparisce!) |
| `update({nome: "Mario"}, {$set: {eta: 45}})` | nel primo documento con nome Mario, imposta l'età a 45 (o aggiunge il campo) |
| `update({nome: "Mario"}, {$push: {eta: 45}})` | appende 45 all'array `eta`, o crea il campo con `[45]` |
| `update({nome: "Mario"}, {$set: {eta: 45}}, {multi: true})` | modifica **tutti** i documenti con nome Mario |

`upsert: true` inserisce un nuovo documento se nessuno soddisfa il selettore.

### Interrogazioni, find

```js
db.nomeCollezione.find()                          // tutti i documenti
db.nomeCollezione.find(SELETTORE)                 // i documenti che soddisfano il selettore
db.nomeCollezione.find(SELETTORE, PROJECTION)     // solo i campi indicati
```

| MongoDB | SQL |
|---|---|
| `db.anagrafica.find()` | `SELECT * FROM anagrafica` |
| `db.anagrafica.find({nome: "Mario", eta: 30})` | `SELECT * FROM anagrafica WHERE nome = 'Mario' AND eta = 30` |
| `db.anagrafica.find({nome: "Mario"}, {eta: 1})` | `SELECT _id, eta FROM anagrafica WHERE nome = 'Mario'` |
| `db.anagrafica.find({$or: [{nome: "Mario"}, {eta: 56}]}, {eta: 1})` | `SELECT _id, eta FROM anagrafica WHERE nome = 'Mario' OR eta = 56` |
| `db.anagrafica.find({eta: {$gte: 60}})` | `SELECT * FROM anagrafica WHERE eta >= 60` |
| `db.anagrafica.find({eta: {$exists: true}})` | `SELECT * FROM anagrafica WHERE eta IS NOT NULL` |
| `db.anagrafica.find({nome: 'Mario'}).sort({eta: 1})` | `... WHERE nome = 'Mario' ORDER BY eta` (1 crescente, −1 decrescente) |
| `db.anagrafica.find({nome: "Mario"}).count()` | `SELECT COUNT(*) FROM anagrafica WHERE nome = 'Mario'` |
| `db.anagrafica.distinct("eta", {nome: "Mario"})` | `SELECT DISTINCT eta FROM anagrafica WHERE nome = 'Mario'` |

Nella proiezione `{eta: 1}` il campo `_id` è incluso di default.

> [!warning] Correzione
> Nella slide l'esempio con `$or` è scritto `find({$or:[{nome: "Mario"},{eta:56}]} {eta:1}])`, con parentesi sbagliate e senza virgola tra selettore e proiezione: la forma corretta è `find({$or: [{nome: "Mario"}, {eta: 56}]}, {eta: 1})`. Nell'esempio con `$exists` manca una graffa di chiusura. Inoltre `{$exists: true}` corrisponde a "il campo **esiste**": un documento con `eta: null` lo soddisfa, mentre in SQL `eta IS NOT NULL` no; l'equivalenza della slide vale solo se i valori nulli non vengono memorizzati esplicitamente.

### Script JavaScript

I comandi si possono raccogliere in uno **script JavaScript** (`mongo myfile.js`), che inizia con la connessione:
```js
conn = new Mongo();
db = conn.getDB("tennis");
```
Lo script può contenere `while`, `if/else`, e **cursori** per scorrere il risultato di una query (annotazione: "semplice: Mongo DB è un sistema JavaScript"):
```js
cursor = db.collection.find(...);
while (cursor.hasNext()) {
    printjson(cursor.next());
}
```
È lo stesso meccanismo del [[04 - BD - Accesso ai Dati da Software#ResultSet e metodi getXXX|ResultSet di JDBC]].

### Correlazioni tra collezioni

![[BD-L07-p037.png]]

Appunti di Simone. In alto la foto della lavagna: "conversione da concettuale a MongoDB", uno schema ER (E – R – F con G) e la traduzione in documenti, "traduzione esempio" a destra. Un'azienda potrebbe proporti una tipologia di database che non usa PostgreSQL ma un altro sistema ancora, ad esempio MongoDB. La bravura dell'ingegnere non sta nel fatto che non sa un linguaggio nuovo, ma nella sua capacità di studiarsi RAPIDAMENTE un nuovo linguaggio, altrimenti non c'è mercato per lui. UN BRAVO STUDENTE È UNO STUDENTE CHE, NONOSTANTE NON SAPPIA UN CAZZO, IN UN GIORNO DI LEZIONE GIÀ SA TUTTA LA LEZIONE (IDEALMENTE). ("Sono un completo fallito"). Noi svilupperemo una nostra metodologia nel saper convertire lo schema concettuale in codice di un altro linguaggio (questa è la nostra capacità da dover allenare).

Esempio: circoli di tennis e soci dei circoli.
- MongoDB **non** ha vincoli di **integrità referenziale** tra collezioni.
- Il **join** tra collezioni è molto difficoltoso.

Le correlazioni si esprimono **replicando gli `_id`** tra collezioni (un riferimento "manuale", senza alcun controllo):
```js
db.circoli.insert({_id: "120", nome: "Nettuno"})
db.soci.insert({nome: "Mario", cognome: "Rossi", circolo: "120"})
```

Per associazioni **uno-a-molti** o **molti-a-molti** si sfrutta il fatto che un campo può essere un **array** (o un documento annidato):
```js
db.soci.insert({nome: "Mario", cognome: "Rossi", circolo: ["120", "150", "200"]})
```

> [!warning] Correzione
> Nelle slide i comandi hanno parentesi sbilanciate: `insert({_id: "120"), nome: "Nettuno"})` e `circolo:["120", "150", "200")]`. Le forme corrette sono quelle riportate sopra.

**Problema**: nome e cognome dei soci di circoli situati a Bologna, **senza join**.

**Soluzione 1**: due query nello stesso script:
```js
db.circoli.find({luogo: "Bologna"}, {})      // >> {_id: "432"}
db.soci.find({circolo: "432"}, {nome: 1, cognome: 1})
```
Il "join" lo fa l'applicazione, a mano: è il lavoro che in relazionale fa il DBMS.

**Soluzione 2**: gli **operatori di aggregazione** (`aggregate`), che definiscono una **pipeline** di operazioni: a ogni passo un operatore prende documenti JSON in input e produce documenti JSON in output.

![[BD-L07-p042.png]]

Il diagramma della pipeline: COLLEZIONE → OPERATORE1 → OPERATORE2 → RISULTATO, con documenti (DOC) che passano da uno stadio all'altro. È come comporre gli operatori dell'algebra relazionale.

### Il join con $lookup

```
Orders                                                   Products
{_id: 1, item: 1, price: 49.99, qty: 1}                  {_id: 1, name: "Kick Scooter", price: 49.99}
{_id: 2, item: 1, price: 49.99, qty: 3}                  {_id: 2, name: "Power Jeep", price: 99.99}
{_id: 3, item: 2, price: 99.99, qty: 1}                  {_id: 3, name: "Power Wheel Lightning McQueen", price: 199.9}
```

Si vuole il join tra Orders e Products con `Orders.item = Products._id`:

```js
db.orders.aggregate(
  { $lookup:
      { from: "products",          // collezione con cui fare il join
        localField: "item",        // campo di orders...
        foreignField: "_id",       // ...uguale a questo campo di products
        as: "ordered_product" }    // nome del nuovo campo
  }
)
```

Risultato: ogni ordine riceve un campo `ordered_product` con l'**array** dei prodotti corrispondenti:
```js
{_id: 1, item: 1, price: 49.99, qty: 1, ordered_product: [{_id: 1, name: "Kick Scooter", price: 49.99}]}
{_id: 2, item: 1, price: 49.99, qty: 3, ordered_product: [{_id: 1, name: "Kick Scooter", price: 49.99}]}
{_id: 3, item: 2, price: 99.99, qty: 1, ordered_product: [{_id: 2, name: "Power Jeep", price: 99.99}]}
```

`$lookup` corrisponde a un [[02 - BD - Modello Relazionale#Join esterno|join esterno sinistro]]: un ordine senza prodotto corrispondente comparirebbe comunque, con l'array vuoto. Il prodotto 3 non compare (nessun ordine lo riferisce).

---

## 7.3 Graph database

Vedi [[Graph Database]].

- Un **graph database** usa una struttura a **grafo** (nodi, archi, proprietà) per rappresentare e memorizzare i dati.
- Offre i metodi **CRUD** (Create, Read, Update, Delete).
- A differenza di altri NoSQL, i sistemi a grafo (es. **Neo4j**) sono in genere ottimizzati per le prestazioni **transazionali** e tendono a garantire le proprietà **ACID**.

Caratteristiche:
- **schemaless**: si accumulano dati incrementalmente senza uno schema rigido predefinito, utile con la dinamica dei big data. Gli aspetti intensionali si possono rappresentare, ma non sono predefiniti e si gestiscono come dati (come in RDF); grande flessibilità nel dare proprietà diverse a elementi diversi, a qualsiasi granularità; ottimi per **dati sparsi**;
- interrogabili con **linguaggi dichiarativi** (alcuni standard), con ottime prestazioni su certe query perché "sanno" gestire tipi specifici di join (ma le prestazioni dipendono dal tipo di query).

![[BD-L07-p049.png]]

**Flessibilità**: un grafo sociale con utenti (Alice, Bob, Zach, James, Charlie, Grace, Davina, Harriet, Ingrid, Fred, Edward) e archi di tipo diverso (`FRIEND_OF`, `COLLEAGUE_OF`, `BOSS_OF`, `LOVES`, `DISLIKES`, `MARRIED_TO`). Aggiungere un nuovo tipo di relazione significa solo aggiungere archi con una nuova etichetta, senza modificare uno schema: incorporare informazione dinamica è naturale e semplice.

**Le relazioni sono native.** I graph database sono adatti quando l'informazione è "nativamente" un grafo: social network, sistemi di raccomandazione, applicazioni geospaziali, reti di calcolatori, controllo degli accessi. Il loro punto di forza è che i **collegamenti** rappresentano **esplicitamente** le relazioni. Nei database relazionali invece le relazioni vanno **simulate** con le foreign key, con overhead di sviluppo e manutenzione, e "navigarle" richiede **join costosi**.

### Esempio, amici e amici degli amici

![[BD-L07-p051.png]]

In relazionale: `Person(ID, Person)` con Alice (1), Bob (2), …, Zach (99), e `PersonFriend(PersonID, FriendID)`. La relazione non è simmetrica: Bob può considerare Zach amico senza che valga il contrario.

**Gli amici di Alice** (quelli che Alice considera amici) sono facili:
```sql
SELECT p2.Person AS ALICE_FRIEND
FROM Person p1 JOIN PersonFriend pf ON p1.ID = pf.PersonID
               JOIN Person p2 ON pf.FriendID = p2.ID
WHERE p1.Person = 'Alice'
```

![[BD-L07-p053.png]]

**Gli amici degli amici** diventano problematici: serve un join in più per ogni livello di profondità.
```sql
SELECT p2.Person AS ALICE_FRIEND_OF_FRIEND
FROM Person p1 JOIN PersonFriend pf1 ON p1.ID = pf1.PersonID
               JOIN PersonFriend pf2 ON pf1.FriendID = pf2.PersonID
               JOIN Person p2 ON pf2.FriendID = p2.ID
WHERE p1.Person = 'Alice' AND pf2.FriendID <> p1.ID     -- esclude Alice stessa
```
Le prestazioni **degradano molto** andando più in profondità nella rete. (È lo stesso limite visto per la [[04 - BD - Accesso ai Dati da Software#Esempio, chiusura transitiva di un grafo|chiusura transitiva]]: una query con un numero fissato di join segue cammini di lunghezza fissata.)

![[BD-L07-p054.png]]

In un graph database Alice, Bob e Zac sono **nodi** collegati da archi `FRIEND_OF`. Le relazioni formano naturalmente **cammini**: interrogare significa **attraversare** il grafo, seguendo i cammini, e le operazioni basate sui cammini sono estremamente efficienti.

| | Database relazionale | Graph database |
|---|---|---|
| come si interroga | **join** | **attraversamento** di cammini (*traversal*) |
| dov'è il grafo | costruito **dinamicamente** dai join; non è esplicito, va dedotto con operazioni pesanti sugli indici | **esplicito**: ogni nodo ha riferimenti diretti ai suoi archi |
| dati considerati | anche se serve un piccolo sottoinsieme (gli amici degli amici di Alice), vanno considerati tutti i dati delle tabelle coinvolte | si visitano solo i nodi raggiunti |
| costo di un passo | un join | passare da un nodo all'adiacente è (quasi) a **tempo costante**: gli archi sono join "cablati" |

### Interrogare un graph database

Vedi [[Regular Path Query]].

Un **attraversamento** (*traversal*) visita nodi e archi del grafo secondo un algoritmo. I linguaggi di query per grafi permettono di attraversare **ricorsivamente** gli archi etichettati verificando l'esistenza di un cammino la cui etichetta soddisfa una **condizione regolare**.

Formalmente:
- un **graph database** su un alfabeto finito $\Sigma$ è $G = (V, E)$ con $V$ insieme finito di nodi ed $E \subseteq V \times \Sigma \times V$ archi **etichettati**;
- un **cammino** $\pi$ da $v_0$ a $v_m$ è una sequenza $(v_0, a_1, v_1)(v_1, a_2, v_2) \dots (v_{m-1}, a_m, v_m)$ di archi di $E$; la sua **etichetta** è la stringa $\lambda(\pi) = a_1 a_2 \dots a_m \in \Sigma^*$;
- una **regular path query** è un'espressione regolare $L$ su $\Sigma$; la sua valutazione $L(G)$ è l'insieme delle coppie $(u, v)$ di nodi per cui esiste un cammino $\pi$ da $u$ a $v$ con $\lambda(\pi) \in L$.

**Sintassi delle espressioni regolari**:
$$L ::= s \mid L \cdot L \mid L | L \mid L^* \mid L^+ \mid L? \mid (L)$$

| Simbolo | Significato |
|---|---|
| $s$ | un simbolo di $\Sigma$ |
| $L \cdot L$ (o $LL$) | concatenazione |
| $L_1 \mid L_2$ | OR |
| $L^*$ | stella di Kleene: 0 o più ripetizioni |
| $L^+$ | 1 o più ripetizioni |
| $L?$ | 0 o 1 occorrenza |

Esempi: "ha antenati" = `isChildOf+`; "sono cugini" (per semplicità anche di se stessi) = `isChildOf·isChildOf·hasChild·hasChild`.

Vedi anche [[Regular Expressions]] nel corso magistrale.

![[BD-L07-p058.png]]

Grafo $G$ con $\Sigma = \{a, b\}$: archi $x \xrightarrow{a} z$, $x \xrightarrow{a} y$, $x \xrightarrow{b} w$, $y \xrightarrow{b} t$. Con $L = ab^*$ (una $a$ seguita da zero o più $b$): $L(G) = \{(x, y), (x, z), (x, t)\}$. $(x, w)$ non c'è perché l'etichetta è $b$, che non inizia con $a$. I linguaggi di query per grafi estendono tipicamente questa classe di query.

![[BD-L07-p059.png]]

Grafo con nodi 0–6 e archi $0 \xrightarrow{a} 1$, $1 \xrightarrow{d} 2$, $2 \xrightarrow{d} 3$, $3 \xrightarrow{c} 5$, $4 \xrightarrow{d} 0$, $3 \xrightarrow{e} 4$, $5 \xrightarrow{a} 6$. Espressione: $d^+(c \mid e)a$, cioè una o più $d$, poi una $c$ o una $e$, poi una $a$.

Cammini che la soddisfano:
- `dca`: $2 \xrightarrow{d} 3 \xrightarrow{c} 5 \xrightarrow{a} 6$, quindi $(2, 6) \in L(G)$;

![[BD-L07-p061.png]]

- `ddca`: $1 \xrightarrow{d} 2 \xrightarrow{d} 3 \xrightarrow{c} 5 \xrightarrow{a} 6$, quindi $(1, 6) \in L(G)$.

Il ramo con $e$ non dà risultati: $3 \xrightarrow{e} 4$ porta a 4, da cui esce solo un arco $d$, quindi $d^+ e a$ non si completa. Grazie al ciclo $0 \to 1 \to 2 \to 3 \to 4 \to 0$ non ci sono altri cammini validi: da 4 si torna a 0, ma l'arco $0 \to 1$ ha etichetta $a$ e interrompe la sequenza di $d$. Quindi $L(G) = \{(2, 6), (1, 6)\}$.

> [!note] Nota
> Lo schema del grafo è ricostruito dalle figure; le slide mostrano solo i due cammini evidenziati (`dca` e `ddca`).

![[BD-L07-p062.png]]

Foto della lavagna dell'ultima lezione, un sillogismo per gli auguri: "1. Studiare Basi di dati è meglio di niente. 2. Niente è meglio delle vacanze di Natale. 3. Studiare Basi di dati è meglio delle vacanze di Natale". È volutamente fallace: "niente" ha due significati diversi nelle due premesse ("non fare nulla" e "nessuna cosa"), e quindi la conclusione non segue.
