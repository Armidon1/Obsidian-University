---
title: Esercizi RDF — Graph Databases
aliases:
  - DM — Esercizi RDF
tags:
  - data-management
  - graph-databases
  - rdf
  - esercizi
source: "03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs.md; conversazione di studio"
---

# Esercizi RDF — Graph Databases

> [!abstract] Obiettivo
> Allenarsi a scrivere e leggere triple, distinguere risorse e valori, usare blank node e rappresentare relazioni con data. Gli ultimi esercizi distinguono i fatti asseriti dalle affermazioni attribuite a qualcuno mediante reificazione. Riferimento: [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs]].

## Come svolgerli

- Scrivi il codice nei blocchi **Svolgimento**, poi aggiungi le spiegazioni richieste.
- Considera ogni esercizio come un grafo indipendente: non eredita le triple degli altri.
- I prefissi qui sotto sono disponibili in tutti gli esercizi; non occorre ricopiarli.
- Puoi scegliere etichette diverse per i blank node, mantenendole coerenti dentro ciascun esercizio.
- Le proprietà del namespace `:` sono definite per gli esercizi con il significato indicato nel testo. Non aggiungere regole di simmetria, transitività, unicità o inferenza non richieste.
- Le soluzioni non sono incluse. Quando hai finito, chiedimi di correggere la nota: valuteremo sia la sintassi sia ciò che il grafo effettivamente afferma.

```turtle
@prefix : <https://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

> [!note] Convenzioni per date e affermazioni
> Usa `xsd:date` per una data completa e `xsd:gYear` per un anno. `:claims` significa “afferma lo statement indicato”; `:believes` significa “crede allo statement indicato”. Questi significati sono convenzioni del nostro vocabolario: RDF da solo non fornisce una logica della credenza né verifica chi abbia ragione.

## 01 — Persone, nomi e classi

- [x] Svolto

Rappresenta i fatti:

1. John conosce Mary.
2. Mary ha nome “Maria”.
3. Mary è una persona.

Usa `:John`, `:Mary`, `foaf:knows`, `foaf:name`, `foaf:Person` e `rdf:type`.

**Svolgimento**

```turtle
# Scrivi qui.
:John foaf:knows :Mary .
:Mary foaf:name "Maria" .
:Mary rdf:type foaf:Person .
```

**Spiegazione:** perché l'oggetto del primo fatto e quello del secondo non si scrivono nello stesso modo? Il nome “Maria” richiede di cambiare `:Mary`?

> Risposta: perché nel primo stiamo dicendo che John conosce una specifica risorsa Mary, di nome "Mary". potenzialmente la risorsa Mary si poteva anche chiamare "SergioPiselloneMassimo".

## 02 — Triple ripetute e proprietà con più valori

- [x] Svolto

Considera:

```turtle
:Ann foaf:knows :John .
:Ann foaf:knows :Mary .
:Ann foaf:knows :John .
:Ann foaf:name "Anna" .
:Ann foaf:name "Giulia" .
:Mary foaf:knows :Ann .
```

1. Quante triple distinte contiene il grafo?
2. Quanti valori espliciti di `foaf:knows` ha Ann? Quali?
3. Il nome “Giulia” sostituisce “Anna”?
4. Il grafo contiene esplicitamente `:John foaf:knows :Ann .`?
5. Scrivi il grafo che otterresti eliminando soltanto il nome “Anna”.

**Risposte**

> 1. 5, perchè vi è una ripetizione di ':Ann foaf:knows :John .' in particolare perché il grafo è un insime di triple, e non ci possono essere ripetizioni di triple 
> 2. 2
> 3. no, Ann si chiama contemporaneamente "anna" e "giulia"
> 4.  La risposta è no. È presente il verso opposto:
:Ann foaf:knows :John .
Una freccia Ann → John non aggiunge automaticamente la freccia John → Ann.

```turtle
# Grafo risultante.
```

## 03 — Prefissi e identità

- [x] Svolto

In questo esercizio sono disponibili anche:

```turtle
@prefix people: <https://example.org/> .
@prefix other: <https://other.example/> .
```

1. Espandi `:Mary`, `people:Mary`, `:mary` e `other:Mary` nelle rispettive IRI complete.
2. Quali scritture producono esattamente la stessa IRI?
3. IRI diverse permettono, da sole, di concludere che si tratti necessariamente di persone diverse?
4. Usare queste IRI in una tripla obbliga a scaricare documenti dai rispettivi indirizzi?

**Risposte**

> 1. https://example.org/Mary, https://example.org/Mary, https://example.org/mary, https://other.example/Mary
> 2. :Mary con people:Mary.
> 3.No: IRI diverse possono identificare la stessa persona. La differenza tra gli identificatori, da sola, non dimostra che le risorse siano diverse
> 3. No, non sono necessariemente dei documenti da scaricare, sono banalmente degli identificatori e devono essere univoci. Gli URL sono nati per essere univoci ed eventulemante anche permettono di specificare come raggiungere una deteminata risorse nel server destinazione, ed è il motivo per cui è tanto usato nel web per scaricare pagine html.

## 04 — Una persona senza IRI

- [x] Svolto

Ann conosce una persona che non vogliamo identificare con una IRI. Questa persona si chiama “Paolo”, è un'istanza di `foaf:Person` e conosce John.

Scrivi **quattro triple** usando un unico blank node.

**Svolgimento**

```turtle
# Scrivi qui.
:Ann foaf:knows _:x .
_:x foaf:name "Paolo" .
_:x rdf:type foaf:Person .
_:x foaf:knows :John .
```

**Spiegazione:** quali informazioni andrebbero perse se sostituissi il blank node con il literal `"Paolo"` nell'oggetto della relazione di conoscenza? Perché `:x` non è equivalente alla notazione `_:x`? 

> Risposta: banalmente perché "Paolo" è solo una stringa e noi non possiamo usarla eventualmente come soggetto o predicato di una tripla. di conseguenza non avremmo potuto dire "esiste una risorsa di nome Paolo che conosce John ed è una persona". il motivo per cui `_:x` è diverso da `:x` è perché `:x` si riferisce all'IRI `https://example.org/x` per come lo abbiamo definito nel prefix. 

