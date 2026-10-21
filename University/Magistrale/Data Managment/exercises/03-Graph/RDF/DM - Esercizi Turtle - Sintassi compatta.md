---
title: Turtle — Sintassi compatta ed esercizi
aliases:
  - DM — Esercizi Turtle
tags:
  - data-management
  - rdf
  - turtle
  - esercizi
source: "03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs.md; W3C RDF 1.1 Turtle"
---

# Turtle — Sintassi compatta ed esercizi

> [!abstract] Obiettivo
> Leggere e scrivere le abbreviazioni Turtle senza cambiare il grafo rappresentato. Partiamo da triple semplici e arriviamo ai blank node scritti con `[ ... ]`. Riferimento: [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Turtle|Nota 03 — Turtle]]. Gli esercizi precedenti sono in [[DM - Esercizi RDF - Graph Databases]].

## Prima di iniziare

I prefissi seguenti sono disponibili in tutti gli esempi e gli esercizi. Ogni esercizio è indipendente. Compila gli spazi di svolgimento; le soluzioni degli esercizi non sono incluse.

```turtle
@prefix : <https://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

**Abbreviare non significa aggiungere fatti o regole**: le scritture equivalenti rappresentano lo stesso grafo, anche se occupano un numero diverso di righe.

## Le quattro abbreviazioni

### Punto e virgola — stesso soggetto

```turtle
:Luca foaf:name "Luca" ;
      foaf:knows :Eva .
```

Espansione:

```turtle
:Luca foaf:name "Luca" .
:Luca foaf:knows :Eva .
```

Il `;` mantiene il soggetto. Dopo di esso scrivi un'altra coppia predicato-oggetto. L'andata a capo e l'indentazione servono alla leggibilità, non determinano quante triple ci sono.

### Virgola — stesso soggetto e predicato

```turtle
:Luca foaf:knows :Eva, :Nina .
```

Espansione:

```turtle
:Luca foaf:knows :Eva .
:Luca foaf:knows :Nina .
```

La `,` introduce un altro oggetto per lo stesso soggetto e predicato. Qui rappresentiamo due triple, non un unico oggetto composto da Eva e Nina.

### `a` — abbreviazione di `rdf:type`

```turtle
:Luca a foaf:Person .
```

Equivale a:

```turtle
:Luca rdf:type foaf:Person .
```

Si usa `a` nella posizione del predicato, senza `:`. Non introduce una nuova proprietà e non sostituisce una classe come `foaf:Person`.

### Parentesi quadre — un blank node senza etichetta

```turtle
:Luca foaf:knows [
    foaf:name "Eva" ;
    a foaf:Person
] .
```

Una possibile espansione, scegliendo un'etichetta nuova, è:

```turtle
:Luca foaf:knows _:persona .
_:persona foaf:name "Eva" .
_:persona rdf:type foaf:Person .
```

Il blocco `[ ... ]` rappresenta il nodo oggetto di `foaf:knows`. Al suo interno quel nodo è il soggetto delle proprietà elencate. Il punto finale chiude la costruzione esterna; non mettere un punto tra le coppie interne.

> [!important] Due blocchi, due nodi nel grafo
> Due occorrenze separate di `[ ... ]` introducono blank node distinti nella struttura del grafo, anche se contengono lo stesso nome. Non collegano esplicitamente i fatti allo stesso nodo. Questo non impone che i nodi denotino persone diverse nella realtà. Per riutilizzare esplicitamente un nodo in più punti, puoi dargli un'etichetta come `_:persona`.

| Segno | Che cosa mantieni o introduci? |
|---|---|
| `;` | Mantieni il soggetto. |
| `,` | Mantieni soggetto e predicato. |
| `a` | Usi `rdf:type` in forma abbreviata. |
| `[ ... ]` | Introduci un blank node e lo descrivi. |

Riferimento ufficiale: [W3C — Turtle](https://www.w3.org/TR/turtle/), sezioni 2.2 (Predicate Lists), 2.3 (Object Lists), 2.4 (IRIs, inclusa l'abbreviazione `a`) e 2.7 (Nesting Unlabeled Blank Nodes).

## 01 — Espandi il punto e virgola

- [x] Svolto

Riscrivi senza `;`, con una tripla completa per riga:

```turtle
:Mary foaf:name "Maria" ;
      foaf:knows :John ;
      rdf:type foaf:Person .
