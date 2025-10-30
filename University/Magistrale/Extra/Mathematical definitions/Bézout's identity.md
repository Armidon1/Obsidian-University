# **Bézout's Identity (Identità di Bézout)**

> È un principio di **aritmetica modulare e teoria dei numeri** che afferma:

> Se ( a ) e ( b ) sono due numeri interi non entrambi zero, esistono **interi ( x ) e ( y )** tali che:  $$a \cdot x + b \cdot y = \gcd(a, b)  $$

---

**Caratteristiche principali:**

- ( $\gcd(a, b)$ ) = massimo comune divisore di ( a ) e ( b ).
    
- Gli interi ( x ) e ( y ) sono chiamati **coefficienti di Bézout**.
    
- Se ($\gcd(a, b) = 1$ ) → ( a ) e ( b ) sono **[[Coprime]]**, e allora esistono ( x, y ) tali che:  $$a \cdot x + b \cdot y = 1  $$    

---

**Esempio pratico:**

- ( a = 12, b = 5 )
- GCD(12,5) = 1 → [[Coprime]]
- Esistono ( x = -2, y = 5 ) perché:  $$12 \cdot (-2) + 5 \cdot 5 = -24 + 25 = 1  $$
---

**Uso in crittografia ([[RSA]], aritmetica modulare):**

- Bézout's Identity garantisce che, se ( e ) è **[[Coprime]] con ((p-1)(q-1))**, allora esiste un **inverso moltiplicativo modulo ((p-1)(q-1))**, cioè la chiave privata ( d ):  $$d \cdot e \equiv 1 \pmod{(p-1)(q-1)}  $$
---

**In breve:**

> **Bézout's Identity** = dati due numeri interi ( a ) e ( b ), esistono interi ( x, y ) tali che  
> ( $a \cdot x + b \cdot y = \gcd(a,b)$ ).  
> Fondamentale per **aritmetica modulare e calcolo inversi in [[RSA]]**.