## 05 — Stesso nodo o nodi separati?

- [x] Svolto

Confronta i due grafi, ciascuno considerato separatamente:

**Grafo A**

```turtle
:John foaf:knows _:x .
_:x foaf:name "Sara" .
_:x foaf:knows :Mary .
```

**Grafo B**

```turtle
:John foaf:knows _:x .
_:y foaf:name "Sara" .
_:z foaf:knows :Mary .
```

1. Quale grafo esprime esplicitamente, mediante un nodo condiviso, che John conosce qualcuno che si chiama Sara e conosce Mary?
2. Il grafo B collega necessariamente tutte e tre le informazioni alla stessa risorsa?
3. Etichette diverse di blank node impongono che le risorse rappresentate siano distinte?
4. Riscrivi A usando `_:persona` al posto di `_:x`. Cambia l'informazione rappresentata?

**Risposte**

> 1. ovviamente il primo grafo perché nel seconod abbiamo definito altri 2 blank nodes, uno che si chiama "Sara" ed un altro che conosce :Mary.
> 2. Non necessariamente, `_:y` potrebbe essere una risorsa differente a `_:x` e lo stesso vale per `_:z`
> 3. Non per forza: possono rappresentare la stessa risorsa ma semplicemente non forza nessuna conclusione.
> 4. giù ho scritto la soluzione:

``` Turtle
:John foaf:knows _:persona .
_:persona foaf:name "Sara" .
_:persona foaf:knows :Mary .
```
al livello semantico non cambia assolutamente niente. `_:persona` è un blank node esattamente come `_:x` potrebbe essere anche un cane oppure un qualsiasi altro oggetto nella realtà. non abbiamo definito che `_:persona rdf:type foaf:Person`
## 06 — Correggere un tentativo

- [x] Svolto

L'intenzione è: “John conosce una persona anonima, chiamata Sara, che conosce Mary”. Individua e correggi gli errori:

```turtle
:John feaf:knows :x .
:x foaf:knows "Sara .
:x foaf:knows Mary
```

**Svolgimento**