```

**Svolgimento**

```turtle
# Scrivi qui.
:Mary foaf:name "Maria" .
:Mary foaf:knows :John .
:Mary rdf:type foaf:Person . 
```

**Quante triple contiene il grafo? Qual è il soggetto di ciascuna?**

> Risposta: 3 triple ed il soggetto di ciascuna è :Mary

## 02 — Comprimi gli oggetti

- [x] Svolto

Riscrivi usando `,`, senza aggiungere triple:

```turtle
:Ann foaf:knows :John .
:Ann foaf:knows :Mary .
:Ann foaf:knows :Sara .
```

**Svolgimento**

```turtle
# Scrivi qui.
:Ann foaf:knows :John , :Mary , :Sara .
```

**Da questa scrittura si deduce che John conosce Mary? Perché?**

> Risposta: non si deduce questo. si deduce che `:Ann` conosce John, Mary e Sara. non possiamo concludere nulla su John ed i restanti perché non ci sono altre informazioni.

## 03 — Mescola le abbreviazioni

- [x] Svolto

Espandi completamente il blocco: niente `;`, `,` o `a`. Conta le triple distinte.

```turtle
:Ann a foaf:Person ;
     foaf:name "Anna", "Ann" ;
     foaf:knows :John, :Mary .
```

**Svolgimento**

```turtle
# Scrivi qui.
:Ann rdf:type foaf:Person .
:Ann foaf:name "Anna" .
:Ann foaf:name "Ann" .
:Ann foaf:knows :John .
:Ann foaf:knows :Mary .
```

> Numero di triple: 5

## 04 — Espandi le parentesi quadre

- [x] Svolto

Riscrivi con triple complete e un blank node etichettato, senza parentesi quadre né altre abbreviazioni:

```turtle
:John foaf:knows [
    a foaf:Person ;
    foaf:name "Sara" ;
    foaf:knows :Mary
] .
```

**Svolgimento**

```turtle
# Scrivi qui.
:John foaf:knows _:x .
_:x rdf:type foaf:Person .
_:x foaf:name "Sara" .
_:x foaf:knows :Mary .
```

**Chi è il soggetto di `foaf:name`? John oppure il nodo interno? Quante triple hai ottenuto?**

> Risposta: il soggetto è un [[Blank Node]] `_:x` che è una persona anonima di nome "Sara" che conosce Mary. John conosce questa persona anonima. ho ottenuto 4 triple.

## 05 — Un nodo condiviso e due nodi separati

- [ ] Svolto

Confronta questi grafi:

**A**

```turtle
:John foaf:knows _:p .
:Mary foaf:knows _:p .
_:p foaf:name "Sara" .
```

**B**

```turtle
:John foaf:knows [ foaf:name "Sara" ] .
:Mary foaf:knows [ foaf:name "Sara" ] .
```

1. Espandi B usando etichette nuove per i blank node.
2. Quale grafo collega esplicitamente John e Mary allo stesso nodo?
3. Il nome “Sara” uguale basta per fondere automaticamente i nodi di B?
4. Sono due grafi equivalenti? Motiva senza assumere che nomi uguali identifichino una sola persona.

**Svolgimento**

```turtle
# Espansione di B.
:John foaf:knows _:x .
_:x foaf:name "Sara" .
:Mary foaf:knows _:y .
_:y foaf:name "Sara" . 
```

> 2. Nessuno.  i due [[Blank Node]]s non sono uguali e non sono uniti
> 3. Assolutamente no: è un Litteral, una banale stringa e non una risorsa. 
> 4. Non sono due grafi equivalenti. i due [[Blank Node]]s possono essere risorse differenti con lo stesso nome.

## 06 — Reificazione in forma compatta

- [x] Svolto

Riscrivi il grafo usando `a` e `;`. Mantieni l'etichetta del blank node, perché John deve continuare a riferirsi a quello statement.

```turtle
_:s rdf:type rdf:Statement .
_:s rdf:subject :Rome .
_:s rdf:predicate :isIn .
_:s rdf:object :Italy .
:John :claims _:s .
```

**Svolgimento**

```turtle
# Scrivi qui.
_:s a rdf:Statement ; 
	rdf:subject :Rome ;
	rdf:predicate :isIn ;
	rdf:object :Italy .
:John  :claims _:s .
```

**La scrittura compatta asserisce automaticamente `:Rome :isIn :Italy .`? Quante triple hai conservato?**

> Risposta: Assolutamente no. Le scritture compatte sono solo delle abbreviazioni di sintassi ma non inserisce nessuna regola. Qui stiamo solo modellando una [[Reificazione]] di tale asserzione di modo da rappresentare un'affermazione detta da John che potrebbe non essere dimostrata o vera. 

> [!tip] Richiamo a distanza
> Domani espandi l'esercizio 03 senza consultare la tabella iniziale. Poi scrivi, a parole, la differenza fra `;` e `,`. Per qualsiasi dubbio, incolla il tentativo in chat o chiedimi di leggere questa nota.
