---
title: "Data Management - Introduction and Relational Model Recap"
aliases:
  - "Data Management Introduction"
  - "Relational Model and Window Functions"
tags:
  - data-management
  - databases
  - relational-algebra
  - sql
  - window-functions
course: "Data Management"
academic-year: "2024/2025"
source: "[[1-Introduction.pdf]]"
---

# Data Management - Introduction and Relational Model Recap

> [!abstract] Purpose of this note
> This note follows the same conceptual order as the source material: course context, relational model, relational algebra, SQL, aggregation, grouping, and window functions. It expands definitions, makes implicit reasoning explicit, and adds worked examples so that the material can be read as a self-contained explanation rather than as presentation prompts.

## Course context

### Intended audience and prerequisites

The course is intended for students in the Master of Science in Engineering in Computer Science and the Master's programme in Management Engineering. It is a 6-credit course.

The course assumes familiarity with:

- the fundamentals of programming structures and programming languages;
- the fundamentals of database systems;
- SQL;
- the relational data model;
- the Entity-Relationship model;
- conceptual and logical database design.

These prerequisites matter because the course does not begin from the question "what is a database?". Instead, it studies how a Database Management System (DBMS) is structured, how it executes and protects data-intensive work, and how a designer or administrator reasons about performance, correctness, and data organization.

### Learning objectives

The course has three broad goals:

1. Understand the structure and functionality of data management systems from the perspective of a **data administrator**. This includes knowing what must be configured, monitored, protected, and optimized.
2. Understand the same systems from the perspective of a **data management tool designer**. This requires looking inside the DBMS at modules such as the buffer manager, transaction manager, recovery manager, storage layer, and query processor.
3. Study additional data management paradigms and workloads, including data warehousing and NoSQL systems.

> [!tip] Two complementary perspectives
> An administrator asks, "How do I make this system reliable, secure, and fast?" A system designer asks, "Which algorithms and internal structures make those guarantees possible?" The course connects these two questions.

### Course organization

The source material identifies Maurizio Lenzerini as the teacher and provides the following reference pages:

- Teacher's page: <http://www.diag.uniroma1.it/lenzerini>
- Course page: <http://www.diag.uniroma1.it/lenzerini/home/?q=node/53>

The stated teaching format includes lectures, exercises integrated into the lectures, possible individual or group projects, a written examination, and an oral examination when needed.

> [!info] Administrative snapshot from the 2024/2025 material
> - Monday lecture: 13:00-15:00, Classroom 41.
> - Wednesday lecture: 10:00-13:00, Classroom 41.
> - Teaching location: Via Eudossiana 18, with an online lecture link also supplied in the course material.
> - Office hours: Tuesday at 17:00, through the indicated Google Meet room.
>
> These details belong to the stated academic year and should be checked against the current course page before being relied upon.

### Learning material

The indicated material consists of:

- M. Lenzerini's lecture notes, distributed through Moodle;
- R. Ramakrishnan and J. Gehrke, *Database Management Systems*, McGraw-Hill;
- papers dedicated to specific topics;
- exercises and problems from previous examinations on the course website.

The lecture notes establish the course's terminology and expected level of formalism. A textbook provides broader explanations and alternative examples, while papers are useful when a topic cannot be treated adequately through a general-purpose textbook alone.

### Course roadmap

The course connects logical data modelling with the internal behavior of a DBMS.

#### Data warehousing

- data warehouse architectures and operators;
- data warehouse design.

A data warehouse is designed primarily for analytical workloads. It integrates historical data and supports aggregation, reporting, and multidimensional analysis. This differs from a conventional operational database, whose main objective is to process day-to-day transactions efficiently.

#### NoSQL databases

- document-oriented databases;
- graph databases;
- the relationship between OLAP and OLTP workloads.

NoSQL does not mean that relational databases are obsolete. It groups several models that make different trade-offs about schema, joins, distribution, and access patterns. Document databases organize records around aggregate documents; graph databases make relationships first-class objects.

#### OLTP and OLAP

**Online Transaction Processing (OLTP)** systems support frequent, short, operational transactions such as purchases, bookings, and account updates. They usually favor normalized schemas, fast point lookups, concurrency, and strong transactional guarantees.

**Online Analytical Processing (OLAP)** systems support scans, aggregations, historical analysis, and decision-making. They often use denormalized or multidimensional structures and are optimized for reading large volumes of data. A data warehouse is primarily an OLAP environment, although real architectures may combine operational and analytical techniques.

#### DBMS modules

- overall DBMS architecture;
- buffer manager.

The buffer manager moves database pages between persistent storage and main memory. Because disk and memory have very different costs and persistence properties, buffer management is fundamental to performance and correctness.

#### Transaction management

- the concept of transaction;
- concurrency control.

A transaction represents a logical unit of work. Concurrency control permits multiple transactions to execute together without producing outcomes that violate the intended isolation guarantees.

#### Crash management

- classification of failures;
- recovery.

Recovery mechanisms use information such as logs to restore a valid state after failures. The system must distinguish, for example, a transaction failure from a process, system, or storage failure because each requires a different response.

#### Physical database structures

- file organizations for database management;
- principles of physical database design.

The logical schema describes *what* the data means. Physical design decides *how* it is stored: page layout, record organization, indexes, clustering choices, and other structures that strongly affect execution cost.

#### Query processing

- evaluation of relational algebra operators;
- fundamentals of query optimization.

A SQL query describes the desired result. The query processor transforms it into a plan made of physical operators. Optimization is the task of selecting a plan with an acceptable estimated cost from many equivalent alternatives.

---

## Recap: relational databases

## The relational data model

The relational model was introduced by E. F. Codd in 1970. Its central idea is to represent data through **relations**, a mathematical concept that can be visualized as a table.

Consider a checking-account relation:

| branch_name | account_no | customer_name | balance |
|---|---|---|---:|
| Orsay | 10991-06284 | Abiteboul | 3567.53 |
| Hawthorne | 10992-35671 | Hull | 11245.75 |

The table representation is convenient, but the mathematical definition is more precise. Given domains $D_1, D_2, \ldots, D_k$, a $k$-ary relation $R$ is a subset of their Cartesian product:

$$
R \subseteq D_1 \times D_2 \times \cdots \times D_k
$$

An element of the relation is a **tuple**:

$$
(a_1,a_2,\ldots,a_k)
$$

