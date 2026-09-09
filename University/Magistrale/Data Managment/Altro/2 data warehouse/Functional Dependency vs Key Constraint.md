---
title: Functional Dependency vs Key Constraint
aliases:
  - Dipendenza funzionale e vincolo di chiave
  - FD vs Key
tags:
  - modello-relazionale
  - dipendenze-funzionali
  - chiavi
  - vincoli-integrita
  - rolap
related:
  - "[[Functional-Dependencies-Relational-and-ROLAP]]"
  - "[[Data-Warehousing-Complete-Notes]]"
---

# Functional Dependency vs Key Constraint

> [!abstract]
> Una **dipendenza funzionale** esprime una determinazione univoca tra insiemi di attributi. Un **vincolo di chiave** è un caso particolare di dipendenza funzionale nel quale il determinante identifica univocamente una tupla e, quindi, determina tutti gli attributi della relazione. Di conseguenza, ogni chiave è il determinante di una FD verso l'intero schema, ma non ogni FD definisce una chiave.

## Dipendenza funzionale

Sia dato lo schema relazionale:

$$
R(A_1,A_2,\ldots,A_n)
$$

Una dipendenza funzionale ha la forma:

$$
X \rightarrow Y
$$

dove $X$ e $Y$ sono insiemi di attributi di $R$.

La FD è soddisfatta se, per ogni coppia di tuple $t_1,t_2$:

$$
t_1[X]=t_2[X] \Rightarrow t_1[Y]=t_2[Y]
$$

In altre parole:

> Se due tuple hanno gli stessi valori per gli attributi di $X$, devono avere gli stessi valori anche per gli attributi di $Y$.

$X$ prende il nome di **determinante**, mentre $Y$ è l'insieme degli attributi determinati.

### Esempio

Consideriamo:

```text
PRODUCT(product_id, product_name, type, category)
```

Supponiamo che ogni prodotto appartenga a un solo tipo e ogni tipo a una sola categoria:

$$
product\_id \rightarrow product\_name,type,category
$$

$$
type \rightarrow category
$$

La seconda dipendenza stabilisce che due prodotti aventi lo stesso `type` devono avere anche la stessa `category`.

Tuttavia, `type` non determina necessariamente `product_id`, perché più prodotti possono appartenere allo stesso tipo.

| product_id | product_name | type | category |
|---:|---|---|---|
| 1 | Shiny | Detergent | Cleaning |
| 2 | Bleachy | Detergent | Cleaning |

Vale:

$$
type \rightarrow category
$$

ma non vale:

$$
type \rightarrow product\_id
$$

`type` è quindi un determinante, ma non è una chiave di `PRODUCT`.

## La FD come vincolo d'integrità

Una dipendenza funzionale è un **integrity constraint** perché stabilisce quali istanze della relazione sono ammesse.

Se dichiariamo:

$$
type \rightarrow category
$$

la seguente istanza è illegale:

| product_id | type | category |
|---:|---|---|
| 1 | Detergent | Cleaning |
| 2 | Detergent | Food |

Le due tuple concordano su `type`, ma non su `category`, violando la dipendenza funzionale.

> [!important]
> Una FD è una proprietà semantica dello schema e deve valere in ogni istanza valida. Il fatto che sia rispettata nei dati presenti in un determinato momento non basta a dimostrare che rappresenti una regola del dominio.

## Superchiave

Sia $U$ l'insieme di tutti gli attributi di una relazione $R$. Un insieme di attributi $K$ è una **superchiave** se determina tutti gli attributi della relazione:

$$
K \rightarrow U
$$

Equivalentemente:

$$
K \rightarrow R
$$

Consideriamo:

```text
STUDENT(student_id, tax_code, name, degree_programme)
```

Se `student_id` identifica univocamente uno studente, vale:

$$
student\_id \rightarrow tax\_code,name,degree\_programme
$$

Poiché `student_id` determina tutti gli attributi, è una superchiave.

Anche l'insieme:

```text
(student_id, name)
```

è una superchiave, perché contiene già `student_id`. `name`, però, è ridondante ai fini dell'identificazione.

## Chiave candidata

Una **candidate key** è una superchiave minimale. Deve rispettare due condizioni:

1. determina tutti gli attributi della relazione;
2. nessun suo sottoinsieme proprio determina tutti gli attributi.

Formalmente:

$$
K \rightarrow U
$$

e non deve esistere $K' \subset K$ tale che:

$$
K' \rightarrow U
$$

Pertanto:

- `(student_id, name)` è una superchiave;
- `student_id` è una candidate key, se da solo identifica lo studente;
- una candidate key scelta come identificatore principale diventa la **primary key**;
- le altre candidate key sono chiavi alternative.

## Key constraint

Un **key constraint** stabilisce che non possono esistere due tuple distinte con gli stessi valori della chiave.

Se `student_id` è una chiave, non sono ammesse due tuple come:

| student_id | name | degree_programme |
|---:|---|---|
| 101 | Alice | Computer Science |
| 101 | Bob | Economics |

Il vincolo di chiave implica la dipendenza:

$$
student\_id \rightarrow name,degree\_programme
$$

Infatti, se due tuple hanno lo stesso `student_id`, il key constraint impedisce che siano due tuple differenti. Di conseguenza, devono coincidere anche sugli altri attributi.

## Relazione tra FD e key constraint

La relazione fondamentale è:

$$
K\text{ è una superchiave di }R
\iff
K \rightarrow R
$$

Per una candidate key bisogna aggiungere la minimalità:

$$
K\text{ è candidate key}
\iff
K \rightarrow R
\text{ e }K\text{ è minimale}
$$

Quindi:

| Concetto | Condizione |
|---|---|
| Determinante di una FD | Determina almeno un insieme di attributi. |
| Superchiave | Determina tutti gli attributi della relazione. |
| Candidate key | È una superchiave minimale. |
| Primary key | È la candidate key scelta come identificatore principale. |

> [!summary]
> Il key constraint può essere espresso mediante una FD verso tutti gli attributi. Una FD generica, invece, può determinare solamente una parte della relazione e quindi non definire una chiave.

## Esempio con chiave composta

Consideriamo:

```text
ORDER_LINE(order_id, product_id, quantity, unit_price)
```

Supponiamo che ogni prodotto possa comparire al massimo una volta in ciascun ordine. Vale:

$$
(order\_id,product\_id) \rightarrow quantity,unit\_price
$$

La coppia `(order_id, product_id)` determina l'intera tupla ed è quindi una superchiave.

Non vale generalmente:

$$
order\_id \rightarrow quantity
$$

perché un ordine contiene più prodotti. Non vale neanche:

$$
product\_id \rightarrow quantity
$$

perché lo stesso prodotto compare in ordini differenti.

Poiché nessun attributo della coppia può essere rimosso, `(order_id, product_id)` è una candidate key.

Se il dominio permettesse allo stesso prodotto di apparire in più righe dello stesso ordine, la coppia non sarebbe più una chiave. Potrebbe essere necessario usare:

```text
(order_id, line_number)
```

Questo mostra che la chiave dipende dalla semantica e dalla granularità dei fatti rappresentati.

## Chiusura degli attributi

La chiusura $X^+$ contiene tutti gli attributi funzionalmente determinati da $X$ rispetto a un insieme di FD.

Per verificare se $X$ è una superchiave:

1. si calcola $X^+$;
2. si controlla se la chiusura contiene tutti gli attributi della relazione.

Data:

```text
R(order_id, product_id, customer_id, order_date, quantity)
```

con:

$$
order\_id \rightarrow customer\_id,order\_date
$$

$$
(order\_id,product\_id) \rightarrow quantity
$$

otteniamo:

$$
(order\_id,product\_id)^+
=
\{order\_id,product\_id,customer\_id,order\_date,quantity\}
$$

La chiusura contiene tutti gli attributi, quindi `(order_id, product_id)` è una superchiave. Se è anche minimale, è una candidate key.

## Perché studiare le FD che non definiscono chiavi?

Le FD con un determinante non chiave possono rivelare ridondanze e anomalie.

Nella relazione:

```text
PRODUCT(product_id, product_name, type, category)
```

abbiamo:

$$
product\_id \rightarrow type
$$

$$
type \rightarrow category
$$

La categoria viene ripetuta per tutti i prodotti dello stesso tipo. Questo può causare anomalie di aggiornamento, inserimento e cancellazione.

