---
title: Data Warehousing - Complete Course Notes
aliases:
  - Data Warehousing
  - DW and OLAP
tags:
  - data-management
  - data-warehousing
  - olap
  - dimensional-modeling
  - university
source: 2-DataWarehousing.pdf
authors:
  - Domenico Lembo
  - Maurizio Lenzerini
reference: M. Golfarelli and S. Rizzi, Data Warehouse Design - Modern Principles and Methodologies, McGraw-Hill, 2009
---

# Data Warehousing

![[Pasted image 20260902131329.png]]
[[Data Warehouse Intro.excalidraw]]
> [!abstract]
> Data warehousing is the discipline concerned with collecting data from heterogeneous operational sources, reconciling it, preserving its history, and organizing it for analysis and decision support. A data warehouse does not replace operational databases. It complements them by serving a different workload: instead of efficiently recording individual business events, it makes large collections of historical events easy to explore, compare, and aggregate.

The central idea of this course is that **running an organization** and **understanding an organization** are different computational problems. Operational systems record what is happening: an order is placed, an examination is registered, a payment is received, or a patient is admitted. Decision-support systems use many such events to answer broader questions: How are sales changing? Which programmes are growing? What is the average waiting time? Which customer groups are most profitable?

The relational model, SQL, functional dependencies, keys, constraints, and normalization remain essential. Data warehousing does not discard them. It uses them in a different architectural and design context, where historical coverage, data integration, aggregation, and analytical performance are the main concerns.

## Contents