```turtle
# Versione corretta.
:John feaf:knows _:x .
_:x rdf:type foaf:Person .
_:x feaf:name "Sara" .
_:x feaf:knows :Mary .
```

**Spiegazione:** elenca gli errori di sintassi, prefisso e significato che hai corretto.

> Risposta: il fatto che lo definiamo anonima la persona, indica che non possiamo dagli esplicitamente una risorsa specifica mediante un IRI, allora usiamo il blank node `_:x`. Se usaimo un blank node dobbiamo specificare inoltre che sia una Persona. inoltre non si è chiuso la stringa "Sara" con gli apici e di conseguenza avevamo che `:x foaf:knows "Sara \n:x foaf:knows Mary"` e mancava il punto finale. 

## 07 — Un'amicizia con una data

- [x] Svolto

Mary e Ann partecipano a un'amicizia iniziata il **12 marzo 2019**.

Rappresenta l'amicizia come una risorsa anonima, con **quattro triple**. Usa la classe `:Friendship`, la proprietà `:participant` per ciascuna persona e `:since` per la data.

**Svolgimento**

```turtle
# Scrivi qui.
_:x rdf:type :Friendship .
_:x :participant :Mary .
_:x :participant :Ann .
_:x :since "2019-03-12"^^xsd:date .
```

**Spiegazione:** che cosa rappresenta il blank node? Perché la data va collegata a quel nodo? Il tuo grafo implica automaticamente la tripla `:Mary :isFriendOf :Ann .` senza regole aggiuntive?

> Risposta: quel blank node rappresenta una friendship tra `:Mary` ed `:Ann` iniziata nella data 2019-03-12. la data va collegata a quel nodo perché effettivamente indica la nascita della relationship. Non implica necessariamente `:Mary :isFriendOf :Ann .` perché potrebbe implicare solo `:Ann :isFriendOf :Mary .` e non viceversa. in particolare, non abbiamo creato delle regole che specificato che mostrano collegamenti tra `:participant`, `:Relationship` e `:isFriendOf`.

> [!note] Come ottenere anche la relazione `:isFriendOf`
> Una soluzione che rappresenta esplicitamente anche la relazione binaria mantiene le quattro triple sopra e aggiunge `:Mary :isFriendOf :Ann .`. In questo caso il fatto è **asserito direttamente**, non ricavato automaticamente dalla struttura dell'amicizia. Per **dedurlo** dalle sole quattro triple, serve invece una regola aggiuntiva, espressa qui in pseudocodice:
>
> **Se** `f rdf:type :Friendship`, `f :participant a`, `f :participant b` e `a` e `b` sono distinti, **allora** `a :isFriendOf b`.
>
> Le lettere `f`, `a` e `b` sono variabili della regola, non termini Turtle. Un motore che applica questa regola ricaverebbe sia `:Mary :isFriendOf :Ann .` sia `:Ann :isFriendOf :Mary .`, scambiando i due partecipanti: stiamo quindi scegliendo un modello di amicizia simmetrica. La condizione di distinzione evita di generare amicizie con sé stessi; in generale la distinzione deve essere verificata dal sistema, non dedotta soltanto da IRI diverse. Questa regola non fa parte dell'inferenza standard RDF/RDFS: va fornita a un sistema che supporti regole aggiuntive.

## 08 — Due amicizie, due date

- [x] Svolto

Mary partecipa:

- a un'amicizia con Ann, iniziata il **12 marzo 2019**;
- a un'amicizia con John, iniziata il **1º giugno 2020**.

Usa lo stesso modello dell'esercizio 07. Ogni amicizia ha un solo anno-mese-giorno di inizio nel modello richiesto.

**Svolgimento**

```turtle
# Scrivi qui.
_:x rdf:type :Relationship .
_:x :participant :Mary .
_:x :participant :Ann .
_:x :since "12-03-2019"^^xsd:date .

_:y rdf:type :Relationship .
_:y :participant :Mary .
_:y :participant :John .
_:y :since "01-06-2020"^^xsd:date .
```

**Spiegazione:** che cosa comunicheresti, involontariamente, usando lo stesso blank node per entrambe le amicizie?

> Risposta: diremmo che ci sarebbe una relationship tra `:John`, `:Ann` e `:Mary`, che è nata dal "12-03-2019" ed anche dal "01-06-2020", il che non sarebbe molto chiaro.

