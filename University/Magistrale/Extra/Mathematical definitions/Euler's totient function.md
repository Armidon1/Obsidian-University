**Euler’s Totient Function (Funzione Totiente di Eulero)**

> La **funzione totiente di Eulero**, indicata con ( $\varphi(n)$), conta **quanti numeri interi positivi minori di ( n )** sono **coprimi con ( n )** (cioè hanno $GCD = 1$ con ( n )).

---

### 🔹 **Definizione formale:**  
$$\varphi(n) = |{ k \in \mathbb{N} \mid 1 \leq k \leq n, \ \gcd(k, n) = 1 }|  $$

---

### 🔸 **Esempi:**

- $( n = 1 ) → ( \varphi(1) = 1 )$
    
- ( n = 5 ) → numeri coprimi con 5: {1, 2, 3, 4} → $( \varphi(5) = 4 )$
    
- ( n = 8 ) → coprimi con 8: {1, 3, 5, 7} → $( \varphi(8) = 4 )$
    

---

### 🔹 **Formula generale:**

Se ( n ) ha la **fattorizzazione in primi**:  
  
$n = p_1^{a_1} \cdot p_2^{a_2} \cdot \ldots \cdot p_k^{a_k}$


allora:  

$\varphi(n) = n \cdot \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right)$  


---

### 🔸 **Casi particolari:**

- Se ( n = p ) (numero primo) →  $\varphi(p) = p - 1$
    (perché tutti i numeri da 1 a ( p-1 ) sono coprimi con ( p ))
    
- Se $( n = p \cdot q )$ (prodotti di due primi distinti): $\varphi(n) = (p - 1)(q - 1)$
    

---

### 🔐 **Uso in crittografia (RSA):**

- Nell’algoritmo **[[RSA]]**, si sceglie ( $n = p \cdot q$), dove ( p ) e ( q ) sono primi.
    
- Si calcola $( \varphi(n) = (p - 1)(q - 1) )$.
    
- La chiave pubblica ( e ) deve essere **coprima con ($\varphi(n)$ )**.
    
- La chiave privata ( d ) è l’inverso moltiplicativo di ( e ) modulo ($\varphi(n)$ ):  
    $e \cdot d \equiv 1 \pmod{\varphi(n)}$
    

---

### **In breve:**

> **Euler’s totient function** ( $\varphi(n)$ ) = numero di interi < ( n ) che sono coprimi con ( n ).  
> Fondamentale per la **teoria dei numeri** e la **sicurezza dell’[[RSA]]**, poiché determina la struttura dei numeri invertibili modulo ( n ).