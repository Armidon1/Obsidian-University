# **One-Way Function (Funzione a Senso Unico)**

> Una **one-way function** è una funzione matematica che è **facile da calcolare in un verso**, ma **difficile da invertire**.

In altre parole:    
$$f(x) \text{ è facile da calcolare, ma dato } y = f(x), \text{ è computazionalmente difficile trovare } x.  $$
![[Pasted image 20251023113341.png]]
---

### 🔹 **Proprietà principali:**

1. **Facilità di calcolo:**  
    Per un qualsiasi input ( x ), ( f(x) ) si calcola in tempo polinomiale.
    
2. **Difficoltà di inversione:**  
    Non esiste un algoritmo efficiente per trovare ( x ) dato ( f(x) ) (a meno di forza bruta).
    
---
Nel dettaglio
> [!One-Way Function]
> 
> A function $f: \{0,1\}^* \rightarrow \{0,1\}^*$ is called a one-way function ([[OWF]]) if it satisfies two properties:
> 
> 1. **Efficiently computable:**
>     
>     - There exists a deterministic polynomial-time algorithm (it's "easy" or "fast") that, given any input $x$, computes $f(x)$.
>         
> 2. **Hard to invert on average:**
>     
>     - For every probabilistic polynomial-time algorithm $A$ (an "attacker"), for every positive polynomial $p(\cdot)$, and for sufficiently large $n$:
>         
>         $$\Pr_{x \leftarrow \{0,1\}^n}[A(f(x)) \in f^{-1}(f(x))] < \frac{1}{p(n)}$$
>         
>     - In plain English: Any efficient (polynomial-time) attacker $A$, given an output $y = f(x)$ (where $x$ was chosen randomly), has only a negligible probability of finding _any_ valid input $x'$ that produces $y$.
>         

---

### 🔸 **Esempi di one-way functions (concettuali):**

- **Hash crittografici** come [[SHA-2]]56  $$f(x) = \text{SHA-256}(x)  $$
    Facile da calcolare, ma impossibile (praticamente) invertire.
    
- **Moltiplicazione di grandi numeri primi:**  $$f(p, q) = p \cdot q  $$
    Facile moltiplicare, difficile fattorizzare → base della sicurezza **[[RSA]]**.
    
---

vedi di più in [[7 CS  Lower Level - Asymmetric encryption#2. Candidate One-Way Functions]]

---

### 🔐 **Importanza in crittografia:**

Le one-way functions sono **fondamentali** perché sono alla base di molti meccanismi di sicurezza:

- **Hashing** (integrità dei dati)
    
- **Digital signatures**
    
- **Password storage**
    
- **Key derivation functions**
    
- **Public key cryptography**
    

---