where each value $a_i$ belongs to the corresponding domain $D_i$.

### Essential terminology

| Term | Meaning |
|---|---|
| Relation schema | The relation name and its attributes, such as `Account(branch_name, account_no, customer_name, balance)` |
| Relation instance | The finite set of tuples currently stored for that schema |
| Attribute | A named component of a tuple, visualized as a column |
| Tuple | One element of the relation, visualized as a row |
| Domain | The admissible set and interpretation of values for an attribute |
| Arity / degree | Number of attributes in the schema |
| Cardinality | Number of tuples in a particular relation instance |

> [!important] Mathematical relation versus SQL table
> A mathematical relation is a set: it has no duplicate tuples and no intrinsic row order. SQL usually works with **bags** or **multisets**, so duplicates may exist unless `DISTINCT`, a key, or another constraint removes them. SQL output is unordered unless the outer query includes `ORDER BY`.

## Query languages for the relational model

Codd introduced two foundational query formalisms.

### Relational algebra

Relational algebra is **procedural** in the formal sense: a query is an expression that specifies a sequence or composition of operations over relations. Each operator consumes one or more relations and returns another relation. Because input and output share the same kind of object, operators can be nested freely; this property is called **closure**.

### Relational calculus

Relational calculus is **declarative**: a query states the logical property that result tuples must satisfy, using first-order logic, rather than prescribing a sequence of relational operators.

### Codd's theorem

Codd's theorem establishes that relational algebra and the safe forms of relational calculus have essentially the same expressive power. The important lesson is that a procedural algebraic description and a declarative logical description can characterize the same class of relational queries.

### SQL

SQL is the practical standard used by relational DBMSs. It combines declarative features with constructs that reflect relational algebra, grouping, ordering, recursion, and other extensions. Users generally state the desired result, while the optimizer decides how to compute it.

> [!note] Why relational algebra still matters
> Even when users write SQL, a DBMS commonly translates the query into an internal algebraic representation. Relational algebra therefore provides both a theory for understanding queries and a vocabulary for query plans and optimization rules.

---

## The five basic operations of relational algebra

The core algebra can be generated from five operations:

1. union;
2. difference;
3. Cartesian product;
4. projection;
5. selection.

Union, difference, and Cartesian product are binary operators. Projection and selection are unary operators. Renaming may be treated as an explicit operator in extended presentations, but the source notation permits renaming within projection.

Any syntactically valid composition of these operators is a relational algebra expression. Other familiar operations, including intersection and joins, can be defined from this core.

## Union and difference

Let $R$ and $S$ be $k$-ary relations.

### Union

The union contains every tuple that occurs in at least one input:

$$
R \cup S = \{t \mid t \in R \lor t \in S\}
$$

### Difference

The difference contains tuples in the first input but not in the second:

$$
R - S = \{t \mid t \in R \land t \notin S\}
$$

### Compatibility requirement

The two inputs must be **union-compatible**:

- they must have the same arity;
- corresponding components must have compatible domains or SQL data types;
- attribute names do not necessarily have to match, because a renaming can align them.

Consider:

**Employee**

| Code | Name | Age |
|---:|---|---:|
| 7274 | Rossi | 42 |
| 7432 | Neri | 54 |
| 9824 | Verdi | 45 |

**Director**

| Code | Name | Age |
|---:|---|---:|
| 9297 | Neri | 33 |
| 7432 | Neri | 54 |
| 9824 | Verdi | 45 |

Then:

**$Employee \cup Director$**

| Code | Name | Age |
|---:|---|---:|
| 7274 | Rossi | 42 |
| 7432 | Neri | 54 |
| 9824 | Verdi | 45 |
| 9297 | Neri | 33 |

The two common tuples appear only once because relational algebra uses set semantics.

**$Employee - Director$**

| Code | Name | Age |
|---:|---|---:|
| 7274 | Rossi | 42 |

Difference is not commutative: in this example, $Director - Employee$ would instead contain `(9297, Neri, 33)`.

## Cartesian product

Let $R$ have arity $m$ and $S$ have arity $n$. Their Cartesian product combines every tuple of $R$ with every tuple of $S$:

$$
R \times S = \{(a_1,\ldots,a_m,b_1,\ldots,b_n) \mid (a_1,\ldots,a_m) \in R \land (b_1,\ldots,b_n) \in S\}
$$

The result has arity $m+n$, and its cardinality is:

$$
|R \times S| = |R| \cdot |S|
$$

Example:

**Employee**

| Emp | Dept |
|---|---|
| Rossi | A |
| Neri | B |
| Bianchi | B |

**Dept**

| Code | Chair |
|---|---|
| A | Mori |
| B | Bruni |

**$Employee \times Dept$**

| Emp | Employee.Dept | Dept.Code | Chair |
|---|---|---|---|
| Rossi | A | A | Mori |
| Rossi | A | B | Bruni |
| Neri | B | A | Mori |
| Neri | B | B | Bruni |
| Bianchi | B | A | Mori |
| Bianchi | B | B | Bruni |

The product by itself often creates many combinations that have no business meaning. Its main role is to provide candidate pairs that a later selection can filter. A join is precisely this combination of product and filtering.

> [!warning] Attribute ambiguity
> If both inputs contain an attribute with the same name, qualify it as `Employee.Dept` and `Dept.Dept`, or rename one of the attributes before combining the relations.

## Projection

Projection selects, reorders, and possibly renames attributes. The common notation is:

$$
\pi_{A_1,\ldots,A_m}(R)
$$

or:

$$
\operatorname{PROJ}_{A_1,\ldots,A_m}(R)
$$

Applying a projection:

- removes every attribute not listed;
- orders the remaining attributes according to the list;
- may rename attributes;
- eliminates duplicate result tuples under relational algebra's set semantics.

Consider:

| Code | Name | Site | Salary |
|---:|---|---|---:|
| 7309 | Neri | Napoli | 55 |
| 5998 | Neri | Milano | 64 |
| 9553 | Rossi | Roma | 44 |
| 5698 | Rossi | Roma | 64 |

Then:

$$
\pi_{Name,Site}(Employee)
$$

produces:

| Name | Site |
|---|---|
| Neri | Napoli |
| Neri | Milano |
| Rossi | Roma |

