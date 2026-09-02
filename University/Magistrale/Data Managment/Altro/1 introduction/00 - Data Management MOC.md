---
title: "Data Management MOC"
aliases: ["Data Management Map of Content"]
tags: [data-management, moc]
source: "[[1-Introduction.pdf]]"
---

# Data Management - Map of Content

> [!abstract]
> This map follows the conceptual progression from the relational model to relational algebra, SQL, aggregation, and window functions. Use it as the entry point for the atomic notes.

## Foundations

1. [[Relational Data Model]]
2. [[Relational Algebra]]
3. [[Relational Calculus]]
4. [[Codd's Theorem]]
5. [[Set Semantics vs Bag Semantics]]

## Relational algebra operators

6. [[Selection in Relational Algebra]]
7. [[Projection in Relational Algebra]]
8. [[Cartesian Product]]
9. [[Union in Relational Algebra]]
10. [[Difference in Relational Algebra]]
11. [[Intersection in Relational Algebra]]
12. [[Theta Join]]
13. [[Equijoin]]
14. [[Natural Join]]
15. [[Derived Operators in Relational Algebra]]

## Query patterns

16. [[Existential Queries in Databases]]
17. [[Queries Expressing Absence]]
18. [[Universal Quantification in Databases]]
19. [[Finding Minimum or Maximum Rows per Group]]
20. [[Renaming in Relational Algebra]]

## SQL core

21. [[SQL and Relational Algebra Correspondence]]
22. [[Logical Order of SQL Query Evaluation]]
23. [[SQL Aliases and Attribute Qualification]]
24. [[NULL and Three-Valued Logic]]

## Aggregation and grouping

25. [[SQL Aggregate Functions]]
26. [[COUNT in SQL]]
27. [[NULL and Aggregate Functions]]
28. [[GROUP BY]]
29. [[Homogeneous Target List]]
30. [[WHERE vs HAVING]]
31. [[SQL Query Granularity]]

## Window functions

32. [[SQL Window Functions]]
33. [[GROUP BY vs Window Functions]]
34. [[OVER Clause]]
35. [[PARTITION BY]]
36. [[Window ORDER BY]]
37. [[Window Frames]]
38. [[ROWS vs RANGE]]
39. [[ROW_NUMBER]]
40. [[RANK vs DENSE_RANK vs ROW_NUMBER]]
41. [[Aggregate Window Functions]]
42. [[LAG and LEAD]]
43. [[Running Totals]]
44. [[Moving Averages]]
45. [[Top-N per Group]]

## Suggested learning paths

### Formal foundations

[[Relational Data Model]] -> [[Relational Algebra]] -> [[Relational Calculus]] -> [[Codd's Theorem]]

### From algebra to SQL

[[Selection in Relational Algebra]] -> [[Projection in Relational Algebra]] -> [[Theta Join]] -> [[SQL and Relational Algebra Correspondence]]

### Negation and difficult queries

[[Difference in Relational Algebra]] -> [[Queries Expressing Absence]] -> [[Universal Quantification in Databases]]

### Aggregation

[[SQL Aggregate Functions]] -> [[GROUP BY]] -> [[WHERE vs HAVING]] -> [[SQL Query Granularity]]

### Window functions

[[SQL Window Functions]] -> [[OVER Clause]] -> [[PARTITION BY]] -> [[Window ORDER BY]] -> [[Window Frames]]

### Ranking and time-oriented analysis

[[ROW_NUMBER]] -> [[RANK vs DENSE_RANK vs ROW_NUMBER]] -> [[LAG and LEAD]] -> [[Running Totals]] -> [[Moving Averages]]