## 09 — Reificare una tripla

- [x] Svolto

Descrivi mediante reificazione standard la tripla:

```turtle
:Mary :hasFriendship _:friendship .
```

Usa `_:maryStatement` per lo statement e scrivi **quattro triple**. Non aggiungere la tripla originale al grafo della soluzione.

**Svolgimento**

```turtle
# Scrivi qui.
_:maryStatement rdf:type :Statement .
_:maryStatement rdf:subject :Mary .
_:maryStatement rdf:predicates :hasFriendship .
_:maryStatement rdf:object _:friendship .
```

**Spiegazione:** che cosa rappresentano rispettivamente `_:maryStatement` e `_:friendship`? Perché sostituire `:Mary` con `_:Mary` cambierebbe l'affermazione descritta? Il grafo della soluzione asserisce la tripla originale?

> Risposta: `_:maryStatement` è un [[Blank Node]] che rappresenta una reificazione della tupla di sopra con la particolarità di essere uno statement di mary e non una realtà fattuale. di conseguenza non asserisce la tripla originale che esplicita che ESISTE realmente una fiendship `_:friendship` di cui `:Mary` fa parte. sostiene `:Mary` con `_:Mary` staccherebbe l'associazione di tale [[Blank Node]] all'effettiva risorsa `:Mary` identificata dal rispettivo IRI.

## 10 — Chi sostiene un'affermazione?

- [x] Svolto

Simone afferma che Roma si trova in Italia. Vuoi registrare **l'attribuzione a Simone**, senza asserire direttamente il contenuto della sua affermazione.

Reifica `:Rome :isIn :Italy .` e collega Simone allo statement usando `:claims`. Servono **cinque triple**.

**Svolgimento**

```turtle
# Scrivi qui.
_:simoneStatement rdf:type rdf:Statement .
_:simoneStatement rdf:subject :Rome .
_:simoneStatement rdf:predicate :isIn .
_:simoneStatement rdf:object :Italy .

:Simone :claims _:simoneStatement .
```

**Spiegazione:** che cosa cambierebbe se aggiungessi anche `:Rome :isIn :Italy .`? Il nome del blank node, da solo, dice che Simone è l'autore dell'affermazione?

> Risposta: il nome del blank node da solo non crea nessun collegamento diretto "claims" con l'effettiva risorsa `:Simone`, di conseguenza sarebbe uno Statement fine a se stesso. Se avessimo aggiunto anche la tupla originale, avremmo la certezza che `:Rome` fosse effettivamente in `:Italy` e `:Simone` con il suo statement ha ragione ahahaah. 

## 11 — Un dato e un'affermazione con date diverse

- [x] Svolto

Scenario inventato, senza riferimenti storici: nel catalogo il libro `:LibroA` risulta pubblicato nel **2020**. Simone afferma invece che lo stesso libro è stato pubblicato nel **2018**.

Usa `:publicationYear` e `xsd:gYear`:

1. Asserisci direttamente l'anno del catalogo.
2. Reifica la tripla sull'anno attribuito a Simone.
3. Collega Simone a quello statement, senza asserire direttamente il 2018 come anno del libro.

**Svolgimento**

```turtle
# Scrivi qui.
:LibroA :publicationYear "2020"^^xsd:gYear .

_:simoneStatement rdf:type rdf:Statement .
_:simoneStatement rdf:subject :LibroA .
_:simoneStatement rdf:predicate :publicationYear .
_:simoneStatement rdf:object "2018"^^xsd:gYear .
:Simone :claims _:simoneStatement .
```

**Spiegazione:** quali anni sono oggetto di triple dirette `:LibroA :publicationYear ...` nel tuo grafo? RDF da solo conclude che Simone sbaglia? Quale assunzione sull'anno di pubblicazione servirebbe per trattare i due anni come incompatibili?

> Il grafo asserisce direttamente soltanto il 2020. Il 2018 compare nello statement attribuito a Simone. RDF non stabilisce automaticamente che Simone sbagli: occorre assumere un unico anno di pubblicazione per il libro e confrontare la sua affermazione con il dato del catalogo assunto come corretto