The two occurrences of `(Rossi, Roma)` collapse into one tuple. In SQL, `SELECT Name, Site FROM Employee` would normally preserve both occurrences, whereas `SELECT DISTINCT Name, Site FROM Employee` matches the set-based projection.

### Renaming during projection

A notation such as:

$$
\pi_{N \leftarrow Name,\; A \leftarrow Age}(Employee)
$$

means: retain `Name` and `Age`, but call the output attributes `N` and `A`.

### Positional notation

Attributes can also be referenced by position. If $R(A,B,C,D)$, then:

$$
\pi_{C,A}(R) = \pi_{3,1}(R)
$$

Formally:

$$
\pi_{i_1,\ldots,i_m}(R) = \{(a_1,\ldots,a_m) \mid \exists(b_1,\ldots,b_k) \in R:\ a_1=b_{i_1},\ldots,a_m=b_{i_m}\}
$$

Named attributes are usually clearer and less fragile: positional references change meaning if the schema's column order changes.

## Selection

Selection filters tuples while preserving the relation's attributes:

$$
\sigma_{\Theta}(R)
$$

or:

$$
\operatorname{SEL}_{\Theta}(R)
$$

The condition $\Theta$ is evaluated for each tuple. The result contains exactly the tuples for which the condition is true:

$$
\sigma_{\Theta}(R) = \{t \in R \mid \Theta(t)\}
$$

Conditions are built from:

- comparisons such as $=, \neq, <, >, \leq, \geq$;
- constants, attribute names, or positional components;
- Boolean connectives: conjunction $\land$, disjunction $\lor$, and negation $\neg$.

Examples include:

$$
\sigma_{balance > 10000}(Savings)
$$

$$
\sigma_{branch\_name = \text{"Aptos"}}(Savings)
$$

$$
\sigma_{branch\_name = \text{"Aptos"} \land balance < 1000}(Savings)
$$

For the employee relation above:

$$
\sigma_{Salary > 50}(Employee)
$$

returns:

| Code | Name | Site | Salary |
|---:|---|---|---:|
| 7309 | Neri | Napoli | 55 |
| 5998 | Neri | Milano | 64 |
| 5698 | Rossi | Roma | 64 |

### Ordered and unordered domains

The operators `<`, `>`, `<=`, and `>=` require an ordering on the domain. Numeric values, dates, and lexicographically ordered strings may support such comparisons. For a domain with no meaningful total order, only equality and inequality may be appropriate.

When attributes are referenced by component number, a notation such as `$4 > 100` means that the fourth component must be greater than 100.

> [!note] SQL and `NULL`
> Classical relational algebra assumes ordinary values and two-valued logic. SQL adds `NULL` and three-valued logic: a comparison with `NULL` is generally `UNKNOWN`, not `TRUE` or `FALSE`. Use `IS NULL` and `IS NOT NULL` when testing for missing values.

## Relational algebra expressions

A relational algebra expression is obtained by recursively combining relation schemas and operators. A simplified grammar is:

$$
E ::= R \mid S \mid (E_1 \cup E_2) \mid (E_1-E_2) \mid (E_1 \times E_2) \mid \pi_X(E) \mid \sigma_{\Theta}(E)
$$

where:

- $R,S,\ldots$ are relation schemas;
- $X$ is an attribute list, possibly including renaming;
- $\Theta$ is a condition.

The expression tree matters. For example:

$$
\pi_{Name}(\sigma_{Salary>50}(Employee))
$$

first selects well-paid employees and then keeps their names. The closure property guarantees that the output of selection can immediately serve as the input of projection.

---

## Derived operations

An operation is **derived** when it can be expressed using the five basic operators. Derived operators do not necessarily add expressive power, but they make queries much easier to write and understand.

## Intersection

For union-compatible relations $R$ and $S$:

$$
R \cap S = \{t \mid t \in R \land t \in S\}
$$

Intersection can be expressed using difference:

$$
R \cap S = R - (R-S) = S-(S-R)
$$

For the `Employee` and `Director` relations used earlier:

| Code | Name | Age |
|---:|---|---:|
| 7432 | Neri | 54 |
| 9824 | Verdi | 45 |

These are exactly the tuples occurring in both relations.

## Theta join

A theta join combines two relations and retains only pairs that satisfy a condition $\Theta$:

$$
R \bowtie_{\Theta} S = \sigma_{\Theta}(R \times S)
$$

If an attribute name occurs in both inputs, qualification such as `R.A` and `S.A` removes ambiguity.

An **equijoin** is a theta join whose condition consists of equality comparisons. A theta join may also use non-equality predicates such as `<`, `>`, or `!=`.

### Example: salaries of department chairs

Let:

$$
F(name,dpt,salary)
$$

represent faculty members, and:

$$
C(dpt,name)
$$

represent department chairs. The department and salary of each chair can be obtained as:

$$
C\text{-}SALARY(dpt,salary) =
\pi_{F.dpt,F.salary}
(\sigma_{F.name=C.name \land F.dpt=C.dpt}(F \times C))
$$

Including the department equality avoids accidentally matching two people with the same name in different departments.

### Expressing intersection with an equijoin and projection

For union-compatible $k$-ary relations $R(A_1,\ldots,A_k)$ and $S(B_1,\ldots,B_k)$, match tuples whose corresponding components are all equal, then project one copy:

$$
R \cap S =
\pi_{R.A_1,\ldots,R.A_k}
\left(
R \bowtie_{R.A_1=S.B_1 \land \cdots \land R.A_k=S.B_k} S
\right)
$$

Every projected tuple occurs in both inputs, and every tuple occurring in both inputs produces a match. Projection's set semantics removes any duplicate matches.

### Example: faculty earning more than their chair

Using $C\text{-}SALARY(dpt,salary)$, the names of EE faculty members whose salary exceeds their chair's salary are:

$$
\pi_{F.name}
\left(
\sigma_{
F.dpt=\text{"EE"}
\land F.dpt=C.dpt
\land F.salary>C.salary
}
(F \times C\text{-}SALARY)
\right)
$$

This is not an equijoin because the predicate includes `F.salary > C.salary`.

## Natural join

The natural join matches tuples on **all attributes that have the same name** and includes one copy of each common attribute in the result.

Suppose:

$$
Teaches(facname,course,term)
$$

and:

$$
Enrolls(studname,course,term)
$$

Their natural join matches on both `course` and `term`:

$$
Enrolls \bowtie Teaches
$$

