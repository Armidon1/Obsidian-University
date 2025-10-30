### **Numeri Coprime (o Relativamente Primi)**

> Due numeri interi ( a ) e ( b ) si dicono **coprime** se **non hanno altri divisori comuni oltre a 1**.

---

**Caratteristiche principali:**

- Il massimo comune divisore (GCD) è 1:  $$\text{GCD}(a, b) = 1  $$
- Non è necessario che siano primi tra loro; devono solo **non avere fattori comuni**.
    

---

**Esempi:**

1. ( 8 ) e ( 15 ) → GCD(8,15) = 1 → coprime
    
2. ( 14 ) e ( 25 ) → GCD(14,25) = 1 → coprime
    
3. ( 12 ) e ( 18 ) → GCD(12,18) = 6 → **non coprime**
    

---

**Uso in crittografia (RSA):**

- Nella generazione di chiavi RSA:
    
    - Si sceglie ( e ) tale che sia **copr[]()ime con ((p-1)(q-1))**, dove ( p ) e ( q ) sono primi scelti per il modulo ( $n = p \cdot q$).
        
    - Questo garantisce che **esista un inverso moltiplicativo modulo ((p-1)(q-1))**, necessario per calcolare la chiave privata ( d ).
        

---

**In breve:**

> **Numeri coprime** = due numeri che **non condividono fattori primi**, cioè il loro **GCD = 1**.  
> Fondamentali in crittografia e aritmetica modulare.