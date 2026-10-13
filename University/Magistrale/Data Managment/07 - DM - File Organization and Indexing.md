---
title: Access File Manager — File Organization and Indexing
aliases:
  - DM — File Organization and Indexing
  - Access file manager
  - Indexes
tags:
  - data-management
  - dbms-architecture
  - file-organization
  - indexing
  - external-sorting
  - b-plus-tree
  - cost-model
source: 7-FileOrganization.pdf
---

# Access File Manager — File Organization and Indexing

> [!abstract] Purpose of this lecture
> Part 7 of the course (M. Lenzerini) studies the **access file manager**, the DBMS module just above the [[06 - DM - Buffer Management|buffer manager]]: it decides **how the records of a relation are laid out in pages and files** and **which auxiliary structures (indexes)** let the DBMS find them without reading everything. The slides have three parts: (7.1) pages and records; (7.2) simple file organizations (heap, sorted, hashed) with their **cost model**, plus **external sorting**; (7.3) index organizations: properties of indexes, sorted indexes, and tree indexes (**ISAM** and **B+-tree**). These costs are the input of [[08 - DM - Evaluation of Relational Operators]].
>
> Course map: [[00 - Data Management MOC]]. Base triennale: Basi di Dati only mentions `create index` ([[03 - BD - SQL#Indici|BD — Indici]]) and a cost model for logical restructuring ([[Modello di Costo]]); here we see what an index *is* and what it costs. The distinction between **search key** and **key** builds on [[Superchiave e Chiave]] and [[Chiave Primaria]]. A file system faces similar problems: [[File System]] · [[Strutture Dati del File System]] (Sistemi Operativi).

> [!note] Numbering in the slides
> The slides are titled "Part 7" but number their sections "5.1, 5.2, 5.3" (left over from an earlier edition, A.Y. 2022/2023). This note uses 7.1–7.3.

---

## Architecture of a DBMS

The usual diagram (see [[05 - DM - Concurrency Control#Architecture of a DBMS|Lecture 5]]) places the **access file manager** between the SQL engine and the buffer manager: the SQL engine asks for records ("all employees with salary > 1000"), the access file manager translates the request into page requests (`fix`/`unfix`) to the buffer manager.

---

# 7.1 Pages and records

## Relations, files, pages and records

![[DM-L07-p005.png]]

The ER diagram summarizes the physical model:

- a **relation** is stored in one or more **DB files**, and (usually) a DB file stores one relation (cardinalities (1,n) – (1,1));
- a DB file is **formed** by one or more **pages**; each page belongs to one file;
- a page **contains** one or more **records**; each record is in one page;
- the dashed relationship **R-R** (relation – record) is **derived**: a record belongs to a relation because it is in a page of a file storing that relation.

## Pages and records

- A page usually has the size of a **block**, the unit of transfer to/from the buffer pool.
- A page has an address (**page id**) and is made of **slots**, each with an address; a page may also have a **header** (e.g. pointers to other pages).
- A **slot** can contain one record (typically all records in a page belong to one relation) and has a number (**slot id**) identifying it within the page.
- Each record therefore has an identifier, the **record id**: $rid = \langle page\ id, slot\ number\rangle$.
- A record usually has a header too: pointer to its schema, its length, timestamps of last modification or read, etc.

Vedi [[Record Identifier]].

### Pages with fixed-length records

![[DM-L07-p007.png]]

- **Packed**: records occupy slots $1..N$ contiguously, and the header stores $N$. Free space is at the end, so inserting is easy; but **deleting** a record means moving others to keep them packed, which **changes their rids**, a problem if other pages refer to them.
- **Unpacked**: the page has $M$ slots and a **bit array** (1 = occupied, 0 = free). Records never move; finding a record or a free slot requires checking the bit array.

### Pages with variable-length records

![[DM-L07-p008.png]]

The page ends with a **slot directory**: for each slot the offset (and length) of its record, the number of slots $N$, and a pointer to the start of free space. A rid $(i, k)$ points to the $k$-th directory entry, which points to the record.

- Records can **move within the page** (to compact free space) without changing their rid: only the directory entry is updated.
- Deleting a record sets its directory entry to $-1$. Data and free space are reorganized periodically.

![[DM-L07-p009.png]]

If a record grows and must **move to another page** $j$, the old position stores a **forwarding address** $(j,h)$: the rid $(i,2)$ remains valid, at the cost of one extra page access.

### Format of records

![[DM-L07-p010.png]]

**Fixed-length records**: fields $F_1..F_4$ have fixed lengths $L_1..L_4$; the address of $F_3$ is $B + L_1 + L_2$ where $B$ is the base address. The field information is the same for all records of a type and lives in the **system catalog**.

![[DM-L07-p011.png]]

**Variable-length records** (fixed number of fields), two alternatives:

1. fields **separated by special symbols** (`$`), preceded by the number of fields;
2. an **array of offsets** at the start of the record, one per field (plus one for the end).

Alternative (2) allows **direct access** to any field and stores **NULLs efficiently**: two consecutive equal offsets mean an empty field (NULL).

Base triennale: [[Valore Nullo]]

### Records larger than a page

If a record does not fit in a page, it is split into **fragments**, each fitting in a page: the record is **spanned**. Each record/fragment needs a bit telling whether it is a fragment, bits telling whether it is the first or last fragment, and pointers to the previous and next fragments. Very large values such as **BLOBs** (binary large objects: images, video, audio, radar signals) may occupy a whole sequence of pages.

---

# 7.2 Simple file organizations

## File

A **file** is a collection of pages, each containing records. Usually one file stores one relation, but there are exceptions (see [[#Another application: clustered files]]). A file organization must support:

- insert / delete / update a record;
- read the record with a given rid;
- **scan** all records, possibly only those satisfying a condition.

![[DM-L07-p015.png]]

The taxonomy of file organizations, which structures the rest of the lecture:

- **simple**: **heap**, **sorted**, **static hash** (which coincides with the hashed file);
- **index-based**: **hash** indexes (static, or dynamic: extendible and linear hashing), **tree** indexes (**ISAM**, **B+-tree**), **sorted** indexes.

## Heap file

Vedi [[Heap File]].

Records are stored in pages **with no order** among pages or records. Pages are allocated and deallocated as the relation grows and shrinks. The DBMS must keep track of the file's pages, of the records in them, and of **free space**.

![[DM-L07-p018.png]]

**Lists**: a header page points to two linked lists, **full pages** and **pages with free space**. A new page obtained from the disk manager is put at the head of the free-space list; a page that becomes empty is removed.

![[DM-L07-p019.png]]

**Directory**: the header page starts a **directory**, a list of pages whose entries point to data pages and record how much free space each has. Searching for free space costs a number of accesses **linear in the directory size**, not in the relation size (much smaller, since an entry is a few bytes).

## Sorted file

Records are sorted within each page on a set of fields, the **search key**; pages are sorted accordingly and stored contiguously. Sorting helps for `ORDER BY`, searching, joins, etc.

## Hashed file

Vedi [[Hashed File]].

Pages are organized in **buckets**; a bucket is one **primary page** plus possibly **overflow pages** linked to it. Given a search key value $k$, a **hash function** computes the bucket containing the record.

![[DM-L07-p022.png]]

- The number $N$ of primary pages (buckets) is **fixed**: allocated sequentially, never deallocated, with overflow pages if needed (**static hashing**).
- The bucket of key $k$ is $h(k) \bmod N$; $h$ composed with $\bmod N$ should distribute values **uniformly** over $0..N-1$.
- Long overflow chains degrade performance; dynamic schemes (extendible, linear hashing) solve this, and appear in the taxonomy.

## Cost model

Vedi [[Cost Model for File Organizations]].

| Symbol | Meaning | Typical value |
|---|---|---|
| $B$ | number of pages in the file | |
| $R$ | number of records per page | |
| $D$ | time to read/write a page | 15 ms |
| $C$ | average time to process a record | 100 ns |

Since $D \gg C$ (five orders of magnitude), I/O dominates: we characterize operations by the **number of page accesses** in the worst case, and by their big-O complexity.

### Operations

- **Scan**: load all pages, locate records in them.
- **Equality selection**: load the pages with relevant records; the record is unique if the equality is on a relation key.
- **Range selection**: load the pages with relevant records.
- **Insertion**: locate the page, load it, modify it, write it back, plus other pages if needed.
- **Deletion**: similar to insertion.

### Heap file costs

We ignore the cost of managing free space.

| Operation | Time | Pages | O |
|---|---|---|---|
| Scan | $B(D+RC)$ | $B$ | $O(B)$ |
| Equality selection | $B(D+RC)$ | $B$ | $O(B)$ |
| Range selection | $B(D+RC)$ | $B$ | $O(B)$ |
| Insertion | $D+C+D$ (load last page, insert, write) | 2 | $O(1)$ |
| Deletion by rid | $D+C+D$ | 2 | $O(1)$ |
| Deletion by condition | $B(D+RC)+XC+YD$ | $B+Y$ | $O(B+X+Y)$ |

($X$ = records to delete, $Y$ = pages containing them.) For an equality on a key where the record exists and is equally likely in any page, the **average** cost is $\frac{B}{2}(D+RC)$.

### Sorted file: search

The trivial method scans the file: $\frac B2(D+RC)$ on average whether or not the record exists. If the pages are contiguous at addresses $a_1..a_B$, a generic search for key $K$ in $(h_1,h_2)$ is:

1. if $(h_1,h_2)$ is empty, fail;
2. choose a tentative address $i$ and load page $p_i$;
3. if $K$ is in $p_i$, succeed;
4. if $K$ is smaller than the minimum key in $p_i$, repeat on $(h_1, i-1)$, else on $(i+1, h_2)$.

The choice of $i$ gives two algorithms:

- **binary search**: $i$ in the middle of the range;
- **interpolation search**: if keys are numeric and uniform in $(K_{min},K_{max})$, $p_K = \frac{K-K_{min}}{K_{max}-K_{min}}$ estimates the fraction of records with key $\le K$, and $i = a_1 + p_K(a_B-a_1)$.

Range $(K_1,K_2)$: search $K_1$, then scan forward until values exceed $K_2$. Insertion: shift records to keep the order, or use overflow storage and reorganize periodically. Deletion: find and remove, possibly compacting.

### Sorted file costs

| Operation | Time | Pages | O |
|---|---|---|---|
| Scan | $B(D+RC)$ | $B$ | $O(B)$ |
| Equality on search key (binary) | $(2C+D)(1+\log_2B)+C\log_2R$ | $1+\log_2B$ | $O(\log_2B)$ |
| Equality (interpolation, average) | $(2C+D)\log_2\log_2B+C\log_2R$ | $\log_2\log_2B$ | $O(\log_2\log_2B)$; worst case $B(D+RC)$ |
| Range on search key | $(2C+D)(1+\log_2B)+C\log_2R+(f_s B-1)(D+RC)$ | $1+\log_2B+f_sB-1$ | $O(\log_2B+f_sB)$ |
| Insertion (worst: first position, no overflow) | search $+C+2B(D+RC)$ | $1+\log_2B+2B$ | $O(B)$ |

- Binary search: $1+\log_2B$ steps, each 1 I/O + 2 comparisons; then binary search inside the page, $C\log_2R$.
- $f_s=\frac{K_2-K_1}{K_{max}-K_{min}}$ is the expected fraction of pages in the range (**selectivity**).
- Insertion in the middle on average: search $+C+B(D+RC)$ (read and write half the file).
- Deletion is similar to insertion if empty slots are not allowed.

### Hashed file costs (rough)

Pages are kept about **80% full** to limit overflows, so the file has $1.25B$ pages.

| Operation | Cost | O |
|---|---|---|
| Scan | $1.25B(D+RC)$ | $O(B)$ |
| Equality on search key | $(D+RC)\times$ (overflow factor) | $O(1)$ + overflow |
| Range on search key | $1.25B(D+RC)$ (hashing destroys order) | $O(B)$ |
| Insertion | $2D+RC$ | $O(1)$ + overflow |
| Deletion | search $+D+RC$ | $O(1)$ + overflow |

### Comparison

| Organization | Scan | Equality | Range | Insertion | Deletion |
|---|---|---|---|---|---|
| Heap | $O(B)$ | $O(B)$ | $O(B)$ | $O(1)$ | $O(B)$ |
| Sorted | $O(B)$ | $O(\log_2B)$ (on key) | $O(\log_2B)$ + relevant pages | $O(\log_2B+B)$ | $O(\log_2B+B)$ |
| Hashed | $O(B)$ | $O(1)$ + relevant pages | $O(B)$ | $O(1)$ | $O(1)$ + relevant pages |

(Binary search for sorted files, no overflow for hashed files.) No organization wins everywhere: this motivates indexes.

---

## External sorting

Vedi [[External Merge Sort]].

### Why sorting

![[DM-L07-p038.png]]

Sorting is not only for sorted files: users want sorted results (`ORDER BY`), sorting is the first step of **bulk-loading a B+-tree**, it eliminates **duplicates** (`DISTINCT`), and the **sort-merge** join and other operators rely on it ([[08 - DM - Evaluation of Relational Operators]]).

Why not quicksort, mergesort, heapsort…? Because the data **does not fit in main memory**. Sorting on secondary storage (**external sorting**) is very different from internal sorting.

### Merge sort in main memory

![[DM-L07-p041.png]]

Internal merge sort splits the list (Banana, Grapefruit, Apple, Orange, Mango, Kiwi, Strawberry, Blueberry) down to small sorted sublists…

![[DM-L07-p042.png]]

…and merges them pairwise into longer sorted lists until one remains (Apple, Banana, Blueberry, Grapefruit, Kiwi, Mango, Orange, Strawberry).

It needs $O(N\log_2N)$ comparisons for $N$ records: if each step touched the disk, that would mean $O(N\log_2N)$ I/Os. **Key insight**: sort by **pages**, not records: read whole pages into the buffer, process them in memory, write processed blocks, repeat.

### 2-way external merge sort

![[DM-L07-p044.png]]

- **Pass 0**: read each page, sort it in memory, write it: $B$ sorted runs of 1 page.
- **Pass 1**: merge pairs of pages into runs of 2 pages (2 input frames, 1 output frame).
- **Pass 2**: merge pairs of runs into runs of 4 pages; and so on until one run.

Cost: each pass reads and writes $B$ pages. After passes $1..k$ there are $B/2, B/4, \ldots, B/2^k$ runs; stop when $B/2^k\le1$, i.e. $k\ge\log_2B$. Total passes $\lceil\log_2B\rceil+1$, cost

$$2B(\lceil\log_2B\rceil+1)$$

**Example**: $10^6$ records of 100 bytes, 8 KB pages → 80 records/page → $B=12{,}500$ pages.

- Plain merge sort, one I/O per record operation: $2N(\log_2N+1)\approx 41{,}863{,}137$ I/Os.
- 2-way external merge sort: $2B(\log_2B+1)\approx 365{,}241$ I/Os.
- At about 10 ms per I/O: **4.8 days vs 1 hour**.

> [!note] Rounding in the example
> The slide's figure 365,241 uses $\log_2 12{,}500\approx13.61$ without the ceiling. With the formula above, $\lceil 13.61\rceil+1=15$ passes and $2\cdot12{,}500\cdot15=375{,}000$ I/Os: the conclusion (about one hour) does not change.

### Multipass (k-way) merge sort

2-way merge sort uses only **3 frames**, while a DBMS can devote many (100 MB = 12,800 pages of 8 KB). Using more frames reduces the number of passes, and cost is $2B\times\#passes$.

With $F$ frames:

- **Pass 0**: read $F$ pages at a time, sort them in memory, write a **run** (sorted sublist) of $F$ pages: $S=\lceil B/F\rceil$ runs.
- **Pass $i\ge1$**: use $F-1$ input frames and 1 output frame; merge $Z=F-1$ runs at a time into one: keep one page of each input run in its frame, repeatedly move the smallest record to the output frame; when an input page is exhausted, load the next page of that run; when the output frame is full, write it.
- Repeat until one run remains.

![[DM-L07-p050.png]]

One pass with $Z=3$: groups of three runs (green bars) are merged, each into one longer run below.

![[DM-L07-p060.png]]

A single merge operation: the $Z$ grey frames hold the current page of each input run (red = consumed part), the last frame is the output buffer; pages come in from the runs below and leave to the output file on the right.

**Complexity.** After pass 0 there are $S=B/F$ runs; after pass $i$ there are $S/Z^i$; stop when $S/Z^k\le1$, i.e. $k\ge\log_ZS$:

$$\text{cost} = 2B(\lceil\log_Z S\rceil+1) = 2B\left(\left\lceil\log_Z\frac BF\right\rceil+1\right)\approx 2B\log_{F-1}B\quad(Z=F-1)$$

**Example (slides)**: 12,500 pages, 10 buffer frames: "4 passes, 100,000 I/Os, 17 minutes vs 1 hour for 2-way".

> [!warning] Correzione
> With $F=10$: pass 0 produces $\lceil12{,}500/10\rceil=1{,}250$ runs; merging 9 at a time gives $139\to16\to2\to1$ runs, i.e. **4 merge passes + pass 0 = 5 passes**, $2\cdot12{,}500\cdot5=125{,}000$ I/Os (about 21 minutes at 10 ms per I/O). The slide's "4 passes / 100,000 I/Os" matches the approximation $2B\log_{F-1}B$ ($\approx107{,}000$) or forgets pass 0. Either way it is far better than the 2-way sort.

> [!question]- Exercise 1 — when does the sort take two passes?
> Two passes = pass 0 (create runs) + one merge pass. The merge pass can merge at most $F-1$ runs, each of at most $F$ pages: $B\le F(F-1)\approx(F-1)^2$. So with $F$ frames we can sort about $F^2$ pages in 2 passes: e.g. 1,000 frames sort 1,000,000 pages.

> [!question]- Exercise 2 — three passes, $N$ passes
> After pass 0 we have $B/F$ runs; each merge pass divides the number by $F-1$. Three passes (two merge passes): $B/F\le(F-1)^2$, i.e. $B\le F(F-1)^2$. $N$ passes: $B\le F(F-1)^{N-1}$.

**Recursive formulation.** Base: if $B(R)\le F$, sort $R$ in memory and write it. Step: otherwise partition $R$ into $F-1$ groups, sort each recursively, then merge the $F-1$ sorted sublists with one output frame. (Exercise: show it is equivalent to the iterative version.)

---

# 7.3 Index organizations

## The notion of index

Vedi [[Database Index]].

An **index** is any method that, given a property of records (typically the value of one or more fields), finds the records with that property **quickly**.

An index is built on the **search key**: any subset of the fields of the relation.

> [!important] Search key ≠ key
> A **key** is a minimal set of fields that uniquely identifies records ([[Superchiave e Chiave]]). A **search key** is any set of fields on which the index is built; it may or may not coincide with a key.

### Data entry, index entry, data record

An index-based implementation of $R$ has:

- an **index file** (possibly virtual, e.g. for a hash index) containing
  - **data entries**: each contains a value $k$ of the search key and is used to locate the data records with value $k$;
  - **index entries** (in some organizations): used to navigate the index itself;
- a **data file** containing the **data records** of $R$.

## Properties of an index

1. organization; 2. structure of data entries; 3. clustering / non-clustering; 4. primary / secondary; 5. dense / sparse; 6. simple / composite key; 7. single / multi level.

### Organization

- **Sorted index**: the index is a sorted file.
- **Tree-based index**: the index is a tree.
- **Hash-based index**: the index is a function from search key values to record addresses.

### Structure of data entries

Vedi [[Data Entry Alternatives]].

For a data entry $k^*$ with search key value $k$:

1. $k^*$ **is the data record** itself (extreme case; e.g. the hashed file). At most one index per data file can use it.
2. $k^* = (k, r)$, where $r$ is a reference (e.g. a rid) to a data record with key $k$: the index file is independent of the data file.
3. $k^* = (k, r\text{-}list)$, a list of references: more compact (each key once), but variable-length entries.

### Clustering and non-clustering

Vedi [[Clustering Index]].

![[DM-L07-p082.png]]

An index is **(strongly) clustering** if its data entries are stored in an order **coherent with the order of the data records** in the data file; otherwise it is **non-clustering** (unclustered). In the figure, on the left the data entries of an unclustered index point all over the data file; on the right the pointers of a clustered index go to consecutive data pages.

An index can still be **weakly clustering**: for each value $V$ of the search key, all tuples with value $V$ are on the same page (or on as few linked pages as can hold them), even if the file is not sorted on the search key. Strongly clustering ⇒ weakly clustering. Some authors call "clustering" what is here "weakly clustering". In the course "clustering" means strongly clustering.

- A sorted index using alternative 1 is clustered by definition.
- Otherwise, an index is clustered only if the data file is sorted on its search key.
- A clustered index supports **range search** effectively.
- There can be **at most one** clustered index per data file (the file has one physical order).

### Primary and secondary

- A **primary (key) index** has a search key that **includes the primary key**; otherwise it is a **secondary** index.
- Some texts use "primary index" for "strongly clustering index" and "secondary" for "non-clustering": beware.
- **Duplicates** = data entries with the same search key value. A primary index has none; a secondary index typically has some; a secondary index whose search key contains a (non-primary) key is **unique** and has none.
- A secondary non-unique index can avoid duplicates by using alternative 3 (one entry per value with a rid list), or alternative 2 with a weakly clustering index (one entry per value pointing to the first record; the others follow).

### Dense and sparse

Vedi [[Dense and Sparse Index]].

![[DM-L07-p088.png]]

An index is **dense** if every search key value appearing in the data file appears in at least one data entry; otherwise **sparse**. On the right a dense index on `age` (every age value has an entry); on the left a sparse index on `name` with one entry per data page (Azzurri, Lilla, Verdi: the first name on each page). A sparse index only works if the file is sorted on its key: **a sparse index is clustered**, so there is at most one sparse index per file. An index using alternative 1 is dense by definition; a sparse index is more compact.

![[DM-L07-p089.png]]

A dense index is **strongly dense** if it has exactly one data entry per data record, carrying that record's value: with alternatives 2–3 the references are **rids** (green arrows).

![[DM-L07-p090.png]]

In a sparse index there is typically one data entry per data page, with the key of the first record of the page: the references are **page ids** (red arrows). In this figure many records share the name Azzurri, so two data entries have the key "Azzurri".

### Simple and composite search keys

A search key is **simple** (one field) or **composite**. With a composite key, an **equality query** fixes all fields; a query fixing only a **prefix** of the fields is in fact a **range query**. Composite indexes support more queries and allow **index-only evaluation** when all fields needed by the query are in the search key; but they are updated more often.

![[DM-L07-p092.png]]

Four indexes on records ordered by name: on $\langle age, sal\rangle$, $\langle age\rangle$, $\langle sal, age\rangle$, $\langle sal\rangle$. The composite indexes sort lexicographically: $\langle age,sal\rangle$ is ordered by age and, for equal age, by salary. A query `age = 20` is a range on $\langle age, sal\rangle$, while `sal = 3000` cannot use $\langle age, sal\rangle$ efficiently (not a prefix).

### Single level and multi level

A **single-level** index is one index file over the data file. A **multi-level** index builds an index on an index file, recursively.

---

## Sorted index organization

### Basic idea

![[DM-L07-p095.png]]

To find students with avg-grade > 27 we could binary-search a file sorted on avg-grade, but for large files even that is expensive. Idea: build an auxiliary **sorted file (index)** of search key values with pointers to data pages: binary search now runs on a much smaller file (data entries are smaller than records, and the index can even be sparse).

- **Clustering sorted index** (primary sorted index, or **indexed sequential file**): the data file is sorted on the same search key; often the key is the primary key.
- **Non-clustering sorted index** (secondary sorted index): the data file is unsorted (heap) or sorted on other fields.
- Alternative 1 is never used; by default alternative 2.

### Clustering sorted index on a key (unique)

**Dense**:

![[DM-L07-p101.png]]

The dense index (left) has one entry per key (10, 20, …, 120), each pointing to the record in the sequential file (right, two records per page). Index and data file have the same order; their pages may be contiguous or chained.

- A data entry is much smaller than a record, so the index uses far fewer pages.
- It is especially useful when the **index fits in the buffer** but the data file does not: then one page access suffices for any key.
- Binary or interpolation search on the index handles equality searches.

> [!example] Dense index size
> $10^6$ tuples, 10 per 4096-byte page → 100,000 pages ≈ 400 MB. Key 30 bytes + pointer 8 bytes = 38 bytes → 100 pairs per page. The dense index has $10^6/100 = 10{,}000$ pages ≈ 40 MB, which may fit in the buffer; otherwise binary search needs $\lceil\log_2 10{,}000\rceil = 14$ accesses (13–14).

**Sparse**: one data entry per data page, with the key of the first record in the page. To find $K$, search the index for the **largest key ≤ K** and follow its pointer to the data page, then search that page.

![[DM-L07-p106.png]]

The sparse index contains 10, 30, 50, 70, … (the first key of each data page). Page pointers can be smaller than rids.

> [!example] Sparse index size
> 100,000 data pages → 100,000 entries → $100{,}000/100 = 1{,}000$ index pages ≈ 4 MB: plausibly in main memory.

![[DM-L07-p109.png]]

If the data file is **contiguous**, pointers can be omitted: the $i$-th index entry corresponds to the $i$-th page, at offset $(i-1)\times$ page size (e.g. $K_3$ → $(3-1)\cdot1024=2048$ bytes).

| Dense | Sparse |
|---|---|
| can tell whether a record exists without accessing the file (index-only) | less space: more of the index stays in memory |
| more space | checking existence requires accessing the data page |

**Range search**: find the first value, then move forward in the index or in the data file (possible because the file is sorted coherently with the index). With a weakly clustering index, the range must be processed value by value, accessing data pages for each.

### Clustering sorted index on a non-key (duplicates)

![[DM-L07-p114.png]]

1. **Strongly dense with duplicates** (alternative 2): one entry per record (10, 10, 10, 20, 20, 30, 30, 30, …). To find $K$: find the first $K$ in the index, take the following $K$s, follow all pointers.

![[DM-L07-p116.png]]

2. **Dense with alternative 3**: one entry per value with the list of pointers to all its records.

These two solutions are rarely used, because the next one is better.

![[DM-L07-p118.png]]

3. **(Non-strongly) dense, alternative 2, no duplicates**: one entry per distinct value, pointing to the **first** record with that value. To find 20: follow the pointer, then move forward in the (sorted) data file, sequentially or along the page chain.

![[DM-L07-p120.png]]

4. **Sparse, usual rule**: one entry per page with the first key of the page (duplicates may appear in the index: 10, 10, 20, 30). Careful when searching for 20 or 30: a value may start on the page *before* the one whose first key equals it. Rule: find the last entry $E_1$ with key ≤ K, move backward to the first entry $E_2$ with key < K (or the first entry); all pages from $E_2$ to $E_1$ may contain $K$. For 20: $E_1$ = the entry 20, $E_2$ = the second entry 10; the page of $E_2$ ends with 20s.

![[DM-L07-p123.png]]

5. **Sparse, pointing to the first instance of each value**: the entry for a page holds the smallest key in that page that is **new** (did not appear in previous pages); pages with no new value have no entry. To find $K$, look for the entry equal to $K$, or less than $K$ with the next greater than $K$; follow it and scan forward. For 20: entry 20 → its page; for 35: entry 30 (next is 40) → page with 30, 35.

### Multi-level clustering sorted index

![[DM-L07-p126.png]]

A sorted index can itself be large; put a **sorted index on the index**: here the 2nd level (10, 90, 170, 250, 330, …) points to pages of the 1st level (10, 30, 50, …), which point to the data file. The first level can be dense or sparse, but **higher levels must be sparse** (a dense index on an index would be as large as the index). If the second level fits in memory, 2 page accesses find any record (2–3 with three levels).

> [!example] Two levels
> 1,000 first-level (sparse) pages → second level of $1{,}000/100=10$ pages: certainly in the buffer.

(Insertion and deletion in a clustering sorted index are left to the students.)

### Non-clustering sorted index on a key

The data file is sorted on another field.

![[DM-L07-p135.png]]

A **sparse** non-clustering index makes **no sense**: the first key of each data page (30, 20, 80, 100, …) says nothing about where the other keys are.

![[DM-L07-p136.png]]

A **dense** non-clustering index makes sense: one entry per record (10, 20, 30, …), with **record pointers** going to scattered pages.

- It supports **equality search** reasonably well.
- It supports **range search** well only with **index-only** access; if the data file must be accessed, each record may be on a different page and the cost grows a lot.

![[DM-L07-p138.png]]

Multi-level works here too: first level dense, second level sparse.

### Non-clustering sorted index on a non-key

With duplicates, the pointers of an index page go to many different data pages: retrieving all records with key 10 may require visiting three different pages, many more accesses than with a clustering index.

![[DM-L07-p142.png]]

A popular method: dense index with alternative 3 realized through **buckets**: each index value points to a bucket containing the pointers to all its records.

Vedi [[Inverted List]].

![[DM-L07-p145.png]]

Buckets (**inverted lists**) also help query answering. `EMP(name, dept, floor, …)` with a primary index on name and secondary indexes on dept and floor. *Employees of the Toy department on the 2nd floor*: intersect the pointer set of bucket "Toy" with that of bucket "2nd", then fetch only the matching records.

![[DM-L07-p147.png]]

The same idea is used in **information retrieval**: for each word ("cat", "dog") an inverted list points to the documents containing it. Queries such as *cat AND dog*, *cat OR dog*, *cat AND NOT dog* become intersection, union and difference of pointer sets.

### Another application: clustered files

Normally one file stores one relation, but a DBMS can store two relations in one file, a **clustered file** (not to be confused with a clustered index).

`Movie(title, year, length, studioname)`, `Studio(name, address, president)`; `studioname` references `Studio`.

- Query 1: `select title, year from Movie where studioname = ZZZ` → sort Movie by studioname and build a secondary sorted index on it.
- Query 2: `select president from Movie, Studio where title = YYY and Movie.studioname = Studio.name` → a join.

![[DM-L07-p151.png]]

Store each Studio record followed by the Movie records of that studio (dropping `studioname`): a data page then contains "studio 1, its movies, studio 2, its movies, …".

- The president of the studio of a movie is likely on the **same page** as the movie, saving at least one access; the movies of a studio are near the studio.
- To find studios by name, use a **clustering primary sorted index on Studio.name** (query 1); to find movies by title, a **non-clustering secondary sorted index on Movie.title** (query 2).
- Price: scanning one relation is more expensive (pages mix both relations).

Base triennale: this is a physical-level form of what logical design calls *accorpamento* (merging tables to save joins): [[06 - BD - Progettazione Logica#Accorpamento caso 4, per denormalizzazione|BD — Accorpamento per denormalizzazione]] · [[Foreign Key]] · [[Join]]

---

## Tree-based index organization

### The problem with sorted indexes

![[DM-L07-p155.png]]

With insertions and deletions a sorted index degrades: keys that do not fit in the sequential area (31, 35, 36, 32, 38, 34 inserted between 30 and 40) go to an **overflow area** that is not sequential, so searches must follow chains.

### General characteristics of tree indexes

Iterating the multi-level idea until the top fits in one page gives a **tree index**, which can also solve the degradation problem. In a tree index:

- every node is a **page**;
- the **leaves** contain the data entries;
- every search goes from the **root** to a leaf, so the **height** must be small;
- links between nodes are pointers between pages.

![[DM-L07-p157.png]]

An intermediate node has $m+1$ pointers $P_0..P_m$ separated by $m$ keys $K_1\le\ldots\le K_m$: $P_{i-1}$ leads to entries **less than** $K_i$; $P_i$ leads to entries **≥ $K_i$** (and $< K_{i+1}$).

Two kinds: **ISAM** for static data, **B+-tree** for dynamic data. (We assume no duplicate search key values; everything generalizes.)

### ISAM

Vedi [[ISAM]].

![[DM-L07-p159.png]]

**ISAM** (*Indexed Sequential Access Method*): non-leaf pages contain index entries, leaves contain data entries and can be scanned sequentially; extra records go into **overflow pages** chained to the primary leaf pages. The structure is **static**: leaves can change, intermediate nodes never.

- ISAM is **balanced**: all root-to-leaf paths have the same length (except possibly the last).
- All non-leaf nodes have the same number $F$ of children, the **fan-out**; a tree of height $h$ has $F^h$ leaves.
- With $F\ge100$, a tree of height 4 has $10^8$ leaf pages: **4 I/Os** find any page (3 if the root is in the buffer), versus $\log_210^8>25$ for binary search.
- **Creation**: allocate leaves sequentially, then build the intermediate nodes.
- **Search**: from the root, compare keys until a leaf: $\log_FN$ ($N$ = leaves).
- **Insert**: find the leaf, add an overflow page if needed, insert the record in the data file.
- **Delete**: remove from the leaf; deallocate an overflow page if it becomes empty; delete the data record.

![[DM-L07-p162.png]]

Example with 2 entries per node: root 40; children (20, 33) and (51, 63); leaves 10* 15* | 20* 27* | 33* 37* | 40* 46* | 51* 55* | 63* 97*.

![[DM-L07-p163.png]]

Inserting 23*, 48*, 41*, 42*: leaves are full, so 23* goes to an overflow page of leaf 20*–27*, 48* and 41* to an overflow page of leaf 40*–46*, and 42* to a second overflow page chained after it.

![[DM-L07-p164.png]]

Deleting 42*, 51*, 97*: 42*'s overflow page becomes empty and is deallocated; 51* and 97* disappear from their leaves. Note that **51 still appears in the index entries**: only leaves can change.

### B+-tree

Vedi [[B+-Tree]].

A **B+-tree** is a balanced tree that overcomes ISAM's problems with insertions and deletions.

- If a page holds $d$ keys and $d+1$ pointers, $d$ is the **rank** (order) of the tree.
- Every node holds $m_i$ entries with $\lceil (d+1)/2\rceil \lesssim m_i\le d$ (at least half full); the root may have fewer (at least one).
- The **leaves** contain the data entries and are **linked in a list** in search-key order, which supports range queries: find the leaf of the first value, then scan the list.

**Height.** If every non-leaf node has $n$ children, $h$ levels give $n^h$ leaves, so $h=\log_nM$ for $M$ leaves. With variable fan-out, use the average $F$ (often $\frac{d+d/2}{2}=\frac34d$): $h\approx\log_FM$.

#### Search

![[DM-L07-p167.png]]

Searching `24 < age ≤ 44`: from the root (12, 78) go to the middle child ($12\le age<78$), then to (19, 56) and its middle child ($19\le age<56$), then to (33, 44), reaching leaf F1, which contains the first age greater than 24. Then scan the linked leaves F1 → F2 → F3 until the first value outside the range (Bianchi, 50).

- Equality search on a key costs at most the **height**, $\log_FN$.
- $F$ should be as large as possible (it depends on the block size): typically $F\ge100$, and with $F=100$ and $10^6$ leaves the cost is 4 (3 with the root in the buffer). Most pages are leaves.
- B+-trees (especially clustering ones) are **ideal for range** access and very effective (though not ideal, compared to hashing) for equality.

#### Insertion

Recursive algorithm (index only; insertion in the data file is orthogonal):

1. find the leaf and insert the key if there is room;
2. otherwise **split** the leaf into two, dividing the keys equally;
3. the split produces a new pointer to insert in the parent: do it recursively;
4. if the root is full, split it and create a **new root** above: the tree grows **by one level only at the root**.

**Splitting a leaf** $N$ with $n$ keys (the maximum) to insert the $(n+1)$-th key: let $S$ be the sorted $n+1$ keys; create a right sibling $M$; keep the first $\lceil(n+1)/2\rceil$ pairs in $N$, move the others to $M$; **copy** the smallest key of $M$ up to the parent with a pointer to $M$.

**Splitting a non-leaf** $N$ with $n$ keys and $n+1$ pointers receiving one more pointer: keep the first $\lceil (n+2)/2\rceil$ pointers in $N$ and move the rest to $M$; the first $\lceil n/2\rceil$ keys stay in $N$, the last $\lfloor n/2\rfloor$ go to $M$, and the **middle key moves up** to the parent (it stays in neither node).

![[DM-L07-p173.png]]

Example ($d=4$): root (14, 19, 24, 33), leaves 2* 3* 5* 7* | 14* 16* | 19* 20* 22* | 24* 27* 29* | 33* 34* 38* 39*. Insert 8*.

![[DM-L07-p174.png]]

The leaf 2* 3* 5* 7* is full: split into N = 2* 3* and M = 5* 7* 8*; **5 is copied** to the parent (it stays in the leaf). The root would now have 5 keys (5, 14, 19, 24, 33): split into (5, 14) and (24, 33) and **push 19 up** (it does not stay in the children). Every non-root node keeps at least $d/2=2$ entries.

![[DM-L07-p175.png]]

The new root contains 19: the height increased by one. Typically a B+-tree grows **in breadth**; it grows in depth only when inserting into a full root.

#### Deletion

If after the deletion node $N$ still has at least the minimum number of keys, nothing else is needed. Otherwise:

1. **Redistribution**: if an adjacent sibling has more than the minimum, move one key-pointer pair to $N$ and adjust the separating key in the parent (if the right sibling $M$ gives its smallest key, the parent's key for $M$ must become $M$'s new smallest key).
2. **Coalesce**: if neither sibling can lend, merge $N$ with one of them (together they fit in one node), adjust the parent and delete a key and pointer there; if the parent underflows, apply the algorithm recursively. This may **lower the height**.

Sometimes coalesce is not implemented: deletions leave free space for future insertions.

![[DM-L07-p178.png]]

(a) $n=4$, parent (10, 40, 100), leaves (10, 20) and (40, 50): delete 50.

![[DM-L07-p179.png]]

(b) The leaf (40) underflows and its sibling (10, 20) has only the minimum: **coalesce** into (10, 20, 40) and remove 40 from the parent, which becomes (10, 100).

![[DM-L07-p181.png]]

(c) If the left sibling is (10, 20, 30, 35), it can lend: **redistribute** 35 into the right leaf, which becomes (35, 40), and change the parent's separator from 40 to 35.

![[DM-L07-p182.png]]

(d) **Non-leaf coalesce**, delete 37: root 25; internal nodes (10, 20) and (30, 40); leaves (1, 3), (10, 14), (20, 22), (25, 26), (30, 37), (40, 45).

![[DM-L07-p185.png]]

Leaf (30) underflows; siblings (25, 26) and (40, 45) have only the minimum, so it is merged into (25, 26, 30). The internal node (30, 40) loses a key and is left with (40) and two children, below the minimum; its sibling (10, 20) cannot lend, so the two internal nodes are merged **pulling down the root key 25**: the new node (10, 20, 25, 40) becomes the **new root**, and the height decreases.

### Cost of a clustered B+-tree index

Assume alternative 1 and fan-out $F$. Leaves are on average **67% full**, so the physical leaf pages are $B' = 1.5B$ ($B$ = minimum pages needed for the data entries, here the data records).

| Operation | Time | Pages | O |
|---|---|---|---|
| Scan | $1.5B(D+RC)$ | $1.5B$ | $O(B)$ |
| Equality | $D\log_F(1.5B)+C\log_2R$ | $\log_F(1.5B)$ | $O(\log_FB)$ |
| Range | as equality + further leaves | | |
| Insertion | $D\log_F(1.5B)+C\log_2R+C+D$ | | $O(\log_FB)$ |
| Deletion | similar to insertion | | |

(Typically the records of interest are on one page; in practice the root is in the buffer, saving one access; costs of splits/merges are ignored. With alternative 2, compute the leaf pages needed for the data entries and multiply by 1.5.)

> [!question]- Exercise 3 — alternative 2 and 3 for a clustered B+-tree
> With alternative 2 the leaves contain $(k, rid)$ pairs: the number of leaf pages is $1.5\times$(entries / entries per page) and is much smaller than the data file. Equality: $\log_F(\text{leaves})$ to reach the leaf, plus the data page(s): since the index is clustered, the matching records are on consecutive pages, so a range costs one leaf traversal plus the data pages of the range (not one page per record). Dense vs sparse: a sparse index has one entry per data page, fewer leaves (height decreases), but it can only answer existence by visiting the data page. With alternative 3 the leaves are even smaller for non-unique keys (one entry per value), at the cost of variable-length entries.

### Cost of an unclustered B+-tree index

Assume a heap data file and a dense index with alternative 2, data entries 1/10 of a record: leaves need $0.1B$ pages, physically $1.5\cdot0.1B=0.15B$; a leaf page holds $10\cdot0.67R=6.7R$ entries.

| Operation | Cost |
|---|---|
| Scan (in key order) | $0.15B(D+6.7RC)+BR(D+C)$ |
| Equality | $D\log_F(0.15B)+C\log_2(6.7R)+XD$ |
| Range | like equality, $X$ may be large |
| Insertion | $2D+C$ (heap) $+D\log_F(0.15B)+C\log_2(6.7R)+D$ |
| Deletion | $D\log_F(0.15B)+C\log_2(6.7R)+D+2(C+D)$ |

- Scan through the index can cost **one I/O per record** ($BR$): it is often better to **ignore the index**, and if order is needed, sort the file: about $4B$ I/Os with a 2-pass sort, much less.
- In equality and range, $X$ is the number of matching records: possibly one I/O each. Again, with many matches, a scan or a sort of the file may be cheaper.

### Estimating the number of leaves

- Leaves are 67% full: physical leaves = 1.5 × required leaves.
- Alternative 1: required leaves = data pages.
- Dense index on a key: one entry per record; divide by entries per page.
- Dense non-unique index with duplicates: estimate the average number of records per value.
- Sparse index: one entry per data page.

---

## Discussion

| Organization | Strengths | Weaknesses |
|---|---|---|
| Heap file | space; scan and insertion | search and deletion |
| Sorted file | space; search better than heap | insertion and deletion |
| Clustered tree index | limited space overhead; efficient insert, delete, search; **optimal for range** | |
| Static hash index | efficient equality, insertion, deletion; **optimal for equality** | scan and range search |

> [!summary]
> No file organization is uniformly superior. The physical design of a database chooses, relation by relation, the organization and the indexes that best fit the workload; the query optimizer of [[08 - DM - Evaluation of Relational Operators]] then chooses, query by query, which of them to use.

### Self-assessment questions

1. Why does a slot directory allow records to move within a page without changing their rid?
2. Derive the cost of an equality search on a sorted file with binary search.
3. How many passes does external merge sort need for $B$ pages and $F$ frames? When are two passes enough?
4. What is the difference between search key and key? Between clustering and primary index?
5. Why must a sparse index be clustering?
6. Why do higher levels of a multi-level index have to be sparse?
7. Show the B+-tree after inserting 8* in the example, and explain which keys are copied up and which are pushed up.
8. When is it better to ignore an unclustered index and scan or sort the file?