Nel modello relazionale normalizzato possiamo decomporre:

```text
PRODUCT(product_id, product_name, type_id)
TYPE(type_id, type, category)
```

Le FD non servono quindi solamente a trovare le chiavi: guidano anche la normalizzazione.

## Collegamento con ROLAP

In una dimension table di uno star schema possiamo avere:

```text
PRODUCT_DIM(
    product_key,
    product,
    type,
    category
)
```

Valgono:

$$
product\_key \rightarrow product,type,category
$$

$$
product \rightarrow type
$$

$$
type \rightarrow category
$$

`product_key` è una chiave perché determina l'intera tupla. `product` e `type` descrivono invece i passaggi della gerarchia dimensionale:

```mermaid
flowchart LR
    P["product"] --> T["type"]
    T --> C["category"]
    C --> A["all products"]
```

Le FD di gerarchia permettono un roll-up non ambiguo da prodotto a tipo e da tipo a categoria. Tuttavia, `type` non è una chiave della dimension table, perché molti prodotti possono avere lo stesso tipo.

Uno star schema mantiene intenzionalmente queste dipendenze transitive nella stessa dimension table per ridurre il numero di join. Uno snowflake schema può invece normalizzarle in tabelle separate.

## Chiave della fact table

Consideriamo:

```text
SALES_FACT(date_key, store_key, product_key, quantity, revenue)
```

Se la granularità è:

> Una riga rappresenta le vendite di un prodotto, in un negozio, in una data.

allora può valere:

$$
(date\_key,store\_key,product\_key)
\rightarrow quantity,revenue
$$

La combinazione delle chiavi dimensionali è una candidate key della fact table solamente se può esistere al massimo una riga per quella combinazione.

Se vengono registrate le singole righe degli scontrini, più eventi possono condividere data, negozio e prodotto. In quel caso la combinazione non identifica la tupla e occorre includere, per esempio, `receipt_key` e `line_number`.

> [!important]
> La chiave della fact table deriva dalla granularità dichiarata. Il semplice fatto che alcuni attributi siano foreign key verso le dimensioni non significa automaticamente che la loro combinazione sia una chiave.

## FD, key e foreign key

Una foreign key non è una dipendenza funzionale.

- La **FD** esprime determinazione univoca tra attributi.
- La **key** è un determinante dell'intera relazione.
- La **foreign key** impone che un valore referente corrisponda a una chiave esistente in un'altra relazione.

Esempio:

```text
EMPLOYEE(employee_id, name, department_id)
DEPARTMENT(department_id, department_name)
```

In `DEPARTMENT` vale:

$$
department\_id \rightarrow department\_name
$$

perché `department_id` è una chiave.

La foreign key `EMPLOYEE.department_id` garantisce che il dipartimento esista, ma non implica:

$$
department\_id \rightarrow employee\_id
$$

perché molti dipendenti possono appartenere allo stesso dipartimento.

## Formula da ricordare

> Una dipendenza funzionale $X \rightarrow Y$ stabilisce che $X$ determina univocamente $Y$. Se $X$ determina tutti gli attributi della relazione, allora $X$ è una superchiave. Se è anche minimale, è una candidate key.

In forma compatta:

$$
\text{Candidate key}
\subseteq
\text{Superkey}
\subseteq
\text{Determinanti di FD}
$$

La relazione di inclusione riguarda i concetti: tutte le candidate key sono superchiavi e tutte le superchiavi sono determinanti di dipendenze verso l'intero schema. Esistono però molti determinanti che non sono superchiavi.

## Domande di autoverifica

1. Che differenza esiste tra $X \rightarrow Y$ e $X \rightarrow R$?
2. Perché una candidate key deve essere minimale?
3. Può esistere una FD il cui determinante non sia una superchiave?
4. Come si utilizza la chiusura degli attributi per verificare una superchiave?
5. Perché `type -> category` non rende necessariamente `type` una chiave di `PRODUCT`?
6. Qual è il collegamento tra FD e normalizzazione?
7. In che modo le FD rappresentano le gerarchie dimensionali ROLAP?
8. Perché la chiave di una fact table dipende dalla sua granularità?
9. Perché una foreign key non è una FD?
