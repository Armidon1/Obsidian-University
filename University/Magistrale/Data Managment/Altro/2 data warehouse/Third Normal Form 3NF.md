La **Third Normal Form (3NF)**, o **terza forma normale**, è una proprietà degli schemi relazionali pensata per ridurre la ridondanza e prevenire anomalie durante inserimenti, modifiche e cancellazioni.

L’idea semplificata è:

> In una tabella in 3NF, gli attributi non appartenenti alla chiave devono dipendere dalla chiave, dalla chiave intera e non da altri attributi non-chiave.

## Esempio normalizzato male

Consideriamo:

```text
PRODUCT(
    product_id,
    product_name,
    type,
    category,
    department
)
```

La chiave è `product_id` e valgono queste dipendenze:

$product\_id\rightarrow type$ 
$type\rightarrow category$ 
$category\rightarrow department$

Per transitività:

$product\_id\rightarrow category$ 
$product\_id\rightarrow department$

Il problema è che `category` e `department` non dipendono dalla chiave soltanto in maniera diretta: possono essere ricavati attraversando attributi non-chiave:

$product\_id\rightarrow type\rightarrow category\rightarrow department$

Queste sono **dipendenze transitive dalla chiave**.

La tabella non è in 3NF perché esistono dipendenze come:

$type\rightarrow category$

nelle quali:

- `type` non è una superchiave della tabella;
    
- `category` non appartiene a una chiave candidata.
    

## Quale ridondanza produce?

Supponiamo che molti prodotti appartengano allo stesso tipo:

|product_id|product|type|category|department|
|--:|---|---|---|---|
|101|iPhone|Smartphone|Electronics|Technology|
|102|Galaxy|Smartphone|Electronics|Technology|
|103|Pixel|Smartphone|Electronics|Technology|

`Electronics` e `Technology` vengono ripetuti in ogni riga.

Questo può produrre anomalie:

- **Update anomaly:** per rinominare `Technology` dobbiamo modificare molte righe;
    
- **Insertion anomaly:** potremmo non riuscire a inserire un nuovo tipo finché non esiste almeno un prodotto;
    
- **Deletion anomaly:** eliminando l’ultimo prodotto di un tipo potremmo perdere anche le informazioni sul tipo.
    

## Come si raggiunge la 3NF?

Possiamo decomporre la tabella:

```text
PRODUCT(product_id, product_name, type_id)

TYPE(type_id, type_name, category_id)

CATEGORY(category_id, category_name, department_id)

DEPARTMENT(department_id, department_name)
```

Ora ogni informazione viene memorizzata una sola volta:

```text
PRODUCT → TYPE → CATEGORY → DEPARTMENT
```

Nel data warehousing questa struttura corrisponde sostanzialmente a uno **snowflake schema**.

## Definizione formale

Una relazione è in 3NF se, per ogni dipendenza funzionale non banale:

$X\rightarrow A$

vale almeno una delle condizioni seguenti:

1. XX è una superchiave;
    
2. AA è un attributo primo, cioè appartiene ad almeno una chiave candidata.
    

Nel nostro esempio:

$type\rightarrow category$

viola la 3NF perché `type` non identifica univocamente una riga di `PRODUCT` e `category` non appartiene alla chiave.

## Perché una dimension table viola intenzionalmente la 3NF?

In uno star schema manteniamo tutto nella stessa tabella:

```text
DIM_PRODUCT(
    product_sk,
    product_name,
    type,
    category,
    department
)
```

La ridondanza è accettata intenzionalmente perché una query deve eseguire un solo join:

```sql
SELECT d.category, SUM(f.revenue)
FROM FACT_SALE f
JOIN DIM_PRODUCT d
  ON f.product_sk = d.product_sk
GROUP BY d.category;
```

Se la dimensione fosse normalizzata, servirebbero più join:

```text
FACT_SALE
  → PRODUCT
  → TYPE
  → CATEGORY
  → DEPARTMENT
```

Quindi:

|Star schema|Snowflake schema|
|---|---|
|Dimensioni denormalizzate|Dimensioni normalizzate|
|Viola generalmente la 3NF|Può rispettare la 3NF|
|Dati descrittivi ripetuti|Minore ridondanza|
|Query più semplici|Query con più join|
|Ottimizzato per OLAP|Più vicino alla progettazione relazionale tradizionale|

La teoria della normalizzazione rimane valida: lo star schema accetta consapevolmente alcune anomalie e ridondanze perché il warehouse è prevalentemente letto tramite query analitiche e viene aggiornato attraverso processi ETL controllati, non tramite numerose transazioni concorrenti.