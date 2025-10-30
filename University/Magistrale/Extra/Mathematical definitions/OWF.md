# **One-Way Function (Funzione a Senso Unico)**

> Una **one-way function** è una funzione matematica che è **facile da calcolare in un verso**, ma **difficile da invertire**.

In altre parole:    
$$f(x) \text{ è facile da calcolare, ma dato } y = f(x), \text{ è computazionalmente difficile trovare } x.  $$

---

### 🔹 **Proprietà principali:**

1. **Facilità di calcolo:**  
    Per un qualsiasi input ( x ), ( f(x) ) si calcola in tempo polinomiale.
    
2. **Difficoltà di inversione:**  
    Non esiste un algoritmo efficiente per trovare ( x ) dato ( f(x) ) (a meno di forza bruta).
    

---

### 🔸 **Esempi di one-way functions (concettuali):**

- **Hash crittografici** come SHA-256  
    [  
    f(x) = \text{SHA-256}(x)  
    ]  
    Facile da calcolare, ma impossibile (praticamente) invertire.
    
- **Moltiplicazione di grandi numeri primi:**  
    [  
    f(p, q) = p \cdot q  
    ]  
    Facile moltiplicare, difficile fattorizzare → base della sicurezza **RSA**.
    

---

### 🔐 **Importanza in crittografia:**

Le one-way functions sono **fondamentali** perché sono alla base di molti meccanismi di sicurezza:

- **Hashing** (integrità dei dati)
    
- **Digital signatures**
    
- **Password storage**
    
- **Key derivation functions**
    
- **Public key cryptography**
    

---

### 🧠 **Formalmente:**

Una funzione ( f: X \rightarrow Y ) è _one-way_ se:

1. ( f ) è computabile in tempo polinomiale.
    
2. Per quasi tutti gli ( y \in Y ), è computazionalmente **infeasible** trovare un ( x \in X ) tale che ( f(x) = y ).
    

---

### **In breve:**

> Una **one-way function** è una funzione “facile da calcolare ma difficile da invertire”.  
> È il **pilastro matematico della crittografia moderna**, su cui si basano hash, firme digitali e cifrature asimmetriche.