It produces a relation such as:

$$
TaughtBy(studname,course,term,facname)
$$

The equivalent core-algebra expression is:

$$
\pi_{E.studname,E.course,E.term,T.facname}
\left(
\sigma_{T.course=E.course \land T.term=E.term}
(Enrolls \times Teaches)
\right)
$$

More generally, if $A_1,\ldots,A_k$ are the common attributes of $R$ and $S$:

$$
R \bowtie S =
\pi_{\text{all attributes, with one copy of each }A_i}
\left(
\sigma_{R.A_1=S.A_1 \land \cdots \land R.A_k=S.A_k}(R \times S)
\right)
$$

### Naive evaluation idea

A conceptual nested-loop algorithm is:

1. take each tuple of $R$;
2. compare it with every tuple of $S$;
3. retain pairs that agree on all common attributes;
4. concatenate each matching pair;
5. remove the duplicate copies of common attributes.

This explains the semantics, not necessarily the implementation. A DBMS may instead use a hash join, merge join, index nested-loop join, or another physical algorithm.

> [!warning] Natural join is schema-sensitive
> A natural join silently uses every common attribute name. If an unrelated same-named column is later added to both tables, the query's meaning changes. In production SQL, an explicit `JOIN ... ON ...` or `JOIN ... USING (...)` is often safer because the intended match is visible.

---

## Relational algebra exercises

Consider:

$$
Graduated(gcode,mark,school)
$$

$$
School(scode,city)
$$

`Graduated` records a student code, graduation mark, and school code. `School` stores every school, including schools for which there may be no matching `Graduated` tuple.

### Cities with at least one school having a student who graduated with 100

The phrase **at least one** is existential: finding one matching graduation tuple is sufficient.

1. Select graduations with mark 100.
2. Join them with their schools.
3. Project the cities.

$$
\pi_{city}
\left(
\sigma_{mark=100}(Graduated)
\bowtie_{school=scode}
School
\right)
$$

Projection removes duplicate city names, so a city with several qualifying schools still appears once.

### Schools where no student graduated with 100

Begin with all schools, then subtract the schools that have at least one mark of 100:

$$
\pi_{scode}(School)
-
\rho_{scode \leftarrow school}
\left(
\pi_{school}(\sigma_{mark=100}(Graduated))
\right)
$$

The renaming makes the operands union-compatible. This query includes schools with no graduates at all, because such schools certainly have no recorded student with mark 100.

> [!tip] General pattern for "no"
> `All candidates - candidates having a forbidden witness` is a fundamental relational-algebra pattern for negation.

### Cities where every school has a student who graduated with 100

The universal condition **every school** is most naturally solved through its negation:

> A city is valid if there does not exist a school in that city with no student who graduated with 100.

Define:

$$
GoodSchools =
\rho_{scode \leftarrow school}
\left(
\pi_{school}(\sigma_{mark=100}(Graduated))
\right)
$$

Then:

$$
BadSchools = \pi_{scode}(School) - GoodSchools
$$

and:

$$
BadCities = \pi_{city}(School \bowtie BadSchools)
$$

The answer is:

$$
\pi_{city}(School) - BadCities
$$

Expanded into one expression:

$$
\pi_{city}(School)
-
\pi_{city}
\left(
School \bowtie
\left[
\pi_{scode}(School)
-
\rho_{scode \leftarrow school}
\left(
\pi_{school}(\sigma_{mark=100}(Graduated))
\right)
\right]
\right)
$$

> [!important] Universal quantification by double negation
> "For every school, property $P$ holds" is equivalent to "there is no school for which $P$ does not hold." This transformation appears repeatedly in relational algebra and SQL.

### Students with the minimum graduation mark in each school

There may be ties, so the result must retain **all** students whose mark is minimal in their school.

Rename two copies of `Graduated`:

$$
G_1(gcode_1,mark_1,school_1) = Graduated
$$

$$
G_2(gcode_2,mark_2,school_2) = Graduated
$$

A tuple in $G_1$ is not minimal if another tuple in the same school has a smaller mark:

$$
NonMinimum =
\pi_{gcode_1,mark_1,school_1}
\left(
\sigma_{school_1=school_2 \land mark_1>mark_2}
(G_1 \times G_2)
\right)
$$

Subtract those tuples from all graduations and project the required attributes:

$$
\pi_{school,gcode}(Graduated - NonMinimum)
$$

The strict comparison `>` is essential. If two students share the smallest mark, neither has a strictly smaller competitor, so both remain in the answer.

---

## SQL: Structured Query Language

SQL is the standard language family for relational database systems. The core query form considered here is:

```sql
SELECT DISTINCT <attribute_or_expression_list>
FROM <relation_list>
WHERE <condition>;
```

More formally, if the query reads:

```sql
SELECT DISTINCT Ri1.A1, ..., Rim.Am
FROM R1, ..., Rk
WHERE gamma;
```

then:

- `R1, ..., Rk` are relation names, possibly renamed through aliases such as `R1 AS X`;
- each selected item refers to an attribute or an allowed expression;
- `gamma` is a Boolean SQL condition.

The keyword `DISTINCT` is important when relating SQL to classical relational algebra. SQL normally preserves duplicates, whereas classical relational algebra eliminates them.

## SQL and relational algebra

The basic correspondence is:

| SQL component | Relational algebra role |
|---|---|
| `FROM` | Build combinations of input tuples, conceptually a Cartesian product |
| `WHERE` | Selection |
| `SELECT DISTINCT` | Projection with duplicate elimination |

Thus:

```sql
SELECT DISTINCT Ri1.A1, ..., Rim.Am
FROM R1, ..., Rk
WHERE gamma;
```

corresponds to:

$$
\pi_{Ri_1.A_1,\ldots,Ri_m.A_m}
\left(
\sigma_{\gamma}(R_1 \times \cdots \times R_k)
\right)
$$

This is a semantic interpretation. A real DBMS does not have to materialize the full Cartesian product before filtering; the optimizer can choose a join algorithm that directly generates matching pairs.

## SQL exercises

The following solutions use the same `Graduated` and `School` schema. The relation name is consistently written as `Graduated`.

### Cities with at least one school having a mark of 100

```sql
SELECT DISTINCT s.city
FROM Graduated AS g
JOIN School AS s
  ON g.school = s.scode
WHERE g.mark = 100;
```

