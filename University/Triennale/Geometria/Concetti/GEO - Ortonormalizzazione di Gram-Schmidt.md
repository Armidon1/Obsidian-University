---
title: "Ortonormalizzazione di Gram-Schmidt"
aliases:
  - "GEO — Ortonormalizzazione di Gram-Schmidt"
tags:
  - geometria
  - concetto
source: "pdf/Geometria.pdf"
---

# Ortonormalizzazione di Gram-Schmidt

> [!summary] In breve
> Gram-Schmidt trasforma una base in una base ortonormale dello stesso sottospazio, sottraendo a ogni vettore le componenti nelle direzioni già costruite.

$$u_k=v_k-\sum_{j<k}\frac{\langle v_k,u_j\rangle}{\langle u_j,u_j\rangle}u_j,\qquad q_k=\frac{u_k}{\|u_k\|}.$$

Si parte da $u_1=v_1$. L’indipendenza dei vettori iniziali garantisce che nessun $u_k$ sia nullo. Normalizzare senza aver prima ortogonalizzato non basta.

## Collegamenti

[[GEO - Prodotto scalare standard in Rn]] · [[GEO - Matrici ortogonali]]

[[MOC - Geometria]]

> [!info] Approfondimento
> [[38 - GEO - Prodotto scalare in Rn#38.2 - Basi ortonormali|Capitolo 38 — Basi ortonormali]]

_(Accascina–Monti, § 38.2, libro pp. 643–649; PDF pp. 659–665.)_