## 12 — John crede all'amicizia con data

- [x] Svolto

Rappresenta: **“John crede che Mary sia amica di Ann dal 12 marzo 2019”**.

Per fissare il modello e rendere la correzione precisa, considera queste tre affermazioni come il contenuto da attribuire a John:

```turtle
:Mary :hasFriendship _:friendship .
:Ann :isInFriendship _:friendship .
_:friendship :since "2019-03-12"^^xsd:date .
```

Non inserirle direttamente come fatti: reifica ciascuna usando un nodo distinto e collega John a ciascuno statement con `:believes`. Tutte devono riferirsi alla stessa amicizia.

**Svolgimento**

```turtle
# Scrivi qui.
_:maryFriendshipStatement rdf:type rdf:Statement .
_:maryFriendshipStatement rdf:subject :Mary .
_:maryFriendshipStatement rdf:predicate :hasFriendship .
_:maryFriendshipStatement rdf:object _:friendship .

_:annFriendshipStatement rdf:type rdf:Statement .
_:annFriendshipStatement rdf:subject :Ann .
_:annFriendshipStatement rdf:predicate :isInFriendship .
_:annFriendshipStatement rdf:object _:friendship .

_:johnStatement rdf:type rdf:Statement .
_:johnStatement rdf:subject _:friendship .
_:johnStatement rdf:predicate :since . 
_:johnStatement rdf:object "2019-03-12"^^xsd:date .

:John :believes _:johnStatement .
:john :believes _:maryFriendshipStatement .
:john :believes _:annFriendshipStatement .
```

**Spiegazione**

1. Quale nodo rappresenta l'amicizia? Quali rappresentano affermazioni?
2. Nel blocco che descrive l'inizio dell'amicizia, qual è l'oggetto di `rdf:subject`? Perché?
3. Quali attribuzioni mancherebbero se John fosse collegato soltanto allo statement sulla data?
4. Le tre affermazioni descritte vengono automaticamente asserite dal grafo?
5. Come distingueresti concettualmente “l'amicizia è iniziata nel 2019” da “John ha iniziato a crederci nel 2021”? Indica a quale risorsa collegheresti ciascuna data, senza sviluppare per forza tutte le triple.

> 1. `_:friendship` che notiamo non essere collegato direttamente da `:ann` e `:mary` quindi non abbiamo certezze sulla vera amicizia. `_:johnStatement`,  `_:annStatement` e `_:maryFriendshipStatement`. Da notare che solo `:John` crede però nell'affermazione `_:johnStatement`. 
> 2. `_:friendship`, perché qui il soggetto di cui stiamo parlando è proprio l'amicizia stessa.
> 3. Non sapremmo nulla riguardo al `_friendship` che stiamo considerando.
> 4. Non stiamo dando la certezza che Mary sia in amicizia con Ann, ma stiamo solo descrivendo l'affermazione che John crede riguardo ad una loro ipotetica amicizia.
> 5. se vogliamo dire esplicitamente che l'amicizia è iniziata dal 2019, allora avremo dovuto aggiungere effettivamente le triple `:Mary :hasFriendship _:friendship . :Ann :isInFriendship _:friendship . _:friendship :since "2019-03-12"^^xsd:date .` ed invece  avremmo modifica la tripla `_:johnStatement rdf:object "2019"^^xsd:gYear .` con `_:johnStatement rdf:object "2021"^^xsd:gYear .`

## Prima di chiedere la correzione

- [x] Ho completato anche le spiegazioni, non soltanto il codice.
- [x] Ho controllato punti finali, virgolette, prefissi e maiuscole/minuscole.
- [x] Ho distinto `:Mary` da `_:Mary` e da `"Mary"`.
- [x] Per ogni nodo intermedio so dire se rappresenta una persona, una relazione o un'affermazione.
- [x] Ho distinto ciò che asserisco direttamente da ciò che attribuisco a qualcuno.

> [!tip] Come riprendere la correzione
> Scrivi in chat: “Ho svolto gli esercizi nella nota DM - Esercizi RDF - Graph Databases: correggili”. Puoi anche chiedere la correzione di un intervallo, per esempio 01–06, lasciando gli altri da svolgere.