`DISTINCT` is needed if the requested answer is a set of cities: multiple qualifying graduates or schools may otherwise repeat a city.

### Schools with no student who graduated with 100

A direct translation using `NOT IN` is:

```sql
SELECT s.scode
FROM School AS s
WHERE s.scode NOT IN (
    SELECT g.school
    FROM Graduated AS g
    WHERE g.mark = 100
);
```

However, `NOT IN` has a subtle interaction with `NULL`. If the subquery can return `NULL`, the predicate may become `UNKNOWN` for every candidate. A robust formulation is:

```sql
SELECT s.scode
FROM School AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM Graduated AS g
    WHERE g.school = s.scode
      AND g.mark = 100
);
```

The correlated subquery asks whether a forbidden witness exists for the current school. `NOT EXISTS` keeps the school precisely when no such row exists.

### Cities where every school has a student who graduated with 100

This is the SQL version of double negation:

```sql
SELECT DISTINCT s.city
FROM School AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM School AS school_in_city
    WHERE school_in_city.city = s.city
      AND NOT EXISTS (
          SELECT 1
          FROM Graduated AS g
          WHERE g.school = school_in_city.scode
            AND g.mark = 100
      )
);
```

Read it from the inside out:

1. the innermost query looks for a mark-100 graduate in one school;
2. the first `NOT EXISTS` identifies a school without such a graduate;
3. the outer `NOT EXISTS` keeps cities having no bad school.

### Students with the minimum graduation mark in each school

Using a correlated aggregate subquery:

```sql
SELECT g1.school, g1.gcode
FROM Graduated AS g1
WHERE g1.mark = (
    SELECT MIN(g2.mark)
    FROM Graduated AS g2
    WHERE g2.school = g1.school
);
```

The inner query computes the minimum only among rows belonging to the current student's school. Equality with that minimum retains ties automatically.

---

## Aggregation operators

An aggregate function maps a set or multiset of input rows to a single value. Common aggregates include:

- `COUNT`;
- `MIN`;
- `MAX`;
- `AVG`;
- `SUM`.

A simplified syntax is:

```sql
aggregate_function([DISTINCT] expression)
```

Without `GROUP BY`, the filtered query result is treated as one group. With `GROUP BY`, the input is partitioned and the aggregate is computed independently for each group.

## `COUNT`

The three important forms are:

```sql
COUNT(*)
```

Counts rows, regardless of whether some columns are `NULL`.

```sql
COUNT(attribute)
```

Counts non-`NULL` values of the expression. Duplicates count separately.

```sql
COUNT(DISTINCT attribute)
```

Counts distinct non-`NULL` values.

Consider:

**Paternity**

| father | child |
|---|---|
| Sergio | Franco |
| Luigi | Olga |
| Luigi | Filippo |
| Franco | Andrea |
| Franco | Aldo |

To count Franco's children:

```sql
SELECT COUNT(*) AS num_children_of_franco
FROM Paternity
WHERE father = 'Franco';
```

The logical order is important: `WHERE` first retains Franco's two rows, and `COUNT(*)` then returns `2`.

### `COUNT` and `NULL`

Consider:

| name | age | income |
|---|---:|---:|
| Andrea | 27 | 21 |
| Aldo | 25 | `NULL` |
| Maria | 55 | 21 |
| Anna | 50 | 35 |

Then:

| Expression | Result | Reason |
|---|---:|---|
| `COUNT(*)` | 4 | Four rows exist |
| `COUNT(income)` | 3 | One income is `NULL` |
| `COUNT(DISTINCT income)` | 2 | The non-`NULL` values are 21 and 35 |

> [!important] A practical counting rule
> Use `COUNT(*)` to count rows. Use `COUNT(column)` only when you intentionally want to ignore rows where that expression is `NULL`.

## `SUM`, `AVG`, `MAX`, and `MIN`

These functions take an attribute or expression rather than `*`.

- `SUM` adds non-`NULL` input values.
- `AVG` computes the arithmetic mean of non-`NULL` values.
- `MAX` returns the greatest non-`NULL` value according to the domain's order.
- `MIN` returns the least non-`NULL` value.

Example: average income of Franco's children:

```sql
SELECT AVG(p.income) AS average_income
FROM Persons AS p
JOIN Paternity AS f
  ON p.name = f.child
WHERE f.father = 'Franco';
```

### Aggregation and `NULL`

For incomes `30, NULL, 36, 36`:

```sql
SELECT AVG(income)
FROM Persons;
```

returns:

$$
\frac{30+36+36}{3}=34
$$

The denominator is 3, not 4, because `AVG` ignores the `NULL` input.

If no non-`NULL` value exists, `SUM`, `AVG`, `MIN`, and `MAX` return `NULL`; `COUNT` returns `0`. This distinction is useful when handling empty groups or unmatched outer joins.

## Aggregation and the target list

The query:

```sql
SELECT name, MAX(income)
FROM Persons;
```

does not define which person's `name` should accompany the global maximum. There is one aggregate result but potentially many input names. In standards-conforming behavior, an ungrouped, non-aggregated column cannot simply be placed beside a global aggregate.

A homogeneous aggregate target list is meaningful:

```sql
SELECT MIN(age), AVG(income)
FROM Persons;
```

Both expressions return one value for the same global group.

> [!note] Finding the row associated with an extreme value
> `MAX(income)` returns the maximum value, not the entire row that contains it. To retrieve the corresponding person or people, use a subquery, join, or ranking window function.

---

## Aggregation and grouping

Without grouping, an aggregate is evaluated over all rows that survive `FROM` and `WHERE`. `GROUP BY` instead partitions those rows according to one or more grouping expressions:

```sql
GROUP BY attribute_list
```

### Number of children for each father

```sql
SELECT father, COUNT(*) AS num_children
FROM Paternity
GROUP BY father;
```

Result:

| father | num_children |
|---|---:|
| Sergio | 1 |
| Luigi | 2 |
| Franco | 2 |

Conceptually:

1. `FROM` and `WHERE` form the input rows.
2. Rows sharing the same grouping values are placed in one group.
3. Each aggregate is evaluated separately on each group.
4. The query emits one result row per group.

`GROUP BY` therefore changes the result's granularity. The input has one row per parent-child fact; the result has one row per father.

## Grouping exercise: maximum income by age

Find the maximum income for each age among people who are at least 18, and include the age:

```sql
SELECT age, MAX(income) AS maximum_income
FROM Persons
WHERE age >= 18
GROUP BY age;
```

`WHERE age >= 18` removes underage persons before groups are formed. Each remaining age becomes one group.

## Conditions on groups: `HAVING`

`WHERE` filters individual input rows. `HAVING` filters groups after grouping and aggregation.

Example: fathers whose children's average income exceeds 25:

```sql
SELECT f.father, AVG(p.income) AS average_income
FROM Persons AS p
JOIN Paternity AS f
  ON f.child = p.name
GROUP BY f.father
HAVING AVG(p.income) > 25;
```

The aggregate can appear in both the target list and the `HAVING` predicate because both refer to the current group.

### `WHERE` and `HAVING` together

Find fathers whose children younger than 30 have an average income greater than 20:

```sql
SELECT f.father, AVG(p.income) AS average_income
FROM Persons AS p
JOIN Paternity AS f
  ON f.child = p.name
WHERE p.age < 30
GROUP BY f.father
HAVING AVG(p.income) > 20;
```

The clauses answer two different questions:

- `WHERE p.age < 30`: which child rows are allowed to contribute to the group?
- `HAVING AVG(p.income) > 20`: which completed father groups are allowed in the output?

Moving the age condition to `HAVING` would either be invalid or change the meaning because `age` is not a group-level expression.

## Summary of `SELECT` syntax

A useful simplified grammar is:

```sql
SELECT      <attributes_or_expressions>
FROM        <tables>
[WHERE      <row_conditions>]
[GROUP BY   <grouping_expressions>]
[HAVING     <group_conditions>]
[ORDER BY   <sorting_expressions>]
[LIMIT      <number>];
```

The written order is not the conceptual evaluation order. A useful logical model is:

1. `FROM` and joins;
2. `WHERE`;
3. `GROUP BY`;
4. aggregate evaluation;
5. `HAVING`;
6. window functions;
7. `SELECT`;
8. duplicate elimination for `DISTINCT`;
9. `ORDER BY`;
10. `LIMIT`.

This model explains, for example, why a window function can operate on grouped query results but cannot usually be referenced directly in `WHERE` of the same query block.

## Grouping and a homogeneous target list

In a grouped query, each output expression must have one well-defined value per group. It should therefore be:

- a grouping expression;
- an aggregate expression;
- or an expression functionally determined in a way the DBMS recognizes.

This query is conceptually ambiguous:

```sql
SELECT age, income
FROM Persons
GROUP BY age;
```

There may be many incomes for one age. Which should be returned?

This query is well-defined:

```sql
SELECT age, AVG(income) AS average_income
FROM Persons
GROUP BY age;
```

There is exactly one average for each age group.

PostgreSQL normally rejects a selected non-aggregated column that is neither grouped nor accepted as functionally dependent on grouped columns. Some DBMSs or permissive configurations may choose an arbitrary value instead. Such behavior should not be relied upon: it is unclear to readers and may be non-deterministic.

---

## The notion of a window

A **window function** performs a calculation over rows related to the current result row while preserving that row in the output.

This is the defining difference:

| Aggregate query with `GROUP BY` | Window function |
|---|---|
| Collapses each group into one output row | Preserves the original row granularity |
| Changes what one result row represents | Adds an analytic value beside each row |
| Group membership is specified by `GROUP BY` | Related rows are specified inside `OVER(...)` |
| Useful for summaries | Useful for comparisons, rankings, running calculations, and annotated detail |

A useful mental translation is:

> For the current row, identify a related set of rows and compute a value over that set.

Common window-capable functions include:

- ranking functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`;
- aggregate functions used as windows: `SUM`, `AVG`, `MIN`, `MAX`, `COUNT`;
- navigation functions: `LAG`, `LEAD`;
- distribution functions, such as `PERCENT_RANK`, `CUME_DIST`, and `NTILE` in systems that support them.

## A first window-function example

Consider an employee table with one row per employee:

```sql
SELECT
    name,
    department_id,
    salary,
    SUM(salary) OVER (
        PARTITION BY department_id
    ) AS department_total
FROM Employee
ORDER BY department_id, name;
```

The keyword `OVER` turns `SUM(salary)` from a collapsing aggregate into a windowed aggregate. `PARTITION BY department_id` splits the result rows into disjoint partitions. Each employee receives the sum calculated over that employee's partition.

Using the example data:

| name | department_id | salary | department_total |
|---|---:|---:|---:|
| Newt | `NULL` | 75000 | 75000 |
| Dag | 10 | `NULL` | 370000 |
| Ed | 10 | 100000 | 370000 |
| Fred | 10 | 60000 | 370000 |
| Jon | 10 | 60000 | 370000 |
| Michael | 10 | 70000 | 370000 |
| Newt | 10 | 80000 | 370000 |
| Lebedev | 20 | 65000 | 130000 |
| Pete | 20 | 65000 | 130000 |
| Jeff | 30 | 300000 | 370000 |
| Will | 30 | 70000 | 370000 |

Notice that:

- every row remains present;
- the partition total repeats on each row of the partition;
- `SUM` ignores Dag's `NULL` salary;
- rows with `NULL department_id` form a partition together, just as `GROUP BY department_id` would group `NULL` keys together;
- two departments can have the same total without becoming the same partition.

### Why `GROUP BY` cannot return the same shape directly

The following query is invalid in a strict SQL system:

```sql
SELECT
    name,
    department_id,
    salary,
    SUM(salary) AS department_total
FROM Employee
GROUP BY department_id;
```

There is one output row per department but potentially many values of `name` and `salary`. Those detail columns are not well-defined at department granularity.

A valid grouped query must drop the detail columns:

```sql
SELECT
    department_id,
    SUM(salary) AS department_total