- [[#From Data to Information|From data to information and decision support]]
- [[#Data Warehouse Architectures|Data warehouse architectures]]
- [[#ETL Extraction Cleansing Transformation and Loading|ETL]]
- [[#The Multidimensional Data Model|The multidimensional data model]]
- [[#Accessing a Data Warehouse|Reports, dashboards, data mining, and OLAP]]
- [[#Implementing the Multidimensional Model|ROLAP, MOLAP, and hybrid implementation]]
- [[#The Need for a Design Methodology|Facts, grain, and design methodology]]
- [[#Conceptual Modelling for Data Warehouses|Conceptual modelling and DFM]]
- [[#Logical Models for Data Marts|Logical models for data marts]]
- [[#ROLAP The Star Schema|Star schemas]]
- [[#The Snowflake Schema|Snowflake schemas]]
- [[#Logical Design|Logical design and DFM translation]]
- [[#How the Whole Topic Fits Together|Final synthesis]]
- [[#Compact Glossary|Glossary]]
- [[#Questions for Self-Assessment|Self-assessment questions]]

## From Data to Information

Every organization accumulates a large amount of **primary data** through its daily activities. Each individual record is meaningful, but its strategic value is usually limited. A single sale tells us what happened in one transaction; it does not, by itself, tell us whether the company is improving.

Useful information is obtained through a progressive process of:

1. selecting the relevant operational data;
2. cleaning and integrating it;
3. grouping it according to meaningful business perspectives;
4. computing summaries, comparisons, and trends;
5. presenting the result as reports, dashboards, or interactive analyses.

As we move from raw data to strategic knowledge, **volume normally decreases while decision value increases**. Millions of transaction rows may become a report containing a few dozen indicators. This does not mean that detail is useless: detailed data is the evidence from which trustworthy summaries are derived.

> [!example]
> A university operational database may contain one row for every examination attempt. From those rows, an analytical system can derive the average grade by course, the pass rate by academic year, and long-term trends in student performance. The individual examination is data; the trend is information that may support a decision.

## Decision Support Systems

A **Decision Support System ([[DSS]])** is a set of interactive information technologies and analytical techniques designed to help people make decisions. The DSS is broader than the data warehouse:

- the **data warehouse** provides an integrated and historical data foundation (it is an actual data base);
- reports, dashboards, OLAP tools, data-mining algorithms, and what-if tools use that foundation;
- decision-makers interpret the results in their organizational context.

Historically, decision-support tools were mainly used to describe the past, identify problems, and reduce costs. Their role has progressively expanded toward anticipating the future, suggesting changes, and increasing profits or organizational effectiveness. Prediction does not eliminate uncertainty; it uses historical evidence to make uncertainty more manageable.

Data warehouses have served as the typical data back end of DSSs since the 1990s because decision support requires stable, reconciled data that should not depend on the temporary state or availability of operational applications.

## A Typical Scenario

Consider a large organization with many branches. Each branch may have its own operational database, software, identifiers, conventions, and history. Management wants to evaluate the contribution of each branch to the overall result.

Directly querying all source systems creates several difficulties:

- the sources may encode the same concept differently;
- some systems may be unavailable when an analysis is run;
- historical values may already have been overwritten;
- analytical queries may slow down operational transactions;
- different analysts may apply different definitions and obtain conflicting results.

A **data warehouse** addresses this situation by acting as an information repository that integrates and reorganizes data collected from multiple internal and external sources. It makes the reconciled data available for analysis, planning, and decision-making.

This definition contains three important ideas. First, warehouse data is normally **copied** from operational sources rather than created from nothing. Second, it is **reorganized according to analytical needs**, not merely collected. Third, the value of the warehouse comes from a shared interpretation of data, not from size alone.

## Operational Work and Decision-Support Work

At a university, day-to-day operations include transactions concerning classrooms, lectures, examinations, events, student procedures, and academic staff. These operations manipulate specific records and must complete reliably and quickly.

Decision-support operations ask a different kind of question:

- How has enrolment changed over the last decade?
- How do average grades vary across programmes?
- How many students graduate each year?
- Which facilities are underused?
- Is the time to graduation increasing?

The examples are domain-specific, but the distinction is general. A commercial organization records orders and later analyses demand. A hospital records admissions and later analyses outcomes and costs. A transport company records journeys and later analyses capacity and delays.

## OLTP and OLAP

**On-Line Transactional Processing (OLTP)** supports day-to-day operations. A typical OLTP request reads or writes a small number of tuples, often through a predefined application operation.

```sql
UPDATE EXAM
SET grade = 27
WHERE exam_id = 4581;
```

OLTP systems must provide low latency, concurrency control, integrity enforcement, and reliable transaction management. They are optimized for many users performing short, predictable operations.

**On-Line Analytical Processing (OLAP)** supports interactive analysis. A typical OLAP query scans and aggregates many records, often across several years and business dimensions.

```sql
SELECT academic_year, programme, AVG(grade) AS average_grade
FROM EXAM_FACT
GROUP BY academic_year, programme;
```

An analytical workload is usually exploratory. The result of one query inspires the next question, so the full workload cannot be frozen into application code beforehand.

Combining OLTP and OLAP on the same operational database creates conflicts:

- a large analytical scan competes with short transactions for CPU, memory, storage bandwidth, and locks;
- operational schemas are optimized for updates, not for broad aggregation;
- operational systems tend to preserve current state rather than long history;
- source-specific meanings make cross-system analysis unreliable.

One of the main goals of data warehousing is therefore to **separate OLAP from OLTP**, both physically and conceptually.

> [!note]
> “On-line” in OLTP and OLAP does not simply mean “on the Internet.” It indicates interactive access: users expect the system to respond while they are working.

## Application Areas

Data-warehouse technologies are useful wherever operational events accumulate and decisions require comparison across subjects, locations, and time. Common application areas include:

- **commerce:** sales, complaints, shipments, inventory, and customer care;
- **manufacturing:** production costs, suppliers, orders, inventory, and delivery;
- **financial services:** credit risk, investment analysis, and fraud detection;
- **transportation:** demand, fleet management, capacity, and maintenance;
- **telecommunications:** call traffic, network behaviour, customer profiles, and retention;
- **healthcare:** admissions, discharges, treatments, outcomes, and cost centres.

The technology is not tied to profit-oriented companies. Any organization with repeated events and decision-making requirements can benefit from the same principles.

## Organizational Complaints and Warehouse Requirements

Typical complaints about organizational data reveal the requirements of a data warehouse.

| Complaint | Underlying problem | Warehouse requirement |
|---|---|---|
| “We have a great deal of data, but cannot access it.” | Data is fragmented or too technical. | Accessibility through shared structures and tools. |
| “People with the same role obtain different results.” | Definitions and source data are inconsistent. | Integration based on a standard enterprise model. |
| “We need to select, group, and manipulate data in many ways.” | Questions are not known in advance. | Flexible, interactive queries. |
| “Show me only what matters.” | Raw detail hides decision-relevant patterns. | Summaries, measures, and multidimensional views. |
| “Some data is known to be wrong.” | Source quality is insufficient. | Cleansing, validation, correctness, and completeness. |

Consequently, data warehousing emphasizes accessibility for non-specialists, integrated definitions, flexible querying, multidimensional representation, and high-quality data.

## Definition and Fundamental Properties of a Data Warehouse

A data warehouse is a collection of data designed to support decision-making processes. According to the classical definition, it is **subject-oriented, integrated, time-variant, and non-volatile**. When we say "Integrated" we mean that the source of information/data comes from different databases and are being manipulated in a way to be more useful for a possible analysis. 

### Subject-Oriented Analysis

Operational systems are organized around applications and processes: ticket reservation, admission management, invoicing, or examination registration. Each application stores the information needed to execute its own workflow.

A warehouse is instead organized around stable **subjects of analysis**, such as customers, products, physicians, regions, students, or courses. “Subject” means a business theme, not a database table or a software application.

This shift allows information about the same subject to be combined across operational boundaries. For example, customer information may be distributed among sales, support, billing, and marketing systems. A subject-oriented warehouse reconciles those fragments so that the customer can be analysed as a coherent entity.

### Integrated and Consistent Data

Warehouse data comes from multiple operational databases and possibly external sources. Integration produces a unified view by resolving heterogeneity in:

- names and codes;
- data types and formats;
- units of measure and currencies;
- levels of detail;
- identifiers for the same real-world entity;
- definitions of measures and categories.

Integration does not usually add new observations about reality. It mainly **rearranges and reconciles existing information**. Derived measures may be computed, but they remain grounded in source facts. The difference beetwen Rearrange (riorganizzazione) and reconcile (conciliazione) is that rearrange works on the actual structure of database/tables (like changing how data are being stored for optimization purposes) while the reconcile is somithing that resolvs the ambiguity of the data (like 2 guys with the exact same ID is not acceptable). 

Notice that **External Sources** comes from open databases or, in general, open data that are available Online. Never understimate how powerfull are those data and how easy are accessible. Many people don't know that they even exists and where to find them.

### Evolution over Time

Operational databases normally focus on current state. When a value changes, the previous value may be overwritten. A warehouse must support historical analysis, so it stores observations covering a longer time interval and grows through periodic loading.

Time becomes part of fact identification. For example, the number of students in a programme is not identified by the programme alone but by the programme together with an academic period.

```text
(Computer Science, 2024) -> 1,250 enrolled students
(Computer Science, 2025) -> 1,340 enrolled students
```

More generally, the same entity or event type may appear at several dates, snapshots, or validity intervals. This historical depth makes trends and comparisons possible.

### Non-Volatility

Operational records are continuously inserted, updated, and deleted. Warehouse data is mainly accessed in read-only mode and changed through controlled loading processes. Previously loaded history is not routinely overwritten by end-user transactions.

Non-volatility does not literally mean that the database can never be corrected, archived, or changed. It means that analytical history is stable: ordinary business operations do not mutate it directly. This reduces the need for the advanced transaction-management behaviour required by operational applications. The main technical concerns instead become query throughput, availability, scalability, and resilience under large analytical scans.

## Operational and Analytical Queries

Operational queries generally access a small number of tuples in several normalized tables connected by simple relationships. Their core workload is known in advance because it is embedded in application functions. Ad hoc queries are occasional.

Analytical queries perform dynamic, multidimensional analyses. They may scan millions of records and compute numeric summaries of organizational performance. Interactivity is essential, because an analysis session evolves as the user interprets intermediate results.

| Feature | Operational databases | Data warehouses |
|---|---|---|
| Typical users | Thousands of operational users | Hundreds of analysts and decision-makers |
| Workload | Preset transactions | Specific and evolving analysis queries |
| Access pattern | Hundreds of records; read and write | Millions of records; mainly read-only |
| Goal | Execute application processes | Support decisions |
| Data | Detailed, numeric and alphanumeric | Often summarized and mainly numeric, while retaining useful detail |
| Integration | Application-oriented | Subject-oriented |
| Quality focus | Integrity of individual transactions | Consistency across sources and time |
| Time coverage | Mainly current data | Current and historical data |
| Updates | Continuous | Periodic and controlled |
| Model | Usually normalized | Often denormalized and multidimensional |
| Optimization | Fast access to a small database portion | Fast analysis of a large database portion |

The distinction is not absolute: operational databases may keep history, and modern warehouses may ingest data frequently. The table describes the dominant design priorities.


# Data Warehouse Architectures

Architecture determines where data is physically stored, where integration occurs, and how clearly OLTP is separated from OLAP. Three reference architectures are considered: single-layer, two-layer, and three-layer.

## Single-Layer Architecture (nobody uses it anymore)

![[Pasted image 20260902131504.png]]

A single-layer architecture minimizes data replication by leaving the only physical data in the source systems. The “warehouse” is virtual: middleware interprets analytical requests and submits them directly to operational sources.

This approach has serious limitations:

- it fails to isolate OLAP workloads from OLTP workloads;
- integration is performed at query time and may be incomplete or inconsistent;
- historical coverage cannot exceed what the sources retain;
- source availability directly determines analytical availability;
- complex requests may interfere with essential transactions.

The architecture can be acceptable when analytical needs are narrow, sources are few and stable, and data volumes are small. It is rarely the preferred solution for a broad enterprise warehouse.

This was an historical reality: before the storage was really expensive, so the middleware extracts values from the operational databases, modifies it in real time and retrieves informations to the manager: no real data warehouse here. 

## Two-Layer Architecture

![[Pasted image 20260902131526.png]]

The two-layer architecture introduces a physical warehouse layer distinct from the source layer. Operational and external data is extracted through ETL processes, temporarily handled in a **data-staging area**, and loaded into a **primary data warehouse**. Reporting, OLAP, data-mining, and what-if tools query the warehouse rather than the operational sources.

**Metadata** accompanies the warehouse. It describes schemas, mappings, transformations, data origins, loading rules, quality information, and business definitions. Metadata makes the warehouse understandable and manageable; without it, users see values but cannot reliably interpret how they were produced.

But there is no entity that integrates and cleans those raw data, so the result can be problematic.  

### Data Marts

A **data mart** is a subset or aggregation of warehouse data relevant to a particular business area, department, or user category. A marketing data mart may focus on campaigns and customer behaviour, whereas a finance data mart may focus on revenue, cost, and risk. **Basically a data mart is a subset of data warehouse, that is preciselly for a specific Organization's department, where for "subset" we intend not only a smaller portion of the data, but also organized differently and with differents structures for an optimized result**. For istance: the marketing department could have its own little data warehouse and we will call it as data mart marketing. Do you remember the "Subject Oriented" view? Well, the data mart is the technology that enhance this property.

Data marts populated from a primary warehouse are called **dependent data marts**. 

![[Pasted image 20260902151752.png]]
They are useful because:

- they support incremental warehouse development;
- each one focuses on the needs of a specific user group;
- their smaller size can improve query performance;
- they inherit common definitions and quality rules from the primary warehouse.

An **independent data mart** is populated directly from source systems, without a primary enterprise warehouse. 
![[Pasted image 20260902151814.png]]This can shorten an isolated project, but independent marts may define the same concepts differently and produce incompatible results. A local optimization may therefore create an enterprise integration problem.

### Advantages of Physical Separation

The two-layer architecture offers several advantages:

- high-quality information remains available even if a source is temporarily inaccessible;
- analytical queries do not interfere with transaction processing;
- the warehouse can expose a multidimensional organization even when sources are relational or semi-structured;
- the mismatch between current detailed OLTP data and historical summarized OLAP data can be handled explicitly;
- schemas, indexes, partitions, and materialized views can be optimized specifically for analysis.

## Three-Layer Architecture

![[Pasted image 20260902131543.png]]

The three-layer architecture introduces a **reconciled data layer** between sources and the warehouse. This layer materializes detailed operational data after integration and cleansing. It therefore contains data that is already correct, consistent, and expressed according to a common enterprise model, but is not yet necessarily organized for a particular analytical fact. The Reconcilied Data can be seen as a database that contains the PERFECT and reorganized data from the operatiional data and external data. 

The layers have distinct responsibilities:

1. the **source layer** contains operational and external data;
2. the **reconciled layer** separates source extraction and integration from analytical organization;
3. the **warehouse layer** stores subject-oriented historical data, possibly feeding data marts;
4. analysis tools consume warehouse information.

The main advantage is separation of concerns. Source-specific problems are resolved once in the reconciled layer, which becomes a reusable enterprise reference. Warehouse population can then concentrate on dimensions, facts, granularity, and analytical performance.

What is the difference between Primary datawarehouse and reconciled database? The Primary datawarehouse may be built with different technologies and not only with [[Relational Data Model|Relational Data Technology]], while in the reconciled database tipically is a relational database. So for instance the reconciled database can be MariaDB, PostgreSQL or whatsoever relational database, while the primary data warehouse can be whatever database, like also a Graph database or [[MongoDB]] NoSQL databses.

The cost is additional storage, data replication, and design complexity. Whether the extra layer is justified depends on the number and heterogeneity of sources, the need for reusable integrated detail, and organizational governance. Here we have also 2 times the ETL that moves twice the data, which costs more, most we have a cleaner result. This is something that many organization wants to have, although is very difficult to achive. 

Domanda: differenza tra ETL e Reconciled layer?

But what about the Meta-Data? By meta data here we mean those extra tables/databases that are being automatically created from the database engine (like in PostgreSQL), for instance those information.table that contains which attribuse are in specifics tables or which tables there exists in a specific database. those informazion are usefull in a perspective of a third service which has to know from the outside how the database is organized. 

# ETL: Extraction, Cleansing, Transformation, and Loading

ETL is very massive concept, there are massive tools sold by vendors like Oracles or many opensource. There is another course that talks only about this. We are just going to talk what actually this fucking thing is. 

**ETL** is the process that extracts data from sources, improves and integrates it, converts it to the target representation, and loads it into the warehouse. At an abstract level, ETL aims to produce a single, high-quality, detailed view of relevant source data. This process is also called **reconciliation**.

Reconciliation occurs at least twice conceptually:

- during the initial population of the warehouse;
- during every later update cycle.

Some literature merges cleansing and transformation. In this course, cleansing mainly corrects **values**, while transformation mainly corrects or changes **formats and structures**. In practice, the two are closely connected.

## Extraction
![[Pasted image 20260902160712.png]]

Extraction determines which source data enters the pipeline and how changes are detected.

**Static extraction** is used for initial population. It resembles a snapshot of the relevant operational data at a particular time. Because the first load can be large, its consistency and timing require careful planning.

**Incremental extraction** captures changes made since the previous extraction. Common techniques include:

- reading the transaction log maintained by the source DBMS;
- selecting rows according to reliable timestamps;
- receiving source-driven events or change notifications.

Incremental extraction is more efficient than copying the entire source repeatedly, but it is also more delicate. The process must not miss changes, duplicate them, or apply them in the wrong order. Deletes, late-arriving data, clock differences, and failed runs require explicit handling.

Data relevance and quality affect extraction choices. Not every source field belongs in the warehouse, and a field that cannot be interpreted reliably may need additional governance before use.

## Cleansing

![[Pasted image 20260902161314.png]]

Cleansing improves data quality. Common source problems include:

- duplicate records;
- logically inconsistent values, such as a city and postal code that do not correspond;
- missing data;
- unexpected use of fields;
- impossible or incorrect values;
- inconsistent representations caused by abbreviations or local conventions;
- typing mistakes;
- several identifiers for the same real-world entity.

Cleansing rules may reject a record, repair it, standardize it, flag it for review, or preserve it with a quality indicator. A correction must be explainable: silently inventing a value can make the warehouse look complete while reducing trust.

> [!example]
> A customer record written as one free-text block can first be parsed into first name, last name, street, postal code, city, and country. “Downing St.” and “United Kingdom” can then be standardized. Finally, the postal code can be validated and corrected if authoritative evidence shows that it is inconsistent with the address. Formatting, standardization, and correction are different operations even when they occur in the same pipeline.

## Transformation

![[Pasted image 20260902161324.png]]

Transformation maps heterogeneous source representations into the warehouse representation. The mapping can be difficult because sources may contain different schemas, units, encodings, and levels of granularity, as well as unstructured text that hides useful information.

Typical transformations used to populate a reconciled layer include:

- **conversion and standardization:** aligning storage formats, units, currencies, dates, and codes;
- **matching:** determining which fields or entities in different sources are equivalent;
- **selection:** retaining only relevant fields and records;
- **derivation:** computing a target value from one or more source values.

Transformations used to populate the analytical warehouse also include:

- replacing operational normalization with controlled denormalization;
- aggregating detailed data to selected granularities;
- assigning surrogate keys to dimension members;
- deriving measures according to shared business rules.

The transformation layer is where technical mappings and business semantics meet. For example, adding two revenue values is meaningful only after currency, taxation, return handling, and time conventions have been aligned.

![[Pasted image 20260902160737.png]]

The last part can be in a JSON format. the standardization is being done with the usage of more metadata maybe. 

## Loading

![[Pasted image 20260902161335.png]]

Loading writes the transformed data into the warehouse.

A **refresh** completely rewrites warehouse data. It is normally associated with static extraction and initial population. Refreshing can also be suitable for a small derived table when full reconstruction is simpler and safer than change tracking.

An **update** adds changes detected through incremental extraction. In the classical warehouse model, an update normally appends new information without deleting or overwriting pre-existing history.

Loading is not just insertion. A reliable load must coordinate referential integrity, dimension keys, fact granularity, duplicate prevention, late data, error recovery, and metadata about when and how the load was executed.

> [!summary]
> Extraction asks **what changed?** Cleansing asks **is the value trustworthy?** Transformation asks **how should it be represented and interpreted?** Loading asks **how can it be incorporated safely into warehouse history?**

**WE WILL CONCENTRATE MORE IN THE ETL PART IN THE O-LAB PART**. Howewer Loading we have the problem of "when do you move data": We have to decide something like "everynight", and the decision is up to the company.
# The Multidimensional Data Model

The question now is: Well, now what do we have in the data warehouse? a multidimensional data: what it is? See the Three dimensional sales cube example later.

The multidimensional model describes how users conceptually see and query a warehouse. It is not necessarily the physical storage model. A relational DBMS can implement the same multidimensional view through tables, keys, and SQL.

Organization-specific phenomena are represented as **facts**. A fact is viewed as a point in a multidimensional space, or informally as a cell in a cube:

- each axis is a **dimension** relevant to the analysis;
- each cell contains one or more numerical **measures**;
- each dimension may have a **hierarchy** that supports progressively coarser levels of analysis. The idea is: a single date (a specific dimension for instance, see the three-dimensional sales cube) can be aggregated in a moth, a motnh ina year, a year in a decay, so this means that an associated date we can have an hierarchy of possible analysis. But why is it important? it is, because we would like to know how can we aggregate that dimension.



## A Three-Dimensional Sales Cube

![[Pasted image 20260902161522.png]]

Suppose that ten packages of a particular detergent are sold in one store on a particular date. The event has three coordinates:

```text
product = Shiny
store   = EverMore
date    = 2008-05-04
```

and a measure:

```text
quantity = 10
```

The conceptual cube has `product`, `store`, and `date` as axes. The cell at their intersection stores the measure. A real system is not limited to three dimensions; the cube metaphor is used because three-dimensional geometry makes the idea easy to visualize.

The **grain** of this fact is “one product, in one store, on one date.” Grain states exactly what one fact record represents. It must be fixed before measures are interpreted, because `quantity = 10` is ambiguous without its coordinates and level of detail.

Notice: every cell can be interpreted as a tuple (product, store, date): i could represent a tuple as a cell of a n-dimensional way, and a grain is a specific value that can be retrieved by joining more tables with a proper key constraint. This kind of view helps a lot in comapare to the "table" view of the relational database. In math this is an appliction of the isomorphism property: the capability to change the system from A to B wihtout loosing informations and revert from B to A. Key constraints in the end is an application of a bigger math property called function contraint.

Now when we see a cube, we should also be able to see the hierarchie behind of it.

## Hierarchies and Functional Dependencies

![[Pasted image 20260902172412.png]]

A dimension can be described at several aggregation levels. For example:

```text
product -> type -> category -> all products
store   -> city -> region -> all stores
date    -> month -> quarter -> year -> all dates
```

Each arrow expresses a many-to-one relationship and normally a functional dependency. If each product has exactly one type and each type belongs to exactly one category, then:

$$
product \rightarrow type, \qquad type \rightarrow category
$$

By transitivity:

$$
product \rightarrow category
$$

These dependencies make aggregation semantically well-defined. We can group product-level facts by type or category because every product determines one member at each higher level.

“All products” and “all stores” represent the top of the corresponding hierarchies. Aggregating to that level removes the distinction among individual members of the dimension.

Notice: an hierarchie is a tree, a tree is a graph and a graph is an application of a RELATION. I can represent it as a Relation.

### Spiegotto più chiaro

Il professore sta mostrando gerarchie e dipendenze funzionali perché sono il “ponte” tra:

- la visione multidimensionale a cubo usata dall’utente;
    
- la rappresentazione relazionale usata dal DBMS;
    
- le operazioni di aggregazione OLAP, come il roll-up.
    

Il punto non è soltanto classificare i prodotti: bisogna formalizzare perché possiamo passare correttamente da vendite per prodotto a vendite per tipo o categoria.

#### Il cubo al livello più dettagliato

Supponiamo di analizzare le vendite attraverso tre dimensioni:

```text
product × store × date
```

Ogni cella contiene una misura:

```text
quantity sold
```

Una cella potrebbe quindi essere:

```text
(product = P1, store = S1, date = D1) → quantity = 10
```

Possiamo pensare al cubo come a una funzione parziale:

$$C : Product \times Store \times Date \rightarrow Quantity$$

È parziale perché non tutte le combinazioni possibili corrispondono a una vendita realmente avvenuta.

#### La rappresentazione relazionale equivalente

Lo stesso contenuto può essere rappresentato con una relazione:

```text
SALES(product, store, date, quantity)
```

|product|store|date|quantity|
|---|---|---|--:|
|P1|S1|D1|10|
|P2|S1|D1|5|
|P3|S2|D1|8|

La corrispondenza è:

|Modello multidimensionale|Modello relazionale|
|---|---|
|Asse del cubo|Attributo dimensionale|
|Coordinata|Valore dell’attributo|
|Cella|Tupla della fact table|
|Contenuto della cella|Misura|
|Cella vuota|Assenza della tupla|

Quindi:

```text
Cella del cubo:
(P1, S1, D1) → 10

Tupla relazionale:
(P1, S1, D1, 10)
```

Questo è probabilmente ciò che il professore chiama “isomorfismo”: la stessa informazione può essere vista come un insieme di celle multidimensionali oppure come un insieme di tuple relazionali.

#### Dove entrano le gerarchie?

Le coordinate del cubo precedente sono al livello più dettagliato:

```text
product
store
date
```

Ma un utente non vuole necessariamente analizzare sempre le singole vendite. Potrebbe voler conoscere:

- le vendite per tipo di prodotto;
    
- le vendite per categoria;
    
- le vendite per città;
    
- le vendite per regione;
    
- le vendite per mese o anno.
    

Per rendere possibili questi passaggi, ogni dimensione contiene una gerarchia:

```text
product -> type -> category -> all products
store   -> city -> region -> all stores
date    -> month -> quarter -> year -> all dates
```

La gerarchia indica i livelli ai quali possiamo osservare e aggregare i fatti.

#### Perché gli archi sono dipendenze funzionali?

Prendiamo:

```text
product -> type -> category
```

Immaginiamo questi dati:

|product|type|category|
|---|---|---|
|Shiny|Detergent|House cleaning|
|Bleachy|Detergent|House cleaning|
|CleanHand|Soap|House cleaning|
|DrinkMe|Soft drink|Food|

La dipendenza:
$$product \rightarrow type$$

significa che, dato un prodotto, il suo tipo è determinato univocamente.

Non possono quindi esistere due tuple come:

|product|type|
|---|---|
|Shiny|Detergent|
|Shiny|Soft drink|

Allo stesso modo:

$type→category$

significa che ogni tipo appartiene a una sola categoria.

Grazie alla transitività:

$$product \rightarrow type \quad\land\quad type \rightarrow category \quad\Rightarrow\quad product \rightarrow category$$

Conoscendo un prodotto possiamo quindi determinare senza ambiguità anche la sua categoria.

#### Perché questo è necessario per l’aggregazione?

Supponiamo di avere le vendite dettagliate:

|product|quantity|
|---|--:|
|Shiny|10|
|Bleachy|15|
|CleanHand|7|
|DrinkMe|20|

Vogliamo passare dalle vendite per prodotto alle vendite per tipo:

|type|total quantity|
|---|--:|
|Detergent|25|
|Soap|7|
|Soft drink|20|

Questa operazione è un **roll-up**:

```text
product → type
```

È possibile perché ogni prodotto determina esattamente un tipo. Ogni vendita viene quindi assegnata a un solo gruppo.

Possiamo poi fare un altro roll-up:

```text
type → category
```

ottenendo:

|category|total quantity|
|---|--:|
|House cleaning|32|
|Food|20|

Le dipendenze funzionali garantiscono che ogni fatto dettagliato abbia un percorso di aggregazione univoco:

```text
Shiny
  ↓
Detergent
  ↓
House cleaning
  ↓
All products
```

#### Traduzione del roll-up in SQL

In uno star schema potremmo avere:

```text
SALES(product_key, store_key, date_key, quantity)

PRODUCT(
    product_key,
    product,
    type,
    category
)
```

Il cubo dettagliato per prodotto corrisponde a:

```sql
SELECT
    p.product,
    SUM(f.quantity) AS total_quantity
FROM SALES AS f
JOIN PRODUCT AS p
    ON f.product_key = p.product_key
GROUP BY p.product;
```

Il roll-up da `product` a `type` cambia il livello del `GROUP BY`:

```sql
SELECT
    p.type,
    SUM(f.quantity) AS total_quantity
FROM SALES AS f
JOIN PRODUCT AS p
    ON f.product_key = p.product_key
GROUP BY p.type;
```

Il roll-up fino a `category` diventa:

```sql
SELECT
    p.category,
    SUM(f.quantity) AS total_quantity
FROM SALES AS f
JOIN PRODUCT AS p
    ON f.product_key = p.product_key
GROUP BY p.category;
```

Quindi, nel modello multidimensionale diciamo:

```text
Roll-up: product → type → category
```

Nel modello relazionale eseguiamo:

```text
JOIN con la dimension table
+
GROUP BY sull’attributo del livello desiderato
+
funzione di aggregazione sulla misura
```

#### Come cambia il cubo

Il cubo di partenza potrebbe essere:

```text
product × store × date
```

Dopo un roll-up su tutte le dimensioni:

```text
type × city × month
```

La nuova cella:

```text
(Detergent, Rome, January) → 2,500
```

riassume tutte le celle dettagliate relative:

- ai prodotti di tipo `Detergent`;
    
- ai negozi situati a `Rome`;
    
- alle date appartenenti a `January`.
    

Le gerarchie definiscono quindi quali celle dettagliate devono essere raccolte nella stessa cella aggregata.

#### Perché serve l’unicità?

Supponiamo che un prodotto possa appartenere contemporaneamente a due tipi:

```text
P1 → Type A
P1 → Type B
```

Se `P1` ha venduto 10 unità, aggregando per tipo potremmo ottenere:

|type|quantity|
|---|--:|
|Type A|10|
|Type B|10|

Il totale diventerebbe 20, anche se sono state vendute solo 10 unità.

Questo succede perché non abbiamo più una relazione many-to-one:
$$product \not\rightarrow type$$

Abbiamo una relazione many-to-many. Non è una gerarchia semplice e richiede una modellazione diversa, ad esempio una bridge table e, talvolta, dei pesi di allocazione.

Le dipendenze funzionali garantiscono quindi la proprietà di **summarizability**: la possibilità di aggregare senza duplicazioni o ambiguità.

#### Il significato di “All products”

`All products` è il livello più alto della gerarchia:

```text
product → type → category → all products
```

Tutti i prodotti appartengono allo stesso membro finale, che possiamo immaginare come una costante:

```text
Shiny    → All products
Bleachy  → All products
DrinkMe  → All products
```

Aggregare a questo livello significa eliminare completamente la distinzione tra prodotti:

```sql
SELECT SUM(quantity)
FROM SALES;
```

Otteniamo il totale generale delle vendite rispetto alla dimensione prodotto.

Analogamente:

```text
all stores → non distinguiamo più i negozi
all dates  → non distinguiamo più i periodi
```

Se aggreghiamo tutte le dimensioni al livello `All`, otteniamo una sola cella: il totale complessivo dell’intero cubo.

#### Il senso del discorso del professore

La sequenza logica è questa:

1. Un fatto multidimensionale è identificato dalle coordinate del cubo.
    
2. Una cella può essere rappresentata come una tupla relazionale.
    
3. Le dimensioni hanno livelli di dettaglio organizzati in gerarchie.
    
4. Gli archi delle gerarchie corrispondono a dipendenze funzionali many-to-one.
    
5. Le dipendenze funzionali rendono univoco il passaggio dal dettaglio ai livelli superiori.
    
6. Il roll-up multidimensionale viene implementato relazionalmente attraverso `JOIN`, `GROUP BY` e funzioni di aggregazione.
    

La frase da ricordare è:

> Le gerarchie definiscono i livelli ai quali un cubo può essere aggregato; le dipendenze funzionali garantiscono che ogni valore dettagliato appartenga in modo univoco a un valore del livello superiore.

In forma estremamente compatta:
![[Pasted image 20260902174716.png]]

## Restrictions: Slicing, Dicing, and Projection

Restrictions select a portion of a cube.

**Slicing** fixes one or more dimensions to a specific value. Fixing `store = EverMore`, for example, removes store as a varying axis and returns a lower-dimensional view over product and date.

**Dicing** applies more general selection predicates, possibly involving higher hierarchy levels:

```text
year = 2008
region = Florida
category = Food
```

Dicing selects a sub-cube but does not itself imply aggregation. If data is filtered to Florida, individual Florida stores may still remain visible.

**Projection** selects only a subset of measures. A cube containing quantity, revenue, and number of receipts can be projected onto revenue alone.

These operations correspond to familiar relational ideas, but are expressed in analytical vocabulary: slice and dice resemble selections, while projection keeps selected measures.

## Aggregation

Aggregation replaces fine-grained facts with coarser **secondary events**. Daily sales by product and store may be aggregated into monthly sales by product type and city. Each coarser cell summarizes all compatible detailed cells.

For an additive quantity measure, a coarse value can be computed by `SUM`. If several products of one type sold quantities 2,800, 1,700, and 2,000, their type-level quantity is 6,500.

Aggregation can occur along one or several dimensions:

- date to month, quarter, or year;
- product to type or category;
- store to city or region.

Precomputed aggregates improve response time but consume storage and require maintenance. This trade-off will reappear in materialized views and MOLAP cubes.

# Accessing a Data Warehouse

Once data has been extracted, cleansed, integrated, transformed, and loaded, it must be turned into useful information. Four principal access approaches are considered: reports, dashboards, data mining, and OLAP.

They differ in how much the question is known in advance and how actively the user explores the result.

| Approach | Typical purpose | User interaction |
|---|---|---|
| Reports | Distribute predefined information periodically | Mostly passive |
| Dashboards | Monitor a limited set of important indicators | Quick inspection and limited filtering |
| Data mining | Discover patterns not explicitly specified as ordinary queries | Model-driven discovery |
| OLAP | Explore facts across dimensions and detail levels | Active, iterative navigation |

## Reports

Reports serve users who need information in an essentially static structure at predetermined intervals. A monthly revenue report might always show the same product categories and the latest three months.

Reports are appropriate when the information requirement is stable, the audience should not need technical knowledge, and consistency of presentation matters. Their limitation is the same property that makes them simple: the designer decides the structure in advance.

## Dashboards

A dashboard presents a concise overview of relevant phenomena through indicators, tables, charts, and alerts. The term is a metaphor from a vehicle dashboard: a limited number of instruments should tell the operator whether the system is behaving normally.

Dashboards are often used by senior managers because they compress complex data into a quick view. Their effectiveness depends less on decorative graphics than on careful selection and definition of **key performance indicators**. A misleading indicator remains misleading even if it is visually attractive.

Dashboards are not a replacement for deeper analysis. When an indicator reveals a problem, an OLAP or specialized analysis tool is needed to investigate its causes.

## Data Mining

Data mining searches large data collections for significant patterns that users may not discover through ordinary queries. It combines techniques from statistics, artificial intelligence, machine learning, and pattern recognition.

An SQL query normally asks for a pattern that the user has already formulated, such as average revenue by region. Data mining is used when the user can specify the phenomenon and available data but does not already know the relationship to retrieve.

Applications include market segmentation, buying-habit analysis, fraud detection, risk assessment, clinical analysis, epidemiology, investment modelling, and recognition of similar event sequences.

### Association Rules

An association rule has the form:

$$
X \Rightarrow Y
$$

For example, `{shoes} => {socks}` suggests that transactions containing shoes tend also to contain socks. It does not by itself establish causation.

Two measures evaluate a rule:

$$
support(X \Rightarrow Y) = \frac{\#(transactions\ containing\ X \cup Y)}{\#(all\ transactions)}
$$

$$
confidence(X \Rightarrow Y) = \frac{\#(transactions\ containing\ X \cup Y)}{\#(transactions\ containing\ X)}
$$

Support measures how common the combined pattern is. Confidence estimates how often `Y` occurs among transactions containing `X`. A rule with high confidence but extremely low support may be unreliable or commercially unimportant, so both measures matter.

Association-rule extraction searches for rules above chosen support and confidence thresholds. Apriori is a classical algorithm. Common applications include targeted advertising, supermarket shelf placement, market-basket analysis, and analysis of substitution when a product is unavailable.

### Clustering

Clustering represents objects as points in a multidimensional feature space and groups similar objects into a smaller number of clusters. No class label is supplied beforehand; the goal is to discover structure in the population.

Possible applications include customer segmentation, grouping clinical cases by symptoms, and identifying epidemiological patterns. The interpretation of a cluster is a human and domain task: an algorithm can identify proximity without automatically explaining its business meaning.

### Classifiers and Decision Trees

Classification starts with a **training set** containing known categories and examples already labelled with those categories. A classifier learns a profile or decision boundary and assigns new items to a category.

A decision tree is an interpretable classifier that recursively tests attributes. For example, a risk model might first test age, then car type, and finally assign a high or low risk class. Decision trees are useful not only for prediction but also for understanding which conditions lead to a result.

Applications include credit, mortgage, loan, and insurance risk assessment. Because classification affects real decisions, label quality, bias, error costs, and validation must be considered in addition to predictive accuracy.

### Time Series

Time-series analysis examines ordered sequences of measurements to identify recurring, changing, or atypical patterns. Applications include:

- identifying correlated movements in financial instruments;
- revealing anomalies in monitoring systems;
- comparing organizational growth trajectories;
- analysing navigation paths and other event sequences.

Order is essential: the same set of values arranged differently can represent a different trend.

## OLAP

OLAP is the most characteristic way to exploit warehouse information. It allows users whose questions cannot be fully specified beforehand to explore data interactively according to the multidimensional model.

Unlike a report reader, an OLAP user plays an active role. The user begins with one view, interprets it, and changes the level of detail, dimensions, or filters to formulate the next view. This requires:

- knowledge of the business meaning of the data;
- support for complex queries;
- an interface understandable to users who may not write SQL;
- acceptable response times across an evolving sequence of queries.

## The OLAP Session

An OLAP session is a **navigation path** through a fact. The user changes viewpoints and levels of detail one step at a time. Each step is represented by an OLAP operator that transforms the previous query into a new one.

Results are multidimensional even when displayed as two-dimensional tables. Multiple headers, nested rows and columns, colours, and interactive controls preserve the dimensional structure in a form a screen can display.

## Functional Dependencies Revisited

For a relation schema $R(A_1,\ldots,A_n)$, a functional dependency

$$
A_{i_1}, A_{i_2}, \ldots, A_{i_k} \rightarrow A_j
$$

holds in an instance when any two tuples that agree on the attributes on the left also agree on the attribute on the right. Declaring the dependency at schema level means it must hold in every valid instance.

Functional dependencies are crucial in dimensional hierarchies. If `month -> quarter` and `quarter -> year`, the system can move from month-level data to quarter- or year-level data without ambiguity. A hierarchy that violates its expected dependencies produces incorrect aggregation.

## The Virtual-Mall Example

The virtual-mall example uses a sales fact with three principal hierarchies:

```text
Time:            Time -> Month -> Quarter -> Year
Product:         Product -> Subcategory -> Category
Customer region: Customer -> Customer City -> Customer Region
```

Revenue can be analysed at any compatible combination of levels, such as revenue by product category, quarter, and customer region. This example provides the common setting for the OLAP operators below.

## OLAP Operators

### Roll-Up

**Roll-up** increases aggregation by removing a detail level from a hierarchy. Examples include:

```text
month -> quarter -> year
customer city -> customer region
product -> subcategory -> category
```

Measures must be combined through a valid aggregation operator, often `SUM`. Roll-up therefore changes both the grouping attributes and the measure values.

Conceptually, a time roll-up can be expressed as:

```sql
SELECT year, category, customer_region, SUM(revenue)
FROM SALES_ANALYSIS
GROUP BY year, category, customer_region;
```

### Drill-Down

**Drill-down** is the inverse of roll-up. It moves toward finer detail, such as region to city or year to quarter. Drill-down does not recreate detail that was never stored. It is possible only if the warehouse retains or can derive the finer-grained data.

A drill-down can be restricted to one context, for example revealing customer cities only for `year = 1998`.

### Slice and Dice

**Slice-and-dice** produces a sub-cube through selection conditions.

- slicing fixes a dimension, for example `year = 2006`, and can reduce dimensionality;
- dicing uses a more general predicate, such as `year = 2006 AND category = 'Electronics' AND revenue > 80 AND customer_region = 'Northwest'`.

The operation changes which cells are considered, not necessarily their aggregation level.

### Pivoting

**Pivoting** changes the layout of a multidimensional result. A dimension displayed in rows may be moved to columns, or dimensions may exchange display roles. The underlying data and aggregation do not change; only the perspective does.

Pivoting is important because a layout that makes one comparison obvious may hide another. Placing years in columns is useful for temporal comparison, whereas placing regions in columns is useful for geographic comparison.

### Drill-Across

**Drill-across** combines measures from different cubes or fact schemata at compatible aggregation levels. For example, a sales cube containing revenue can be combined with a promotion cube containing discounts.

Compatibility is essential. If one fact is recorded daily by product and store while another is monthly by category and region, they cannot be joined naively. Both must first be aligned to common dimensions and a common grain.

# Implementing the Multidimensional Model

The multidimensional model is a conceptual and user-facing abstraction. It can be implemented through relational structures, native multidimensional structures, or a hybrid of the two.

## ROLAP

**Relational OLAP (ROLAP)** implements multidimensional analysis on a relational DBMS. It benefits from mature relational technology, SQL, established administration experience, scalability, and broad availability.

The relational model does not natively contain the first-class concepts “dimension,” “measure,” and “hierarchy.” They must be represented through specialized relational schemas, principally star and snowflake schemas.

Large joins may cause performance problems. ROLAP therefore uses controlled denormalization, indexes, partitions, query rewriting, and **materialized views** that store selected query results or aggregates in advance.

ROLAP generally supports large data volumes and many users, but some multidimensional operations require more processing time or storage than in a native cube engine.

### ROLAP Architecture

A ROLAP engine acts as middleware between the relational back end and the analytical front end:

1. the user submits a multidimensional request;
2. the engine interprets dimensions, hierarchies, measures, and metadata;
3. it translates the request into SQL;
4. the relational server executes the SQL;
5. the engine converts the tabular result back into a multidimensional form for the client.

Metadata is central to this translation because it tells the engine which tables and joins implement each business concept.

## MOLAP

**Multidimensional OLAP (MOLAP)** uses an ad hoc logical model in which multidimensional data and operations are represented natively, commonly through array-like cube structures.

### Primary and Secondary Events

A **primary event** is a particular occurrence of a fact identified by one value for each dimension. Each measure has a value for that event. For example:

```text
date = 2008-10-10
store = SmartMart
product = Shiny
quantity = 10
revenue = 25
```

A **secondary event** aggregates the compatible primary events at coarser dimensional levels. Sales may be aggregated from date to month, product to type, and store to city. Hierarchies define which aggregations are meaningful and how granularity increases.

### Data Cubes and Materialization

The primary cube contains the finest stored events. Secondary cubes contain coarser aggregates along one or more dimensions. For a fact with store, time, and product dimensions, possible secondary cubes include:

- store-product;
- store-time;
- time-product;
- store only;
- time only;
- product only;
- the zero-dimensional grand total.

Not every secondary cube needs to be stored. It can be computed by aggregating the primary cube, but frequently used cubes may be **materialized** to reduce response time. Choosing which aggregates to materialize is an optimization problem balancing query speed, storage, and refresh cost.

MOLAP access is positional: array coordinates identify cells directly. This makes many multidimensional operations natural and avoids relational joins, often producing excellent performance.

### Advantages and Limitations

MOLAP offers fast and natural cube operations. However:

- implementations and logical models vary among vendors;
- there is no universal query language, although MDX became an important de facto language;
- loading and cube processing can be slow;
- some systems impose practical limits on the number or cardinality of dimensions;
- sparse multidimensional spaces require specialized storage strategies.

### The Sparsity Problem

Every combination of dimension values defines a possible coordinate, but most possible events may never occur. If there are 10,000 products, 1,000 stores, and 3,650 dates, the logical space contains 36.5 billion coordinates even if only a small fraction corresponds to an actual sale.

Storing empty cells wastes resources. ROLAP naturally stores only rows for events that occurred. MOLAP systems use compression, indexing, chunking, and other sparse-array techniques.

A cube can be partitioned into **chunks**, classified as dense or sparse. Dense chunks are attractive candidates for native multidimensional storage because most cells are useful.

### Hybrid OLAP

Hybrid strategies combine ROLAP and MOLAP. Possible designs include:

- storing dense chunks in MOLAP and sparse chunks in ROLAP;
- storing detailed primary facts in ROLAP and aggregated secondary cubes in MOLAP;
- storing frequently accessed data in MOLAP and less frequently accessed data in ROLAP.

The purpose is not to find a universally superior technology, but to place each data structure where its access pattern is handled most effectively.

# The Need for a Design Methodology

Data-warehouse projects combine source integration, historical semantics, multidimensional requirements, data quality, performance, and organizational governance. Without a methodological approach, teams often produce isolated reports or inconsistent data marts instead of a coherent analytical system.

A methodology makes design decisions explicit and repeatable. It reduces risk by learning from earlier projects and by separating requirement analysis, conceptual design, logical design, physical optimization, ETL, and validation.

The methodology introduced in the remainder of the course moves through three abstractions:

1. **requirements:** which organizational events and decisions matter?
2. **conceptual design:** what are the facts, measures, dimensions, and hierarchies, independently of the target DBMS?
3. **logical design:** how are those concepts represented in a relational star or snowflake schema, or in a multidimensional system?

## Facts, Dimensions, Granularity, and Historical Interval

A **fact type** is a concept on which data-mart users base decisions. It describes a category of dynamic events or observations, such as sales, purchases, shipments, admissions, calls, or inventory snapshots. An individual fact is one instance of that type.

Fact types must be identified during requirement analysis. A noun alone is not sufficient: “customer” is usually a dimension, whereas “customer purchase” can be a fact because it represents an event that occurs over time.

Designers must also identify the fact dimensions. Together, their lowest levels determine the **granularity**, or grain, of the stored event. Granularity is a deliberate compromise:

- fine grain preserves flexibility and allows unforeseen analyses, but creates a large fact table;
- coarse grain reduces volume and can improve performance, but permanently removes detail.

> [!important]
> The grain should be stated in one unambiguous sentence before measures are chosen. For example: “One fact row represents one product sold in one store on one date as part of one receipt.” Mixing facts with different grains in the same table produces double counting and ambiguous measures.

Most facts also require a **historical interval**: the period covered by the stored events. A ten-year analysis is impossible if only the latest year is retained, regardless of query technology.

## Typical Facts in Different Application Fields

The same modelling vocabulary applies across domains.

| Application field | Data mart | Typical facts |
|---|---|---|
| Business and manufacturing | Suppliers | Purchases, stock, inventory, distribution |
| Business and manufacturing | Production | Packaging, inventory, delivery, manufacturing |
| Business and manufacturing | Demand management | Sales, invoices, orders, shipments, complaints |
| Business and manufacturing | Marketing | Promotions, customer retention, advertising campaigns |
| Finance | Banks | Checking accounts, bank transfers, mortgages, loans |
| Finance | Investments | Securities and stock-exchange transactions |
| Finance | Services | Credit cards and standing-order payments |
| Healthcare | Divisions | Admissions, discharges, transfers, operations, diagnoses, prescriptions |
| Healthcare | Accident and emergency | Admissions, tests, discharges |
| Healthcare | Epidemiology | Diseases, outbreaks, treatments, vaccinations |
| Transportation | Goods and passengers | Demand, supply, transport |
| Transportation | Maintenance | Maintenance operations |
| Telecommunications | Traffic management | Network traffic and calls |
| Telecommunications | Customer relationship management | Retention, complaints, services |

The table illustrates that facts are events or evolving observations. The particular nouns change, but the design questions remain: What occurred? At what grain? Along which dimensions? With which numerical measures? Over what historical interval?

# Conceptual Modelling for Data Warehouses

Conceptual modelling documents the meaning of warehouse data independently of physical tables or a specific OLAP product. Accurate conceptual design is necessary for completeness, communication, and later logical design.

Although the Entity-Relationship model can technically represent relevant entities and relationships, it does not treat facts, dimensions, measures, hierarchies, and aggregation behaviour as first-class concepts. A large ER schema often hides the analytical structure users need to discuss.

The course therefore adopts the **Dimensional Fact Model (DFM)**.

## The Dimensional Fact Model

DFM is a graphical conceptual model for data marts. It is intended to:

- support conceptual design effectively;
- allow user queries to be formulated intuitively;
- support communication between designers and end users;
- refine and validate requirements;
- provide a stable platform for logical design independent of the target implementation;
- produce expressive documentation.

A DFM design consists of one or more **fact schemata**. Each fact schema describes a fact, its measures, dimensions, dimensional attributes, and hierarchies.

## Basic Constructs

### Fact Type

A fact type is a decision-relevant concept that normally represents a set of dynamic events. Examples include sales, shipments, purchases, calls, and complaints. The fact should occur or evolve over time; a static catalogue item is more naturally a dimension member.

In DFM, the fact is drawn as a central box. This visually emphasizes that measures describe the fact while dimensions identify and contextualize it.

### Measure

A **measure** is a numerical property of a fact that supports quantitative analysis. A sale may have:

- quantity;
- unit price;
- revenue or receipts;
- number of customers.

Measures must be interpreted at the fact grain. `quantity = 10` means ten units for exactly the dimensional combination that identifies the event.

Not every numeric field is automatically a useful measure. A product code may be numeric but acts as an identifier. Conversely, a fact schema may contain no explicit measures when only event occurrence matters.

### Dimension

A **dimension** is a finite-domain property that provides a coordinate for analysing a fact. Typical sales dimensions are product, store, and date. The combination of dimension values identifies a primary event, subject to any additional integrity constraints.

Dimensions answer the analytical questions “by what?” and “according to which perspective?” Measures answer “how much?” or “how many?”

### Dimensional Attributes and Hierarchies

The term **dimensional attribute** includes both the root dimension and the discrete attributes that describe it. A product may be described by type, category, brand, and department.

A **hierarchy** is a directed tree rooted in a dimension. Its arcs represent many-to-one associations between dimensional attributes. A path such as

```text
product -> type -> category -> department
```

defines progressively coarser aggregation levels. Hierarchies are not arbitrary drawing conventions: their arcs encode functional dependencies that must hold in the data.

## Relationship with ER Diagrams

An ER model can represent entities corresponding to dimensions and relationships corresponding to facts. Measures can appear as relationship attributes. Nevertheless, the analytical roles remain implicit. DFM makes them visually and semantically explicit:

- the fact is immediately recognizable;
- measures are distinguished from descriptive data;
- dimensions show the fact grain;
- hierarchies expose valid aggregation paths;
- advanced constructs express optionality, shared structures, and additivity.

DFM does not claim that ER is incapable of representing the domain. It provides a vocabulary better aligned with analytical reasoning.

## Naming Conventions

Clear names prevent ambiguity across large analytical models.

- Every dimensional attribute in one fact schema should have a distinct name.
- Similar attributes can be qualified by their predecessor, such as `brandCity` and `storeCity`.
- Names should describe the concept itself rather than the current fact. Prefer `product` and `date` over `shippedProduct` and `shipmentDate`.
- Attributes with the same meaning in different fact schemata should have the same name.

The final rule is especially important for drill-across: common names document conformed semantics across facts.

## Descriptive Attributes

A **descriptive attribute** is functionally determined by a dimensional attribute but does not introduce a useful aggregation level. It provides contextual information rather than a coordinate for grouping.

For example, a product may determine a package description, or a store may determine a telephone number. Grouping sales by a long textual description may be possible but is not normally a meaningful hierarchy level.

A descriptive attribute can also be attached directly to a fact when it describes a primary event but should neither identify the event nor be aggregated. An order note or a transaction reference can have this role.

The distinction is semantic, not merely based on data type. A string can be a dimensional level if users group by it, while a numeric value can be descriptive if it is not analysed quantitatively.

## Cross-Dimensional Attributes

A **cross-dimensional attribute** is a descriptive value determined by the combination of two or more dimensional attributes rather than by one hierarchy member alone.

For example, value-added tax may depend on both product category and country:

$$
(category, country) \rightarrow VAT
$$

Neither category nor country alone determines the tax rate. In an ER model this corresponds naturally to an attribute of a relationship between the participating concepts. In a relational implementation it usually becomes a separate table keyed by the determining attributes.

## Optional Attributes and Measures

An arc to a dimensional attribute may be optional. If `product -> diet` is optional, some products have no diet value. Attributes above that optional point may consequently also be undefined for those products.

A measure may also be optional. For example, `shipmentCost` may be unavailable for certain shipment facts. DFM marks optional elements explicitly because missingness changes both queries and interpretation.

`NULL` should not be treated as a single universal value. It may mean “not applicable,” “unknown,” “not yet available,” or “source error.” A warehouse design should preserve the intended meaning, often through explicit special dimension members or quality flags.

## Optional Dimensions

An optional dimension means that some primary events are identified by the other dimensions only. For example, a sale may or may not be associated with a promotion.

This is stronger than an optional descriptive property: the absent value belongs to a coordinate that would normally help identify the fact. The logical design must prevent accidental loss of facts in joins and must decide how “no promotion” is represented.

## Coverage

Coverage constrains two or more arcs leaving the same dimensional attribute. It combines two independent properties.

**Completeness:**

- **total (T):** every parent value is associated with at least one child value;
- **partial (P):** some parent values may be associated with no child value.

**Exclusivity:**

- **disjoint (D):** a parent value is associated with at most one of the child branches;
- **overlapping (O):** a parent value may be associated with two or more branches.

The combinations mean:

| Coverage | Meaning |
|---|---|
| T-D | Exactly one branch applies. |
| P-D | At most one branch applies. |
| T-O | At least one branch applies, possibly several. |
| P-O | No participation requirement and overlap is allowed. |

A P-O coverage is equivalent to independent optional branches. Coverage resembles specialization constraints in conceptual modelling, but here it governs alternative hierarchy paths.

## Convergence

**Convergence** occurs when different hierarchy paths lead to the same higher-level concept and must agree. Suppose a store determines a city, the city determines a state, and the store also determines a sales district whose hierarchy leads to a state. The state obtained through both paths must be identical.

Convergence is an integrity constraint. It is not guaranteed merely because both paths have an attribute named `state`; the agreement must be enforced or validated.

If one alternate path simply skips intermediate attributes and adds no distinct semantics, the convergence is redundant. Transitivity of functional dependencies already implies the direct relationship. The model should avoid drawing unnecessary duplicate paths.

## Shared Hierarchies

A **shared hierarchy** avoids replicating the same hierarchy portion several times in one or more fact schemata.

A call fact, for example, may use the same telephone-number hierarchy twice: once for the calling number and once for the called number. The underlying structure is shared, while arc labels define the two roles.

This idea anticipates a **role-playing dimension** in logical design: the same dimension table can be referenced by several foreign keys with different meanings, just as a date dimension can act as order date, shipment date, or payment date.

## Multiple Arcs

Ordinary hierarchy arcs represent many-to-one relationships. A **multiple arc** represents a many-to-many relationship between dimensional attributes. A book can have several authors, and an author can write several books.

When a multiple arc enters a root dimension, one fact coordinate may effectively be a group of values. A hospital admission, for example, can have several diagnoses. This complicates fact identification and aggregation because joining through the many-to-many relationship can multiply rows.

In relational design, a multiple arc is represented through a bridge table. Optional allocation weights can distribute a fact measure across participants while preserving totals.

## Additivity

Aggregation requires a valid operator for combining measures from primary events into secondary events. `SUM` is not automatically meaningful for every measure or along every dimension.

### Flow, Level, and Unit Measures

**Flow measures** are accumulated over a time interval: daily units sold, monthly receipts, or yearly births. They can normally be summed across both temporal and non-temporal hierarchies.

**Level measures** describe a state at a particular time: inventory level or population. Summing inventory across products or warehouses may be meaningful, but summing daily inventory levels across time is not. Across time, `AVG`, `MIN`, `MAX`, or an end-of-period value may be valid.

**Unit measures** are relative values observed at a time: unit price, discount percentage, or exchange rate. They generally should not be summed across either temporal or non-temporal dimensions. A weighted average may be more meaningful than a simple average.

| Measure type | Temporal hierarchies | Non-temporal hierarchies |
|---|---|---|
| Flow | SUM, AVG, MIN, MAX | SUM, AVG, MIN, MAX |
| Level | AVG, MIN, MAX | SUM, AVG, MIN, MAX |
| Unit | AVG, MIN, MAX | AVG, MIN, MAX |

The table gives typical valid operators, not a substitute for domain semantics. For example, an average unit price should often be weighted by quantity.

### Additive and Non-Additive Measures

A measure is **additive along a dimension** when `SUM` can be used along that dimension's hierarchy. Otherwise it is non-additive along that dimension.

Inventory level is typically additive across product or warehouse but non-additive across date. Adding Monday's stock to Tuesday's stock does not describe stock at a meaningful instant.

The number of customers estimated from receipt counts is non-additive across product. One receipt may contain several products, so summing product-level customer counts counts the same customer or receipt more than once.

Unit price is commonly non-additive across all dimensions. DFM records non-additivity explicitly, along with the alternative valid operators where appropriate.

> [!warning]
> Many analytical errors are aggregation errors rather than SQL syntax errors. A query can execute correctly and still produce a meaningless total because the chosen measure is not additive at that grain or along that dimension.

## Empty Fact Schemata

A fact schema is **empty** when it has no measures. Its primary events record only that something occurred. Attendance, event participation, or the presence of a relationship can be analysed in this way.

At higher aggregation levels, `COUNT` gives the number of primary events. An empty fact schema is therefore not useless: event occurrence itself is measurable.

The grain must still be clear. Counting rows is correct only if each row represents exactly one occurrence and duplicate loading is prevented.

## Overlapping Fact Schemata

Different fact schemata represent different event types, but users may need to compare their measures. A drill-across query might compare sales with inventory or shipments with orders.

An **overlapping fact schema** describes the common analytical space:

- its measures are the union of the measures from the participating facts;
- its hierarchies retain only attributes present in all corresponding hierarchies;
- each common attribute domain is restricted to the intersection of compatible domains.

In practical terms, facts must be brought to a common grain before comparison. Joining detailed fact tables directly can create a many-to-many explosion. Aggregating each fact separately to conformed dimensions and then joining the results is safer.

## Integrity Constraints in DFM

Not every relevant rule can be represented by the diagram. Additional integrity constraints may be documented as explicit sentences. Common examples include:

- conditions governing missing dimensional values;
- functional dependencies between attributes;
- identification rules stating that only a proper subset of dimensions is needed to identify the fact;
- convergence and domain restrictions;
- business rules for valid measure combinations.

These constraints are part of the model, not optional commentary. They guide ETL validation, key design, and correct query formulation.

# Logical Models for Data Marts

Conceptual modelling is independent of the technology chosen during architectural design. Logical modelling is not: it must translate the conceptual facts and dimensions into structures supported by the target system.

Two principal alternatives are:

- **MOLAP**, where data is stored in intrinsically multidimensional structures such as arrays;
- **ROLAP**, where multidimensional data is represented through the relational model.

The remainder of the course concentrates on ROLAP and on the relational structures that implement facts, measures, dimensions, and hierarchies.

# ROLAP: The Star Schema

A **star schema** represents one fact schema through a central fact table surrounded by dimension tables. Its shape resembles a star because each dimension table connects directly to the fact table.

Formally, a star schema contains:

- dimension relations $DT_1,\ldots,DT_n$, one for each dimension;
- a primary key $k_i$ for every dimension table, usually a surrogate key;
- dimensional attributes at different aggregation levels in each dimension table;
- a fact table $FT$ containing foreign keys $k_1,\ldots,k_n$ and one column for each measure.

The fact-table primary key is normally the combination of dimension foreign keys, unless an integrity constraint says that a subset is sufficient or the implementation introduces a separate fact-row key.

## Structure

A simplified sales star can be represented as follows:

```text
DATE(keyD, fullDate, month, quarter, year, holiday)
STORE(keyS, store, storeCity, state, country, salesManager)
PRODUCT(keyP, product, brand, type, category, department)

SALES(keyD, keyS, keyP, quantity, receipts, numberOfCustomers)
```

`SALES` contains the event measures and references the descriptive context. The grain might be:

> One SALES row represents the sales of one product, in one store, on one date.

The dimension keys in the fact table define the cube coordinates. Joining a fact row to the dimensions reconstructs its multidimensional context.

## Surrogate Keys

A **surrogate key** is an identifier generated for warehouse purposes rather than inherited directly from a source business system. Surrogate keys are useful because:

- different sources may use different natural identifiers;
- a source identifier can change or be reused;
- warehouse history may require several versions of the same business entity;
- a compact numeric key makes fact-table references predictable;
- special members such as “unknown” or “not applicable” can be represented explicitly.

The natural business key is normally retained as a dimension attribute for matching and audit. A surrogate key does not eliminate the need to understand real-world identity.

## Instances and Meaning

A fact-table tuple such as

```text
(keyD = 17, keyS = 3, keyP = 42, quantity = 100, receipts = 80)
```

does not expose its full meaning until the keys are joined to dimension rows. The dimension tables may reveal that the fact concerns a date in January 2008, a store in Austin, and a dairy product of a certain brand.

This separation keeps repeated descriptive values out of the very large fact table while allowing the dimensions themselves to be deliberately denormalized.

## Why Dimension Tables Are Denormalized

In a product dimension, dependencies such as

```text
product -> type -> category -> department
```

create transitive dependencies, so the table is not in Third Normal Form. This is intentional in a star schema.

Denormalization provides a major analytical advantage: one join reaches every attribute of a dimension. The cost is redundancy, because category and department values repeat for many products. The trade-off is often acceptable because dimension tables are much smaller than the fact table and are updated through controlled ETL rather than high-concurrency transactions.

This does not mean normalization theory has become false. The design accepts known redundancy to optimize a different workload.

## Fact-Table Size and Sparsity

The fact table contains tuples at the chosen grain. A fine-grained fact can produce a very large table, so partitioning, indexing, clustering, compression, and materialized aggregates may be required.

Unlike a dense multidimensional array, a ROLAP fact table stores only dimensional combinations for which an event occurred. Non-events consume no fact rows, so relational storage naturally avoids the basic cube sparsity problem.

## Integrity Constraints in a Star Schema

The relational representation inherits the semantic constraints of the conceptual model.

- Dimension and measure attributes are non-null by default in the course notation; optional attributes are marked explicitly.
- Functional dependencies within dimensions must be preserved.
- Fact foreign keys must reference valid dimension members.
- A documented subset of dimension keys may identify a fact if the full set is not required.
- Grain and additivity rules remain valid even if SQL cannot enforce all of them directly.

A warehouse often uses an “unknown” dimension member instead of a null foreign key so that an incomplete fact remains joinable and visible in quality analysis.

## OLAP Queries over a Star Schema

Joining the fact table to all dimension tables produces a multidimensional view:

```sql
SELECT *
FROM SALES AS ft
JOIN PRODUCT AS p ON ft.keyP = p.keyP
JOIN STORE   AS s ON ft.keyS = s.keyS
JOIN DATE_DIM AS d ON ft.keyD = d.keyD;
```

Suppose the request is:

> For food products, compute quantity by store city, week, and product type.

The multidimensional expression corresponds to a relational selection, join, grouping, and aggregation:

```sql
SELECT
    s.storeCity,
    d.week,
    p.type,
    SUM(ft.quantity) AS total_quantity
FROM SALES AS ft
JOIN PRODUCT AS p ON ft.keyP = p.keyP
JOIN STORE   AS s ON ft.keyS = s.keyS
JOIN DATE_DIM AS d ON ft.keyD = d.keyD
WHERE p.category = 'Food'
GROUP BY s.storeCity, d.week, p.type;
```

The SQL operators have a clear multidimensional interpretation:

| SQL component | Multidimensional meaning |
|---|---|
| `JOIN` | Recover dimension context for facts. |
| `WHERE` | Slice or dice the cube. |
| `GROUP BY` | Select the aggregation level. |
| `SUM` | Roll up an additive measure. |
| Selected columns | Determine the visible dimensions and measures. |

# The Snowflake Schema

A star dimension is deliberately denormalized. A **snowflake schema** reduces this denormalization by decomposing some or all transitive dependencies into separate relations.

For example, a star dimension might contain:

```text
STORE(keyS, store, storeCity, state, country, salesManager)
```

with dependencies:

```text
keyS -> store
store -> storeCity
storeCity -> state
state -> country
store -> salesManager
```

A snowflake design can separate the city hierarchy:

```text
STORE(keyS, store, keyC, salesManager)
CITY(keyC, storeCity, state, country)
```

`STORE` is a **primary dimension table** because its key is referenced by the fact table. `CITY` is a **secondary dimension table** reached through another dimension table.

## Structure

More generally, a snowflake dimension table contains:

- its own primary key, normally surrogate;
- a subset of attributes functionally dependent on that key;
- foreign keys to other tables needed to reconstruct the complete dimension.

A product hierarchy can be decomposed into:

```text
PRODUCT(keyP, product, brand, keyT)
TYPE(keyT, type, keyCategory)
CATEGORY(keyCategory, category, department)
```

The fact table still references `PRODUCT`, not every secondary table.

## Advantages and Costs

Normalization reduces repeated dimensional values and can substantially save storage when many low-level members share a small number of higher-level members.

It also produces smaller primary dimension tables, so queries needing only low-level attributes may join smaller relations. However:

- additional surrogate keys and foreign keys are required;
- queries involving secondary attributes need more joins;
- the schema is less immediately understandable to users;
- additional joins can increase query time and optimizer complexity.

The choice should be workload-driven. Snowflaking a small dimension purely for theoretical normalization may add complexity without meaningful benefit.

## Correct Snowflake Decomposition

When a dimension is decomposed at a hierarchy attribute, the new relation must include every attribute that directly or transitively depends on the natural key of that hierarchy level.

In the store example, `storeCity`, `state`, and `country` belong together because:

$$
storeCity \rightarrow state \rightarrow country
$$

Leaving `country` in the store table while moving `storeCity` and `state` to `CITY` would not properly isolate the transitive dependency and could reintroduce inconsistency.

## OLAP Queries over a Snowflake Schema

The earlier food-sales query requires more joins when city, product type, and category are stored in secondary tables:

```sql
SELECT
    c.storeCity,
    d.week,
    t.type,
    SUM(ft.quantity) AS total_quantity
FROM SALES AS ft
JOIN PRODUCT  AS p   ON ft.keyP = p.keyP
JOIN TYPE     AS t   ON p.keyT = t.keyT
JOIN CATEGORY AS cat ON t.keyCategory = cat.keyCategory
JOIN STORE    AS s   ON ft.keyS = s.keyS
JOIN CITY     AS c   ON s.keyC = c.keyC
JOIN DATE_DIM AS d   ON ft.keyD = d.keyD
WHERE cat.category = 'Food'
GROUP BY c.storeCity, d.week, t.type;
```

The analytical request has not changed. Only its relational implementation is more elaborate.

# Logical Design

Logical design transforms a conceptual fact schema into the schema of a data mart. It is not a mechanical translation based only on the diagram.

Its inputs include:

- the conceptual schema;
- the expected workload;
- data volumes and cardinalities;
- system and platform constraints.

Its output is a logical schema suitable for implementation. Unlike operational logical design, warehouse design deliberately considers redundancy and denormalization.

## Main Steps

The principal steps are:

1. choose a logical model and schema style, such as star or snowflake;
2. translate fact schemata into logical schemata;
3. choose views or aggregates to materialize;
4. apply further optimizations, such as indexes and partitions.

The steps interact. A materialized view is useful only for an important workload, and the workload can be estimated only after facts, grain, dimensions, and expected data volume are understood.

## Star versus Snowflake

There is no universal rule that one schema is always superior.

A star schema emphasizes simplicity and fast access through fewer joins. This is closely aligned with the traditional data-warehouse philosophy of making analytical structures easy to understand.

Snowflaking can be beneficial when the ratio between the cardinality of a primary dimension level and a secondary level is very high. If millions of products belong to a few product types, separating type data can remove a large amount of repetition while adding a join to a very small table.

Snowflaking is also useful when part of a hierarchy is shared among several dimensions. A common city-state-country table, for example, can be reused by warehouse and customer hierarchies.

| Prefer a star when... | Consider snowflaking when... |
|---|---|
| Query simplicity is a major goal. | Repetition in a large dimension is substantial. |
| Dimension tables are relatively small. | A high-level hierarchy has low cardinality relative to the leaf level. |
| Most queries traverse several hierarchy levels. | A hierarchy portion is shared by several dimensions. |
| Fewer joins improve the dominant workload. | Storage or maintenance savings justify extra joins. |

## Translating Fact Schemata into Star Schemata

The basic translation rule is:

> Create a fact table containing dimension keys, all measures, and descriptive attributes directly connected to the fact. For each hierarchy, create one dimension table containing all its dimensional and descriptive attributes.

This simple rule handles the basic constructs. Advanced DFM constructs require additional decisions.

## Translating Descriptive Attributes

A descriptive attribute connected to a dimensional attribute is placed in the dimension table containing that attribute. A descriptive attribute connected directly to the fact is placed in the fact table.

The attribute must be compatible with the table grain. A fact-level description that makes sense only for detailed primary events must be omitted from an aggregate fact table or materialized aggregate, because several incompatible descriptions could correspond to one aggregated row.

Similarly, when a dimension hierarchy is snowflaked, a description belongs only in a table containing the member it describes.

## Translating Cross-Dimensional Attributes

A cross-dimensional attribute determined by $a_1,\ldots,a_m$ becomes a new relation whose key contains the determining attributes and whose non-key columns contain the cross-dimensional values.

For VAT determined by category and country:

```text
VAT_RULE(categoryKey, countryKey, vatRate)
PRIMARY KEY(categoryKey, countryKey)
```

The table represents a many-to-many association between the participating dimensions, enriched with an attribute.

The designer must decide whether to use the natural composite key or introduce a surrogate key. The choice depends on key width, reference frequency, clarity, and storage cost. A surrogate key should not obscure the uniqueness constraint on the natural determinant.

## Translating Shared Hierarchies

If two hierarchies contain exactly the same attributes, the dimension table should not be duplicated. Its key is imported into the fact table more than once, with role-specific foreign-key names.

```text
CALL(
    callingNumberKey,
    calledNumberKey,
    dateKey,
    hourKey,
    numberOfCalls,
    duration
)
```

Both number keys reference the same `NUMBER` dimension. Query aliases distinguish the roles:

```sql
JOIN NUMBER AS calling ON ft.callingNumberKey = calling.numberKey
JOIN NUMBER AS called  ON ft.calledNumberKey  = called.numberKey
```

If two hierarchies share only a higher portion, the designer has two alternatives:

1. duplicate the common attributes in separate denormalized dimensions;
2. snowflake both dimensions at the first shared attribute and reuse a common secondary table.

The first favours simple star queries; the second reduces redundancy and centralizes shared hierarchy maintenance.

## Translating Multiple Arcs

A many-to-many hierarchy relationship requires a **bridge table**. For books and authors:

```text
BOOK(bookKey, book, genre)
AUTHOR(authorKey, author)
BRIDGE_AUTHOR(bookKey, authorKey, weight)
```

The bridge primary key is the combination of the connected keys. An optional `weight` allocates a percentage of the fact to each participant.

Suppose a sale of 100 monetary units concerns a book with two authors. Joining without a weighting rule produces two rows and can yield a total of 200 when grouped by author. With weights of 0.5 and 0.5, allocated revenue remains 100.

Weights are not always appropriate. If the analytical question is “How many authors are associated with sold books?”, allocation is different from revenue attribution. The measure semantics and intended aggregation must determine bridge usage.

# How the Whole Topic Fits Together

The course follows one continuous design argument:

1. **Operational systems produce detailed current data.** They are optimized for transactions and application integrity.
2. **Decision support needs integrated historical information.** Direct analytical access to operational sources is unreliable and interferes with OLTP.
3. **A warehouse architecture creates separation.** ETL reconciles sources and loads a stable analytical repository, possibly with reconciled layers and data marts.
4. **Users think multidimensionally.** Facts are quantified by measures and examined through dimensions and hierarchies.
5. **OLAP provides interactive navigation.** Roll-up, drill-down, slice-and-dice, pivot, and drill-across transform the analytical view.
6. **Conceptual design makes semantics explicit.** DFM describes facts, grain, measures, hierarchies, constraints, optionality, and additivity independently of storage.
7. **Logical design maps the concepts to technology.** ROLAP uses star or snowflake schemas; MOLAP uses native cubes; hybrid systems combine their strengths.
8. **Correctness depends on semantics as much as structure.** A syntactically valid query is not trustworthy if sources were not reconciled, grains are mixed, hierarchies are invalid, or measures are aggregated incorrectly.

> [!summary]
> An OLTP system answers **“What is the current state of this operation?”** A data warehouse helps answer **“What patterns emerge when many operations are integrated and observed across subjects and time?”** DFM specifies what those analyses mean; star, snowflake, ROLAP, and MOLAP specify how they can be implemented.

# Compact Glossary

| Term | Meaning |
|---|---|
| DSS | A collection of tools and techniques supporting decisions. |
| Data warehouse | Integrated, subject-oriented, historical, non-volatile analytical data repository. |
| OLTP | Processing of short operational transactions. |
| OLAP | Interactive multidimensional analysis. |
| ETL | Extraction, cleansing/transformation, and loading of source data. |
| Reconciled data | Detailed source data after integration and cleansing. |
| Data mart | Analytical subset focused on a business area or user group. |
| Metadata | Information describing schemas, meanings, origins, mappings, and loading rules. |
| Fact | An event or evolving phenomenon relevant to decisions. |
| Grain | The exact level of detail represented by one fact. |
| Measure | A quantitative property of a fact. |
| Dimension | An analysis coordinate used to identify and group facts. |
| Hierarchy | Many-to-one path through progressively coarser dimensional levels. |
| Roll-up | Move to a coarser aggregation level. |
| Drill-down | Move to a finer aggregation level. |
| Slice and dice | Restrict the cube through predicates. |
| Pivot | Change the display orientation of dimensions. |
| Drill-across | Compare compatible measures from different facts. |
| DFM | Conceptual model for facts, dimensions, measures, hierarchies, and constraints. |
| Additivity | Validity of summing a measure along a dimension. |
| ROLAP | Relational implementation of multidimensional analysis. |
| MOLAP | Native multidimensional implementation based on cube structures. |
| Star schema | Central fact table connected directly to denormalized dimension tables. |
| Snowflake schema | Star variant with partly normalized dimension hierarchies. |
| Surrogate key | Warehouse-generated identifier independent of source business keys. |
| Bridge table | Relation implementing a many-to-many dimensional association. |
| Materialized view | Precomputed query result stored to accelerate later queries. |

# Questions for Self-Assessment

1. Why can a database be perfectly normalized and still be unsuitable for enterprise analysis?
2. Which problems are solved by physically separating OLAP from OLTP?
3. How does a reconciled layer differ from the primary data warehouse?
4. Why are cleansing and transformation conceptually different even when implemented together?
5. State the grain of a fact before listing its measures. Why does the order matter?
6. Which functional dependencies justify a `product -> type -> category` hierarchy?
7. What is the difference between slicing and rolling up?
8. Why is inventory additive across warehouses but not normally across dates?
9. Why can customer counts become incorrect when summed across products?
10. How does a ROLAP engine translate a multidimensional request into relational operations?
11. Why is sparsity a direct problem for MOLAP but less direct for ROLAP?
12. What trade-off is made when a star dimension is snowflaked?
13. How should two facts at different grains be combined in a drill-across query?
14. When is a bridge table required, and why may it contain weights?
15. Which design choices are conceptual, which are logical, and which are physical optimizations?

[^1]: 