FROM Employee
GROUP BY department_id
ORDER BY department_id;
```

Result:

| department_id | department_total |
|---:|---:|
| `NULL` | 75000 |
| 10 | 370000 |
| 20 | 130000 |
| 30 | 370000 |

This result answers "what is each department total?" The window query answers "what is the department total associated with each employee?" The number is similar, but the output granularity and therefore the query's meaning are different.

---

## Components of a window function

The general shape is:

```sql
function(arguments) OVER (
    [PARTITION BY partition_expressions]
    [ORDER BY ordering_expressions]
    [ROWS | RANGE | GROUPS frame_clause]
)
```

### Function

The function determines the kind of value to compute: a sum, average, sequence number, rank, preceding value, and so on.

### `OVER(...)`

`OVER` marks the expression as a window function. An empty specification:

```sql
SUM(salary) OVER ()
```

uses all rows available to the current query block as one partition.

### `PARTITION BY`

`PARTITION BY` divides rows into independent groups for the window calculation. It is optional. If omitted, all rows form one partition.

```sql
SUM(salary) OVER (PARTITION BY department_id)
```

The result restarts independently for each department, but rows are not collapsed.

### Window `ORDER BY`

The `ORDER BY` inside `OVER` defines the logical sequence used by functions such as `ROW_NUMBER`, `LAG`, `LEAD`, and running aggregates:

```sql
ROW_NUMBER() OVER (
    PARTITION BY department_id
    ORDER BY salary DESC
)
```

This order is independent of the query's final presentation order. The outer `ORDER BY` controls how result rows are displayed:

```sql
SELECT ...
FROM ...
ORDER BY name;
```

The window can rank by salary while the final output is displayed alphabetically.

### Window frame

For many ordered aggregate windows, the frame identifies which rows around the current row contribute to the calculation. Common boundaries include:

- `UNBOUNDED PRECEDING`: the beginning of the partition;
- `n PRECEDING`: $n$ rows or value units before the current row;
- `CURRENT ROW`;
- `n FOLLOWING`;
- `UNBOUNDED FOLLOWING`: the end of the partition.

Example running total:

```sql
SUM(amount) OVER (
    PARTITION BY account_id
    ORDER BY transaction_time, transaction_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

Example moving average over the current and two preceding rows:

```sql
AVG(amount) OVER (
    PARTITION BY account_id
    ORDER BY transaction_time, transaction_id
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)
```

### `ROWS` versus `RANGE`

`ROWS` counts physical row positions in the window order. `RANGE` groups rows according to ordering values and treats rows with equal ordering values as peers when applying boundaries such as `CURRENT ROW`.

This difference matters when ties exist. For a predictable row-by-row running calculation, explicitly write a `ROWS` frame and use a deterministic ordering key.

> [!warning] Do not rely blindly on the default frame
> When a window contains `ORDER BY`, aggregate window functions often receive a default frame ending at the current row or its peer group. The exact consequence can be surprising with duplicate ordering values. Write the intended frame explicitly when correctness depends on it.

## Can the first window query be expressed without windows?

Yes. Window functions provide a direct analytic notation, but a partition total can be computed in a grouped subquery and joined back to the detail rows:

```sql
SELECT
    e.name,
    e.department_id,
    e.salary,
    d.department_total
FROM Employee AS e
JOIN (
    SELECT
        department_id,
        SUM(salary) AS department_total
    FROM Employee
    GROUP BY department_id
) AS d
  ON e.department_id IS NOT DISTINCT FROM d.department_id
ORDER BY e.department_id, e.name;
```

`IS NOT DISTINCT FROM` is PostgreSQL's null-safe equality: it allows the `NULL` department partition to match its grouped total. With an enforced `NOT NULL` department key, ordinary equality is sufficient.

A correlated subquery is another possibility:

```sql
SELECT
    e.name,
    e.department_id,
    e.salary,
    (
        SELECT SUM(e2.salary)
        FROM Employee AS e2
        WHERE e2.department_id IS NOT DISTINCT FROM e.department_id
    ) AS department_total
FROM Employee AS e;
```

The window version is shorter, expresses the analytic intent directly, and allows several related calculations to share one partitioning and ordering scheme. The alternatives are still useful because they reveal what the window calculation means: compute a group-level value and attach it to every matching detail row.

---

## `ROW_NUMBER()`

`ROW_NUMBER()` assigns the integers `1, 2, 3, ...` to rows in the window order, independently inside each partition.

```sql
SELECT
    employee_id,
    department,
    salary,
    ROW_NUMBER() OVER (
        PARTITION BY department
        ORDER BY salary DESC, employee_id
    ) AS row_num
FROM Employees;
```

Interpretation:

1. split employees by department;
2. within each department, order salaries from highest to lowest;
3. use `employee_id` to break salary ties deterministically;
4. number the ordered rows;
5. restart from 1 in the next department.

### Why a tie-breaker matters

If the window order is only `ORDER BY salary DESC`, equal salaries may be returned in either order. `ROW_NUMBER()` must still give them different numbers, but which tied employee gets the smaller number is not logically determined. Adding a stable unique key makes the result reproducible.

### Typical uses

- select one representative row per group;
- return the top $N$ rows per group;
- deduplicate records according to an explicit preference;
- create stable row positions for pagination when the ordering is deterministic.

Example: top two salaries per department:

```sql
WITH ranked AS (
    SELECT
        e.*,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC, employee_id
        ) AS rn
    FROM Employees AS e
)
SELECT *
FROM ranked
WHERE rn <= 2;
```

The extra query level is needed because window functions are evaluated after `WHERE` in the same query block.

---

## `RANK()` and `DENSE_RANK()`

Both functions assign the same rank to peers - rows tied on all window `ORDER BY` expressions. They differ in the number assigned after a tie.

```sql
SELECT
    employee_id,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS salary_rank,
    DENSE_RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS dense_salary_rank
FROM Employees;
```

Example:

| Employee | Department | Salary | `ROW_NUMBER()` | `RANK()` | `DENSE_RANK()` |
|---|---|---:|---:|---:|---:|
| A | HR | 5000 | 1 | 1 | 1 |
| B | HR | 5000 | 2 | 1 | 1 |
| C | HR | 4500 | 3 | 3 | 2 |
| D | HR | 4000 | 4 | 4 | 3 |

The key distinction is:

- `ROW_NUMBER`: every row gets a unique position; ties are not preserved as equal positions;
- `RANK`: tied rows share a rank, and later ranks contain gaps;
- `DENSE_RANK`: tied rows share a rank, and later ranks do not contain gaps.

### Choosing the correct ranking function

- Use `ROW_NUMBER` when you need exactly one row at each position.
- Use `RANK` for competition-style ranking: two people tied for first imply that the next person is third.
- Use `DENSE_RANK` when you want consecutive levels of distinct values: the second distinct salary receives rank 2.

> [!warning] Tie-breaking changes peer groups
> If `employee_id` is added to the `ORDER BY` of `RANK()` or `DENSE_RANK()`, rows with equal salaries are no longer peers because their full ordering keys differ. Use a tie-breaker for `ROW_NUMBER`, but include it in a rank only if you intentionally want to break the tie.

---

## `SUM()` with `OVER(...)`

An aggregate function becomes a windowed aggregate when followed by `OVER`. It computes an aggregate value without collapsing the detail rows.

### Partition total

```sql
SELECT
    employee_id,
    department,
    salary,
    SUM(salary) OVER (
        PARTITION BY department
    ) AS total_salary
FROM Employees;
```

Each employee receives the total salary of their department.

### Grand total

```sql
SUM(salary) OVER () AS company_total_salary
```

No `PARTITION BY` means that all available rows form one partition.

### Percentage of the department total

```sql
salary * 100.0
    / NULLIF(
        SUM(salary) OVER (PARTITION BY department),
        0
      ) AS department_salary_percentage
```

`NULLIF(..., 0)` prevents division by zero.

### Running total

```sql
SUM(salary) OVER (
    PARTITION BY department
    ORDER BY hire_date, employee_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_salary
```

Here, `ORDER BY` and the frame change the meaning. The function no longer returns the full partition total on every row; it returns the total from the beginning of the partition through the current row.

> [!important] Same function, different windows
> `SUM(x) OVER ()`, `SUM(x) OVER (PARTITION BY g)`, and `SUM(x) OVER (PARTITION BY g ORDER BY t ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` answer three different questions: grand total, group total, and group running total.

---

## `LAG()` and `LEAD()`

`LAG` accesses a value from a preceding row in the window order. `LEAD` accesses a value from a following row.

```sql
SELECT
    employee_id,
    department,
    salary,
    LAG(salary) OVER (
        PARTITION BY department
        ORDER BY salary, employee_id
    ) AS previous_salary,
    LEAD(salary) OVER (
        PARTITION BY department
        ORDER BY salary, employee_id
    ) AS next_salary
FROM Employees;
```

Inside each department:

- the first ordered row has no preceding row, so `LAG` returns `NULL` by default;
- the last ordered row has no following row, so `LEAD` returns `NULL` by default;
- the calculation restarts at each partition boundary.

### Offsets and defaults

The general forms are:

```sql
LAG(expression, offset, default) OVER (...)
LEAD(expression, offset, default) OVER (...)
```

For example:

```sql
LAG(salary, 2, 0) OVER (...)
```

looks two rows backward and returns `0` if no such row exists.

### Comparing consecutive observations

For a salary history table:

```sql
SELECT
    employee_id,
    effective_date,
    salary,
    salary - LAG(salary) OVER (
        PARTITION BY employee_id
        ORDER BY effective_date
    ) AS salary_change
FROM SalaryHistory;
```

For each employee, this subtracts the previous recorded salary from the current one. The same pattern applies to prices, monthly sales, sensor readings, balances, and event timestamps.

> [!note] `LAG` and frame clauses
> Navigation functions use the partition ordering to locate another row. In PostgreSQL, `LAG` and `LEAD` are based on partition position rather than the aggregate window frame. The ordering is therefore essential; the frame is usually relevant to aggregate windows such as running sums and moving averages.

---

## Practical use cases for window functions

### Pagination

`ROW_NUMBER()` can assign stable positions to an ordered result. For user-facing pagination, the ordering must be unique and stable; otherwise records may move between pages. Keyset pagination can be preferable for large, frequently changing datasets.

### Ranking

`RANK()` and `DENSE_RANK()` can rank employees by salary, customers by revenue, products by sales, or teams by score while explicitly controlling how ties are treated.

### Previous and next observations

`LAG()` and `LEAD()` compare consecutive purchases, measurements, states, or events without a self-join.

### Running totals and moving statistics

Windowed `SUM`, `AVG`, `MIN`, and `MAX` can calculate cumulative totals, moving averages, rolling minima, and other time-oriented statistics.

### Percentile and distribution analysis

Functions such as `PERCENT_RANK`, `CUME_DIST`, `NTILE`, and ordered-set aggregates can locate a row within a distribution. Their exact availability and syntax depend on the DBMS.

### Top-N per group

Rank rows inside each category and filter the rank from an outer query. This is a common reporting task that is awkward with a single ordinary `GROUP BY`.

### Deduplication

Assign `ROW_NUMBER()` within a duplicate key, ordering by data quality or recency, then retain `rn = 1`. This makes the choice of surviving record explicit.

---

## Final synthesis

Window functions enable analytical calculations while retaining row-level detail. The decisive concept is not the function name by itself, but the complete window specification:

```sql
function(...) OVER (
    PARTITION BY ...
    ORDER BY ...
    ROWS BETWEEN ... AND ...
)
```

Ask four questions whenever you read or design one:

1. **What does one output row represent?** The original employee, transaction, or observation should normally remain visible.
2. **Which rows belong to the same partition?** If `PARTITION BY` is absent, the whole input is one partition.
3. **In what logical order are rows processed?** This determines ranking, navigation, and running calculations.
4. **Which part of the ordered partition is in the frame?** This is crucial for rolling and cumulative aggregates.

### Compact comparison

| Goal | Appropriate construct |
|---|---|
| One summary row per department | `GROUP BY department` |
| Department total beside every employee | `SUM(salary) OVER (PARTITION BY department)` |
| Unique position within a department | `ROW_NUMBER()` |
| Competition ranking with gaps after ties | `RANK()` |
| Ranking distinct values without gaps | `DENSE_RANK()` |
| Previous or next observation | `LAG()` / `LEAD()` |
| Cumulative value | Ordered aggregate window with an explicit frame |

### Mental model

```text
GROUP BY: many input rows -> one output row per group
WINDOW:   many related rows -> one analytic value attached to each current row
```

The broader progression of the material is now visible:

1. The relational model defines data as relations.
2. Relational algebra defines operations that transform relations.
3. SQL provides a practical language whose core can be understood through those operations.
4. Aggregates summarize sets of rows.
5. `GROUP BY` changes result granularity by producing one row per group.
6. Window functions reuse group-like and order-aware calculations without sacrificing the granularity of the current result.

> [!success] Core takeaway
> Use `GROUP BY` when the group itself should become the output row. Use a window function when the original row should remain the output row but needs information derived from related rows.
